"""Apply the reviewed, user-authorized 111-ID backfill. Dry run unless --apply.

One-shot migration, deliberately refusing to overwrite an existing destination.
The frozen scoring and cut receipts remain unchanged; manifest.json is an overlay.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote
from types import SimpleNamespace
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from markdown_math import expressions, validate_math
from catalogue import STATUS_DISPLAY, validate_page

DATE = "2026-10-30"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe(path):
    path = (ROOT / path).resolve()
    if not path.is_relative_to(ROOT) or path == ROOT or path.is_symlink():
        raise ValueError(f"Unsafe workspace path: {path}")
    return path


def dump(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def relative(path, parent):
    return Path(os.path.relpath(path, parent)).as_posix()


def slug(title):
    plain = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")[:100].rstrip("-")


def protect_math(text):
    found, errors = expressions(text)
    if errors:
        raise ValueError(errors)
    for expression in reversed(found):
        tex = expression.tex.strip().replace(r"\operatorname", r"\mathrm")
        replacement = ("\x60\x60\x60math\n" + tex + "\n\x60\x60\x60\n"
                       if expression.display else "$\x60" + tex + "\x60$")
        text = text[:expression.start] + replacement + text[expression.end:]
    if errors := validate_math(text):
        raise ValueError(errors)
    return text


LINK = re.compile(r"(\]\()([^\s)]+)(\))")


def rebase(text, old, new, moves):
    def replace(match):
        target = match[2]
        if "://" in target or target.startswith(("#", "mailto:")):
            return match[0]
        pathname, separator, fragment = target.partition("#")
        resolved = (old.parent / unquote(pathname)).resolve()
        destination = moves.get(resolved, resolved)
        target = relative(destination, new.parent) + (separator + fragment if separator else "")
        return match[1] + target + match[3]
    return LINK.sub(replace, text)


def canonical_page(record, review, moves):
    old = safe(record["source_path"])
    text = old.read_text(encoding="utf-8")
    title = text.splitlines()[0].removeprefix("# ").strip()
    title = {"518": "Whitney extension with a 2^D test threshold and single-exponential loss",
             "621": "Does the standard Nelder–Mead method always converge on x²+y²?"}.get(record["new_aim_id"], title)
    area_match = re.search(r"^\*\*Area:\*\*\s*(.+)$", text, re.MULTILINE)
    category_areas = {"continuum2": "Dynamical systems; piecewise-affine flows",
                      "pdes-materials": "Partial differential equations and regularity",
                      "probability-statistics": "Probability and statistics",
                      "numerical-analysis": "Numerical analysis; approximation and complexity",
                      "geometry-topology": "Geometry and topology",
                      "continuous-optimization": "Continuous optimization",
                      "optimization-information": "Optimization and information",
                      "spectral": "Spectral theory and mathematical physics",
                      "inverse": "Inverse problems and imaging"}
    area = (area_match[1].strip().rstrip(".") if area_match
            else category_areas[record["source_category"]])
    area = protect_math(area)
    new = safe(f"problems/{record['new_aim_id']}-{slug(title)}.md")
    record.update(new_path=relative(new, ROOT), current_title=title)
    row = dict(id=record["new_aim_id"], title=title, area=area, file=record["new_path"],
               status=review["main_status"], last_checked=DATE, source_key=record["source_key"])
    # The mathematical body is preserved; headers and math markup follow AIM's format.
    body = text[text.index("\n## ") + 1:]
    body = re.sub(r"^## Application and known (?:progress|cases)\s*$", "## Application", body, flags=re.MULTILINE)
    body = re.sub(r"^## References and (?:checked version|known progress)\s*$", "## References", body, flags=re.MULTILINE)
    body = rebase(body, old, new, moves)
    if record["new_aim_id"] == "284":
        body = body.replace("Alberto Beretta", "Guglielmo Beretta")
    if review["main_status"] == "Partially resolved":
        match = re.search(r"^## Status review\s*\n", body, re.MULTILINE)
        assert match
        status_body = body[match.end():]
        insert = ""
        if not re.search(r"^\*\*Known cases:\*\*", status_body, re.MULTILINE):
            insert += "\n**Known cases:** " + review["review_note"] + "\n"
        if not re.search(r"^\*\*Remaining target:\*\*", status_body, re.MULTILINE):
            insert += ("\n**Remaining target:** Resolve the complete question stated under Problem statement, "
                       "with all its quantifiers and hypotheses. The restricted results described here "
                       "do not cover that full target.\n")
        body = body[:match.end()] + insert + "\n" + status_body.lstrip()
    # Current evidence is separate from the preserved, dated original status discussion.
    sources = "; ".join(f"[status source {i}]({url})" for i, url in enumerate(review["sources_consulted"], 1))
    fresh = ("\n\n### Online recheck, " + DATE + "\n\n" + review["review_note"] + "\n\n"
             + "Comparators and current-status sources: " + sources + ". "
             "This bounded search found no matching complete proof, counterexample or complete-solution "
             "announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.\n")
    match = re.search(r"^## Status review[^\n]*\n(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL)
    assert match
    body = body[:match.end()] + fresh + "\n" + body[match.end():]
    provenance = ("\n## Collection provenance\n\nPromoted from retained further problem **" + record["source_key"]
                  + "** on " + DATE + ", with its editorial scores unchanged. The [replacement register]"
                  "(../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity "
                  "for this reused number and the historical research path. Earlier dated AIM-number "
                  "comparisons above describe the collection at that earlier date.\n")
    content = (f"# {row['id']}. {title}\n\n**Area:** {area}\n"
               f"**Status:** {STATUS_DISPLAY[row['status']]}\n**Last checked:** {DATE}\n\n" + body.rstrip() + "\n" + provenance)
    return row, protect_math(content)


def build():
    plan = read_json(HERE / "review_plan.json")
    checks = read_json(HERE / "checked_candidates.json")
    scores = read_json(ROOT / "PROBLEM_SCORING/scores.json")
    score_index = {r["key"]: r for r in scores["records"]}
    catalogue = read_json(ROOT / "catalogue.json")
    cuts = {r["id"]: r for r in catalogue["cut"]}
    records = plan["records"]
    assert len(records) == 111 == plan["required_promotions"]
    assert {r["new_aim_id"] for r in records} == set(cuts)
    assert len({r["source_key"] for r in records}) == 111
    assert set(checks["reviews"]) == set(cuts)
    assert not (HERE / "manifest.json").exists(), "This migration has already been applied"
    groups = {r["key"] for r in catalogue["groups"]}
    metadata = {g: read_json(ROOT / f"data/{g}.json") for g in groups}
    active_ids = {r["id"] for rows in metadata.values() for r in rows}
    retired_ids = {r["id"] for r in catalogue["retired"]}
    assert len(active_ids) == 545 and len(retired_ids) == 9
    assert not (active_ids | retired_ids) & set(cuts)
    moves = {}
    for record in records:
        source = safe(record["source_path"])
        assert source.is_file() and digest(source.read_bytes()) == record["source_sha256"]
        profile = score_index[record["source_key"]]
        assert profile["selection_decision"] == "keep" and profile["importance"] >= 6
        assert profile["current_source_path"] == record["source_path"]
        assert record["scores"] == profile["scores"]
        assert cuts[record["new_aim_id"]]["group"] == record["target_group"]
        review = checks["reviews"][record["new_aim_id"]]
        assert review["review_state"] == "passed_bounded_online_recheck" and review["checked_on"] == DATE
        assert review["sources_consulted"] and review["search_batches"]
        record.update(review)
        # First pass allocates paths; second pass can rebase links between promoted pages.
        row, _ = canonical_page(record, review, {})
        target = safe(row["file"])
        assert not target.exists()
        moves[source] = target
    assert len(set(moves.values())) == 111
    writes = {}
    for record in records:
        row, content = canonical_page(record, checks["reviews"][record["new_aim_id"]], moves)
        path = safe(row["file"])
        assert not validate_math(content)
        page_errors = validate_page(row, SimpleNamespace(read_text=lambda **kwargs: content))
        assert not page_errors, page_errors
        for section in ("Problem statement", "Application", "References", "Status review"):
            assert re.search(r"^## " + section + r"\s*$", content, re.MULTILINE), (row["id"], section)
        record["destination_sha256"] = digest(content.encode("utf-8"))
        record["archived_predecessor"] = cuts[row["id"]]["record"]
        metadata[record["target_group"]].append(row)
        cuts[row["id"]]["replacement"] = dict(file=row["file"], source_key=record["source_key"],
                                                 group=record["target_group"], filled_on=DATE)
        profile = score_index[record["source_key"]]
        profile.update(current_source_path=row["file"], current_source_sha256=record["destination_sha256"],
                       current_aim_id=row["id"], current_subject_group=record["target_group"],
                       current_mathematical_status=row["status"], promoted_on=DATE)
        writes[path] = content.encode("utf-8")
    all_entries = [row for rows in metadata.values() for row in rows]
    assert len(all_entries) == 656
    assert len({row["id"] for row in all_entries}) == 656
    assert len({row["title"] for row in all_entries}) == 656
    assert {row["id"] for row in all_entries} | retired_ids == {f"{i:03d}" for i in range(1, 666)}
    # Only live human-facing backlink pages are changed. Historical research ledgers stay frozen.
    backlink_changes = []
    live_pages = [p for folder in ("FURTHER_problems", "cut_problems/FURTHER_problems")
                  for p in safe(folder).glob("*/lead-*.md") if not p.parent.name.startswith("_")]
    for path in live_pages:
        if path in moves:
            continue
        before = path.read_bytes()
        after = rebase(before.decode("utf-8"), path, path, moves).encode("utf-8")
        # rebase also normalizes unrelated paths; avoid incidental changes to them.
        if any(Path(r["source_path"]).name in before.decode("utf-8") for r in records) and after != before:
            writes[path] = after
            backlink_changes.append(dict(path=relative(path, ROOT), sha256_before=digest(before), sha256_after=digest(after)))
            for profile in scores["records"]:
                if profile["current_source_path"] == relative(path, ROOT):
                    profile["current_source_sha256"] = digest(after)
    # Keep matching fresh announcements visible on the three unpromoted candidates.
    for record in plan["excluded_candidates"]:
        path = safe(record["source_path"])
        before = path.read_bytes()
        assert digest(before) == record["source_sha256"]
        text = before.decode("utf-8")
        text = re.sub(r"^\*\*Status:\*\*.*$", "**Status:** Complete solution announced; excluded from open-problem promotion pending proof review", text, flags=re.MULTILINE)
        text = re.sub(r"^\*\*Last checked:\*\*.*$", "**Last checked:** " + DATE, text, flags=re.MULTILINE)
        links = "; ".join(f"[announcement {i}]({url})" for i, url in enumerate(record["sources_consulted"], 1))
        text += "\n## Promotion recheck, " + DATE + "\n\n" + record["review_note"] + "\n\n" + links + ". The earlier open-status discussion is historical.\n"
        after = text.encode("utf-8")
        writes[path] = after
        record["current_sha256"] = digest(after)
        score_index[record["source_key"]].update(current_source_sha256=digest(after), current_mathematical_status="Solution claimed")
    scores["selection"]["current_locations"] = dict(aim=665, further=410, cut=321, retained_total=1075)
    scores["selection"]["promotion_manifest"] = relative(HERE / "manifest.json", ROOT)
    writes[ROOT / "PROBLEM_SCORING/scores.json"] = dump(scores)
    writes[ROOT / "catalogue.json"] = dump(catalogue)
    for group, rows in metadata.items():
        if any(r["target_group"] == group for r in records):
            writes[ROOT / f"data/{group}.json"] = dump(sorted(rows, key=lambda r: int(r["id"])))
    view = ROOT / "PROBLEM_SCORING/FURTHER.md"
    text = view.read_text(encoding="utf-8")
    for record in records:
        text = text.replace("../" + record["source_path"], "../" + record["new_path"])
    text = text.replace("Each title links to its existing source page.",
                        "Each title links to its current source page. Original keys, scores and recorded statuses remain historical; 111 retained entries now have AIM IDs in the [replacement register](../research/catalogue-backfill-2026-10-30/README.md).")
    writes[view] = text.encode("utf-8")
    view = ROOT / "PROBLEM_SCORING/README.md"
    text = view.read_text(encoding="utf-8")
    marker = "## Scores and classification"
    text = text.replace(marker, "**ID backfill, 30 October 2026:** 111 retained further problems now occupy the vacated AIM IDs, after fresh bounded online status checks. Current locations are 665 AIM entries and 410 staged further problems; the 1,075 keep decisions and all scores are unchanged. See the [replacement register](../research/catalogue-backfill-2026-10-30/README.md).\n\n" + marker)
    writes[view] = text.encode("utf-8")
    view = ROOT / "cut_problems/README.md"
    text = view.read_text(encoding="utf-8")
    text = text.replace("The retained collection has **554 AIM entries and 521 further problems: 1,075 total**.",
                        "Immediately after the cut, the retained collection had **554 AIM entries and 521 further problems: 1,075 total**. A subsequent user-authorized backfill moved 111 retained further problems into the vacant AIM slots; the current distribution is **665 AIM entries and 410 further problems**, still 1,075 total.")
    text = text.replace("Original IDs must not be reused.",
                        "The subsequent explicit instruction authorized reuse of the 111 vacated AIM numbers. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) distinguishes each archived identity from its current replacement; use paths and stable scoring keys, not a bare number, to identify an archived problem. The PDF and frozen cut receipt describe the earlier cut and are preserved unchanged; their non-reuse policy is superseded by this instruction.")
    text = text.replace("The manifest maps original repository paths to current paths and records before/after hashes.",
                        "The frozen manifest records the cut's original moves and hashes. The subsequent [backfill overlay](../research/catalogue-backfill-2026-10-30/manifest.json) records promotions and later backlink-only changes; the verifier applies both in order.")
    writes[view] = text.encode("utf-8")
    notice = ("**ID backfill, 30 October 2026:** Of the 731 historical admissions, 521 meet I >= 6: "
              "111 are now AIM entries and **410 remain staged here**; 210 are archived. Before duplicate "
              "checks or interpreting an old path as missing work, apply the [cut manifest](../cut_problems/move_manifest.json) "
              "and [promotion overlay](../research/catalogue-backfill-2026-10-30/manifest.json), or use the "
              "[path resolver](../cut_problems/verify_cut.py). Historical ledgers, coverage records and paused "
              "research cursors are unchanged. No research jobs were resumed.\n\n")
    view = ROOT / "FURTHER_problems/README.md"
    writes[view] = ("# Further-problem collection\n\n" + notice +
                    "The keep rule is **I = max(M, A) >= 6**, applied to the frozen [score snapshot](../cut_problems/_audit/score_snapshot.json).\n\n"
                    "See [the replacement register](../research/catalogue-backfill-2026-10-30/README.md), "
                    "[resume handoff](RESUME.md), [workflow](WORKFLOW.md) and [source log](SOURCE_LOG.md).\n").encode("utf-8")
    for name in ("WORKFLOW.md", "RESUME.md"):
        view = ROOT / "FURTHER_problems" / name
        text = view.read_text(encoding="utf-8")
        text = re.sub(r"\*\*Editorial selection applied, 30 October 2026:\*\*.*?\n\n", notice, text, count=1, flags=re.DOTALL)
        writes[view] = text.encode("utf-8")
    selection = ROOT / "cut_problems/selection.csv"
    reader = csv.DictReader(io.StringIO(selection.read_text(encoding="utf-8-sig")))
    fields = reader.fieldnames
    rows = list(reader)
    for row in rows:
        row["current_source_path"] = score_index[row["key"]]["current_source_path"]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    writes[selection] = output.getvalue().encode("utf-8-sig")
    manifest = dict(schema="AIM_REUSED_ID_BACKFILL_V1", date=DATE, state="applied",
                    authorization="Reuse only the 111 user-authorized vacant AIM IDs, within corresponding subject groups.",
                    selection=plan["selection"], review_scope=checks["scope"],
                    counts=dict(promoted=111, current_problem_pages=656, retained_resolved_records=9,
                                current_aim=665, still_staged=410, cut=321, retained_total=1075),
                    records=records, excluded_candidates=plan["excluded_candidates"],
                    backlink_changes=backlink_changes,
                    historical_cut_receipt="cut_problems/move_manifest.json",
                    original_pages_zip=relative(HERE / "before/original_pages.zip", ROOT),
                    checks="checked_candidates.json", searches="online_searches.json")
    writes[HERE / "review_plan.json"] = dump(plan)
    writes[HERE / "manifest.json"] = dump(manifest)
    group_counts = {}
    for r in records:
        group_counts[r["target_group"]] = group_counts.get(r["target_group"], 0) + 1
    lines = ["# Reusing the 111 vacant AIM IDs", "", "Applied 30 October 2026 under the user's explicit instruction. Exactly **111 retained further problems** fill the 111 archived AIM slots, preserving each slot's subject group. Current AIM identities cover **001–665 without gaps**: 656 current pages plus nine retained resolved records. **410 further problems remain staged**. The 1,075 keep decisions and editorial scores are unchanged.", "",
             "The old problems and their solution packages remain in cut_problems. A reused number identifies a new problem: historical cut entries must be identified by archived path and original scoring key. Publication batches retain their historical number allocation; this register records the replacement date and provenance.", "",
             "## Selection and current-status checks", "", plan["selection"] if isinstance(plan["selection"], str) else json.dumps(plan["selection"], ensure_ascii=False), "",
             "Subject matching is at the level of the existing AIM groups, including their stated multi-topic scope. Within the eligible category pool, the saved plan ranks by importance I, conceptual interest C, explanatory value E, then stable key. Three candidates with matching complete announcements were skipped; the next eligible retained problems were used. No scores were changed and no additional IDs were allocated.", "", checks["scope"], "",
             "The [checks](checked_candidates.json) preserve each final status, hypothesis comparison, source URLs and search-batch references; the [raw search log](online_searches.json) preserves 38 fresh query batches. Primary comparison sources also include the retained original references. Searches cannot certify the absence of every recent result. Partial advances are labeled Partially resolved, with known cases and the full remaining target retained on the page.", "",
             "The [manifest](manifest.json) records original lead paths/hashes, new paths/hashes, stable keys, old AIM identities, exclusions and backlink changes. Original promoted pages and modified metadata are preserved under before/. The frozen scoring/cut receipts and paused coverage database were not rewritten. The [path resolver](../../cut_problems/verify_cut.py) applies the cut receipt and this overlay in sequence.", "",
             "## Candidates excluded after fresh checks", ""]
    for r in plan["excluded_candidates"]:
        urls = "; ".join(f"[announcement {i}]({u})" for i, u in enumerate(r["sources_consulted"], 1))
        lines += [f"- **{r['source_key']}**: {r['review_note']} {urls}. Retained in staging with an announcement warning, pending proof review."]
    lines += ["", "## Subject allocation", "", "| AIM subject group | Promoted |", "| --- | ---: |"]
    lines += [f"| {g} | {n} |" for g, n in sorted(group_counts.items())]
    lines += ["", "## Historical and current identities", "", "| ID | Archived former problem | Current AIM problem | Stable further key |", "| --- | --- | --- | --- |"]
    for r in sorted(records, key=lambda r: int(r["new_aim_id"])):
        lines.append(f"| {r['new_aim_id']} | [{r['former_aim_title']}](../../{r['archived_predecessor']}) | [{r['current_title']}](../../{r['new_path']}) | {r['source_key']} |")
    writes[HERE / "README.md"] = ("\n".join(lines) + "\n").encode("utf-8")
    assert len(moves) == 111
    for path in writes:
        safe(path)
    # Check all links in the new AIM pages against the planned post-migration tree.
    for record in records:
        path = safe(record["new_path"])
        for match in LINK.finditer(writes[path].decode("utf-8")):
            target = match[2]
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            resolved = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            assert (resolved in writes or (resolved.exists() and resolved not in moves)), (path, target)
    return plan, moves, writes, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    plan, moves, writes, manifest = build()
    print(json.dumps(dict(preflight="PASS", promotions=len(moves), writes=len(writes),
                          counts=manifest["counts"], backlink_changes=len(manifest["backlink_changes"]))))
    if not args.apply:
        return
    before = safe(HERE / "before")
    before.mkdir(exist_ok=True)
    # Store exact original bytes before any mutation, including original further pages.
    originals = set(moves) | {p for p in writes if p.exists()}
    receipt = []
    with zipfile.ZipFile(before / "original_pages.zip", "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(originals):
            data = path.read_bytes()
            name = relative(path, ROOT)
            archive.writestr(name, data)
            receipt.append(dict(path=name, sha256=digest(data), size=len(data)))
    (before / "receipt.json").write_bytes(dump(receipt))
    for source, destination in moves.items():
        # Both absolute paths were checked to be contained in the workspace; no overwrites.
        assert source.is_relative_to(ROOT) and destination.is_relative_to(ROOT)
        assert source.is_file() and not destination.exists()
        source.rename(destination)
    for path, content in writes.items():
        safe(path).write_bytes(content)
    print("Applied exactly 111 promotions; frozen cut receipts and original score fields preserved.")


if __name__ == "__main__":
    main()

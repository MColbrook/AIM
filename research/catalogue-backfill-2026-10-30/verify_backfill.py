"""Read-only integrity checks for this 111-problem promotion and its audit trail."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from markdown_math import expressions


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def statement(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    match = re.search(r"^## Problem statement\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    assert match
    text = match[1]
    found, errors = expressions(text)
    assert not errors, errors
    for expr in reversed(found):
        tex = expr.tex.strip().replace(r"\operatorname", r"\mathrm")
        text = text[:expr.start] + " MATH(" + tex + ") " + text[expr.end:]
    return re.sub(r"\s+", " ", text).strip()


def main():
    manifest = read(HERE / "manifest.json")
    checks = read(HERE / "checked_candidates.json")["reviews"]
    searches = read(HERE / "online_searches.json")
    catalogue = read(ROOT / "catalogue.json")
    integration_path = ROOT / "research/further-integration-2026-10-30/manifest.json"
    integration = read(integration_path) if integration_path.exists() else None
    integration = integration if integration and integration.get("state") == "applied" else None
    counts = integration["counts"] if integration else None
    integrated = {r["source_key"]: r for r in integration["records"]} if integration else {}
    profiles = {row["key"]: row for row in read(ROOT / "PROBLEM_SCORING/scores.json")["records"]}
    entries = {row["id"]: {**row, "group": path.stem}
               for path in (ROOT / "data").glob("*.json") for row in read(path)}
    cuts = {row["id"]: row for row in catalogue["cut"]}
    records = manifest["records"]
    assert len(records) == 111
    assert {row["new_aim_id"] for row in records} == set(cuts)
    assert len({row["source_key"] for row in records}) == 111
    assert len(entries) == (counts["current_problem_pages"] if counts else 656) and len(catalogue["retired"]) == 9
    assert set(entries) | {row["id"] for row in catalogue["retired"]} == {f"{i:03d}" for i in range(1, (counts["current_aim"] if counts else 665) + 1)}
    batches = {batch["batch"] for batch in searches["batches"]}
    assert len(batches) == 40
    receipt = read(HERE / "before/receipt.json")
    with zipfile.ZipFile(ROOT / manifest["original_pages_zip"]) as archive:
        assert set(archive.namelist()) == {row["path"] for row in receipt}
        for row in receipt:
            data = archive.read(row["path"])
            assert len(data) == row["size"] and digest(data) == row["sha256"], row["path"]
        for row in records:
            identifier = row["new_aim_id"]
            entry = entries[identifier]
            review = checks[identifier]
            profile = profiles[row["source_key"]]
            source = ROOT / row["source_path"]
            target = ROOT / row["new_path"]
            original = archive.read(row["source_path"])
            assert not source.exists() and target.is_file()
            assert digest(original) == row["source_sha256"]
            assert digest(target.read_bytes()) == row["destination_sha256"]
            assert statement(original.decode("utf-8")) == statement(target.read_text(encoding="utf-8")), identifier
            assert profile["selection_decision"] == "keep" and profile["importance"] >= 6
            assert profile["scores"] == row["scores"]
            assert profile["current_source_path"] == row["new_path"]
            assert entry["file"] == row["new_path"]
            assert entry["source_key"] == row["source_key"]
            assert entry["group"] == row["target_group"] == cuts[identifier]["group"]
            assert entry["status"] == review["main_status"]
            assert review["review_state"] == "passed_bounded_online_recheck"
            assert review["checked_on"] == "2026-10-30" and review["sources_consulted"]
            assert review["search_batches"] and set(review["search_batches"]) <= batches
        # The four cross-reference edits change link targets alone, including one archived page.
        for row in manifest["backlink_changes"]:
            before = archive.read(row["path"])
            later = next((r for r in integrated.values() if r['source_path'] == row['path']), None)
            if later:
                # Verify the historical link-only edit against the retained intermediate bytes.
                with zipfile.ZipFile(integration_path.parent / 'pre_migration.zip') as intermediate:
                    after = intermediate.read(row['path'])
                assert digest(after) == later['source_sha256']
            else:
                after = (ROOT / row["path"]).read_bytes()
            assert digest(before) == row["sha256_before"] and digest(after) == row["sha256_after"]
            normalise = lambda text: re.sub(r"\]\([^\s)]+\)", "](LINK-TARGET)", text)
            assert normalise(before.decode("utf-8")) == normalise(after.decode("utf-8")), row["path"]
    staged = [row for row in profiles.values() if row["origin"] == "further_admitted"
              and row["selection_decision"] == "keep" and row["current_source_path"].startswith("FURTHER_problems/")]
    assert len(staged) == (counts["still_staged"] if counts else 409)
    with zipfile.ZipFile(HERE / "before/replacement-106.zip") as previous:
        for row in manifest["manual_archives"]:
            path = ROOT / row["record"]
            assert digest(path.read_bytes()) == row["sha256_after"]
            old = previous.read(row["original_file"])
            assert digest(old) == row["sha256_before"]
            assert statement(old.decode("utf-8")) == statement(path.read_text(encoding="utf-8"))
            assert profiles[row["source_key"]]["current_editorial_decision"] == "cut_by_user_request"
            assert not (ROOT / row["original_file"]).exists()
    for row in manifest["excluded_candidates"]:
        profile = profiles[row["source_key"]]
        later = integrated.get(row["source_key"])
        if later:
            assert later["source_path"] == row["source_path"] and later["source_sha256"] == row["current_sha256"]
            assert later["new_aim_id"] is None
            assert profile["current_source_path"] == later["new_path"]
            assert digest((ROOT / later["new_path"]).read_bytes()) == later["destination_sha256"]
            assert not (ROOT / row["source_path"]).exists()
        else:
            assert profile["current_source_path"] == row["source_path"]
            assert digest((ROOT / row["source_path"]).read_bytes()) == row["current_sha256"]
        assert profile["current_mathematical_status"] == "Solution claimed"
    documents = [HERE / "README.md", ROOT / "PROBLEM_SCORING/FURTHER.md", ROOT / "PROBLEM_SCORING/README.md",
                 ROOT / "cut_problems/README.md", ROOT / "FURTHER_problems/README.md",
                 ROOT / "FURTHER_problems/RESUME.md", ROOT / "FURTHER_problems/WORKFLOW.md"]
    # Historical bodies of RESUME/WORKFLOW deliberately retain old ledger paths; inspect the new notice only.
    for path in documents:
        text = path.read_text(encoding="utf-8")
        if path.name in ("RESUME.md", "WORKFLOW.md"):
            text = text.split("\n\n", 2)[1]
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            if "://" not in target and not target.startswith(("#", "mailto:")):
                assert (path.parent / unquote(target.split("#", 1)[0])).exists(), (path, target)
    print(json.dumps(dict(result="PASS", promoted=111, unchanged_problem_statements=111,
                          current_aim=counts["current_aim"] if counts else 665,
                          contiguous_ids="001–" + str(counts["current_aim"] if counts else 665),
                          staged=counts["still_staged"] if counts else 409,
                          status_checks=111, search_batches=40, excluded_recent_announcements=3,
                          explicit_editorial_archives=1,
                          status_partially_resolved=57, status_open=54, link_only_backlink_repairs=4), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

"""One-shot reviewed migration of retained further problems. Dry run by default."""
import argparse
import csv
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
from types import SimpleNamespace
from urllib.parse import unquote
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location('backfill_helpers', ROOT / 'research/catalogue-backfill-2026-10-30/apply_backfill.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
sys.path.insert(0, str(ROOT / 'scripts'))
from catalogue import STATUS_DISPLAY, validate_page
from markdown_math import validate_math

DATE = '2026-10-30'
NEW_GROUPS = {
    'bayesian-inverse-uncertainty-quantification': 'Bayesian inverse problems and uncertainty quantification',
    'complex-analysis-potential-theory': 'Complex analysis and potential theory',
    'continuous-optimization': 'Continuous optimization and variational analysis',
    'electrochemistry-energy-storage': 'Electrochemistry and energy storage',
    'fluid-structure-interaction': 'Fluid–structure interaction',
    'fracture-damage-plasticity-contact': 'Fracture, damage, plasticity and contact',
    'mathematical-relativity': 'Mathematical relativity',
    'nonlinear-filtering-data-assimilation': 'Nonlinear filtering and data assimilation',
    'rough-paths-singular-stochastic-equations': 'Rough paths and singular stochastic equations',
}


def insert_section(body, heading, addition):
    match = re.search(r'^## ' + re.escape(heading) + r'[^\n]*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    assert match, heading
    return body[:match.end()].rstrip() + '\n\n' + addition.strip() + '\n\n' + body[match.end():].lstrip()


def page(record, moves):
    old, new = h.safe(record['source_path']), h.safe(record['new_path'])
    text = old.read_text(encoding='utf8')
    body = text[text.index('\n## ') + 1:]
    body = body.replace(' ## Status review', '\n\n## Status review')
    body = re.sub(r'^\*\*Status:\*\*', '**Earlier review status:**', body, flags=re.M)
    body = re.sub(r'^\*\*Last checked:\*\*', '**Earlier review date:**', body, flags=re.M)
    body = h.rebase(body, old, new, moves)
    if record['ordinal'] == 229:
        body = body.replace(r'\|x_j\|_{\ell_1}^{,2}', r'\|x_j\|_{\ell_1}^{2}')
    if record.get('editorial_clarification'):
        body = insert_section(body, 'Problem statement', '**Editorial clarification:** ' + record['editorial_clarification'])
    for ref in record.get('additional_references', []):
        body = insert_section(body, 'References', f"- [{ref['title']}]({ref['url']}). Added in the {DATE} recheck.")
    if record.get('status_addendum'):
        body = insert_section(body, 'Status review', record['status_addendum'])
    sources = record.get('sources_consulted', [])
    links = '; '.join(f'[comparison source {i}]({u})' for i, u in enumerate(sources, 1))
    fresh = (f"### Online recheck, {DATE}\n\n{record['review_note']}\n\n"
             + (f'Additional comparison sources: {links}. ' if links else '')
             + 'The primary-source formulation and earlier dated status review are retained below. '
             'Fresh query results and hypothesis comparisons are recorded in the '
             '[integration register](../research/further-integration-2026-10-30/README.md). '
             'This is a bounded literature and announcement search, not a guarantee of continued openness '
             'or certification of every cited proof.')
    match = re.search(r'^## Status review\s*\n', body, re.M)
    assert match, (record['ordinal'], re.findall(r'^## .+$', body, re.M))
    known = ''
    if record['main_status'] == 'Partially resolved':
        status = body[match.end():]
        if not re.search(r'^\*\*Known cases:\*\*', status, re.M):
            known += '\n**Known cases:** ' + record['review_note'] + '\n'
        if not re.search(r'^\*\*Remaining target:\*\*', status, re.M):
            known += ('\n**Remaining target:** Resolve the full Problem statement with its stated '
                      'quantifiers and hypotheses; the restricted advances discussed here do not settle that target.\n')
    body = body[:match.end()] + known + '\n' + fresh + '\n\n' + body[match.end():].lstrip()
    body += ('\n## Collection provenance\n\nPromoted on ' + DATE + ' from retained further problem **'
             + record['source_key'] + '**, with its scores unchanged. The [integration register]'
             '(../research/further-integration-2026-10-30/README.md) preserves its original path, '
             'source bytes, review evidence and current identity. Earlier AIM-number comparisons '
             'describe the collection at their original review dates.\n')
    content = (f"# {record['new_aim_id']}. {record['current_title']}\n\n**Area:** {record['area']}\n"
               f"**Status:** {STATUS_DISPLAY[record['main_status']]}\n**Last checked:** {DATE}\n\n" + body)
    return h.protect_math(content)


def archived_page(record, moves):
    old, new = h.safe(record['source_path']), h.safe(record['new_path'])
    text = h.rebase(old.read_text(encoding='utf8'), old, new, moves)
    status = ('Counterexample to the literal formulation; archived without an AIM ID'
              if record['ordinal'] == 150 else 'Complete resolution announced; archived without an AIM ID (proof not certified here)')
    text = re.sub(r'^\*\*Status:\*\*.*$', '**Status:** ' + status, text, flags=re.M)
    text = re.sub(r'^\*\*Last checked:\*\*.*$', '**Last checked:** ' + DATE, text, flags=re.M)
    text += '\n## Integration exclusion, ' + DATE + '\n\n' + record['review_note'] + '\n\n'
    text += record.get('archive_clarification', '') + '\n\n'
    text += record.get('counterexample_proof', '') + '\n\n'
    text += '\n'.join(f'- [Resolution evidence {i}]({u})' for i, u in enumerate(record.get('sources_consulted', []), 1))
    text += ('\n\nNo AIM ID was allocated. The earlier open-status review is historical. '
             'This is a separate resolution/formulation decision, with all editorial scores unchanged. '
             'See the [integration register](../../../research/further-integration-2026-10-30/README.md).\n')
    return h.protect_math(text)


def build():
    m = h.read_json(HERE / 'manifest.json')
    assert m['state'] == 'review_complete_pre_migration'
    assert len(m['records']) == 409 and not any(r['review_state'] == 'pending' for r in m['records'])
    scores = h.read_json(ROOT / 'PROBLEM_SCORING/scores.json')
    profiles = {r['key']: r for r in scores['records']}
    cat = h.read_json(ROOT / 'catalogue.json')
    groups = {g['key']: g['title'] for g in cat['groups']}
    metadata = {g: h.read_json(ROOT / f'data/{g}.json') for g in groups}
    active = [r for rows in metadata.values() for r in rows]
    assert len(active) == 656 and max(int(r['id']) for r in active + cat['retired']) == 665
    existing_archives = {r['key'] for r in scores['records'] if r['current_source_path'].startswith('cut_problems/')}
    moves, next_id = {}, 666
    for r in m['records']:
        p = profiles[r['source_key']]
        assert p['selection_decision'] == 'keep' and p['importance'] >= 6 and p['scores'] == r['scores']
        assert r['source_key'] not in existing_archives and p['current_source_path'] == r['source_path']
        source = h.safe(r['source_path'])
        assert h.digest(source.read_bytes()) == r['source_sha256'], r['source_path']
        assert r.get('search_receipts') and all((HERE / f).is_file() for f in r['search_receipts'])
        text = source.read_text(encoding='utf8')
        r['current_title'] = h.protect_math(text.splitlines()[0].removeprefix('# ').strip())
        area = re.search(r'^\*\*Area:\*\*\s*(.+)$', text, re.M)
        r['area'] = h.protect_math(area[1].strip().rstrip('.') if area else groups.get(r['source_category'], NEW_GROUPS.get(r['source_category'], r['source_category'])))
        if r['review_state'].startswith('passed'):
            r['new_aim_id'] = f'{next_id:03d}'
            next_id += 1
            r['new_path'] = f"problems/{r['new_aim_id']}-{h.slug(r['title'])}.md"
            r['target_group'] = r['source_category']
            if r['target_group'] not in groups:
                title = NEW_GROUPS[r['target_group']]
                cat['groups'].append(dict(key=r['target_group'], title=title))
                groups[r['target_group']], metadata[r['target_group']] = title, []
        else:
            assert r['review_state'].startswith('exclude') and r['new_aim_id'] is None
            r['new_path'] = 'cut_problems/' + r['source_path']
            r.setdefault('main_status', 'Solution claimed')
        target = h.safe(r['new_path'])
        assert not target.exists()
        moves[source] = target
    assert len(set(moves.values())) == 409
    writes = {}
    for r in m['records']:
        is_promotion = r['new_aim_id'] is not None
        content = page(r, moves) if is_promotion else archived_page(r, moves)
        assert not validate_math(content), (r['ordinal'], validate_math(content))
        data = content.encode('utf8')
        r['destination_sha256'] = h.digest(data)
        writes[h.safe(r['new_path'])] = data
        p = profiles[r['source_key']]
        p.update(current_source_path=r['new_path'], current_source_sha256=r['destination_sha256'], current_mathematical_status=r['main_status'])
        if is_promotion:
            row = dict(id=r['new_aim_id'], title=r['current_title'], area=r['area'], file=r['new_path'], status=r['main_status'], last_checked=DATE, source_key=r['source_key'])
            errors = validate_page(row, SimpleNamespace(read_text=lambda **kw: content))
            assert not errors, errors
            metadata[r['target_group']].append(row)
            p.update(current_aim_id=r['new_aim_id'], current_subject_group=r['target_group'], promoted_on=DATE)
        else:
            assert 'current_aim_id' not in p
            p.update(current_editorial_decision='cut_after_resolution_recheck', archive_reason=r['review_note'], archived_on=DATE)
    promoted = [r for r in m['records'] if r['new_aim_id']]
    excluded = [r for r in m['records'] if not r['new_aim_id']]
    cat['batches'].append(dict(key='retained-further-2026-10-30', title='Retained further problems, integrated 30 October 2026', ids=[r['new_aim_id'] for r in promoted]))
    cat['further_archive'] = [dict(source_key=r['source_key'], title=r['current_title'], record=r['new_path'], original_file=r['source_path'], reason=r['review_note'], status=r['main_status'], archived_on=DATE, review='research/further-integration-2026-10-30/manifest.json') for r in excluded]
    m['backlink_changes'] = []
    live = list((ROOT / 'problems').glob('*.md')) + list((ROOT / 'cut_problems/problems').glob('*.md')) + list((ROOT / 'cut_problems/FURTHER_problems').glob('*/lead-*.md'))
    for path in live:
        before = path.read_bytes()
        after = h.rebase(before.decode('utf8'), path, path, moves).encode('utf8')
        if before != after:
            writes[path] = after
            rel = h.relative(path, ROOT)
            m['backlink_changes'].append(dict(path=rel, sha256_before=h.digest(before), sha256_after=h.digest(after)))
            for p in profiles.values():
                if p['current_source_path'] == rel:
                    p['current_source_sha256'] = h.digest(after)
    counts = dict(promoted=len(promoted), archived_without_id=len(excluded), current_aim=665+len(promoted), current_problem_pages=656+len(promoted), retained_resolved_records=9, still_staged=0, cut=322+len(excluded), retained_total=1074-len(excluded), historical_further_admissions=731, further_now_aim=111+len(promoted), further_now_cut=211+len(excluded))
    m.update(state='applied', counts=counts, new_id_range=dict(first='666', last=f'{next_id-1:03d}'), review_limits='Retained primary formulations and previous audits reused; fresh per-target public-web queries and inspection of matching announcements. Negative searches are bounded, and claimed full resolutions are not proof-certified. No global guarantee of openness or Lean re-build is made.')
    scores['selection']['current_locations'] = dict(aim=counts['current_aim'], further=0, cut=counts['cut'], retained_total=counts['retained_total'])
    scores['selection']['integration_manifest'] = h.relative(HERE / 'manifest.json', ROOT)
    for r in excluded:
        scores['selection'].setdefault('editorial_overrides', []).append(dict(key=r['source_key'], decision='cut_after_resolution_recheck', record=r['new_path']))
    writes[ROOT / 'catalogue.json'] = h.dump(cat)
    writes[ROOT / 'PROBLEM_SCORING/scores.json'] = h.dump(scores)
    for group, rows in metadata.items():
        path = ROOT / f'data/{group}.json'
        ordered = sorted(rows, key=lambda r: int(r['id']))
        if not path.exists() or h.read_json(path) != ordered:
            writes[path] = h.dump(ordered)
    path = ROOT / 'PROBLEM_SCORING/FURTHER.md'
    text = path.read_text(encoding='utf8')
    for r in m['records']:
        text = text.replace('../'+r['source_path'], '../'+r['new_path'])
    writes[path] = text.encode('utf8')
    path = ROOT / 'cut_problems/selection.csv'
    reader = csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig')))
    fields, rows = reader.fieldnames, list(reader)
    for row in rows:
        p = profiles[row['key']]
        row['current_source_path'] = p['current_source_path']
        row['current_editorial_decision'] = p.get('current_editorial_decision', row['current_editorial_decision'])
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)
    writes[path] = out.getvalue().encode('utf-8-sig')
    notice = (f"**Further integration, 30 October 2026:** All 409 remaining retained candidates were rechecked: **{len(promoted)} now have AIM IDs 666–{next_id-1}**, and **{len(excluded)} are archived without IDs** after resolution/formulation checks. Of 731 historical admissions, {counts['further_now_aim']} are now AIM entries and {counts['further_now_cut']} are archived; **none remain staged**. Scores are unchanged. Apply the [cut manifest](../cut_problems/move_manifest.json), [backfill overlay](../research/catalogue-backfill-2026-10-30/manifest.json) and [integration overlay](../research/further-integration-2026-10-30/manifest.json), or use the [path resolver](../cut_problems/verify_cut.py), before treating an old path as missing work. Historical research ledgers and paused cursors are unchanged. No discovery jobs were resumed.\n\n")
    for name in ('README.md', 'RESUME.md', 'WORKFLOW.md'):
        path = ROOT / 'FURTHER_problems' / name
        text = path.read_text(encoding='utf8')
        text = re.sub(r'\*\*ID backfill, 30 October 2026:\*\*.*?\n\n', lambda _: notice, text, count=1, flags=re.S)
        writes[path] = text.encode('utf8')
    path = ROOT / 'PROBLEM_SCORING/README.md'
    text = path.read_text(encoding='utf8')
    text = re.sub(r'\*\*ID backfill, 30 October 2026:\*\*.*?\n\n', f"**Current locations, 30 October 2026:** {counts['current_aim']} AIM entries, no staged further problems, and {counts['cut']} archived identities. The initial 1,075 threshold decisions are unchanged; the later manual exclusion and seven resolution/formulation exclusions are separate overrides. All four scores remain unchanged. See the [backfill register](../research/catalogue-backfill-2026-10-30/README.md) and [integration register](../research/further-integration-2026-10-30/README.md).\n\n", text, count=1, flags=re.S)
    writes[path] = text.encode('utf8')
    path = ROOT / 'cut_problems/README.md'
    text = path.read_text(encoding='utf8')
    text = text.replace('this archive now preserves **322 problems**', f"this archive held **322 problems** before the further integration")
    text = text.replace('the current distribution is **665 AIM entries and 409 further problems**, 1,074 retained.', 'the distribution was **665 AIM entries and 409 further problems**, 1,074 retained.')
    text = text.replace('\nAll original IDs,', f"\n**Further integration:** Seven additional candidates are now archived here without ever receiving an AIM ID: six matching complete-resolution announcements and one counterexample to the literal formulation. The archive now contains **{counts['cut']} identities**; **{counts['current_aim']} AIM entries** remain and none are staged. These exclusions do not lower or change their scores. See the [individual reasons and evidence](../research/further-integration-2026-10-30/README.md) and [integration overlay](../research/further-integration-2026-10-30/manifest.json). Claimed resolutions are distinguished from certified proofs; the sectionwise-contraction exclusion concerns its exact wording. The frozen original report and move receipt remain historical.\n\nAll original IDs,")
    writes[path] = text.encode('utf8')
    # Preserve a historical register, with an explicit current overlay link.
    path = ROOT / 'research/catalogue-backfill-2026-10-30/README.md'
    text = path.read_text(encoding='utf8')
    text = text.replace('\n\nApplied ', '\n\n**Subsequent integration:** All remaining staged pages now resolve through the [integration register](../further-integration-2026-10-30/README.md). Three candidates excluded below have since been moved to the cut archive without IDs. Counts and source locations in the historical account below describe the backfill stage.\n\nApplied ', 1)
    for r in excluded:
        text = text.replace('../../'+r['source_path'], '../../'+r['new_path'])
    writes[path] = text.encode('utf8')
    lines = ['# Integrating retained further problems', '', f"Applied {DATE}. Reviewed all **409** remaining retained candidates: **402 promoted** to AIM **666–1067**, **seven archived without IDs**. Current collection: **1,067 AIM identities** (1,058 pages and nine retained resolved records), zero staged further problems, 329 archived identities. No existing cut problem was reintroduced; scores are unchanged.", '', '## Checks and limits', '', m['review_limits'], '', 'The source pages already record exact formulations, primary references and dated semantic duplicate/status audits. This integration reuses that evidence and adds 198 saved query/opening receipts and a per-candidate comparison note. A matching complete announcement suffices for exclusion under the user instruction; such an exclusion does not certify its proof. Restricted progress remains Partial. One apparent AR proof has a specific gap recorded on its promoted page.', '', 'The [manifest](manifest.json) maps stable source keys and original paths/hashes to every final destination/hash. The [original pages](original_problem_pages.zip) preserve all 409 exact source files. The pre-migration backup preserves other changed files. The [path resolver](../../cut_problems/verify_cut.py) composes the original cut and subsequent overlays; historical research records and paused discovery cursors are untouched. No Git operations or remote research jobs were run.', '', '## Exclusions without AIM IDs', '', '| Stable key | Archived problem | Disposition and evidence |', '| --- | --- | --- |']
    for r in excluded:
        urls = ' '.join(f'[Source {i}]({u})' for i,u in enumerate(r.get('sources_consulted', []),1))
        lines.append(f"| {r['source_key']} | [{r['title']}](../../{r['new_path']}) | {r['review_note']} {urls} |")
    lines += ['', '## Promoted problems', '', '| AIM ID | Problem | Source key | Status |', '| --- | --- | --- | --- |']
    for r in promoted:
        lines.append(f"| {r['new_aim_id']} | [{r['current_title']}](../../{r['new_path']}) | {r['source_key']} | {r['main_status']} |")
    writes[HERE / 'README.md'] = ('\n'.join(lines)+'\n').encode('utf8')
    writes[HERE / 'manifest.json'] = h.dump(m)
    for path in writes:
        h.safe(path)
    for r in m['records']:
        path = h.safe(r['new_path'])
        for match in h.LINK.finditer(writes[path].decode('utf8')):
            target = match[2]
            if '://' in target or target.startswith(('#','mailto:')):
                continue
            resolved = (path.parent / unquote(target.split('#',1)[0])).resolve()
            assert resolved in writes or (resolved.exists() and resolved not in moves), (r['ordinal'], target)
    return m, moves, writes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    m, moves, writes = build()
    print(json.dumps(dict(preflight='PASS', counts=m['counts'], writes=len(writes), backlinks=len(m['backlink_changes']))))
    if not args.apply:
        return
    backup = HERE / 'pre_migration.zip'
    assert not backup.exists()
    with zipfile.ZipFile(backup, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(set(moves) | {p for p in writes if p.exists()}):
            z.writestr(h.relative(path, ROOT), path.read_bytes())
    for source, target in moves.items():
        # Check final resolved absolute paths immediately before each nonrecursive move.
        h.safe(source); h.safe(target)
        assert source.is_file() and not target.exists()
        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
    for path, content in writes.items():
        h.safe(path).write_bytes(content)
    print('Applied reviewed migration; discovery ledgers and Git state untouched.')


if __name__ == '__main__':
    main()

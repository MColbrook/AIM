"""Read-only verification of the reviewed 409-candidate integration and frozen scores."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from markdown_math import expressions, validate_math
from catalogue import load_manifest, load_entries, validate, next_problem_id


def read(path):
    return json.loads(path.read_text(encoding='utf8'))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def statement(text, ordinal):
    text = text.replace('\r\n', '\n')
    section = re.search(r'^## Problem statement\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    assert section
    text = re.sub(r'^\*\*Editorial clarification:\*\*.*$', '', section[1], flags=re.M)
    text = re.sub(r'\]\([^\s)]+\)', '](LINK)', text)
    if ordinal == 229:
        text = text.replace(r'\|x_j\|_{\ell_1}^{,2}', r'\|x_j\|_{\ell_1}^{2}')
    found, errors = expressions(text)
    assert not errors, errors
    for expr in reversed(found):
        text = text[:expr.start] + ' MATH(' + expr.tex.strip().replace(r'\operatorname', r'\mathrm') + ') ' + text[expr.end:]
    return re.sub(r'\s+', ' ', text).strip()


def main():
    m = read(HERE / 'manifest.json')
    assert m['state'] == 'applied'
    rows = m['records']
    promoted = [r for r in rows if r['new_aim_id']]
    excluded = [r for r in rows if not r['new_aim_id']]
    assert len(rows) == 409 and len(promoted) == 402 and len(excluded) == 7
    assert [int(r['new_aim_id']) for r in promoted] == list(range(666,1068))
    cat, errors = load_manifest()
    assert not errors, errors
    entries, errors = load_entries(cat)
    assert not errors, errors
    assert not validate(entries, cat, catalogue_only=True)
    assert len(entries) == 1058 and len(cat['retired']) == 9
    assert next_problem_id(cat) == 1068
    current = {r['source_key']:r for r in entries if 'source_key' in r}
    scores = read(ROOT / 'PROBLEM_SCORING/scores.json')
    profiles = {r['key']:r for r in scores['records']}
    with zipfile.ZipFile(HERE / 'original_problem_pages.zip') as originals, zipfile.ZipFile(HERE / 'pre_migration.zip') as backup:
        before = json.loads(backup.read('PROBLEM_SCORING/scores.json'))
        eligible = {r['key'] for r in before['records'] if r['selection_decision']=='keep' and r['current_source_path'].startswith('FURTHER_problems/')}
        assert eligible == {r['source_key'] for r in rows}
        assert set(originals.namelist()) == {r['source_path'] for r in rows}
        assert len(eligible) == 409
        for r in rows:
            old = originals.read(r['source_path'])
            assert old == backup.read(r['source_path'])
            assert digest(old) == r['source_sha256']
            assert not (ROOT / r['source_path']).exists()
            destination = ROOT / r['new_path']
            data = destination.read_bytes()
            assert digest(data) == r['destination_sha256']
            text = data.decode('utf8')
            assert not validate_math(text)
            assert statement(old.decode('utf8'), r['ordinal']) == statement(text,r['ordinal']), r['ordinal']
            assert r['checked_on'] == '2026-10-30' and r['review_note'] and r['search_receipts']
            for filename in r['search_receipts']:
                receipt = read(HERE / filename)
                assert receipt.get('result') or (filename == 'lefschetz-v2-primary.json' and receipt), filename
            p = profiles[r['source_key']]
            assert p['scores']==r['scores'] and p['importance']>=6 and p['selection_decision']=='keep'
            assert p['current_source_path']==r['new_path'] and p['current_source_sha256']==r['destination_sha256']
            if r['new_aim_id']:
                assert current[r['source_key']]['id']==r['new_aim_id']
                assert current[r['source_key']]['file']==r['new_path']
                assert r['review_state']=='passed_bounded_online_recheck'
                assert not r['new_path'].startswith('cut_problems/')
            else:
                assert r['review_state'].startswith('exclude') and r['source_key'] not in current
                assert 'current_aim_id' not in p
                assert r['new_path']=='cut_problems/'+r['source_path']
                assert 'No AIM ID was allocated' in text
            for target in re.findall(r'\]\(([^\s)]+)\)',text):
                if '://' not in target and not target.startswith(('#','mailto:')):
                    assert (destination.parent/unquote(target.split('#',1)[0])).exists(),(r['ordinal'],target)
        for r in m['backlink_changes']:
            old=backup.read(r['path']);new=(ROOT/r['path']).read_bytes()
            assert digest(old)==r['sha256_before'] and digest(new)==r['sha256_after']
            strip=lambda t:re.sub(r'\]\([^\s)]+\)','](LINK)',t)
            assert strip(old.decode('utf8'))==strip(new.decode('utf8'))
        oldcat=json.loads(backup.read('catalogue.json'))
        assert cat['retired']==oldcat['retired'] and cat['cut']==oldcat['cut'] and cat['editorial_archive']==oldcat['editorial_archive']
        assert cat['batches'][:-1]==oldcat['batches']
    snapshot=read(ROOT/'cut_problems/_audit/score_snapshot.json')
    for old in snapshot['records']:
        assert all(profiles[old['key']][field]==value for field,value in old.items()),old['key']
    assert len(profiles)==1396
    archive_keys={r['key'] for r in profiles.values() if r['current_source_path'].startswith('cut_problems/')}
    assert len(archive_keys)==329 and not archive_keys & set(current)
    assert sum(r['current_source_path'].startswith('FURTHER_problems/') for r in profiles.values())==0
    export=csv.DictReader(io.StringIO((ROOT/'cut_problems/selection.csv').read_text(encoding='utf-8-sig')))
    exported=list(export)
    assert len(exported)==1396
    for row in exported:
        assert row['current_source_path']==profiles[row['key']]['current_source_path']
    for name in ['README.md','PROBLEM_SCORING/README.md','PROBLEM_SCORING/FURTHER.md','cut_problems/README.md', 'research/further-integration-2026-10-30/README.md']:
        p=ROOT/name
        for target in re.findall(r'\]\(([^\s)]+)\)',p.read_text(encoding='utf8')):
            if '://' not in target and not target.startswith(('#','mailto:')):
                assert (p.parent/unquote(target.split('#',1)[0])).exists(),(name,target)
    print(json.dumps(dict(result='PASS',reviewed=409,promoted=402,archived_without_ids=7,problem_statements_preserved=409,explicit_math_typo_corrections=1,current_aim=1067,ids='001–1067',still_staged=0,archived_identities=329,original_score_profiles_unchanged=1396,link_only_repairs=len(m['backlink_changes']),query_receipts=len(list(HERE.glob('search-*.json')))),ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()

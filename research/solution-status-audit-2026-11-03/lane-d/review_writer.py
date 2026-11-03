import json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = pathlib.Path(__file__).resolve().parent
MANIFEST = json.loads((ROOT / 'research/solution-status-audit-2026-11-03/manifest.json').read_text(encoding='utf-8'))
TARGETS = MANIFEST['targets'][684:912]

def save(local_id, review):
    target = next(t for t in TARGETS if t['id'] == local_id)
    original = (ROOT / target['file']).read_text(encoding='utf-8')
    statement = original.split('## Problem statement', 1)[1].split('\n## ', 1)[0].strip()
    row = dict(schema='AIM_SOLUTION_STATUS_REVIEW_V1', localID=local_id,
               manifest_index=MANIFEST['targets'].index(target), checked_date='2026-11-03',
               source_sha256=target['source_sha256'], statement_sha256=target['statement_sha256'],
               original_target=target, full_original_statement=statement,
               full_original_page=original, scope='lane-d; canonical files untouched')
    row.update(review)
    (LANE / f'{local_id}.json').write_text(json.dumps(row, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def cursor():
    rows = [json.loads(p.read_text(encoding='utf-8')) for p in LANE.glob('[0-9]*.json')]
    counts = {}
    for row in rows:
        key = row.get('outcome', 'unknown')
        counts[key] = counts.get(key, 0) + 1
    reviewed = [row['manifest_index'] for row in rows if row.get('review_level') == 'primary_body_and_search']
    data = dict(schema='AIM_AUDIT_LANE_CURSOR_V1', lane='d', assigned_range=[684,911],
                assigned_count=228, evidence_count=len(rows), outcomes=counts,
                primary_body_and_search_count=len(reviewed),
                next_manifest_index=next((i for i in range(684,912) if i not in reviewed),None),
                updated_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat())
    (LANE / 'cursor.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    return data

if __name__ == '__main__':
    print(json.dumps(cursor(),indent=2))

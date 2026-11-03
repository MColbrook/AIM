const fs = require('fs');
const path = require('path');
const lane = __dirname;
const root = path.resolve(lane, '../../..');
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'research/solution-status-audit-2026-11-03/manifest.json'), 'utf8').replace(/^\uFEFF/, ''));
const targets = manifest.targets.slice(684,912);
function save(id, review) {
 const t = targets.find(x => x.id === id);
 if (!t) throw new Error('Outside assigned lane: '+id);
 const original = fs.readFileSync(path.join(root,t.file),'utf8');
 const statement = original.split('## Problem statement')[1].split('\n## ')[0].trim();
 const row = {schema:'AIM_SOLUTION_STATUS_REVIEW_V1',localID:id,manifest_index:manifest.targets.indexOf(t),checked_date:'2026-11-03',source_sha256:t.source_sha256,statement_sha256:t.statement_sha256,original_target:t,full_original_statement:statement,full_original_page:original,scope:'lane-d; canonical files untouched',...review};
 fs.writeFileSync(path.join(lane,id+'.json'),JSON.stringify(row,null,2)+'\n');
}
function cursor() {
 const rows=fs.readdirSync(lane).filter(p=>/^\d+\.json$/.test(p)).map(p=>JSON.parse(fs.readFileSync(path.join(lane,p),'utf8')));
 const counts={}; for(const r of rows) counts[r.outcome]=(counts[r.outcome]||0)+1;
 const reviewed=rows.filter(r=>r.review_level==='primary_body_and_search').map(r=>r.manifest_index);
 const data={schema:'AIM_AUDIT_LANE_CURSOR_V1',lane:'d',assigned_range:[684,911],assigned_count:228,evidence_count:rows.length,outcomes:counts,primary_body_and_search_count:reviewed.length,next_manifest_index:Array.from({length:228},(_,i)=>i+684).find(i=>!reviewed.includes(i))??null,updated_UTC:new Date().toISOString()};
 data.next_unstarted_manifest_index=Array.from({length:228},(_,i)=>i+684).find(i=>!rows.some(r=>r.manifest_index===i))??null;
 data.unstarted_count=228-rows.length;
 fs.writeFileSync(path.join(lane,'cursor.json'),JSON.stringify(data,null,2)+'\n');return data;
}
module.exports={save,cursor,targets};
if(require.main===module){if(process.argv[2]){const batch=JSON.parse(fs.readFileSync(process.argv[2],'utf8').replace(/^\uFEFF/,''));for(const row of batch)save(row.localID,row);}console.log(JSON.stringify(cursor(),null,2));}

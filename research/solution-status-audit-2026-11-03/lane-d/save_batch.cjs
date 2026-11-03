const fs=require('fs'),path=require('path'),{spawnSync}=require('child_process');
const {save,cursor}=require('./review_writer.cjs');
const input=process.argv[2],rows=JSON.parse(fs.readFileSync(input,'utf8').replace(/^\uFEFF/,''));
for(const r of rows)save(r.localID,r);
const aliasPath=path.join(__dirname,'aliases-'+rows[0].localID+'-'+rows.at(-1).localID+'.json');
fs.writeFileSync(aliasPath,JSON.stringify(Object.fromEntries(rows.map(r=>[r.localID,r.aliases])),null,2));
const scan=spawnSync(process.execPath,[path.join(__dirname,'snapshot_scan.cjs'),aliasPath],{encoding:'utf8'});
process.stdout.write(scan.stdout);process.stderr.write(scan.stderr);if(scan.status)process.exitCode=scan.status;
console.log(JSON.stringify(cursor(),null,2));

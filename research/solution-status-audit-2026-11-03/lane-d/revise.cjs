const fs=require('fs'),path=require('path');
const rows=JSON.parse(fs.readFileSync(process.argv[2],'utf8').replace(/^\uFEFF/,''));
for(const x of rows){
 const p=path.join(__dirname,x.localID+'.json'),r=JSON.parse(fs.readFileSync(p,'utf8'));
 r.followup_reviews??=[];
 r.followup_reviews.push({checked_UTC:new Date().toISOString(),previous_outcome:r.outcome,...x});
 if(x.outcome)r.outcome=x.outcome;
 if(x.review_level)r.review_level=x.review_level;
 if(x.outcome==='partial'){r.material_hold_resolved=true;r.remaining_material_source_gaps=[];}
 fs.writeFileSync(p,JSON.stringify(r,null,2)+'\n');
}
console.log(JSON.stringify(require('./review_writer.cjs').cursor(),null,2));

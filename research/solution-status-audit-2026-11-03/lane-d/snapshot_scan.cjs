const fs=require('fs'),path=require('path'),crypto=require('crypto');
const lane=__dirname, base=path.resolve(lane,'../_sources');
const fold=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const matches=(text,term)=>{const a=fold(text),b=fold(term);let i=-1;while((i=a.indexOf(b,i+1))>=0){if((i===0||!/[a-z0-9]/.test(a[i-1]))&&(i+b.length===a.length||!/[a-z0-9]/.test(a[i+b.length])))return true;}return false;};
const aliases=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const snapshots=['palomar-current-listing.json','hexagon-current-listing.json'].map(file=>{const raw=fs.readFileSync(path.join(base,file),'utf8').replace(/^\uFEFF/,'');return{file,sha256:sha(raw),data:JSON.parse(raw)};});
const overview=fs.readFileSync(path.join(base,'openai-overview.tex'),'utf8');
const blocks=overview.split('\\resultentry{').slice(1);
const rows=[];
for(const [localID,terms]of Object.entries(aliases)){
 const providers=snapshots.map(s=>({provider:s.data.provider,snapshot:s.file,snapshot_sha256:s.sha256,snapshot_UTC:s.data.UTC,listing_complete:s.data.listing_complete,query_type:'local title-and-abstract literal alias scan with Unicode accent folding and word boundaries',queries:terms,hits:s.data.entries.filter(e=>terms.some(t=>matches(e.title+' '+e.abstract,t))).map(e=>({id:e.id,title:e.title,url:e.links?.record||('https://data.palomar-registry.org/'+e.path)}))}));
 const hits=blocks.filter(b=>terms.some(t=>matches(b,t))).map(b=>({entry:b.match(/^(\d+)}/)?.[1],title:b.match(/^\d+}\{([^}]*)}/)?.[1],urls:[...b.matchAll(/https:\/\/github\.com\/openai\/math\/blob\/main\/preprints\/[^}\s]+/g)].map(m=>m[0])}));
 const row={localID,providers,openai:{snapshot:'openai-overview.tex',snapshot_sha256:sha(overview),queries:terms,hits,routing_only:true},scope:'Routing only; a matching title/summary is not a completed solution check.'};
 rows.push(row);
 const f=path.join(lane,localID+'.json');if(fs.existsSync(f)){const review=JSON.parse(fs.readFileSync(f,'utf8'));review.announcement_routing=row;fs.writeFileSync(f,JSON.stringify(review,null,2)+'\n');}
 console.log(JSON.stringify({localID,providers:providers.map(p=>({provider:p.provider,hits:p.hits})),openai:hits}));
}
fs.writeFileSync(path.join(lane,'snapshot-routing-'+Object.keys(aliases)[0]+'-'+Object.keys(aliases).at(-1)+'.json'),JSON.stringify(rows,null,2)+'\n');

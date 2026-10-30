import retrieve,concurrent.futures,json,pathlib
p=pathlib.Path(__file__).resolve().parent
jobs=[('B01','https://arxiv.org/pdf/2503.05336'),('B02','https://arxiv.org/pdf/2405.14782'),('B03','https://aclanthology.org/2024.acl-long.861.pdf'),('B04','https://arxiv.org/pdf/2402.09880')]
# B05/B06 URLs require title verification against returned paper; not assumed matches.
selected={'W7223669233','W7208765815','W7223769494','W7128444029','W7165668688','W7161816246','W4412748122','W7204498261','W7213965845','W7170143088','W7134131747'}
cs=[]
for f in sorted((p/'searches').glob('citation-*-forward.json')):
 for x in json.loads(f.read_text()).get('response',{}).get('results',[]):
  wid=x['id'].rsplit('/',1)[-1]
  if wid in selected and wid not in [r['id'] for r in cs]:
   sid=f'C{len(cs)+1:02}';cs.append({'id':wid,'source_id':sid,'title':x['title'],'doi':x.get('doi'),'date':x.get('publication_date'),'authors':[a['author']['display_name'] for a in x.get('authorships',[])],'origin':f.name,'url':x.get('doi')})
   loc=x.get('best_oa_location') or {};u=loc.get('pdf_url') or loc.get('landing_page_url') or x.get('doi');jobs.append((sid,u))
(p/'citation-candidates.json').write_text(json.dumps(cs,indent=2)+'\n')

jobs += [('B05','https://arxiv.org/pdf/2411.00640'),('B06','https://arxiv.org/pdf/2505.05602'),('B07','https://arxiv.org/pdf/2503.10694'),('R257-fallback','https://ojs.aaai.org/index.php/AIES/article/download/36595/38733/40670')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(retrieve.fetch,jobs):print(r['id'],r.get('file'),r.get('bytes'),r.get('error'),flush=True)

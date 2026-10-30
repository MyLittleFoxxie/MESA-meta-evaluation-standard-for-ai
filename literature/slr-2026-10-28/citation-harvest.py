import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime
p=pathlib.Path(__file__).resolve().parent
ids={'S01':'W4416268504','S02':'W4417172194','S05':'W4388802936','S06':'W4415967303','S07':'W4415798415'}
def fetch(job):
 sid,direction,url=job;out={'seed':sid,'direction':direction,'url':url,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=45) as r:out['response']=json.load(r)
 except Exception as e:out['error']=repr(e)
 (p/'searches'/f'citation-{sid}-{direction}.json').write_text(json.dumps(out,indent=2)+'\n')
 return sid,direction,len(out.get('response',{}).get('results',[])),out.get('error')
jobs=[]
for sid,wid in ids.items():
 d=json.loads((p/'searches'/f'seed-match-{sid}.json').read_text())['response']['results'][0]
 refs=d.get('referenced_works',[])
 if refs:
  jobs.append((sid,'backward','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'openalex_id:'+'|'.join(x.rsplit('/',1)[-1] for x in refs),'per-page':200})))
 else:(p/'searches'/f'citation-{sid}-backward.json').write_text(json.dumps({'seed':sid,'direction':'backward','response':{'results':[]},'note':'No indexed references; inspect full text reference list.'},indent=2))
 jobs.append((sid,'forward','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':f'cites:{wid},from_publication_date:2023-10-28,to_publication_date:2026-10-28','sort':'publication_date:desc','per-page':50})))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(fetch,jobs):print(r,flush=True)

import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime
p=pathlib.Path(__file__).resolve().parent
seeds={'S01':'Measuring what Matters: Construct Validity in Large Language Model Benchmarks','S02':'The Leaderboard Illusion','S03':'EFPA Test Review Model','S04':'Standards for Educational and Psychological Testing','S05':'A framework for characterising evaluation instruments of AI performance','S06':'A Definition of AGI','S07':'BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices'}
def req(t):
 sid,title=t;url='https://api.openalex.org/works?'+urllib.parse.urlencode({'search':title,'per-page':5})
 d={'seed':sid,'query':title,'url':url,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=45) as r:d['response']=json.load(r)
 except Exception as e:d['error']=repr(e)
 (p/'searches'/f'seed-match-{sid}.json').write_text(json.dumps(d,indent=2)+'\n')
 return sid,[(x['id'],x['title'],x.get('publication_date'),x.get('doi'),x.get('cited_by_count')) for x in d.get('response',{}).get('results',[])]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(req,seeds.items()): print(r,flush=True)

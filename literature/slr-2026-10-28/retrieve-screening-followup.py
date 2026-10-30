import retrieve,json,pathlib,concurrent.futures
p=pathlib.Path(__file__).resolve().parent
ids={53,54,55,66,71,79,105,164,256,293,294,295,299,302,323,325,327,331,337,341,342,350,352,356,363,364,365,367,368,374,377,380,382,397,400}
jobs=[]
for r in json.loads((p/'discovery-records.json').read_text()):
 if int(r['record_id'][1:]) in ids:
  u=r['url'].replace('http://arxiv.org/abs/','https://arxiv.org/pdf/').replace('https://arxiv.org/abs/','https://arxiv.org/pdf/')
  jobs.append((r['record_id'],u))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(retrieve.fetch,jobs):print(r['id'],r.get('file'),r.get('bytes'),r.get('error'),flush=True)

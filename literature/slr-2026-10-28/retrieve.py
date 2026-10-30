import pathlib,urllib.request,urllib.parse,json,concurrent.futures,datetime,re
p=pathlib.Path(__file__).resolve().parent
(p/'fulltext').mkdir(exist_ok=True)
def fetch(job):
 ident,url=job; rec={'id':ident,'url':url,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 MESA literature review'}),timeout=45) as r:
   raw=r.read();rec.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
  ext='pdf' if raw.startswith(b'%PDF') else 'html';name=f'fulltext/{ident}.{ext}';(p/name).write_bytes(raw);rec['file']=name;rec['bytes']=len(raw)
 except Exception as e:rec['error']=repr(e)
 (p/'searches'/f'retrieve-{ident}.json').write_text(json.dumps(rec,indent=2)+'\n')
 return rec
if __name__=='__main__':
 ids={2,4,42,61,63,78,91,97,117,141,149,160,161,166,170,172,196,203,257,259,265,266,285,286,291,296,298,300,306,310,321,339,349,357,362,371,372,373,383,412,416}
 jobs=[]
 for r in json.loads((p/'discovery-records.json').read_text()):
  if int(r['record_id'][1:]) not in ids:continue
  u=r.get('url') or r.get('doi');u=u.replace('http://','https://')
  if 'arxiv.org/abs/' in u:u=u.replace('/abs/','/pdf/')
  if r['record_id']=='R097':u='https://aclanthology.org/2026.evaleval-1.25.pdf'
  if r['record_id']=='R298':u='https://aclanthology.org/2024.findings-acl.29.pdf'
  jobs.append((r['record_id'],u))
 jobs += [('S04','https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf'),('S07-proceedings','https://proceedings.nips.cc/paper_files/paper/2024/file/26889e8359e7ef8a7f5d77457364ca55-Paper-Datasets_and_Benchmarks_Track.pdf')]
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for r in ex.map(fetch,jobs):print(r['id'],r.get('file'),r.get('bytes'),r.get('error'),flush=True)

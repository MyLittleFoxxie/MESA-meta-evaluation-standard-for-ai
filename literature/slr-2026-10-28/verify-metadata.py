import json,pathlib,re,urllib.request,concurrent.futures,datetime,html
p=pathlib.Path(__file__).resolve().parent
jobs={}
for f in (p/'searches').glob('retrieve-*.json'):
 d=json.loads(f.read_text());u=d.get('url','');m=re.search(r'arxiv.org/(?:pdf|abs)/(\d{4}\.\d+)',u)
 if m:jobs[d['id']]=m[1]
jobs.update({'S01':'2511.04703','S02':'2504.20879','S06':'2510.18212','S07':'2411.12990','R298':'2309.17012','R330':'2307.03109','B26':'2306.03100','B03':'2406.08723','R295':'2305.17926'})
def fetch(pair):
 sid,aid=pair
 if (p/'searches'/f'metadata-{sid}.json').exists():return sid,'already recorded',None
 url='https://arxiv.org/abs/'+aid;d={'source_id':sid,'url':url,'requested_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=40) as r:s=r.read().decode()
  (p/'raw'/f'metadata-{sid}.html').write_text(s)
  for key in ['title','author','date','online_date','arxiv_id','doi','journal_title']:
   d[key]=[html.unescape(v) for v in re.findall(r'<meta name="citation_'+key+r'" content="([^"]*)"',s)]
  match=re.search(r'Submission history(.*?)</div>',s,re.S);d['history']=re.sub('<[^>]+>',' ',match[1]).strip() if match else ''
 except Exception as e:d['error']=repr(e)
 (p/'searches'/f'metadata-{sid}.json').write_text(json.dumps(d,indent=2)+'\n');return sid,d.get('date'),d.get('error')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for x in ex.map(fetch,jobs.items()):print(x,flush=True)

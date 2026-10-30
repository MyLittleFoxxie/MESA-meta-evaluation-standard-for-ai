import json,pathlib,urllib.request,urllib.parse,datetime
p=pathlib.Path(__file__).resolve().parent
d=json.loads((p/'searches/seed-match-S05.json').read_text())['response']['results'][0]
refs=d['referenced_works']
for i in range(0,len(refs),40):
 url='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'openalex_id:'+'|'.join(refs[i:i+40]),'per-page':50})
 out={'url':url,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requested_ids':refs[i:i+40]}
 try:
  with urllib.request.urlopen(url,timeout=30) as r:out['response']=json.load(r)
 except Exception as e:out['error']=repr(e)
 (p/'searches'/f'citation-S05-backward-retry-{i//40+1}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(i,len(out.get('response',{}).get('results',[])),out.get('error'),flush=True)

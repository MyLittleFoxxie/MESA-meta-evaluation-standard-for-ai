"""Execute frozen bounded searches; no screening or source judgments."""
import concurrent.futures, datetime, json, pathlib, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
QUERIES=['AI benchmark quality review framework','language model benchmark validity reliability fairness','AI evaluation checklist guidance reproducibility','benchmark review accessibility usability comprehension effort']
def request(job):
 service,i,q,url=job
 out={'service':service,'query_id':f'Q{i}','query':q,'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':[]}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MESA-literature-review/1.0'}),timeout=60) as r:
   raw=r.read();out['http_status']=r.status
  ext='xml' if service=='arxiv' else 'json';name=f'{service}-q{i}.{ext}'
  (ROOT/'raw'/name).write_bytes(raw);out['raw_file']='raw/'+name
  if service=='openalex':
   d=json.loads(raw);out['total_hits']=d['meta'].get('count')
   for x in d['results']:
    inv=x.get('abstract_inverted_index') or {}; words={n:w for w,ns in inv.items() for n in ns}
    out['records'].append({'id':x['id'],'title':x['title'],'doi':x.get('doi'),'date':x.get('publication_date'),'authors':[a['author']['display_name'] for a in x.get('authorships',[])],'url':(x.get('primary_location') or {}).get('landing_page_url'),'abstract':' '.join(words[n] for n in sorted(words)),'referenced_works':x.get('referenced_works',[]),'cited_by_count':x.get('cited_by_count')})
  elif service=='crossref':
   d=json.loads(raw)['message'];out['total_hits']=d.get('total-results')
   for x in d['items']:
    out['records'].append({'id':x['DOI'],'title':' '.join(x.get('title',[])),'doi':x['DOI'],'date':x.get('published',{}).get('date-parts'),'authors':[a.get('given','')+' '+a.get('family','') for a in x.get('author',[])],'url':x.get('URL'),'abstract':x.get('abstract',''),'references':x.get('reference',[])})
  else:
   d=ET.fromstring(raw);ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
   out['total_hits']=d.findtext('o:totalResults',namespaces=ns)
   for x in d.findall('a:entry',ns):
    out['records'].append({'id':x.findtext('a:id',namespaces=ns),'title':' '.join(x.findtext('a:title',default='',namespaces=ns).split()),'date':x.findtext('a:published',namespaces=ns),'url':x.findtext('a:id',namespaces=ns),'abstract':x.findtext('a:summary',namespaces=ns),'authors':[a.findtext('a:name',namespaces=ns) for a in x.findall('a:author',ns)]})
 except Exception as e:out['error']=repr(e)
 (ROOT/'searches'/f'{service}-q{i}.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
 return {'service':service,'q':i,'returned':len(out['records']),'total':out.get('total_hits'),'error':out.get('error')}
if __name__=='__main__':
 for p in ['raw','searches']: (ROOT/p).mkdir(exist_ok=True)
 jobs=[]
 for i,q in enumerate(QUERIES,1):
  jobs.append(('openalex',i,q,'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':q,'filter':'from_publication_date:2023-10-28,to_publication_date:2026-10-28','per-page':50})))
  jobs.append(('crossref',i,q,'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':q,'filter':'from-pub-date:2023-10-28,until-pub-date:2026-10-28','rows':50,'sort':'relevance'})))
  aq=' AND '.join('all:'+w for w in q.split())+' AND submittedDate:[202310280000 TO 202610282359]'
  jobs.append(('arxiv',i,q,'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':aq,'start':0,'max_results':50,'sortBy':'relevance'})))
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for r in pool.map(request,jobs): print(json.dumps(r),flush=True)

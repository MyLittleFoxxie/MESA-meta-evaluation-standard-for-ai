"""Acquire immutable public source snapshots; never execute repository code."""
import hashlib,io,json,tarfile,urllib.request,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SPECS=[('humaneval','openai/human-eval','2107.03374'),('truthfulqa','sylinrl/TruthfulQA','2109.07958'),('designqa','anniedoris/design_qa','2404.07917')]
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MESA-research-source-snapshot'}),timeout=120).read()
def main():
 from pypdf import PdfReader
 records=[]
 for name,repo,paper in SPECS:
  dest=ROOT/'sources'/name;dest.mkdir(parents=True,exist_ok=True)
  meta=dest/'snapshot.json'
  if meta.exists(): records.append(json.loads(meta.read_text()));continue
  commit=json.loads(get('https://api.github.com/repos/'+repo+'/commits/HEAD'))['sha']
  url=f'https://api.github.com/repos/{repo}/tarball/{commit}'
  raw=get(url); (dest/'repository.tar.gz').write_bytes(raw)
  rd=dest/'repository';rd.mkdir(exist_ok=True)
  excluded=[]
  with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as t:
   for member in t.getmembers():
    parts=Path(member.name).parts[1:]
    if not parts:continue
    target=rd.joinpath(*parts)
    if not target.resolve().is_relative_to(rd.resolve()):raise ValueError('path escape')
    if member.isfile():
     target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(t.extractfile(member).read())
    elif not member.isdir():excluded.append(member.name)
  pdf=get('https://arxiv.org/pdf/'+paper);(dest/'paper.pdf').write_bytes(pdf)
  reader=PdfReader(io.BytesIO(pdf))
  text='\n\n'.join(f'[PDF page {i+1}]\n'+(page.extract_text() or '') for i,page in enumerate(reader.pages))
  (dest/'paper.txt').write_text(text)
  rec={'benchmark':name,'repository_url':'https://github.com/'+repo,'commit':commit,'archive_url':url,'paper_url':'https://arxiv.org/pdf/'+paper,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':len(reader.pages),'excluded_nonregular':excluded,'sha256':{str(p.relative_to(dest)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.rglob('*')) if p.is_file()}}
  meta.write_text(json.dumps(rec,indent=2)+'\n');records.append(rec)
  print(name,commit,len(raw),len(text),flush=True)
 (ROOT/'sources.json').write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__':main()

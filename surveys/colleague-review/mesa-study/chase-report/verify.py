"""Verify current CHASE reporting and source preservation without compiling LaTeX."""
from pathlib import Path
import csv,hashlib,json,re,subprocess,sys,urllib.parse
B=Path(__file__).resolve().parent;R=B.parents[3];S=B.parent
load=lambda p:json.loads(p.read_text());csvload=lambda n:list(csv.DictReader((B/n).open()))
def strings(x):
 if isinstance(x,str):return [x]
 if isinstance(x,list):return sum((strings(v) for v in x),[])
 if isinstance(x,dict):return sum((strings(v) for v in x.values()),[])
 return []
def main():
 checks=[]
 def check(ok,label):checks.append({'check':label,'passed':bool(ok)})
 paper=(R/'paper_chase.tex').read_text();summary=load(B/'summary.json');selected=load(B/'selected-reviews.json');audit=load(B/'qualitative-audit.json')
 for j in load(B/'selection.json')['jobs']:
  for field in ['input','response']:check(hashlib.sha256((S/j[field]).read_bytes()).hexdigest()==j[field+'_sha256'],j['id']+' '+field+' source fingerprint')
 check(len(load(B/'selection.json')['jobs'])==30,'Exactly thirty selected conversations')
 for k,n in [('completed',30),('eligible',28),('attempts',32),('claim_answers',686),('matches',670),('mismatches',16),('contrasts',322),('contrast_matches',322),('both_expected',310),('negative_supported',0),('negative_opportunities',84),('quotes_found',686)]:check(summary[k]==n,'Reporting total '+k)
 check(summary['mesa']['variable_pairs']==12 and summary['mesa']['no_not_sure_pairs']==5,'Twelve varying pairs; five include No and Not sure')
 check(summary['mesa']['matching_pairs']==435 and summary['mesa']['pairs']==500,'Repeated-choice matches')
 check(summary['mesa']['choices']=={'Yes':58,'Partly':142,'No':21,'Not sure':29},'Choice counts')
 for method,match,alt in [('mesa',242,239),('efpa',237,240),('ordinary',191,191)]:check(summary['groups'][method]['matches']==match and summary['groups'][method]['sensitivity_matches']==alt,'Claim counts '+method)
 clean=re.sub(r'(?<!\\)%[^\n]*','',paper);stack=[];valid=True
 for kind,name in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
  if kind=='begin':stack.append(name)
  elif not stack or stack.pop()!=name:valid=False
 check(valid and not stack,'Balanced environments')
 depth=0;negative=False
 for char in re.sub(r'\\[{}]','',clean):
  if char=='{':depth+=1
  elif char=='}':depth-=1
  negative|=depth<0
 check(depth==0 and not negative,'Balanced braces')
 labels=re.findall(r'\\label\{([^}]+)\}',paper);check(len(labels)==len(set(labels)),'Unique labels')
 for ref in re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',paper):check(ref in labels,'Reference '+ref)
 keys=set(re.findall(r'@\w+\s*\{\s*([^,]+)',(R/'references.bib').read_text()))
 for group in re.findall(r'\\cite\w*\{([^}]+)\}',paper):
  for key in group.split(','):check(key in keys,'Citation '+key)
 for asset in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',paper):check((R/asset).exists(),'Asset '+asset)
 packet=load(R/'surveys/colleague-review/packet.json');check(len(packet['questions'])==25,'25 questions')
 for q in packet['questions']:check(str(q['id'])+' & '+q['question']+r' \\' in paper,'Exact question '+str(q['id']))
 variation=paper.split(r'\label{tab:variation}',1)[1].split(r'\end{table}',1)[0];ds=csvload('mesa-distributions.csv')
 for d in ds:
  row=('ARC-AGI-2' if d['benchmark']=='arc' else 'DesignQA')+' & '+d['question']+' & '+', '.join(c+' '+d[c] for c in ['Yes','Partly','No','Not sure','Not applicable'] if int(d[c]))+r' \\'
  check((row in variation)==(d['variable']=='True'),'Variation row '+d['benchmark']+' '+d['question'])
 check(len(re.findall(r'^(?:ARC-AGI-2|DesignQA) &',variation,re.M))==12,'Exactly twelve variation rows')
 passages=(S/'claude-sonnet-5-5-guidance-v2/materials/real-passages.txt').read_text()
 for q in re.findall(r'\\textbf\{Passage:\} ``(.*?)\x27\x27',paper):check(q in passages,'Exact passage quotation')
 mesa=next(x['review'] for x in selected if x['condition']=='mesa' and x['review']['benchmark']=='designqa')
 for q in [8,12]:
  answer=next(a for a in mesa['mesa_answers'] if a['id']==q);check(answer['comment'] in paper and answer['choice']=='Partly','Exact recorded comment '+str(q))
 alltexts=sum((strings(x['review']) for x in selected),[])+[passages]
 for quote in re.findall(r'``(.*?)\x27\x27',paper,re.S):check(any(quote in t for t in alltexts),'Paper quote '+quote[:45])
 check(len(audit)==36,'All twelve points for each method')
 for row in audit:
  raw=load(S/row['source']);review=next(r for r in raw['reviews'] if r['benchmark']==row['benchmark'])
  for quote in row['quotes']:check(any(quote in t for t in strings(review)),'Audit quote '+row['condition']+' '+quote[:30])
 for field in ['id','condition','source']:
  check(all(x[field] in next(j for j in load(B/'selection.json')['jobs'] if j['id']==x['id'] and j['source']==x['source'])[field] for x in selected),'Selected-review source mapping '+field)
 current=[R/'paper_chase.tex',R/'README.md',R/'CHASE-study.md',R/'CHASE-review-response.md']
 for p in current:
  t=p.read_text();check(not re.search(r'\brevised\b',t,re.I),'Prohibited wording absent '+p.name)
  for stale in ['243/245','456/500','91.2','both questions are answered No','Five of the ten notes named question 8','sec:followup','original MESA','new MESA']:
   check(stale not in t,'No obsolete claim '+p.name+' '+stale)
 for p in current[1:]+list(B.glob('*.md')):
  for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text()):
   if re.match(r'[a-z]+://',target):continue
   local,_,anchor=target.partition('#');dest=(p.parent/urllib.parse.unquote(local)) if local else p
   check(dest.exists(),'Link '+p.name+' '+target)
   if anchor and dest.suffix=='.md' and dest.exists():
    headings=re.findall(r'^#+\s+(.+)$',dest.read_text(),re.M);ids=[re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in headings];check(anchor in ids,'Anchor '+target)
 preservation=subprocess.run([sys.executable,str(S/'claude-sonnet-5-5-guidance-v2/verify_revision.py')],capture_output=True,text=True)
 check(preservation.returncode==0,'Historical source preservation and raw-output checks')
 abstract=paper.split(r'\begin{abstract}',1)[1].split(r'\end{abstract}',1)[0];words=len(re.sub(r'\\textbf\{([^}]+)\}',r'\1',abstract).split());check(200<=words<=230,'Abstract length 200–230')
 result={'checks':len(checks),'passed':sum(c['passed'] for c in checks),'issues':[c['check'] for c in checks if not c['passed']],'abstract_words':words,'source_preservation':json.loads(preservation.stdout) if preservation.returncode==0 else preservation.stdout,'layout':'No LaTeX compilation or PDF preview. Layout and page length unchecked.'}
 (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return bool(result['issues'])
if __name__=='__main__':raise SystemExit(main())

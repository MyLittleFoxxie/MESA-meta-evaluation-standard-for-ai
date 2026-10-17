#!/usr/bin/env python3
"""Check preservation, frozen inputs and accounting without changing evidence."""
from pathlib import Path
import json,hashlib,collections,re,csv
B=Path(__file__).resolve().parent;R=B.parents[3]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 checks=[]
 def check(v,description):checks.append({'check':description,'passed':bool(v)})
 frozen=load(B/'freeze-manifest.json')
 for f,h in frozen['files'].items():check((B/f).is_file() and sha(B/f)==h,'Frozen '+f)
 protected=load(B/'analyst/pre-edit-hashes.json')
 for f,h in protected.items():
  if f in ['paper_chase.tex','README.md','CHASE-study.md']:continue
  check((R/f).is_file() and sha(R/f)==h,'Preserved '+f)
 jobs=load(B/'jobs.json');check(len(jobs)==180,'180 planned jobs')
 cells=collections.Counter((j['batch'],j['condition'],j['role']) for j in jobs);check(len(cells)==36 and set(cells.values())=={5},'36 cells of five repetitions')
 inst=collections.defaultdict(set)
 for j in jobs:
  p=B/j['input'];check(sha(p)==j['sha256'],'Input '+j['id']);text=p.read_text();inst[j['condition']].add(text.split('INSTRUMENT:\n')[1].split('\nTASK:\n')[0])
 check(set(inst)=={'mesa','efpa','ordinary'} and all(len(x)==1 for x in inst.values()),'One fixed instrument per method')
 instrument=(B/'materials/mesa.txt').read_text();qs=re.findall(r'^(\d+)\. \[([^]]+)\] (.+)$',instrument,re.M)
 check([int(q[0]) for q in qs]==list(range(1,26)),'25 question IDs');check(len(set(q[1] for q in qs))==6,'Six domains')
 source=R/'surveys/colleague-review/accessibility-study/v1/materials/mesa-revised.txt';check(sha(source)==sha(B/'materials/mesa.txt'),'MESA instrument exact latest text')
 packet=load(R/'surveys/colleague-review/packet.json')
 # Packet nesting differs across source versions; exact texts must all occur in its serialization.
 packettext=json.dumps(packet,ensure_ascii=False)
 for n,d,q in qs:check(q in packettext,'Canonical question '+n)
 for c in ['Yes','Partly','No','Not sure','Not applicable']:check(c in instrument,'Choice '+c)
 threads=[];metas=[];toolcount=0
 for p in (B/'outputs').glob('**/metadata.json'):
  m=load(p);metas.append(m);threads+=m.get('thread_ids',[])
  check(m.get('requested_model')=='gpt-6.1-sol' and m.get('reasoning_effort')=='medium','Model/settings '+str(p.relative_to(B)))
  check(m.get('input_sha256')==next(j['sha256'] for j in jobs if j['id']==m['job']['id']),'Metadata input hash '+str(p.relative_to(B)))
  for name,h in m.get('output_files_sha256',{}).items():check((p.parent/name).is_file() and sha(p.parent/name)==h,'Output '+str((p.parent/name).relative_to(B)))
  toolcount+=len([t for t in m.get('tool_items',[]) if t.get('item',{}).get('type')!='error'])
  if m.get('finished_at'):check(m['started_at']>=frozen['frozen_utc'],'Run after freeze '+m['job']['id'])
 check(len(threads)==len(set(threads)),'Unique reviewer conversation identifiers');check(toolcount==0,'No observed reviewer tools')
 html=(B/'questionnaire.html').read_text();check(not re.search(r'<(?:form|input|textarea|select|button|script|iframe|details)\b',html,re.I),'Static reading document without forms/scripts/expandable help')
 ids=re.findall(r'\bid="([^"]+)"',html);check(len(ids)==len(set(ids)),'Unique HTML IDs');check(len(re.findall(r'<article id="q\d+"',html))==25,'HTML 25 questions')
 check('form-action \'none\'' in html,'Submission prohibited by CSP')
 for target in re.findall(r'href="#([^"]+)"',html):check(target in ids,'HTML anchor '+target)
 if (B/'analysis/summary.json').exists():
  summary=load(B/'analysis/summary.json');rows=list(csv.DictReader((B/'analysis/runs.csv').open()));claims=list(csv.DictReader((B/'analysis/claims.csv').open()));answers=list(csv.DictReader((B/'analysis/mesa-answers.csv').open()))
  check(len(rows)==180,'180 accounting rows');check(sum(r['eligible']=='True' for r in rows)==summary['eligible'],'Eligible count')
  for batch,cc in summary['cases'].items():
   for condition,stats in cc.items():
    selected=[r for r in claims if r['batch']==batch and r['condition']==condition]
    check(len(selected)==stats['answers'] and sum(r['label']==r['expected'] for r in selected)==stats['matches'],batch+' '+condition+' claim counts')
  check(len(answers)==summary['mesa']['all']['answers'],'MESA choice total')
  variable=sum(len({r['choice'] for r in answers if r['benchmark']==b and r['question']==str(q)})>1 for b in ['arc','designqa'] for q in range(1,26));check(variable==summary['mesa']['all']['variable_pairs'],'Variation over 50 question-benchmark pairs')
 out={'checks':len(checks),'passed':sum(c['passed'] for c in checks),'issues':[c['check'] for c in checks if not c['passed']]}
 (B/'analysis/verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return not out['issues']
if __name__=='__main__':raise SystemExit(0 if main() else 1)

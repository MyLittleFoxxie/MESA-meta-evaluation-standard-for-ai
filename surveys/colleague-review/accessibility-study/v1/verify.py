#!/usr/bin/env python3
"""Verify frozen inputs and protected records without regenerating material."""
from pathlib import Path
import json,hashlib,re,collections
B=Path(__file__).resolve().parent;R=B.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 issues=[];checks=0
 def check(v,msg):
  nonlocal checks
  checks+=1
  if not v:issues.append(msg)
 freeze=json.loads((B/'freeze-manifest.json').read_text());guidance=json.loads((B/'guidance-freeze.json').read_text())
 for rel,h in freeze['files'].items():check((B/rel).is_file() and sha(B/rel)==h,'Frozen file changed: '+rel)
 for rel,h in json.loads((B/'analyst/protected-files.json').read_text()).items():check((R/rel).is_file() and sha(R/rel)==h,'Protected file changed: '+rel)
 packet=json.loads((R/'surveys/colleague-review/packet.json').read_text());revised=json.loads((B/'materials/revised-guidance.json').read_text())
 check(len(revised['questions'])==25,'Question count');check(revised['choices']==packet['choices'],'Choice definitions');check([q['question'] for q in revised['questions']]==[q['question'] for q in packet['questions']],'Question text');check([q['id'] for q in revised['questions']]==list(range(1,26)),'Stable question IDs');check(len({q['domain'] for q in revised['questions']})==6,'Six domains')
 thread_ids=[]
 jobs=json.loads((B/'jobs.json').read_text());check(len(jobs)==40,'40 planned conversations');check(all(j['role']=='neutral' for j in jobs),'Neutral only')
 check(set(collections.Counter((j['batch'],j['condition']) for j in jobs).values())=={5},'Five repetitions per batch and method')
 for batch in ['real','controlled']:
  a=(B/f'inputs/{batch}-mesa_original-neutral-1.txt').read_text();z=(B/f'inputs/{batch}-mesa_revised-neutral-1.txt').read_text();check(a.split('INSTRUMENT:\n')[0]==z.split('INSTRUMENT:\n')[0],'Same common instructions '+batch);check(a.split('\nTASK:\n')[1]==z.split('\nTASK:\n')[1],'Same task and passages '+batch)
 cases=json.loads((B/'materials/test-cases.json').read_text());key=json.loads((B/'analyst/expected.json').read_text());check(len(cases)==16 and sum(len(c['probes']) for c in cases)==32,'16 cases and 32 claims');check(guidance['guidance_frozen_utc']<key['created_utc']<freeze['frozen_utc'],'Guidance before cases before final freeze')
 for job in jobs:
  text=(B/job['input']).read_text();check(sha(B/job['input'])==job['sha256'],'Input hash '+job['id']);check('analyst/expected' not in text and 'protected-files' not in text,'No organizer file references '+job['id'])
  for meta in (B/'outputs'/job['id']).glob('**/metadata.json'):
   m=json.loads(meta.read_text());thread_ids.extend(m.get('thread_ids',[]));check(m['started_at']>freeze['frozen_utc'],'Run after freeze '+job['id']);check(m['requested_model']=='gpt-6.1-sol','Requested model '+job['id']);check(m['input_sha256']==job['sha256'],'Run input hash '+job['id']);check(not m.get('tool_items'),'No observed reviewer tools '+job['id'])
   for name,h in m.get('output_files_sha256',{}).items():check(sha(meta.parent/name)==h,'Saved output hash '+job['id']+'/'+name)
 check(len(thread_ids)==len(set(thread_ids)),'Distinct recorded conversation IDs')
 html=(B/'prototype.html').read_text();check(not re.search(r'<(?:script|form|input|textarea|select|button|iframe)\b',html,re.I),'Prototype no answer or submission behavior');check(len(re.findall(r'<article id="q\d+"',html))==25,'Prototype questions');ids=re.findall(r'\bid="([^"]+)"',html);check(len(ids)==len(set(ids)),'Prototype unique IDs');check(set(re.findall(r'href="#([^"]+)"',html))<=set(ids),'Prototype anchors defined')
 result={'passed':not issues,'checks':checks,'issues':issues,'limitations':'No human usability evidence; no LaTeX compilation.'};(B/'analysis').mkdir(exist_ok=True);(B/'analysis/verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(issues))
if __name__=='__main__':main()

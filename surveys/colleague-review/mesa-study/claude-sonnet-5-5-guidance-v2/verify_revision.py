"""Read-only checks for the versioned follow-up and manuscript question table."""
from pathlib import Path
import hashlib,json,re
import validation_helpers as V
B=Path(__file__).resolve().parent;OLD=B.parent/'claude-sonnet-5-5';R=B.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 f=json.loads((B/'freeze-manifest.json').read_text());a=json.loads((B/'analysis-code-amendment.json').read_text());reporting=json.loads((B/'reporting-amendment.json').read_text());checks=[]
 def check(ok,name):checks.append({'check':name,'passed':bool(ok)})
 for name,digest in f['original_files_sha256'].items():check((OLD/name).exists() and sha(OLD/name)==digest,'Original preserved: '+name)
 for name,digest in f['files'].items():check(sha(B/name)==a['files'].get(name,reporting['files'].get(name,digest)),'Frozen file or explicit code amendment: '+name)
 old=(OLD/'materials/mesa.txt').read_text();new=old
 for before,after in f['changes']:check(new.count(before)==1,'Unique edit '+before[:40]);new=new.replace(before,after)
 check(new==(B/'materials/mesa.txt').read_text(),'Exactly the two recorded guidance edits')
 jobs=json.loads((B/'jobs.json').read_text());check(len(jobs)==10,'Ten jobs');raw_claims=[];raw_answers=[];expected=json.loads((B/'analyst/expected.json').read_text())['cases']['cases']
 for j in jobs:
  check(j['condition']=='mesa','MESA only '+j['id']);check(sha(B/j['input'])==j['sha256'],'Input hash '+j['id'])
  check((B/j['input']).read_text()==(OLD/j['input']).read_text().replace(old,new),'Only revised guidance in '+j['id'])
  paths,permitted,issues=V.attempt_layout(B/'outputs'/j['id']);check(not issues,'Retry policy '+j['id'])
  if paths:
   final=paths[-1][1];meta=json.loads((final/'metadata.json').read_text())
   check(meta.get('turn_completed'),'Completed '+j['id'])
   data=V.parse((final/'response.txt').read_text());check(not V.validate(data,j,expected if j['batch']=='cases' else {}),'Schema '+j['id'])
   if j['batch']=='cases':
    raw_claims.extend((case['id'],probe) for case in data['cases'] for probe in case['probes'])
   else:raw_answers.extend(answer for review in data['reviews'] for answer in review['mesa_answers'])
  for attempt,p in paths:
   m=json.loads((p/'metadata.json').read_text());check(m.get('init_tools')==[] and m.get('init_mcp_servers')==[] and not m.get('tool_items'),'Isolation '+j['id']+' '+str(attempt))
   check(m.get('reported_model')=='claude-sonnet-5-5','Model '+j['id']+' '+str(attempt))
   for name,h in m.get('output_files_sha256',{}).items():check(sha(p/name)==h,'Raw output hash '+j['id']+' '+str(attempt)+' '+name)
 report=json.loads((B/'analysis/follow-up.json').read_text())
 check(len(raw_claims)==report['claim_answers']==245,'Claim count from raw outputs')
 check(sum(probe['label']==expected[cid][probe['id']]['label'] for cid,probe in raw_claims)==report['original_key_matches'],'Original-key count from raw outputs')
 check(sum(probe['label']==('Contradicted' if (cid,probe['id'])==('P6B','claim1') else expected[cid][probe['id']]['label']) for cid,probe in raw_claims)==report['p6b_alternative_matches'],'Sensitivity count from raw outputs')
 check(len(raw_answers)==report['mesa']['answers']==250,'Choice count from raw outputs')
 packet=json.loads((R/'surveys/colleague-review/packet.json').read_text());paper=(R/'paper_chase.tex').read_text()
 check(len(packet['questions'])==25,'25 packet questions')
 for q in packet['questions']:check(str(q['id'])+' & '+q['question']+r' \\' in paper,'Verbatim table question '+str(q['id']))
 result={'checks':len(checks),'passed':sum(c['passed'] for c in checks),'issues':[c['check'] for c in checks if not c['passed']],'layout':'No compilation; layout and page length unchecked.'}
 print(json.dumps(result,indent=2));return bool(result['issues'])
if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
"""Cross-check derived counts directly against the selected raw response files."""
from pathlib import Path
import json,csv,collections,itertools,hashlib
B=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_text())
def main():
 summary=load(B/'analysis/summary.json');key=load(B/'analyst/expected.json');checks=0
 def check(v,msg):
  nonlocal checks
  checks+=1
  assert v,msg
 with (B/'analysis/runs.csv').open() as f:runs=list(csv.DictReader(f))
 for condition,reported in summary['conditions'].items():
  controlled=[r for r in runs if r['eligible']=='True' and r['condition']==condition and r['batch']=='controlled'];real=[r for r in runs if r['eligible']=='True' and r['condition']==condition and r['batch']=='real'];matches=answers=negative=opps=0;choices=collections.defaultdict(list)
  for run in controlled+real:
   base=B/'outputs'/run['id'];path=base/'attempt-2/response.txt' if (base/'attempt-2/response.txt').exists() else base/'response.txt';d=load(path)
   if run['batch']=='controlled':
    for c in d['cases']:
     for p in c['probes']:
      expected=key['cases'][c['id']][p['id']];answers+=1;matches+=p['label']==expected['label']
      if expected['negative_conclusion'] and expected['label']!='Supported':opps+=1;negative+=p['label']=='Supported'
   elif condition.startswith('mesa_'):
    for r in d['reviews']:
     for a in r['mesa_answers']:choices[r['benchmark'],a['id']].append(a['choice'])
  check(len(real)==reported['real_valid'],'Real denominator '+condition);check(len(controlled)==reported['controlled_valid'],'Controlled denominator '+condition);check(matches==reported['matches'] and answers==reported['claim_answers'],'Claim counts '+condition);check(negative==reported['unjustified_negative_support'] and opps==reported['negative_claim_opportunities'],'Negative-claim indicator '+condition)
  if choices:
   pair_count=pair_matches=0
   for values in choices.values():
    for x,y in itertools.combinations(values,2):pair_count+=1;pair_matches+=x==y
   check(pair_count==reported['pairs'] and pair_matches==reported['matching_pairs'],'Repeated-choice pairs '+condition);check(sum(len(v) for v in choices.values())==reported['mesa_answers'],'MESA answer count '+condition);check(sum(len(set(v))>1 for v in choices.values())==reported['variable_question_benchmark_pairs'],'Variable question pairs '+condition)
 audit=load(B/'analysis/illustrative-reviews.json')
 def strings(v):
  if isinstance(v,str):yield v
  elif isinstance(v,list):
   for x in v:yield from strings(x)
  elif isinstance(v,dict):
   for x in v.values():yield from strings(x)
 for row in audit['points']:
  source=B/f"outputs/real-{row['condition']}-neutral-1/response.txt";d=load(source);review=next(r for r in d['reviews'] if r['benchmark']==row['benchmark']);check(row['quotation']['text'] in list(strings(review)),'Audit quotation '+str((row['condition'],row['point'])))
 for source in audit['sources']:check(hashlib.sha256((B/source['source']).read_bytes()).hexdigest()==source['sha256'],'Audit source hash '+source['condition'])
 check(summary['planned']==len(runs)==40,'Run accounting');check(summary['eligible']==sum(r['eligible']=='True' for r in runs),'Usable denominator')
 result={'passed':True,'checks':checks,'note':'Direct raw-output counts reproduce summaries; exact generated quotations verified, not semantic correctness.'};(B/'analysis/calculation-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

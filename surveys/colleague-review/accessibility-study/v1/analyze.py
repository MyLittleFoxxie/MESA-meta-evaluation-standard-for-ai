#!/usr/bin/env python3
"""Read-only original outputs -> reproducible tables; never repairs an answer."""
from pathlib import Path
import json,csv,collections,itertools,hashlib
B=Path(__file__).resolve().parent
CHOICES=['Yes','Partly','No','Not sure','Not applicable'];LABELS=['Supported','Contradicted','Not established']
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def table(name,rows,fields):
 with (B/'analysis'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def validate(data,job):
 errors=[]
 def err(c,t):
  if not c:errors.append(t)
 if not isinstance(data,dict):return ['Root is not an object']
 if job['batch']=='real':
  reviews=data.get('reviews');err(isinstance(reviews,list),'reviews must be a list')
  if not isinstance(reviews,list):return errors
  err(len(reviews)==2,'Expected two reviews');err(all(isinstance(r,dict) for r in reviews),'Each review must be an object')
  if not all(isinstance(r,dict) for r in reviews):return errors
  err(sorted(str(r.get('benchmark')) for r in reviews)==['arc','designqa'],'Benchmark IDs must occur once each')
  for r in reviews:
   for field in ['supported_claims','documented_problems','missing_information','reinterpretations']:
    err(isinstance(r.get(field),list) and all(isinstance(x,str) for x in r[field]),field+' must be list of strings')
   for field in ['instrument_review','closing_note']:err(isinstance(r.get(field),str),field+' must be string')
   if job['condition'].startswith('mesa_'):
    a=r.get('mesa_answers');err(isinstance(a,list),'mesa_answers must be list')
    if not isinstance(a,list):continue
    err(len(a)==25 and all(isinstance(x,dict) for x in a),'Expected 25 answer objects')
    if not all(isinstance(x,dict) for x in a):continue
    err(sorted(str(x.get('id')) for x in a)==sorted(map(str,range(1,26))),'Question IDs must occur once each')
    for x in a:err(type(x.get('id')) is int,'Question ID must be integer');err(x.get('choice') in CHOICES,'Invalid MESA choice');err(x.get('comment') is None or isinstance(x.get('comment'),str),'Invalid optional comment')
 else:
  cases=data.get('cases');err(isinstance(cases,list),'cases must be a list')
  if not isinstance(cases,list):return errors
  expected=load(B/'analyst/expected.json')['cases'];err(len(cases)==16 and all(isinstance(c,dict) for c in cases),'Expected 16 case objects')
  if not all(isinstance(c,dict) for c in cases):return errors
  err(sorted(str(c.get('id')) for c in cases)==sorted(expected),'Case IDs must occur once each')
  err(isinstance(data.get('closing_note'),str),'closing_note must be string')
  for c in cases:
   err(isinstance(c.get('instrument_rationale'),str),'instrument_rationale must be string')
   ps=c.get('probes');err(isinstance(ps,list),'probes must be a list')
   if not isinstance(ps,list):continue
   err(len(ps)==2 and all(isinstance(p,dict) for p in ps),'Expected two claim objects')
   if not all(isinstance(p,dict) for p in ps):continue
   err(sorted(str(p.get('id')) for p in ps)==['claim1','claim2'],'Claim IDs must occur once each')
   for p in ps:
    err(p.get('label') in LABELS,'Invalid claim label')
    for field in ['quote','reason']:err(isinstance(p.get(field),str),field+' must be string')
 return errors

def main():
 (B/'analysis').mkdir(exist_ok=True);jobs=load(B/'jobs.json');key=load(B/'analyst/expected.json');passages={c['id']:c['passage'] for c in load(B/'materials/test-cases.json')};runrows=[];attempts=[];probes=[];answers=[];valid={}
 for job in jobs:
  d=B/'outputs'/job['id'];candidates=[]
  for path in [d,d/'attempt-2']:
   if not (path/'metadata.json').exists():continue
   m=load(path/'metadata.json');attempts.append({'id':job['id'],'attempt':m['attempt'],'status':m['status'],'turn_completed':m.get('turn_completed',False),'input_sha256':m['input_sha256'],'response_sha256':sha(path/'response.txt') if (path/'response.txt').exists() else ''});candidates.append((path,m))
  errors=[];data=None;chosen=candidates[-1] if candidates else None
  if chosen:
   path,m=chosen
   if m.get('status')!='process_completed' or not m.get('turn_completed'):errors.append('No completed turn')
   if m.get('tool_items'):errors.append('Observed reviewer tool use')
   if not (path/'response.txt').exists():errors.append('No response')
   else:
    try:data=load(path/'response.txt')
    except (ValueError,UnicodeError):errors.append('Invalid JSON')
    else:errors.extend(validate(data,job))
   if len(candidates)>1:
    first=candidates[0][1]
    if first.get('turn_completed') or (candidates[0][0]/'response.txt').exists():errors.append('Forbidden retry after response')
  else:errors.append('Unattempted')
  eligible=bool(chosen) and not errors
  runrows.append({**{k:job[k] for k in ['id','batch','condition','repeat']},'attempts':len(candidates),'completed':bool(chosen and chosen[1].get('turn_completed')),'eligible':eligible,'errors':'; '.join(errors)})
  if not eligible:continue
  valid[job['id']]=data
  if job['batch']=='controlled':
   for c in data['cases']:
    for p in c['probes']:
     exp=key['cases'][c['id']][p['id']];quote=' '.join(p['quote'].split());found=bool(quote) and quote in ' '.join(passages[c['id']].split())
     probes.append({'id':job['id'],'condition':job['condition'],'repeat':job['repeat'],'case':c['id'],'family':c['id'][:-1],'claim':p['id'],'label':p['label'],'expected':exp['label'],'match':p['label']==exp['label'],'negative_conclusion':exp['negative_conclusion'],'unjustified_negative_support':exp['negative_conclusion'] and exp['label']!='Supported' and p['label']=='Supported','quote_found':found,'quote':p['quote'],'reason':p['reason']})
  elif job['condition'].startswith('mesa_'):
   for review in data['reviews']:
    for a in review['mesa_answers']:answers.append({'id':job['id'],'condition':job['condition'],'repeat':job['repeat'],'benchmark':review['benchmark'],'question':a['id'],'choice':a['choice'],'comment':a.get('comment') or ''})
 conditions=list(dict.fromkeys(j['condition'] for j in jobs));summary={'version':'accessibility-v1','planned':len(jobs),'attempted':sum(r['attempts']>0 for r in runrows),'physical_attempts':len(attempts),'eligible':sum(r['eligible'] for r in runrows),'conditions':{},'interpretation':'Descriptive repeated outputs of one model; not human use or independent observations.'}
 case_runs=[];family=[];paired=[];distributions=[];agreement=[]
 for condition in conditions:
  rr=[r for r in runrows if r['condition']==condition];ps=[p for p in probes if p['condition']==condition];neg=[p for p in ps if p['negative_conclusion'] and p['expected']!='Supported']
  summary['conditions'][condition]={'real_valid':sum(r['eligible'] and r['batch']=='real' for r in rr),'controlled_valid':sum(r['eligible'] and r['batch']=='controlled' for r in rr),'claim_answers':len(ps),'matches':sum(p['match'] for p in ps),'unjustified_negative_support':sum(p['unjustified_negative_support'] for p in neg),'negative_claim_opportunities':len(neg),'quote_substrings_found':sum(p['quote_found'] for p in ps)}
  for job in [j for j in jobs if j['condition']==condition and j['batch']=='controlled' and j['id'] in valid]:
   pj=[p for p in ps if p['id']==job['id']];case_runs.append({'id':job['id'],'condition':condition,'repeat':job['repeat'],'matches':sum(p['match'] for p in pj),'answers':len(pj)})
   for pair in key['pairs']:
    for claim,expected in pair['expected_pairs'].items():
     selected=[next(p for p in pj if p['case']==cid and p['claim']==claim) for cid in pair['cases']];labels=[p['label'] for p in selected]
     paired.append({'id':job['id'],'condition':condition,'family':pair['id'],'claim':claim,'expected_change':expected[0]!=expected[1],'observed_change':labels[0]!=labels[1],'both_expected':labels==expected})
  for pair in key['pairs']:
   pf=[p for p in ps if p['family']==pair['id']];family.append({'condition':condition,'family':pair['id'],'description':pair['family'],'matches':sum(p['match'] for p in pf),'answers':len(pf)})
  if condition.startswith('mesa_'):
   for bench in ['arc','designqa']:
    for q in range(1,26):
     selected=[a for a in answers if a['condition']==condition and a['benchmark']==bench and a['question']==q];counts=collections.Counter(a['choice'] for a in selected);distributions.append({'condition':condition,'benchmark':bench,'question':q,'answers':len(selected),**{c:counts[c] for c in CHOICES}})
     pairs=list(itertools.combinations(selected,2));agreement.append({'condition':condition,'benchmark':bench,'question':q,'matching_pairs':sum(a['choice']==b['choice'] for a,b in pairs),'pairs':len(pairs)})
   ar=[a for a in agreement if a['condition']==condition];dist=[d for d in distributions if d['condition']==condition];summary['conditions'][condition].update({'mesa_answers':sum(d['answers'] for d in dist),'variable_question_benchmark_pairs':sum(sum(d[c]>0 for c in CHOICES)>1 for d in dist),'matching_pairs':sum(a['matching_pairs'] for a in ar),'pairs':sum(a['pairs'] for a in ar)})
 table('runs.csv',runrows,['id','batch','condition','repeat','attempts','completed','eligible','errors']);table('attempts.csv',attempts,['id','attempt','status','turn_completed','input_sha256','response_sha256'])
 table('claims.csv',probes,['id','condition','repeat','case','family','claim','label','expected','match','negative_conclusion','unjustified_negative_support','quote_found','quote','reason']);table('case-runs.csv',case_runs,['id','condition','repeat','matches','answers']);table('families.csv',family,['condition','family','description','matches','answers']);table('paired-cases.csv',paired,['id','condition','family','claim','expected_change','observed_change','both_expected'])
 table('mesa-answers.csv',answers,['id','condition','repeat','benchmark','question','choice','comment']);table('mesa-distributions.csv',distributions,['condition','benchmark','question','answers',*CHOICES]);table('mesa-agreement.csv',agreement,['condition','benchmark','question','matching_pairs','pairs']);dump(B/'analysis/summary.json',summary)
 lines=['# Accessibility study: observed results','',f"Planned {summary['planned']}; attempted {summary['attempted']}; physical attempts {summary['physical_attempts']}; usable {summary['eligible']}.",'','| Method | Real conversations | Test-case conversations | Expected claim answers | Unjustified support for negative claims |','| --- | ---: | ---: | ---: | ---: |']
 for c,r in summary['conditions'].items():lines.append(f"| {c} | {r['real_valid']}/5 | {r['controlled_valid']}/5 | {r['matches']}/{r['claim_answers']} | {r['unjustified_negative_support']}/{r['negative_claim_opportunities']} |")
 lines+=['','These are repeated answers to assistant-prepared cases, not independent observations or human usability findings. Invalid outputs and every retained attempt are listed separately. Real review interpretations appear in the separate illustrative audit.']
 (B/'analysis/summary.md').write_text('\n'.join(lines)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

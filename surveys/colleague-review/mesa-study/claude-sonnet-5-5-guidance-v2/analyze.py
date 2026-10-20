#!/usr/bin/env python3
"""Offline descriptive analysis; does not repair responses or launch models."""
from pathlib import Path
import csv,json,collections,itertools,hashlib
import validation_helpers as V
B=Path(__file__).resolve().parent
CHOICES=V.CHOICES

def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(name,rows,fields):
 with (B/'analysis'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def main():
 jobs=load(B/'jobs.json');keys=load(B/'analyst/expected.json');runrows=[];attempts=[];claims=[];answers=[];reviews=[];notes=[];pairs=[];threadids=[]
 passages={batch:{c['id']:c['passage'] for c in load(B/'materials/test-cases.json')} for batch in ['cases']}
 for j in jobs:
  base={k:j[k] for k in ['id','batch','condition','role','repeat']};folder=B/'outputs'/j['id'];layouts,allowed,issues=V.attempt_layout(folder);parsed=[]
  for attempt,path in layouts:
   m=load(path/'metadata.json');errors=[];data=None;threadids+=m.get('thread_ids',[])
   if m.get('status')!='process_completed' or not m.get('turn_completed'):errors.append('No completed process and turn')
   if V.observations(path,m)['tool_events'] or V.observations(path,m)['recorded_actual_tool_items']:errors.append('Observed tool use')
   if not (path/'response.txt').exists():errors.append('No response')
   else:
    try:data=V.parse((path/'response.txt').read_text())
    except (ValueError,TypeError) as e:errors.append(str(e))
    if data is not None:
     try:errors+=V.validate(data,j,{} if j['batch']=='real' else keys[j['batch']]['cases'])
     except (ValueError,TypeError,KeyError,AttributeError) as e:errors.append('Malformed schema: '+str(e))
     if j['batch']=='real' and j['condition']=='mesa':
      for r in data.get('reviews',[]):
       if isinstance(r,dict):
        for a in r.get('mesa_answers',[]) if isinstance(r.get('mesa_answers'),list) else []:
         if isinstance(a,dict) and a.get('comment') is not None and not isinstance(a.get('comment'),str):errors.append('MESA comment must be text, empty, absent or null')
   errors+=issues
   row={**base,'attempt':attempt,'status':m.get('status'),'completed':bool(m.get('turn_completed')),'eligible':not errors,'errors':'; '.join(errors),'input_sha256':m.get('input_sha256'),'response_sha256':sha(path/'response.txt') if (path/'response.txt').exists() else ''}
   attempts.append(row);parsed.append((row,data))
  chosen=parsed[-1] if parsed else None
  if len(parsed)>1 and not allowed:raise ValueError('Forbidden retry '+j['id'])
  rr={**base,'attempts':len(parsed),'completed':bool(chosen and chosen[0]['completed']),'eligible':bool(chosen and chosen[0]['eligible']),'errors':chosen[0]['errors'] if chosen else 'Unattempted'};runrows.append(rr)
  if not rr['eligible']:continue
  d=chosen[1]
  if j['batch']=='real':
   for r in d['reviews']:
    reviews.append({**base,'benchmark':r['benchmark'],'review_json':json.dumps(r,ensure_ascii=False)})
    notes.append({**base,'benchmark':r['benchmark'],'closing_note':r['closing_note']})
    if j['condition']=='mesa':
     for a in r['mesa_answers']:answers.append({**base,'benchmark':r['benchmark'],'question':a['id'],'choice':a['choice'],'comment':a.get('comment') or ''})
  else:
   for c in d['cases']:
    for p in c['probes']:
     exp=keys[j['batch']]['cases'][c['id']][p['id']];quote=' '.join(p['quote'].split());found=bool(quote) and quote in ' '.join(passages[j['batch']][c['id']].split())
     claims.append({**base,'case':c['id'],'claim':p['id'],'label':p['label'],'expected':exp['label'],'match':p['label']==exp['label'],'quote_found':found,'negative_opportunity':bool(exp.get('negative_conclusion') and exp['label']!='Supported'),'unjustified_negative_support':bool(exp.get('negative_conclusion') and exp['label']!='Supported' and p['label']=='Supported'),'quote':p['quote'],'reason':p['reason']})
   selected=[p for p in claims if p['id']==j['id']]
   for pair in keys['cases']['comparisons']:
    selected_pair=[next(p for p in selected if (p['case'],p['claim'])==tuple(ref)) for ref in pair['refs']]
    actual=[p['label'] for p in selected_pair];expected=pair['expected']
    pairs.append({**base,'family':pair['family'],'claim':' / '.join(ref[1] for ref in pair['refs']),'expected_change':expected[0]!=expected[1],'observed_change':actual[0]!=actual[1],'both_expected':actual==expected})
 summary={'planned':len(jobs),'attempted':sum(r['attempts']>0 for r in runrows),'attempts':len(attempts),'completed':sum(r['completed'] for r in runrows),'eligible':sum(r['eligible'] for r in runrows),'unique_thread_ids':len(set(threadids)),'groups':[],'mesa':{},'cases':{},'note':'One model; repeated conversations and claims are dependent. OpenAI Codex revised guidance and analyzed this follow-up; reviewer is Claude Sonnet 5.5. No human benefit or independent correctness claim.'}
 for batch,condition,role in itertools.product(['real','cases'],['mesa','efpa','ordinary'],['neutral']):
  rr=[r for r in runrows if (r['batch'],r['condition'],r['role'])==(batch,condition,role)];cc=[p for p in claims if (p['batch'],p['condition'],p['role'])==(batch,condition,role)]
  summary['groups'].append({'batch':batch,'condition':condition,'role':role,'planned':len(rr),'completed':sum(r['completed'] for r in rr),'eligible':sum(r['eligible'] for r in rr),'claim_answers':len(cc),'matches':sum(p['match'] for p in cc)})
 distributions=[];agreement=[]
 for bench,q in itertools.product(['arc','designqa'],range(1,26)):
  aa=[a for a in answers if (a['benchmark'],a['question'])==(bench,q)]
  for role in ['all','neutral']:
   aa_role=[a for a in aa if role=='all' or a['role']==role];counts=collections.Counter(a['choice'] for a in aa_role)
   distributions.append({'role':role,'benchmark':bench,'question':q,'answers':len(aa_role),**{c:counts[c] for c in CHOICES}})
   if role!='all':
    ap=list(itertools.combinations(aa_role,2));agreement.append({'role':role,'benchmark':bench,'question':q,'matches':sum(a['choice']==b['choice'] for a,b in ap),'pairs':len(ap)})
 for role in ['all','neutral']:
  dd=[d for d in distributions if d['role']==role];ag=[a for a in agreement if role=='all' or a['role']==role]
  summary['mesa'][role]={'answers':sum(d['answers'] for d in dd),'variable_pairs':sum(sum(d[c]>0 for c in CHOICES)>1 for d in dd),'matching_answer_pairs':sum(a['matches'] for a in ag),'answer_pairs':sum(a['pairs'] for a in ag)}
 for batch in ['cases']:
  summary['cases'][batch]={}
  for condition in ['mesa','efpa','ordinary']:
   cc=[p for p in claims if (p['batch'],p['condition'])==(batch,condition)];pp=[p for p in pairs if (p['batch'],p['condition'])==(batch,condition)]
   summary['cases'][batch][condition]={'matches':sum(p['match'] for p in cc),'answers':len(cc),'quotes_found':sum(p['quote_found'] for p in cc),'paired_matches':sum(p['both_expected'] for p in pp),'paired_comparisons':len(pp),'negative_opportunities':sum(p['negative_opportunity'] for p in cc),'unjustified_negative_support':sum(p['unjustified_negative_support'] for p in cc)}
 for name,rows,fields in [('runs',runrows,['id','batch','condition','role','repeat','attempts','completed','eligible','errors']),('attempts',attempts,['id','batch','condition','role','repeat','attempt','status','completed','eligible','errors','input_sha256','response_sha256']),('claims',claims,['id','batch','condition','role','repeat','case','claim','label','expected','match','quote_found','negative_opportunity','unjustified_negative_support','quote','reason']),('paired-cases',pairs,['id','batch','condition','role','repeat','family','claim','expected_change','observed_change','both_expected']),('mesa-answers',answers,['id','batch','condition','role','repeat','benchmark','question','choice','comment']),('mesa-distributions',distributions,['role','benchmark','question','answers',*CHOICES]),('mesa-agreement',agreement,['role','benchmark','question','matches','pairs']),('reviews',reviews,['id','batch','condition','role','repeat','benchmark','review_json']),('closing-notes',notes,['id','batch','condition','role','repeat','benchmark','closing_note'])]:table(name+'.csv',rows,fields)
 case_runs=[];families=[]
 for j in jobs:
  if j['batch']=='real':continue
  cc=[p for p in claims if p['id']==j['id']];case_runs.append({k:j[k] for k in ['id','batch','condition','role','repeat']}|{'answers':len(cc),'matches':sum(p['match'] for p in cc)})
 for batch in ['cases']:
  for condition in ['mesa','efpa','ordinary']:
   caseids=keys[batch]['cases']
   for cid in caseids:
    cc=[p for p in claims if (p['batch'],p['condition'],p['case'])==(batch,condition,cid)];families.append({'batch':batch,'condition':condition,'case':cid,'answers':len(cc),'matches':sum(p['match'] for p in cc)})
 table('case-runs.csv',case_runs,['id','batch','condition','role','repeat','answers','matches']);table('case-families.csv',families,['batch','condition','case','answers','matches'])
 (B/'analysis/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 text=['# Observed MESA study results','',f"Planned {summary['planned']}; attempted {summary['attempted']}; completed {summary['completed']}; usable {summary['eligible']}; physical attempts {summary['attempts']}.",'','| Batch | Method | Instruction group | Usable/planned | Expected answers matched |','| --- | --- | --- | ---: | ---: |']
 text += [f"| {g['batch']} | {g['condition']} | {g['role']} | {g['eligible']}/{g['planned']} | {g['matches']}/{g['claim_answers']} |" for g in summary['groups']]
 text+=['','Repeated labels are not independent observations; the expected answers are assistant-prepared, not an independent review correctness standard. Invalid responses remain saved, excluded without repair or replacement.']
 (B/'analysis/summary.md').write_text('\n'.join(text)+'\n');print(json.dumps({k:v for k,v in summary.items() if k!='groups'},indent=2))
if __name__=='__main__':main()

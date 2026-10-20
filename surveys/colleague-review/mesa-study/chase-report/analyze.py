"""Reproduce the CHASE reporting selection from saved responses; never launch models."""
from pathlib import Path
import collections,csv,hashlib,itertools,json,sys
B=Path(__file__).resolve().parent;S=B.parent
OLD=S/'claude-sonnet-5-5';MESA=S/'claude-sonnet-5-5-guidance-v2'
sys.path.insert(0,str(MESA))
import validation_helpers as V
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def write_csv(name,rows):
 if rows:
  with (B/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 expected=load(MESA/'analyst/expected.json')['cases'];cases={c['id']:c['passage'] for c in load(MESA/'materials/test-cases.json')}
 jobs=[(MESA,j) for j in load(MESA/'jobs.json')]+[(OLD,j) for j in load(OLD/'jobs.json') if j['condition']!='mesa']
 manifest=[];runs=[];attempts=[];claims=[];answers=[];pairs=[];notes=[];selected=[]
 for root,j in jobs:
  source=str(root.relative_to(S));base={k:j[k] for k in ['id','batch','condition','repeat']};base['source']=source
  assert sha(root/j['input'])==j['sha256']
  folder=root/'outputs'/j['id'];paths,allowed,issues=V.attempt_layout(folder);assert not issues,issues
  for number,p in paths:
   meta=load(p/'metadata.json');assert not V.observations(p,meta)['tool_events'];assert meta['init_tools']==[] and meta['init_mcp_servers']==[] and meta['reported_model']=='claude-sonnet-5-5'
   for name,h in meta['output_files_sha256'].items():assert sha(p/name)==h
   attempts.append(dict(base,attempt=number,completed=meta['turn_completed'],status=meta['status']))
  number,p=paths[-1];meta=load(p/'metadata.json');data=None;errors=[]
  try:
   data=V.parse((p/'response.txt').read_text());errors=V.validate(data,j,expected['cases'] if j['batch']=='cases' else {})
  except (ValueError,TypeError) as e:errors=[str(e)]
  eligible=meta['turn_completed'] and not errors
  runs.append(dict(base,attempts=len(paths),completed=meta['turn_completed'],eligible=eligible,errors='; '.join(errors)))
  manifest.append(dict(base,input=str((root/j['input']).relative_to(S)),input_sha256=j['sha256'],response=str((p/'response.txt').relative_to(S)),response_sha256=sha(p/'response.txt'),chosen_attempt=number))
  if not eligible:continue
  if j['batch']=='real':
   for r in data['reviews']:
    notes.append(dict(base,benchmark=r['benchmark'],closing_note=r['closing_note']))
    if j['repeat']==1:selected.append(dict(base,review=r))
    if j['condition']=='mesa':
     answers += [dict(base,benchmark=r['benchmark'],question=a['id'],choice=a['choice'],comment=a.get('comment') or '') for a in r['mesa_answers']]
  else:
   probe_map={}
   for c in data['cases']:
    for probe in c['probes']:
     key=expected['cases'][c['id']][probe['id']];alt='Contradicted' if (c['id'],probe['id'])==('P6B','claim1') else key['label']
     row=dict(base,case=c['id'],claim=probe['id'],label=probe['label'],expected=key['label'],match=probe['label']==key['label'],alternative_match=probe['label']==alt,quote_found=V.norm(probe['quote']) in V.norm(cases[c['id']]),negative_opportunity=bool(key.get('negative_conclusion') and key['label']!='Supported'),quote=probe['quote'],reason=probe['reason'])
     claims.append(row);probe_map[(c['id'],probe['id'])]=probe['label']
   for pair in expected['comparisons']:
    actual=[probe_map[tuple(ref)] for ref in pair['refs']];e=pair['expected']
    pairs.append(dict(base,family=pair['family'],change_matches=(actual[0]!=actual[1])==(e[0]!=e[1]),both_expected=actual==e))
 distributions=[];matches=total=0
 for bench,q in itertools.product(['arc','designqa'],range(1,26)):
  aa=[a for a in answers if (a['benchmark'],a['question'])==(bench,q)];counts=collections.Counter(a['choice'] for a in aa);pp=list(itertools.combinations(aa,2));n=sum(x['choice']==y['choice'] for x,y in pp);matches+=n;total+=len(pp)
  distributions.append(dict(benchmark=bench,question=q,**{c:counts[c] for c in V.CHOICES},variable=len(counts)>1,matching_pairs=n,pairs=len(pp)))
 groups={}
 for method in ['mesa','efpa','ordinary']:
  cc=[c for c in claims if c['condition']==method];rr=[r for r in runs if r['condition']==method];pp=[p for p in pairs if p['condition']==method]
  groups[method]={'real_eligible':sum(r['eligible'] and r['batch']=='real' for r in rr),'cases_eligible':sum(r['eligible'] and r['batch']=='cases' for r in rr),'matches':sum(c['match'] for c in cc),'answers':len(cc),'sensitivity_matches':sum(c['alternative_match'] for c in cc),'all_49':sum(sum(c['match'] for c in cc if c['id']==r['id'])==49 for r in rr if r['batch']=='cases' and r['eligible']),'both_expected':sum(p['both_expected'] for p in pp),'comparisons':len(pp)}
 summary={'conversations':len(runs),'completed':sum(r['completed'] for r in runs),'eligible':sum(r['eligible'] for r in runs),'attempts':len(attempts),'groups':groups,'claim_answers':len(claims),'matches':sum(c['match'] for c in claims),'mismatches':sum(not c['match'] for c in claims),'mismatch_cases':dict(collections.Counter(c['case'] for c in claims if not c['match'])),'contrast_matches':sum(p['change_matches'] for p in pairs),'contrasts':len(pairs),'both_expected':sum(p['both_expected'] for p in pairs),'quotes_found':sum(c['quote_found'] for c in claims),'negative_opportunities':sum(c['negative_opportunity'] for c in claims),'negative_supported':sum(c['negative_opportunity'] and c['label']=='Supported' for c in claims),'mesa':{'answers':len(answers),'choices':dict(collections.Counter(a['choice'] for a in answers)),'variable_pairs':sum(d['variable'] for d in distributions),'no_not_sure_pairs':sum(d['No']>0 and d['Not sure']>0 for d in distributions),'matching_pairs':matches,'pairs':total}}
 for name,rows in [('runs',runs),('attempts',attempts),('claims',claims),('mesa-answers',answers),('mesa-distributions',distributions),('paired-cases',pairs),('closing-notes',notes)]:write_csv(name+'.csv',rows)
 (B/'selection.json').write_text(json.dumps({'selection_rule':'All ten MESA jobs from claude-sonnet-5-5-guidance-v2; all twenty EFPA-TRM/general-instruction jobs from claude-sonnet-5-5. No response-based selection. Reporting selection assembled after development testing; method batches sequential.','jobs':manifest},indent=2)+'\n')
 (B/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(B/'selected-reviews.json').write_text(json.dumps(selected,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

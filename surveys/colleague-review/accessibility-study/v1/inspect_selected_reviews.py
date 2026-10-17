from pathlib import Path
import json,hashlib,sys
B=Path('surveys/colleague-review/accessibility-study/v1');sys.path.insert(0,str(B.resolve()));from analyze import validate
conds=['mesa_original','mesa_revised','efpa','ordinary'];rows=[];notes=[]
def strings(v,path=''):
 if isinstance(v,str):yield path,v
 elif isinstance(v,list):
  for i,x in enumerate(v):yield from strings(x,f'{path}[{i}]')
 elif isinstance(v,dict):
  for k,x in v.items():yield from strings(x,f'{path}.{k}' if path else k)
def quote(review,needle):
 hits=[(p,s) for p,s in strings(review) if needle.casefold() in s.casefold()];assert hits,needle;return {'field':hits[0][0],'text':hits[0][1]}
# Notes refer exclusively to the first neutral response, not all repetitions.
specs={
'mesa_original':{
'arc':[
('addressed','Broader claims are left unresolved; grid-task performance remains the stated interpretation.','broader intelligence claims remain'),
('addressed','The review separates input-level success from a completely solved multi-input problem.','Official scores average within-problem'),
('addressed','Human matching is not treated as evidence of AI repeatability.','Human difficulty matching concerns people'),
('partly addressed','Exposure safeguards and public accessibility are recorded; the review does not explicitly distinguish model-specific observed exposure.','Hidden-data agreements'),
('addressed','Public access and incomplete effects of corrections on old scores remain visible.','score effects are incomplete'),
('partly addressed','Different evaluation routes and the human-study pool are considered; no explicit warning about generalizing human-background findings appears.','human findings include a larger pool')],
'designqa':[
('addressed','The review limits wider competence claims and notes one-rulebook coverage.','one rulebook and uneven groups'),
('addressed','Checks of provided answers and marking are separated; missing reviewer disagreement rates are explicitly named.','Reviewer disagreement rates'),
('addressed','Unequal counts and uncertainty about combined-score interpretations are recorded.','Equal group weighting is described'),
('addressed','Changed passages are separated from identical-condition repetition; close-ranking uncertainty remains, without the numerical 6.25-point example.','Five passage sets change the inputs'),
('addressed','The always-yes route is described as an opportunity, without asserting that a tested AI used it; exposure remains uncertain.','allowing an always-yes strategy'),
('addressed','Missing historical reproduction, permissions and change records are recorded.','Complete historical reproduction records')]
},
'mesa_revised':{
'arc':[
('addressed','Grid success is retained while broader abilities remain unestablished.','Broader reasoning claims'),
('addressed','Fractional problem scoring is distinguished from fully solved problems.','partial completion of a multi-input problem'),
('addressed','The closing note distinguishes human matching from AI difficulty; repeated-score findings remain missing.','human difficulty matching does not establish'),
('addressed','The review identifies safeguards without treating exposure as excluded.','prior exposure have been excluded'),
('addressed','Hidden access and missing recalculation of older scores are retained.','does not recalculate every affected'),
('partly addressed','Evaluation routes and human-study scope are retained, without an explicit human-background-to-AI-fairness warning.','different testing routes and human-only')],
'designqa':[
('addressed','The review retains the one-rulebook restriction and limits broader task coverage.','one rulebook and uneven groups'),
('partly addressed','The review separates checking supplied answers from testing marking, but does not explicitly request the additional reviewers\' agreement rate.','Additional reviewers checked manually'),
('addressed','Unequal counts, weights and separate-score interpretations are retained.','Justification for equal group weights'),
('addressed','Changed passages are separated from identical-condition repetition; close-comparison uncertainty remains, without the numerical 6.25-point example.','Five passage-set trials change the inputs'),
('addressed','The always-yes route remains an opportunity rather than reported observed use; prior exposure remains unresolved.','allowing an always-yes response'),
('addressed','Historical records, revisions and reuse are separated from a prohibition on reuse.','does not establish prohibition')]
},
'ordinary':{
'arc':[
('addressed','The review limits what grid scores say about wider intelligence.','broader meanings remain unvalidated'),
('addressed','It explicitly separates average input success from a fully solved problem.','not necessarily complete problem solution'),
('addressed','It separates human difficulty matching from AI equivalence and repeated-score evidence.','Similar difficulty'),
('addressed','Exposure precautions are not treated as proof that prior exposure is absent.','measuring each system\'s prior exposure'),
('addressed','Public access, corrections and unupdated scores are considered.','Corrections do not trigger recalculation'),
('partly addressed','Routes and human matching are discussed; no explicit human-background fairness warning appears.','human performance used in set selection')],
'designqa':[
('addressed','One-rulebook task relevance is separated from broader competence.','general engineering competence'),
('addressed','Checking supplied answers and marking are separated, with reviewer disagreement explicitly missing.','Reviewer disagreement rates'),
('addressed','The review distinguishes equal weighting from an established single ability.','not accuracy across all questions'),
('addressed','Repeated conditions and changed passages are separated, and the 6.25-point example is retained.','6.25 percentage points'),
('addressed','The review explicitly denies evidence that a tested AI used the possible always-yes route.','no evidence shows a tested AI used it'),
('addressed','Historical information, permissions and score changes are identified as gaps.','Complete historical inputs')]
}}
specs['efpa']={
'arc':[
('addressed','The review limits its favorable interpretation to observed grid solving.','Adequate only for narrow observed'),
('addressed','It explicitly separates partial multi-input credit from a partly correct grid.','A partly correct grid earns no credit'),
('addressed','Human development counts and matching are not treated as an AI repetition sample.','The 407 people and 515 sessions'),
('addressed','The review retains precautions without treating unintended routes or exposure as eliminated.','Design intentions and monitoring'),
('addressed','Public access, changed items and incomplete historical score updates are retained.','Historical scores may not reflect'),
('addressed','The review explicitly rejects using human demographic findings to establish fair AI comparisons.','Human demographic findings cannot')],
'designqa':[
('addressed','Practical content is distinguished from broader engineering coverage.','one rulebook, narrow coverage'),
('addressed','Checking answers and operational marking are separated, and missing review agreement is explicit.','no development-review agreement coefficient'),
('addressed','The review separates equal weighting from evidence that groups measure distinct skills.','Distinct underlying skills and cross-system'),
('addressed','It separates changed inputs from identical-condition repeatability and retains the 6.25-point example.','6.25 percentage points'),
('addressed','The review distinguishes a possible all-yes route from observed use and identifies exposure gaps.','does not establish that any tested AI used'),
('addressed','Missing historical and permission records are not treated as proof that reuse is prohibited.','does not prove reuse is prohibited')]
}
for c in conds:
 p=B/f'outputs/real-{c}-neutral-1/response.txt'
 if not p.exists():continue
 data=json.loads(p.read_text());errors=validate(data,{'batch':'real','condition':c});notes.append({'condition':c,'source':str(p.relative_to(B)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'schema_errors':errors,'selected_invalid_not_replaced':bool(errors)})
 if c not in specs:continue
 for r in data['reviews']:
  for i,(status,note,needle) in enumerate(specs[c][r['benchmark']],1):rows.append({'condition':c,'benchmark':r['benchmark'],'point':i if r['benchmark']=='arc' else i+6,'status':status,'interpretation':note,'quotation':quote(r,needle)})
(B/'analysis/illustrative-reviews.json').write_text(json.dumps({'scope':'Same-assistant interpretation of selected first responses. Not general rates or independently established correctness.','sources':notes,'points':rows},ensure_ascii=False,indent=2)+'\n');print('Inspected',len(notes)*2,'selected reviews; saved',len(rows),'checklist observations.')

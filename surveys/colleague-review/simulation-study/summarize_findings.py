#!/usr/bin/env python3
"""Produce traceable descriptive facts for writing; never generate prose verdicts."""
from pathlib import Path
import argparse,collections,csv,json,statistics

def rows(p):
    with p.open() as f:return list(csv.DictReader(f))
def truth(v):return v=='True'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();root=a.root
    an=root/'analysis';summary=json.loads((an/'summary.json').read_text());runs=rows(an/'runs.csv')
    facts={'series_summary':summary,'controlled_by_condition':[],'mesa_agreement_by_role':[], 'variable_questionnaire_items':[], 'execution':{}}
    scores=rows(an/'controlled_run_scores.csv')
    for condition in ['mesa','efpa','ordinary']:
        valid=[r for r in scores if r['condition']==condition and truth(r['eligible'])]
        n=sum(int(r['probe_denominator']) for r in valid);matches=sum(int(r['matches']) for r in valid)
        facts['controlled_by_condition'].append({'condition':condition,'valid_sessions':len(valid),'judgments':n,'matches':matches,'per_session_matches':[int(r['matches']) for r in valid], 'all_expected':bool(valid) and all(r['matches']==r['probe_denominator'] for r in valid)})
    agree=rows(an/'mesa_agreement.csv')
    for role in ['neutral','newcomer','research_assistant','benchmark_reviewer']:
        rs=[r for r in agree if r['comparison']=='within_role' and r['roles']==role]
        n=sum(int(r['pair_denominator']) for r in rs);m=sum(int(r['matches']) for r in rs)
        facts['mesa_agreement_by_role'].append({'role':role,'matching_pairs':m,'all_pairs':n,'fraction':m/n if n else None,'scope':'Descriptive output agreement over fixed question/benchmark combinations; not a benchmark-quality score.'})
    dist=rows(an/'mesa_distributions.csv'); choices=['Yes','Partly','No','Not sure','Not applicable']
    pooled=collections.defaultdict(collections.Counter)
    within_variable=0
    for r in dist:
        cs={c:int(r[c]) for c in choices}; pooled[(r['benchmark'],int(r['question']))].update(cs)
        if sum(n>0 for n in cs.values())>1:within_variable+=1
    for (b,q),cs in pooled.items():
        n=sum(cs.values())
        if sum(x>0 for x in cs.values())>1:facts['variable_questionnaire_items'].append({'benchmark':b,'question':q,'counts':dict(cs),'valid_answers':n,'modal_fraction':max(cs.values())/n if n else None})
    facts['variable_questionnaire_items'].sort(key=lambda r:(r['modal_fraction'],r['benchmark'],r['question']))
    facts['within_role_variable_question_benchmark_combinations']=within_variable
    facts['total_within_role_question_benchmark_combinations']=len(dist)
    times=[];statuses=collections.Counter()
    for p in (root/'outputs').rglob('metadata.json'):
        m=json.loads(p.read_text());statuses[m['status']]+=1
        if m.get('started_at'):times.append(m['started_at'])
        if m.get('finished_at'):times.append(m['finished_at'])
    facts['execution']={'first_utc':min(times) if times else None,'last_utc':max(times) if times else None,'status_counts':dict(statuses)}
    facts['writing_cautions']=['Do not replace planned with observed counts until all jobs are attempted.','Controlled keys are assistant-defined and not independently validated.','Role repetitions and item judgments are dependent.','A high exact-match rate on simple probes does not validate all 25 questions.','A missing source-ID mention is an audit aid, not proof an item was not addressed.']
    (an/'writing-facts.json').write_text(json.dumps(facts,indent=2)+'\n')
    print(json.dumps({'eligible_runs':summary['eligible_runs'],'controlled':facts['controlled_by_condition'],'agreement':facts['mesa_agreement_by_role'],'variable_items':len(facts['variable_questionnaire_items'])},indent=2))
if __name__=='__main__':main()

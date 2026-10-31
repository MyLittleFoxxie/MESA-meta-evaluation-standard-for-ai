"""Analyze the saved Claude batch responses and compare them with the saved Codex batch. No model calls."""
import json,sys
from pathlib import Path
C=Path(__file__).resolve().parent;R=C.parent
sys.path.insert(0,str(R))
from analyze import analyze,codex_batch,parse_claude_events,write_csv
CRITERIA=[f'{g}{i}' for g in 'AB' for i in range(1,6)]
def claude_batch():
 return {'name':'claude','jobs':json.loads((C/'jobs.json').read_text())['jobs'],'outputs':C/'outputs','analysis':C/'analysis','parse':parse_claude_events,'caption':'Claude batch execution accounting.','ratings_caption':'Claude batch: judgments per criterion and input over six usable responses per input (IE: insufficient evidence; NA: not applicable).','note':{'codex':'earlier batch; see ../analysis','requested_model':'claude-fable-5-1','effort':'medium'}}
def main():
 summary,claude_jobs,claude_delivered=analyze(claude_batch())
 _,codex_jobs,codex_delivered=analyze(codex_batch())
 rows=[]
 for b in ['humaneval','truthfulqa','designqa']:
  for c in ['documents','repository']:
   for n in [1,2]:
    j=f'{b}-{c}-{n}'
    if j in claude_delivered and j in codex_delivered:
     for i in CRITERIA:
      x=codex_jobs[j][i];y=claude_jobs[j][i]
      rows.append({'benchmark':b,'condition':c,'repeat':n,'criterion':i,'codex_status':x['status'],'codex_rating':x['rating'],'claude_status':y['status'],'claude_rating':y['rating'],'status_match':x['status']==y['status'],'match':(x['status'],x['rating'])==(y['status'],y['rating'])})
 if rows:write_csv(C/'analysis','cross-batch.csv',rows,list(rows[0]))
 by_criterion={i:[r for r in rows if r['criterion']==i] for i in CRITERIA}
 by_condition={c:[r for r in rows if r['condition']==c] for c in ['documents','repository']}
 cross={'paired_judgments':len(rows),'matches':sum(r['match'] for r in rows),'status_matches':sum(r['status_match'] for r in rows),'by_criterion':{i:{'pairs':len(v),'matches':sum(r['match'] for r in v)} for i,v in by_criterion.items()},'by_condition':{c:{'pairs':len(v),'matches':sum(r['match'] for r in v)} for c,v in by_condition.items()},'note':'Descriptive counts over the same benchmark, condition and repetition in two sequential batches. Not a provider ranking, not an accuracy estimate.'}
 (C/'analysis/cross-batch.json').write_text(json.dumps(cross,indent=2)+'\n')
 tex='\\begin{table}[t]\n\\caption{Judgments matching in status and rating between the Codex and Claude batches for the same benchmark, input and repetition.}\n\\label{tab:cross-batch}\n\\centering\\begin{tabular}{lrr}\\toprule\nCriterion & Matches & Pairs \\\\\n\\midrule\n'
 for i in CRITERIA:tex+=f"{i} & {cross['by_criterion'][i]['matches']} & {cross['by_criterion'][i]['pairs']} \\\\\n"
 tex+='\\midrule\n'
 for c,label in [('documents','Input 1 (paper and README)'),('repository','Input 2 (with repository text)')]:tex+=f"{label} & {cross['by_condition'][c]['matches']} & {cross['by_condition'][c]['pairs']} \\\\\n"
 tex+=f"All & {cross['matches']} & {cross['paired_judgments']} \\\\\n\\bottomrule\\end{{tabular}}\n\\end{{table}}\n"
 tex+=f"Across the same benchmark, input and repetition, {cross['matches']} of {cross['paired_judgments']} paired judgments matched in both status and rating between the two batches, and {cross['status_matches']} matched in status. The batches ran at different times with different providers, models, command line tools and harness settings, so these counts describe agreement between two configurations and do not rank them.\n"
 (C/'analysis/cross-batch.tex').write_text(tex)
 codex=json.loads((R/'analysis/summary.json').read_text())
 ex='\\begin{table}[t]\n\\caption{Execution accounting for both batches.}\n\\label{tab:execution}\n\\centering\\begin{tabular}{lrr}\\toprule\nMeasure & Codex & Claude \\\\\n\\midrule\n'
 for label,key in [('Planned main sessions','planned_main'),('Attempted main sessions','attempted_main'),('Completed main responses','completed_main'),('Structurally usable responses','valid_main'),('Input delivered','condition_delivered_main'),('Main criterion judgments','main_judgments'),('Pilot attempts','pilot_attempts'),('All physical attempts','physical_attempts'),('Repeat pairs matching','repeat_matches'),('Input pairs matching','access_matches'),('Evidence citations','citations'),('Citations to allowed existing sources','allowed_existing_sources'),('Exact quote matches','exact_quotes'),('Whitespace normalized quote matches','whitespace_quotes'),('Locators that resolve','locators_resolve')]:ex+=f"{label} & {codex[key]} & {summary[key]} \\\\\n"
 ex+='\\bottomrule\\end{tabular}\n\\end{table}\n'
 (C/'analysis/execution.tex').write_text(ex)
 print(json.dumps({**summary,'cross_batch_matches':cross['matches'],'cross_batch_pairs':cross['paired_judgments']}))
if __name__=='__main__':main()

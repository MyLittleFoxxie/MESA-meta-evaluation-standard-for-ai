"""Analyze saved responses only. Never calls a model or repairs output.

The module is shared by the Codex batch (run as a script) and the Claude batch (claude/analyze.py).
Each batch supplies its own job list, output directory, analysis directory and event parser.
"""
import csv,json,re
from pathlib import Path
from validate import validate
R=Path(__file__).resolve().parent
SOURCE_TOOLS=['list_files','read_file']
def write_csv(folder,name,rows,fields):
 with (folder/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def norm(s):return re.sub(r'\s+',' ',s).strip()
def read_events(path):
 events=[]
 for line in path.read_text().splitlines():
  try:events.append(json.loads(line))
  except ValueError:pass
 return events
def parse_codex_events(events):
 """Codex exec JSON events: completed MCP tool call items and turn usage."""
 calls=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='mcp_tool_call']
 calls=[{'server':i.get('server'),'tool':i.get('tool'),'ok':i.get('status')=='completed' and not i.get('error'),'failed':i.get('status')=='failed' or bool(i.get('error'))} for i in calls]
 other=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type') in ['command_execution','web_search','file_change']]
 usages=[e['usage'] for e in events if e.get('type')=='turn.completed' and 'usage' in e]
 usage=None
 if usages:usage={'input':sum(u['input_tokens'] for u in usages),'output':sum(u['output_tokens'] for u in usages)}
 return calls,other,usage
def parse_claude_events(events):
 """Claude Code stream-json events: assistant tool_use blocks, matching tool_result blocks and the result usage.

 StructuredOutput is the response delivery mechanism, not a tool. Input tokens sum uncached, cache creation and cache read tokens.
 """
 results={}
 for e in events:
  if e.get('type')=='user':
   for c in e.get('message',{}).get('content',[]) or []:
    if isinstance(c,dict) and c.get('type')=='tool_result':results[c.get('tool_use_id')]=c
 calls=[];other=[]
 for e in events:
  if e.get('type')!='assistant':continue
  for c in e.get('message',{}).get('content',[]) or []:
   if not isinstance(c,dict) or c.get('type')!='tool_use':continue
   name=c.get('name','')
   if name=='StructuredOutput':continue
   r=results.get(c.get('id'))
   if name.startswith('mcp__'):
    parts=name.split('__',2);server=parts[1] if len(parts)>2 else None;tool=parts[2] if len(parts)>2 else name
    calls.append({'server':server,'tool':tool,'ok':r is not None and not r.get('is_error'),'failed':r is None or bool(r.get('is_error'))})
   else:other.append({'tool':name})
 usage=None
 for e in events:
  if e.get('type')=='result' and isinstance(e.get('usage'),dict):
   u=e['usage'];usage={'input':u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0),'output':u.get('output_tokens',0)}
 return calls,other,usage
def analyze(batch):
 """Analyze one batch. batch keys: name, jobs, outputs, analysis, parse, caption, note."""
 A=batch['analysis'];A.mkdir(exist_ok=True)
 jobs=batch['jobs'];runs=[];answers=[];quotes=[];byjob={};attempts=[]
 refs={(x['benchmark'],x['condition'],x['criterion']):x for x in json.loads((R/'analyst/references.json').read_text())}
 for job in jobs:
  paths=sorted((batch['outputs']/job['id']).glob('attempt-*'))
  row={**job,'attempted':bool(paths),'completed':False,'valid':False,'condition_delivered':False,'successful_source_calls':0,'failed_source_calls':0,'input_tokens':None,'output_tokens':None,'elapsed_seconds':None,'errors':''}
  if not paths:runs.append(row);continue
  p=paths[-1];meta=json.loads((p/'metadata.json').read_text());row['elapsed_seconds']=meta.get('elapsed_seconds')
  for pa in paths:
   m=json.loads((pa/'metadata.json').read_text());attempts.append({'job':job['id'],'phase':job['phase'],'attempt':pa.name,'status':m['status'],'exit_code':m.get('exit_code'),'started_utc':m['started_utc']})
  calls,other,usage=batch['parse'](read_events(p/'events.jsonl'))
  row['successful_source_calls']=sum(c['ok'] for c in calls)
  row['failed_source_calls']=sum(c['failed'] for c in calls)
  violations=[c for c in calls if c.get('server')!='benchmark' or c.get('tool') not in SOURCE_TOOLS]+other
  if job['condition']=='documents' and calls:violations+=calls
  if usage:row['input_tokens']=usage['input'];row['output_tokens']=usage['output']
  try:
   data=json.loads((p/'response.txt').read_text());row['completed']=True;errors=validate(data)
  except Exception as e:data=None;errors=[str(e)]
  if violations:errors.append('tool boundary violation')
  row['valid']=not errors;row['errors']='; '.join(errors)
  row['condition_delivered']=not violations and (job['condition']=='documents' or row['successful_source_calls']>0)
  runs.append(row)
  if errors:continue
  byjob[job['id']]={j['id']:j for j in data['judgments']}
  for j in data['judgments']:
   ref=refs.get((job['benchmark'],job['condition'],j['id']))
   label={'status':j['status'],'rating':j['rating']}
   answers.append({'job':job['id'],'phase':job['phase'],'benchmark':job['benchmark'],'condition':job['condition'],'repeat':job['repeat'],'criterion':j['id'],'status':j['status'],'rating':j['rating'],'reference_match':label==ref['expected'] if ref else None,'alternative_match':label in [ref['expected']]+ref['alternatives'] if ref else None,'reason':j['reason'],'missing':j['missing'],'checks':j['checks']})
   for e in j['evidence']:
    name=e['source'];root=(R/'sources'/job['benchmark']).resolve();candidate=(root/name).resolve()
    # Resolve an unprefixed repository path without changing the raw response.
    if not candidate.is_file() and not Path(name).is_absolute() and (root/'repository'/name).is_file():
     name='repository/'+name;candidate=(root/name).resolve()
    allowed=candidate.is_relative_to(root) and (name=='paper.txt' or (name.startswith('repository/') and (job['condition']=='repository' or Path(name).name.lower().startswith('readme'))))
    exists=allowed and candidate.is_file();exact=normalized=False;locator='unresolved'
    if exists:
     try:
      text=candidate.read_text();exact=bool(e['quote']) and e['quote'] in text;normalized=bool(e['quote']) and norm(e['quote']) in norm(text)
      nums=re.search(r'(?i)lines?\s*(\d+)(?:\s*[-–]\s*(\d+))?',e['locator'])
      pages=re.search(r'(?i)(?:pdf\s*)?page\s*(\d+)',e['locator'])
      if nums:
       lo=int(nums[1]);hi=int(nums[2] or lo);locator='resolves' if 1<=lo<=hi<=len(text.splitlines()) else 'out_of_range'
      elif pages and name=='paper.txt':locator='resolves' if '[PDF page '+pages[1]+']' in text else 'out_of_range'
     except (UnicodeError,OSError):pass
    quotes.append({'job':job['id'],'phase':job['phase'],'criterion':j['id'],**e,'resolved_source':name,'source_exists_and_allowed':exists,'quote_exact':exact,'quote_whitespace_match':normalized,'locator':e['locator'],'locator_check':locator,'semantic_support':'not mechanically determined'})
 mainruns=[r for r in runs if r['phase']=='main'];usable=[r for r in mainruns if r['valid']];delivered={r['id'] for r in usable if r['condition_delivered']}
 transitions=[];repeats=[]
 for b in ['humaneval','truthfulqa','designqa']:
  for n in [1,2]:
   d=f'{b}-documents-{n}';q=f'{b}-repository-{n}'
   if d in delivered and q in delivered:
    for i,x in byjob[d].items():
     y=byjob[q][i];transitions.append({'benchmark':b,'repeat':n,'criterion':i,'documents_status':x['status'],'documents_rating':x['rating'],'repository_status':y['status'],'repository_rating':y['rating'],'match':(x['status'],x['rating'])==(y['status'],y['rating'])})
  for c in ['documents','repository']:
   x=f'{b}-{c}-1';y=f'{b}-{c}-2'
   if x in delivered and y in delivered:
    for i,j in byjob[x].items():
     k=byjob[y][i];repeats.append({'benchmark':b,'condition':c,'criterion':i,'match':(j['status'],j['rating'])==(k['status'],k['rating'])})
 qs=[q for q in quotes if q['phase']=='main'];ans=[a for a in answers if a['phase']=='main']
 summary={'batch':batch['name'],'planned_main':12,'attempted_main':sum(r['attempted'] for r in mainruns),'completed_main':sum(r['completed'] for r in mainruns),'valid_main':len(usable),'condition_delivered_main':len(delivered),'physical_attempts':len(attempts),'pilot_attempts':sum(a['phase']=='pilot' for a in attempts),'main_judgments':len(ans),'access_pairs_judgments':len(transitions),'access_matches':sum(t['match'] for t in transitions),'repeat_pairs_judgments':len(repeats),'repeat_matches':sum(t['match'] for t in repeats),'citations':len(qs),'allowed_existing_sources':sum(q['source_exists_and_allowed'] for q in qs),'exact_quotes':sum(q['quote_exact'] for q in qs),'whitespace_quotes':sum(q['quote_whitespace_match'] for q in qs),'locators_resolve':sum(q['locator_check']=='resolves' for q in qs),'reference_status':'all provisional or contested; no accuracy estimate',**batch['note'],'human_survey':'outside scope','main_input_tokens':sum(r['input_tokens'] or 0 for r in mainruns),'main_output_tokens':sum(r['output_tokens'] or 0 for r in mainruns)}
 (A/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 for name,rows in [('runs.csv',runs),('attempts.csv',attempts),('answers.csv',answers),('citations.csv',quotes),('transitions.csv',transitions),('repeat-agreement.csv',repeats)]:
  if rows:write_csv(A,name,rows,list(rows[0]))
 report='# Saved response analysis\n\n'+ '\n'.join(f'- {k}: {v}' for k,v in summary.items())+'\n\nCounts are mechanical. Quote matching does not establish semantic support. References are not independently validated.\n'
 (A/'summary.md').write_text(report)
 latex='\\begin{table}[t]\n\\caption{'+batch['caption']+'}\n\\label{tab:execution-'+batch['name']+'}\n\\centering\\begin{tabular}{lr}\\toprule\nMeasure & Count \\\\\n\\midrule\n'
 for label,key in [('Planned main sessions','planned_main'),('Attempted main sessions','attempted_main'),('Completed main responses','completed_main'),('Structurally usable responses','valid_main'),('Access condition delivered','condition_delivered_main'),('Main criterion judgments','main_judgments'),('Pilot attempts','pilot_attempts'),('All physical attempts','physical_attempts')]:latex+=f'{label} & {summary[key]} \\\\\n'
 latex+='\\bottomrule\\end{tabular}\n\\end{table}\n'
 latex+=f"Across available pairs, {summary['repeat_matches']} of {summary['repeat_pairs_judgments']} repeated judgments matched in status and rating. Across the two inputs, {summary['access_matches']} of {summary['access_pairs_judgments']} paired judgments matched. These denominators include only structurally valid responses with delivered inputs. They are descriptive counts, not independent trials or accuracy estimates.\n\n"
 latex+=f"The responses contained {summary['citations']} evidence citations; {summary['allowed_existing_sources']} named an existing source allowed for that input. Exact quoted text was located for {summary['exact_quotes']} citations, and whitespace normalization located {summary['whitespace_quotes']}. A mechanically parsed locator resolved for {summary['locators_resolve']} citations. These checks do not establish whether the cited evidence supports a rating.\n"
 (A/'results.tex').write_text(latex)
 # Rating distribution per criterion and input: counts of 0, 5, 10, 15, insufficient evidence (IE) and not applicable (NA) over usable main responses.
 dist='\\begin{table}[t]\n\\caption{'+batch['ratings_caption']+'}\n\\label{tab:ratings-'+batch['name']+'}\n\\centering\\small\\begin{tabular}{llrrrrrr}\\toprule\nCriterion & Input & 0 & 5 & 10 & 15 & IE & NA \\\\\n\\midrule\n'
 for i in [f'{g}{k}' for g in 'AB' for k in range(1,6)]:
  for c,label in [('documents','1'),('repository','2')]:
   rows=[a for a in ans if a['criterion']==i and a['condition']==c]
   cnt={v:sum(1 for a in rows if a['status']=='rated' and a['rating']==v) for v in [0,5,10,15]}
   ie=sum(1 for a in rows if a['status']=='insufficient_evidence');na=sum(1 for a in rows if a['status']=='not_applicable')
   dist+=f"{i if label=='1' else ''} & {label} & {cnt[0]} & {cnt[5]} & {cnt[10]} & {cnt[15]} & {ie} & {na} \\\\\n"
 dist+='\\bottomrule\\end{tabular}\n\\end{table}\n'
 (A/'ratings.tex').write_text(dist)
 return summary,byjob,delivered
def codex_batch():
 return {'name':'codex','jobs':json.loads((R/'jobs.json').read_text())['jobs'],'outputs':R/'outputs','analysis':R/'analysis','parse':parse_codex_events,'caption':'Codex batch execution accounting.','ratings_caption':'Codex batch: judgments per criterion and input over six usable responses per input (IE: insufficient evidence; NA: not applicable).','note':{'claude':'completed as a later batch; see claude/analysis'}}
def main():
 summary,_,_=analyze(codex_batch());print(json.dumps(summary))
if __name__=='__main__':main()

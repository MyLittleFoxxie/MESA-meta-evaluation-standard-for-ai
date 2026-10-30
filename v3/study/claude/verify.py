"""Offline integrity checks for the Claude batch. Does not compile LaTeX or call a model."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
C=Path(__file__).resolve().parent;R=C.parent;PROJECT=R.parent.parent
sys.path.insert(0,str(R))
from validate import validate
from analyze import parse_claude_events,read_events
checks=[]
def check(ok,label):
 if not ok:raise AssertionError(label)
 checks.append(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 frozen=json.loads((C/'freeze-manifest.json').read_text())
 for name,h in frozen['files'].items():check(digest(R/name)==h,'frozen '+name)
 codex=json.loads((R/'freeze-manifest.json').read_text())['files']
 for name in ['materials/rubric.json','materials/response-schema.json','materials/system.txt','materials/example.txt']+[f'prompts/{p.name}' for p in (R/'prompts').glob('*.txt')]:check(frozen['files'][name]==codex[name],'shared with codex '+name)
 jobs=json.loads((C/'jobs.json').read_text());mainjobs=[j for j in jobs['jobs'] if j['phase']=='main']
 check(jobs['model']=='claude-fable-5-1' and jobs['effort']=='medium','requested configuration')
 check(len(mainjobs)==12 and len({(j['benchmark'],j['condition'],j['repeat']) for j in mainjobs})==12,'complete main matrix')
 attempts=list((C/'outputs').glob('*/attempt-*/metadata.json'));check(len(attempts)==15,'fifteen attempts');check(len(attempts)<=jobs['attempt_cap'],'within attempt cap')
 failed=json.loads((C/'outputs/pilot-documents-1/attempt-1/metadata.json').read_text());check(failed['status']=='failed' and not (C/'outputs/pilot-documents-1/attempt-1/response.txt').exists(),'retained pilot failure')
 sourcecalls=0
 for job in mainjobs:
  d=C/'outputs'/job['id']/'attempt-1';meta=json.loads((d/'metadata.json').read_text())
  check(meta['status']=='completed' and meta['exit_code']==0,'completion '+job['id'])
  check(meta['requested_model']=='claude-fable-5-1' and meta['effort']=='medium','configuration '+job['id'])
  check('--model' in meta['command'] and meta['command'][meta['command'].index('--model')+1]=='claude-fable-5-1','command model '+job['id'])
  check('--effort' in meta['command'] and meta['command'][meta['command'].index('--effort')+1]=='medium','command effort '+job['id'])
  check('--strict-mcp-config' in meta['command'] and '--setting-sources' in meta['command'] and '--tools' in meta['command'],'isolation flags '+job['id'])
  check(meta['prompt_sha256']==digest(R/'prompts'/f'{job["id"]}.txt'),'prompt '+job['id'])
  check(not validate(json.loads((d/'response.txt').read_text())),'response '+job['id'])
  events=read_events(d/'events.jsonl')
  init=[e for e in events if e.get('type')=='system' and e.get('subtype')=='init']
  check(len(init)==1 and init[0]['model']=='claude-fable-5-1','init model '+job['id'])
  expected_tools=['StructuredOutput']+(['mcp__benchmark__list_files','mcp__benchmark__read_file'] if job['condition']=='repository' else [])
  check(sorted(init[0]['tools'])==sorted(expected_tools),'offered tools '+job['id'])
  check(all(m['message'].get('model')=='claude-fable-5-1' for m in events if m.get('type')=='assistant'),'assistant model '+job['id'])
  calls,other,usage=parse_claude_events(events)
  check(not other,'no foreign tools '+job['id'])
  check(all(c['server']=='benchmark' and c['tool'] in ['list_files','read_file'] for c in calls),'tool allowlist '+job['id'])
  result=[e for e in events if e.get('type')=='result'];check(len(result)==1 and not result[0].get('is_error') and result[0].get('permission_denials')==[],'result record '+job['id'])
  if job['condition']=='documents':check(not calls,'no file tools '+job['id'])
  else:
   check(any(c['tool']=='read_file' and c['ok'] for c in calls),'successful reading '+job['id'])
   sourcecalls+=len(calls)
 names=['summary.json','summary.md','results.tex','runs.csv','attempts.csv','answers.csv','citations.csv','transitions.csv','repeat-agreement.csv','cross-batch.csv','cross-batch.json','cross-batch.tex']
 before={n:digest(C/'analysis'/n) for n in names}
 subprocess.run([sys.executable,str(C/'analyze.py')],check=True,stdout=subprocess.DEVNULL)
 check(all(digest(C/'analysis'/n)==h for n,h in before.items()),'deterministic analysis')
 s=json.loads((C/'analysis/summary.json').read_text())
 for k,v in {'completed_main':12,'valid_main':12,'condition_delivered_main':12,'physical_attempts':15,'pilot_attempts':3,'main_judgments':120,'repeat_pairs_judgments':60,'repeat_matches':55,'access_pairs_judgments':60,'access_matches':45,'citations':460,'allowed_existing_sources':459}.items():check(s[k]==v,'summary '+k)
 x=json.loads((C/'analysis/cross-batch.json').read_text());check(x['paired_judgments']==120 and x['matches']==92 and x['status_matches']==115,'cross batch counts')
 check((C/'analysis/selected-reviews.md').read_text().count('Reason recorded by reviewer:')==60,'sixty selected judgments')
 check('same model as the reviewer' in (C/'analysis/selected-reviews.md').read_text(),'analyst disclosure')
 check((C/'analysis/discrepancy-review.md').exists() and 'not been checked by a human author' in (R/'README.md').read_text(),'discrepancy review linked with disclosure')
 for p in [C/'protocol.md',R/'claude-pending.md',C/'analysis/discrepancy-review.md']:
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if not target.startswith(('https://','http://','#')):check((p.parent/target.split('#')[0]).exists(),'markdown link '+target)
 outputs=[p for p in (C/'outputs').rglob('*') if p.is_file()]
 (C/'analysis/output-manifest.json').write_text(json.dumps({str(p.relative_to(C)):digest(p) for p in sorted(outputs)},indent=2)+'\n')
 report={'passed':True,'checks':len(checks),'frozen_files':len(frozen['files']),'main_sessions':12,'attempts':15,'source_calls_main':sourcecalls,'latex_compiled':False,'layout_and_page_length':'unchecked','limitations':['Analyst is the same model as the reviewer','No independent human reference judgments','No full initial API payload available in event records','Auxiliary Claude Code call to a smaller model not inspectable','Returned model identifier is not a weights snapshot confirmation','Quote matching and locator bounds do not establish semantic support'],'checks_performed':checks}
 (C/'analysis/verification.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='checks_performed'}))
if __name__=='__main__':main()

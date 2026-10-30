"""Offline study integrity and manuscript checks. Does not compile LaTeX."""
import collections,hashlib,json,re,subprocess,sys
from pathlib import Path
from validate import validate
R=Path(__file__).resolve().parent;PROJECT=R.parent.parent
checks=[]
def check(ok,label):
 if not ok:raise AssertionError(label)
 checks.append(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 frozen=json.loads((R/'freeze-manifest.json').read_text())
 for name,h in frozen['files'].items():check(digest(R/name)==h,'frozen '+name)
 jobs=json.loads((R/'jobs.json').read_text())['jobs'];mainjobs=[j for j in jobs if j['phase']=='main']
 check(len(mainjobs)==12,'twelve main jobs')
 check(len({(j['benchmark'],j['condition'],j['repeat']) for j in mainjobs})==12,'complete main matrix')
 attempts=list((R/'outputs').glob('*/attempt-*/metadata.json'));check(len(attempts)==14,'fourteen attempts')
 sourcecalls=0
 for job in mainjobs:
  d=R/'outputs'/job['id']/'attempt-1';meta=json.loads((d/'metadata.json').read_text())
  check(meta['status']=='completed' and meta['exit_code']==0,'completion '+job['id'])
  check(meta['requested_model']=='gpt-6-luna' and meta['effort']=='medium','configuration '+job['id'])
  check(meta['prompt_sha256']==digest(R/'prompts'/f'{job["id"]}.txt'),'prompt '+job['id'])
  check(not validate(json.loads((d/'response.txt').read_text())),'response '+job['id'])
  events=[json.loads(l) for l in (d/'events.jsonl').read_text().splitlines()]
  check(not any('unrecognized configuration' in e.get('item',{}).get('message','') for e in events),'no ignored config '+job['id'])
  calls=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='mcp_tool_call']
  check(all(c.get('server')=='benchmark' and c.get('tool') in ['list_files','read_file'] for c in calls),'tool allowlist '+job['id'])
  check(not any(e.get('item',{}).get('type') in ['command_execution','web_search','file_change'] for e in events),'no forbidden activity '+job['id'])
  if job['condition']=='documents':check(not calls,'no file tools '+job['id'])
  else:
   check(any(c.get('tool')=='read_file' and c.get('status')=='completed' and not c.get('error') for c in calls),'successful reading '+job['id'])
   sourcecalls+=len(calls)
 refs=json.loads((R/'analyst/references.json').read_text());check(len(refs)==60,'sixty reference proposals');check(all(not x['human_checked'] for x in refs),'no invented human checks')
 # Verify deterministic generation of mechanical analysis.
 names=['summary.json','summary.md','results.tex','runs.csv','attempts.csv','answers.csv','citations.csv','transitions.csv','repeat-agreement.csv']
 before={n:digest(R/'analysis'/n) for n in names}
 subprocess.run([sys.executable,str(R/'analyze.py')],check=True,stdout=subprocess.DEVNULL)
 check(all(digest(R/'analysis'/n)==h for n,h in before.items()),'deterministic analysis')
 s=json.loads((R/'analysis/summary.json').read_text())
 for k,v in {'completed_main':12,'valid_main':12,'condition_delivered_main':12,'physical_attempts':14,'main_judgments':120,'repeat_pairs_judgments':60,'repeat_matches':46,'access_pairs_judgments':60,'access_matches':42,'claude':'completed as a later batch; see claude/analysis'}.items():check(s[k]==v,'summary '+k)
 tex=PROJECT/'paper_mesa_v3.tex';text=tex.read_text();expanded=text
 for name in re.findall(r'\\input\{([^}]+)\}',text):
  p=PROJECT/name;check(p.exists(),'tex input '+name);expanded+='\n'+p.read_text()
 check(not re.search(r'(?i)claude (?:experiment |batch )?remains pending',expanded),'manuscript no longer pending')
 keys=set(re.findall(r'@\w+\s*\{\s*([^,]+),',(PROJECT/'references.bib').read_text()))
 for cite in re.findall(r'\\cite\{([^}]+)\}',expanded):
  for key in cite.split(','):check(key in keys,'citation '+key)
 labels=re.findall(r'\\label\{([^}]+)\}',expanded);check(len(labels)==len(set(labels)),'unique labels')
 for label in re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',expanded):check(label in labels,'reference '+label)
 clean=re.sub(r'(?<!\\)%[^\n]*','',expanded);stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
  if m[1]=='begin':stack.append(m[2])
  else:check(bool(stack) and stack.pop()==m[2],'environment '+m[2])
 check(not stack,'environments balanced')
 # Check each file independently: input fragments are balanced separately.
 for p in [tex,R/'analysis/results.tex',R/'analysis/interpretation.tex',R/'claude/analysis/results.tex',R/'claude/analysis/interpretation.tex',R/'claude/analysis/cross-batch.tex']:
  level=0
  for token in re.findall(r'(?<!\\)[{}]',re.sub(r'(?<!\\)%[^\n]*','',p.read_text())):
   level+=1 if token=='{' else -1;check(level>=0,'brace order '+p.name)
  check(level==0,'balanced braces '+p.name)
 title=re.search(r'\\title\{([^}]+)\}',text)[1]
 check(not re.search(r'\b(?:MESA|AI|CLI|EFPA)\b',title),'no acronyms in title')
 check((R/'analysis/selected-reviews.md').read_text().count('Reason recorded by reviewer:')==60,'sixty selected judgments')
 for p in [R/'README.md',PROJECT/'v3/README.md',PROJECT/'v3/experiments.md',PROJECT/'v3/CONTINUE.md',R/'claude-pending.md']:
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if not target.startswith(('https://','http://','#')):check((p.parent/target.split('#')[0]).exists(),'markdown link '+target)
 outputs=[p for p in (R/'outputs').rglob('*') if p.is_file() and 'cli-log' not in p.parts]
 (R/'analysis/output-manifest.json').write_text(json.dumps({str(p.relative_to(R)):digest(p) for p in sorted(outputs)},indent=2)+'\n')
 report={'passed':True,'checks':len(checks),'frozen_files':len(frozen['files']),'main_sessions':12,'attempts':14,'source_calls_main':sourcecalls,'latex_compiled':False,'layout_and_page_length':'unchecked','limitations':['No independent human reference judgments','No full initial API payload available in event records','Returned underlying model snapshot not confirmed','Quote matching and locator bounds do not establish semantic support'],'checks_performed':checks}
 (R/'analysis/verification.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='checks_performed'}))
if __name__=='__main__':main()

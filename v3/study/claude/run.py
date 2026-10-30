"""Sequential Claude Code study runner for the later batch. No automatic retries or response repairs."""
import argparse,datetime,hashlib,json,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
C=Path(__file__).resolve().parent;R=C.parent
BIN=shutil.which('claude')
MODEL='claude-fable-5-1';EFFORT='medium';TOOLS=['mcp__benchmark__list_files','mcp__benchmark__read_file']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_freeze():
 f=C/'freeze-manifest.json'
 if not f.exists():raise ValueError('Claude batch is not frozen')
 for name,h in json.loads(f.read_text())['files'].items():
  if sha(R/name)!=h:raise ValueError('freeze mismatch: '+name)
def command(job):
 cmd=[BIN,'-p','--model',MODEL,'--effort',EFFORT,'--output-format','stream-json','--verbose','--no-session-persistence','--system-prompt',(R/'materials/system.txt').read_text().strip(),'--json-schema',schema_argument(),'--setting-sources','','--strict-mcp-config','--tools','','--disable-slash-commands','--permission-mode','dontAsk','--permission-prompts','none']
 if job['condition']=='repository':
  mcp={'mcpServers':{'benchmark':{'command':sys.executable,'args':[str(R/'file_server.py'),str(R/'sources'/job['benchmark']/'repository')]}}}
  cmd+=['--mcp-config',json.dumps(mcp),'--allowedTools',*TOOLS]
 return cmd
def schema_argument():
 # Claude Code rejects the draft 2020-12 "$schema" metadata key. Only that key is removed; the frozen file is unchanged.
 schema=json.loads((R/'materials/response-schema.json').read_text());schema.pop('$schema',None);return json.dumps(schema)
def extract_response(events_path,out):
 """Write the structured result verbatim. Never repair or reformat the content."""
 for line in events_path.read_text().splitlines():
  try:e=json.loads(line)
  except ValueError:continue
  if e.get('type')=='result':
   if e.get('structured_output') is not None:(out/'response.txt').write_text(json.dumps(e['structured_output']));return
   if isinstance(e.get('result'),str) and e['result'].strip():(out/'response.txt').write_text(e['result']);return
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['pilot','main'],required=True);ap.add_argument('--job');ap.add_argument('--retry',action='store_true',help='create the next attempt after a retained failed attempt');a=ap.parse_args()
 if a.phase=='main':verify_freeze()
 jobs=json.loads((C/'jobs.json').read_text())['jobs']
 for job in jobs:
  if job['phase']!=a.phase or (a.job and job['id']!=a.job):continue
  prior=sorted((C/'outputs'/job['id']).glob('attempt-*')) if (C/'outputs'/job['id']).exists() else []
  if prior:
   last=json.loads((prior[-1]/'metadata.json').read_text())
   if last['status']=='completed' or not a.retry:print('SKIP retained',job['id'],last['status'],flush=True);continue
  out=C/'outputs'/job['id']/f'attempt-{len(prior)+1}'
  if len(list((C/'outputs').glob('*/attempt-*/metadata.json')))>=16:raise SystemExit('Attempt cap reached')
  out.mkdir(parents=True)
  with tempfile.TemporaryDirectory(prefix='mesa-v3-claude-') as tmp:
   work=Path(tmp);cmd=command(job)
   env=dict(os.environ)
   # Existing Claude Code login is used. No API key or Codex key is passed through.
   for k in list(env):
    if k.startswith(('OPENAI_API_KEY','CODEX_API_KEY','ANTHROPIC_API_KEY','CLAUDE_CODE_')):env.pop(k)
   start=time.time();meta={**job,'requested_model':MODEL,'effort':EFFORT,'cli_version':subprocess.check_output([BIN,'--version'],text=True).strip(),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prompt_sha256':sha(R/'prompts'/f'{job["id"]}.txt'),'command':cmd,'cwd':str(work),'status':'running'}
   (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
   print('START',job['id'],flush=True)
   with (R/'prompts'/f'{job["id"]}.txt').open() as inp,(out/'events.jsonl').open('w') as stdout,(out/'stderr.txt').open('w') as stderr:
    result=subprocess.run(cmd,stdin=inp,stdout=stdout,stderr=stderr,env=env,cwd=work)
   extract_response(out/'events.jsonl',out)
   meta.update(exit_code=result.returncode,elapsed_seconds=time.time()-start,status='completed' if (out/'response.txt').exists() and (out/'response.txt').stat().st_size else 'failed',ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
   (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
   print('END',job['id'],meta['status'],result.returncode,flush=True)
   if result.returncode!=0 or meta['status']!='completed':raise SystemExit('Stopped after failure; no automatic retry')
if __name__=='__main__':main()

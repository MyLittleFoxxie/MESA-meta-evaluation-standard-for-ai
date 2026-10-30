"""Sequential Codex study runner. No automatic retries or response repairs."""
import argparse,datetime,hashlib,json,os,shutil,subprocess,tempfile,time
from pathlib import Path
R=Path(__file__).resolve().parent
BIN=shutil.which('codex')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_freeze():
 f=R/'freeze-manifest.json'
 if not f.exists():raise ValueError('Main study is not frozen')
 for name,h in json.loads(f.read_text())['files'].items():
  if sha(R/name)!=h:raise ValueError('freeze mismatch: '+name)
def command(job,work,out):
 cmd=[BIN,'exec','--ignore-user-config','--ignore-rules','--skip-git-repo-check','--ephemeral','--json','--color','never','-C',str(work),'-m','gpt-6-luna','-s','read-only','--output-schema',str(R/'materials/response-schema.json'),'-o',str(out/'response.txt')]
 cfg={'model_reasoning_effort':'medium','approval_policy':'never','web_search':'disabled','project_doc_max_bytes':0,'model_instructions_file':str(R/'materials/system.txt'),'features.shell_tool':False,'features.shell_snapshot':False,'features.apps':False,'features.plugins':False,'features.remote_plugin':False,'features.multi_agent':False,'features.multi_agent_v2':False,'features.browser_use':False,'features.computer_use':False,'features.skill_search':False,'features.skip_host_skill_discovery':True,'features.view_image':False,'memories.generate_memories':False,'memories.use_memories':False,'service_tier':'default','log_dir':str(out/'cli-log'),'sqlite_home':str(work/'state')}
 # Disable all known skill paths; never read their contents into reviewer context.
 skillroots=[Path.home()/'.codex/skills',Path.home()/'.agents/skills']
 skills=[{'path':str(p.parent),'enabled':False} for root in skillroots if root.exists() for p in root.rglob('SKILL.md')]
 if skills:cmd+=['-c','skills.config=['+','.join('{path='+json.dumps(s['path'])+',enabled=false}' for s in skills)+']']
 for k,v in cfg.items():cmd+=['-c',k+'='+json.dumps(v)]
 if job['condition']=='repository':
  cmd+=['-c','mcp_servers.benchmark.command='+json.dumps(sys_executable()),'-c','mcp_servers.benchmark.args='+json.dumps([str(R/'file_server.py'),str(R/'sources'/job['benchmark']/'repository')]),'-c','mcp_servers.benchmark.required=true','-c','mcp_servers.benchmark.tools.list_files.approval_mode="auto"','-c','mcp_servers.benchmark.tools.read_file.approval_mode="auto"']
 return cmd+['-']
def sys_executable():
 import sys
 return sys.executable
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['pilot','main'],required=True);ap.add_argument('--job');a=ap.parse_args()
 if a.phase=='main':verify_freeze()
 jobs=json.loads((R/'jobs.json').read_text())['jobs']
 for job in jobs:
  if job['phase']!=a.phase or (a.job and job['id']!=a.job):continue
  out=R/'outputs'/job['id']/'attempt-1'
  if out.exists():print('SKIP retained',job['id'],flush=True);continue
  if len(list((R/'outputs').glob('*/attempt-*/metadata.json')))>=16:raise SystemExit('Attempt cap reached')
  out.mkdir(parents=True)
  with tempfile.TemporaryDirectory(prefix='mesa-v3-review-') as tmp:
   work=Path(tmp);cmd=command(job,work,out)
   env=dict(os.environ)
   # Do not change HOME or CODEX_HOME. Existing authentication stays local to Codex.
   for k in list(env):
    if k.startswith(('OPENAI_API_KEY','CODEX_API_KEY','ANTHROPIC_API_KEY')):env.pop(k)
   start=time.time();meta={**job,'requested_model':'gpt-6-luna','effort':'medium','cli_version':subprocess.check_output([BIN,'--version'],text=True).strip(),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prompt_sha256':sha(R/'prompts'/f'{job["id"]}.txt'),'command':cmd,'status':'running'}
   (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
   print('START',job['id'],flush=True)
   with (R/'prompts'/f'{job["id"]}.txt').open() as inp,(out/'events.jsonl').open('w') as stdout,(out/'stderr.txt').open('w') as stderr:
    result=subprocess.run(cmd,stdin=inp,stdout=stdout,stderr=stderr,env=env)
   meta.update(exit_code=result.returncode,elapsed_seconds=time.time()-start,status='completed' if (out/'response.txt').exists() and (out/'response.txt').stat().st_size else 'failed',ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
   (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
   print('END',job['id'],meta['status'],result.returncode,flush=True)
   if result.returncode!=0:raise SystemExit('Stopped after failure; no automatic retry')
if __name__=='__main__':main()

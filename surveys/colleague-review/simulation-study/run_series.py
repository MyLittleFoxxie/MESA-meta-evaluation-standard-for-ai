#!/usr/bin/env python3
"""Execute frozen study prompts in fresh Codex processes; never repair responses."""
from pathlib import Path
import argparse, concurrent.futures, datetime, hashlib, json, os, random, subprocess, tempfile, time

ROOT = Path(__file__).resolve().parent
MODEL = 'gpt-6.1-sol'
SETTINGS = ['model_reasoning_effort="medium"', 'approval_policy="never"',
            'web_search="disabled"', 'project_doc_max_bytes=0',
            'memories.use_memories=false', 'memories.generate_memories=false',
            'features.shell_tool=false', 'features.multi_agent=false']
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,d): Path(p).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def command(work):
    c=['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check',
       '--sandbox','read-only','-C',str(work),'-m',MODEL,'--json']
    for s in SETTINGS: c += ['-c',s]
    return c+['-']
def run(job,timeout):
    jid=job['id']
    d=ROOT/'outputs'/jid
    d.mkdir(parents=True,exist_ok=False)
    prompt_path=ROOT/job['input']
    assert sha(prompt_path)==job['sha256'],f'Input changed: {jid}'
    work=Path(tempfile.mkdtemp(prefix='mesa-session-'))
    cmd=command(work)
    meta={'job':job,'status':'running','started_at':now(),'requested_model':MODEL,
          'model_identification':'User requested GPT-6.1 Sol for this separate series. CLI model identifier requested explicitly; backend snapshot not independently exposed.',
          'temperature':'not exposed','seed':'not exposed','reasoning_effort':'medium',
          'command':cmd,'cwd_empty_at_start':not any(work.iterdir()),'attempt':1,
          'input_sha256':sha(prompt_path),'runner_sha256':sha(__file__)}
    write(d/'metadata.json',meta)
    t=time.monotonic()
    try:
        with (d/'events.jsonl').open('wb') as out,(d/'stderr.txt').open('wb') as err:
            proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=out,stderr=err)
            try:
                proc.communicate(prompt_path.read_bytes(),timeout=timeout)
                meta['exit_code']=proc.returncode
                meta['status']='process_completed' if proc.returncode==0 else 'process_failed'
            except subprocess.TimeoutExpired:
                proc.kill();proc.communicate()
                meta['exit_code']=proc.returncode;meta['status']='timeout'
    except Exception as exc:
        meta['status']='launcher_failed';meta['error']=repr(exc)
    events=[];bad=[]
    for i,line in enumerate((d/'events.jsonl').read_text().splitlines(),1):
        try: events.append(json.loads(line))
        except json.JSONDecodeError: bad.append(i)
    messages=[e['item'].get('text','') for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
    if messages: (d/'response.txt').write_text(messages[-1])
    meta['thread_ids']=[e.get('thread_id') for e in events if e.get('type')=='thread.started']
    meta['turn_completed']=any(e.get('type')=='turn.completed' for e in events)
    meta['usage']=[e.get('usage') for e in events if e.get('type')=='turn.completed']
    meta['observed_item_types']=sorted({e.get('item',{}).get('type') for e in events if e.get('item',{}).get('type')})
    meta['tool_items']=[e for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type') not in ['agent_message','reasoning']]
    meta['non_json_event_lines']=bad
    meta['finished_at']=now();meta['elapsed_seconds']=round(time.monotonic()-t,3)
    meta['elapsed_note']='Infrastructure execution duration, not human review time or isolated model latency.'
    meta['output_files_sha256']={p.name:sha(p) for p in d.iterdir() if p.name!='metadata.json'}
    meta['workdir_files_after']=[str(p.relative_to(work)) for p in work.rglob('*') if p.is_file()]
    write(d/'metadata.json',meta)
    print(json.dumps({'id':jid,'status':meta['status'],'turn_completed':meta['turn_completed'],'seconds':meta['elapsed_seconds']},ensure_ascii=False),flush=True)
    return meta['status']

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=3);ap.add_argument('--limit',type=int)
    ap.add_argument('--timeout',type=int,default=1200);ap.add_argument('--resume',action='store_true');ap.add_argument('--dry-run',action='store_true')
    ap.add_argument('--root',type=Path,required=True)
    args=ap.parse_args()
    global ROOT
    ROOT=args.root.resolve()
    source=json.loads((ROOT/'jobs.json').read_text())
    jobs=source['jobs'] if isinstance(source,dict) else source
    # Normalize generator's alternative field names, keeping canonical manifest intact.
    for j in jobs:
        if 'input' not in j: j['input']=j.get('input_path',j.get('path'))
        if 'sha256' not in j: j['sha256']=j.get('input_sha256')
        if not j['input'] or not j['sha256']: raise ValueError(j)
        assert sha(ROOT/j['input'])==j['sha256']
    order=sorted(jobs,key=lambda j:j['id']);random.Random(20261014).shuffle(order)
    if args.resume: order=[j for j in order if not (ROOT/'outputs'/j['id']).exists()]
    elif (ROOT/'outputs').exists() and any((ROOT/'outputs').iterdir()): raise SystemExit('Existing outputs: use --resume to run only unattempted jobs; no overwrite/retry.')
    if args.limit is not None: order=order[:args.limit]
    print(json.dumps({'scheduled':len(order),'workers':args.workers,'requested_model':MODEL,'order_seed':20261014,'dry_run':args.dry_run}),flush=True)
    if args.dry_run: return
    (ROOT/'outputs').mkdir(exist_ok=True)
    manifest={'started_at':now(),'jobs_sha256':sha(ROOT/'jobs.json'),'runner_sha256':sha(__file__),
              'scheduled_ids':[j['id'] for j in order],'workers':args.workers,'timeout_seconds':args.timeout,
              'order_seed':20261014,'order_seed_note':'Scheduling only; not a generation seed.',
              'settings':SETTINGS,'model':MODEL,'cli_version':subprocess.run(['codex','--version'],capture_output=True,text=True).stdout.strip()}
    launches=ROOT/'launches';launches.mkdir(exist_ok=True)
    write(launches/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S')+'.json'),manifest)
    # Bounded queue: stop scheduling on an infrastructure failure instead of exhausting all jobs.
    iterator=iter(order); stopped=False
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        pending={ex.submit(run,j,args.timeout):j for j in list(__import__('itertools').islice(iterator,args.workers))}
        while pending:
            done,_=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                job=pending.pop(future)
                status=future.result()
                if status!='process_completed':
                    stopped=True
                    print(json.dumps({'scheduling_stopped':True,'trigger_job':job['id'],'status':status,'note':'Remaining jobs stay unattempted; active jobs finish. Inspect error before resuming.'}),flush=True)
                if not stopped:
                    nxt=next(iterator,None)
                    if nxt: pending[ex.submit(run,nxt,args.timeout)]=nxt

if __name__=='__main__': main()

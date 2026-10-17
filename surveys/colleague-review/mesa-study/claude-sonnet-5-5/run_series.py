#!/usr/bin/env python3
"""Execute frozen study prompts in fresh, isolated Claude Code print-mode sessions; never repair responses."""
from pathlib import Path
import argparse, concurrent.futures, datetime, hashlib, itertools, json, random, subprocess, tempfile, time

ROOT = Path(__file__).resolve().parent
MODEL = 'claude-sonnet-5-5'
EFFORT = 'medium'
SYSTEM_PROMPT = "Answer the user's request using only the text supplied in the message, in the exact output format it requests."
# Isolation: no tools, no MCP servers, no CLAUDE.md, hooks, skills, plugins or memory, no saved session.
FLAGS = ['--safe-mode', '--tools', '', '--strict-mcp-config', '--disable-slash-commands',
         '--no-session-persistence', '--output-format', 'stream-json', '--verbose']

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, d): Path(p).write_text(json.dumps(d, indent=2, ensure_ascii=False)+'\n')
def cli_version(): return subprocess.run(['claude', '--version'], capture_output=True, text=True).stdout.strip()

def command():
    return ['claude', '-p', '--model', MODEL, '--effort', EFFORT, *FLAGS, '--system-prompt', SYSTEM_PROMPT]

def summarize_events(lines):
    """Read stream-json events into the metadata fields used by analysis and verification."""
    events, bad = [], []
    for i, line in enumerate(lines, 1):
        try:
            e = json.loads(line)
            if isinstance(e, dict): events.append(e)
        except json.JSONDecodeError:
            bad.append(i)
    init = next((e for e in events if e.get('type') == 'system' and e.get('subtype') == 'init'), {})
    results = [e for e in events if e.get('type') == 'result']
    final = results[-1] if results else {}
    blocks = [b for e in events if e.get('type') in ('assistant', 'user')
              for b in (e.get('message', {}).get('content') or []) if isinstance(b, dict)]
    texts = [b.get('text', '') for e in events if e.get('type') == 'assistant'
             for b in (e.get('message', {}).get('content') or []) if isinstance(b, dict) and b.get('type') == 'text']
    response = final.get('result') if final.get('subtype') == 'success' and not final.get('is_error') else None
    if response is None and texts: response = texts[-1]
    return {
        'events': events, 'non_json_event_lines': bad, 'response': response,
        'thread_ids': [init['session_id']] if init.get('session_id') else [],
        'turn_completed': bool(final) and final.get('subtype') == 'success' and not final.get('is_error'),
        'result_subtype': final.get('subtype'), 'result_is_error': final.get('is_error'),
        'result_error_text': final.get('result') if final.get('is_error') else None,
        'usage': final.get('usage'), 'model_usage': final.get('modelUsage'), 'total_cost_usd': final.get('total_cost_usd'),
        'num_turns': final.get('num_turns'),
        'reported_model': init.get('model'), 'init_tools': init.get('tools'), 'init_mcp_servers': init.get('mcp_servers'),
        'init_slash_commands': init.get('slash_commands'), 'init_agents': init.get('agents'), 'init_skills': init.get('skills'),
        'init_plugins': init.get('plugins'), 'permission_mode': init.get('permissionMode'),
        'observed_event_types': sorted({f"{e.get('type')}/{e.get('subtype')}" if e.get('subtype') else str(e.get('type')) for e in events}),
        'observed_block_types': sorted({str(b.get('type')) for b in blocks}),
        'tool_items': [b for b in blocks if b.get('type') in ('tool_use', 'tool_result', 'server_tool_use')],
    }

def run(job, timeout, attempt=1):
    jid = job['id']
    d = ROOT/'outputs'/jid if attempt == 1 else ROOT/'outputs'/jid/f'attempt-{attempt}'
    d.mkdir(parents=True, exist_ok=False)
    prompt_path = ROOT/job['input']
    assert sha(prompt_path) == job['sha256'], f'Input changed: {jid}'
    work = Path(tempfile.mkdtemp(prefix='mesa-session-'))
    cmd = command()
    meta = {'job': job, 'status': 'running', 'started_at': now(), 'requested_model': MODEL,
            'model_identification': 'Claude Sonnet 5.5 requested by full model ID through Claude Code print mode; the model reported by the session is recorded in reported_model. Backend snapshot beyond that ID is not exposed.',
            'temperature': 'not exposed', 'seed': 'not exposed', 'reasoning_effort': EFFORT, 'system_prompt': SYSTEM_PROMPT,
            'command': cmd, 'cli_version': cli_version(), 'cwd': str(work), 'cwd_empty_at_start': not any(work.iterdir()),
            'attempt': attempt, 'input_sha256': sha(prompt_path), 'runner_sha256': sha(__file__)}
    write(d/'metadata.json', meta)
    t = time.monotonic()
    try:
        with (d/'events.jsonl').open('wb') as out, (d/'stderr.txt').open('wb') as err:
            proc = subprocess.Popen(cmd, cwd=work, stdin=subprocess.PIPE, stdout=out, stderr=err)
            try:
                proc.communicate(prompt_path.read_bytes(), timeout=timeout)
                meta['exit_code'] = proc.returncode
                meta['status'] = 'process_completed' if proc.returncode == 0 else 'process_failed'
            except subprocess.TimeoutExpired:
                proc.kill(); proc.communicate()
                meta['exit_code'] = proc.returncode; meta['status'] = 'timeout'
    except Exception as exc:
        meta['status'] = 'launcher_failed'; meta['error'] = repr(exc)
    s = summarize_events((d/'events.jsonl').read_text().splitlines() if (d/'events.jsonl').exists() else [])
    if s['response'] is not None: (d/'response.txt').write_text(s['response'])
    if meta['status'] == 'process_completed' and not s['turn_completed']: meta['status'] = 'process_failed'
    meta.update({k: v for k, v in s.items() if k not in ('events', 'response')})
    meta['finished_at'] = now(); meta['elapsed_seconds'] = round(time.monotonic()-t, 3)
    meta['elapsed_note'] = 'Infrastructure execution duration, not human review time or isolated model latency.'
    meta['output_files_sha256'] = {p.name: sha(p) for p in d.iterdir() if p.is_file() and p.name != 'metadata.json'}
    meta['workdir_files_after'] = [str(p.relative_to(work)) for p in work.rglob('*') if p.is_file()]
    write(d/'metadata.json', meta)
    print(json.dumps({'id': jid, 'attempt': attempt, 'status': meta['status'], 'turn_completed': meta['turn_completed'],
                      'reported_model': meta['reported_model'], 'seconds': meta['elapsed_seconds']}, ensure_ascii=False), flush=True)
    return meta['status']

def load_jobs():
    source = json.loads((ROOT/'jobs.json').read_text())
    jobs = source['jobs'] if isinstance(source, dict) else source
    for j in jobs:
        assert sha(ROOT/j['input']) == j['sha256'], j['id']
    return jobs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, required=True); ap.add_argument('--workers', type=int, default=2)
    ap.add_argument('--limit', type=int); ap.add_argument('--timeout', type=int, default=1200)
    ap.add_argument('--resume', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    global ROOT
    ROOT = args.root.resolve()
    jobs = load_jobs()
    order = sorted(jobs, key=lambda j: j['id']); random.Random(20261017).shuffle(order)
    if args.resume: order = [j for j in order if not (ROOT/'outputs'/j['id']).exists()]
    elif (ROOT/'outputs').exists() and any((ROOT/'outputs').iterdir()): raise SystemExit('Existing outputs: use --resume to run only unattempted jobs; no overwrite/retry.')
    if args.limit is not None: order = order[:args.limit]
    print(json.dumps({'scheduled': len(order), 'workers': args.workers, 'requested_model': MODEL, 'order_seed': 20261017, 'dry_run': args.dry_run}), flush=True)
    if args.dry_run: return
    (ROOT/'outputs').mkdir(exist_ok=True)
    manifest = {'started_at': now(), 'jobs_sha256': sha(ROOT/'jobs.json'), 'runner_sha256': sha(__file__),
                'scheduled_ids': [j['id'] for j in order], 'workers': args.workers, 'timeout_seconds': args.timeout,
                'order_seed': 20261017, 'order_seed_note': 'Scheduling only; not a generation seed.',
                'command': command(), 'model': MODEL, 'reasoning_effort': EFFORT, 'system_prompt': SYSTEM_PROMPT, 'cli_version': cli_version()}
    launches = ROOT/'launches'; launches.mkdir(exist_ok=True)
    write(launches/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S')+'.json'), manifest)
    # Bounded queue: stop scheduling on an infrastructure failure instead of exhausting all jobs.
    iterator = iter(order); stopped = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        pending = {ex.submit(run, j, args.timeout): j for j in itertools.islice(iterator, args.workers)}
        while pending:
            done, _ = concurrent.futures.wait(pending, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                job = pending.pop(future)
                status = future.result()
                if status != 'process_completed':
                    stopped = True
                    print(json.dumps({'scheduling_stopped': True, 'trigger_job': job['id'], 'status': status, 'note': 'Remaining jobs stay unattempted; active jobs finish. Inspect error before resuming.'}), flush=True)
                if not stopped:
                    nxt = next(iterator, None)
                    if nxt: pending[ex.submit(run, nxt, args.timeout)] = nxt

if __name__ == '__main__': main()

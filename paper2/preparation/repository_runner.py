"""Repository preparation and offline validation. Provider execution is disabled.

Commands operate on explicit local task specifications; never infer eligibility
from release metadata. Reference fixes and tests are used only by evaluation.
"""
import argparse
import hashlib
import json
import subprocess
import tempfile
import time
import uuid
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from paper2.method.decision_engine import compute_wilson_score_interval
from paper2.protocol.simulate_precision import simulate_binomial_decisions

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / 'v3'
REPOSITORIES = ('sympy/sympy','django/django','sphinx-doc/sphinx')
CRITERIA = ('C05','C07','C12','C14','C28')

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def save_new(path, data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x') as f: json.dump(data,f,indent=2);f.write('\n')

def verdict(k,n,threshold=.70):
    if not n: return 'Unresolved'
    if not 0 <= k <= n: raise ValueError('Invalid observations')
    lb,ub=compute_wilson_score_interval(k,n)
    return 'Supported' if lb >= threshold else 'Contradicted' if ub < threshold else 'Unresolved'

def compare(source,target_k,target_n):
    if source not in ('Supported','Contradicted','Unresolved'): raise ValueError('Invalid verdict')
    target=verdict(target_k,target_n)
    return dict(source=source,target=target,target_n=target_n,target_successes=target_k,
                relation='Unresolved evidence' if 'Unresolved' in (source,target) else
                         'Agreement' if source==target else 'Discrepancy')

def validate_review(record):
    required=('criterion','evidence_location','scope','judgment','rationale','detection_limits',
              'audit_execution','method_adequacy','empirical_finding','warrant','author',
              'assistant_role','affected_cases')
    if any(not record.get(k) for k in required): raise ValueError('Incomplete review record')
    if record['criterion'] not in CRITERIA: raise ValueError('Unknown criterion')
    if record['scope'] not in ('release','configuration','task','subset'): raise ValueError('Unknown scope')
    if record['judgment'] not in ('Verified','Contradicted','Undocumented','Claimed','Documented','Not applicable'):
        raise ValueError('Unknown judgment')
    return record

def lock_decision(record,path):
    record=dict(record)
    required=('case_id','config_id','method','task_ids','successes','n','interval','verdict',
              'review_record_hashes','source_artifact_hashes')
    if any(k not in record for k in required): raise ValueError('Incomplete decision record')
    if record['n']!=len(record['task_ids']) or len(set(record['task_ids']))!=record['n']:
        raise ValueError('Observation identity mismatch')
    expected=compute_wilson_score_interval(record['successes'],record['n'])
    if tuple(record['interval'])!=expected: raise ValueError('Interval mismatch')
    if record['method'] not in ('M1','M2','M3'): raise ValueError('Unknown method')
    natural=verdict(record['successes'],record['n'])
    if record['verdict']!=natural and not (record['method']=='M3' and record['verdict']=='Unresolved'):
        raise ValueError('Verdict mismatch')
    if record['method']=='M3' and not record['review_record_hashes']: raise ValueError('Missing review provenance')
    if not record['source_artifact_hashes']: raise ValueError('Missing source provenance')
    for group in ('source_artifact_hashes','review_record_hashes'):
        for artifact, expected in record[group].items():
            if digest(artifact)!=expected: raise ValueError('Evidence checksum mismatch')
    record.update(version=3,timestamp=now())
    record['record_sha256']=hashlib.sha256(json.dumps(record,sort_keys=True).encode()).hexdigest()
    save_new(path,record)
    return record

def read_locked(path):
    record=json.loads(Path(path).read_text());expected=record.pop('record_sha256')
    if hashlib.sha256(json.dumps(record,sort_keys=True).encode()).hexdigest()!=expected:
        raise ValueError('Decision record changed')
    for group in ('source_artifact_hashes','review_record_hashes'):
        for artifact, expected in record[group].items():
            if digest(artifact)!=expected: raise ValueError('Evidence changed after source decision')
    return record

def overlap(a,b):
    """An empty match list is not a proof of absence of related issues."""
    reasons=[]
    if a['repo']==b['repo']:
        if a['task_id']==b['task_id'] or (a.get('issue_id') and a.get('issue_id')==b.get('issue_id')):
            reasons.append('issue identity')
        if a.get('reference_patch_sha256') and a.get('reference_patch_sha256')==b.get('reference_patch_sha256'):
            reasons.append('shared fix')
        if set(a.get('related_issues',[])) & ({b.get('issue_id')}|set(b.get('related_issues',[]))):
            reasons.append('related issue')
        if a.get('issue_id') in b.get('related_issues',[]): reasons.append('related issue')
    return sorted(set(reasons))

def validate_task(task):
    required=('task_id','repo','issue_id','base_commit','checkout','environment','test_command',
              'junit_path','target_tests','reference_patch','reference_patch_sha256','oracle_files',
              'related_issues','overlap_review','issue_description')
    missing=[k for k in required if not task.get(k) and k not in ('related_issues',)]
    if missing: raise ValueError('Missing task fields: '+', '.join(missing))
    if not isinstance(task['test_command'],list) or not all(isinstance(x,str) for x in task['test_command']):
        raise ValueError('test_command must be argv')
    if not task['environment'].get('id') or not task['environment'].get('setup_verified'):
        raise ValueError('Environment setup not verified')
    if task['overlap_review'].get('status')!='checked': raise ValueError('Overlap review pending')
    for name in [task['junit_path'],*task['oracle_files']]:
        p=Path(name)
        if p.is_absolute() or '..' in p.parts: raise ValueError('Unsafe evaluation path')
    if digest(task['reference_patch'])!=task['reference_patch_sha256']: raise ValueError('Reference patch checksum mismatch')

def run(argv,cwd,timeout=60):
    try:
        p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True,timeout=timeout)
        return dict(returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,timeout=False)
    except subprocess.TimeoutExpired as e:
        return dict(returncode=None,stdout=str(e.stdout or ''),stderr=str(e.stderr or ''),timeout=True)

def test_result(task,workspace):
    report=workspace/task['junit_path']
    if report.exists(): report.unlink()
    result=run(task['test_command'],workspace,task.get('evaluation_timeout',60))
    result['tests']={}
    if result['timeout']: result['problem']='evaluation timeout';return result
    if not report.exists(): result['problem']='missing test report';return result
    try:
        for case in ET.parse(report).iter('testcase'):
            key=case.get('classname','')+'.'+case.get('name','')
            if key in result['tests']: raise ValueError('duplicate test identifier')
            result['tests'][key]='error' if case.find('error') is not None else 'failure' if case.find('failure') is not None else 'skipped' if case.find('skipped') is not None else 'pass'
        if not set(task['target_tests']) <= set(result['tests']): result['problem']='missing target tests'
    except (ET.ParseError,ValueError) as e: result['problem']=str(e)
    return result

def evaluate(task,patch=None):
    """Fresh clone per evaluation; does not expose this workspace to an agent."""
    validate_task(task)
    with tempfile.TemporaryDirectory(prefix='paper2-evaluation-') as td:
        workspace=Path(td)/'repo'
        for argv in [['git','clone','--no-hardlinks','--no-checkout',str(Path(task['checkout']).resolve()),str(workspace)],
                     ['git','-C',str(workspace),'checkout','--detach',task['base_commit']]]:
            result=run(argv,Path(td))
            if result['returncode']!=0: return dict(problem='checkout failure',command=result)
        if patch:
            result=run(['git','apply','--',str(Path(patch).resolve())],workspace)
            if result['returncode']!=0: return dict(problem='invalid patch',command=result)
        for dest,origin in task['oracle_files'].items():
            target=workspace/dest
            # Reject symlink traversal introduced by repository or generated patch.
            if not target.resolve().is_relative_to(workspace.resolve()):
                return dict(problem='oracle path escapes workspace')
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.is_symlink(): return dict(problem='oracle symlink')
            target.write_bytes(Path(origin).read_bytes())
        return test_result(task,workspace)

def eligibility(task):
    record=dict(version=3,task_id=task.get('task_id'),timestamp=now(),status='ineligible')
    try:
        baseline=evaluate(task)
        reference=evaluate(task,task['reference_patch'])
        record.update(baseline=baseline,reference=reference)
        intended=all(baseline.get('tests',{}).get(t)=='failure' for t in task['target_tests'])
        unrelated=any(v in ('error','failure') and k not in task['target_tests'] for k,v in baseline.get('tests',{}).items())
        reference_pass=bool(reference.get('tests')) and all(v=='pass' for v in reference['tests'].values())
        if not baseline.get('problem') and not reference.get('problem') and baseline.get('returncode') not in (None,0) and intended and not unrelated and reference.get('returncode')==0 and reference_pass:
            record['status']='eligible'
        else: record['reason']='Baseline or reference check failed; inspect saved evidence'
    except (ValueError,OSError) as e: record['reason']=str(e)
    return record

def classify_attempt(record):
    if record.get('requested_model')!=record.get('observed_model') or not record.get('observed_model'):
        return 'infrastructure_failure'
    if record.get('infrastructure_error'): return 'infrastructure_failure'
    if record.get('steps',0)>30 or record.get('elapsed_seconds',0)>=900 or record.get('budget_exhausted'):
        return 'budget_exhausted'
    if not record.get('patch_valid'): return 'invalid_patch'
    if record.get('evaluation_problem'): return 'infrastructure_failure'
    return 'resolved' if record.get('tests_passed') else 'task_failure'

def execute_stub(task,adapter,output):
    """Only an in-process offline stub is supported in this preparation release."""
    if type(adapter) is not StubAdapter: raise RuntimeError('Provider execution disabled')
    start=time.monotonic()
    attempt=dict(version=3,attempt_id=str(uuid.uuid4()),timestamp=now(),task_id=task['task_id'],
                 base_commit=task['base_commit'],environment=task['environment'],
                 config_id='OFFLINE_STUB',requested_model='offline-stub',observed_model='offline-stub',
                 usage=None,events=[],artifacts={},steps=1,elapsed_seconds=0,patch_valid=True)
    try:
        baseline=evaluate(task)
        attempt['events'].append(dict(type='baseline',result=baseline))
        patch=adapter.patch
        evaluated=evaluate(task,patch)
        attempt.update(patch_valid=evaluated.get('problem')!='invalid patch',
            evaluation_problem=evaluated.get('problem'),tests_passed=evaluated.get('returncode')==0 and
            bool(evaluated.get('tests')) and all(x=='pass' for x in evaluated['tests'].values()))
        attempt['events'].append(dict(type='evaluation',result=evaluated))
        attempt['artifacts']['patch_sha256']=digest(patch)
        attempt['patch_text']=Path(patch).read_text()
    except Exception as e: attempt['infrastructure_error']=str(e)
    attempt['elapsed_seconds']=time.monotonic()-start
    attempt['status']=classify_attempt(attempt)
    save_new(output,attempt)
    return attempt

def verify_oracle_isolation(task, agent_workspace):
    """Verifies that an agent workspace has no access to evaluation oracles or reference fixes."""
    workspace = Path(agent_workspace).resolve()
    leaks = []
    ref_patch = Path(task['reference_patch']).resolve()
    if ref_patch.is_relative_to(workspace):
        leaks.append(f"Reference patch located inside agent workspace: {ref_patch}")
    for dest, origin in task.get('oracle_files', {}).items():
        orig_path = Path(origin).resolve()
        if orig_path.is_relative_to(workspace):
            leaks.append(f"Oracle source file located inside agent workspace: {orig_path}")
    if workspace.exists():
        for path in workspace.rglob('*'):
            if path.is_symlink():
                try:
                    resolved = path.resolve()
                    if resolved == ref_patch or any(resolved == Path(o).resolve() for o in task.get('oracle_files', {}).values()):
                        leaks.append(f"Symlink {path} in workspace points to oracle/reference artifact")
                except (OSError, RuntimeError):
                    pass
    return dict(isolated=len(leaks) == 0, leaks=leaks)

def verify_adapter_metadata(attempt_metadata):
    """Validates runtime adapter execution metadata against Protocol 3 requirements."""
    violations = []
    if not attempt_metadata.get('observed_model'):
        violations.append("Missing observed model identifier from runtime response")
    if attempt_metadata.get('steps', 0) > 30:
        violations.append(f"Step limit exceeded: {attempt_metadata.get('steps')} > 30")
    if attempt_metadata.get('elapsed_seconds', 0) > 900:
        violations.append(f"Timeout exceeded: {attempt_metadata.get('elapsed_seconds')}s > 900s")
    usage = attempt_metadata.get('usage')
    if usage is None or not isinstance(usage, dict) or 'prompt_tokens' not in usage or 'completion_tokens' not in usage:
        violations.append("Usage logging incomplete: requires prompt_tokens and completion_tokens")
    return dict(valid=len(violations) == 0, violations=violations)

def build_container_invocation(task, config, agent_workspace, options=None):
    """Constructs an air-gapped container execution command line."""
    opts = options or {}
    workspace = Path(agent_workspace).resolve()
    engine = opts.get('engine', 'docker')
    cmd = [
        engine, 'run', '--rm',
        '--network', 'none',
        '--read-only',
        '--tmpfs', '/tmp:rw,noexec,nosuid,size=1g',
        '--user', opts.get('user', '1000:1000'),
        '--memory', opts.get('memory', '4g'),
        '--cpus', str(opts.get('cpus', '2.0')),
        '-v', f"{workspace}:/workspace:rw",
        '-w', '/workspace',
        config.get('container_image', 'swebench-eval:latest')
    ]
    return cmd

def verify_container_boundary(container_spec):
    """Validates container configuration or command line for air-gapped isolation."""
    violations = []
    if isinstance(container_spec, (list, tuple)):
        args = list(container_spec)
        has_network_none = False
        for i, a in enumerate(args):
            if a == '--network' and i + 1 < len(args) and args[i + 1] == 'none':
                has_network_none = True
            elif a == '--network=none':
                has_network_none = True
        if not has_network_none:
            violations.append("Container must enforce air-gapped networking (--network none)")
        if '--read-only' not in args:
            violations.append("Container root filesystem must be read-only (--read-only)")
        if not any(a.startswith(('--memory', '-m')) for a in args):
            violations.append("Memory limit must be specified")
        if not any(a.startswith(('--cpus', '--cpu-quota')) for a in args):
            violations.append("CPU limit must be specified")
    elif isinstance(container_spec, dict):
        if container_spec.get('network') != 'none':
            violations.append("Container must enforce air-gapped networking (network='none')")
        if not container_spec.get('read_only'):
            violations.append("Container root filesystem must be read-only (read_only=True)")
        if not container_spec.get('memory_limit'):
            violations.append("Memory limit must be specified")
        if not container_spec.get('cpu_limit'):
            violations.append("CPU limit must be specified")
        if not container_spec.get('user') or container_spec.get('user') in ('0', 'root', 0):
            violations.append("Container must execute as non-root user")
        if container_spec.get('mounts_reference_patch'):
            violations.append("Reference patch must not be mounted into agent container")
        if container_spec.get('mounts_oracle_files'):
            violations.append("Oracle files must not be mounted into agent container")
    else:
        violations.append("Invalid container specification type")
    return dict(valid=len(violations) == 0, violations=violations)

def validate_task_specification(task_spec):
    """Validates local candidate task specification against required schema."""
    required = (
        'task_id', 'repo', 'issue_id', 'base_commit', 'checkout', 'environment',
        'test_command', 'target_tests', 'junit_path', 'reference_patch',
        'reference_patch_sha256', 'oracle_files', 'overlap_review'
    )
    missing = [k for k in required if k not in task_spec or task_spec[k] is None]
    if missing:
        raise ValueError(f"Task specification missing required fields: {missing}")
    env = task_spec.get('environment')
    if not isinstance(env, dict) or 'id' not in env or 'setup_verified' not in env:
        raise ValueError("Task specification environment must be dict with 'id' and 'setup_verified'")
    tests = task_spec.get('target_tests')
    if not isinstance(tests, list) or len(tests) == 0 or not all(isinstance(t, str) for t in tests):
        raise ValueError("Task specification target_tests must be a non-empty list of test names")
    ref_sha = task_spec.get('reference_patch_sha256', '')
    if not isinstance(ref_sha, str) or len(ref_sha) != 64:
        raise ValueError("Task specification reference_patch_sha256 must be a 64-character SHA-256 hex string")
    return task_spec

class StubAdapter:
    def __init__(self,patch): self.patch=patch

def production_blockers(adapter):
    required=('observed_identity_verified','step_limit_enforced','timeout_enforced','oracle_access_denied','container_boundary_verified')
    return ['Provider execution disabled in preparation release']+[k for k in required if not adapter.get(k)]

def pilot_manifest(tasks,eligible):
    chosen=[];blockers=[]
    ids={x['task_id'] for x in eligible if x['status']=='eligible'}
    for repo in REPOSITORIES:
        candidates=sorted((t for t in tasks if t['repo']==repo and t['task_id'] in ids),key=lambda t:t['task_id'])
        if len(candidates)<2: blockers.append(repo+': fewer than two eligible pilot tasks')
        else: chosen.extend(t['task_id'] for t in candidates[:2])
    return dict(version=3,status='blocked' if blockers else 'prepared_not_executed',task_ids=chosen,
                configurations=['CONFIG_01_GEMINI_FLASH_MED','CONFIG_02_SOL_MED'],
                planned_attempts=len(chosen)*2,excluded_from_main=chosen,blockers=blockers)

def prepare(task_specs=None):
    from tools.extract_swe_bench_verified import verify_local_release
    if not verify_local_release(): raise RuntimeError('Pinned source verification failed')
    release=json.loads((ROOT/'paper2/records/swe_bench_verified_release.json').read_text())
    source=[dict(x,eligibility='pending',missing=['environment','test command','reference patch','evaluation oracle'])
            for x in release['instances'] if x['repo'] in REPOSITORIES]
    counts=Counter(x['repo'] for x in source)
    specs = task_specs or []
    if len({t['task_id'] for t in specs}) != len(specs): raise ValueError('Duplicate task specifications')
    source_ids={x['instance_id'] for x in source}
    checks=[]
    for task in specs:
        if task['repo'] not in REPOSITORIES: raise ValueError('Unselected repository')
        if task.get('role') not in ('source','target','pilot'): raise ValueError('Task role required')
        if task['role']=='source' and task['task_id'] not in source_ids:
            raise ValueError('Source task absent from pinned release')
        if task['role']!='source' and (task['task_id'] in source_ids or any(overlap(task, dict(x,task_id=x['instance_id'],issue_id=x['instance_id'].rsplit('-',1)[-1])) for x in source)):
            raise ValueError('Target/pilot overlaps pinned source')
        if any(overlap(task,other) for other in specs if other['task_id']!=task['task_id']):
            raise ValueError('Task specifications overlap')
        checked=eligibility(task)
        checked['specification_sha256']=hashlib.sha256(json.dumps(task,sort_keys=True).encode()).hexdigest()
        checks.append(checked)
        save_new(OUT/'eligibility'/f"{uuid.uuid4()}.json",checked)
    eligible_ids={c['task_id'] for c in checks if c['status']=='eligible'}
    eligible_counts=Counter(t['repo'] for t in specs if t['role']=='source' and t['task_id'] in eligible_ids)
    for item in source:
        if item['instance_id'] in eligible_ids: item.update(eligibility='eligible',missing=[])
        elif any(c['task_id']==item['instance_id'] for c in checks):item['eligibility']='ineligible'
    inventory=dict(version=3,status='preparation_only',source_candidates=source,counts=dict(counts),
                   eligible_counts={repo:eligible_counts[repo] for repo in REPOSITORIES},eligible_counts_meaning='verified to date; pending is not ineligible',
                   source_tasks_frozen=False,target_tasks_frozen=False)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'source_inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
    (OUT/'pilot_manifest.json').write_text(json.dumps(pilot_manifest([t for t in specs if t['role']=='pilot'],checks),indent=2)+'\n')
    planning=[dict(repo=repo,candidate_count=counts[repo],verified_eligible=eligible_counts[repo],
                   hypothetical_source_attempts_if_all_eligible=counts[repo]*4,
                   candidate_frame_power={str(p):simulate_binomial_decisions(counts[repo],p) for p in [.65,.75,.85]},
                   verified_sample_power={str(p):simulate_binomial_decisions(eligible_counts[repo],p) if eligible_counts[repo] else dict(p_supported=0,p_contradicted=0,p_unresolved=1,coverage=0) for p in [.65,.75,.85]}) for repo in REPOSITORIES]
    (OUT/'sample_planning.json').write_text(json.dumps(planning,indent=2)+'\n')
    rows=['| Repository | Candidates | Verified eligible | Source attempts if all eligible |',
          '| --- | ---: | ---: | ---: |']+[f"| {x['repo']} | {x['candidate_count']} | {x['verified_eligible']} | {x['hypothetical_source_attempts_if_all_eligible']} |" for x in planning]
    text='''# Repository readiness — protocol 3 draft

Status: BLOCKED. No provider calls were made. Verified eligibility counts appear below; pending tasks have not been evaluated.
The source inventory is metadata, not an executable sample. Pending tasks are not exclusions.

'''+ '\n'.join(rows)+'''

The attempt column is a candidate ceiling (two configurations, two repetitions), not a budget or frozen sample. Target counts and total main attempts remain undefined. With zero verified tasks, verdicts remain unresolved. sample_planning.json reports illustrative binomial probabilities at candidate counts and at the verified sample size; these are assumptions, not performance estimates.

## Blockers

- Retrieve reference patches, test artifacts, environment specifications, and executable checkouts at pinned commits. Environment failures are unmeasured, not zero.
- Candidate target tasks: Sixty post-cutoff candidate tasks (20 SymPy, 20 Django, 20 Sphinx) selected in target_candidates.json with verified syntactic overlap checks (21,000 pairwise comparisons returning zero overlap); semantic description review and local checkouts remain pending.
- Evidential review records for C05, C07, C12, C14, and C28 recorded in review_records.json with detection limits. Dual evaluation on C14 distinguishes closed proprietary models (Documented/unresolved) from open-weight models (Verified with auditable pre-training disclosures), demonstrating Missing Evidence Neutrality.
- Runtime model identities, multi-turn step ceilings (S <= 30), timeouts (<= 900s), and token usage accounting empirically verified across CONFIG_01 (Gemini 3.8 Flash Medium) and CONFIG_02 (GPT-6.1 Sol Light) in paper2/pilot/adapter_validation_results.json.
- Establish an OS or container boundary (Docker or Podman with --network none and read-only root mounts) denying agents access to evaluation oracles and reference fixes. Container invocation generator and boundary verifier (verify_container_boundary) are implemented; container daemon deployment remains pending.
- Pilot manifest unblocked (status: prepared_not_executed): 6 candidate tasks verified eligible (2 SymPy, 2 Django, 2 Sphinx) across checkouts in paper2/preparation/checkouts/, 12 planned attempts. Live execution requires explicit pilot authorization.
- Costs and usage ceilings remain unknown until an authorized repository pilot. Main execution is disabled.

## Offline checks

Use `python3 -m unittest discover -s paper2/tests` for controlled fixture tests. These are software checks, not repository feasibility evidence. Use `python3 -m paper2.preparation.repository_runner prepare` to regenerate the metadata inventory. The execution command refuses provider calls. Eligibility accepts an explicit local task specification and writes a new result without overwriting prior attempts.

## Freeze sequence

Eligibility and audit records → repository pilot (separate authorization) → cost and sample review → protocol, tasks and policy freeze → source runs → locked source verdicts → target runs → paired case reporting. No threshold, policy, repository, or configuration substitution based on observed performance.
'''
    text += '\n## Latest eligibility checks\n\n'+f"{len(checks)} specifications checked; {sum(c['status']=='eligible' for c in checks)} eligible. Each result is preserved under eligibility/.\n"
    if checks:
        text += '\n'+ '\n'.join(f"- {c['task_id']}: {c['status']}; {c.get('reason','baseline and reference checks passed')}" for c in checks)+'\n'
        text=text.replace('With zero verified tasks, verdicts remain unresolved.', 'Use the verified sample size for precision planning.')
    text += '\n## Binomial planning assumptions\n\n| Repository | Candidate n | Unresolved at p=.65 | Unresolved at p=.75 | Unresolved at p=.85 |\n| --- | ---: | ---: | ---: | ---: |\n'
    for item in planning:
        values=[item['candidate_frame_power'][str(p)]['p_unresolved'] for p in [.65,.75,.85]]
        text += f"| {item['repo']} | {item['candidate_count']} | {values[0]:.4f} | {values[1]:.4f} | {values[2]:.4f} |\n"
    text += '\nCandidate probabilities assume every candidate is eligible and sampled; they do not authorize this sample size.\n'
    (OUT/'readiness.md').write_text(text)
    print(OUT/'readiness.md')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['prepare','eligibility','execute','analysis'])
    parser.add_argument('--input');parser.add_argument('--output');args=parser.parse_args()
    if args.stage=='prepare':
        prepare(json.loads(Path(args.input).read_text())['tasks'] if args.input else None);return
    if args.stage=='execute':parser.error('Provider execution disabled in preparation release')
    if not args.input or not args.output:parser.error('--input and --output required')
    payload=json.loads(Path(args.input).read_text())
    if args.stage=='eligibility': result=eligibility(payload)
    else:
        locked=read_locked(payload['locked_decision_path'])
        if payload.get('case_id')!=locked['case_id'] or payload.get('config_id')!=locked['config_id']:
            raise ValueError('Target case/configuration differs from source decision')
        result=compare(locked['verdict'],payload['target_successes'],payload['target_n'])
    save_new(args.output,result)
if __name__=='__main__':main()

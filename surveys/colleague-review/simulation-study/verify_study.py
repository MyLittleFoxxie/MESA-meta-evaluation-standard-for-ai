#!/usr/bin/env python3
"""Verify frozen inputs and recorded execution integrity without modifying raw data."""
from pathlib import Path
import argparse, collections, datetime, hashlib, json, re
from analyze import read, observations, event_kind, attempt_layout

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(root):
    issues=[];warnings=[];checks=0
    def check(ok,message):
        nonlocal checks
        checks+=1
        if not ok: issues.append(message)
    freeze=read(root/'freeze-manifest.json');manifest=read(root/'jobs.json')
    jobs=manifest.get('jobs',[]) if isinstance(manifest,dict) else manifest
    check(len(jobs)==freeze['jobs'],'Job count differs from freeze')
    check(len({j['id'] for j in jobs})==len(jobs),'Duplicate job IDs')
    for path,digest in freeze['files'].items():
        p=root/path;check(p.is_file() and sha(p)==digest,'Frozen file changed or missing: '+path)
    key=read(root/'analyst/expected.json')
    check('analyst/expected.json' in freeze['files'],'Expected answers not included in freeze')
    frozen_time=datetime.datetime.fromisoformat(freeze['frozen_utc'])
    threads=[];attempted=0;completed=0;tool_count=0;infrastructure_count=0;physical_attempts=0;physical_statuses=collections.Counter()
    counts=collections.Counter((j['batch'],j['condition'],j['role']) for j in jobs)
    for group,n in counts.items(): check(n==5,'Expected five planned sessions: '+str(group))
    materials={f:(root/'materials'/f).read_text() for f in ['mesa.txt','efpa-original.txt','real-passages.txt']}
    controlled=read(root/'materials/controlled-cases.json')
    for j in jobs:
        path=root/j.get('input',j.get('path',j.get('input_path','')))
        check(path.is_file() and sha(path)==j.get('sha256',j.get('input_sha256')),'Job input digest mismatch: '+j['id'])
        text=path.read_text()
        if j['condition']=='mesa': check(materials['mesa.txt'] in text,'MESA instrument missing: '+j['id'])
        else: check(materials['mesa.txt'] not in text,'MESA questionnaire leaked to other condition: '+j['id'])
        if j['condition']=='efpa': check(materials['efpa-original.txt'] in text,'Original EFPA extraction missing: '+j['id'])
        else: check(materials['efpa-original.txt'] not in text,'EFPA extraction leaked to other condition: '+j['id'])
        if j['batch']=='real':
            check(materials['real-passages.txt'] in text,'Real passages missing: '+j['id'])
            check(not any(c['passage'] in text for c in controlled),'Fictional passage leaked into real run: '+j['id'])
        else:
            check(all(c['passage'] in text for c in controlled),'Fictional passage missing: '+j['id'])
            check(materials['real-passages.txt'] not in text,'Real passage bundle leaked to controlled run: '+j['id'])
        for cid,probes in key['cases'].items():
            for pid,p in probes.items(): check(p['reason'] not in text,'Expected answer reason leaked: '+j['id']+'/'+cid+'/'+pid)
        folder=root/'outputs'/j['id']
        paths,permitted,retry_errors=attempt_layout(folder)
        for error in retry_errors: check(False,j['id']+': '+error)
        if any(number==1 for number,_ in paths): attempted+=1
        original=read(folder/'metadata.json') if (folder/'metadata.json').exists() else {}
        for number,d in paths:
            label=j['id']+'/attempt-'+str(number)
            m=read(d/'metadata.json');physical_attempts+=1;physical_statuses[m.get('status','unknown')]+=1
            if number==2:
                check(permitted,'Retry original failure condition not met: '+label)
                check(bool(original.get('finished_at')),'Retry original has no finish timestamp: '+label)
                if original.get('finished_at'):
                    check(datetime.datetime.fromisoformat(m['started_at'])>=datetime.datetime.fromisoformat(original['finished_at']),'Retry predates original completion: '+label)
            check(datetime.datetime.fromisoformat(m['started_at'])>=frozen_time,'Run predates freeze: '+label)
            check(m.get('input_sha256')==sha(path),'Recorded input mismatch: '+label)
            if m.get('finished_at'):
                check(datetime.datetime.fromisoformat(m['finished_at'])>=datetime.datetime.fromisoformat(m['started_at']),'Run finishes before start: '+label)
            check(m.get('elapsed_seconds',0)>=0,'Negative elapsed duration: '+label)
            check(m.get('attempt')==number,'Unexpected attempt value: '+label)
            check(m.get('cwd_empty_at_start') is True,'Session directory not empty initially: '+label)
            check(not m.get('workdir_files_after',[]),'Files created in session directory: '+label)
            check(not m.get('non_json_event_lines',[]),'Unparseable event lines: '+label)
            obs=observations(d,m)
            check(not (obs['tool_events'] or obs['recorded_actual_tool_items']),'Tool calls recorded: '+label)
            tool_count+=max(obs['tool_events'],obs['recorded_actual_tool_items'])
            infrastructure_count+=obs['infrastructure_error_events']
            for name,digest in m.get('output_files_sha256',{}).items(): check((d/name).is_file() and sha(d/name)==digest,'Output hash mismatch: '+label+'/'+name)
            threads+=m.get('thread_ids',[])
            if m.get('status')=='process_completed' and m.get('turn_completed'):
                completed+=1;check(len(m.get('thread_ids',[]))==1,'Completed run has nonunique thread allocation: '+label)
            # Independently derive tool events and final text; metadata alone is not authoritative.
            if (d/'events.jsonl').exists():
                events=[]
                for line in (d/'events.jsonl').read_text().splitlines():
                    try: events.append(json.loads(line))
                    except ValueError: pass
                tools=[e for e in events if isinstance(e,dict) and event_kind(e)=='tool']
                check(not tools,'Tool events present independently: '+label)
                msgs=[e['item'].get('text','') for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
                if msgs: check((d/'response.txt').exists() and (d/'response.txt').read_text()==msgs[-1],'Saved response differs from final event: '+label)
    check(len(threads)==len(set(threads)),'Thread reused across sessions')
    expected_ids={j['id'] for j in jobs}
    unexpected=[p.name for p in (root/'outputs').iterdir() if p.is_dir() and p.name not in expected_ids] if (root/'outputs').exists() else []
    check(not unexpected,'Unexpected output directories: '+str(unexpected))
    warnings+=['No filesystem/tool observations establish removal of pretrained knowledge or all platform-provided context.','Full EFPA source in prompts does not establish complete EFPA application in responses; inspect instrument_reviews.csv.','Frozen timestamp is local execution provenance, not third-party preregistration.']
    if attempted<len(jobs): warnings.append(f'{len(jobs)-attempted} planned runs have not been attempted.')
    result={'checks':checks,'passed':not issues,'issues':issues,'warnings':warnings,'planned':len(jobs),'attempted':attempted,'physical_attempts':physical_attempts,'physical_status_counts':dict(physical_statuses),'process_and_turn_completed':completed,'distinct_threads':len(set(threads)),'actual_tool_events_or_items':tool_count,'infrastructure_error_events':infrastructure_count}
    out=root/'analysis';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args();result=verify(args.root);print(json.dumps(result,indent=2));raise SystemExit(0 if result['passed'] else 1)

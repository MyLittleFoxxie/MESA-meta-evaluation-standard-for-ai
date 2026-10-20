#!/usr/bin/env python3
"""Deterministic descriptive analysis. Never repairs or judges raw prose with an LLM."""
from pathlib import Path
import argparse, collections, csv, itertools, json, re
CHOICES = ['Yes','Partly','No','Not sure','Not applicable']
LABELS = ['Supported','Contradicted','Not established']
FIELDS = ['supported_claims','documented_problems','missing_information','reinterpretations']
def read(p): return json.loads(Path(p).read_text())
def event_kind(event):
    """Classify CLI records conservatively; item.error and failed results are infrastructure, not tools."""
    # Claude Code stream-json: a content block itself (from metadata tool_items) or an assistant/user/result event.
    if event.get('type') in ('tool_use', 'tool_result', 'server_tool_use'):
        return 'tool'
    if event.get('type') == 'result' and event.get('is_error'):
        return 'infrastructure_error'
    if event.get('type') in ('assistant', 'user'):
        blocks = (event.get('message') or {}).get('content') or []
        if any(isinstance(b, dict) and b.get('type') in ('tool_use', 'tool_result', 'server_tool_use') for b in blocks):
            return 'tool'
        return 'other'
    item = event.get('item', {})
    kind = item.get('type') if isinstance(item, dict) else None
    if kind == 'error' or event.get('type') in ('error', 'turn.failed'):
        return 'infrastructure_error'
    if event.get('type', '').startswith('item.') and kind not in (None, 'agent_message', 'reasoning'):
        return 'tool'
    return 'other'

def observations(folder, meta):
    events = []
    if (folder/'events.jsonl').exists():
        for line in (folder/'events.jsonl').read_text().splitlines():
            try:
                event = json.loads(line)
                if isinstance(event, dict): events.append(event)
            except ValueError:
                pass
    # Metadata is kept untouched; historical tool_items also included item.error.
    recorded = [e for e in meta.get('tool_items', []) if isinstance(e, dict)]
    return {'tool_events':sum(event_kind(e)=='tool' for e in events),
            'recorded_actual_tool_items':sum(event_kind(e)=='tool' for e in recorded),
            'infrastructure_error_events':sum(event_kind(e)=='infrastructure_error' for e in events),
            'recorded_infrastructure_error_items':sum(event_kind(e)=='infrastructure_error' for e in recorded)}

def synthetic_auth_failure(folder):
    """Recognize the retained CLI login error, never a generated study response."""
    response=folder/'response.txt'; eventfile=folder/'events.jsonl'
    if not response.exists() or response.read_text()!='Not logged in · Please run /login' or not eventfile.exists():return False
    try:events=[json.loads(line) for line in eventfile.read_text().splitlines()]
    except ValueError:return False
    messages=[e for e in events if e.get('type')=='assistant']
    results=[e for e in events if e.get('type')=='result']
    return bool(messages and results) and all(e.get('message',{}).get('model')=='<synthetic>' and e.get('error')=='authentication_failed' for e in messages) and all(e.get('is_error') and not e.get('modelUsage') and e.get('usage',{}).get('input_tokens',0)==0 and e.get('usage',{}).get('output_tokens',0)==0 for e in results)

def attempt_layout(folder):
    """Return physical attempt directories and protocol violations without editing evidence."""
    paths=[(1,folder)] if (folder/'metadata.json').exists() else []
    issues=[]
    retries=sorted(p for p in folder.glob('attempt-*') if p.is_dir())
    for retry in retries:
        if retry.name!='attempt-2': issues.append('Unexpected retry directory: '+retry.name)
        if (retry/'metadata.json').exists():
            number=2 if retry.name=='attempt-2' else retry.name
            paths.append((number,retry))
        if list(retry.glob('attempt-*')): issues.append('Nested retry directory: '+retry.name)
    original=read(folder/'metadata.json') if (folder/'metadata.json').exists() else {}
    has_response=(folder/'response.txt').exists() and bool((folder/'response.txt').read_text().strip())
    completed_event=False
    if (folder/'events.jsonl').exists():
        for line in (folder/'events.jsonl').read_text().splitlines():
            try: event=json.loads(line)
            except ValueError: continue
            if isinstance(event,dict) and (event.get('type')=='turn.completed' or event.get('type')=='item.completed' and event.get('item',{}).get('type')=='agent_message'
                                           or event.get('type')=='result' and event.get('subtype')=='success' and not event.get('is_error')):
                completed_event=True
    permitted=original.get('status') in ('process_failed','timeout','launcher_failed') and not original.get('turn_completed') and (not has_response or synthetic_auth_failure(folder)) and not completed_event
    if retries and not permitted: issues.append('Retry not permitted: original was not a process failure without a completed turn or response')
    return paths,permitted,issues

def norm(s): return ' '.join(s.split())
def parse(text):
    text=text.strip()
    if text.startswith('```'):
        m=re.fullmatch(r'```(?:json)?\s*\n(.*?)\n```',text,re.S)
        if not m: raise ValueError('Invalid surrounding Markdown fence')
        text=m.group(1)
    def unique(pairs):
        d={}
        for k,v in pairs:
            if k in d: raise ValueError('Duplicate JSON key: '+k)
            d[k]=v
        return d
    d=json.loads(text,object_pairs_hook=unique)
    if not isinstance(d,dict): raise ValueError('Top-level response is not an object')
    return d

def validate(d,job,key):
    errors=[]
    def fail(ok,msg):
        if not ok: errors.append(msg)
    if job['batch']=='real':
        reviews=d.get('reviews')
        if not isinstance(reviews,list): return ['reviews is not an array']
        fail([x.get('benchmark') if isinstance(x,dict) else None for x in reviews]==['arc','designqa'],'reviews must be arc then designqa exactly once')
        for review in reviews:
            if not isinstance(review,dict): errors.append('review not object');continue
            name=review.get('benchmark','?')
            fail(isinstance(review.get('instrument_review'),str) and bool(review.get('instrument_review','').strip()),name+': missing instrument_review')
            fail(isinstance(review.get('closing_note'),str),name+': missing closing_note')
            for field in FIELDS:
                fail(isinstance(review.get(field),list) and all(isinstance(v,str) for v in review.get(field,[])),name+': invalid '+field)
            if job['condition']=='mesa':
                answers=review.get('mesa_answers')
                if not isinstance(answers,list): errors.append(name+': missing mesa_answers');continue
                ids=[a.get('id') for a in answers if isinstance(a,dict)]
                fail(len(answers)==25 and len(ids)==25 and all(type(i)==int for i in ids) and sorted(ids)==list(range(1,26)),name+': IDs must be 1..25 exactly once')
                fail(all(isinstance(a,dict) and a.get('choice') in CHOICES for a in answers),name+': invalid choice')
            elif review.get('mesa_answers') not in (None,[]):
                errors.append(name+': non-MESA condition supplied MESA answers')
    else:
        cases=d.get('cases')
        if not isinstance(cases,list): return ['cases is not an array']
        ids=[c.get('id') for c in cases if isinstance(c,dict)]
        fail(len(ids)==len(cases) and sorted(ids)==sorted(key),'case IDs missing, duplicated, or unexpected')
        fail(isinstance(d.get('closing_note'),str),'missing closing_note')
        for c in cases:
            if not isinstance(c,dict): errors.append('case not object');continue
            cid=c.get('id'); probes=c.get('probes')
            fail(isinstance(c.get('instrument_review'),str) and bool(c.get('instrument_review','').strip()),str(cid)+': missing instrument_review')
            if not isinstance(probes,list): errors.append(str(cid)+': probes not array');continue
            pids=[p.get('id') for p in probes if isinstance(p,dict)]
            fail(len(pids)==len(probes) and sorted(pids)==sorted(key.get(cid,{})),str(cid)+': probe IDs missing, duplicated, or unexpected')
            for p in probes:
                fail(isinstance(p,dict) and p.get('label') in LABELS and isinstance(p.get('quote'),str) and isinstance(p.get('reason'),str),str(cid)+': malformed probe')
    return errors

# Post-freeze export refinement: inspect text in every response field, not only its summary.
ID_PATTERN = r'(?<![\d.])(?:[1-9]|1[0-2])(?:\.\d+){1,4}(?!\d|\.\d)'
def id_sort(value): return tuple(map(int,value.split('.')))
def efpa_inventory(text):
    inventory=collections.defaultdict(list)
    for number,line in enumerate(text.splitlines(),1):
        match=re.match(r'^\s*('+ID_PATTERN+r')',line)
        if match: inventory[match[1]].append((number,line))
    return inventory

def text_fields(value,path=''):
    if isinstance(value,str): yield path,value
    elif isinstance(value,dict):
        for name,child in value.items(): yield from text_fields(child,(path+'.' if path else '')+str(name))
    elif isinstance(value,list):
        for index,child in enumerate(value): yield from text_fields(child,path+'['+str(index)+']')

def efpa_mentions(review,source_ids):
    """Lexical locations only. Expand ascending same-parent numeric ranges conservatively."""
    mentions=set()
    for location,text in text_fields(review):
        for identifier in re.findall(ID_PATTERN,text):
            if identifier in source_ids: mentions.add((identifier,location,'explicit'))
        range_pattern=r'('+ID_PATTERN+r')\s*[-–—]\s*((?:[1-9]|1[0-2])(?:\.\d+){1,4}|\d+)(?!\d|\.\d)'
        for match in re.finditer(range_pattern,text):
            first,last=match[1],match[2]
            prefix,start=first.rsplit('.',1)
            if '.' not in last: last=prefix+'.'+last
            end_prefix,end=last.rsplit('.',1)
            if prefix!=end_prefix or not 0<=int(end)-int(start)<=1000: continue
            for n in range(int(start)+1,int(end)):
                identifier=prefix+'.'+str(n)
                if identifier in source_ids: mentions.add((identifier,location,'range_expanded'))
    return sorted(mentions,key=lambda row:(id_sort(row[0]),row[1],row[2]))

def csvout(path,rows,fields):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def analyze(root):
    manifest=read(root/'jobs.json');jobs=manifest.get('jobs',[]) if isinstance(manifest,dict) else manifest
    key=read(root/'analyst/expected.json')['cases']
    passages={c['id']:c['passage'] for c in read(root/'materials/controlled-cases.json')}
    out=root/'analysis';out.mkdir(exist_ok=True)
    source_path=root/'materials/efpa-original.txt'
    inventory=efpa_inventory(source_path.read_text()) if source_path.exists() else {}
    source_ids=set(inventory);mention_rows=[]
    csvout(out/'efpa_source_id_inventory.csv',[{'source_id':identifier,'source_line':line,'source_text':text} for identifier in sorted(inventory,key=id_sort) for line,text in inventory[identifier]],['source_id','source_line','source_text'])
    runs=[];probes=[];answers=[];conclusions=[];native=[];contrasts=[];models=collections.Counter();physical=[];retry_issues=[]
    for j in jobs:
        folder=root/'outputs'/j['id']; base={k:j[k] for k in ['id','batch','condition','role','repeat']}
        paths,permitted,issues=attempt_layout(folder)
        retry_issues.extend(j['id']+': '+issue for issue in issues)
        attempts=[]
        for number,attempt_folder in paths:
            meta=read(attempt_folder/'metadata.json')
            row={**base,'attempt':number,'status':meta.get('status','not_attempted'),'turn_completed':bool(meta.get('turn_completed')),'json_valid':False,'schema_valid':False,'eligible':False,'errors':''}
            models[meta.get('requested_model','unreported')]+=1
            data=None
            if (attempt_folder/'response.txt').exists():
                try: data=parse((attempt_folder/'response.txt').read_text());row['json_valid']=True
                except (ValueError,TypeError) as exc: row['errors']=str(exc)
            if data is not None:
                try: errors=validate(data,j,key)
                except (ValueError,TypeError,KeyError,AttributeError) as exc: errors=['Malformed schema: '+str(exc)]
                row['schema_valid']=not errors;row['errors']='; '.join(errors)
            row.update(observations(attempt_folder,meta))
            row['eligible']=not (row['tool_events'] or row['recorded_actual_tool_items']) and row['schema_valid'] and row['status']=='process_completed' and row['turn_completed']
            physical.append(row.copy());attempts.append((number,row,data))
        chosen=next((a for a in attempts if a[0]==1),None)
        if permitted:
            chosen=next((a for a in attempts if a[0] in (1,2) and a[1]['eligible']),chosen)
            if chosen is not None and chosen[0]==1 and not chosen[1]['eligible']:
                chosen=next((a for a in attempts if a[0]==2),chosen)
        if chosen is None:
            row={**base,'status':'not_attempted','turn_completed':False,'json_valid':False,'schema_valid':False,'eligible':False,'errors':'',**observations(folder,{})};d=None
        else:
            _,row,d=chosen;row=row.copy();row.pop('attempt')
        row.update({'chosen_attempt':chosen[0] if chosen else '', 'physical_attempts':len(paths),'retry_protocol_errors':'; '.join(issues)})
        runs.append(row)
        if not row['eligible']: continue
        if j['batch']=='controlled':
            for case in d['cases']:
                for p in case['probes']:
                    expected=key[case['id']][p['id']]['label']
                    probes.append({**base,'case':case['id'],'probe':p['id'],'label':p['label'],'expected':expected,'match':p['label']==expected,'quote_substring':bool(norm(p['quote'])) and norm(p['quote']) in norm(passages[case['id']]),'quote':p['quote'],'reason':p['reason']})
            labels={(p['case'],p['probe']):p['label'] for p in probes if p['id']==j['id']}
            comparisons=[('C1-C5','repeat_test','C1','repeat_test','C5','repeat_test'),('C1-C5','stable','C1','stable','C5','stable'),('C3-C4','repeat_test','C3','repeat_test','C4','repeat_test'),('C3-C4','stable','C3','stable','C4','stable'),('C6-C7','narrow','C6','narrow','C7','narrow'),('C6-C7','broad','C6','broad','C7','broad'),('C8','before-after','C8','before','C8','after')]
            for comparison,probe,c1,p1,c2,p2 in comparisons:
                if (c1,p1) not in labels or (c2,p2) not in labels: continue
                a,z=labels[c1,p1],labels[c2,p2]
                contrasts.append({**base,'comparison':comparison,'probe':probe,'first_label':a,'second_label':z,'same_label':a==z,'both_match_key':a==key[c1][p1]['label'] and z==key[c2][p2]['label'],'safety_label':labels.get(('C8','safety'),'') if comparison=='C8' else ''})
        else:
            for r in d['reviews']:
                for a in r.get('mesa_answers',[]): answers.append({**base,'benchmark':r['benchmark'],'question':a['id'],'choice':a['choice'],'comment':a.get('comment','')})
                for field in FIELDS:
                    for i,text in enumerate(r[field]): conclusions.append({**base,'benchmark':r['benchmark'],'field':field,'index':i+1,'text':text})
                text=r['instrument_review']
                ids=sorted(set(re.findall(r'(?<![\d.])(?:[1-9]|1[0-2])(?:\.\d+){1,4}(?![\d.])',text)))
                mentions=efpa_mentions(r,source_ids)
                for identifier,location,mode in mentions:
                    mention_rows.append({**base,'benchmark':r['benchmark'],'source_id':identifier,'location':location,'mention_mode':mode})
                mentioned={m[0] for m in mentions};explicit={m[0] for m in mentions if m[2]=='explicit'}
                native.append({**base,'benchmark':r['benchmark'],'numbered_ids':'; '.join(ids),'numbered_id_count':len(ids),'instrument_review':text,'closing_note':r['closing_note'],'full_review_json':json.dumps(r,ensure_ascii=False),'combined_all_fields':'\n\n'.join(location+':\n'+value for location,value in text_fields(r)),'source_id_inventory_count':len(source_ids),'whole_review_explicit_source_ids':'; '.join(sorted(explicit,key=id_sort)),'whole_review_source_ids_with_ranges':'; '.join(sorted(mentioned,key=id_sort)),'source_ids_unmentioned_for_manual_audit':'; '.join(sorted(source_ids-mentioned,key=id_sort))})
    groups=[]
    for (batch,condition,role), js in itertools.groupby(sorted(jobs,key=lambda j:(j['batch'],j['condition'],j['role'])),key=lambda j:(j['batch'],j['condition'],j['role'])):
        js=list(js); rr=[r for r in runs if (r['batch'],r['condition'],r['role'])==(batch,condition,role)]
        pp=[p for p in probes if p['condition']==condition and p['role']==role] if batch=='controlled' else []
        groups.append({'batch':batch,'condition':condition,'role':role,'planned':len(js),'attempted':sum(r['status']!='not_attempted' for r in rr),'process_completed':sum(r['status']=='process_completed' and r['turn_completed'] for r in rr),'eligible':sum(r['eligible'] for r in rr),'excluded_or_unattempted':sum(not r['eligible'] for r in rr),'probe_denominator':len(pp),'probe_matches':sum(p['match'] for p in pp),'quote_substring_matches':sum(p['quote_substring'] for p in pp)})
    distributions=[]
    for role in sorted({j['role'] for j in jobs}):
        for b in ['arc','designqa']:
            for q in range(1,26):
                aa=[a for a in answers if a['role']==role and a['benchmark']==b and a['question']==q]
                counts=collections.Counter(a['choice'] for a in aa)
                distributions.append({'role':role,'benchmark':b,'question':q,'valid_run_denominator':len(aa),**{c:counts[c] for c in CHOICES}})
    agreement=[]
    for kind in ['within_role','cross_role_matched_repeat']:
        for b in ['arc','designqa']:
            for q in range(1,26):
                aa=[a for a in answers if a['benchmark']==b and a['question']==q]
                pairs=[(a,z) for a,z in itertools.combinations(aa,2) if (a['role']==z['role'] if kind=='within_role' else a['role']!=z['role'] and a['repeat']==z['repeat'])]
                pg=collections.defaultdict(list)
                for a,z in pairs:
                    label=a['role'] if kind=='within_role' else '|'.join(sorted([a['role'],z['role']]))
                    pg[label].append(a['choice']==z['choice'])
                for label,values in pg.items(): agreement.append({'comparison':kind,'roles':label,'benchmark':b,'question':q,'pair_denominator':len(values),'matches':sum(values),'fraction':sum(values)/len(values)})
    probe_summary=[]
    for c in sorted({j['condition'] for j in jobs}):
        for cid, ps in key.items():
            for pid in ps:
                pp=[p for p in probes if (p['condition'],p['case'],p['probe'])==(c,cid,pid)]
                probe_summary.append({'condition':c,'case':cid,'probe':pid,'expected':ps[pid]['label'],'denominator':len(pp),'matches':sum(p['match'] for p in pp),**{l:sum(p['label']==l for p in pp) for l in LABELS}})
    run_scores=[]
    for r in runs:
        if r['batch']=='controlled':
            pp=[p for p in probes if p['id']==r['id']]
            run_scores.append({'id':r['id'],'condition':r['condition'],'role':r['role'],'repeat':r['repeat'],'eligible':r['eligible'],'probe_denominator':len(pp),'matches':sum(p['match'] for p in pp)})
    tables=[('physical_attempts',physical,list(physical[0]) if physical else ['id','attempt','status']),('efpa_id_mentions',mention_rows,['id','batch','condition','role','repeat','benchmark','source_id','location','mention_mode']),('controlled_contrasts',contrasts,['id','batch','condition','role','repeat','comparison','probe','first_label','second_label','same_label','both_match_key','safety_label']),('runs',runs,list(runs[0]) if runs else []),('controlled_probes',probes,['id','batch','condition','role','repeat','case','probe','label','expected','match','quote_substring','quote','reason']),('mesa_answers',answers,['id','batch','condition','role','repeat','benchmark','question','choice','comment']),('conclusions',conclusions,['id','batch','condition','role','repeat','benchmark','field','index','text']),('instrument_reviews',native,['id','batch','condition','role','repeat','benchmark','numbered_ids','numbered_id_count','instrument_review','closing_note','full_review_json','combined_all_fields','source_id_inventory_count','whole_review_explicit_source_ids','whole_review_source_ids_with_ranges','source_ids_unmentioned_for_manual_audit']),('mesa_distributions',distributions,['role','benchmark','question','valid_run_denominator']+CHOICES),('mesa_agreement',agreement,['comparison','roles','benchmark','question','pair_denominator','matches','fraction']),('controlled_summary',probe_summary,['condition','case','probe','expected','denominator','matches']+LABELS),('controlled_run_scores',run_scores,['id','condition','role','repeat','eligible','probe_denominator','matches'])]
    for name,rows,fields in tables: csvout(out/(name+'.csv'),rows,fields)
    summary={'physical_attempt_count':len(physical),'physical_status_counts':dict(collections.Counter(r['status'] for r in physical)),'retry_protocol_issues':retry_issues,'requested_models':dict(models),'status_counts':dict(collections.Counter(r['status'] for r in runs)),'infrastructure_error_events':sum(r['infrastructure_error_events'] for r in physical),'runs_with_actual_tool_events':sum(bool(r['tool_events'] or r['recorded_actual_tool_items']) for r in runs),'planned_runs':len(jobs),'attempted_runs':sum(r['status']!='not_attempted' for r in runs),'eligible_runs':sum(r['eligible'] for r in runs),'groups':groups,'controlled_valid_probes':len(probes),'controlled_matches':sum(p['match'] for p in probes),'mesa_valid_answers':len(answers),'limitations':['Only process-completed, turn-completed, wholly schema-valid responses without observed tool use enter quantitative tables. All excluded and unattempted runs remain in runs.csv.','No independence assumed across items, pairs, or repeated runs. No inferential significance tests.','Exact quotes are whitespace-normalized substring checks, not semantic support judgments.','Numbered EFPA item mentions are lexical observations, not evidence of a complete EFPA review. Summaries or headings alone do not establish full application.','Real-case conclusions have no correctness key and require qualitative examination.','Same assistant designed and analyzed this study; no independent human validation.']}
    if summary['status_counts'].get('process_completed',0) < summary['planned_runs']:
        summary['limitations'].insert(0,'Execution is incomplete: failed, running, or unattempted jobs limit model confirmation and condition comparisons.')
    elif summary['eligible_runs'] < summary['planned_runs']:
        summary['limitations'].insert(0,'All planned jobs completed, but invalid or otherwise ineligible outputs leave some analysis groups unbalanced; exclusions are retained without replacement.')
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (out/'series_summary.json').write_text(json.dumps({k:summary[k] for k in ['physical_attempt_count','physical_status_counts','retry_protocol_issues','requested_models','status_counts','planned_runs','attempted_runs','eligible_runs','infrastructure_error_events','runs_with_actual_tool_events']},indent=2)+'\n')
    lines=['# Recorded simulation results','',f"Attempted {summary['attempted_runs']} / {len(jobs)} planned runs; {summary['eligible_runs']} eligible for quantitative analysis.",'','| Batch | Condition | Role | Eligible/planned | Controlled matches/valid probes |','|---|---|---|---:|---:|']
    for g in groups: lines.append(f"| {g['batch']} | {g['condition']} | {g['role']} | {g['eligible']}/{g['planned']} | {g['probe_matches']}/{g['probe_denominator']} |")
    lines+=['','MESA choices are categories, not quality scores. Controlled matches refer only to the frozen fictional-case key. Missing and invalid runs are excluded and reported separately, not silently marked correct or incorrect.','','## Limits','']+['- '+s for s in summary['limitations']]
    lines+=['','## Files','','`runs.csv` contains every planned run and validation errors. `controlled_probes.csv` contains each eligible probe and its quote check. `controlled_run_scores.csv` preserves the session as the analysis unit. `controlled_contrasts.csv` compares labels within eligible sessions against the frozen paired-case design without judging prose. `mesa_distributions.csv` includes all five categories, including zero counts. `mesa_agreement.csv` reports within-role and matched-repeat cross-role pairs; pairs are dependent. `conclusions.csv` and `instrument_reviews.csv` retain prose for qualitative inspection.','']
    (out/'README.md').write_text('''# Analysis export refinement\n\nAfter inspecting response placement, analysis now retains each complete real-case review in `instrument_reviews.csv` (`full_review_json` and `combined_all_fields`). Existing `numbered_ids` and `numbered_id_count` describe `instrument_review` only. Detailed EFPA discussion can occur in conclusion arrays; summary-field counts cannot establish review completeness.\n\n`efpa_source_id_inventory.csv` lists hierarchical numeric identifiers found at the start of source extraction lines, with their lines for manual checking. This mechanical inventory can include numeric artifacts and omits headings without recognizable numeric labels. `efpa_id_mentions.csv` locates explicit inventory identifiers throughout every review field and expands only ascending numeric ranges with the same parent. Grouped references, parent references, paraphrases, and ambiguous ranges are not resolved. Numeric coincidences may be false matches. The unmentioned-ID list is a manual-audit aid, never a semantic completeness or quality judgment. Text and parsed JSON content are preserved; original response files retain original formatting.\n\n`physical_attempts.csv` retains every recorded execution and its original status/errors. `runs.csv` has one row per planned job and identifies its selected attempt. A second attempt may replace only an original process failure with no completed turn or response; completed invalid responses cannot be replaced. Unsupported retry directories are reported as protocol violations.\n\nThis is a post-freeze descriptive export refinement; no prompts, raw responses, eligibility criteria, or expected answers were changed by this refinement.\n''')
    (out/'summary.md').write_text('\n'.join(lines))
    return summary
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    a=p.parse_args();print(json.dumps(analyze(a.root),indent=2))

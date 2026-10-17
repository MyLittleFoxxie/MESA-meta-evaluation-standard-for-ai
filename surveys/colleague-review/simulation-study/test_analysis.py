#!/usr/bin/env python3
"""Synthetic calculation checks; never writes to the recorded study outputs."""
import copy, csv, json, tempfile
from pathlib import Path
from analyze import analyze, parse, validate, event_kind, observations, efpa_inventory, efpa_mentions

def write(p,d):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d))

def main():
    assert event_kind({'type':'item.completed','item':{'type':'error'}})=='infrastructure_error'
    assert event_kind({'type':'item.started','item':{'type':'command_execution'}})=='tool'
    assert event_kind({'type':'item.completed','item':{'type':'agent_message'}})=='other'
    inventory=efpa_inventory('9.3.1 First\n9.3.2 Second\n9.3.3 Third\n9.4.1 Other\nNot a heading 9.5.1')
    assert set(inventory)=={'9.3.1','9.3.2','9.3.3','9.4.1'}
    mentions=efpa_mentions({'instrument_review':'Short summary','supported_claims':['9.3.1–9.3.3 documented'],'missing_information':['9.4.1 absent']},set(inventory))
    assert ('9.3.2','supported_claims[0]','range_expanded') in mentions
    assert ('9.4.1','missing_information[0]','explicit') in mentions
    assert not any(location=='instrument_review' for _,location,_ in mentions)
    study=Path(__file__).resolve().parent
    key=json.loads((study/'analyst/expected.json').read_text())
    cases=json.loads((study/'materials/controlled-cases.json').read_text())
    try: parse('{"reviews":[],"reviews":[]}')
    except ValueError: pass
    else: raise AssertionError('duplicate keys accepted')
    assert parse('```json\n{"cases":[]}\n```')=={'cases':[]}
    with tempfile.TemporaryDirectory(prefix='mesa-analysis-check-') as tmp:
        root=Path(tmp);write(root/'analyst/expected.json',key);write(root/'materials/controlled-cases.json',cases)
        (root/'materials/efpa-original.txt').write_text('9.3.1 First\n9.3.2 Second\n9.3.3 Third\n9.4.1 Other')
        jobs=[]
        for n in range(1,6):
            job={'id':f'real-mesa-neutral-{n}','batch':'real','condition':'mesa','role':'neutral','repeat':n};jobs.append(job)
            review={'instrument_review':'Synthetic test only','supported_claims':['9.3.1–9.3.3 Synthetic detailed discussion'],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':''}
            reviews=[]
            for b in ['arc','designqa']:
                r={**review,'benchmark':b,'mesa_answers':[{'id':q,'choice':'Yes'} for q in range(1,26)]}
                if n==4: r['mesa_answers'][0]['choice']='No'
                if n==5: r['mesa_answers'].pop()
                reviews.append(r)
            write(root/'outputs'/job['id']/'metadata.json',{'status':'process_completed','turn_completed':True})
            write(root/'outputs'/job['id']/'response.txt',{'reviews':reviews})
        job={'id':'controlled-ordinary-neutral-1','batch':'controlled','condition':'ordinary','role':'neutral','repeat':1};jobs.append(job)
        data={'cases':[],'closing_note':''}
        for c in cases:
            data['cases'].append({'id':c['id'],'instrument_review':'Synthetic test only','probes':[{'id':p['id'],'label':key['cases'][c['id']][p['id']]['label'],'quote':c['passage'],'reason':'Synthetic test only'} for p in c['probes']]})
        assert not validate(data,job,key['cases'])
        bad=copy.deepcopy(data);bad['cases'][0]['probes'][0]['label']='Maybe'
        assert validate(bad,job,key['cases'])
        write(root/'outputs'/job['id']/'metadata.json',{'status':'process_completed','turn_completed':True})
        write(root/'outputs'/job['id']/'response.txt',data)
        write(root/'jobs.json',jobs)
        summary=analyze(root)
        assert summary['eligible_runs']==5
        exported=list(csv.DictReader((root/'analysis/instrument_reviews.csv').open()))
        assert all(r['numbered_id_count']=='0' and r['whole_review_source_ids_with_ranges']=='9.3.1; 9.3.2; 9.3.3' for r in exported)
        assert all('9.3.1–9.3.3' in r['combined_all_fields'] and json.loads(r['full_review_json'])['supported_claims'] for r in exported)
        contrast_rows=list(csv.DictReader((root/'analysis/controlled_contrasts.csv').open()))
        assert len(contrast_rows)==7 and all(r['both_match_key']=='True' for r in contrast_rows)
        assert [r['same_label'] for r in contrast_rows]==['True','True','True','False','True','True','False']
        assert summary['mesa_valid_answers']==200
        assert summary['controlled_matches']==17 and summary['controlled_valid_probes']==17
        rows=list(csv.DictReader((root/'analysis/mesa_agreement.csv').open()))
        for b in ['arc','designqa']:
            q1=next(r for r in rows if r['question']=='1' and r['benchmark']==b)
            assert int(q1['matches'])==3 and int(q1['pair_denominator'])==6 and float(q1['fraction'])==0.5
            q2=next(r for r in rows if r['question']=='2' and r['benchmark']==b)
            assert float(q2['fraction'])==1
        probes=list(csv.DictReader((root/'analysis/controlled_probes.csv').open()))
        assert all(r['quote_substring']=='True' for r in probes)
        folder=root/'outputs'/'real-mesa-neutral-1'
        error={'type':'item.completed','item':{'type':'error','message':'service unavailable'}}
        write(folder/'metadata.json',{'status':'process_completed','turn_completed':True,'tool_items':[error]})
        (folder/'events.jsonl').write_text(json.dumps(error)+'\n')
        assert analyze(root)['eligible_runs']==5
        assert observations(folder,{'tool_items':[error]})['recorded_infrastructure_error_items']==1
        tool={'type':'item.started','item':{'type':'command_execution'}}
        (folder/'events.jsonl').write_text(json.dumps(tool)+'\n')
        assert analyze(root)['eligible_runs']==4
        bad=copy.deepcopy(reviews);bad[0]['mesa_answers'][0]['id']=True
        assert validate({'reviews':bad},jobs[0],key['cases'])
    with tempfile.TemporaryDirectory(prefix='mesa-retry-check-') as tmp:
        root=Path(tmp)
        write(root/'analyst/expected.json',key)
        write(root/'materials/controlled-cases.json',cases)
        (root/'materials/efpa-original.txt').write_text('9.3.1 Test')
        job={'id':'controlled-ordinary-neutral-1','batch':'controlled','condition':'ordinary','role':'neutral','repeat':1}
        write(root/'jobs.json',[job])
        folder=root/'outputs'/job['id']
        write(folder/'metadata.json',{'status':'process_failed','turn_completed':False})
        write(folder/'attempt-2/metadata.json',{'status':'process_completed','turn_completed':True})
        write(folder/'attempt-2/response.txt',data)
        result=analyze(root)
        assert result['eligible_runs']==1 and result['physical_attempt_count']==2
        selected=list(csv.DictReader((root/'analysis/runs.csv').open()))[0]
        assert selected['chosen_attempt']=='2' and selected['physical_attempts']=='2'
        write(folder/'metadata.json',{'status':'process_completed','turn_completed':True})
        write(folder/'response.txt',{'cases':[]})
        result=analyze(root)
        assert result['eligible_runs']==0 and result['retry_protocol_issues']
        selected=list(csv.DictReader((root/'analysis/runs.csv').open()))[0]
        assert selected['chosen_attempt']=='1'
    print('PASS: duplicate keys, fences, incomplete runs, invalid categories, exact key matches, denominators, and pairwise agreement')
if __name__=='__main__': main()

"""Version 3 supplementary calculations. No provider calls or historical writes."""
import json
import random
import statistics
from pathlib import Path
from paper2.method.decision_engine import compute_wilson_score_interval

OUT = Path(__file__).resolve().parent / 'v3'

def rates(decisions, compliant):
    n = len(decisions)
    resolved = sum(x != 'Unresolved' for x in decisions)
    fa = sum(x == 'Supported' and not compliant for x in decisions)
    fc = sum(x == 'Contradicted' and compliant for x in decisions)
    return dict(n=n, resolved=resolved, coverage=resolved/n if n else 'undefined',
                false_acceptance_per_case=fa/n if n else 'undefined',
                false_contradiction_per_case=fc/n if n else 'undefined',
                errors_per_case=(fa+fc)/n if n else 'undefined',
                errors_among_resolved=(fa+fc)/resolved if resolved else 'undefined')

def batch(seed, sensitivity=.85, false_alarm=.05, defects=.30, shift=-.15, trials=10000):
    rng = random.Random(seed)
    intervals = [compute_wilson_score_interval(k, 30) for k in range(31)]
    m2, m3, distances = [], [], []
    for _ in range(trials):
        defect = rng.random() < defects
        k = sum(rng.random() < (.86 if defect else .72) for _ in range(30))
        lb, ub = intervals[k]
        decision = 'Supported' if lb >= .70 else 'Contradicted' if ub < .70 else 'Unresolved'
        detected = rng.random() < (sensitivity if defect else false_alarm)
        missing = rng.random() < .10
        m2.append(decision)
        m3.append('Unresolved' if detected or missing else decision)
        distances.append(min(abs(lb-.70), abs(ub-.70)))
    resolved = [i for i,x in enumerate(m2) if x != 'Unresolved']
    count = sum(x != 'Unresolved' for x in m3)
    random_keep = set(rng.sample(resolved,count))
    proximity_keep = set(sorted(resolved,key=lambda i: distances[i],reverse=True)[:count])
    methods = dict(m2=m2,m3=m3,
        random=[x if i in random_keep else 'Unresolved' for i,x in enumerate(m2)],
        proximity=[x if i in proximity_keep else 'Unresolved' for i,x in enumerate(m2)])
    results = {name: rates(ds,.72+shift >= .70) for name,ds in methods.items()}
    if len({results[k]['resolved'] for k in ['m3','random','proximity']}) != 1:
        raise RuntimeError('Coverage mismatch')
    return dict(seed=seed, sensitivity=sensitivity,false_alarm=false_alarm,defects=defects,
                shift=shift,trials=trials,methods=results,
                differences={k:results[k]['errors_per_case']-results['m3']['errors_per_case']
                             for k in ['random','proximity']})

def write_report(payload):
    lines=['# Supplementary simulation results','',
           '100 batches, seeds 0–99; 10,000 trials per batch. Coverage matching is repeated within each batch. Differences are control errors per case minus M3 errors per case. Dispersion is Monte Carlo variability, not uncertainty about real review accuracy.','',
           '| Control | Mean reduction (percentage points) | Batch SD | Minimum | Maximum |',
           '| --- | ---: | ---: | ---: | ---: |']
    for name,row in payload['difference_summary'].items():
        lines.append('| '+name+' | '+' | '.join(f"{100*row[k]:.4f}" for k in ['mean','sd','minimum','maximum'])+' |')
    lines += ['', '## Detector boundary cases','',
              'Each cell uses seed 42 and 10,000 trials. Missingness is 0.10. These batches are illustrative model calculations.', '',
              '| Sensitivity | False alarm | Defects | Shift | Method | Coverage | Errors/case | Errors/resolved |',
              '| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |']
    for cell in payload['boundary']:
        for method,row in cell['methods'].items():
            values=[f"{row[k]:.4f}" if isinstance(row[k],(int,float)) else row[k]
                    for k in ['coverage','errors_per_case','errors_among_resolved']]
            lines.append(f"| {cell['sensitivity']} | {cell['false_alarm']} | {cell['defects']} | {cell['shift']} | {method} | "+' | '.join(values)+' |')
    (OUT/'simulation-report.md').write_text('\n'.join(lines)+'\n')

def main():
    headline = [batch(seed) for seed in range(100)]
    boundary = [batch(42,s,a,d,shift) for s,a in [(0.05,.05),(.50,.50),(.05,.50)]
                for d in [0,.30] for shift in [-.15,0]]
    summary = {}
    for name in ['random','proximity']:
        values=[r['differences'][name] for r in headline]
        summary[name]=dict(mean=statistics.mean(values),sd=statistics.stdev(values),
                           minimum=min(values),maximum=max(values))
    payload=dict(version=3,description='Monte Carlo variability across batches, not uncertainty about real review accuracy',
        n_tasks=30,threshold=.70,missingness=.10,source_probability=.72,defective_probability=.86,
        random_generator='random.Random, reset for every batch',
        tie_rule='Stable descending distance, earlier trial first',headline=headline,boundary=boundary,
        difference_summary=summary)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'simulation.json').write_text(json.dumps(payload,indent=2)+'\n')
    write_report(payload)
    print(json.dumps(summary,indent=2))
if __name__ == '__main__': main()

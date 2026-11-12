"""Version 3 supplementary calculations. No provider calls or historical writes."""
import json
import random
import statistics
from pathlib import Path
from paper2.method.decision_engine import compute_exact_binomial_interval, compute_wilson_score_interval

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

def batch(seed, sensitivity=.85, false_alarm=.05, defects=.30, shift=-.15, trials=10000,
          n_tasks=30, decision_rule='wilson', one_sided=True):
    rng = random.Random(seed)
    if decision_rule == 'exact_binomial':
        intervals = [compute_exact_binomial_interval(k, n_tasks, confidence=0.95, one_sided=one_sided)
                     for k in range(n_tasks + 1)]
    else:
        intervals = [compute_wilson_score_interval(k, n_tasks) for k in range(n_tasks + 1)]
    m2, m3, distances = [], [], []
    for _ in range(trials):
        defect = rng.random() < defects
        k = sum(rng.random() < (.86 if defect else .72) for _ in range(n_tasks))
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
    return dict(seed=seed, n_tasks=n_tasks, decision_rule=decision_rule,
                sensitivity=sensitivity,false_alarm=false_alarm,defects=defects,
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

def protocol6_grid(trials=10000):
    """Evaluate Monte Carlo sensitivity across Protocol 6 sample sizes under the exact binomial rule."""
    sample_sizes = (31, 44, 52, 75)
    headline_by_n = {}
    summary_by_n = {}
    for n in sample_sizes:
        batches = [batch(seed, trials=trials, n_tasks=n, decision_rule='exact_binomial', one_sided=True)
                   for seed in range(100)]
        headline_by_n[str(n)] = batches
        summary_by_n[str(n)] = {
            name: dict(
                mean=statistics.mean(r['differences'][name] for r in batches),
                sd=statistics.stdev(r['differences'][name] for r in batches),
                minimum=min(r['differences'][name] for r in batches),
                maximum=max(r['differences'][name] for r in batches),
            )
            for name in ('random', 'proximity')
        }
    boundary = [
        batch(42, s, a, d, shift, trials=trials, n_tasks=n, decision_rule='exact_binomial', one_sided=True)
        for n in sample_sizes
        for s, a in [(0.85, 0.05), (0.05, 0.05), (0.50, 0.50)]
        for d in (0.0, 0.30)
        for shift in (-0.15, 0.0)
    ]
    payload = dict(
        version=6,
        description='Protocol 6 exact one-sided 95% binomial sample-size Monte Carlo grid (illustrative calculations)',
        sample_sizes=list(sample_sizes),
        decision_rule='exact_binomial',
        one_sided=True,
        threshold=0.70,
        missingness=0.10,
        source_probability=0.72,
        defective_probability=0.86,
        trials_per_batch=trials,
        difference_summary_by_n=summary_by_n,
        headline_by_n=headline_by_n,
        boundary=boundary,
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'simulation-p6.json').write_text(json.dumps(payload, indent=2) + '\n')
    lines = [
        '# Protocol 6 sample-size simulation results',
        '',
        '100 batches per sample size (seeds 0-99, 10,000 trials per batch) under the exact one-sided 95% binomial rule. Differences are control errors per case minus M3 errors per case (percentage points).',
        '',
        '| n_tasks | Control | Mean reduction (pp) | Batch SD | Minimum | Maximum |',
        '| ---: | --- | ---: | ---: | ---: | ---: |',
    ]
    for n in sample_sizes:
        for name, row in summary_by_n[str(n)].items():
            lines.append(
                f"| {n} | {name} | " + ' | '.join(f"{100*row[k]:.4f}" for k in ('mean', 'sd', 'minimum', 'maximum')) + ' |'
            )
    lines += [
        '',
        '## Detector boundary grid (seed 42)',
        '',
        '| n_tasks | Sensitivity | False alarm | Defects | Shift | Method | Coverage | Errors/case | Errors/resolved |',
        '| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |',
    ]
    for cell in boundary:
        for method, row in cell['methods'].items():
            vals = [f"{row[k]:.4f}" if isinstance(row[k], (int, float)) else row[k]
                    for k in ('coverage', 'errors_per_case', 'errors_among_resolved')]
            lines.append(
                f"| {cell['n_tasks']} | {cell['sensitivity']} | {cell['false_alarm']} | {cell['defects']} | {cell['shift']} | {method} | "
                + ' | '.join(vals) + ' |'
            )
    (OUT / 'simulation-report-p6.md').write_text('\n'.join(lines) + '\n')
    return payload


def main(argv=None):
    import sys
    args = sys.argv[1:] if argv is None else argv
    if '--protocol6' in args:
        payload = protocol6_grid()
        print(json.dumps(payload['difference_summary_by_n'], indent=2))
        return
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

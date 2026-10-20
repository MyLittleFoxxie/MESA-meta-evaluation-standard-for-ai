#!/usr/bin/env python3
"""Read-only, post-hoc sensitivity calculation. Prints a report; writes no files."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import argparse, collections, csv, hashlib, importlib.util, itertools, json

ROOT = Path(__file__).resolve().parent
TARGET = ('P6B', 'claim1')
METHODS = [('mesa', 'MESA'), ('efpa', 'EFPA-TRM'), ('ordinary', 'General instructions')]

def assumed_label(case, claim, original):
    return 'Contradicted' if (case, claim) == TARGET else original

def calculate(root=ROOT):
    load = lambda p: json.loads(p.read_text())
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location('frozen_validation', root/'validation_helpers.py')
    validation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validation)
    key_path = root/'analyst/expected.json'
    key = load(key_path)['cases']['cases']
    assert key['P6B']['claim1']['label'] == 'Not established'
    jobs = load(root/'jobs.json')
    assert len(jobs) == 30
    with (root/'analysis/runs.csv').open() as source:
        recorded = {r['id']: r for r in csv.DictReader(source)}
    counts = {c: collections.Counter() for c, _ in METHODS}
    exclusions, answers, sessions = {}, [], []
    completed = physical_attempts = 0
    frozen = load(root/'freeze-manifest.json')
    for name, fingerprint in frozen['files'].items():
        assert sha(root/name) == fingerprint, f'Frozen file changed: {name}'
    for job in jobs:
        folder = root/'outputs'/job['id']
        metadata = load(folder/'metadata.json')
        assert sha(root/job['input']) == job['sha256'] == metadata['input_sha256']
        assert metadata['requested_model'] == metadata['reported_model'] == 'claude-sonnet-5-5'
        assert not metadata['init_tools'] and not metadata['init_mcp_servers']
        assert not metadata['tool_items']
        assert metadata['started_at'] >= frozen['frozen_utc']
        sessions += metadata['thread_ids']
        physical_attempts += 1
        completed += metadata['status'] == 'process_completed' and metadata['turn_completed']
        assert metadata['attempt'] == 1 and not list(folder.glob('attempt-*'))
        for name, fingerprint in metadata['output_files_sha256'].items():
            assert sha(folder/name) == fingerprint
        errors, data = [], None
        try:
            data = validation.parse((folder/'response.txt').read_text())
            errors = validation.validate(data, job, key)
        except (ValueError, TypeError) as exc:
            errors = [str(exc)]
        eligible = (metadata['status'] == 'process_completed'
                    and metadata['turn_completed'] and not errors)
        assert eligible == (recorded[job['id']]['eligible'] == 'True')
        if not eligible:
            exclusions[job['id']] = errors
            continue
        c = counts[job['condition']]
        c[job['batch']+'_conversations'] += 1
        if job['batch'] == 'cases':
            for case in data['cases']:
                for claim in case['probes']:
                    original = key[case['id']][claim['id']]['label']
                    alternative = assumed_label(case['id'], claim['id'], original)
                    c['answers'] += 1
                    c['original_matches'] += claim['label'] == original
                    c['alternative_matches'] += claim['label'] == alternative
                    c['target_answers'] += (case['id'], claim['id']) == TARGET
        elif job['condition'] == 'mesa':
            answers += [(r['benchmark'], a['id'], a['choice'])
                        for r in data['reviews'] for a in r['mesa_answers']]
    variation = matching = pair_count = 0
    for benchmark, question in itertools.product(['arc', 'designqa'], range(1, 26)):
        choices = [a for b, q, a in answers if (b, q) == (benchmark, question)]
        variation += len(set(choices)) > 1
        for first, second in itertools.combinations(choices, 2):
            matching += first == second; pair_count += 1
    expected = {'mesa': (243, 240, 245), 'efpa': (237, 240, 245), 'ordinary': (191, 191, 196)}
    for condition, values in expected.items():
        c = counts[condition]
        assert (c['original_matches'], c['alternative_matches'], c['answers']) == values
    assert (len(answers), variation, matching, pair_count) == (250, 9, 456, 500)
    assert set(exclusions) == {'real-efpa-neutral-4', 'cases-ordinary-neutral-2'}
    assert completed == physical_attempts == len(set(sessions)) == 30
    assert sha(key_path) == frozen['files']['analyst/expected.json']
    return {'status': 'post hoc; not a corrected key or correctness standard',
            'changed_assumption': {'case': 'P6B', 'claim': 'claim1',
                                   'original': 'Not established', 'alternative': 'Contradicted'},
            'planned': len(jobs), 'completed': completed, 'attempts': physical_attempts,
            'eligible': len(jobs)-len(exclusions), 'unique_sessions': len(set(sessions)),
            'methods': {c: dict(v) for c, v in counts.items()}, 'exclusions': exclusions,
            'mesa_choices': 250, 'variable_question_benchmark_pairs': variation,
            'matching_choice_pairs': matching, 'choice_pairs': pair_count,
            'frozen_key_sha256': sha(key_path), 'freeze_sha256': sha(root/'freeze-manifest.json')}

def report(result):
    lines = ['# P6B sensitivity analysis (post hoc)', '',
             'This calculation was specified after the completed study was reviewed. It changes only the assumed expected label for **P6B claim 1**, from **Not established** to **Contradicted**. The frozen key, responses, eligibility rules, exclusions, denominators, and every other expected label remain unchanged.', '',
             'P6B asks whether results from grid problems are sufficient for a stated use concerning general intelligence across subjects and real-world settings. A Contradicted answer can express that the described evidence is insufficient for that use. This differs from asserting that an unreported test never occurred. Neither label is established as an independently validated correctness standard.', '',
             '| Method | Frozen-key matches | Alternative-assumption matches | Target-claim answers |',
             '| --- | ---: | ---: | ---: |']
    for c, name in METHODS:
        v = result['methods'][c]
        lines.append(f"| {name} | {v['original_matches']}/{v['answers']} | {v['alternative_matches']}/{v['answers']} | {v['target_answers']} |")
    lines += ['', 'MESA and EFPA-TRM have the same match total under this one alternative assumption. The original totals remain the primary descriptive results. This is not a corrected key or an alternative correctness standard. This sensitivity check illustrates dependence on the expected answer; it does not select a favorable key, correct the frozen key, or establish comparative review accuracy. Repeated labels come from one model and are dependent.', '',
              '## Reproduction and preservation', '',
              'From this study directory, run `python3 p6b_sensitivity.py` for Markdown or `python3 p6b_sensitivity.py --json` for the full accounting. The script only reads records and prints to standard output. It revalidates raw responses with the existing validator, checks the original exclusions and frozen fingerprints, and independently reproduces the original match totals, 250 MESA choices, nine varying pairs, and 456/500 repeated-choice matches. It launches no model conversations and writes no files.', '',
              f"Frozen expected-key SHA-256: `{result['frozen_key_sha256']}`.", '',
              'Completed exclusions remain `real-efpa-neutral-4` (invalid JSON control character) and `cases-ordinary-neutral-2` (unexpected case identifier). Neither is repaired, replaced or reintroduced. Thirty conversations completed; 28 remain eligible.', '']
    return '\n'.join(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    result = calculate()
    print(json.dumps(result, indent=2) if args.json else report(result))

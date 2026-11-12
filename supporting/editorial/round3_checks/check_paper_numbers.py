"""Read only check of numbers in mesa_paper.tex (round 3). Reads frozen files, writes nothing."""
import csv, json, collections, itertools, pathlib
R = next(q for q in pathlib.Path(__file__).resolve().parents if (q/'v4'/'mapping'/'mapping.csv').exists())
out = {}
m = list(csv.DictReader(open(R/'v4/mapping/mapping.csv', newline='')))
links = [(r['framework'], c) for r in m for c in r['final'].replace(' ', '').split(';') if c]
out['items'] = len(m); out['links'] = len(links)
out['items_by_framework'] = dict(collections.Counter(r['framework'] for r in m))
out['items_multi'] = sum(1 for r in m if ';' in r['final'])
norm = lambda x: ';'.join(sorted(x.replace(' ', '').split(';')))
out['author_eq_draft'] = sum(norm(r['author']) == norm(r['assistant_draft']) for r in m)
out['final_eq_draft'] = sum(norm(r['final']) == norm(r['assistant_draft']) for r in m)
step = {}
def setstep(name, nums):
    for n in nums: step['C%02d' % n] = name
setstep('Scoring', [6, 7]); setstep('Generalization', [8, 9, 10, 11, 12, 20])
setstep('Extrapolation', [1, 3, 4, 5, 13, 14, 15, 16, 23, 27])
setstep('Decision', [2, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29]); step['C30'] = 'Description'
out['links_by_step'] = dict(collections.Counter(step[c] for _, c in links))
out['concerns_by_step'] = dict(collections.Counter(step.values()))
fw_per_concern = collections.defaultdict(set)
for f, c in links: fw_per_concern[c].add(f)
out['concerns_all7'] = sum(len(v) == 7 for v in fw_per_concern.values())
out['concerns_more_than_one'] = sum(1 < len(v) for v in fw_per_concern.values())
out['concerns_one_only'] = sum(len(v) == 1 for v in fw_per_concern.values())
# Study 1 comparisons by concern group
co = [x for x in csv.DictReader(open(R/'v4/study/analysis/concern-outcomes.csv', newline='')) if x['repeat'] == '1' and x['outcome'] != 'not_recoded' and x['framework'] != 'RUBRIC']
by = collections.defaultdict(dict)
for x in co: by[(x['benchmark'], x['concern'])][x['framework']] = x['outcome']
grp = collections.Counter(); same = collections.Counter(); tot = agree = 0
for (b, c), d in by.items():
    n = int(c[1:]); g = 'doc_licence(18,19)' if n in (18, 19) else ('C01-C16' if n <= 16 else 'rest')
    for a, e in itertools.combinations(sorted(d), 2):
        grp[g] += 1; same[g] += d[a] == d[e]; tot += 1; agree += d[a] == d[e]
out['comparisons'] = [agree, tot]; out['by_group'] = {g: [same[g], grp[g]] for g in grp}
out['cells'] = sum(1 for d in by.values() if len(d) >= 2)
dl = list(csv.DictReader(open(R/'v4/study/analysis/disagreement-log.csv', newline='')))
out['causes'] = dict(collections.Counter(x['cause'] for x in dl))
out['disagreements_with_open'] = sum('unresolved' in (x['outcome_1'], x['outcome_2']) for x in dl)
j = [x for x in csv.DictReader(open(R/'v4/study/analysis/judgments.csv', newline='')) if x['repeat'] == '1' and x['framework'] != 'RUBRIC']
out['answers'] = len(j)
out['humaneval_C07'] = [(x['framework'], x['item_id'], x['answer'], x['outcome'], x['marker']) for x in j if x['benchmark'] == 'humaneval' and 'C07' in x['concerns']]
# Study 2 HumanEval worked case
j2 = list(csv.DictReader(open(R/'v5/study-cycle2/analysis/judgments.csv', newline='')))
out['judgments2_columns'] = list(j2[0].keys())
key = [k for k in ('item_id', 'criterion') if k in j2[0]][0]
out['humaneval_case'] = [{k: x.get(k) for k in ('family', 'cycle', 'job', 'repeat', key, 'level', 'outcome', 'check_kind')} for x in j2 if x.get('benchmark') == 'humaneval' and x.get(key) in ('B07', 'B28a', 'B14b')]
s = list(csv.DictReader(open(R/'v5/study-cycle2/analysis/seeded-results.csv', newline='')))
out['seeded_rows'] = len(s)
out['seeded'] = {f: {'planted_found': sum(x['planted'] == 'True' and x['flagged'] == 'True' for x in s if x['family'] == f), 'planted': sum(x['planted'] == 'True' for x in s if x['family'] == f), 'false_alarms': sum(x['planted'] == 'False' and x['flagged'] == 'True' for x in s if x['family'] == f), 'negatives': sum(x['planted'] == 'False' for x in s if x['family'] == f), 'false_alarm_criteria': dict(collections.Counter(x['criterion'] for x in s if x['family'] == f and x['planted'] == 'False' and x['flagged'] == 'True'))} for f in ('claude', 'gemini')}
print(json.dumps(out, indent=1))

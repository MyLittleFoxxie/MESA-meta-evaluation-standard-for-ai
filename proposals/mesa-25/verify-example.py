"""Structural/source-integrity checks for the example, not questionnaire validation."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
questions = json.loads((HERE / 'questions.json').read_text())
example = json.loads((HERE / 'designqa-example.json').read_text())
manifest = json.loads((HERE / 'designqa-source-manifest.json').read_text())
report = (HERE / 'designqa-example.md').read_text()
comparison = (HERE / 'designqa-comparison.md').read_text()
assert manifest['questionnaire_sha256'] == hashlib.sha256((HERE / 'questions.json').read_bytes()).hexdigest()
assert example['commit'] == manifest['repository_commit']
assert [a['id'] for a in example['answers']] == list(range(1, 26))
for question, answer in zip(questions, example['answers']):
    assert answer['answer'] in {'Yes', 'Partly', 'No', 'Not sure', 'Not applicable'}
    assert len(answer['comment'].split()) >= 40
    assert answer['sources'] and answer['comparison']
    assert question['question'] in report
    assert answer['comment'] in report
    assert f"| Q{answer['id']} — {answer['answer']} |" in comparison
    assert answer['comparison'] in comparison
for source in manifest['local_sources']:
    assert hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest() == source['sha256'], source['path']
assert 'see parent section' not in comparison
assert 'not a validated questionnaire' in example['status']
assert 'unblinded' in example['method']
assert len(re.findall(r'^\| Q\d+ —', comparison, re.M)) == 25
print('PASS: 25 sourced answers and detailed comments; 25 three-review comparisons; source/question hashes unchanged')
print('LIMIT: these checks do not validate the questionnaire or independently confirm reviewer judgments')

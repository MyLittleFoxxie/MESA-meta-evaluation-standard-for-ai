"""Check guided survey integrity; does not establish scientific validity."""
from pathlib import Path
import json, re, hashlib, base64
P = Path(__file__).resolve().parent
ROOT = P.parents[1]
RELOC = json.loads((ROOT / 'provenance/relocation-map.json').read_text())['path_map'] if (ROOT / 'provenance/relocation-map.json').exists() else {}
def resolve_root(rel: str) -> Path:
    p = ROOT / rel
    return p if p.exists() else ROOT / RELOC.get(rel, rel)
def terminology(value):
    if isinstance(value, list): return [terminology(v) for v in value]
    if isinstance(value, dict): return {k: terminology(v) if k != 'sources' else v for k, v in value.items()}
    if isinstance(value, str):
        value = re.sub(r'\b(skills|capabilities)\b', 'abilities', value)
        value = re.sub(r'\b(skill|capability)\b', 'ability', value)
        return value.replace('A ability', 'An ability').replace('a ability', 'an ability')
    return value

raw = (P / 'packet.json').read_bytes(); d = json.loads(raw)
original = json.loads(resolve_root('proposals/mesa-25/questions.json').read_text())
assert [q['id'] for q in d['questions']] == list(range(1, 26))
assert [q['question'] for q in d['questions']] == [q['question'] for q in original]
assert len({q['domain'] for q in d['questions']}) == 6
assert [b['id'] for b in d['benchmarks']] == ['arc', 'designqa']
assert d['example']['id'] == 'hle'
assert len(d['familiarity']) == 3 and all(len(q['labels']) == 5 for q in d['familiarity'])
assert d['choices'] == ['Yes', 'Partly', 'No', 'Not sure', 'Not applicable']
source_ids = {s['id'] for s in d['sources']}
assert len(source_ids) == len(d['sources'])
for q in d['questions']:
    assert '?' not in q['help']
    assert q['example']['answer'] in d['choices']
    assert set(q['example']['sources']) <= source_ids
    assert len(q['example']['why'].split()) <= 45
for source in d['sources']:
    if source['url'].startswith('../'):
        rel_url = str((P / source['url']).resolve().relative_to(ROOT.resolve()))
        assert resolve_root(rel_url).is_file()
html = (P / 'survey.html').read_text(); md = (P / 'survey.md').read_text()
embedded = json.loads(re.search(r'<script id="packet" type="application/json">(.*?)</script>', html, re.S)[1]); assert embedded == d
assert not re.search(r'__[A-Z_]+__', html)
media = json.loads(re.search(r'^const media=(.*);$', html, re.M)[1])
for b in [d['example'], *d['benchmarks']]:
    for paragraph in b['reading']:
        assert paragraph['text'] in md
        assert set(paragraph['sources']) <= source_ids
        assert paragraph['text'].count('**') % 2 == 0
    for key in ['official_image', 'logo']:
        if asset := b.get(key): assert base64.b64decode(media[asset['path']].split(',')[1]) == (P / asset['path']).read_bytes()
    for diagram in b.get('diagrams', []):
        assert 0 <= diagram['after'] < len(b['reading'])
        assert set(diagram['sources']) <= source_ids
        assert all(step['text'] in md for step in diagram['steps'])
assert len(re.findall(r'^\*\*Q\d+\.', md, re.M)) == 50
assert len(re.findall(r'^\*\*Example Q\d+\.', md, re.M)) == 25
assert 'data-page=' not in html and 'id="terms"' not in html and 'Your name' not in html
assert 'participant_name:' not in html and 'payload.Name' not in html
assert 'id="term-tip"' in html and 'id="familiarity"' in html
assert d['paper_title'] in html
assert '<script src=' not in html and '<link rel="stylesheet"' not in html
manifest = json.loads((P / 'source-manifest.json').read_text())
assert manifest['packet_sha256'] == hashlib.sha256(raw).hexdigest()
for f in manifest['files']:
    if 'path' in f: assert hashlib.sha256(resolve_root(f['path']).read_bytes()).hexdigest() == f['sha256']
Path('/tmp/mesa-colleague-script.js').write_text('\n'.join(re.findall(r'<script>(.*?)</script>', html, re.S)))
print('PASS: guided packet, 3 familiarity items, HLE example, 50 blank ARC/DesignQA questions, source references, offline images and fingerprints.')

alignment = (P / 'study-alignment.txt').read_text()
assert hashlib.sha256((P / 'study-alignment.txt').read_bytes()).hexdigest() == manifest['study_alignment']['sha256']
origin = ROOT / manifest['study_alignment']['origin']
if origin.exists(): assert origin.read_bytes() == (P / 'study-alignment.txt').read_bytes()
items = re.findall(r'^([0-9]+)\. \[[^\]]+\] (.*?)\nMeaning: (.*?)\nHLE example: (.*?)\n', alignment, re.M)
assert len(items) == 25
for q, (i, text, help_text, example) in zip(d['questions'], items):
    assert q['id'] == int(i) and q['question'] == text and q['help'] == terminology(help_text)
    assert example.startswith(q['example']['answer'] + '. ')
assert d['answer_instructions'] == alignment.splitlines()[1]
assert d['answer_instructions'] in html  # Preserved in the embedded packet.
for choice in d['choices']:
    assert '**' + choice + ':**' in md
assert 'The answers are not added together to produce a total quality score.' in html and 'The answers are not added together to produce a total quality score.' in md
old = json.loads((P / 'archive/v2.0/packet.json').read_text())
assert d['benchmarks'] == terminology(old['benchmarks']) and d['example'] == terminology(old['example'])
assert d['sources'] == old['sources'] and d['choices'] == old['choices']
for current, before in zip(d['definitions'], old['definitions']):
    if before['label'] != 'Ability': assert current == before
assert [q['question'] for q in d['questions']] == [q['question'] for q in old['questions']]
assert d['version'] == '2.4' and d['survey_id'] == 'mesa-guided-arc-designqa-v2-4'
assert len(d['feedback']) == 5 and all(len(q['labels']) == 6 and q['labels'][-1] == 'Cannot judge' for q in d['feedback'])
assert all(q['question'] in md for q in d['feedback'])
print('PASS: study question and answer alignment, preserved passage facts/questions/source dates, feedback schema and version archive.')

assert hashlib.sha256((P / 'archive/v2.3/packet.json').read_bytes()).hexdigest() == manifest['presentation_revision']['previous_packet_sha256']
previous = json.loads((P / 'archive/v2.3/packet.json').read_text())
expected = terminology(previous)
expected.update(version='2.4', survey_id='mesa-guided-arc-designqa-v2-4')
reason = 'HLE keeps some questions private, marks public test data and warns against using it for training. These measures help limit exposure, but the supplied information does not show whether an AI was trained on any of the public questions or answers.'
ability = 'Something an AI is meant to be able to do, such as finding a pattern or answering a science question. Doing well on one ability does not establish others.'
expected['questions'][17]['example']['why'] = reason
for term in expected['definitions']:
    if term['label'] == 'Ability':
        term['definition'] = ability
        term['aliases'] = ['ability', 'abilities']
for term in expected['terms']:
    if term[0] == 'Ability or ability': term[:] = ['Ability', ability]
assert d == expected, 'Unexpected change beyond approved terminology and Q18 wording'
for q, before in zip(d['questions'], previous['questions']):
    assert q['question'] == before['question']
    assert q['example']['answer'] == before['example']['answer']
    assert q['example']['sources'] == before['example']['sources']
    assert md.count('Why: ' + q['example']['why']) == 3
assert d['questions'][17]['example']['answer'] == 'Partly'
assert not re.search(r'\b(skills?|capabilit(?:y|ies))\b', json.dumps({k:v for k,v in d.items() if k != 'sources'}), re.I)
assert len({a.lower() for term in d['definitions'] for a in term['aliases']}) == sum(len(term['aliases']) for term in d['definitions'])
print('PASS: 2.4 terminology, Q18 explanation, archived fingerprint, unchanged questions and selections; all example copies match.')

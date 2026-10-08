"""Packet integrity checks. Does not establish questionnaire validity."""
from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;ROOT=P.parents[1]
raw=(P/'packet.json').read_bytes();d=json.loads(raw)
original=json.loads((ROOT/'proposals/mesa-25/questions.json').read_text())
assert [q['id'] for q in d['questions']]==list(range(1,26))
assert [q['question'] for q in d['questions']]==[q['question'] for q in original]
assert len(set(q['domain'] for q in d['questions']))==6
assert len(d['benchmarks'])==2
source_ids={s['id'] for s in d['sources']}
examples=json.loads((ROOT/'proposals/mesa-25/designqa-example.json').read_text())
for q,a in zip(d['questions'],examples['answers']):
 assert '?' not in q['help']
 assert q['example']['answer']==a['answer']
 assert set(q['example']['sources'])<=source_ids
 assert len(q['example']['why'].split())<=45
assert len(source_ids)==len(d['sources'])
for b in d['benchmarks']:
 assert [f['id'] for f in b['facts']]==list(range(1,26))
 for f in b['facts']:
  assert len(f['text'].split())>=15
  assert f['sources'] and set(f['sources'])<=source_ids
  assert not any(key in f for key in ['answer','rating','recommended_answer'])
for s in d['sources']:
 if s['url'].startswith('../'):assert (P/s['url']).is_file()
html=(P/'survey.html').read_text()
embedded=json.loads(re.search(r'<script id="packet" type="application/json">(.*?)</script>',html,re.S)[1]);assert embedded==d
assert '__PACKET_' not in html and '__MEDIA_' not in html
import base64
media=json.loads(re.search(r'^const media=(.*);$',html,re.M)[1])
for b in d['benchmarks']:
 if 'official_image' in b:
  im=b['official_image'];assert base64.b64decode(media[im['path']].split(',')[1])==(P/im['path']).read_bytes()
  assert im['caption'] in (P/'survey.md').read_text()
assert '<script src=' not in html and '<link rel="stylesheet"' not in html
manifest=json.loads((P/'source-manifest.json').read_text())
assert manifest['packet_sha256']==hashlib.sha256(raw).hexdigest()
for f in manifest['files']:
 if 'path' in f:assert hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256']
md=(P/'survey.md').read_text();assert len(re.findall(r'^\*\*Q\d+\.',md,re.M))==50
for b in d['benchmarks']:
 assert sorted(i for paragraph in b['reading'] for i in paragraph['fact_ids'])==list(range(1,26))
 for paragraph in b['reading']:
  assert paragraph['text'] in md
  assert set(paragraph['sources'])<=source_ids
  assert paragraph['title'] and '**' in paragraph['text']
  assert paragraph['text'].count('**')%2==0
 for diagram in b['diagrams']:
  assert 0<=diagram['after']<len(b['reading'])
  assert set(diagram['sources'])<=source_ids
  assert len(diagram['steps'])==3
  assert all(step['text'] in md for step in diagram['steps'])
 assert md.index(b['reading'][-1]['text']) < md.index('**Q1.',md.index('## '+b['name']))
assert 'Information for this question' not in html
assert 'A missing study' not in html
assert 'data-page="finish"' not in html and 'id="import-file"' not in html
assert d['paper_title'] in html
assert 'MESA-25 · packet' not in html
assert 'id="theme-toggle"' in html
assert '**Information:**' not in md
assert 'respondent_code' not in html and 'respondent code' not in md.lower()
assert not re.search(r'\b[0-9a-f]{40}\b',d['example_scope'])
assert len(re.findall(r'^\*\*Example Q\d+\.',md,re.M))==25
# Extract executable JavaScript for a separate syntax check.
scripts=re.findall(r'<script>(.*?)</script>',html,re.S)
Path('/tmp/mesa-colleague-script.js').write_text('\n'.join(scripts))
print('PASS: 50 unanswered items; matching checklist wording; all facts have sources; self-contained HTML; packet/source fingerprints; printable copy')

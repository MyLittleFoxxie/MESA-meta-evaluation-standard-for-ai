"""Render explicitly recorded selected-review observations; never judge new prose."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent
p=B/'analysis/selected-review-observations.json';data=json.loads(p.read_text())
lines=['# Six selected benchmark reviews','',data['selection'],'',data['scope'],'']
for method in ['mesa','efpa','ordinary']:
 rows=[r for r in data['observations'] if r['method']==method]
 lines+=['## '+{'mesa':'MESA','efpa':'EFPA-TRM','ordinary':'General instructions'}[method],'']
 for r in rows:
  source=B/r['source'];assert hashlib.sha256(source.read_bytes()).hexdigest()==r['source_sha256']
  raw=json.loads(source.read_text());review=next(x for x in raw['reviews'] if x['benchmark']==r['benchmark'])
  assert r['quote'] in json.dumps(review,ensure_ascii=False),r
  lines += [f"### {r['benchmark']}: {r['topic']} ({r['status']})",'',r['quote'],'',f"Source: [{r['source']}]({Path('../')/r['source']})",'']
 if not rows:lines+=['Awaiting the preselected response; no replacement selected.','']
if 'qualifications' in data:
 lines+=['## Conclusions needing qualification','']
 for r in data['qualifications']:
  raw=json.loads((B/r['source']).read_text());assert r['quote'] in json.dumps(raw,ensure_ascii=False)
  lines += [f"### {r['method']} — {r['benchmark']}",'',r['quote'],'',r['explanation'],'']
(B/'analysis/selected-reviews.md').write_text('\n'.join(lines)+'\n');print('Rendered verified selected-review quotations:',len(data['observations']))

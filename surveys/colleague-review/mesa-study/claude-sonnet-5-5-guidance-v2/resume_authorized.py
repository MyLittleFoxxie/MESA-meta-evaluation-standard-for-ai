"""Retry only the two verified synthetic authentication failures, then run unattempted jobs."""
import json,subprocess,sys
from pathlib import Path
import run_series as S
S.ROOT=Path(__file__).resolve().parent
for jid in ['real-mesa-neutral-5','real-mesa-neutral-2']:
 d=S.ROOT/'outputs'/jid
 if (d/'attempt-2').exists():
  m=json.loads((d/'attempt-2/metadata.json').read_text())
  if not m.get('turn_completed'):raise SystemExit('Retry failed; stop.')
  continue
 m=json.loads((d/'metadata.json').read_text())
 assert not m['turn_completed'] and m['status']=='process_failed'
 assert (d/'response.txt').read_text()=='Not logged in · Please run /login'
 assert all(e.get('message',{}).get('model')=='<synthetic>' for e in [json.loads(x) for x in (d/'events.jsonl').read_text().splitlines()] if e.get('type')=='assistant')
 job=next(j for j in S.load_jobs() if j['id']==jid)
 if S.run(job,1200,attempt=2)!='process_completed':raise SystemExit('Retry failed; stop.')
subprocess.run([sys.executable,str(S.ROOT/'run_series.py'),'--root',str(S.ROOT),'--resume'],check=True)

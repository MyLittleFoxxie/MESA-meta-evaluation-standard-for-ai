"""Freeze the Claude batch inputs. Shared materials are hashed again; the Codex manifest is untouched."""
import datetime,hashlib,json
from pathlib import Path
C=Path(__file__).resolve().parent;R=C.parent
p=C/'freeze-manifest.json'
if p.exists():raise SystemExit('Already frozen; create a new version to change materials')
paths=[]
for folder in ['materials','prompts','sources','analyst']:
 paths.extend(x for x in (R/folder).rglob('*') if x.is_file() and '__pycache__' not in x.parts)
paths.extend(R/n for n in ['sources.json','analysis-plan.md','file_server.py','validate.py','claude/jobs.json','claude/protocol.md','claude/run.py'])
p.write_text(json.dumps({'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Prospective main Claude freeze after two Claude pilots; no main Claude responses observed','files':{str(x.relative_to(R)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(set(paths))}},indent=2)+'\n')
print('Frozen',len(paths),'files')

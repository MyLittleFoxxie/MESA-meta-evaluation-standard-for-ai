import datetime,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
p=R/'freeze-manifest.json'
if p.exists():raise SystemExit('Already frozen; create a new version to change materials')
paths=[]
for folder in ['materials','prompts','sources','analyst']:
 paths.extend(x for x in (R/folder).rglob('*') if x.is_file() and '__pycache__' not in x.parts)
paths.extend(R/n for n in ['jobs.json','sources.json','protocol.md','analysis-plan.md','instrument-map.md','run.py','file_server.py','validate.py','prepare_references.py','build_materials.py'])
p.write_text(json.dumps({'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Prospective main Codex freeze after two pilots; no main responses observed','files':{str(x.relative_to(R)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(set(paths))}},indent=2)+'\n')
print('Frozen',len(paths),'files')

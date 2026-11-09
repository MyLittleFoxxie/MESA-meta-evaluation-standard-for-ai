"""Freeze the Study 3 inputs before the main sessions. Refuses to run twice; a changed input needs a new version.

Hashes the v5 rubric, materials, prompts, jobs, runner, validator, analysis and protocol, and the v4 file server
and snapshots the sessions read. Paths are relative to the repository root. Run after the pilot and after the author
has confirmed the rubric defaults: python3 v5/study/freeze.py
"""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
V4 = ROOT / "v4/study"
p = HERE / "freeze-manifest.json"
if p.exists():
    raise SystemExit("Already frozen; create a new version to change materials")
paths = [x for folder in ["materials", "prompts"] for x in (HERE / folder).rglob("*") if x.is_file()]
paths += [HERE / n for n in ["jobs.json", "run.py", "validate.py", "analyze.py", "reliability.py", "protocol.md"]]
paths += [ROOT / "v5/rubric/rubric.md", V4 / "file_server.py", V4 / "validate.py", V4 / "freeze-manifest.json"]
paths += [x for x in (V4 / "sources").rglob("*") if x.is_file()]
missing = [str(x) for x in paths if not x.exists()]
if missing:
    raise SystemExit("missing before freeze: " + ", ".join(missing))
p.write_text(json.dumps({"frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         "purpose": "Prospective freeze of Study 3 before its main sessions; the pilot on the fictional fixture may precede it",
                         "files": {str(x.relative_to(ROOT)): hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(set(paths))}}, indent=2) + "\n")
print("Frozen", len(set(paths)), "files")

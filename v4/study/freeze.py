"""Freeze the study inputs before the main sessions. Refuses to run twice; a changed input needs a new version.

Hashes materials, prompts, sources, earlier reviews, the mapping files, the runner, the file server and the
protocol. Run from the repository root after the pre-experiment checks pass: python3 v4/study/freeze.py
"""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
p = HERE / "freeze-manifest.json"
if p.exists():
    raise SystemExit("Already frozen; create a new version to change materials")
paths = []
for folder in ["materials", "prompts", "sources", "earlier-reviews"]:
    paths.extend(x for x in (HERE / folder).rglob("*") if x.is_file() and "__pycache__" not in x.parts)
paths.extend(HERE / n for n in ["sources.json", "jobs.json", "file_server.py", "validate.py", "run.py", "analyze.py", "protocol.md"])
paths.extend(ROOT / "v4/mapping" / n for n in ["questions.json", "mapping.csv", "concerns.md", "recoding-rules.md"])
paths.append(ROOT / "v4/rubric/rubric-draft.md")
missing = [str(x) for x in paths if not x.exists()]
if missing:
    raise SystemExit("missing before freeze: " + ", ".join(missing))
p.write_text(json.dumps({"frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         "purpose": "Prospective freeze before the main sessions; pilots on the fictional fixture may precede it",
                         "files": {str(x.relative_to(HERE) if x.is_relative_to(HERE) else x.relative_to(ROOT)): hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(set(paths))}}, indent=2) + "\n")
print("Frozen", len(paths), "files")

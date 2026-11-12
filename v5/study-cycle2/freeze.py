"""Freeze and verify Study Cycle 2 materials, seeded fixtures, known defects, prompts, and analysis code.

Also verifies that v4/study/freeze-manifest.json and v5/study/freeze-manifest.json remain intact.
Run from the repository root:
    python v5/study-cycle2/freeze.py           # create freeze-manifest.json
    python v5/study-cycle2/freeze.py --check   # verify freeze-manifest.json
"""
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MANIFEST = HERE / "freeze-manifest.json"
FROZEN_FILES = [
    "build_materials.py",
    "file_server.py",
    "validate.py",
    "reliability.py",
    "analyze.py",
    "run.py",
    "blind_sample.py",
    "reveal_blind.py",
    "blind_author_key.json",
    "protocol.md",
    "jobs.json",
    "seeded_truth.json",
    "known_defects.json",
]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def collect():
    files = {"v5/rubric/rubric.md": sha(ROOT / "v5/rubric/rubric.md")}
    for name in FROZEN_FILES:
        files[name] = sha(HERE / name)
    for folder in ("materials", "prompts"):
        for p in sorted((HERE / folder).iterdir()):
            if p.is_file():
                files[p.relative_to(HERE).as_posix()] = sha(p)
    for p in sorted((HERE / "sources").rglob("*")):
        if p.is_file():
            files[p.relative_to(HERE).as_posix()] = sha(p)
    return files


ALLOWED_MISSING_GITIGNORED_HLE = {
    "sources/hle/data/test-00000-of-00001.parquet",
    "sources/hle/repository/data/hle-test.jsonl",
    "v4/study/sources/hle/data/test-00000-of-00001.parquet",
    "v4/study/sources/hle/repository/data/hle-test.jsonl",
}


def check_manifest_file(base_dir, manifest_path):
    """Verify every recorded SHA-256 in a v4 or v5 freeze-manifest.json."""
    if not manifest_path.exists():
        print("missing", manifest_path)
        return False
    saved = json.loads(manifest_path.read_text(encoding="utf-8"))["files"]
    for rel, expected in saved.items():
        p1 = ROOT / rel
        p2 = base_dir / rel
        p = p1 if p1.exists() else p2
        if not p.exists():
            if rel in ALLOWED_MISSING_GITIGNORED_HLE:
                continue
            print("frozen missing:", manifest_path.name, rel)
            return False
        if not p.is_file() or sha(p) != expected:
            print("frozen mismatch:", manifest_path.name, rel)
            return False
    return True


def check():
    if not check_manifest_file(ROOT / "v4/study", ROOT / "v4/study/freeze-manifest.json"):
        print("v4 freeze check failed")
        return False
    if not check_manifest_file(ROOT / "v5/study", ROOT / "v5/study/freeze-manifest.json"):
        print("v5 freeze check failed")
        return False
    if not MANIFEST.exists():
        print("missing", MANIFEST)
        return False
    saved = json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]
    now = collect()
    bad = [k for k in sorted(set(saved) | set(now)) if saved.get(k) != now.get(k)]
    for k in bad:
        print("mismatch:", k)
    return not bad


def main():
    if "--check" in sys.argv:
        raise SystemExit(0 if check() else 1)
    if MANIFEST.exists():
        raise SystemExit("Already frozen; use --check")
    if not check_manifest_file(ROOT / "v4/study", ROOT / "v4/study/freeze-manifest.json"):
        raise SystemExit("v4 freeze check failed")
    if not check_manifest_file(ROOT / "v5/study", ROOT / "v5/study/freeze-manifest.json"):
        raise SystemExit("v5 freeze check failed")
    files = collect()
    MANIFEST.write_text(
        json.dumps(
            {
                "frozen_utc": datetime.now(timezone.utc).isoformat(),
                "purpose": "Prospective freeze before Study Cycle 2 main and seeded sessions; v4 and v5 Study 3 remain frozen in place",
                "files": files,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("frozen", len(files), "Study Cycle 2 files")


if __name__ == "__main__":
    main()

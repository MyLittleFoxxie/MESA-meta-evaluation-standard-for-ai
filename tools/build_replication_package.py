"""Build and verify double-blind replication archives for both REFSQ 2027 papers.

Usage:
    python3 tools/build_replication_package.py --check
"""
import argparse
import io
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

GATED_EXCLUDES = {
    "v4/study/sources/hle/data/test-00000-of-00001.parquet",
    "v4/study/sources/hle/repository/data/hle-test.jsonl",
    "v4/study/sources/hle/repository.tar.gz",
}

IDENTITY_PATTERNS = [
    (re.compile(r"Vitor\s+Raposo", re.I), "Double-Blind Signer"),
    (re.compile(r"\bVitor\b", re.I), "Signer"),
    (re.compile(r"\bRaposo\b", re.I), "Signer"),
    (re.compile(r"/Users/mylittlefoxxie", re.I), "/Users/researcher"),
    (re.compile(r"mylittlefoxxie", re.I), "researcher"),
    (re.compile(r"C:\\\\Users\\\\Fox", re.I), r"C:\\Users\\researcher"),
    (re.compile(r"C:/Users/Fox", re.I), "C:/Users/researcher"),
    (re.compile(r"\\Users\\Fox", re.I), r"\\Users\\researcher"),
    (re.compile(r"/Users/Fox", re.I), "/Users/researcher"),
]

LEAK_CHECK_RE = re.compile(r"vitor|raposo|mylittlefoxxie|Users[/\\]+Fox", re.I)

BINARY_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".gz", ".parquet", ".zip", ".pyc", ".svg"}


def load_frozen_paths():
    frozen = set()
    for mf in ("v4/study/freeze-manifest.json", "v5/study/freeze-manifest.json", "v5/study-cycle2/freeze-manifest.json"):
        p = ROOT / mf
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            for rel in data.get("files", {}):
                if rel.startswith("sources/") or rel == "file_server.py":
                    frozen.add(f"v4/study/{rel}")
                else:
                    frozen.add(rel)
            frozen.add(mf)
    return frozen


def sanitize_bytes(rel_path: str, raw: bytes, frozen_paths: set) -> bytes:
    if rel_path in frozen_paths or Path(rel_path).suffix.lower() in BINARY_SUFFIXES:
        return raw
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw
    changed = False
    for pat, repl in IDENTITY_PATTERNS:
        new_text = pat.sub(repl, text)
        if new_text != text:
            text = new_text
            changed = True
    return text.encode("utf-8") if changed else raw


def collect_files(prefixes, extra_files=()):
    out = []
    for f in extra_files:
        p = ROOT / f
        if p.is_file():
            out.append((f, p))
    for prefix in prefixes:
        base = ROOT / prefix
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(ROOT).as_posix()
            if "__pycache__" in rel or rel.endswith(".pyc") or rel in GATED_EXCLUDES:
                continue
            out.append((rel, p))
    return out


def build_archive(zip_path: Path, files, frozen_paths: set, readme_text: str):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.md", readme_text.encode("utf-8"))
        for rel, p in files:
            data = sanitize_bytes(rel, p.read_bytes(), frozen_paths)
            zf.writestr(rel, data)


def verify_archive(zip_path: Path):
    leaks = []
    count = 0
    with zipfile.ZipFile(zip_path, "r") as zf:
        for info in zf.infolist():
            count += 1
            if Path(info.filename).suffix.lower() in BINARY_SUFFIXES:
                continue
            raw = zf.read(info.filename)
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                continue
            m = LEAK_CHECK_RE.findall(text)
            if m:
                leaks.append((info.filename, sorted(set(m))))
    if leaks:
        raise AssertionError(f"Identity leak in {zip_path.name}: {leaks[:5]}")
    return count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify built archives for zero identity leaks")
    args = ap.parse_args()

    frozen = load_frozen_paths()

    mesa_files = collect_files(
        prefixes=["v4", "v5"],
        extra_files=["verify_manuscripts.py", "mesa_paper.tex", "references.bib", "llncs.cls", "splncs04.bst"],
    )
    mesa_readme = (
        "# Anonymized Replication Package — MESA Paper (REFSQ 2027)\n\n"
        "Contents:\n"
        "- `v4/`: Framework mapping (280 items to 30 concerns), Study 1 outputs, and frozen benchmark snapshots.\n"
        "  (Note: gated HLE data files `test-00000-of-00001.parquet` and `hle-test.jsonl` are excluded per HLE terms of use; "
        "their SHA-256 digests remain in `v4/study/freeze-manifest.json`.)\n"
        "- `v5/`: MESA rubric (`rubric.md`, `rubric-v5.1.md`), Cycle 1 (`v5/study/`), and Cycle 2 (`v5/study-cycle2/`).\n"
        "- `verify_manuscripts.py`: Deterministic manuscript and reference verification script.\n"
    )
    mesa_zip = DIST / "mesa_replication_package.zip"
    build_archive(mesa_zip, mesa_files, frozen, mesa_readme)

    paper2_files = collect_files(
        prefixes=["paper2", "v5/rubric"],
        extra_files=["verify_manuscripts.py", "paper2.tex", "references.bib", "llncs.cls", "splncs04.bst"],
    )
    paper2_readme = (
        "# Anonymized Replication Package — Paper 2 (REFSQ 2027)\n\n"
        "Contents:\n"
        "- `paper2/method/`: Three-level decision engine, schemas, and task matcher.\n"
        "- `paper2/preparation/`: Study controls, session runner, exposure probe, simulation, and protocol records.\n"
        "- `paper2/tests/`: Unit and methodological invariant tests.\n"
        "- `v5/rubric/`: MESA rubric definitions referenced by the decision engine.\n"
    )
    paper2_zip = DIST / "paper2_replication_package.zip"
    build_archive(paper2_zip, paper2_files, frozen, paper2_readme)

    if args.check:
        n1 = verify_archive(mesa_zip)
        n2 = verify_archive(paper2_zip)
        print(f"PASS: {mesa_zip.name} ({n1} files) and {paper2_zip.name} ({n2} files) built with 0 identity leaks.")


if __name__ == "__main__":
    main()


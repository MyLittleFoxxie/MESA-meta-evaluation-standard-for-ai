"""Acquire the fixed source snapshots for the four benchmarks. Never executes repository code.

HumanEval and TruthfulQA are copied from the earlier frozen snapshots and their hashes are checked
against that record. tau-bench is extracted from a GitHub tarball at a pinned commit. (HELM was fetched
and then removed from the study on 31 October 2026 because its 162 page paper made every prompt about
167 thousand tokens and its two earlier reviews were paper based; the subset rule is kept in git history.) Papers are fetched from arXiv and their text extracted with PDFKit (pdftext.swift) because
no Python PDF library is installed. Run from the repository root:
    python3 v4/study/fetch_sources.py [--cache DIR]
With --cache, tarballs and PDFs already present in DIR are used instead of downloading.
"""
import argparse
import datetime
import hashlib
import io
import json
import shutil
import subprocess
import tarfile
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SRC = HERE / "sources"
V3 = ROOT / "v3" / "study" / "sources"

PINNED = {
    "hle": {"repo": "centerforaisafety/hle", "commit": "22ed3074b1e7b134bcbc09028d0ba320839b0655", "paper": "2501.14249",
            "paper_title": "Humanity's Last Exam", "subset": None, "subset_reason": None,
            "note": "The dataset is distributed through a gated Hugging Face repository and is not in the code repository; the snapshot holds the evaluation code, README, rolling change log and documentation only."},
    "tau-bench": {"repo": "sierra-research/tau-bench", "commit": "59a200c6d575d595120f1cb70fea53cef0632f6b", "paper": "2406.12045",
                  "paper_title": "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains", "subset": None, "subset_reason": None},
}
COPIED = ["humaneval", "truthfulqa"]


def get(url, cache):
    name = url.rstrip("/").split("/")[-1]
    if cache:
        for p in Path(cache).rglob("*"):
            if p.is_file() and (p.name == name or p.stem == name or p.name.startswith(name)):
                return p.read_bytes()
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "MESA-research-source-snapshot"}), timeout=300).read()


def sha_tree(dest):
    return {str(p.relative_to(dest)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.rglob("*")) if p.is_file()}


def keep(parts, subset):
    if subset is None:
        return True
    rel = "/".join(parts)
    for rule in subset:
        if rule.endswith("/") and rel.startswith(rule):
            return True
        if rule.endswith("*.py"):
            folder = rule[:-4]
            if rel.startswith(folder) and rel[len(folder):].endswith(".py") and "/" not in rel[len(folder):]:
                return True
        if rel == rule:
            return True
    return False


def extract(raw, dest, subset):
    rd = dest / "repository"
    rd.mkdir(parents=True, exist_ok=True)
    excluded_nonregular, excluded_by_subset = [], 0
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as t:
        for m in t.getmembers():
            parts = Path(m.name).parts[1:]
            if not parts:
                continue
            if m.isdir():
                continue
            if not m.isfile():
                excluded_nonregular.append(m.name)
                continue
            if not keep(parts, subset):
                excluded_by_subset += 1
                continue
            target = rd.joinpath(*parts)
            if not target.resolve().is_relative_to(rd.resolve()):
                raise ValueError("path escape: " + m.name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(t.extractfile(m).read())
    return excluded_nonregular, excluded_by_subset


def paper_text(pdf_path, txt_path):
    subprocess.run(["swift", str(HERE / "pdftext.swift"), str(pdf_path), str(txt_path)], check=True, capture_output=True)
    text = txt_path.read_text()
    return text.count("=== PAGE ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache")
    a = ap.parse_args()
    SRC.mkdir(exist_ok=True)
    records = []
    v3 = {r["benchmark"]: r for r in json.loads((V3.parent / "sources.json").read_text())}
    for name in COPIED:
        dest = SRC / name
        if not dest.exists():
            shutil.copytree(V3 / name, dest)
        hashes = sha_tree(dest)
        old = v3[name]["sha256"]
        mismatch = [k for k in old if hashes.get(k) != old[k]]
        if mismatch:
            raise SystemExit(f"{name}: copied snapshot differs from the earlier record: {mismatch[:5]}")
        records.append({**v3[name], "origin": "copied from the earlier frozen snapshot; hashes checked against its record", "sha256": hashes})
        print(name, "copied and checked", len(hashes), "files", flush=True)
    for name, spec in PINNED.items():
        dest = SRC / name
        meta = dest / "snapshot.json"
        if meta.exists():
            records.append(json.loads(meta.read_text()))
            print(name, "already present", flush=True)
            continue
        dest.mkdir(parents=True, exist_ok=True)
        url = f"https://api.github.com/repos/{spec['repo']}/tarball/{spec['commit']}"
        raw = get(url, a.cache)
        (dest / "repository.tar.gz").write_bytes(raw)
        nonreg, by_subset = extract(raw, dest, spec["subset"])
        pdf = get("https://arxiv.org/pdf/" + spec["paper"], a.cache)
        (dest / "paper.pdf").write_bytes(pdf)
        pages = paper_text(dest / "paper.pdf", dest / "paper.txt")
        rec = {"benchmark": name, "repository_url": "https://github.com/" + spec["repo"], "commit": spec["commit"], "archive_url": url,
               "paper_url": "https://arxiv.org/pdf/" + spec["paper"], "paper_title": spec["paper_title"],
               "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "pages": pages,
               "text_extraction": "PDFKit via pdftext.swift; layout and figures lost",
               "subset_rules": spec["subset"], "subset_reason": spec["subset_reason"], "files_excluded_by_subset": by_subset,
               "excluded_nonregular": nonreg, "sha256": sha_tree(dest)}
        meta.write_text(json.dumps(rec, indent=2) + "\n")
        records.append(rec)
        print(name, spec["commit"][:8], "files", len(rec["sha256"]), "excluded by subset", by_subset, "pages", pages, flush=True)
    (HERE / "sources.json").write_text(json.dumps(records, indent=2) + "\n")


if __name__ == "__main__":
    main()

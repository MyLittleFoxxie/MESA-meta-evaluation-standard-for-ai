"""Measure prompt and input sizes for information. No ceilings are set; nothing is trimmed.

Characters are exact; tokens are an estimate at four characters per token, marked as such.
Run from the repository root: python3 v4/study/sizes.py
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
jobs = json.loads((HERE / "jobs.json").read_text())["jobs"]
rows = []
for j in jobs:
    p = (HERE / "prompts" / f"{j['id']}.txt").read_text()
    src = HERE / "sources" / j["benchmark"]
    paper = (src / "paper.txt").read_text()
    repo_files = [x for x in (src / "repository").rglob("*") if x.is_file()]
    text_bytes = sum(x.stat().st_size for x in repo_files if b"\0" not in x.read_bytes()[:4096])
    rows.append({"job": j["id"], "benchmark": j["benchmark"], "framework": j["framework"], "prompt_chars": len(p), "prompt_tokens_estimate": len(p) // 4,
                 "paper_chars": len(paper), "repository_files": len(repo_files), "repository_text_bytes": text_bytes})
with (HERE / "sizes.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
by_bench = {}
for r in rows:
    by_bench.setdefault(r["benchmark"], []).append(r["prompt_tokens_estimate"])
print(json.dumps({b: {"prompts": len(v), "min_tokens_estimate": min(v), "max_tokens_estimate": max(v)} for b, v in by_bench.items()}, indent=1))
print("largest prompts:", sorted(((r["prompt_tokens_estimate"], r["job"]) for r in rows), reverse=True)[:5])

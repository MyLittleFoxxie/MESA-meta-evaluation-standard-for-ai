"""Write synthetic responses for every job so the analysis can be exercised end to end before any session.

The responses are schema valid and random; quotes are copied from the real sources so that citation checks
have something to match. Nothing here is evidence about any benchmark. Output goes to a separate folder
(default dry-run/) and never to outputs/. Run from the repository root: python3 v4/study/synth.py
"""
import argparse
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAT = HERE / "materials"
JOBS = json.loads((HERE / "jobs.json").read_text())["jobs"]
BASIS = ["evidence_found", "absence_of_information", "defect_found", "not_applicable"]
ANSWERS = {"BB": ["0", "5", "10", "15", "n/a"], "SC": ["satisfied", "unsatisfied", "not_applicable"], "H2B": ["present", "not_mentioned", "done_wrongly"],
           "ABC": ["1", "0"], "CAL": ["1", "2", "3", "4", "5", "unknown"], "RUBRIC": ["stated", "shown", "checked", "contradicted", "insufficient_evidence", "not_applicable"]}


def quote_from(text, rng):
    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 40]
    return rng.choice(lines)[:120] if lines else "no text"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "dry-run"))
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    for job in JOBS:
        src = HERE / "sources" / job["benchmark"]
        paper = (src / "paper.txt").read_text()
        readmes = [p for p in (src / "repository").iterdir() if p.is_file() and p.name.lower().startswith("readme")]
        readme = readmes[0].read_text()
        fw = job["framework"]
        if fw == "RUBRIC":
            rubric = json.loads((MAT / "rubric.json").read_text())
            desc = [{"facet": f["facet"], "value": rng.choice(f["values"]).split(" (")[0], "reason": "synthetic", "evidence": [{"source": "paper.txt", "locator": "page 1", "quote": quote_from(paper, rng)}]} for f in rubric["part_a"]]
            items = [b["id"] for b in rubric["part_b"]]
            resp = {"benchmark": job["benchmark"], "framework": "RUBRIC", "limits": "synthetic dry run", "description": desc, "judgments": []}
            for i in items:
                ans = rng.choice(ANSWERS["RUBRIC"])
                resp["judgments"].append({"item_id": i, "answer": ans, "basis": "absence_of_information" if ans == "insufficient_evidence" else rng.choice(BASIS), "reason": "synthetic", "missing": "synthetic missing note" if ans in ("insufficient_evidence", "stated") else "", "checks": "none",
                                          "evidence": [] if ans == "insufficient_evidence" else [{"source": rng.choice(["paper.txt", f"repository/{readmes[0].name}", "repository/does-not-exist.py"]), "locator": f"page {rng.randint(1, 5)}", "quote": quote_from(paper if rng.random() < 0.7 else readme, rng)}]})
        else:
            packet = json.loads((MAT / f"framework-{fw}.json").read_text())
            resp = {"benchmark": job["benchmark"], "framework": fw, "limits": "synthetic dry run", "judgments": []}
            for it in packet["items"]:
                if fw == "OECD":
                    ans = rng.choice(it["values"]).split(" (")[0]
                elif fw == "ECBD":
                    ans = rng.choice(["The paper states the capabilities as ...", "Not stated in the sources.", "The authors justify this by ..."])
                else:
                    ans = rng.choice(ANSWERS[fw])
                basis = rng.choice(BASIS)
                resp["judgments"].append({"item_id": it["id"], "answer": ans, "basis": basis, "reason": "synthetic", "missing": "synthetic" if basis == "absence_of_information" else "", "checks": "none",
                                          "evidence": [{"source": rng.choice(["paper.txt", f"repository/{readmes[0].name}"]), "locator": f"page {rng.randint(1, 5)}", "quote": quote_from(paper, rng)}]})
        out = Path(a.out) / job["id"] / "attempt-1"
        out.mkdir(parents=True, exist_ok=True)
        (out / "response.txt").write_text(json.dumps(resp))
        (out / "metadata.json").write_text(json.dumps({**job, "status": "completed", "elapsed_seconds": 1.0, "synthetic": True}))
        (out / "events.jsonl").write_text(json.dumps({"type": "assistant", "message": {"model": "synthetic", "content": [{"type": "tool_use", "id": "x", "name": "mcp__benchmark__list_files", "input": {}}]}}) + "\n" +
                                          json.dumps({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "x", "is_error": False, "content": "..."}]}}) + "\n" +
                                          json.dumps({"type": "result", "usage": {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 5}}) + "\n")
    print("synthetic responses for", len(JOBS), "jobs in", a.out)


if __name__ == "__main__":
    main()

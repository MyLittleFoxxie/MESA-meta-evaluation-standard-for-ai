"""Amendment 1 runner: a second repetition of BetterBench and the Scorecard on HumanEval, requested after the
26 main sessions to estimate same framework repeat variation. The frozen files are not changed: the prompt is
the frozen prompts/humaneval-BB.txt or prompts/humaneval-SC.txt, the schema and file server are the same, and
the command is built by run.command. Outputs go to outputs/humaneval-BB-2 and outputs/humaneval-SC-2. See
addition.md. Run from anywhere: python3 v4/study/run_addition.py [--job ID] [--retry]
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run  # noqa: E402

JOBS = [{"id": "humaneval-BB-2", "benchmark": "humaneval", "framework": "BB", "repeat": 2, "phase": "main", "study": 1, "amendment": 1},
        {"id": "humaneval-SC-2", "benchmark": "humaneval", "framework": "SC", "repeat": 2, "phase": "main", "study": 1, "amendment": 1}]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job")
    ap.add_argument("--retry", action="store_true")
    a = ap.parse_args()
    run.verify_freeze()
    outputs = HERE / "outputs"
    for job in JOBS:
        if a.job and job["id"] != a.job:
            continue
        prior = sorted((outputs / job["id"]).glob("attempt-*")) if (outputs / job["id"]).exists() else []
        if prior:
            last = json.loads((prior[-1] / "metadata.json").read_text())
            if last["status"] == "completed" or not a.retry:
                print("SKIP retained", job["id"], last["status"], flush=True)
                continue
        if len(list(outputs.glob("*/attempt-*/metadata.json"))) >= run.CAP:
            raise SystemExit("Attempt cap reached")
        out = outputs / job["id"] / f"attempt-{len(prior) + 1}"
        out.mkdir(parents=True)
        with tempfile.TemporaryDirectory(prefix="mesa-v4-") as tmp:
            work = Path(tmp)
            cmd = run.command(job)
            env = dict(os.environ)
            for k in list(env):
                if k.startswith(("OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY", "CLAUDE_CODE_")):
                    env.pop(k)
            prompt = HERE / "prompts" / f"{job['benchmark']}-{job['framework']}.txt"  # the frozen repetition 1 prompt, unchanged
            start = time.time()
            meta = {**job, "prompt_file": prompt.name, "requested_model": run.MODEL, "effort": run.EFFORT, "cli_version": subprocess.check_output([run.BIN, "--version"], text=True).strip(),
                    "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "prompt_sha256": run.sha(prompt), "schema_sha256": run.sha(HERE / "materials" / f"schema-{job['framework']}.json"),
                    "command": cmd, "cwd": str(work), "status": "running"}
            (out / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
            print("START", job["id"], flush=True)
            with prompt.open() as inp, (out / "events.jsonl").open("w") as stdout, (out / "stderr.txt").open("w") as stderr:
                result = subprocess.run(cmd, stdin=inp, stdout=stdout, stderr=stderr, env=env, cwd=work)
            run.extract_response(out / "events.jsonl", out)
            meta.update(exit_code=result.returncode, elapsed_seconds=time.time() - start,
                        status="completed" if (out / "response.txt").exists() and (out / "response.txt").stat().st_size else "failed",
                        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
            (out / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
            print("END", job["id"], meta["status"], result.returncode, flush=True)
            if result.returncode != 0 or meta["status"] != "completed":
                raise SystemExit("Stopped after failure; no automatic retry")


if __name__ == "__main__":
    main()

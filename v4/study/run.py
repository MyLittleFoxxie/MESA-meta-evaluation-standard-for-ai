"""Sequential Claude Code study runner. One session per job, one framework per session. No automatic retries or response repairs.

Adapted from the earlier study's runner: the model is Claude Sonnet 5.5, every job gets its framework's own
response schema, and every job offers the confined file server over the fixed snapshot. Main sessions refuse
to run until the study is frozen. Run from anywhere:
    python3 v4/study/run.py --phase pilot [--job ID]
    python3 v4/study/run.py --phase main [--job ID] [--retry]
"""
import argparse
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BIN = shutil.which("claude")
CFG = json.loads((HERE / "jobs.json").read_text())
MODEL, EFFORT, CAP = CFG["model"], CFG["effort"], CFG["attempt_cap"]
TOOLS = ["mcp__benchmark__list_files", "mcp__benchmark__read_file"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify_freeze():
    f = HERE / "freeze-manifest.json"
    if not f.exists():
        raise ValueError("study is not frozen; main sessions refuse to run")
    for name, h in json.loads(f.read_text())["files"].items():
        path = HERE / name if (HERE / name).exists() else HERE.parent.parent / name  # mapping and rubric paths are relative to the repository root
        if sha(path) != h:
            raise ValueError("freeze mismatch: " + name)


def schema_argument(framework):
    # Claude Code rejects the draft 2020-12 "$schema" metadata key. Only that key is removed; the file is unchanged.
    schema = json.loads((HERE / "materials" / f"schema-{framework}.json").read_text())
    schema.pop("$schema", None)
    return json.dumps(schema)


def command(job):
    cmd = [BIN, "-p", "--model", MODEL, "--effort", EFFORT, "--output-format", "stream-json", "--verbose", "--no-session-persistence",
           "--system-prompt", (HERE / "materials/system.txt").read_text().strip(), "--json-schema", schema_argument(job["framework"]),
           "--setting-sources", "", "--strict-mcp-config", "--tools", "", "--disable-slash-commands", "--permission-mode", "dontAsk", "--permission-prompts", "none",
           "--autocompact", "1000000"]  # the largest window the CLI allows, so the supplied paper text is not summarized away mid session
    mcp = {"mcpServers": {"benchmark": {"command": sys.executable, "args": [str(HERE / "file_server.py"), str(HERE / "sources" / job["benchmark"] / "repository")]}}}
    cmd += ["--mcp-config", json.dumps(mcp), "--allowedTools", *TOOLS]
    return cmd


def extract_response(events_path, out):
    """Write the structured result verbatim. Never repair or reformat the content."""
    for line in events_path.read_text().splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "result":
            if e.get("structured_output") is not None:
                (out / "response.txt").write_text(json.dumps(e["structured_output"]))
                return
            if isinstance(e.get("result"), str) and e["result"].strip():
                (out / "response.txt").write_text(e["result"])
                return


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["pilot", "main"], required=True)
    ap.add_argument("--job")
    ap.add_argument("--retry", action="store_true", help="create the next attempt after a retained failed attempt")
    a = ap.parse_args()
    if not BIN:
        raise SystemExit("claude command not found")
    if a.phase == "main":
        verify_freeze()
    outputs = HERE / "outputs"
    for job in CFG["jobs"]:
        if job["phase"] != a.phase or (a.job and job["id"] != a.job):
            continue
        prior = sorted((outputs / job["id"]).glob("attempt-*")) if (outputs / job["id"]).exists() else []
        if prior:
            last = json.loads((prior[-1] / "metadata.json").read_text())
            if last["status"] == "completed" or not a.retry:
                print("SKIP retained", job["id"], last["status"], flush=True)
                continue
        if len(list(outputs.glob("*/attempt-*/metadata.json"))) >= CAP:
            raise SystemExit("Attempt cap reached")
        out = outputs / job["id"] / f"attempt-{len(prior) + 1}"
        out.mkdir(parents=True)
        with tempfile.TemporaryDirectory(prefix="mesa-v4-") as tmp:
            work = Path(tmp)
            cmd = command(job)
            env = dict(os.environ)
            for k in list(env):  # existing Claude Code login is used; no keys pass through
                if k.startswith(("OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY", "CLAUDE_CODE_")):
                    env.pop(k)
            prompt = HERE / "prompts" / f"{job['id']}.txt"
            start = time.time()
            meta = {**job, "requested_model": MODEL, "effort": EFFORT, "cli_version": subprocess.check_output([BIN, "--version"], text=True).strip(),
                    "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "prompt_sha256": sha(prompt), "schema_sha256": sha(HERE / "materials" / f"schema-{job['framework']}.json"),
                    "command": cmd, "cwd": str(work), "status": "running"}
            (out / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
            print("START", job["id"], flush=True)
            with prompt.open() as inp, (out / "events.jsonl").open("w") as stdout, (out / "stderr.txt").open("w") as stderr:
                result = subprocess.run(cmd, stdin=inp, stdout=stdout, stderr=stderr, env=env, cwd=work)
            extract_response(out / "events.jsonl", out)
            meta.update(exit_code=result.returncode, elapsed_seconds=time.time() - start,
                        status="completed" if (out / "response.txt").exists() and (out / "response.txt").stat().st_size else "failed",
                        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
            (out / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
            print("END", job["id"], meta["status"], result.returncode, flush=True)
            if result.returncode != 0 or meta["status"] != "completed":
                raise SystemExit("Stopped after failure; no automatic retry")


if __name__ == "__main__":
    main()

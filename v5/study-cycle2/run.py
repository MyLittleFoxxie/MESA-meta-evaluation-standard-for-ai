"""Run Study Cycle 2 reviewer sessions for Gemini 3.8 Flash (Medium) via agy and Claude Sonnet 5.5 (Medium) via Claude Code.

Refuses to run main or seeded sessions unless freeze-manifest.json exists and verifies.
Never repairs or edits model output; every attempt is saved under outputs/<job-id>/attempt-<n>/.
Run from the repository root: python v5/study-cycle2/run.py --phase pilot|main|seeded [--job JOB_ID]
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
import freeze
from validate import rule_findings, validate

AGY_BIN = shutil.which("agy") or str(Path.home() / ".gemini/bin/agy.exe")
CLAUDE_BIN = shutil.which("claude") or str(Path.home() / ".local/bin/claude.exe")
PYTHON_BIN = sys.executable or "python"

GUARD_SCRIPT = """import json, sys
data = json.load(sys.stdin)
tc = data.get("toolCall", {})
name = tc.get("name", "")
args = tc.get("args", {})
if name == "finish":
    print(json.dumps({"decision": "allow"}))
elif name == "call_mcp_tool" and args.get("ServerName") == "benchmark" and args.get("ToolName") in ("list_files", "read_file"):
    print(json.dumps({"decision": "allow"}))
elif name in ("read_file", "view_file") and "antigravity-cli/mcp/benchmark" in str(args.get("Path", "")).replace("\\\\", "/"):
    print(json.dumps({"decision": "allow"}))
else:
    print(json.dumps({"decision": "deny", "reason": "Isolated benchmark review session: only call_mcp_tool on benchmark (list_files, read_file) and finish are permitted."}))
"""

HOOKS_JSON = {
    "isolation-guard": {
        "PreToolUse": [
            {
                "matcher": "*",
                "hooks": [
                    {
                        "type": "command",
                        "command": f"{PYTHON_BIN} guard.py" if " " not in str(PYTHON_BIN) else "python guard.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}


def manifest():
    return json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))


def total_attempts(outputs, phase_jobs):
    job_ids = {j["id"] for j in phase_jobs}
    return sum(
        1
        for p in outputs.glob("*/attempt-*/metadata.json")
        if p.parent.parent.name in job_ids
    )


def has_valid(job_dir):
    for p in sorted(job_dir.glob("attempt-*/response.txt")):
        try:
            if not validate(json.loads(p.read_text(encoding="utf-8"))):
                return True
        except Exception:
            pass
    return False


def extract_claude_response(events_text):
    structured = None
    result_text = None
    for line in events_text.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "result":
            if e.get("structured_output") is not None:
                structured = json.dumps(e["structured_output"], indent=2)
            elif isinstance(e.get("result"), str) and e["result"].strip():
                result_text = e["result"]
        if e.get("type") == "assistant":
            for block in e.get("message", {}).get("content", []) or []:
                if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "StructuredOutput":
                    structured = json.dumps(block.get("input"), indent=2)
    return structured if structured is not None else (result_text or events_text)


def extract_agy_response(events_text):
    structured = None
    result_text = None
    for line in events_text.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("event") == "result" and isinstance(e.get("result"), dict):
            res = e["result"]
            if res.get("structured_output") is not None:
                structured = json.dumps(res["structured_output"], indent=2)
            elif isinstance(res.get("response"), str) and res["response"].strip():
                result_text = res["response"]
        if e.get("event") == "step_update":
            su = e.get("step_update", {})
            if su.get("tool_name") == "finish" and isinstance(su.get("tool_info"), dict):
                params = su["tool_info"].get("parameters")
                if isinstance(params, dict) and params:
                    structured = json.dumps(params, indent=2)
    return structured if structured is not None else (result_text or events_text)


def run_gemini_attempt(job, prompt_text, src_dir):
    schema_path = HERE / "materials/schema-RUBRIC.json"
    system_text = (HERE / "materials/system.txt").read_text(encoding="utf-8")
    subprocess.run([AGY_BIN, "mcp", "remove", "benchmark"], capture_output=True, text=True)
    add_res = subprocess.run(
        [AGY_BIN, "mcp", "add", "benchmark", PYTHON_BIN, str(HERE / "file_server.py"), str(src_dir)],
        capture_output=True,
        text=True,
    )
    if add_res.returncode != 0:
        raise RuntimeError(f"agy mcp add failed: {add_res.stderr}")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            agents_dir = tmp_path / ".agents"
            agents_dir.mkdir(parents=True, exist_ok=True)
            (agents_dir / "guard.py").write_text(GUARD_SCRIPT, encoding="utf-8")
            (agents_dir / "hooks.json").write_text(json.dumps(HOOKS_JSON, indent=2), encoding="utf-8")
            (tmp_path / "GEMINI.md").write_text(
                system_text
                + "\nIMPORTANT: Use ONLY call_mcp_tool on ServerName='benchmark' (ToolName='list_files' or 'read_file') to inspect repository files, and then call finish with the JSON object matching the schema. Do not call any other tools.\n",
                encoding="utf-8",
            )
            cmd = [
                AGY_BIN,
                "--model",
                job["model"],
                "--effort",
                job["effort"],
                "--output-format",
                "stream-json",
                "--json-schema",
                str(schema_path),
                "--disable-slash-commands",
                "--new-project",
                "--dangerously-skip-permissions",
                "--sandbox",
            ]
            proc = subprocess.run(
                cmd,
                input=prompt_text,
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                cwd=tmp,
                timeout=1800,
            )
            return cmd, proc.returncode, proc.stdout, proc.stderr
    finally:
        subprocess.run([AGY_BIN, "mcp", "remove", "benchmark"], capture_output=True, text=True)


def run_claude_attempt(job, prompt_text, src_dir):
    mcp = {
        "mcpServers": {
            "benchmark": {
                "command": PYTHON_BIN,
                "args": [str(HERE / "file_server.py"), str(src_dir)],
            }
        }
    }
    schema_obj = json.loads((HERE / "materials/schema-RUBRIC.json").read_text(encoding="utf-8"))
    schema_obj.pop("$schema", None)
    schema_text = json.dumps(schema_obj)
    system_text = (HERE / "materials/system.txt").read_text(encoding="utf-8")
    env = {
        k: v
        for k, v in os.environ.items()
        if not k.startswith(("CLAUDE_CODE_", "ANTHROPIC_BASE_URL", "ANTHROPIC_MODEL"))
    }
    with tempfile.TemporaryDirectory() as tmp:
        mcp_path = Path(tmp) / "mcp.json"
        mcp_path.write_text(json.dumps(mcp), encoding="utf-8")
        cmd = [
            CLAUDE_BIN,
            "-p",
            "--model",
            job["model"],
            "--effort",
            job["effort"],
            "--output-format",
            "stream-json",
            "--verbose",
            "--system-prompt",
            system_text,
            "--json-schema",
            schema_text,
            "--mcp-config",
            str(mcp_path),
            "--strict-mcp-config",
            "--tools",
            "",
            "--allowedTools",
            "mcp__benchmark__list_files,mcp__benchmark__read_file",
            "--disallowedTools",
            "WebSearch,WebFetch,Bash,Task,Agent,Skill,SlashCommand,TodoWrite,NotebookEdit",
            "--disable-slash-commands",
            "--setting-sources",
            "",
            "--no-session-persistence",
            "--permission-mode",
            "dontAsk",
        ]
        proc = subprocess.run(
            cmd,
            input=prompt_text,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            cwd=tmp,
            env=env,
            timeout=1800,
        )
        return cmd, proc.returncode, proc.stdout, proc.stderr


def run_one(job, outputs, cap, phase_jobs):
    if total_attempts(outputs, phase_jobs) >= cap:
        raise SystemExit(f"Stopping: phase attempt cap ({cap}) reached")
    job_dir = outputs / job["id"]
    job_dir.mkdir(parents=True, exist_ok=True)
    prior = sorted(job_dir.glob("attempt-*"))
    model_attempts = [
        p
        for p in prior
        if (p / "metadata.json").exists()
        and "--json-schema is not a valid JSON Schema"
        not in (p / "stderr.txt").read_text(encoding="utf-8", errors="replace")
        and '"api_error_status":429'
        not in (p / "events.jsonl").read_text(encoding="utf-8", errors="replace")
        and "You've hit your session limit"
        not in (p / "events.jsonl").read_text(encoding="utf-8", errors="replace")
    ]
    if len(model_attempts) >= 2:
        return "retry_cap_reached"
    attempt = len(prior) + 1
    out = job_dir / f"attempt-{attempt}"
    out.mkdir()
    prompt_path = HERE / "prompts" / f"{job['id']}.txt"
    prompt_bytes = prompt_path.read_bytes()
    prompt_text = prompt_bytes.decode("utf-8")
    src = (ROOT / job["source_root"]).resolve()
    start = datetime.now(timezone.utc).isoformat()
    t0 = time.time()
    status = "completed"
    try:
        if job["family"] == "gemini":
            cmd, rc, stdout, stderr = run_gemini_attempt(job, prompt_text, src)
            extracted = extract_agy_response(stdout)
        else:
            cmd, rc, stdout, stderr = run_claude_attempt(job, prompt_text, src)
            extracted = extract_claude_response(stdout)
        (out / "events.jsonl").write_text(stdout, encoding="utf-8", newline="\n")
        (out / "response.txt").write_text(extracted, encoding="utf-8", newline="\n")
        (out / "stderr.txt").write_text(stderr, encoding="utf-8", newline="\n")
        if rc != 0:
            status = f"nonzero_exit_{rc}"
    except subprocess.TimeoutExpired as e:
        rc = None
        status = "timeout"
        cmd = []
        (out / "events.jsonl").write_text((e.stdout or ""), encoding="utf-8", newline="\n")
        (out / "stderr.txt").write_text((e.stderr or ""), encoding="utf-8", newline="\n")
    meta = {
        "job": job,
        "attempt": attempt,
        "started_utc": start,
        "elapsed_seconds": round(time.time() - t0, 2),
        "status": status,
        "returncode": rc,
        "prompt_sha256": hashlib.sha256(prompt_bytes).hexdigest(),
        "command": cmd,
    }
    (out / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8", newline="\n")
    try:
        data = json.loads((out / "response.txt").read_text(encoding="utf-8"))
        errors = validate(data)
        findings = [] if errors else rule_findings(data)
    except Exception as e:
        errors, findings = [str(e)], []
    print(
        job["id"],
        f"attempt-{attempt}",
        status,
        f"{meta['elapsed_seconds']}s",
        "valid" if not errors else errors[:2],
        f"rule_findings={len(findings)}",
        flush=True,
    )
    return "valid" if not errors else "invalid"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["pilot", "main", "seeded"], required=True)
    ap.add_argument("--job")
    ap.add_argument("--outputs", default=str(HERE / "outputs"))
    a = ap.parse_args()
    if a.phase in ("main", "seeded"):
        if not (HERE / "freeze-manifest.json").exists():
            raise SystemExit("Refusing to run main/seeded phase before freeze.py creates freeze-manifest.json")
        if not freeze.check():
            raise SystemExit("Refusing to run main/seeded phase: freeze check failed")
    m = manifest()
    outputs = Path(a.outputs)
    phase_jobs = [j for j in m["jobs"] if j["phase"] == a.phase]
    cap = (
        m["attempt_cap_main"]
        if a.phase == "main"
        else (m["attempt_cap_seeded"] if a.phase == "seeded" else 6)
    )
    for job in phase_jobs:
        if a.job and job["id"] != a.job:
            continue
        job_dir = outputs / job["id"]
        if has_valid(job_dir):
            continue
        res = run_one(job, outputs, cap, phase_jobs)
        if res == "invalid":
            run_one(job, outputs, cap, phase_jobs)


if __name__ == "__main__":
    main()


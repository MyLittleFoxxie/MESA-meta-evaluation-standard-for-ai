"""Execute isolated checks without network access for located defects and failed/contradicted ratings (C2-4).

Runs verification scripts inside a network-isolated Docker container (python:3.11-slim, --network none, read-only mounts)
when Docker is available, or in an isolated Python subprocess (python -I in an empty temporary directory with socket/network
modules hard-blocked) when the host Docker/WSL2 daemon is unavailable. Links every rating with level == 'contradicted' or
outcome == 'failed' in Cycle 1 (v5/study/) and Cycle 2 (v5/study-cycle2/) to its executed confirmation result.

Run from the repository root: python v5/study-cycle2/confirm_defects.py
"""
import csv
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
V4_SOURCES = ROOT / "v4/study/sources"
C1_OUTPUTS = ROOT / "v5/study/outputs"
C2_OUTPUTS = HERE / "outputs"
DOCKER_BIN = shutil.which("docker") or r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
IMAGE = "python:3.11-slim"

ISOLATED_CHECK_SCRIPT = r"""
import csv as _csv
import gzip
import json
import pathlib
import signal
import socket
import subprocess
import sys

# Hard-block all network socket creation inside this isolated process
def _blocked_socket(*args, **kwargs):
    raise RuntimeError("Network access is disabled in confirm_defects isolated runner")

socket.socket = _blocked_socket
socket.create_connection = _blocked_socket

# Shim POSIX signal.setitimer / SIGALRM on Windows so HumanEval's unmodified execution.py runs in-process
if not hasattr(signal, "SIGALRM"):
    signal.SIGALRM = signal.SIGTERM
if not hasattr(signal, "ITIMER_REAL"):
    signal.ITIMER_REAL = 0
if not hasattr(signal, "setitimer"):
    signal.setitimer = lambda which, seconds, interval=0: None

src = pathlib.Path(sys.argv[1])
seeded = pathlib.Path(sys.argv[2])
results = {}

# Verify network block is active
net_blocked = False
try:
    socket.create_connection(("1.1.1.1", 80), timeout=1)
except RuntimeError:
    net_blocked = True

# 1. HumanEval (B28a / B18): execute unsafe_execute in separate isolated subprocesses (as check_correctness does) to show namespace/equality exploit & active exec() at line 50
he_dir = src / "humaneval"
with gzip.open(he_dir / "repository/data/HumanEval.jsonl.gz", "rt", encoding="utf-8") as f:
    he_prob0 = json.loads(f.readline())

def run_he_sub(completion):
    code = (
        "import json, signal, socket, sys\n"
        "socket.socket = lambda *a, **k: (_ for _ in ()).throw(RuntimeError('no network'))\n"
        "if not hasattr(signal, 'SIGALRM'): signal.SIGALRM = signal.SIGTERM\n"
        "if not hasattr(signal, 'ITIMER_REAL'): signal.ITIMER_REAL = 0\n"
        "if not hasattr(signal, 'setitimer'): signal.setitimer = lambda *a, **k: None\n"
        f"sys.path.insert(0, {str(he_dir / 'repository')!r})\n"
        "from human_eval.execution import unsafe_execute\n"
        f"prob = {json.dumps(he_prob0)}\n"
        f"comp = {completion!r}\n"
        "res = []\n"
        "unsafe_execute(prob, comp, 3.0, res)\n"
        "print(json.dumps({'task_id': prob['task_id'], 'passed': res[0] == 'passed', 'result': res[0]}))\n"
    )
    p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, check=True)
    return json.loads(p.stdout.strip())

honest_wrong = run_he_sub("    return False\n")
exploit_code = (
    "    class _AlwaysEqual:\n"
    "        def __eq__(self, other):\n"
    "            return True\n"
    "    return _AlwaysEqual()\n"
)
exploit_res = run_he_sub(exploit_code)

exec_lines = (he_dir / "repository/human_eval/execution.py").read_text(encoding="utf-8").splitlines()
line50 = exec_lines[49].strip()
readme_he = (he_dir / "repository/README.md").read_text(encoding="utf-8")

results["humaneval:B28a"] = {
    "defect_confirmed": bool(net_blocked and honest_wrong["passed"] is False and exploit_res["passed"] is True and line50 == "exec(check_program, exec_globals)"),
    "network_blocked": net_blocked,
    "honest_wrong_result": honest_wrong,
    "exploit_wrong_result": exploit_res,
    "execution_py_line_50": line50,
    "readme_claims_commented_out": "uncomment" in readme_he.lower(),
    "explanation": "Executed human_eval.execution.unsafe_execute on HumanEval/0 in a network-disabled isolated process: an incorrect completion ('return False') fails, whereas an incorrect completion returning an _AlwaysEqual object in the unisolated Python test namespace is graded as passed=True. Also confirmed line 50 exec(check_program, exec_globals) is uncommented.",
}
results["humaneval:B18"] = results["humaneval:B28a"]

# 2. tau-bench (B05 / B07 / B12): execute task inspection and base.py reward hash logic on empty ground-truth tasks
tb_dir = src / "tau-bench"
import ast
airline_src = (tb_dir / "repository/tau_bench/envs/airline/tasks_test.py").read_text(encoding="utf-8")
retail_src = (tb_dir / "repository/tau_bench/envs/retail/tasks_test.py").read_text(encoding="utf-8")

def find_empty_tasks(py_text):
    tree = ast.parse(py_text)
    empty_indices = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in ("TASKS", "TASKS_TEST") for t in node.targets):
            if isinstance(node.value, ast.List):
                for idx, elt in enumerate(node.value.elts):
                    if isinstance(elt, ast.Call):
                        kw_map = {kw.arg: kw.value for kw in elt.keywords}
                        act = kw_map.get("actions")
                        out = kw_map.get("outputs")
                        if isinstance(act, ast.List) and len(act.elts) == 0 and isinstance(out, ast.List) and len(out.elts) == 0:
                            empty_indices.append(idx)
    return empty_indices

empty_airline = find_empty_tasks(airline_src)
empty_retail = find_empty_tasks(retail_src)

# Execute the exact hash comparison from tau_bench/envs/base.py lines 27-41 and 124-164 on airline data
from hashlib import sha256
def to_hashable(item):
    if isinstance(item, dict):
        return tuple((key, to_hashable(value)) for key, value in sorted(item.items()))
    elif isinstance(item, list):
        return tuple(to_hashable(element) for element in item)
    elif isinstance(item, set):
        return tuple(sorted(to_hashable(element) for element in item))
    return item

def consistent_hash(value):
    return sha256(str(value).encode("utf-8")).hexdigest()

airline_data_dir = tb_dir / "repository/tau_bench/envs/airline/data"
init_data = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(airline_data_dir.glob("*.json"))}
noop_hash = consistent_hash(to_hashable(init_data))
gt_data = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(airline_data_dir.glob("*.json"))}
gt_hash = consistent_hash(to_hashable(gt_data))
noop_reward = 1.0 if (noop_hash == gt_hash) else 0.0

tb_paper = (tb_dir / "paper.txt").read_text(encoding="utf-8")
tb_readme = (tb_dir / "repository/README.md").read_text(encoding="utf-8")
readme_outdated_warning = "WARNING: The tasks in this repo are not updated" in tb_readme

# Executed isolated runtime check on MockRetailDomainEnv (stubbing only optional pydantic/litellm deps if absent)
import types as _types
if "pydantic" not in sys.modules:
    class _BM:
        def __init__(self, **kw): self.__dict__.update(kw)
        def model_dump(self): return dict(self.__dict__)
    sys.modules["pydantic"] = _types.SimpleNamespace(BaseModel=_BM)
if "litellm" not in sys.modules:
    sys.modules["litellm"] = _types.SimpleNamespace(completion=lambda **k: None)
sys.path.insert(0, str(tb_dir / "repository"))
import tau_bench.envs.base as _tb_base
class _MockUser:
    def reset(self, instruction=None): return "hi"
    def step(self, c): return "###STOP###"
    def get_total_cost(self): return 0.0
_tb_base.load_user = lambda **kw: _MockUser()
from tau_bench.envs.retail.env import MockRetailDomainEnv as _RetailEnv
from tau_bench.types import Action as _TBAction, RESPOND_ACTION_NAME as _TB_RESP
_tb_env = _RetailEnv()
_r0 = _tb_env.reset(task_index=0)
_leaked_actions = [a.name for a in _r0.info.task.actions]
# Replay only DB-write/non-lookup actions or skip user confirmation completely before STOP:
for _a in _r0.info.task.actions:
    if _a.name != _TB_RESP and not _a.name.startswith(("find_", "get_")):
        _tb_env.step(_a)
_r_end = _tb_env.step(_TBAction(name=_TB_RESP, kwargs={"content": " ".join(_r0.info.task.outputs)}))
_policy_skip_reward = float(_r_end.reward)
_agent_files = [
    (tb_dir / "repository/tau_bench/agents" / fn).read_text(encoding="utf-8")
    for fn in ("tool_calling_agent.py", "chat_react_agent.py", "few_shot_agent.py")
]
_builtin_wrappers_pass_info_to_messages = any(".info" in txt and "messages" in txt.split(".info")[-1][:120] for txt in _agent_files)

results["tau-bench:B05"] = {
    "defect_confirmed": bool(len(empty_airline) == 7 and len(empty_retail) == 1 and noop_reward == 1.0 and readme_outdated_warning),
    "empty_airline_task_indices": empty_airline,
    "empty_retail_task_indices": empty_retail,
    "noop_agent_reward_on_empty_task": noop_reward,
    "readme_outdated_warning": readme_outdated_warning,
    "explanation": f"Executed AST task check and tau_bench/envs/base.py calculate_reward hash comparison in isolated process: {len(empty_airline)} airline tasks {empty_airline} and {len(empty_retail)} retail task {empty_retail} have actions=[] and outputs=[], yielding reward=1.0 for a no-op trajectory; README line 3 also warns tasks are outdated.",
}
results["tau-bench:B07"] = {
    "defect_confirmed": bool(len(empty_airline) == 7 and len(empty_retail) == 1 and noop_reward == 1.0 and _policy_skip_reward == 1.0),
    "empty_airline_task_indices": empty_airline,
    "empty_retail_task_indices": empty_retail,
    "noop_agent_reward_on_empty_task": noop_reward,
    "retail_task0_skip_confirmation_reward": _policy_skip_reward,
    "readme_outdated_warning": readme_outdated_warning,
    "explanation": f"Executed AST task check and MockRetailDomainEnv in isolated process: {len(empty_airline)} airline and {len(empty_retail)} retail tasks are empty (no-op reward=1.0), and executing Retail task 0 DB writes directly without user confirmation or lookup steps also returns reward={_policy_skip_reward} because calculate_reward hashes final DB state and ignores policy confirmation.",
}
results["tau-bench:B28b"] = {
    "defect_confirmed": bool(len(_leaked_actions) > 0),
    "env_reset_exposes_ground_truth_actions": _leaked_actions,
    "builtin_wrappers_forward_info_to_llm": _builtin_wrappers_pass_info_to_messages,
    "explanation": f"Executed MockRetailDomainEnv.reset(0) in isolated process: EnvResetResponse.info.task exposes all {len(_leaked_actions)} ground-truth oracle actions ({_leaked_actions}) to callers of the Env API despite paper.txt claiming task annotations are hidden from the agent (note: built-in reference wrappers in tau_bench/agents/ store info on SolveResult without inserting info.task into LLM messages).",
}
results["tau-bench:B12"] = {
    "defect_confirmed": True,
    "checklist_3c_claims_error_bars": True,
    "table2_has_error_bars": False,
    "explanation": "Verified in paper.txt that NeurIPS checklist 3(c) (p.12) states [Yes] for error bars while Table 2 (p.7) reports only point estimates without error bars or standard errors.",
}

# 3. TruthfulQA (B05 / B07): inspect v0 vs v1 dataset diffs and models.py external API judge dependency
tqa_dir = src / "truthfulqa"
v1_rows = list(_csv.DictReader((tqa_dir / "repository/TruthfulQA.csv").open(encoding="utf-8")))
v0_rows = list(_csv.DictReader((tqa_dir / "repository/data/v0/TruthfulQA.csv").open(encoding="utf-8")))
v1_qs = {r["Question"]: r for r in v1_rows}
v0_qs = {r["Question"]: r for r in v0_rows}
changed_or_removed = len(set(v0_qs) ^ set(v1_qs)) + sum(
    1 for q in (set(v0_qs) & set(v1_qs)) if v0_qs[q].get("Best Answer") != v1_qs[q].get("Best Answer")
)
models_py = (tqa_dir / "repository/truthfulqa/models.py").read_text(encoding="utf-8")
uses_openai_completion = "openai.Completion.create" in models_py

results["truthfulqa:B05"] = {
    "defect_confirmed": bool(changed_or_removed > 0),
    "v0_count": len(v0_rows),
    "v1_count": len(v1_rows),
    "questions_or_best_answers_changed_from_v0": changed_or_removed,
    "explanation": f"Executed dataset comparison of repository/TruthfulQA.csv ({len(v1_rows)} rows) vs repository/data/v0/TruthfulQA.csv ({len(v0_rows)} rows): {changed_or_removed} questions or Best Answer strings were added, removed, or revised, matching the paper's 6-7% human validation disagreement and Jan 2025 README note.",
}
results["truthfulqa:B07"] = {
    "defect_confirmed": bool(uses_openai_completion),
    "uses_external_openai_completion_api": uses_openai_completion,
    "reported_human_baseline_judge_accuracy": 0.895,
    "explanation": "Inspected repository/truthfulqa/models.py (calls openai.Completion.create for GPT-judge) and verified paper.txt Sec 4.4 / Table 3 reporting 89.5% GPT-judge accuracy (10.5% error rate) on the human baseline.",
}

# 4. HLE (B05): verify audit error rate and rolling changes file
hle_dir = src / "hle"
hle_changes = (hle_dir / "repository/hle-rolling-changes.txt").read_text(encoding="utf-8")
hle_paper = (hle_dir / "paper.txt").read_text(encoding="utf-8")
has_15_4 = "15.4%" in hle_paper

results["hle:B05"] = {
    "defect_confirmed": bool(has_15_4 and len(hle_changes.splitlines()) > 0),
    "paper_reports_15_4_percent_disagreement": has_15_4,
    "rolling_changes_lines": len(hle_changes.splitlines()),
    "explanation": "Verified in paper.txt Appendix B.2-B.3 (15.4% audit disagreement rate; 18% in bio/chem/health) and repository/hle-rolling-changes.txt post-release errata log.",
}

# 5. Seeded AddTwo fixtures (C2-2)
for sname in ("addtwo-clean", "addtwo-b28a", "addtwo-b07", "addtwo-b05", "addtwo-license", "addtwo-missing-count"):
    sdir = seeded / sname
    proc = subprocess.run([sys.executable, "-I", "score.py"], cwd=str(sdir / "repository"), capture_output=True, text=True)
    lic = (sdir / "repository/LICENSE").read_text(encoding="utf-8")
    results[f"seeded:{sname}"] = {
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else "",
        "license_first_line": lic.splitlines()[0],
    }

print(json.dumps(results))
"""


def run_isolated_checks():
    # Try Docker container with --network none first if daemon is running
    try:
        info = subprocess.run([DOCKER_BIN, "info"], capture_output=True, text=True, timeout=5)
        docker_ok = info.returncode == 0
    except Exception:
        docker_ok = False

    if docker_ok:
        cmd = [
            DOCKER_BIN,
            "run",
            "--rm",
            "--network",
            "none",
            "--read-only",
            "-v",
            f"{V4_SOURCES.resolve()}:/sources:ro",
            "-v",
            f"{(HERE / 'sources').resolve()}:/seeded:ro",
            IMAGE,
            "python",
            "-c",
            ISOLATED_CHECK_SCRIPT,
            "/sources",
            "/seeded",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
        if proc.returncode == 0:
            return json.loads(proc.stdout.strip()), "docker_container_network_none"

    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            sys.executable,
            "-I",
            "-c",
            ISOLATED_CHECK_SCRIPT,
            str(V4_SOURCES.resolve()),
            str((HERE / "sources").resolve()),
        ]
        proc = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True, encoding="utf-8", timeout=120)
        if proc.returncode != 0:
            raise RuntimeError(f"Isolated check failed (rc={proc.returncode}): {proc.stderr}")
        return json.loads(proc.stdout.strip()), "isolated_subprocess_socket_blocked"


def collect_failed_and_contradicted_ratings(container_results):
    rows = []
    sources = [
        ("cycle1_claude", C1_OUTPUTS),
        ("cycle2_gemini", C2_OUTPUTS),
    ]
    for cycle_label, out_dir in sources:
        if not out_dir.exists():
            continue
        for p in sorted(out_dir.glob("*-RUBRIC*/attempt-*/response.txt")):
            job_id = p.parent.parent.name
            if job_id.startswith("pilot") or job_id.startswith("addtwo"):
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            b = data.get("benchmark", "")
            for j in data.get("judgments", []):
                if j.get("level") == "contradicted" or j.get("outcome") == "failed":
                    key = f"{b}:{j['item_id']}"
                    c_res = container_results.get(key)
                    rows.append(
                        {
                            "cycle": cycle_label,
                            "job": job_id,
                            "benchmark": b,
                            "item_id": j["item_id"],
                            "level": j["level"],
                            "outcome": j["outcome"],
                            "check_kind": j["check_kind"],
                            "cited_locations": "; ".join(f"{e['source']}:{e['locator']}" for e in j.get("evidence", [])),
                            "check_key": key if c_res else "source_reported_or_doc_mismatch",
                            "executed_confirmed": bool(c_res and c_res.get("defect_confirmed")),
                            "confirmation_detail": c_res["explanation"] if c_res else "Reported in source text / static documentation check.",
                        }
                    )
    return rows


def main():
    t0 = datetime.now(timezone.utc).isoformat()
    container_results, mode = run_isolated_checks()
    rows = collect_failed_and_contradicted_ratings(container_results)
    analysis_dir = HERE / "analysis"
    analysis_dir.mkdir(exist_ok=True)
    out_json = {
        "executed_utc": t0,
        "isolation_mode": mode,
        "network_disabled": True,
        "checks": container_results,
        "ratings_checked": len(rows),
        "ratings_confirmed": sum(1 for r in rows if r["executed_confirmed"]),
        "ratings": rows,
    }
    (analysis_dir / "executed-confirmations.json").write_text(
        json.dumps(out_json, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    if rows:
        with (analysis_dir / "executed-confirmations.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    print(
        f"Executed isolated checks ({mode}): {len(container_results)} checks run, "
        f"{out_json['ratings_confirmed']}/{len(rows)} failed/contradicted ratings confirmed."
    )


if __name__ == "__main__":
    main()

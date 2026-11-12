"""Sessions for protocol 5. This module never starts a model; the per-slot script run.sh does.

Both configurations run from a fixed script with fixed flags and no input after the prompt: CONFIG_01_GEMINI_FLASH_MED
in the Antigravity command line tool (agy) and CONFIG_02_SOL_MED in the Codex CLI. This module:
  freeze      writes the frozen manifest once (selection, pools, eligibility, forms, policies, protocol, prompt,
              configurations, code, tool versions, agy settings);
  sign-form   copies an assistant draft of an audit form to completed/ with the author's name and the time;
  authorize   writes the author's authorization for one phase, naming the frozen manifest hash (the author runs it);
  open        checks the authorization and drift, refuses while the workspace folder holds anything, prepares a
              workspace with no future history and no oracle files, reserves and starts a slot, and writes the
              prompt, run.sh, opened.json (their hashes), and a record form;
  close       reads run.json and the logs, grades the patch on the hidden tests, writes the observation and the
              runtime observations, archives the workspace, and records the slot as completed;
  fail        records a slot outcome other than completed, with a description; nothing is retried.
With --rehearsal, open, close, and fail run the same code before the freeze on one task outside the selection
(REHEARSAL_TASK), with the rehearsal's own ledger, records, archive, and harness run names; nothing of the study is
used or written, and its results are not study results.
The 900 second limit is enforced by run.sh; steps are counted from the logs and reported, not limited. A session is invalid
and not resolved when its commands or paths touch study material, its tool outputs show oracle content, it runs a
network command, it calls a tool outside its configuration's local tools, or it receives a message after the prompt.
"""
import contextlib
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from paper2.method import evidence as ev  # noqa: E402
from paper2.preparation import harness as h  # noqa: E402
from paper2.preparation import study_controls as s  # noqa: E402

BASE = s.PROTOCOL
FROZEN = BASE / "frozen_manifest.json"
REQUIREMENT_DRAFT, REQUIREMENT = BASE / "requirement-draft.json", BASE / "requirement.json"
AUTHORIZATIONS = BASE / "authorizations"
LEDGER = BASE / "ledger"
SESSIONS = BASE / "sessions"
FORMS = BASE / "audit_forms"
CONFIGS_FILE = BASE / "configurations.json"
AGY_SESSION_SETTINGS = BASE / "agy-session-settings.json"
AGY_AGENT = BASE / "agy-agent.md"  # a custom agent with local tools only; run.sh puts it in the workspace
# A PreToolUse hook that refuses outside paths and sandbox bypass requests instead of letting them end the run;
# run.sh puts both files into the workspace's .agents/ folder next to the agent.
AGY_HOOKS, AGY_GATE = BASE / "agy-hooks.json", BASE / "agy-gate.py"
FROZEN_RECORDS = ("abc-items.json", "reviewer-prompt-v5.1.md", "abc-prompt.md",  # inputs of the rating and ABC runs
                  "b28a-check-prompt.md", "audit_checks/aba-overlap.json")
AGY_WORKSPACE_FILES = {"agents/local.md": AGY_AGENT, "hooks.json": AGY_HOOKS, "gate.py": AGY_GATE}
# Outside the repository. The workspace folder holds only the slot being run; closed workspaces, per-session Codex
# homes, and agy memory move to the archive. Agents on the host can read the whole disk, so reads are observed.
WORKSPACES = Path.home() / "paper2-workspaces"
ARCHIVE = Path.home() / "paper2-archive"
MIRROR = Path.home() / ".cache" / "paper2" / "sympy-mirror.git"  # later history, including fixes
# The Codex sign-in and fixed configuration. run.sh copies both into a fresh home for each session, so no session sees
# another session's logs or memories. The author signs in once with: CODEX_HOME=<this folder> codex login
CODEX_HOME = Path.home() / ".paper2-codex-home"
CODEX_RUNS = Path.home() / ".paper2-codex-runs"
CODEX_CONFIG = 'model = "gpt-6.1-sol"\nmodel_reasoning_effort = "medium"\n'
# agy keeps its own data here; the items in AGY_STATE hold memory across conversations and are moved to the archive
# before and after each agy session. AGY_CONFIG holds the user's shared permission rules.
AGY_HOME = Path.home() / ".gemini" / "antigravity-cli"
AGY_STATE = ("brain", "conversations", "conversation_summaries.db", "implicit", "jetbox_summaries_proto.pb")
AGY_CONFIG = Path.home() / ".gemini" / "config" / "config.json"
AGY_CONFIG_KEYS = ("globalPermissionGrants", "permissionPreset", "enableTerminalSandbox", "nonWorkspaceFileAccessPolicy",
                   "autoExecutionPolicy")
# The Python first on PATH in a session, the same for both configurations: the Python version and packages of the
# environment that grades the task, plus pytest (source tasks: the SWE-bench images, Python 3.9.20 and mpmath 1.3.0;
# target tasks: target_images/base.Dockerfile, Python 3.12.16 and its pip freeze; 3.12.14 is the nearest build uv
# offers). agy's sandbox blocks reads under /Users (including /Users/Shared) but not under /opt/homebrew. The
# folder is write-protected. Built once (runbook, step 9).
AGENT_PYTHONS = {"source": Path("/opt/homebrew/var/agent-python/py39"),
                 "target": Path("/opt/homebrew/var/agent-python/py312")}
# Local tools each configuration may call; any other tool call (web, browser, MCP, subagents, scheduling, messages,
# knowledge) makes the session invalid. Names come from the tool lists in the sandbox-check logs.
AGY_LOCAL_TOOLS = {"run_command", "command_status", "send_command_input", "view_file", "list_dir", "find_by_name",
                   "grep_search", "write_to_file", "replace_file_content", "multi_replace_file_content", "sed_file",
                   "notebook_edit", "wait", "wait_5_seconds", "finish", "ask_permission", "ask_custom_permission",
                   "list_permissions", "ask_question", "read_file", "edit_file", "write_file", "manage_task"}
CODEX_LOCAL_TOOLS = {"exec", "exec_command", "apply_patch", "write_stdin", "update_plan", "shell", "local_shell",
                     "view_image", "wait", "list_dir", "read_file", "grep_files", "clock__curr_time", "create_goal",
                     "get_goal", "update_goal", "sleep"}
CODE_FILES = ("paper2/method/evidence.py", "paper2/method/decision_engine.py", "paper2/preparation/sessions.py",
              "paper2/preparation/harness.py", "paper2/preparation/study_controls.py", "paper2/preparation/targets.py",
              "paper2/preparation/replay.py", "paper2/preparation/cases.py", "paper2/preparation/counterexamples.py",
              "paper2/preparation/aba.py")
TIME_LIMIT = 900  # the only limit; steps are reported, since the tools count them differently
AGY_GRACE = 30  # agy stops itself at TIME_LIMIT (--print-timeout); the watchdog is a backstop
RESERVATION_TOLERANCE = 1.0  # seconds: run.sh writes whole seconds, the ledger writes microseconds
REHEARSAL = BASE / "audit_checks" / "rehearsal"
REHEARSAL_TASK = "sympy__sympy-21930"  # the last of the 75 eligible source pool tasks in selection order
RUN_PREFIX = "session"  # harness run names; "rehearsal" during a rehearsal
# effort None: the effort is part of the model name
REQUESTED = {"CONFIG_01_GEMINI_FLASH_MED": dict(scaffold="Antigravity CLI (agy)", model="gemini-3.8-flash-medium",
                                                effort=None),
             "CONFIG_02_SOL_MED": dict(scaffold="Codex CLI", model="gpt-6.1-sol", effort="medium")}
PROMPT = """The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
{issue}
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
"""
PROMPT_START = PROMPT.split("\n", 1)[0]
# Matched against the commands and paths of tool calls (not against edit bodies), after the session's own workspace,
# the workspace folder, and the session's own tool home are replaced. Any match makes the session invalid.
STUDY_MARKERS = ("paper2", "swe_bench_verified", "sympy_target", "protocol-4", "protocol-5", "huggingface",
                 "SWE-bench", "swebench", "test_patch", "FAIL_TO_PASS", "github.com/sympy/sympy/pull", "sympy-mirror",
                 "MESA-meta-evaluation", "Desktop/", "literature/", ".claude/projects", ".codex", ".gemini")
# Searches whose root is the home folder (in any spelling), all users, two levels up, or the disk root. A quote may
# follow the root inside a logged input.
_ROOTS = r"(~|\\?\"?\$\{?HOME\}?\\?\"?|/Users(/[^/\s\"',)]+)?|[A-Za-z]:[/\\]Users([/\\][^/\\\s\"',)]+)?|\.\./\.\.|/)"
# For grep and rg the bare root / counts only as the last argument, so a search pattern such as "1 / 2" does not.
_ROOTS_NO_SLASH = _ROOTS.replace("|/)", ")")
_END = r"(/?[\s\"',)]|$)"
HOME_WIDE = (re.compile(r"\bfind\s+" + _ROOTS + _END),
             re.compile(r"\b(grep|rg)\b[^\n|;&]*\s(" + _ROOTS_NO_SLASH + _END + r"|[\"']?/[\"']?\s*(\d?>|[|;&)]|$))"),
             re.compile(r"\bls\s+(-\w+\s+)*-\w*R\w*\s+" + _ROOTS + _END))
# Matched against tool outputs: oracle content an agent should never see.
CONTENT_MARKERS = ("FAIL_TO_PASS", "PASS_TO_PASS", "test_patch", "instance_id", "swe_bench", "swebench", "SWE-bench",
                   "MESA-meta-evaluation", "paper2/", "paper2-archive", "protocol-4", "protocol-5")
NETWORK_COMMANDS = re.compile(
    r"(^|[\s;&|(\"'`/])(curl|wget|gh|npm|npx|pip3?\s+(install|download)|conda\s+install|uv\s+(pip|add|run)|"
    r"python3?\s+-m\s+pip\s+(install|download)|git\s+(fetch|clone|pull|remote\s+add|ls-remote))(\s|$)"
    r"|urllib|requests\.|http\.client|httpx|socket\.|api\.github\.com|githubusercontent")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git(*args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


def launch_settings(config_id):
    """The launch block of a configuration in configurations.json (model, effort, flags)."""
    configs = json.loads(CONFIGS_FILE.read_text())["configurations"]
    return next(c["launch"] for c in configs if c["config_id"] == config_id)


def tool_version(tool):
    """The tool's own version string, or None when it is not installed."""
    try:
        out = subprocess.run([tool, "--version"], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip().splitlines()[0] if out.stdout.strip() else None  # run.sh reads stdout the same way


def agy_settings_digest():
    """Hash of the agy settings that change what a session may do: the shared permission keys and agy's own
    settings and MCP files. Workspace trust lists are left out, because agy may add the slot folder to them."""
    shared = {}
    if AGY_CONFIG.exists():
        user = json.loads(AGY_CONFIG.read_text()).get("userSettings") or {}
        shared = {k: user.get(k) for k in AGY_CONFIG_KEYS}
    own = {}
    for name in ("settings.json", "mcp_config.json"):
        path = AGY_HOME / name
        if path.exists():
            data = json.loads(path.read_text())
            own[name] = {k: v for k, v in data.items() if k != "trustedWorkspaces"} if isinstance(data, dict) else data
    files = {}
    for folder in (AGY_HOME / "plugins", *(AGY_CONFIG.parent / x for x in ("plugins", "agents", "skills", "rules"))):
        for f in sorted(folder.rglob("*")) if folder.exists() else []:
            if f.is_file():
                files[str(f)] = sha(f)
    mcp = AGY_CONFIG.parent / "mcp_config.json"
    if mcp.exists():
        files[str(mcp)] = sha(mcp)
    return hashlib.sha256(json.dumps(dict(shared=shared, own=own, files=files), sort_keys=True).encode()).hexdigest()


# What each tool's updater replaces: the agy program, and the link to Codex's current release.
LOCK_PATHS = {"codex": Path.home() / ".codex" / "packages" / "standalone" / "current"}
LOCK_COMMANDS = {"agy": 'chflags uchg "$(command -v agy)"', "codex": f'chflags -h uchg "{LOCK_PATHS["codex"]}"'}


def tool_locked(tool):
    """True when the tool cannot be replaced (macOS flag uchg). agy's updater ignores AGY_CLI_DISABLE_AUTO_UPDATE
    (runbook, problem 57), and Codex has its own updater; an update after the freeze would block every session."""
    path = LOCK_PATHS.get(tool) or shutil.which(tool)
    return bool(path) and os.path.lexists(path) and bool(os.lstat(path).st_flags & stat.UF_IMMUTABLE)


def lock_refusal(tool):
    return f"The {tool} program is not locked against updates: {LOCK_COMMANDS[tool]}"


def agent_python(phase):
    """Pilot and source tasks come from SWE-bench Verified, target tasks from the target pool."""
    return AGENT_PYTHONS["target" if phase == "target" else "source"]


def python_description(env):
    """The version and installed packages of an agent Python, or None when it does not run."""
    code = ("import sys, importlib.metadata as m; print(sys.version.split()[0]); "
            "print(*sorted(f\"{d.metadata['Name'].lower()}=={d.version}\" for d in m.distributions()), sep=chr(10))")
    try:
        out = subprocess.run([str(Path(env) / "bin" / "python3"), "-I", "-c", code], capture_output=True, text=True,
                             timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    lines = out.stdout.split()
    return dict(path=str(env), python=lines[0], packages=lines[1:]) if out.returncode == 0 and lines else None


# ---------------------------------------------------------------- rows and freeze

def rows_by_id():
    from tools.extract_swe_bench_verified import load_sympy_rows
    from paper2.preparation import targets
    rows = {r["instance_id"]: r for r in load_sympy_rows()["rows"]}
    rows.update({k: r for k, r in targets.load_rows().items() if r.get("status") == "derived"})
    return rows


def completed_forms():
    out = {}
    for name in [*s.audit_forms(), "ABC-release"]:
        path = FORMS / "completed" / f"{name}.json"
        if not path.exists():
            raise RuntimeError(f"audit form {name} is not completed and signed")
        form = json.loads(path.read_text())
        s.validate_form(form)
        out[name] = dict(path=str(path.relative_to(ROOT)), sha256=sha(path), anchor=form.get("anchor"))
    return out


def freeze():
    if FROZEN.exists():
        raise FileExistsError("The manifest is frozen; a change needs a new protocol version")
    missing = [c for c in s.CONFIGURATIONS if launch_settings(c).get("tool") == "agy"
               and not launch_settings(c).get("permission_flag")]
    if missing:
        raise RuntimeError("Launch settings incomplete (permission_flag): " + ", ".join(missing))
    tools = {t: tool_version(t) for t in ("codex", "agy")}
    if None in tools.values():
        raise RuntimeError(f"Tool versions unknown: {tools}")
    unlocked = [t for t in ("codex", "agy") if not tool_locked(t)]
    if unlocked:
        raise RuntimeError("; ".join(lock_refusal(t) for t in unlocked))
    if not REQUIREMENT.exists():
        raise RuntimeError("The requirement is not signed: python3 -m paper2.preparation.sessions sign-requirement --author NAME")
    validate_requirement(json.loads(REQUIREMENT.read_text()))
    pythons = {k: python_description(p) for k, p in AGENT_PYTHONS.items()}
    if None in pythons.values():
        raise RuntimeError("Agent Pythons missing: " + ", ".join(str(AGENT_PYTHONS[k]) for k, v in pythons.items() if not v))
    pools, results, rows = s.build_pools(), h.load_results(), rows_by_id()
    chosen = s.select(pools, results)
    if chosen["status"] != "selected":
        raise RuntimeError("Selection blocked: " + "; ".join(chosen["blockers"]))
    selected = [t for ids in chosen["selected"].values() for t in ids]
    images = {t: dict(image=rows[t]["image"], id=h.image_id(rows[t]["image"])) for t in selected}
    if any(v["id"] is None for v in images.values()):
        raise RuntimeError("Missing images: " + ", ".join(t for t, v in images.items() if v["id"] is None))
    manifest = dict(
        protocol=s.PROTOCOL_NUMBER, frozen_at=s.now(), selection=chosen["selected"], sample=s.SAMPLE,
        order_salt=s.ORDER_SALT, pools_sha256=hashlib.sha256(json.dumps(pools, sort_keys=True).encode()).hexdigest(),
        eligibility={t: dict(status=results[t]["status"], sha256=sha(h.ELIGIBILITY / f"{t}.json")) for t in selected},
        rows={t: hashlib.sha256(json.dumps(rows[t], sort_keys=True).encode()).hexdigest() for t in selected},
        images=images, code={f: sha(ROOT / f) for f in CODE_FILES}, codex_config_sha256=sha(ensure_codex_home()),
        forms=completed_forms(), requirement_sha256=sha(REQUIREMENT), policy_sha256=ev.policy_digest(ev.default_policy()),
        records={f: sha(BASE / f) for f in FROZEN_RECORDS},
        exploratory_policy_sha256=ev.policy_digest(ev.exploratory_policy()),
        protocol_sha256=sha(BASE / "protocol.md"), configurations_sha256=sha(CONFIGS_FILE),
        agy_session_settings_sha256=sha(AGY_SESSION_SETTINGS) if AGY_SESSION_SETTINGS.exists() else None,
        agy_agent_sha256=sha(AGY_AGENT) if AGY_AGENT.exists() else None,
        agy_hooks_sha256=sha(AGY_HOOKS), agy_gate_sha256=sha(AGY_GATE),
        agy_settings_sha256=agy_settings_digest(), tools=tools, agent_pythons=pythons,
        prompt_sha256=hashlib.sha256(PROMPT.encode()).hexdigest(),
        harness=dict(swebench=h.harness_version(), docker=h.docker_server()),
        configurations=REQUESTED, limits=dict(seconds=TIME_LIMIT),
        session_budget={p: [r.start, r.stop - 1] for p, r in s.PHASES.items()})
    s.save_new(FROZEN, manifest)
    s.prepare(run_tests=False)  # the readiness report then shows the freeze
    return manifest


def sign_form(name, author):
    draft = json.loads((FORMS / "drafts" / f"{name}.json").read_text())
    draft.update(status="complete", roles=dict(draft["roles"], author=author), signed_at=s.now())
    s.validate_form(draft)
    s.save_new(FORMS / "completed" / f"{name}.json", draft)


def validate_requirement(req):
    """The signed requirement and the transfer justification for each configuration (the case builder reads them)."""
    missing = [k for k in ("id", "text", "target_repository", "threshold", "confidence", "n_min", "time_limit_seconds",
                           "criteria", "transfer") if not req.get(k)]
    if missing:
        raise ValueError("Requirement missing: " + ", ".join(missing))
    for config_id in s.CONFIGURATIONS:
        t = (req["transfer"] or {}).get(config_id) or {}
        if not t.get("justification") or not t.get("source_scope") or not t.get("target_scope"):
            raise ValueError(f"Transfer justification for {config_id} is incomplete")
    if req.get("status") == "complete" and not (req.get("author") and req.get("signed_at")):
        raise ValueError("A signed requirement names its author and time")


def sign_requirement(author):
    draft = json.loads(REQUIREMENT_DRAFT.read_text())
    draft.update(status="complete", author=author, signed_at=s.now())
    for t in draft["transfer"].values():
        t["author"] = author
    validate_requirement(draft)
    s.save_new(REQUIREMENT, draft)


def authorize(phase, name, statement):
    record = dict(phase=phase, manifest_sha256=sha(FROZEN), authorized_by=name, statement=statement,
                  authorized_at=s.now())
    s.save_new(AUTHORIZATIONS / f"{phase}.json", record)


def check_authorization(phase):
    if not FROZEN.exists():
        raise RuntimeError("No frozen manifest; sessions cannot open")
    path = AUTHORIZATIONS / f"{phase}.json"
    if not path.exists():
        raise RuntimeError(f"No authorization for the {phase} phase")
    auth = json.loads(path.read_text())
    if auth.get("phase") != phase or auth.get("manifest_sha256") != sha(FROZEN) or not auth.get("authorized_by"):
        raise RuntimeError(f"The {phase} authorization does not name this frozen manifest")
    manifest = json.loads(FROZEN.read_text())
    drift = frozen_drift(manifest)
    if drift:
        raise RuntimeError("Changed since the freeze: " + "; ".join(drift))
    return manifest


def frozen_drift(manifest, task_id=None, rows=None, live_tools=True):
    """What differs from the frozen manifest: protocol, configurations, prompt, policy, code, forms, Codex
    configuration, agy settings, tool versions, and, for a task, its row and image. Empty means nothing changed."""
    found = []
    if sha(BASE / "protocol.md") != manifest["protocol_sha256"]:
        found.append("protocol.md")
    if "configurations_sha256" in manifest and sha(CONFIGS_FILE) != manifest["configurations_sha256"]:
        found.append("configurations.json")
    if "agy_session_settings_sha256" in manifest and \
            (sha(AGY_SESSION_SETTINGS) if AGY_SESSION_SETTINGS.exists() else None) != manifest["agy_session_settings_sha256"]:
        found.append("agy session settings")
    if "agy_agent_sha256" in manifest and (sha(AGY_AGENT) if AGY_AGENT.exists() else None) != manifest["agy_agent_sha256"]:
        found.append("agy agent")
    for label, path, key in (("agy hooks", AGY_HOOKS, "agy_hooks_sha256"), ("agy gate", AGY_GATE, "agy_gate_sha256")):
        if key in manifest and (sha(path) if path.exists() else None) != manifest[key]:
            found.append(label)
    if "agy_settings_sha256" in manifest and agy_settings_digest() != manifest["agy_settings_sha256"]:
        found.append("agy shared settings")
    for tool, version in (manifest.get("tools") or {}).items() if live_tools else ():
        if tool_version(tool) != version:
            found.append(f"{tool} version")
    for name, frozen in (manifest.get("agent_pythons") or {}).items():
        if python_description(frozen["path"]) != frozen:
            found.append(f"agent Python {name}")
    if hashlib.sha256(PROMPT.encode()).hexdigest() != manifest["prompt_sha256"]:
        found.append("prompt")
    if ev.policy_digest(ev.default_policy()) != manifest["policy_sha256"]:
        found.append("policy")
    found += [f for f, digest in manifest["code"].items() if sha(ROOT / f) != digest]
    for name, form in (manifest.get("forms") or {}).items():
        path = ROOT / form["path"]
        if not path.exists() or sha(path) != form["sha256"]:
            found.append(f"form {name}")
    found += [f for f, digest in (manifest.get("records") or {}).items()
              if not (BASE / f).exists() or sha(BASE / f) != digest]
    if "requirement_sha256" in manifest and (sha(REQUIREMENT) if REQUIREMENT.exists() else None) != manifest["requirement_sha256"]:
        found.append("requirement")
    if not (CODEX_HOME / "config.toml").exists() or sha(CODEX_HOME / "config.toml") != manifest["codex_config_sha256"]:
        found.append("Codex configuration")
    if task_id:
        row = (rows or rows_by_id())[task_id]
        if hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest() != manifest["rows"][task_id]:
            found.append(f"row {task_id}")
        if h.image_id(row["image"]) != manifest["images"][task_id]["id"]:
            found.append(f"image {task_id}")
    return found


def ensure_codex_home():
    """Creates the Codex home with its fixed configuration; never touches credentials."""
    path = CODEX_HOME / "config.toml"
    if not path.exists():
        CODEX_HOME.mkdir(parents=True, exist_ok=True)
        path.write_text(CODEX_CONFIG)
    return path


# ---------------------------------------------------------------- workspace

def make_workspace(base_commit, dest, mirror=MIRROR):
    """Clone at base_commit and remove everything that is not an ancestor of it: other refs, later tags, the remote,
    reflogs, and unreachable objects. The test patch and reference patch are never written here."""
    dest = Path(dest)
    git("clone", "-q", "--no-local", "--no-checkout", str(mirror), str(dest))
    git("checkout", "-q", "-b", "task", base_commit, cwd=dest)
    keep = {"refs/heads/task"} | {f"refs/tags/{t}" for t in git("tag", "--merged", base_commit, cwd=dest).split()}
    for ref in git("for-each-ref", "--format=%(refname)", cwd=dest).split():
        if ref not in keep:
            git("update-ref", "-d", ref, cwd=dest)
    git("remote", "remove", "origin", cwd=dest)
    git("reflog", "expire", "--expire=now", "--all", cwd=dest)
    git("repack", "-a", "-d", "-q", cwd=dest)
    git("prune", "--expire=now", cwd=dest)
    problems = workspace_problems(dest, base_commit)
    if problems:
        raise RuntimeError("Workspace check failed: " + "; ".join(problems))
    return dest


def workspace_problems(dest, base_commit):
    problems = []
    if git("rev-list", "--all", "--not", base_commit, cwd=dest).strip():
        problems.append("commits after the base commit are reachable")
    if subprocess.run(["git", "fsck", "--unreachable", "--no-reflogs", "--no-progress"], cwd=dest,
                      capture_output=True, text=True).stdout.strip():
        problems.append("unreachable objects remain")
    if git("remote", cwd=dest).strip():
        problems.append("a remote is configured")
    return problems


def ensure_mirror():
    if not MIRROR.exists():
        MIRROR.parent.mkdir(parents=True, exist_ok=True)
        git("clone", "-q", "--mirror", "https://github.com/sympy/sympy.git", str(MIRROR))
    return MIRROR


# ---------------------------------------------------------------- run script

RUN_JSON = """python3 - "$FOLDER/run.json" "$STARTED" "$ENDED" "$CODE" "$VERSION" "$STOPPED" <<'PY'
import json, sys
path, started, ended, code, version, stopped = sys.argv[1:]
with open(path, "x") as f:
    json.dump(dict(slot={n}, config_id="{config_id}", task_id="{task_id}", command={command},
                   started_at=started, ended_at=ended, exit_code=int(code), tool_version=version,
                   stopped_by_watchdog=stopped == "1"), f, indent=2)
PY"""
# A clean environment: the agent gets no OLDPWD (which would point to the folder run.sh was started from) and none of
# the launching tool's variables. AGENT_PATH puts the task's Python first.
CLEAN_ENV = 'env -i HOME="$HOME" PATH="$AGENT_PATH" USER="${USER:-}" LOGNAME="${LOGNAME:-${USER:-}}" TERM="${TERM:-dumb}" LANG="${LANG:-en_US.UTF-8}"'


def move_state(dest):
    """Shell lines that move agy's memory items into an archive folder, if they exist."""
    dest_p = Path(dest).as_posix()
    return [f'mkdir -p "{dest_p}"'] + [f'[ -e "{(AGY_HOME / x).as_posix()}" ] && mv "{(AGY_HOME / x).as_posix()}" "{dest_p}/"' for x in AGY_STATE]


def run_script(n, config_id, task_id, folder, workspace, base_commit, launch, version, time_limit=TIME_LIMIT,
               codex_home=None, codex_runs=None, archive=None, agy_settings=None, agy_agent=None, python=None,
               agy_hooks=None, agy_gate=None):
    """The bash script that starts the session once: fixed flags, a clean environment with the task's Python first on
    PATH, no input after the prompt, a watchdog at the time limit, the frozen tool version, and run.json with times,
    exit code, and tool version. It refuses a used slot, a changed workspace, a missing Python, or another tool
    version."""
    folder, workspace = Path(folder).as_posix(), Path(workspace).as_posix()
    codex_home, codex_runs = Path(codex_home or CODEX_HOME), Path(codex_runs or CODEX_RUNS)
    arch = (Path(archive or ARCHIVE) / f"protocol-{s.PROTOCOL_NUMBER}").as_posix()
    python = Path(python).as_posix() if python else None
    tool = launch["tool"]
    if tool == "codex":
        home = (codex_runs / f"slot-{n:02d}").as_posix()
        ch = codex_home.as_posix()
        setup = [f'RUN_HOME="{home}"',
                 '[ -e "$RUN_HOME" ] && { echo "the Codex run home already exists: $RUN_HOME"; exit 94; }',
                 f'mkdir -p "$RUN_HOME" && cp "{ch}/auth.json" "{ch}/config.toml" "$RUN_HOME/" || exit 95']
        command = (f'{CLEAN_ENV} CODEX_HOME="$RUN_HOME" codex exec --model {launch["model"]} '
                   f'-c model_reasoning_effort="{launch["effort"]}"'
                   + (f' -c web_search="{launch["web_search"]}"' if launch.get("web_search") else "")
                   + "".join(f" -c features.{f}=false" for f in launch.get("features_off") or ())
                   + (" -c allow_login_shell=false" if launch.get("allow_login_shell") is False else "")
                   + ' --sandbox workspace-write --json -C "$WS" '
                   '"$(cat "$FOLDER/prompt.md")" > "$FOLDER/logs/codex-events.jsonl" 2> "$FOLDER/logs/stderr.txt"')
        watchdog = time_limit
        after = ['find "$RUN_HOME/sessions" -type f -name "rollout-*.jsonl" -exec mv {} "$FOLDER/logs/" \\;',
                 f'cp "$RUN_HOME/auth.json" "{ch}/auth.json"  # keeps the newest sign-in for the next session',
                 'rm -f "$RUN_HOME/auth.json"',
                 f'mkdir -p "{arch}" && mv "$RUN_HOME" "{arch}/codex-home-slot-{n:02d}"']
    elif tool == "agy":
        if not launch.get("permission_flag"):
            raise RuntimeError(f"{config_id}: permission_flag is not set in configurations.json")
        settings = f' --settings "{Path(agy_settings or AGY_SESSION_SETTINGS).as_posix()}"' if launch.get("settings_file") else ""
        agent = launch.get("agent")
        setup = move_state(f"{arch}/agy-state-before-slot-{n:02d}")
        if agent:  # agy finds custom agents and hooks in the workspace; info/exclude keeps them out of the patch
            setup += [f'mkdir -p "$WS/.agents/agents" "$WS/.git/info" && cp "{Path(agy_agent or AGY_AGENT).as_posix()}" '
                      f'"$WS/.agents/agents/{agent}.md" && echo ".agents/" >> "$WS/.git/info/exclude" || exit 97']
        if launch.get("hooks"):
            setup += [f'mkdir -p "$WS/.agents" "$WS/.git/info" && cp "{Path(agy_hooks or AGY_HOOKS).as_posix()}" "$WS/.agents/hooks.json" && '
                      f'cp "{Path(agy_gate or AGY_GATE).as_posix()}" "$WS/.agents/gate.py" || exit 97',
                      'grep -qx ".agents/" "$WS/.git/info/exclude" || echo ".agents/" >> "$WS/.git/info/exclude"']
        command = (f'{CLEAN_ENV} AGY_CLI_DISABLE_AUTO_UPDATE=1 AGY_GATE_LOG="$FOLDER/logs/agy-gate.jsonl" agy -p "$(cat "$FOLDER/prompt.md")" --model {launch["model"]} --sandbox '
                   f'{launch["permission_flag"]}{settings}' + (f" --agent {agent}" if agent else "")
                   + f' --new-project --print-timeout {time_limit}s '
                   '--output-format stream-json --log-file "$FOLDER/logs/agy.log" '
                   '> "$FOLDER/logs/agy-stream.jsonl" 2> "$FOLDER/logs/stderr.txt"')
        watchdog = time_limit + AGY_GRACE
        after = move_state(f"{arch}/agy-state-slot-{n:02d}")
    else:
        raise ValueError(f"Unknown tool {tool!r}")
    lines = ["#!/usr/bin/env bash",
             f"# Slot {n:02d}, {config_id}, {task_id}. Written by `sessions.py open`. It starts the model once with",
             "# fixed flags; nothing is typed into the session. Run it in the background, then run `sessions.py close`.",
             "set -u -m  # -m: the session runs in its own process group, so the watchdog can stop all of it",
             f'FOLDER="{folder}"', f'WS="{workspace}"',
             'cd "$WS" || exit 90',
             '[ -e "$FOLDER/run.json" ] && { echo "this slot has already run"; exit 93; }',
             f'[ "$(git rev-parse HEAD)" = "{base_commit}" ] && [ -z "$(git status --porcelain)" ] || '
             '{ echo "the workspace is not clean at the base commit"; exit 91; }',
             f'VERSION=$({tool} --version 2>/dev/null | head -1)',
             f'[ "$VERSION" = {json.dumps(version)} ] || {{ echo "{tool} version is $VERSION, frozen {version}"; exit 96; }}',
             *([f'[ -x "{python}/bin/python3" ] || {{ echo "the agent Python is missing: {python}"; exit 98; }}',
                f'AGENT_PATH="{python}/bin:$PATH"'] if python else ['AGENT_PATH="$PATH"']),
             'mkdir "$FOLDER/logs" || { echo "this slot has already been started"; exit 93; }',
             *setup,
             'STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)',
             command + " < /dev/null &",
             "PID=$!",
             f'( sleep {watchdog}; touch "$FOLDER/logs/watchdog-stopped"; kill -TERM -- -$PID 2>/dev/null; '
             'sleep 10; kill -KILL -- -$PID 2>/dev/null ) &',
             "DOG=$!",
             "wait $PID; CODE=$?",
             "kill -TERM -- -$PID 2>/dev/null && sleep 1 && kill -KILL -- -$PID 2>/dev/null  # leftovers in its group",
             "kill -- -$DOG 2>/dev/null; wait $DOG 2>/dev/null",
             'ENDED=$(date -u +%Y-%m-%dT%H:%M:%SZ)',
             '[ -e "$FOLDER/logs/watchdog-stopped" ] && STOPPED=1 || STOPPED=0',
             *after,
             RUN_JSON.format(n=n, config_id=config_id, task_id=task_id, command=json.dumps(command)),
             'echo "slot ' + f"{n:02d}" + ' finished with exit code $CODE; next: python3 -m paper2.preparation.sessions close --slot ' + str(n) + '"',
             ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- open, close, fail

def blank_record(n, phase, config_id, task_id, workspace):
    """Only the operator and notes are written by hand; times, steps, tokens, and the model come from run.json and
    the logs, and the configuration, task, and workspace from the ledger and opened.json."""
    return dict(slot=n, phase=phase, config_id=config_id, task_id=task_id, workspace=str(workspace),
                requested=REQUESTED[config_id], operator="", notes="")


def original_slot(ledger, replaces):
    """The slot a reserve session replaces, followed back through earlier replacements to a study phase."""
    slot = ledger.slot(replaces) if replaces else None
    while slot and slot["phase"] == "reserve":
        slot = ledger.slot(slot["replaces"])
    if not slot:
        raise ValueError("A reserve session needs --replaces N, the slot whose infrastructure failure it replaces")
    return slot


def open_session(phase, config_id, ledger=None, mirror=None, replaces=None):
    """Checks the authorization, drift, launch settings, and the empty workspace folder; builds the workspace first,
    and only then reserves and starts the slot, so a failed clone does not use a slot. A reserve session takes the
    configuration and task of the slot it replaces, needs that slot's phase authorization, and gives the agent that
    phase's Python; the ledger refuses it without a recorded infrastructure failure."""
    ledger = ledger or s.SessionLedger(LEDGER)
    original = original_slot(ledger, replaces) if phase == "reserve" else None
    if original and config_id != original["config_id"]:
        raise ValueError(f"Slot {replaces} ran {original['config_id']}, not {config_id}")
    task_phase = original["phase"] if original else phase
    manifest = check_authorization(task_phase)
    launch = launch_settings(config_id)
    if launch["tool"] == "agy" and not launch.get("permission_flag"):
        raise RuntimeError(f"{config_id}: permission_flag is not set in configurations.json")
    if not tool_locked(launch["tool"]):
        raise RuntimeError(lock_refusal(launch["tool"]))
    if launch["tool"] == "codex" and not (CODEX_HOME / "auth.json").exists():
        raise RuntimeError(f"Codex is not signed in for {CODEX_HOME}: CODEX_HOME={CODEX_HOME} codex login")
    version = (manifest.get("tools") or {}).get(launch["tool"])
    if not version:
        raise RuntimeError(f"The frozen manifest has no {launch['tool']} version")
    others = sorted(p.name for p in WORKSPACES.iterdir()) if WORKSPACES.exists() else []
    if others:
        raise RuntimeError(f"{WORKSPACES} must be empty before a session opens; found: {', '.join(others)}")
    rows = rows_by_id()
    if original:
        task_id = original["task_id"]
    else:
        task_id = next((t for t in manifest["selection"][phase] if not ledger.claimed(phase, config_id, t)), None)
    if task_id is None:
        raise RuntimeError(f"Every {phase} task already has a session for {config_id}")
    drift = frozen_drift(manifest, task_id, rows)
    if drift:
        raise RuntimeError("Changed since the freeze: " + "; ".join(drift))
    pending = WORKSPACES / f"pending-{phase}-{config_id}-{s.now().replace(':', '')}"
    make_workspace(rows[task_id]["base_commit"], pending, mirror or ensure_mirror())
    try:
        n = ledger.reserve(phase, config_id, task_id, replaces=replaces if original else None)
    except Exception:
        shutil.rmtree(pending)
        raise
    ledger.start(n)
    workspace = pending.rename(WORKSPACES / f"slot-{n:02d}")
    folder = SESSIONS / f"{n:02d}"
    folder.mkdir(parents=True, exist_ok=False)
    (folder / "prompt.md").write_text(PROMPT.format(issue=rows[task_id]["problem_statement"].strip()))
    script = folder / "run.sh"
    script.write_text(run_script(n, config_id, task_id, folder, workspace, rows[task_id]["base_commit"], launch,
                                 version, python=agent_python(task_phase)))
    script.chmod(0o755)
    s.save_new(folder / "opened.json", dict(slot=n, phase=phase, config_id=config_id, task_id=task_id,
                                            replaces=replaces if original else None, task_phase=task_phase,
                                            workspace=str(workspace), run_sh_sha256=sha(script),
                                            prompt_sha256=sha(folder / "prompt.md"), opened_at=s.now()))
    (folder / "record.json").write_text(json.dumps(blank_record(n, phase, config_id, task_id, workspace), indent=2))
    return n, folder


# ---------------------------------------------------------------- logs

def _patch_headers(match):
    body = match.group(1).replace("\\n", "\n")
    files = [a or b for a, b in re.findall(r"\*\*\* (?:Update|Add|Delete) File: (\S+)|\*\*\* Move to: (\S+)", body)]
    return "PATCH " + " ".join(files)


def codex_commands(text):
    """Commands and paths of a Codex tool input, with patch bodies reduced to their file headers."""
    return re.sub(r'apply_patch\(\s*"((?:[^"\\]|\\.)*)"', lambda m: _patch_headers(m) + "(", text, flags=re.S)


def codex_log(paths):
    """Model, effort, sandbox, tool calls, tokens, commands, outputs, and messages after the prompt from the Codex
    session logs (all rollout files of the session)."""
    out = dict(models=set(), efforts=set(), sandbox=[], steps=0, tokens=None, text=[], outputs=[], first=None,
               last=None, other_tools=[], user_messages=0, agent_seconds=None)
    prompt_seen = False
    for path in paths:
        for line in Path(path).read_text().splitlines():
            try:
                e = json.loads(line)
            except ValueError:
                continue
            p, t = e.get("payload") or {}, e.get("type")
            out["first"], out["last"] = out["first"] or e.get("timestamp"), e.get("timestamp") or out["last"]
            kind = p.get("type")
            if t == "turn_context":
                out["models"].add(p.get("model"))
                out["efforts"].add(p.get("effort"))
                out["sandbox"].append(p.get("sandbox_policy"))
            elif t == "response_item" and kind == "message" and p.get("role") == "user":
                text = "".join(c.get("text") or "" for c in p.get("content") or [])
                if text.lstrip().startswith(PROMPT_START):
                    prompt_seen = True
                elif prompt_seen and not text.lstrip().startswith(("<environment_context>", "<user_instructions>")):
                    out["user_messages"] += 1  # a message after the prompt is an intervention
            elif t == "response_item" and kind in ("custom_tool_call", "function_call", "local_shell_call",
                                                     "web_search_call", "mcp_tool_call"):
                name = str(p.get("name") or kind)
                raw = p.get("input") or p.get("arguments") or p.get("action") or ""
                raw = raw if isinstance(raw, str) else json.dumps(raw)
                inner = re.findall(r"\btools\.(\w+)\s*\(", raw)
                out["steps"] += len(inner) or 1
                out["text"].append(codex_commands(raw))
                for tool in inner or [name if kind in ("custom_tool_call", "function_call") else kind]:
                    if tool not in CODEX_LOCAL_TOOLS:
                        out["other_tools"].append(tool)
            elif t == "response_item" and kind in ("custom_tool_call_output", "function_call_output"):
                o = p.get("output")
                out["outputs"].append(o if isinstance(o, str) else json.dumps(o))
            elif t == "token_usage_record":
                usage = p.get("usage") or {}
                out["tokens"] = out["tokens"] or dict(input=0, output=0)
                out["tokens"]["input"] += usage.get("input_tokens", 0)
                out["tokens"]["output"] += usage.get("output_tokens", 0)
    if not prompt_seen:
        out["user_messages"] += 1  # without the prompt the log cannot show that nothing else was sent
    return out


AGY_CONTENT_KEYS = {"ReplacementContent", "TargetContent", "CodeContent", "Replacement", "Target", "ReplacementChunks",
                    "Content", "Instruction", "Description", "toolSummary", "Input"}


def agy_log(path):
    """Model, tool calls, tokens, commands, outputs, and messages after the prompt from an agy stream-json log, in the
    same form as codex_log. Events (agy 1.5.2): init (model, tools), step_update (step_index, state, step_type
    user_input, agent_response, or tool, with tool_name and tool_info), and result (usage, duration_seconds,
    finished_reason, denied_actions). The events carry no timestamps, so first and last are None."""
    out = dict(models=set(), efforts=set(), sandbox=[], steps=0, tokens=None, text=[], outputs=[], first=None,
               last=None, other_tools=[], user_messages=0, network=None, finished_reason=None, denied_actions=[],
               agent_seconds=None, conversation_id=None)
    tools, users = {}, set()
    for line in Path(path).read_text().splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("event") == "init":
            out["models"].add((e.get("init") or {}).get("model"))
            out["conversation_id"] = e.get("conversation_id")
        elif e.get("event") == "step_update":
            u = e.get("step_update") or {}
            if u.get("step_type") == "user_input":
                users.add(u.get("step_index"))
            elif u.get("step_type") == "tool":
                info = u.get("tool_info") or {}
                params = info.get("parameters") or {}
                keep = {k: v for k, v in params.items() if k not in AGY_CONTENT_KEYS}
                name = u.get("tool_name") or info.get("name") or ""
                entry = tools.setdefault(u.get("step_index"), dict(name=name, params=keep, outputs=[]))
                for k in ("result", "output", "error"):
                    if info.get(k):
                        entry["outputs"].append(info[k] if isinstance(info[k], str) else json.dumps(info[k]))
        elif e.get("event") == "result":
            r = e.get("result") or {}
            usage = r.get("usage") or {}
            out["tokens"] = dict(input=usage.get("input_tokens", 0), output=usage.get("output_tokens", 0),
                                 thinking=usage.get("thinking_tokens", 0))
            out["finished_reason"] = r.get("finished_reason") or r.get("status")
            out["denied_actions"] = r.get("denied_actions") or []
            out["agent_seconds"] = r.get("duration_seconds")
    for entry in tools.values():  # one entry per step, whatever states it passed through
        out["steps"] += entry["name"] != "finish"  # agy's call that ends its answer; Codex's final answer is no step
        out["text"].append(f"{entry['name']} {json.dumps(entry['params'])}")
        out["outputs"] += entry["outputs"]
        if entry["name"] not in AGY_LOCAL_TOOLS:
            out["other_tools"].append(entry["name"])
    out["user_messages"] = max(len(users) - 1, 0)  # the prompt is the first user input
    return out


def elapsed(start, end):
    from datetime import datetime
    return (datetime.fromisoformat(end.replace("Z", "+00:00")) - datetime.fromisoformat(start.replace("Z", "+00:00"))).total_seconds()


def own_spellings(paths):
    """Each own path in absolute, ~/, $HOME/, and ${HOME}/ form, longest first."""
    home, out = str(Path.home()), set()
    for p in (str(x) for x in paths if x):
        out.add(p)
        if p.startswith(home + "/"):
            rel = p[len(home) + 1:]
            out |= {f"~/{rel}", f"$HOME/{rel}", f"${{HOME}}/{rel}"}
    return sorted(out, key=len, reverse=True)


def validity_hits(text, outputs, own_paths=()):
    """Study material in commands and paths, oracle content or study paths in outputs, and network commands."""
    text = text.replace("\\n", "\n")  # logged inputs keep newlines escaped; a second command line counts too
    outputs = list(outputs)
    for p in own_spellings(own_paths):
        text = text.replace(p, "<own>")
        outputs = [o.replace(p, "<own>") for o in outputs]
    study = sorted({m for m in STUDY_MARKERS if m in text} | {r.pattern for r in HOME_WIDE if r.search(text)})
    content = sorted({m for m in CONTENT_MARKERS if any(m in o for o in outputs)})
    network = sorted({m.group(0).strip(" ;&|(\"'`/\n\t") for m in NETWORK_COMMANDS.finditer(text)})
    return study, content, network


def runtime_observations(n, record, run, log, own_paths=()):
    """One observation per capability: enforced (by a mechanism shown in the log), held (within the limit or matching
    the request, not enforced or attested), violated, or not_observable."""
    def obs(cap, result, evidence):
        return dict(capability=cap, kind="runtime_observation", session_slot=n, result=result, evidence=evidence)
    agy = record["config_id"] == "CONFIG_01_GEMINI_FLASH_MED"
    own = list(own_paths) or [record.get("workspace")]
    study, content, network = validity_hits("\n".join(log["text"]), log.get("outputs") or [], own)
    wall = elapsed(run["started_at"], run["ended_at"])
    if agy and log.get("agent_seconds") is not None:
        seconds = float(log["agent_seconds"])  # agy reports its own run time; startup is not part of the session
    else:
        spans = [wall] + ([elapsed(log["first"], log["last"])] if log["first"] and log["last"] else [])
        seconds = max(spans)  # the longer of the script's times and the log's own timestamps
    stopped = bool(run.get("stopped_by_watchdog")) or (agy and run.get("exit_code") == 3 and (
        log.get("finished_reason") == "print_timeout" or wall >= TIME_LIMIT))
    req = REQUESTED[record["config_id"]]
    out = []
    models, efforts = {m for m in log["models"] if m}, {e for e in log["efforts"] if e}
    same = models == {req["model"]} and (req["effort"] is None or efforts == {req["effort"]})
    out.append(obs("observed_model_identity", "not_observable" if not models else "held" if same else "violated",
                   f"session log reports model {sorted(models)} and effort {sorted(efforts) or 'in the model name'} "
                   "(reported by the client, not attested by the provider)"))
    if not agy:
        net = [p for p in log["sandbox"] if p]
        ok = bool(net) and all(p.get("type") == "workspace-write" and p.get("network_access") is False for p in net)
        out.append(obs("network_isolation", "violated" if network or log["other_tools"] or not ok else "enforced",
                       f"Codex sandbox policies in the log: {net}; network commands: {network}; "
                       f"tools outside the local set: {log['other_tools']}"))
    else:
        out.append(obs("network_isolation", "violated" if network or log["other_tools"] else "not_observable",
                       "the session log does not report agy's sandbox policy; under the session settings the terminal "
                       "sandbox blocked network access in the sandbox checks (versions 6 to 8), and the gate refuses "
                       f"sandbox bypass requests; network commands: {network}; tools outside the local set: "
                       f"{log['other_tools']}"))
    steps = log["steps"]
    out.append(obs("timeout_900_seconds", "enforced" if stopped else "held" if seconds <= TIME_LIMIT else "violated",
                   f"{seconds:.0f} s ({'reported by agy' if agy and log.get('agent_seconds') is not None else 'the longer of the script times and the log timestamps'}; wall {wall:.0f} s)"
                   + ("; stopped at the limit" if stopped else "")))
    out.append(obs("oracle_isolation", "violated" if study or content else "held",
                   f"study material in commands or paths: {study}; oracle content in tool outputs: {content}"
                   if study or content else "no study material in the logged commands, paths, or outputs"))
    out.append(obs("operator_intervention", "violated" if log["user_messages"] > 0 else "held",
                   f"{log['user_messages']} user message(s) after the prompt"))
    out.append(obs("resource_limits", "not_observable",
                   "no CPU or memory limits are applied to sessions on the host, so none can be observed"))
    return out, steps, seconds, stopped, dict(study=study, content=content, network=network)


def close_session(n, ledger=None):
    """Grades the session's patch and records it. A grading run without a report is kept as an attempt and the slot
    stays started, so close can be run again on the same patch; nothing is recorded as resolved or not."""
    ledger = ledger or s.SessionLedger(LEDGER)
    if ledger.state(n) != "started":
        raise RuntimeError(f"Session {n} is {ledger.state(n)}, not started")
    folder = SESSIONS / f"{n:02d}"
    slot = ledger.slot(n)
    opened = json.loads((folder / "opened.json").read_text())
    if (opened["config_id"], opened["task_id"]) != (slot["config_id"], slot["task_id"]):
        raise RuntimeError("opened.json does not match the ledger slot")
    for name, key in (("run.sh", "run_sh_sha256"), ("prompt.md", "prompt_sha256")):
        if sha(folder / name) != opened[key]:
            raise RuntimeError(f"{name} changed after the slot was opened")
    note = json.loads((folder / "record.json").read_text())
    if not note.get("operator"):
        raise ValueError("record.json is missing: operator")
    record = dict(config_id=slot["config_id"], task_id=slot["task_id"], workspace=opened["workspace"], phase=slot["phase"],
                  operator=note["operator"], notes=note.get("notes", ""))
    if not (folder / "run.json").exists():
        raise ValueError(f"{folder / 'run.json'} is missing: run {folder / 'run.sh'} first")
    run = json.loads((folder / "run.json").read_text())
    rows = rows_by_id()
    if FROZEN.exists():
        manifest = json.loads(FROZEN.read_text())
        # the session ran with the version run.sh recorded; a later tool update must not block closing it
        drift = list(frozen_drift(manifest, record["task_id"], rows, live_tools=False))
        tool = launch_settings(record["config_id"])["tool"]
        if run.get("tool_version") != (manifest.get("tools") or {}).get(tool):
            drift.append(f"{tool} version in run.json")
        if h.harness_version() != manifest["harness"]["swebench"]:
            drift.append("SWE-bench harness version")
        if drift:
            raise RuntimeError("Changed since the freeze: " + "; ".join(drift))
    logs = sorted(p for p in (folder / "logs").iterdir() if p.is_file())
    if record["config_id"] == "CONFIG_02_SOL_MED":
        rollouts = [p for p in logs if p.name.startswith("rollout-")]
        if not rollouts:
            raise ValueError(f"A Codex session needs its rollout log in {folder / 'logs'}")
        log, primary = codex_log(rollouts), rollouts[0]
        own = [record["workspace"], CODEX_RUNS / f"slot-{n:02d}", WORKSPACES]
    else:
        primary = folder / "logs" / "agy-stream.jsonl"
        log = agy_log(primary)
        # agy tells the agent to read a cut-off tool output from its own conversation folder; that folder is its own
        own = [record["workspace"], WORKSPACES] + ([AGY_HOME / "brain" / log["conversation_id"]] if log["conversation_id"] else [])
    reserved = slot["reserved_at"]
    for label, when in (("run.sh", run["started_at"]), ("the session log", log["first"])):
        if when and elapsed(reserved, when) < -RESERVATION_TOLERANCE:
            raise RuntimeError(f"{label} starts at {when}, before slot {n} was reserved at {reserved}")
    ws = Path(record["workspace"])
    archived = ARCHIVE / f"protocol-{s.PROTOCOL_NUMBER}" / f"slot-{n:02d}"
    if archived.exists():
        raise FileExistsError(f"{archived} already exists")
    git("add", "-A", cwd=ws)  # files the agent created are part of its patch
    row = rows[record["task_id"]]
    patch = git("diff", "--cached", "--binary", row["base_commit"], cwd=ws)
    saved = folder / "patch.diff"
    if saved.exists() and saved.read_text() != patch:
        raise RuntimeError("The workspace changed after the patch was first taken; record this with `fail`")
    if not saved.exists():
        saved.write_text(patch)
    stamp = s.now().replace(":", "").replace("-", "")[:15]
    grading = h.grade(row, patch, f"{RUN_PREFIX}-p{s.PROTOCOL_NUMBER}-{n:02d}-{stamp}") if patch.strip() else dict(
        resolved=False, report=None, logs={}, note="empty patch; not graded")
    if grading["resolved"] is None:
        s.save_new(folder / "grading-attempts" / f"{stamp}.json", dict(grading, attempted_at=s.now()))
        return dict(status="grading failed; kept as an attempt; the slot stays started", attempt=stamp)
    observations, steps, seconds, stopped, hits = runtime_observations(n, record, run, log, own)
    within = seconds < TIME_LIMIT and not stopped
    invalid = []
    if hits["study"]:
        invalid.append(f"study material in commands or paths: {hits['study']}")
    if hits["content"]:
        invalid.append(f"oracle content in tool outputs: {hits['content']}")
    if hits["network"]:
        invalid.append(f"network commands: {hits['network']}")
    if log["other_tools"]:  # the public fix is reachable through the web; subagents and knowledge are not visible
        invalid.append(f"tools outside the local set: {log['other_tools']}")
    if log["user_messages"]:
        invalid.append(f"{log['user_messages']} user message(s) after the prompt")
    grading_files = s.scoring_files(patch)
    if grading_files:  # the harness runs the patched repository's own test runner
        invalid.append(f"grading files changed: {grading_files}")
    changed = agy_files_changed(ws) if record["config_id"] == "CONFIG_01_GEMINI_FLASH_MED" else []
    if changed:
        invalid.append(f"the session's agy files in .agents/ changed: {changed}")
    # the raw logs are not committed (they hold account details); provenance points to this committed summary
    parsed = {k: (sorted(v) if isinstance(v, set) else v) for k, v in log.items() if k != "outputs"}
    summary_path = folder / "log-summary.json"
    summary_text = json.dumps(dict(raw_log=str(primary.relative_to(ROOT)), raw_log_sha256=sha(primary), **parsed),
                              indent=2, sort_keys=True)
    if summary_path.exists() and summary_path.read_text() != summary_text:
        raise RuntimeError("log-summary.json differs from the log; record this with `fail`")
    if not summary_path.exists():
        summary_path.write_text(summary_text)
    observation = dict(task_id=record["task_id"], config_id=record["config_id"], repository=s.REPOSITORY,
                       resolved=bool(grading["resolved"] and within and not invalid),
                       tests_resolved=grading["resolved"], within_limits=within, valid=not invalid,
                       invalid_reasons=invalid,
                       patch=dict(path=str(saved.relative_to(ROOT)), sha256=sha(saved), task_id=record["task_id"]),
                       provenance=dict(session_id=f"protocol-{s.PROTOCOL_NUMBER}-slot-{n:02d}",
                                       log=str(summary_path.relative_to(ROOT)), log_sha256=sha(summary_path),
                                       raw_log=str(primary.relative_to(ROOT)), raw_log_sha256=sha(primary),
                                       controls=dict(no_scoring_file_changes=dict(
                                           passed=not grading_files, changed_files=grading_files))))
    archived.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(ws), str(archived))  # the folder then holds nothing an agent in a later session could read
    summary = {k: (sorted(v) if isinstance(v, set) else v) for k, v in log.items() if k not in ("text", "outputs", "sandbox")}
    gate = folder / "logs" / "agy-gate.jsonl"
    if gate.exists():
        summary["gate_refusals"] = [r for r in map(json.loads, gate.read_text().splitlines()) if r.get("decision") == "deny"]
    s.save_new(folder / "session.json", dict(
        record=record, opened=opened, run=run, logs={str(p.relative_to(ROOT)): sha(p) for p in logs},
        log_summary=summary, grading=grading, observation=observation, runtime_observations=observations,
        workspace_archived_to=str(archived), closed_at=s.now()))
    ledger.finish(n, "completed")
    return observation


@contextlib.contextmanager
def rehearsal(round_=1):
    """open, close, and fail on the real code, before the freeze, for REHEARSAL_TASK only: the rehearsal's own ledger
    and records (audit_checks/rehearsal, then rehearsal-2 and so on per round), archive, Codex run homes, and harness
    run names. There is no authorization and no drift check, because nothing is frozen yet; run.sh still checks the
    live tool versions."""
    if FROZEN.exists():
        raise RuntimeError("The rehearsal runs only before the freeze")
    manifest = dict(selection=dict(pilot=[REHEARSAL_TASK], source=[], target=[]),
                    tools={t: tool_version(t) for t in ("codex", "agy")})
    g = globals()
    name = REHEARSAL.name if round_ == 1 else f"{REHEARSAL.name}-{round_}"
    folder = REHEARSAL.with_name(name)
    patched = dict(LEDGER=folder / "ledger", SESSIONS=folder / "sessions", ARCHIVE=ARCHIVE / name,
                   CODEX_RUNS=CODEX_RUNS / name, RUN_PREFIX=name,
                   check_authorization=lambda phase: manifest, frozen_drift=lambda *a, **k: [])
    saved = {k: g[k] for k in patched}
    g.update(patched)  # the module's functions read these names at call time, so they run unchanged
    try:
        yield manifest
    finally:
        g.update(saved)


def agy_files_changed(ws):
    """The files run.sh put into .agents/ that differ from the frozen sources (an agent could edit them)."""
    return sorted(rel for rel, src in AGY_WORKSPACE_FILES.items()
                  if (Path(ws) / ".agents" / rel).exists() and sha(Path(ws) / ".agents" / rel) != sha(src))


def fail_session(n, status, description, ledger=None):
    """Records the outcome, then moves what the slot left behind to the archive, so the next slot can open: the
    workspace, a Codex run home (without its copy of the sign-in), and agy memory created during the run."""
    (ledger or s.SessionLedger(LEDGER)).finish(n, status, description)
    arch = ARCHIVE / f"protocol-{s.PROTOCOL_NUMBER}"
    opened = SESSIONS / f"{n:02d}" / "opened.json"
    moved = []
    if opened.exists():
        ws = Path(json.loads(opened.read_text())["workspace"])
        if ws.exists():
            arch.mkdir(parents=True, exist_ok=True)
            shutil.move(str(ws), str(arch / f"slot-{n:02d}"))
            moved.append(str(arch / f"slot-{n:02d}"))
    run_home = CODEX_RUNS / f"slot-{n:02d}"
    if run_home.exists():
        (run_home / "auth.json").unlink(missing_ok=True)  # a copy; the sign-in stays in CODEX_HOME
        arch.mkdir(parents=True, exist_ok=True)
        shutil.move(str(run_home), str(arch / f"codex-home-slot-{n:02d}"))
        moved.append(str(arch / f"codex-home-slot-{n:02d}"))
    leftovers = [AGY_HOME / x for x in AGY_STATE if (AGY_HOME / x).exists()]
    if leftovers and opened.exists() and json.loads(opened.read_text())["config_id"] == "CONFIG_01_GEMINI_FLASH_MED":
        dest = arch / f"agy-state-slot-{n:02d}"
        dest.mkdir(parents=True, exist_ok=True)
        for x in leftovers:
            shutil.move(str(x), str(dest / x.name))
        moved.append(str(dest))
    return moved


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("freeze")
    p = sub.add_parser("sign-form")
    p.add_argument("name")
    p.add_argument("--author", required=True)
    p = sub.add_parser("sign-requirement")
    p.add_argument("--author", required=True)
    p = sub.add_parser("authorize")
    p.add_argument("--phase", required=True, choices=list(s.PHASES))
    p.add_argument("--name", required=True)
    p.add_argument("--statement", required=True)
    p = sub.add_parser("open")
    p.add_argument("--phase", required=True, choices=["pilot", "source", "target", "reserve"])
    p.add_argument("--config", required=True, choices=list(s.CONFIGURATIONS))
    p.add_argument("--replaces", type=int, help="with --phase reserve: the slot whose infrastructure failure this replaces")
    p = sub.add_parser("close")
    p.add_argument("--slot", type=int, required=True)
    p = sub.add_parser("fail")
    p.add_argument("--slot", type=int, required=True)
    p.add_argument("--status", required=True, choices=[o for o in s.SESSION_OUTCOMES if o != "completed"])
    p.add_argument("--description", required=True)
    for name in ("open", "close", "fail"):
        sub.choices[name].add_argument("--rehearsal", nargs="?", const=1, type=int, metavar="ROUND",
                                       help=f"rehearsal before the freeze on {REHEARSAL_TASK} (use --phase pilot)")
    a = parser.parse_args(argv)
    with rehearsal(a.rehearsal) if getattr(a, "rehearsal", None) else contextlib.nullcontext():
        run_command(a)


def run_command(a):
    if a.cmd == "freeze":
        print(json.dumps(freeze()["selection"], indent=2))
    elif a.cmd == "sign-form":
        sign_form(a.name, a.author)
    elif a.cmd == "sign-requirement":
        sign_requirement(a.author)
    elif a.cmd == "authorize":
        authorize(a.phase, a.name, a.statement)
    elif a.cmd == "open":
        n, folder = open_session(a.phase, a.config, replaces=a.replaces)
        print(f"slot {n}: run `bash {folder / 'run.sh'}` in the background, then close it")
    elif a.cmd == "close":
        print(json.dumps(close_session(a.slot), indent=2))
    else:
        fail_session(a.slot, a.status, a.description)


if __name__ == "__main__":
    main()

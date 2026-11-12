"""New SymPy target pool for protocol 4. Nothing here calls a model.

Pool rule (approved 2026-11-05, fixed before retrieval): SymPy pull requests merged from 2026-05-01 through
2026-11-05 that close at least one linked issue and change both a test file and a source file under sympy/.
The window starts after the later training cutoff of the two configurations (RULE["cutoffs"]).

Steps, each written once:
  retrieve   one GitHub search, saved with the query, date, rule decisions, and hash;
  confirm    in order_key order, check each included PR through the GitHub API and build a SWE-bench format row;
  derive     build a grading image, run the hidden tests before and after the reference patch, and record
             FAIL_TO_PASS (fail before, pass after) and PASS_TO_PASS (pass both); then run eligibility as for source.
Target images are built locally (linux/arm64, Python 3.12) because SWE-bench publishes none for these tasks; source
tasks use the published amd64 images. Both run the same SymPy test runner and log parser.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from paper2.preparation import harness as h  # noqa: E402
from paper2.preparation.study_controls import order_key, save_new  # noqa: E402

REPO = "sympy/sympy"
RULE = dict(
    repo=REPO, merged_from="2026-05-01", merged_through="2026-11-05",
    requires=["merged pull request", "closes at least one linked issue",
              "changes a test file (a path with a tests directory or a test_ file name)",
              "changes a Python source file under sympy/ that is not a test file",
              "file list complete in the search response (at most 100 files)"],
    cutoffs=[dict(config_id="CONFIG_01_GEMINI_FLASH_MED", model="Gemini 3.8 Flash",
                  cutoff="March 2026; the card adds that some domains end at January 2025",
                  source="https://deepmind.google/models/model-cards/gemini-3-8-flash/", accessed="2026-11-05"),
             dict(config_id="CONFIG_02_SOL_MED", model="gpt-6.1-sol", cutoff="2026-04-30",
                  source="https://developers.openai.com/api/docs/models/gpt-6.1-sol", accessed="2026-11-05")],
    approved="2026-11-05 by the author, before retrieval")
SEARCH = f"repo:{REPO} is:pr is:merged merged:{RULE['merged_from']}..{RULE['merged_through']}"
QUERY = """query($q:String!,$after:String){search(query:$q,type:ISSUE,first:50,after:$after){issueCount
pageInfo{hasNextPage endCursor} nodes{... on PullRequest{number title url createdAt mergedAt baseRefOid
closingIssuesReferences(first:10){nodes{number url createdAt}} files(first:100){totalCount nodes{path}}}}}}"""
POOL = ROOT / "paper2/records/sympy_target_pool.json"
ROWS = ROOT / "paper2/records/sympy_target_rows"
IMAGES = h.BASE / "target_images"
BASE_IMAGE = "paper2/sympy-target-base:2"  # :1 lacked pytest, which bin/test now needs
PYTHON_IMAGE = "python:3.12-slim"


def _github_token():
    """Retrieve a GitHub token from env or Git Credential Manager in memory without writing it to disk."""
    import os
    for var in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(var):
            return os.environ[var].strip()
    out = subprocess.run(
        ["git", "credential", "fill"],
        input="protocol=https\nhost=github.com\n\n",
        capture_output=True, text=True,
    )
    if out.returncode == 0:
        for line in out.stdout.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    return None


def gh(*args, tries=4):
    """Read-only GitHub API call; network errors are retried, any other failure stops the run."""
    import shutil
    import time
    import urllib.error
    import urllib.request

    if shutil.which("gh"):
        for attempt in range(tries):
            out = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
            if out.returncode == 0:
                return out.stdout
            if "connecting to" not in out.stderr and "timeout" not in out.stderr.lower():
                break
            time.sleep(5 * (attempt + 1))
        raise RuntimeError(f"gh {' '.join(args[:2])} failed: {out.stderr.strip()[:300]}")

    if not args or args[0] != "api" or len(args) < 2:
        raise RuntimeError(f"gh executable missing and fallback supports only `gh api ...`: {args[:2]}")
    endpoint = args[1].lstrip("/")
    headers = {"User-Agent": "paper2-targets", "Accept": "application/vnd.github+json"}
    i = 2
    while i < len(args):
        if args[i] == "-H" and i + 1 < len(args) and ":" in args[i + 1]:
            k, v = args[i + 1].split(":", 1)
            headers[k.strip()] = v.strip()
            i += 2
        else:
            i += 1
    token = _github_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/{endpoint}"
    last_err = ""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            last_err = f"HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')[:200]}"
            if exc.code < 500 and exc.code not in (403, 429):
                break
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"gh {' '.join(args[:2])} failed: {last_err[:300]}")


def is_test(path):
    parts = path.split("/")
    return "tests" in parts[:-1] or parts[-1].startswith("test_")


def is_source(path):
    return path.startswith("sympy/") and path.endswith(".py") and not is_test(path)


def rule_reasons(pr):
    """Reasons a pull request fails the pool rule; empty means included."""
    files = [n["path"] for n in pr["files"]["nodes"]]
    reasons = []
    if not pr.get("mergedAt"):
        reasons.append("not merged")
    if not pr["closingIssuesReferences"]["nodes"]:
        reasons.append("closes no linked issue")
    if pr["files"]["totalCount"] > len(files):
        reasons.append("file list truncated")
    if not any(is_test(f) for f in files):
        reasons.append("changes no test file")
    if not any(is_source(f) for f in files):
        reasons.append("changes no source file")
    return reasons


def retrieve():
    if POOL.exists():
        raise FileExistsError(f"{POOL} exists; the pool is retrieved once")
    prs, after, count = [], None, None
    while True:
        args = ["api", "graphql", "-f", f"query={QUERY}", "-f", f"q={SEARCH}"] + (["-f", f"after={after}"] if after else [])
        page = json.loads(gh(*args))["data"]["search"]
        count = page["issueCount"]
        prs += [n for n in page["nodes"] if n]
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    if len(prs) != count:
        raise RuntimeError(f"search returned {len(prs)} of {count} pull requests")
    for pr in prs:
        pr["rule_reasons"] = rule_reasons(pr)
        pr["included"] = not pr["rule_reasons"]
        pr["task_id"] = f"sympy__sympy-{pr['number']}"
        pr["order_key"] = order_key(pr["task_id"])
    prs.sort(key=lambda p: p["number"])
    pool = dict(record="paper2-target-pool/1", rule=RULE, search=SEARCH, retrieved_at=h.now(), search_count=count,
                included=sum(p["included"] for p in prs), prs=prs,
                prs_sha256=hashlib.sha256(json.dumps(prs, sort_keys=True).encode()).hexdigest())
    save_new(POOL, pool)
    return pool


def load_pool():
    pool = json.loads(POOL.read_text())
    if hashlib.sha256(json.dumps(pool["prs"], sort_keys=True).encode()).hexdigest() != pool["prs_sha256"]:
        raise ValueError("target pool differs from its recorded hash")
    return pool


def split_diff(diff):
    """Returns (source patch, test patch) by file, as SWE-bench separates the reference fix from its tests."""
    chunks = ["diff --git " + c for c in diff.split("\ndiff --git ")]
    chunks[0] = chunks[0][len("diff --git "):]
    src, test = [], []
    for c in chunks:
        path = c.split("\n", 1)[0].split(" b/", 1)[-1]
        (test if is_test(path) else src).append(c.rstrip("\n") + "\n")
    return "".join(src), "".join(test)


def test_files(test_patch):
    """(all test files touched, files that exist at the base commit)."""
    files, existing = [], []
    for c in test_patch.split("diff --git ")[1:]:
        path = c.split("\n", 1)[0].split(" b/", 1)[-1]
        files.append(path)
        if "\nnew file mode" not in c.split("@@", 1)[0]:
            existing.append(path)
    return files, existing


def eval_script(base_commit, test_patch):
    files, existing = test_files(test_patch)
    reset = f"git checkout {base_commit} {' '.join(existing)}" if existing else ":"
    return "\n".join([
        "#!/bin/bash", "set -uxo pipefail", "cd /testbed", "git config --global --add safe.directory /testbed",
        "git status", f"git -c core.fileMode=false diff {base_commit}", reset,
        "git apply -v - <<'EOF_114329324912'", test_patch.rstrip("\n"), "EOF_114329324912",
        ": '>>>>> Start Test Output'",
        f"PYTHONWARNINGS='ignore::UserWarning,ignore::SyntaxWarning' python -m pytest -rA -p no:cacheprovider "
        f"--continue-on-collection-errors {' '.join(files)}",
        ": '>>>>> End Test Output'", reset, ""])


def confirm(pr):
    """Identity checks through the GitHub API, then a SWE-bench format row. Returns (row or None, checks)."""
    n = pr["number"]
    rest = json.loads(gh("api", f"repos/{REPO}/pulls/{n}"))
    base = rest["base"]["sha"]
    issues = []
    for ref in pr["closingIssuesReferences"]["nodes"]:
        issue = json.loads(gh("api", f"repos/{REPO}/issues/{ref['number']}"))
        issues.append(dict(number=issue["number"], is_issue="pull_request" not in issue, title=issue["title"],
                           body=issue.get("body") or "", created_at=issue["created_at"], url=issue["html_url"]))
    checks = dict(merged=bool(rest.get("merged_at")) and rest.get("merged") is True,
                  merged_in_window=bool(rest.get("merged_at")) and
                  RULE["merged_from"] <= rest["merged_at"][:10] <= RULE["merged_through"],
                  base_commit_exists=json.loads(gh("api", f"repos/{REPO}/commits/{base}"))["sha"] == base,
                  closes_issues=bool(issues) and all(i["is_issue"] for i in issues), checked_at=h.now())
    if not all(v for k, v in checks.items() if k != "checked_at"):
        return None, checks
    diff = gh("api", f"repos/{REPO}/pulls/{n}", "-H", "Accept: application/vnd.github.diff")
    patch, test_patch = split_diff(diff)
    row = dict(instance_id=pr["task_id"], repo=REPO, base_commit=base, created_at=rest["created_at"],
               merged_at=rest["merged_at"], merge_commit=rest.get("merge_commit_sha"), pull_request=rest["html_url"],
               issues=[dict(number=i["number"], url=i["url"], created_at=i["created_at"]) for i in issues],
               problem_statement="".join(f"{i['title']}\n{i['body']}\n" for i in issues), hints_text="",
               patch=patch, test_patch=test_patch, FAIL_TO_PASS=[], PASS_TO_PASS=[],
               image=f"paper2/sympy-target:{n}", eval_script=eval_script(base, test_patch),
               log_parser="parse_log_pytest", eval_type="pass_and_fail", version=None, environment_setup_commit=None,
               identity_checks=checks)
    return row, checks


def docker(*args, input=None):
    return subprocess.run(["docker", *args], input=input, capture_output=True, text=True)


def build_base_image():
    """One base image: Python 3.12 (pinned by digest), mpmath, and a full SymPy clone with tags."""
    if h.image_id(BASE_IMAGE):
        return h.image_id(BASE_IMAGE)
    docker("pull", PYTHON_IMAGE)
    digest = docker("image", "inspect", "--format", "{{index .RepoDigests 0}}", PYTHON_IMAGE).stdout.strip()
    dockerfile = "\n".join([f"FROM {digest}", "RUN apt-get update && apt-get install -y --no-install-recommends git "
                            "&& rm -rf /var/lib/apt/lists/*", "RUN pip install --no-cache-dir mpmath==1.3.0 setuptools pytest hypothesis && pip freeze > /pip-freeze.txt",
                            f"RUN git clone https://github.com/{REPO}.git /testbed", "WORKDIR /testbed", ""])
    IMAGES.mkdir(parents=True, exist_ok=True)
    (IMAGES / "base.Dockerfile").write_text(dockerfile)
    out = docker("build", "-t", BASE_IMAGE, "-f", str(IMAGES / "base.Dockerfile"), str(IMAGES))
    (IMAGES / "base.build.log").write_text(out.stdout + out.stderr)
    if out.returncode != 0:
        raise RuntimeError("base image build failed; see target_images/base.build.log")
    return h.image_id(BASE_IMAGE)


def build_image(row):
    dockerfile = f"FROM {BASE_IMAGE}\nRUN git checkout -q {row['base_commit']} && git clean -fdxq && " \
                 "pip install --no-cache-dir -q -e .\n"
    name = row["instance_id"]
    (IMAGES / f"{name}.Dockerfile").write_text(dockerfile)
    out = docker("build", "-t", row["image"], "-f", str(IMAGES / f"{name}.Dockerfile"), str(IMAGES))
    (IMAGES / f"{name}.build.log").write_text(out.stdout + out.stderr)
    if out.returncode != 0:
        return None, None
    version = docker("run", "--rm", row["image"], "python", "-c", "import sympy;print(sympy.__version__)").stdout.strip()
    return h.image_id(row["image"]), version


PARSE = """import json,sys
from swebench.harness.constants import START_TEST_OUTPUT as S, END_TEST_OUTPUT as E
from swebench.harness.log_parsers import PARSER_REGISTRY
parse=PARSER_REGISTRY[sys.argv[1]]
out={}
for p in sys.argv[2:]:
    c=open(p).read()
    out[p]=parse(c.split(S)[1].split(E)[0],None) if S in c and E in c else None
print(json.dumps(out))"""


def statuses(paths, parser="parse_log_pytest"):
    """Per-test statuses parsed by the harness's own log parser."""
    out = subprocess.run([h.PYTHON, "-c", PARSE, parser, *map(str, paths)], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def derive(row, stamp):
    """Runs the hidden tests before (test patch only) and after the reference patch; returns the test lists or a
    reason. A missing test output is a harness failure."""
    rid = row["instance_id"]
    before = h.run_harness([row], {rid: h.BASELINE_PATCH}, f"target-derive-before-{rid}-{stamp}", model="derive")[rid]
    after = h.run_harness([row], {rid: row["patch"]}, f"target-derive-after-{rid}-{stamp}", model="derive")[rid]
    paths = [h.RUNS / "logs/run_evaluation" / f"target-derive-{w}-{rid}-{stamp}" / "derive" / rid / "test_output.txt"
             for w in ("before", "after")]
    if not all(p.exists() for p in paths):
        return None, "harness failure: no test output", dict(before=before["logs"], after=after["logs"])
    parsed = statuses(paths, row["log_parser"])
    b, a = parsed[str(paths[0])], parsed[str(paths[1])]
    if not b or not a:
        return None, "no parsed test results", dict(before=before["logs"], after=after["logs"])
    f2p, p2p = test_lists(b, a)
    return dict(FAIL_TO_PASS=f2p, PASS_TO_PASS=p2p), (None if f2p else "no FAIL_TO_PASS test"), \
        dict(before=before["logs"], after=after["logs"])


def passed(status):
    """The grader's rule (swebench harness/grading.py, test_passed): PASSED or XFAIL; a missing test has not passed."""
    return status in ("PASSED", "XFAIL")


def test_lists(before, after):
    """FAIL_TO_PASS: passes after the reference patch and did not pass before (failed, errored, skipped, or did not
    run, for example when its file failed to import). PASS_TO_PASS: passes both before and after."""
    f2p = sorted(t for t, s in after.items() if passed(s) and not passed(before.get(t)))
    p2p = sorted(t for t, s in after.items() if passed(s) and passed(before.get(t)))
    return f2p, p2p


def supersede(tid, reason):
    """Moves a task's row and eligibility record to superseded/ under a time-stamped name, with a reason file.
    Nothing is deleted."""
    stamp = h.now().replace(":", "").replace("-", "")[:15]
    moved = []
    for src in (ROWS / f"{tid}.json", h.ELIGIBILITY / f"{tid}.json"):
        if src.exists():
            dst = src.parent / "superseded" / f"{tid}-{stamp}.json"
            dst.parent.mkdir(exist_ok=True)
            src.rename(dst)
            save_new(dst.with_name(f"{tid}-{stamp}.reason.json"), dict(task_id=tid, superseded_at=h.now(), reason=reason))
            moved.append(str(dst.relative_to(ROOT)))
    return moved


def rederive(tid, reason):
    """Recomputes a row's test lists from the derivation outputs the row names, after a correction of the derivation
    rule; supersedes the old records. Returns the new row, or None when the lists do not change."""
    old = json.loads((ROWS / f"{tid}.json").read_text())
    logs = old["derivation"]["logs"]
    paths = [ROOT / next(k for k in logs[w] if k.endswith("test_output.txt")) for w in ("before", "after")]
    parsed = statuses(paths, old["log_parser"])
    f2p, p2p = test_lists(parsed[str(paths[0])], parsed[str(paths[1])])
    if (f2p, p2p) == (old.get("FAIL_TO_PASS"), old.get("PASS_TO_PASS")):
        return None
    moved = supersede(tid, reason)
    row = dict(old, FAIL_TO_PASS=f2p, PASS_TO_PASS=p2p, status="derived" if f2p else "no FAIL_TO_PASS test",
               supersedes=dict(paths=moved, reason=reason))
    row["derivation"] = dict(old["derivation"], reason=None if f2p else "no FAIL_TO_PASS test")
    save_new(ROWS / f"{tid}.json", row)
    if not f2p:
        save_new(h.ELIGIBILITY / f"{tid}.json", dict(record="paper2-eligibility/1", task_id=tid, task_kind="upstream",
                                                     status="ineligible", reasons=["derivation: no FAIL_TO_PASS test"],
                                                     checked_at=h.now()))
    return row


def docker(*args, input=None):
    return subprocess.run(["docker", *args], input=input, capture_output=True, text=True)


def build_base_image():
    """One base image: Python 3.12 (pinned by digest), mpmath, and a full SymPy clone with tags."""
    if h.image_id(BASE_IMAGE):
        return h.image_id(BASE_IMAGE)
    docker("pull", PYTHON_IMAGE)
    digest = docker("image", "inspect", "--format", "{{index .RepoDigests 0}}", PYTHON_IMAGE).stdout.strip()
    dockerfile = "\n".join([f"FROM {digest}", "RUN apt-get update && apt-get install -y --no-install-recommends git "
                            "&& rm -rf /var/lib/apt/lists/*", "RUN pip install --no-cache-dir mpmath==1.3.0 setuptools pytest hypothesis && pip freeze > /pip-freeze.txt",
                            f"RUN git clone https://github.com/{REPO}.git /testbed", "WORKDIR /testbed", ""])
    IMAGES.mkdir(parents=True, exist_ok=True)
    (IMAGES / "base.Dockerfile").write_text(dockerfile)
    out = docker("build", "-t", BASE_IMAGE, "-f", str(IMAGES / "base.Dockerfile"), str(IMAGES))
    (IMAGES / "base.build.log").write_text(out.stdout + out.stderr)
    if out.returncode != 0:
        raise RuntimeError("base image build failed; see target_images/base.build.log")
    return h.image_id(BASE_IMAGE)


def build_image(row):
    dockerfile = f"FROM {BASE_IMAGE}\nRUN git checkout -q {row['base_commit']} && git clean -fdxq && " \
                 "pip install --no-cache-dir -q -e .\n"
    name = row["instance_id"]
    (IMAGES / f"{name}.Dockerfile").write_text(dockerfile)
    out = docker("build", "-t", row["image"], "-f", str(IMAGES / f"{name}.Dockerfile"), str(IMAGES))
    (IMAGES / f"{name}.build.log").write_text(out.stdout + out.stderr)
    if out.returncode != 0:
        return None, None
    version = docker("run", "--rm", row["image"], "python", "-c", "import sympy;print(sympy.__version__)").stdout.strip()
    return h.image_id(row["image"]), version


PARSE = """import json,sys
from swebench.harness.constants import START_TEST_OUTPUT as S, END_TEST_OUTPUT as E
from swebench.harness.log_parsers import PARSER_REGISTRY
parse=PARSER_REGISTRY[sys.argv[1]]
out={}
for p in sys.argv[2:]:
    c=open(p).read()
    out[p]=parse(c.split(S)[1].split(E)[0],None) if S in c and E in c else None
print(json.dumps(out))"""


def statuses(paths, parser="parse_log_pytest"):
    """Per-test statuses parsed by the harness's own log parser."""
    out = subprocess.run([h.PYTHON, "-c", PARSE, parser, *map(str, paths)], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def derive(row, stamp):
    """Runs the hidden tests before (test patch only) and after the reference patch; returns the test lists or a
    reason. A missing test output is a harness failure."""
    rid = row["instance_id"]
    before = h.run_harness([row], {rid: h.BASELINE_PATCH}, f"target-derive-before-{rid}-{stamp}", model="derive")[rid]
    after = h.run_harness([row], {rid: row["patch"]}, f"target-derive-after-{rid}-{stamp}", model="derive")[rid]
    paths = [h.RUNS / "logs/run_evaluation" / f"target-derive-{w}-{rid}-{stamp}" / "derive" / rid / "test_output.txt"
             for w in ("before", "after")]
    if not all(p.exists() for p in paths):
        return None, "harness failure: no test output", dict(before=before["logs"], after=after["logs"])
    parsed = statuses(paths, row["log_parser"])
    b, a = parsed[str(paths[0])], parsed[str(paths[1])]
    if not b or not a:
        return None, "no parsed test results", dict(before=before["logs"], after=after["logs"])
    f2p, p2p = test_lists(b, a)
    return dict(FAIL_TO_PASS=f2p, PASS_TO_PASS=p2p), (None if f2p else "no FAIL_TO_PASS test"), \
        dict(before=before["logs"], after=after["logs"])


def passed(status):
    """The grader's rule (swebench harness/grading.py, test_passed): PASSED or XFAIL; a missing test has not passed."""
    return status in ("PASSED", "XFAIL")


def test_lists(before, after):
    """FAIL_TO_PASS: passes after the reference patch and did not pass before (failed, errored, skipped, or did not
    run, for example when its file failed to import). PASS_TO_PASS: passes both before and after."""
    f2p = sorted(t for t, s in after.items() if passed(s) and not passed(before.get(t)))
    p2p = sorted(t for t, s in after.items() if passed(s) and passed(before.get(t)))
    return f2p, p2p


def rederive(tid, reason):
    """Recomputes a row's test lists from its saved derivation outputs after a correction of the derivation rule.
    The old row and any old eligibility record move to superseded/ with the reason; nothing is deleted. Returns the
    new row, or None when the lists do not change."""
    import glob
    old = json.loads((ROWS / f"{tid}.json").read_text())
    paths = [Path(glob.glob(str(h.RUNS / "logs/run_evaluation" / f"target-derive-{w}-{tid}-2*" / "derive" / tid /
                                "test_output.txt"))[0]) for w in ("before", "after")]
    parsed = statuses(paths, old["log_parser"])
    f2p, p2p = test_lists(parsed[str(paths[0])], parsed[str(paths[1])])
    if (f2p, p2p) == (old.get("FAIL_TO_PASS"), old.get("PASS_TO_PASS")):
        return None
    stamp = h.now()
    for src, dst in ((ROWS / f"{tid}.json", ROWS / "superseded" / f"{tid}.json"),
                     (h.ELIGIBILITY / f"{tid}.json", h.ELIGIBILITY / "superseded" / f"{tid}.json")):
        if src.exists():
            dst.parent.mkdir(exist_ok=True)
            src.rename(dst)
            save_new(dst.with_suffix(".reason.json"), dict(task_id=tid, superseded_at=stamp, reason=reason))
    row = dict(old, FAIL_TO_PASS=f2p, PASS_TO_PASS=p2p, status="derived" if f2p else "no FAIL_TO_PASS test",
               supersedes=dict(path=f"superseded/{tid}.json", reason=reason, at=stamp))
    row["derivation"] = dict(old.get("derivation") or {}, reason=None if f2p else "no FAIL_TO_PASS test")
    save_new(ROWS / f"{tid}.json", row)
    return row


def process(need=6, predicate=None):
    """Confirms and derives matching candidates in order_key order until `need` targets are eligible or the pool
    ends. Rows and outcomes are written once. A task without a FAIL_TO_PASS test, or without parsed results, is
    ineligible; an image build or harness failure is kept as an attempt and the task stays pending for a later run.
    Candidates after the last eligible one stay unchecked, because selection takes the first eligible tasks in order."""
    pool = load_pool()
    ROWS.mkdir(parents=True, exist_ok=True)
    build_base_image()
    results, rows = h.load_results(), load_rows()
    match = predicate or (lambda p: p["included"])
    earlier = []  # candidates before this one in order; only these can fill the first `need` eligible places
    for pr in sorted((p for p in pool["prs"] if match(p)), key=lambda p: p["order_key"]):
        if sum(1 for t in earlier if (results.get(t) or {}).get("status") == "eligible") >= need:
            break
        tid, stamp = pr["task_id"], h.now().replace(":", "").replace("-", "")[:15]
        earlier.append(tid)
        if tid in results:
            continue
        row = rows.get(tid)
        if row is None:
            row, checks = confirm(pr)
            if row is None:
                save_new(ROWS / f"{tid}.json", dict(task_id=tid, status="identity not confirmed", identity_checks=checks))
                print(tid, "identity not confirmed")
                continue
            image, row["version"] = build_image(row)
            if image is None:
                save_new(h.ELIGIBILITY / "attempts" / f"{tid}-{stamp}.json",
                         dict(task_id=tid, task_kind="upstream", status="harness_failure", checked_at=h.now(),
                              reasons=[f"image build failed; see {(IMAGES / (tid + '.build.log')).relative_to(ROOT)}"]))
                print(tid, "image build failed (attempt kept; task pending)")
                continue
            lists, reason, logs = derive(row, stamp)
            if reason and reason.startswith("harness failure"):
                save_new(h.ELIGIBILITY / "attempts" / f"{tid}-{stamp}.json",
                         dict(task_id=tid, task_kind="upstream", status="harness_failure", checked_at=h.now(),
                              reasons=[reason], logs=logs))
                print(tid, reason, "(attempt kept; task pending)")
                continue
            row.update(lists or {}, derivation=dict(reason=reason, logs=logs, image_id=image),
                       status="derived" if not reason else reason)
            save_new(ROWS / f"{tid}.json", row)
            rows[tid] = row
            if reason:
                rec = dict(record="paper2-eligibility/1", task_id=tid, task_kind="upstream", status="ineligible",
                           reasons=[f"derivation: {reason}"], checked_at=h.now(), derivation_logs=logs)
                save_new(h.ELIGIBILITY / f"{tid}.json", rec)
                results[tid] = rec
                print(tid, "ineligible:", reason)
                continue
        if row.get("status") != "derived":
            continue
        for rec in h.run_eligibility([row], "upstream", "target"):
            if rec["status"] != "harness_failure":
                results[tid] = rec
            print(tid, rec["status"], "; ".join(rec["reasons"]))


def load_rows():
    return {p.stem: json.loads(p.read_text()) for p in sorted(ROWS.glob("*.json"))}


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("retrieve")
    p = sub.add_parser("process")
    p.add_argument("--need", type=int, default=6)
    args = parser.parse_args(argv)
    if args.cmd == "retrieve":
        pool = retrieve()
        print(f"{pool['search_count']} merged pull requests; {pool['included']} meet the rule")
    else:
        process(args.need)


if __name__ == "__main__":
    main()

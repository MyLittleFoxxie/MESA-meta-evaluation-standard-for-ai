"""Run each valid independent check script on the agent's own patch.
Reads the protocol 6 records only. Writes results outside the repository.
For each task: SymPy at the base commit (downloaded as a tarball), then three trees:
base (check must fail), maintainers' fix (check must pass), agent patch."""
import json, os, sys, subprocess, tarfile, shutil, glob, time, urllib.request, pathlib
ROOT = pathlib.Path(os.environ["REPO"]); P6 = ROOT/"paper2/preparation/protocol-6"
OUT = pathlib.Path(os.environ.get("OUT", pathlib.Path.home()/"gapcheck")); CACHE = OUT/"cache"; CACHE.mkdir(parents=True, exist_ok=True)
RES = OUT/"results.json"
res = json.loads(RES.read_text()) if RES.exists() else {}
rows = json.loads((ROOT/"paper2/records/swe_bench_verified_sympy_rows.json").read_text())
rows = {r["instance_id"]: r for r in (rows if isinstance(rows, list) else rows.get("rows") or rows.values())}
for f in glob.glob(str(ROOT/"paper2/records/sympy_target_rows/*.json")):
    r = json.loads(open(f).read()); rows[r["instance_id"]] = r
sessions = {}
for d in sorted((P6/"sessions").iterdir()):
    if (d/"session.json").exists():
        s = json.loads((d/"session.json").read_text()); o = s["observation"]
        if s["record"]["phase"] in ("source", "target"):
            sessions[o["task_id"]] = dict(phase=s["record"]["phase"], dir=str(d), tests_resolved=o["tests_resolved"], resolved=o["resolved"], valid=o["valid"])
def run_check(tree, check, py):
    try:
        p = subprocess.run([py, str(check)], cwd=tree, capture_output=True, timeout=45, env={**os.environ, "PYTHONPATH": str(tree) + os.pathsep + os.environ.get("SHIM", ""), "PYTHONDONTWRITEBYTECODE": "1"})
        return p.returncode, (p.stdout.decode(errors="replace")[-300:] + p.stderr.decode(errors="replace")[-500:])
    except subprocess.TimeoutExpired:
        return "timeout", ""
def tree_for(sha):
    t = CACHE/(sha+".tar.gz")
    if not t.exists():
        urllib.request.urlretrieve("https://codeload.github.com/sympy/sympy/tar.gz/"+sha, t)
    d = OUT/"work"/sha
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
    with tarfile.open(t) as tf: tf.extractall(d)
    return next(d.iterdir())
def apply(tree, patch_text):
    p = subprocess.run(["patch", "-p1", "-s", "--no-backup-if-mismatch"], cwd=tree, input=patch_text.encode(), capture_output=True)
    return p.returncode, (p.stdout+p.stderr).decode(errors="replace")[-300:]
py = os.environ.get("PY", sys.executable); budget = float(os.environ.get("BUDGET", "140")); t0 = time.time()
todo = [t for t in sessions if t not in res or (os.environ.get("RETRY") and res[t].get("status") == os.environ.get("RETRY"))]
for task in todo:
    if time.time() - t0 > budget: break
    att = json.loads((P6/"audit_checks/b07-counterexamples"/task/"attempt.json").read_text())
    out = dict(phase=sessions[task]["phase"], outcome=att.get("outcome"), check_valid=bool((att.get("check") or {}).get("valid")), **{k: sessions[task][k] for k in ("tests_resolved", "resolved", "valid")}, py=py)
    if not out["check_valid"]:
        out["status"] = "no valid check"; res[task] = out; RES.write_text(json.dumps(res, indent=1)); continue
    check = P6/"audit_checks/b07-counterexamples"/task/"check.py"; row = rows[task]
    try:
        tree = tree_for(row["base_commit"])
        out["base"] = run_check(tree, check, py)
        rc, msg = apply(tree, row["patch"]); out["fix_apply"] = rc
        out["fix"] = run_check(tree, check, py)
        tree = tree_for(row["base_commit"])
        agent_patch = open(os.path.join(sessions[task]["dir"], "patch.diff")).read()
        if agent_patch.strip():
            rc, msg = apply(tree, agent_patch); out["agent_apply"] = rc
            out["agent"] = run_check(tree, check, py)
        else:
            out["agent"] = ["empty patch", ""]
        sane = out["base"][0] not in (0,) and out["fix"][0] == 0 and out["fix_apply"] == 0
        out["status"] = "ok" if sane else "environment differs"
        shutil.rmtree(OUT/"work", ignore_errors=True)
    except Exception as e:
        out["status"] = "error"; out["error"] = repr(e)[:300]
    res[task] = out; RES.write_text(json.dumps(res, indent=1))
import collections
print("done", len(res), "of", len(sessions), collections.Counter(v["status"] for v in res.values()))

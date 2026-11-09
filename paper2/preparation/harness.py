"""Eligibility checks and patch grading with the SWE-bench harness (swebench 5) in Docker.

The harness runs from a separate virtual environment (PAPER2_SWEBENCH_PYTHON) so the repository keeps no new
dependency. Nothing here calls a model. Results are written once and never replaced.

Eligibility of a task needs two harness runs on the task's hidden tests:
  baseline   the source left unchanged: every FAIL_TO_PASS test fails and every PASS_TO_PASS test passes;
  reference  the reference patch: every FAIL_TO_PASS and PASS_TO_PASS test passes.
A missing report (image, environment, or harness failure) is a harness failure: it is kept as an attempt and
the task stays pending.
"""
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from paper2.preparation.study_controls import order_key, save_new  # noqa: E402

PYTHON = os.environ.get("PAPER2_SWEBENCH_PYTHON", str(Path.home() / ".venvs/paper2-swebench/bin/python"))
BASE = ROOT / "paper2/preparation/protocol-4"
RUNS = BASE / "harness"
ELIGIBILITY = BASE / "eligibility"
# shortcut: the harness skips empty patches, so the baseline adds one marker file outside the package and leaves
# the source unchanged; replace it if the harness gains a run mode without a patch.
BASELINE_PATCH = ("diff --git a/.paper2_baseline b/.paper2_baseline\nnew file mode 100644\n--- /dev/null\n"
                  "+++ b/.paper2_baseline\n@@ -0,0 +1 @@\n+baseline check: source unchanged\n")
LOG_FILES = ("report.json", "test_output.txt", "run_instance.log", "patch.diff")


def now():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def harness_version():
    out = subprocess.run([PYTHON, "-c", "import swebench;print(swebench.__version__)"], capture_output=True, text=True)
    return out.stdout.strip() or None


def docker_server():
    out = subprocess.run(["docker", "version", "--format", "{{.Server.Version}} {{.Server.Os}}/{{.Server.Arch}}"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError("Docker daemon is not reachable; start Docker Desktop first")
    return out.stdout.strip()


def image_id(image):
    out = subprocess.run(["docker", "image", "inspect", "--format", "{{.Id}}", image], capture_output=True, text=True)
    return out.stdout.strip() or None


def ensure_image(image):
    """SWE-bench publishes amd64 images only; the harness pulls for the host platform (arm64) and fails, so the
    image is pulled for amd64 first and runs under emulation."""
    if image and not image_id(image):
        subprocess.run(["docker", "pull", "--platform", "linux/amd64", image], capture_output=True, text=True)
    return image_id(image) if image else None


def run_harness(rows, patches, run_id, model="paper2", max_workers=2):
    """rows: dataset rows; patches: {instance_id: patch text}. Returns {instance_id: dict(report, logs)}.
    A run identifier is used once; the harness skips instances that already have a report under it."""
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    dataset = run_dir / "dataset.json"
    dataset.write_text(json.dumps([r for r in rows if r["instance_id"] in patches], indent=1))
    preds = run_dir / "predictions.json"
    preds.write_text(json.dumps([dict(instance_id=i, model_name_or_path=model, model_patch=p) for i, p in patches.items()]))
    with (run_dir / "harness.log").open("w") as log:
        subprocess.run([PYTHON, "-m", "swebench.harness.run_evaluation", "-d", str(dataset), "-p", str(preds),
                        "-id", run_id, "--max_workers", str(max_workers), "--report_dir", str(run_dir)],
                       cwd=RUNS, stdout=log, stderr=subprocess.STDOUT)
    out = {}
    for iid in patches:
        folder = RUNS / "logs/run_evaluation" / run_id / model / iid
        report = folder / "report.json"
        out[iid] = dict(report=json.loads(report.read_text())[iid] if report.exists() else None,
                        logs={str(p.relative_to(ROOT)): sha256(p) for p in (folder / f for f in LOG_FILES) if p.exists()})
    return out


def check(report, expect_fail_to_pass):
    """Returns a list of problems; empty means the run shows what the check expects."""
    if report is None:
        return ["no report (image, environment, or harness failure)"]
    if not report.get("patch_successfully_applied"):
        return ["patch did not apply"]
    status, problems = report.get("tests_status") or {}, []
    f2p, p2p = status.get("FAIL_TO_PASS", {}), status.get("PASS_TO_PASS", {})
    if expect_fail_to_pass == "fail" and f2p.get("success"):
        problems.append(f"FAIL_TO_PASS tests already pass: {f2p['success']}")
    if expect_fail_to_pass == "pass" and f2p.get("failure"):
        problems.append(f"FAIL_TO_PASS tests fail: {f2p['failure']}")
    if p2p.get("failure"):
        problems.append(f"PASS_TO_PASS tests fail: {p2p['failure']}")
    return problems


def eligibility_record(row, kind, baseline, reference, run_ids, versions):
    """A missing report is a harness failure, not a property of the task: the record is kept as an attempt and the
    task stays pending."""
    problems = [f"baseline: {p}" for p in check(baseline["report"], "fail")] + \
               [f"reference: {p}" for p in check(reference["report"], "pass")]
    failed = baseline["report"] is None or reference["report"] is None
    return dict(record="paper2-eligibility/1", task_id=row["instance_id"], task_kind=kind,
                status="harness_failure" if failed else "ineligible" if problems else "eligible",
                reasons=problems, checked_at=now(),
                base_commit=row["base_commit"], image=row.get("image"), image_id=image_id(row["image"]) if row.get("image") else None,
                runs=run_ids, harness=versions,
                baseline=dict(tests_status=(baseline["report"] or {}).get("tests_status"), logs=baseline["logs"]),
                reference=dict(tests_status=(reference["report"] or {}).get("tests_status"), logs=reference["logs"],
                               patch_sha256=hashlib.sha256(row["patch"].encode()).hexdigest()))


def run_eligibility(rows, kind, label, max_workers=2):
    """Checks every row without a saved result, in order_key order, and writes each result once."""
    versions = dict(swebench=harness_version(), docker=docker_server())
    todo = sorted((r for r in rows if not (ELIGIBILITY / f"{r['instance_id']}.json").exists()),
                  key=lambda r: order_key(r["instance_id"]))
    if not todo:
        return []
    for r in todo:
        ensure_image(r.get("image"))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    runs = dict(baseline=f"{label}-baseline-{stamp}", reference=f"{label}-reference-{stamp}")
    base = run_harness(todo, {r["instance_id"]: BASELINE_PATCH for r in todo}, runs["baseline"], max_workers=max_workers)
    ref = run_harness(todo, {r["instance_id"]: r["patch"] for r in todo}, runs["reference"], max_workers=max_workers)
    written = []
    for r in todo:
        rec = eligibility_record(r, kind, base[r["instance_id"]], ref[r["instance_id"]], runs, versions)
        name = f"{r['instance_id']}.json" if rec["status"] != "harness_failure" else f"attempts/{r['instance_id']}-{stamp}.json"
        save_new(ELIGIBILITY / name, rec)
        written.append(rec)
    return written


def load_results():
    return {p.stem: json.loads(p.read_text()) for p in sorted(ELIGIBILITY.glob("*.json"))}


def grade(row, patch_text, run_id):
    """Grades one session patch on the task's hidden tests. Returns resolved (True, False, or None when no
    report exists) with the report and log hashes."""
    res = run_harness([row], {row["instance_id"]: patch_text}, run_id, model="session")[row["instance_id"]]
    report = res["report"]
    return dict(resolved=None if report is None else bool(report.get("resolved")), report=report, logs=res["logs"],
                harness=dict(swebench=harness_version(), docker=docker_server()), image=row.get("image"))


def image_history(row):
    """B28 auditor check: commits reachable in a published image beyond the base commit, and the files they change.
    Only the harness's own setup commit (setup@swebench.com) is expected; any other commit could reveal the fix."""
    script = (f"cd /testbed && git log --all --format='%H|%ae|%s' --not {row['base_commit']} && echo '--' && "
              f"git diff --stat {row['base_commit']} HEAD | tail -1")
    out = subprocess.run(["docker", "run", "--rm", "--platform", "linux/amd64", "--network", "none", row["image"],
                          "bash", "-c", script], capture_output=True, text=True)
    log, _, stat = out.stdout.partition("--\n")
    commits = [dict(zip(("sha", "email", "subject"), line.split("|", 2))) for line in log.splitlines() if line]
    return dict(task_id=row["instance_id"], image=row["image"], image_id=image_id(row["image"]), returncode=out.returncode,
                commits_after_base=commits, files_changed_since_base=stat.strip(),
                other_commits=[c for c in commits if c.get("email") != "setup@swebench.com"])


def image_check(rows):
    results = [image_history(r) for r in rows]
    record = dict(record="paper2-audit-check/1", check="B28 published image history", checked_at=now(),
                  procedure="For each image, list commits reachable beyond the task's base commit (git log --all "
                            "--not base) and the files changed between the base commit and HEAD, with no network.",
                  images=len(results), failed_runs=sum(r["returncode"] != 0 for r in results),
                  images_with_other_commits=[r["task_id"] for r in results if r["other_commits"]],
                  images_with_changed_files=[r["task_id"] for r in results if r["files_changed_since_base"]],
                  results=results)
    save_new(BASE / "audit_checks" / "b28-image-history.json", record)
    return record


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("eligibility", help="check source pool tasks without a saved result")
    e.add_argument("--limit", type=int, help="check only the first N unchecked tasks in order")
    e.add_argument("--workers", type=int, default=2)
    sub.add_parser("image-check", help="B28 auditor check of the published source images")
    args = parser.parse_args(argv)
    from tools.extract_swe_bench_verified import load_sympy_rows
    if args.cmd == "image-check":
        rec = image_check(load_sympy_rows()["rows"])
        print(rec["images"], "images;", rec["failed_runs"], "failed runs; other commits:", rec["images_with_other_commits"],
              "; changed files:", rec["images_with_changed_files"])
        return
    rows = sorted(load_sympy_rows()["rows"], key=lambda r: order_key(r["instance_id"]))
    rows = [r for r in rows if not (ELIGIBILITY / f"{r['instance_id']}.json").exists()][:args.limit]
    for rec in run_eligibility(rows, "upstream", "source", args.workers):
        print(rec["task_id"], rec["status"], "; ".join(rec["reasons"]))


if __name__ == "__main__":
    main()

"""B07 cheating attempts for protocol 5 of Paper 2. Nothing here runs a coding agent.

For one source task, Claude Sonnet 5.5 writes into audit_checks/b07-counterexamples/<task>/, from the issue text and
the real fix only:
  behaviors.md       the behaviors the issue asks for;
  check.py           an independent check of those behaviors: exit code 0 when every behavior holds;
  candidate-N.diff   at most three cheating patches, each meant to pass the task's hidden tests while breaking a
                     listed behavior; or no-candidate.md, saying why no such patch could be written.
`run` then checks the check (it must fail on the code before the fix and pass with the real fix), grades each
candidate on the hidden tests with the SWE-bench harness, runs the check on it, and writes one log per candidate and
attempt.json, once. A defect is demonstrated when the check is valid, the harness resolves a candidate, and the check
fails on it; `evidence.counterexample_demonstrated` reads the same fields from the B07 rating form.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from paper2.method.evidence import counterexample_demonstrated, sha256_file  # noqa: E402
from paper2.preparation import harness as h  # noqa: E402
from paper2.preparation import study_controls as s  # noqa: E402

RECORDS = s.PROTOCOL / "audit_checks" / "b07-counterexamples"
MAX_CANDIDATES = 3
ENV = "source /opt/miniconda3/bin/activate && conda activate testbed && cd /testbed"
AUTHOR = "Claude Sonnet 5.5 (Claude Code subagents), at the author's request"


def _rel(path):
    path = Path(path).resolve()
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def run_check(image, patch_text, check_path):
    """Runs check.py in the task image without network, after applying patch_text (none for the code before the
    fix). Returns the exit code and the end of the output."""
    with tempfile.TemporaryDirectory() as d:
        Path(d, "patch.diff").write_text(patch_text)
        shutil.copy(check_path, Path(d, "check.py"))
        apply = "git apply /audit/patch.diff && " if patch_text.strip() else ""
        out = subprocess.run(["docker", "run", "--rm", "--platform", "linux/amd64", "--network", "none",
                              "-v", f"{d}:/audit:ro", image, "bash", "-c", f"{ENV} && {apply}python /audit/check.py"],
                             capture_output=True, text=True, timeout=900)
    return dict(exit_code=out.returncode, output=(out.stdout + out.stderr)[-20000:])


def run(task_id, row, folder=None):
    folder = Path(folder or RECORDS / task_id)
    if (folder / "attempt.json").exists():
        raise FileExistsError(f"{task_id} already has an attempt; attempts are written once")
    check, behaviors = folder / "check.py", folder / "behaviors.md"
    candidates = sorted(folder.glob("candidate-*.diff"))
    if not check.exists() or not behaviors.exists():
        raise ValueError("An attempt needs behaviors.md and check.py")
    if len(candidates) > MAX_CANDIDATES:
        raise ValueError(f"At most {MAX_CANDIDATES} candidates")
    if not candidates and not (folder / "no-candidate.md").exists():
        raise ValueError("Without a candidate, no-candidate.md must say why")
    stamp = h.now().replace(":", "").replace("-", "")[:15]
    before, reference = run_check(row["image"], "", check), run_check(row["image"], row["patch"], check)
    valid = before["exit_code"] != 0 and reference["exit_code"] == 0
    graded = []
    for i, cand in enumerate(candidates, 1):
        patch = cand.read_text()
        graded.append((cand, h.grade(row, patch, f"b07-{task_id}-{i}-{stamp}"), run_check(row["image"], patch, check)))
    failed = [cand.name for cand, grading, _ in graded if grading["resolved"] is None]
    if failed:  # a harness failure is not an attempt outcome; nothing is written, so the run can be repeated
        raise RuntimeError(f"{task_id}: the harness gave no report for {', '.join(failed)}; nothing recorded")
    results = []
    for cand, grading, checked in graded:
        log = folder / f"{cand.stem}.log.json"
        report = grading.get("report") or {}
        s.save_new(log, dict(task_id=task_id, candidate=cand.name, harness_resolved=grading["resolved"],
                             tests_status=report.get("tests_status"), harness_logs=grading.get("logs"), check=checked))
        cx = dict(task_id=task_id, patch=dict(path=_rel(cand), sha256=sha256_file(cand)),
                  command=["swebench harness on FAIL_TO_PASS and PASS_TO_PASS", "python check.py"],
                  result=dict(oracle_outcome={True: "pass", False: "fail"}.get(grading["resolved"], "error"),
                              behavior_check="pass" if checked["exit_code"] == 0 else "fail",
                              log=dict(path=_rel(log), sha256=sha256_file(log))))
        results.append(dict(cx, demonstrated=valid and counterexample_demonstrated(cx)))
    outcome = ("check invalid" if not valid else "defect demonstrated" if any(r["demonstrated"] for r in results)
               else "no candidate" if not candidates else "no defect demonstrated")
    record = dict(record="paper2-b07-attempt/1", task_id=task_id, attempted_by=AUTHOR, checked_at=h.now(),
                  behaviors=dict(path=_rel(behaviors), sha256=sha256_file(behaviors)),
                  check=dict(path=_rel(check), sha256=sha256_file(check),
                             before_fix=dict(exit_code=before["exit_code"]), real_fix=dict(exit_code=reference["exit_code"]),
                             valid=valid),
                  candidates=results, outcome=outcome)
    s.save_new(folder / "attempt.json", record)
    return record


SCORING_RECORDS = s.PROTOCOL / "audit_checks" / "b28a-scoring-check"


def scoring_check(task_id, row, folder=None):
    """B28a check run by the reviewer: can a patch that changes only the test-running files (bin/test, runtests.py,
    conftest.py, ...) make the harness grade a task resolved without fixing it? Grades each candidate-*.diff in the
    task's folder and writes check.json once. A harness failure writes nothing, so the check can be repeated."""
    folder = Path(folder or SCORING_RECORDS / task_id)
    if (folder / "check.json").exists():
        raise FileExistsError(f"{task_id} already has a grading check; checks are written once")
    candidates = sorted(folder.glob("candidate-*.diff"))
    if not candidates or len(candidates) > MAX_CANDIDATES:
        raise ValueError(f"A grading check needs 1 to {MAX_CANDIDATES} candidates")
    for cand in candidates:
        patch = cand.read_text()
        files = re.findall(r"^diff --git a/(\S+) b/(\S+)$", patch, re.M)
        changed = sorted({f for pair in files for f in pair})
        if not changed or set(changed) - set(s.scoring_files(patch)):
            raise ValueError(f"{cand.name} must change only test-running files: {changed}")
    stamp = h.now().replace(":", "").replace("-", "")[:15]
    graded = [(cand, h.grade(row, cand.read_text(), f"b28a-{task_id}-{i}-{stamp}")) for i, cand in enumerate(candidates, 1)]
    failed = [cand.name for cand, grading in graded if grading["resolved"] is None]
    if failed:
        raise RuntimeError(f"{task_id}: the harness gave no report for {', '.join(failed)}; nothing recorded")
    results = []
    for cand, grading in graded:
        report = grading.get("report") or {}
        results.append(dict(patch=dict(path=_rel(cand), sha256=sha256_file(cand)), files=s.scoring_files(cand.read_text()),
                            harness_resolved=grading["resolved"], tests_status=report.get("tests_status"),
                            harness_logs=grading.get("logs"), harness=grading.get("harness")))
    record = dict(record="paper2-b28a-grading-check/1", task_id=task_id, checked_by=AUTHOR, checked_at=h.now(),
                  image=row.get("image"), candidates=results,
                  outcome="grading altered" if any(r["harness_resolved"] for r in results) else "grading held")
    s.save_new(folder / "check.json", record)
    return record


def summary(folder=RECORDS):
    """Outcome per task, and for each demonstrated defect the entry the B07 rating form lists under task_defects."""
    out = {}
    for path in sorted(Path(folder).glob("*/attempt.json")):
        rec = json.loads(path.read_text())
        shown = next((c for c in rec["candidates"] if c["demonstrated"]), None)
        cx = {k: v for k, v in shown.items() if k != "demonstrated"} if shown else None
        out[rec["task_id"]] = dict(outcome=rec["outcome"], attempt=_rel(path), sha256=sha256_file(path),
                                   task_defect=dict(task_id=rec["task_id"], counterexample=cx,
                                                    summary="tests accept a patch that breaks a behavior the issue asks for",
                                                    evidence_location=cx["result"]["log"]["path"],
                                                    artifacts={_rel(path): sha256_file(path)}) if cx else None)
    return out


def main(argv=None):
    import argparse
    from paper2.preparation.sessions import rows_by_id
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run").add_argument("task")
    sub.add_parser("summary")
    sub.add_parser("scoring-check").add_argument("task")
    a = parser.parse_args(argv)
    if a.cmd == "run":
        rec = run(a.task, rows_by_id()[a.task])
        print(a.task, rec["outcome"])
    elif a.cmd == "scoring-check":
        rec = scoring_check(a.task, rows_by_id()[a.task])
        print(a.task, rec["outcome"])
    else:
        print(json.dumps(summary(), indent=2))


if __name__ == "__main__":
    main()

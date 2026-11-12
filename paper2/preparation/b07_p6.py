"""Protocol 6 B07 cross-family incomplete-patch and verification-check pipeline (P6-5, P6-7).

Separation of roles:
- Stage 1 (Model Family A: gpt-6.1-sol via Codex CLI) writes behaviors.md and up to three candidate incomplete
  patches (or no-candidate.md) from the issue text, reference patch, and test patch inside a clean base checkout.
- Stage 2 (Model Family B: gemini-3.8-flash-medium via Antigravity CLI) runs in a separate clean checkout without
  access to candidate patches and writes an independent check.py strictly from the issue text, behaviors.md, and
  reference fix.
- Stage 3 runs counterexamples.run inside Docker with --network none to verify before_fix != 0, real_fix == 0,
  oracle grading on each candidate, and check.py outcomes, writing attempt.json and refreshing blind_b07_sheet.json.
"""
import argparse
import ast
import concurrent.futures
from contextlib import contextmanager
import json
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from paper2.preparation import counterexamples as cx  # noqa: E402
from paper2.preparation import harness as h  # noqa: E402
from paper2.preparation import protocol6 as p6  # noqa: E402
from paper2.preparation import sessions as ss  # noqa: E402
from paper2.preparation import study_controls as s  # noqa: E402

RECORDS = p6.PROTOCOL / "audit_checks" / "b07-counterexamples"
BLIND_SHEET = p6.PROTOCOL / "blind_b07_sheet.json"
PRIVATE_LABELS = p6.PROTOCOL / "audit_checks" / "b07_model_labels.json"
STAGE1_MODEL = "gpt-6.1-sol"
STAGE2_MODEL = "gemini-3.8-flash-medium"
B07_P6_AUTHOR = (
    f"Stage 1 (candidates & behaviors): {STAGE1_MODEL} (Codex CLI); "
    f"Stage 2 (verification check.py): {STAGE2_MODEL} (Antigravity CLI), blind to candidates"
)


def _cli_path(tool: str) -> str:
    found = shutil.which(tool)
    if not found:
        raise RuntimeError(f"CLI binary not found on PATH: {tool}")
    return found


@contextmanager
def _work_temp_dir() -> Iterator[Path]:
    """Create a temp workspace directory inheriting parent ACLs so sandbox subprocesses stay readable."""
    base = Path(tempfile.gettempdir()) / "p6_b07_ws"
    base.mkdir(parents=True, exist_ok=True)
    path = base / f"w_{uuid.uuid4().hex[:12]}"
    path.mkdir(parents=True, exist_ok=True)
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)


def checkout_clean(base_commit: str, dest: Path, mirror: Optional[Path] = None) -> Path:
    """Create a fast detached SymPy checkout at base_commit with no future refs."""
    mirror_path = Path(mirror or ss.ensure_mirror())
    dest = Path(dest)
    subprocess.run(["git", "clone", "-q", "--shared", str(mirror_path), str(dest)], check=True)
    subprocess.run(["git", "-C", str(dest), "checkout", "-q", "--detach", base_commit], check=True)
    subprocess.run(["git", "-C", str(dest), "remote", "remove", "origin"], check=True)
    return dest


def _sanitize_behaviors(text: str) -> str:
    """Strip any accidental candidate filenames from behaviors.md before Stage 2 sees it."""
    lines = []
    for line in (text or "").splitlines():
        if re.search(r"candidate-\d+\.diff", line, re.I):
            continue
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def normalize_diff(diff_text: str) -> str:
    """Normalize line endings to LF and guarantee a trailing newline without stripping trailing space context lines."""
    norm = (diff_text or "").replace("\r\n", "\n")
    if norm and not norm.endswith("\n"):
        norm += "\n"
    return norm


def validate_diff_applies(ws: Path, diff_text: str) -> bool:
    """True when diff_text is a non-empty unified diff that cleanly applies to ws."""
    if not (diff_text or "").strip() or "diff --git " not in diff_text:
        return False
    with tempfile.NamedTemporaryFile("w", suffix=".diff", encoding="utf-8", newline="\n", delete=False) as tf:
        tf.write(diff_text)
        tmp_path = Path(tf.name)
    try:
        res = subprocess.run(
            ["git", "-C", str(ws), "apply", "--check", str(tmp_path)],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        return res.returncode == 0
    finally:
        tmp_path.unlink(missing_ok=True)


def stage1_prompt(task_id: str, row: Dict[str, Any]) -> str:
    """Build Stage 1 prompt (Model Family A: behaviors.md + candidate-N.diff incomplete patches)."""
    return "\n".join([
        f"You are auditing benchmark task `{task_id}` (`sympy/sympy` at base commit `{row['base_commit']}`) for criterion B07 (test suite completeness).",
        "The current working directory is a clean SymPy checkout at the base commit.",
        "",
        "<issue>",
        (row.get("problem_statement") or "").strip(),
        "</issue>",
        "",
        "<reference_patch>",
        (row.get("patch") or "").strip(),
        "</reference_patch>",
        "",
        "<test_patch>",
        (row.get("test_patch") or "").strip(),
        "</test_patch>",
        "",
        "Hidden tests checked by the harness:",
        f"- FAIL_TO_PASS: {json.dumps(row.get('FAIL_TO_PASS') or [])}",
        f"- PASS_TO_PASS: {json.dumps(row.get('PASS_TO_PASS') or [])}",
        "",
        "Instructions (write outputs ONLY inside `_p6_stage1/`, NEVER create `check.py` or `b07_check.py`):",
        "1. Create `_p6_stage1/behaviors.md`: a concise bulleted list of concrete behaviors requested in `<issue>`. Do NOT mention any candidate diffs or patches.",
        "2. Inspect `<test_patch>` vs `<reference_patch>` vs `<issue>`. Construct 1 to 3 minimal incomplete patches `_p6_stage1/candidate-1.diff` (and `candidate-2.diff`, `candidate-3.diff` if distinct gaps exist) that:",
        "   - apply cleanly to this base commit,",
        "   - are designed to PASS all tests in `FAIL_TO_PASS` and `PASS_TO_PASS`, yet",
        "   - omit, hardcode, mishandle an edge case, or break a concrete behavior stated in `<issue>`.",
        "3. Generate each diff reliably by editing the repo files, running `git diff > _p6_stage1/candidate-N.diff`, then resetting with `git checkout -- .` before writing the next candidate.",
        "4. IMPORTANT environment rule: Host Python does NOT have `mpmath` or `pytest` installed, and Docker Stage 3 grades every candidate against the real test suite automatically. NEVER execute SymPy or pytest on the host, and NEVER write helper scripts, runners, or stubs into `_p6_stage1/`; put ONLY `behaviors.md` and `candidate-N.diff` (or `no-candidate.md`) inside `_p6_stage1/`.",
        "5. If every stated behavior is thoroughly enforced by `<test_patch>`, write `_p6_stage1/no-candidate.md` explaining why no incomplete candidate could be constructed.",
        "6. Ensure the repository working tree is clean (`git checkout -- .`) before finishing.",
    ])


def run_stage1_codex(task_id: str, row: Dict[str, Any], out_dir: Path, timeout: int = 240) -> None:
    """Execute Stage 1 via Codex CLI in an isolated checkout and copy validated outputs."""
    out_dir = Path(out_dir)
    if (out_dir / "behaviors.md").exists() and (
        list(out_dir.glob("candidate-*.diff")) or (out_dir / "no-candidate.md").exists()
    ):
        return
    codex_bin = _cli_path("codex")
    with _work_temp_dir() as tmp:
        ws = checkout_clean(row["base_commit"], tmp / "ws")
        stage_dir = ws / "_p6_stage1"
        stage_dir.mkdir(parents=True, exist_ok=True)
        out_msg = tmp / "stage1_last.txt"
        cmd = [
            codex_bin, "exec", "--skip-git-repo-check", "--ignore-rules", "--model", STAGE1_MODEL,
            "-c", "model_reasoning_effort=medium", "-c", "web_search=disabled", "-c", "features.apps=false",
            "--sandbox", "workspace-write", "--ephemeral", "-C", str(ws), "-o", str(out_msg), "-",
        ]
        res = subprocess.run(
            cmd, cwd=str(ws), input=stage1_prompt(task_id, row),
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout + 30,
        )
        if res.returncode != 0:
            raise RuntimeError(f"Stage 1 codex failed for {task_id} ({res.returncode}): {(res.stderr or res.stdout)[-400:]}")
        beh_src = stage_dir / "behaviors.md"
        if not beh_src.exists():
            raise RuntimeError(f"Stage 1 did not write _p6_stage1/behaviors.md for {task_id}")
        subprocess.run(["git", "-C", str(ws), "checkout", "--", "."], check=True)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "behaviors.md").write_bytes(_sanitize_behaviors(beh_src.read_text(encoding="utf-8")).replace("\r\n", "\n").encode("utf-8"))
        kept = 0
        for cand_path in sorted(stage_dir.glob("candidate-*.diff"))[: cx.MAX_CANDIDATES]:
            diff_text = normalize_diff(cand_path.read_text(encoding="utf-8", errors="replace"))
            if validate_diff_applies(ws, diff_text):
                kept += 1
                (out_dir / f"candidate-{kept}.diff").write_bytes(diff_text.replace("\r\n", "\n").encode("utf-8"))
        if kept == 0:
            nc = stage_dir / "no-candidate.md"
            reason = nc.read_text(encoding="utf-8") if nc.exists() else "No valid applying incomplete candidate generated in Stage 1."
            (out_dir / "no-candidate.md").write_bytes((reason.strip() + "\n").replace("\r\n", "\n").encode("utf-8"))


def stage2_prompt(task_id: str, row: Dict[str, Any], behaviors_text: str) -> str:
    """Build Stage 2 prompt (Model Family B: write b07_check.py strictly blind to candidate diffs)."""
    return "\n".join([
        f"You are an independent verification test writer (Model Family B) for `{task_id}` (`sympy/sympy` at `{row['base_commit']}`).",
        "Write a single standalone Python script named `b07_check.py` in the root of this workspace.",
        "",
        "<issue>",
        (row.get("problem_statement") or "").strip(),
        "</issue>",
        "",
        "<behaviors_requested>",
        behaviors_text.strip(),
        "</behaviors_requested>",
        "",
        "<reference_patch>",
        (row.get("patch") or "").strip(),
        "</reference_patch>",
        "",
        "Strict requirements for `b07_check.py`:",
        "1. It will be invoked inside a Linux Docker container after either (a) no patch (`base_commit`) or (b) a candidate/reference patch via `python /audit/check.py` (keep assertions Linux-compatible; do not assume Windows paths or `os.path.normcase` lowercasing).",
        "2. Exit with code 0 ONLY if EVERY behavior requested in `<issue>` and `<behaviors_requested>` holds; exit with non-zero (e.g., via `AssertionError` or `sys.exit(1)`) if ANY stated behavior fails.",
        "3. It MUST fail (`exit_code != 0`) on unpatched `base_commit` and MUST pass (`exit_code == 0`) once `<reference_patch>` is applied.",
        "4. IMPORTANT grounding rule: Inspect at most 2-3 narrow line ranges around the `@@` hunks in `<reference_patch>` (do not run directory listings or scan full files) and verify EVERY assertion in `b07_check.py` against the actual functions, APIs, and code paths changed in `<reference_patch>`. Do NOT add assertions targeting unrelated or unedited subsystems (for example new assumptions `ask(Q....)` when `<reference_patch>` only edits old assumptions) that `<reference_patch>` would fail!",
        "5. Rely only on Python stdlib + `sympy` imports from `/testbed` (do NOT spawn pytest subprocesses or use network/external packages beyond sympy/mpmath).",
        "6. IMPORTANT environment rule: Host Python does NOT have `mpmath` installed and Stage 3 Docker executes `/audit/check.py` automatically, so do NOT try running `sympy`, `pytest`, or `dir`/`ls` on the host.",
        "7. Write `b07_check.py` cleanly into the workspace root promptly using `write_to_file`.",
    ])


def _prepare_agy_workspace(ws: Path) -> None:
    agents_dir = ws / ".agents" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p6.PROTOCOL / "agy-agent.md", agents_dir / "local.md")
    shutil.copyfile(p6.PROTOCOL / "agy-gate.py", ws / ".agents" / "gate.py")
    hooks = json.loads((p6.PROTOCOL / "agy-hooks.json").read_text(encoding="utf-8"))
    py_exe = str(Path(sys.executable))
    py_cmd = f'"{py_exe}"' if " " in py_exe else py_exe
    for block in hooks.values():
        for entry in block.get("PreToolUse") or []:
            for hk in entry.get("hooks") or []:
                if hk.get("type") == "command":
                    hk["command"] = f"{py_cmd} gate.py"
    (ws / ".agents" / "hooks.json").write_text(json.dumps(hooks, indent=2) + "\n", encoding="utf-8")
    excl = ws / ".git" / "info" / "exclude"
    excl.parent.mkdir(parents=True, exist_ok=True)
    existing = excl.read_text(encoding="utf-8") if excl.exists() else ""
    (excl).write_text(existing + "\n.agents/\nb07_check.py\n", encoding="utf-8")


def run_stage2_agy(task_id: str, row: Dict[str, Any], out_dir: Path, timeout: int = 300, attempts: int = 2) -> None:
    """Execute Stage 2 via Antigravity CLI (gemini-3.8-flash-medium) blind to all candidate patches."""
    out_dir = Path(out_dir)
    if (out_dir / "check.py").exists():
        return
    behaviors_path = out_dir / "behaviors.md"
    if not behaviors_path.exists():
        raise ValueError(f"Stage 2 requires behaviors.md in {out_dir}")
    behaviors_text = behaviors_path.read_text(encoding="utf-8")
    agy_bin = _cli_path("agy")
    settings_path = p6.PROTOCOL / "agy-session-settings.json"
    last_err: Optional[Exception] = None
    for _ in range(max(1, attempts)):
        with _work_temp_dir() as tmp:
            ws = checkout_clean(row["base_commit"], tmp / "ws")
            _prepare_agy_workspace(ws)
            prompt_text = stage2_prompt(task_id, row, behaviors_text)
            if len(prompt_text) > 20000:
                (ws / "b07_stage2_prompt.md").write_bytes(prompt_text.replace("\r\n", "\n").encode("utf-8"))
                cli_prompt = (
                    "Read b07_stage2_prompt.md in the workspace root (you may read it in chunks if large) "
                    "and follow all instructions in it to create b07_check.py."
                )
            else:
                cli_prompt = prompt_text
            cmd = [
                agy_bin, "--model", STAGE2_MODEL, "--effort", "medium", "--sandbox",
                "--mode", "accept-edits", "--settings", str(settings_path), "--agent", "local",
                "--disable-slash-commands", "--new-project", "--output-format", "stream-json",
                "--print-timeout", f"{timeout}s", "-p", cli_prompt,
            ]
            try:
                res = subprocess.run(
                    cmd, cwd=str(ws), stdin=subprocess.DEVNULL, capture_output=True,
                    text=True, encoding="utf-8", errors="replace", timeout=timeout + 30,
                )
            except subprocess.TimeoutExpired as exc:
                last_err = exc
                continue
            if res.returncode != 0:
                last_err = RuntimeError(f"Stage 2 agy failed for {task_id} ({res.returncode}): {(res.stderr or res.stdout)[-400:]}")
                continue
            check_src = ws / "b07_check.py"
            if not check_src.exists():
                last_err = RuntimeError(f"Stage 2 did not create b07_check.py for {task_id}")
                continue
            code = check_src.read_text(encoding="utf-8")
            try:
                ast.parse(code)
            except SyntaxError as exc:
                last_err = RuntimeError(f"Stage 2 check.py syntax error for {task_id}: {exc}")
                continue
            (out_dir / "check.py").write_bytes((code.rstrip() + "\n").replace("\r\n", "\n").encode("utf-8"))
            return
    raise RuntimeError(str(last_err))


def _ensure_image(image: str) -> None:
    if h.image_id(image) is not None:
        return
    if str(image).startswith("paper2/"):
        raise RuntimeError(f"Missing locally built target image {image}")
    subprocess.run(["docker", "pull", "--platform", "linux/amd64", image], check=True)


def stage3_verify(
    task_id: str,
    row: Dict[str, Any],
    out_dir: Path,
    cleanup_source_images: bool = True,
    min_free_gb: float = 5.5,
) -> Dict[str, Any]:
    """Run Docker verification on candidates + check.py and guard host disk budget."""
    out_dir = Path(out_dir)
    attempt_path = out_dir / "attempt.json"
    if attempt_path.exists():
        return json.loads(attempt_path.read_text(encoding="utf-8"))
    _ensure_image(row["image"])
    rec = cx.run(task_id, row, folder=out_dir, author=B07_P6_AUTHOR)
    if cleanup_source_images and str(row["image"]).startswith("swebench/"):
        free_gb = shutil.disk_usage(ROOT).free / 1e9
        if free_gb < min_free_gb:
            subprocess.run(["docker", "rmi", "-f", row["image"]], capture_output=True)
    return rec


def update_blind_b07_sheet(
    manifest_path: Optional[Path] = None,
    records_dir: Path = RECORDS,
    sheet_path: Path = BLIND_SHEET,
    private_labels_path: Path = PRIVATE_LABELS,
    task_ids: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Populate blind_b07_sheet.json with issue excerpt + claimed behavior for passing incomplete patches."""
    if task_ids is not None:
        ordered_ids = list(task_ids)
    else:
        mpath = Path(manifest_path or (p6.PROTOCOL / "study_manifest.json"))
        manifest = json.loads(mpath.read_text(encoding="utf-8"))
        selected = manifest.get("selected") or {}
        planned = (manifest.get("selection") or {}).get("planned") or {}
        ordered_ids = list(selected.get("source") or planned.get("source") or []) + list(
            selected.get("target") or planned.get("target") or []
        )
        if manifest_path is None and not (selected.get("source") or selected.get("target")):
            seen = set(ordered_ids)
            rdir = Path(records_dir)
            if rdir.exists():
                extra = sorted(d.name for d in rdir.iterdir() if d.is_dir() and (d / "attempt.json").exists() and d.name not in seen)
                ordered_ids.extend(extra)
    rows = ss.rows_by_id()
    existing_items: Dict[str, Dict[str, Any]] = {}
    if Path(sheet_path).exists():
        prev = json.loads(Path(sheet_path).read_text(encoding="utf-8"))
        for item in prev.get("items") or []:
            existing_items[item["task_id"]] = item

    passing_cands: Dict[str, Dict[str, Any]] = {}
    private_labels: Dict[str, Any] = {}
    for tid in ordered_ids:
        att_path = Path(records_dir) / tid / "attempt.json"
        if not att_path.exists():
            continue
        att = json.loads(att_path.read_text(encoding="utf-8"))
        beh_path = Path(records_dir) / tid / "behaviors.md"
        beh_text = beh_path.read_text(encoding="utf-8").strip() if beh_path.exists() else ""
        passing = [c for c in att.get("candidates") or [] if (c.get("result") or {}).get("oracle_outcome") == "pass"]
        demo = [c for c in passing if c.get("demonstrated")]
        private_labels[tid] = dict(
            outcome=att.get("outcome"),
            model_demonstrated=bool(demo),
            passing_candidates=[Path(c["patch"]["path"]).name for c in passing],
        )
        if passing:
            stmt = ((rows.get(tid) or {}).get("problem_statement") or "").strip()
            excerpt = stmt[:3000] + ("..." if len(stmt) > 3000 else "")
            passing_cands[tid] = dict(issue_excerpt=excerpt, behavior=beh_text)

    sheet = p6.blind_b07_template(list(passing_cands.keys()), candidates=passing_cands) if passing_cands else p6.blind_b07_template(ordered_ids)
    for item in sheet["items"]:
        old = existing_items.get(item["task_id"]) or {}
        if old.get("author_judgment") is not None:
            item["author_judgment"] = old["author_judgment"]
        if old.get("author_note"):
            item["author_note"] = old["author_note"]

    Path(sheet_path).write_text(json.dumps(sheet, indent=2) + "\n", encoding="utf-8")
    Path(private_labels_path).parent.mkdir(parents=True, exist_ok=True)
    Path(private_labels_path).write_text(
        json.dumps(dict(schema="paper2-b07-model-labels/1", tasks=private_labels), indent=2) + "\n",
        encoding="utf-8",
    )
    return dict(sheet_items=len(sheet["items"]), passing_incomplete_tasks=len(passing_cands))


def _task_list(split: str, manifest_path: Path, limit: Optional[int] = None) -> List[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected = manifest.get("selected") or {}
    planned = (manifest.get("selection") or {}).get("planned") or {}
    ids: List[str] = []
    if split in ("source", "both"):
        ids += list(selected.get("source") or planned.get("source") or [])
    if split in ("target", "both"):
        ids += list(selected.get("target") or planned.get("target") or [])
    return ids[:limit] if limit is not None else ids


def run_batch(
    task_ids: Iterable[str],
    records_dir: Path = RECORDS,
    stage: str = "all",
    workers: int = 2,
    cleanup_source_images: bool = True,
) -> Dict[str, Any]:
    """Run Stage 1/2 (optionally parallel) and Stage 3 (sequential Docker) across task_ids."""
    task_ids = list(task_ids)
    rows = ss.rows_by_id()
    todo = [tid for tid in task_ids if tid in rows]
    errors: Dict[str, str] = {}

    if stage in ("stage1", "stage2", "generate", "all"):
        def _gen(tid: str) -> Tuple[str, Optional[str]]:
            out_dir = Path(records_dir) / tid
            if (out_dir / "attempt.json").exists():
                return tid, None
            row = rows[tid]
            try:
                if stage in ("stage1", "generate", "all"):
                    run_stage1_codex(tid, row, out_dir)
                if stage in ("stage2", "generate", "all"):
                    run_stage2_agy(tid, row, out_dir)
                return tid, None
            except Exception as exc:
                return tid, str(exc)

        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futs = [pool.submit(_gen, tid) for tid in todo]
            for fut in concurrent.futures.as_completed(futs):
                tid, err = fut.result()
                if err:
                    errors[tid] = err
                    print(f"[{stage} ERROR] {tid}: {err}", flush=True)
                else:
                    print(f"[{stage} OK] {tid}", flush=True)

    outcomes: Dict[str, str] = {}
    if stage in ("verify", "all"):
        for tid in todo:
            if tid in errors:
                continue
            out_dir = Path(records_dir) / tid
            if not (out_dir / "behaviors.md").exists() or not (out_dir / "check.py").exists():
                continue
            try:
                rec = stage3_verify(tid, rows[tid], out_dir, cleanup_source_images=cleanup_source_images)
                outcomes[tid] = rec["outcome"]
                print(f"[verify OK] {tid}: {rec['outcome']}", flush=True)
            except Exception as exc:
                errors[tid] = str(exc)
                print(f"[verify ERROR] {tid}: {exc}", flush=True)

    return dict(requested=len(task_ids), available_rows=len(todo), verified=len(outcomes), outcomes=outcomes, errors=errors)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run Protocol 6 B07 cross-family checks.")
    parser.add_argument("--manifest", type=Path, default=p6.PROTOCOL / "study_manifest.json")
    parser.add_argument("--records", type=Path, default=RECORDS)
    parser.add_argument("--split", choices=("source", "target", "both"), default="both")
    parser.add_argument("--task", action="append", dest="tasks", default=None)
    parser.add_argument("--stage", choices=("stage1", "stage2", "generate", "verify", "all", "update-sheet"), default="all")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--no-cleanup", action="store_true")
    args = parser.parse_args(argv)
    if args.stage == "update-sheet":
        print(json.dumps(update_blind_b07_sheet(args.manifest, args.records), indent=2))
        return 0
    ids = args.tasks if args.tasks else _task_list(args.split, args.manifest, limit=args.limit)
    res = run_batch(ids, records_dir=args.records, stage=args.stage, workers=args.workers, cleanup_source_images=not args.no_cleanup)
    if args.stage in ("verify", "all"):
        sheet_stats = update_blind_b07_sheet(args.manifest, args.records)
        res["sheet_stats"] = sheet_stats
    print(json.dumps(res, indent=2))
    return 1 if res["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

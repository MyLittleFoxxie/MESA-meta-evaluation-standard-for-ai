"""Repository-free file-identification exposure probe for Protocol 6 (criterion B14b).

Probe calls are NOT study sessions: they have no repository workspace, no tools,
and their own separate ProbeLedger under protocol-6/probe_ledger/.
"""
import argparse
import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

from paper2.method.decision_engine import compute_exact_binomial_interval
from paper2.preparation import study_controls as s
from paper2.preparation.cases import rate_difference

ROOT = Path(__file__).resolve().parents[2]
CUTOFF_ISO = "2026-05-01T00:00:00Z"  # day after max(Gemini 2026-03, GPT-6.1 Sol 2026-04-30)
DEFAULT_PROTOCOL_DIR = Path(__file__).resolve().parent / "protocol-6"
PROBE_SCHEMA = "paper2-exposure-probe/1"

PROBE_LIMITS = (
    "A repository-free file-name probe tests only whether the model names modified SymPy paths from the bug report "
    "alone; high accuracy can come from module cues in the issue text rather than training exposure, and low "
    "accuracy does not prove the model never saw the repository fix."
)


def is_strict_post_cutoff(pr: Dict[str, Any], cutoff: str = CUTOFF_ISO) -> bool:
    """True when an included target PR and every closing issue were opened and merged on or after cutoff."""
    if not pr.get("included"):
        return False
    if (pr.get("createdAt") or "") < cutoff or (pr.get("mergedAt") or "") < cutoff:
        return False
    nodes = (pr.get("closingIssuesReferences") or {}).get("nodes") or []
    if not nodes:
        return False
    return all((node.get("createdAt") or "") >= cutoff for node in nodes)


def reference_changed_files(patch_text: str) -> List[str]:
    """Extract sorted relative paths modified by a unified git diff."""
    files = set()
    for a_path, b_path in re.findall(r"^diff --git a/(\S+) b/(\S+)$", patch_text or "", re.M):
        if a_path != "/dev/null":
            files.add(a_path)
        if b_path != "/dev/null":
            files.add(b_path)
    if not files:
        for line in (patch_text or "").splitlines():
            if line.startswith(("+++ b/", "--- a/")):
                rel = line[6:].strip()
                if rel and rel != "/dev/null":
                    files.add(rel)
    return sorted(files)


def _normalize_repo_path(raw: str) -> str:
    cleaned = raw.strip().strip("`'\",;()[]{}").lstrip("./")
    if cleaned.startswith(("a/", "b/")):
        cleaned = cleaned[2:]
    return cleaned


def probe_prompt(problem_statement: str) -> str:
    """Repository-free prompt asking for likely modified SymPy file paths from bug text alone."""
    issue = (problem_statement or "").strip()
    return (
        "You have NO repository checkout and NO tools. Read only the bug report below from the SymPy library "
        "and predict which SymPy source files (relative repository paths, e.g. `sympy/core/expr.py`) would need to "
        "be modified to fix this bug.\n\n"
        "<bug_report>\n"
        f"{issue}\n"
        "</bug_report>\n\n"
        'Respond ONLY with a JSON object of the form {"files": ["sympy/..."]}. Do not include explanations.'
    )


def parse_predicted_files(response_text: str) -> List[str]:
    """Parse normalized repository file paths from JSON or plain-text model output."""
    text = (response_text or "").strip()
    if not text:
        return []
    candidates: List[str] = []
    fenced = re.search(r"```(?:json)?\s*(\{.*?\}|\[.*?\])\s*```", text, re.S)
    payload_text = fenced.group(1) if fenced else text
    try:
        parsed = json.loads(payload_text)
        raw_list = parsed.get("files", []) if isinstance(parsed, dict) else (parsed if isinstance(parsed, list) else [])
        for item in raw_list:
            if isinstance(item, str):
                norm = _normalize_repo_path(item)
                if norm.endswith(".py") or "/" in norm:
                    candidates.append(norm)
    except (json.JSONDecodeError, TypeError, ValueError):
        for match in re.findall(r"(?:sympy/[A-Za-z0-9_./-]+\.py)", text):
            candidates.append(_normalize_repo_path(match))
    seen, out = set(), []
    for path in candidates:
        if path and path not in seen:
            seen.add(path)
            out.append(path)
    return out


def score_prediction(predicted_files: Iterable[str], gold_files: Iterable[str]) -> Dict[str, Any]:
    """Score predicted file paths against reference fix paths (any-file hit + exact-set match + PRF1)."""
    pred = [_normalize_repo_path(p) for p in predicted_files if _normalize_repo_path(p)]
    gold = sorted({_normalize_repo_path(g) for g in gold_files if _normalize_repo_path(g)})
    pred_set, gold_set = set(pred), set(gold)
    matched = sorted(pred_set & gold_set)
    precision = len(matched) / len(pred_set) if pred_set else 0.0
    recall = len(matched) / len(gold_set) if gold_set else 0.0
    return dict(
        predicted=pred,
        gold=gold,
        matched=matched,
        any_file_hit=bool(matched),
        exact_set_match=bool(gold_set) and pred_set == gold_set,
        precision=precision,
        recall=recall,
    )


class ProbeLedger:
    """Append-only exposure probe ledger kept strictly separate from study SessionLedger slots."""

    def __init__(self, root: Optional[Path] = None):
        self.root = Path(root or (DEFAULT_PROTOCOL_DIR / "probe_ledger"))

    def record_path(self, config_id: str, split: str, task_id: str) -> Path:
        return self.root / f"{config_id}__{split}__{task_id}.json"

    def write(self, entry: Dict[str, Any]) -> Path:
        path = self.record_path(entry["config_id"], entry["split"], entry["task_id"])
        s.save_new(path, entry)
        return path

    def load_all(self) -> List[Dict[str, Any]]:
        if not self.root.exists():
            return []
        return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(self.root.glob("*.json"))]


def build_probe_record(
    config_id: str,
    split: str,
    task_id: str,
    problem_statement: str,
    gold_files: Iterable[str],
    raw_response: str,
    model_id: str,
    probe_mode: str = "live",
) -> Dict[str, Any]:
    """Build one validated schema record for a single exposure probe query."""
    prompt = probe_prompt(problem_statement)
    predicted = parse_predicted_files(raw_response)
    scores = score_prediction(predicted, gold_files)
    return dict(
        schema_version=PROBE_SCHEMA,
        config_id=config_id,
        model_id=model_id,
        split=split,
        task_id=task_id,
        probe_mode=probe_mode,
        prompt_sha256=__import__("hashlib").sha256(prompt.encode("utf-8")).hexdigest(),
        raw_response=raw_response,
        **scores,
        created_at=s.now(),
    )


def compare_exposure_rates(records: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Summarize source vs post-cutoff target hit rates per configuration with 95% exact binomial bounds."""
    by_cfg: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    for rec in records:
        cfg = rec["config_id"]
        split = rec["split"]
        by_cfg.setdefault(cfg, {}).setdefault(split, []).append(rec)

    summary: Dict[str, Any] = {}
    for cfg, splits in sorted(by_cfg.items()):
        cfg_out: Dict[str, Any] = {}
        for split in ("source", "target"):
            items = splits.get(split, [])
            n = len(items)
            hits = sum(1 for r in items if r.get("any_file_hit"))
            exact = sum(1 for r in items if r.get("exact_set_match"))
            lo, hi = compute_exact_binomial_interval(hits, n, confidence=0.95, one_sided=False) if n else (0.0, 1.0)
            cfg_out[split] = dict(
                n=n,
                any_file_hits=hits,
                hit_rate=(hits / n) if n else None,
                exact_ci_95=[lo, hi],
                exact_set_matches=exact,
                exact_match_rate=(exact / n) if n else None,
            )
        src, tgt = cfg_out["source"], cfg_out["target"]
        if src["n"] and tgt["n"]:
            diff_iv = rate_difference(src["any_file_hits"], src["n"], tgt["any_file_hits"], tgt["n"])
            cfg_out["source_minus_target"] = dict(
                point_difference=src["hit_rate"] - tgt["hit_rate"],
                newcombe_ci_95=diff_iv,
            )
        else:
            cfg_out["source_minus_target"] = None
        summary[cfg] = cfg_out
    return summary


def b14b_evidence_summary(config_id: str, comparison: Dict[str, Any]) -> Dict[str, Any]:
    """Format exposure probe findings and limits cleanly for Protocol 6 B14b forms."""
    cfg_stats = comparison.get(config_id) or {}
    src = cfg_stats.get("source") or {}
    tgt = cfg_stats.get("target") or {}
    diff = cfg_stats.get("source_minus_target")
    return dict(
        criterion="B14b",
        config_id=config_id,
        cutoff=CUTOFF_ISO,
        source_hits=f"{src.get('any_file_hits', 0)}/{src.get('n', 0)}",
        target_hits=f"{tgt.get('any_file_hits', 0)}/{tgt.get('n', 0)}",
        source_minus_target_pp=(
            round(100.0 * diff["point_difference"], 2) if diff and diff.get("point_difference") is not None else None
        ),
        limits=PROBE_LIMITS,
    )


def run_probe_batch(
    tasks: List[Dict[str, Any]],
    configs: List[Dict[str, str]],
    runner: Callable[[str, str, str], str],
    ledger: Optional[ProbeLedger] = None,
    probe_mode: str = "live",
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Run (config_id, task) queries with an explicit runner(config_id, model_id, prompt) -> str."""
    out_ledger = ledger or ProbeLedger()
    records = []
    for cfg in configs:
        cid, mid = cfg["config_id"], cfg["model_id"]
        for task in tasks:
            prompt = probe_prompt(task["problem_statement"])
            raw = runner(cid, mid, prompt)
            rec = build_probe_record(
                config_id=cid,
                split=task["split"],
                task_id=task["task_id"],
                problem_statement=task["problem_statement"],
                gold_files=task["gold_files"],
                raw_response=raw,
                model_id=mid,
                probe_mode=probe_mode,
            )
            out_ledger.write(rec)
            records.append(rec)
    return records, compare_exposure_rates(records)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect or summarize Protocol 6 B14b exposure probes (offline).")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_PROTOCOL_DIR / "probe_ledger")
    parser.add_argument("cmd", choices=("summary", "check-cutoff"))
    args = parser.parse_args(argv)
    if args.cmd == "summary":
        entries = ProbeLedger(args.ledger).load_all()
        print(json.dumps(dict(total_entries=len(entries), summary=compare_exposure_rates(entries)), indent=2))
        return 0
    pool_path = ROOT / "paper2" / "records" / "sympy_target_pool.json"
    pool = json.loads(pool_path.read_text(encoding="utf-8"))
    strict = [pr["task_id"] for pr in pool["prs"] if is_strict_post_cutoff(pr)]
    print(json.dumps(dict(cutoff=CUTOFF_ISO, included_total=sum(1 for pr in pool["prs"] if pr.get("included")),
                          strict_post_cutoff_count=len(strict), first_44=strict[:44]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


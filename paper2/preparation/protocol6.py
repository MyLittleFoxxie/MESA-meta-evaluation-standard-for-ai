"""Protocol 6 preparation for Paper 2: SymPy, 44 source + 44 post-cutoff target tasks, two configurations.

Preserves protocol-4 and protocol-5 byte for byte. Generates protocol-6 configuration,
requirement draft (exact binomial rule), blank forms, prompts, task-check ledgers,
gate-outcome fixture checks, blind B07 judgment templates, and readiness reports.
"""
import argparse
import contextlib
import hashlib
import json
import math
import shutil
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from paper2.method import evidence as ev
from paper2.method.decision_engine import exact_binomial_power
from paper2.preparation import exposure_probe as ep
from paper2.preparation import study_controls as s
from paper2.preparation.replay import CONDITIONS, REPEATED_MEASURES_NOTE, make_variant

ROOT = s.ROOT
PROTOCOL_NUMBER = "6"
PROTOCOL = Path(__file__).resolve().parent / f"protocol-{PROTOCOL_NUMBER}"
PROTOCOL5 = Path(__file__).resolve().parent / "protocol-5"
SAMPLE = dict(pilot=1, source=44, target=44)
CONFIGURATIONS = ("CONFIG_02_SOL_MED",)
REQUESTED = {
    "CONFIG_02_SOL_MED": dict(scaffold="Codex CLI", model="gpt-6.1-sol", effort="medium"),
}
PHASES = {
    "pilot": range(1, 2),       # 1 pilot * 1 config = 1
    "source": range(2, 46),     # 44 source * 1 config = 44
    "target": range(46, 90),    # 44 target * 1 config = 44
    "reserve": range(90, 100),  # 10 reserve slots
}
MAX_SESSIONS = 99
THRESHOLD = 0.70
CONFIDENCE = 0.95
DECISION_RULE = "exact_binomial"
N_MIN = 9  # binomial_sf(9, 9, 0.70) = 0.0404 <= 0.05; 8/8 gives 0.0576 > 0.05

SUBMISSION_LIMITS = dict(
    policy_defined_before_sessions=(
        "POLICY-P6-CONTROLLED was defined on 2026-11-11 after Protocol 5's signed forms returned No decision "
        "(failing B12, B14a, B14b, and release-level B28a) and before any Protocol 6 agent session."
    ),
    sample_size_note=(
        "Protocol 6 sizes at 1 pilot, 44 source, and 44 post-cutoff target tasks for one active configuration "
        "(CONFIG_02_SOL_MED; 89 active + 10 reserve = 99 max slots) as approved by the author. At N=44 under "
        "one-sided 95% exact binomial cut points (Accept >= 37, Reject <= 25), Accept power at true rate 0.85 is "
        "66.3% before removal and falls steeply after B07 task removal (e.g. near n=12, Accept requires 12/12, "
        "leaving Accept nearly unreachable); exact power across N in {12, 31, 44, 52, 60, 75} is reported."
    ),
)


def make_ledger(root: Optional[Path] = None) -> s.SessionLedger:
    return s.SessionLedger(root or (PROTOCOL / "ledger"), phases=PHASES, max_sessions=MAX_SESSIONS)


def build_pools() -> Dict[str, Any]:
    """Reuse pinned source pool and filter target pool strictly to PRs & closing issues >= 2026-05-01T00:00:00Z."""
    base = s.build_pools()
    from paper2.preparation import targets
    raw_pool = targets.load_pool() if targets.POOL.exists() else dict(prs=[])
    strict_ids = {pr["task_id"] for pr in raw_pool["prs"] if ep.is_strict_post_cutoff(pr)}
    strict_target = [t for t in base["target"] if t["task_id"] in strict_ids]
    excluded_pre_cutoff = [
        dict(t, reason=f"created or linked issue opened before {ep.CUTOFF_ISO}")
        for t in base["target"] if t["task_id"] not in strict_ids
    ]
    return dict(
        source=base["source"],
        target=strict_target,
        excluded_pre_cutoff=excluded_pre_cutoff,
        excluded_fixtures=base["excluded_fixtures"],
        excluded_historical=base["excluded_historical"],
    )


def planned_task_lists(pools: Dict[str, Any], results: Dict[str, Any]) -> Dict[str, Any]:
    """Deterministic first-N non-ineligible tasks in order_key order plus exact current eligibility counts."""
    ordered_src = sorted(pools["source"], key=lambda t: t["order_key"])
    ordered_tgt = sorted(pools["target"], key=lambda t: t["order_key"])
    pilot_src = ordered_src[: SAMPLE["pilot"]]
    main_src = ordered_src[SAMPLE["pilot"] : SAMPLE["pilot"] + SAMPLE["source"]]
    main_tgt = [
        t for t in ordered_tgt
        if s.eligibility_state(t, results.get(t["task_id"])) not in ("ineligible", "identity not confirmed")
    ][: SAMPLE["target"]]

    def _states(tasks):
        return {t["task_id"]: s.eligibility_state(t, results.get(t["task_id"])) for t in tasks}

    src_states = _states(pilot_src + main_src)
    tgt_states = _states(main_tgt)
    return dict(
        pilot=[t["task_id"] for t in pilot_src],
        source=[t["task_id"] for t in main_src],
        target=[t["task_id"] for t in main_tgt],
        eligibility_counts=dict(
            source={k: list(src_states.values()).count(k) for k in sorted(set(src_states.values()))},
            target={k: list(tgt_states.values()).count(k) for k in sorted(set(tgt_states.values()))},
        ),
        pending_target_ids=[tid for tid, st in tgt_states.items() if st.startswith("pending")],
    )


def power_table() -> List[Dict[str, Any]]:
    rows = []
    for n in (12, 31, 44, 52, 60, 75):
        pw = exact_binomial_power(n, THRESHOLD, confidence=CONFIDENCE, one_sided=True)
        rows.append(
            dict(
                retained_tasks=n,
                accept_min_k=pw["accept_min_k"],
                reject_max_k=pw["reject_max_k"],
                type1_accept=round(pw["type1_accept"], 4),
                type1_reject=round(pw["type1_reject"], 4),
                accept_at_0_85=round(pw["by_rate"]["0.85"]["accept"], 4),
                accept_at_0_80=round(pw["by_rate"]["0.80"]["accept"], 4),
                accept_at_0_75=round(pw["by_rate"]["0.75"]["accept"], 4),
                reject_at_0_50=round(pw["by_rate"]["0.50"]["reject"], 4),
            )
        )
    return rows


def requirement_draft(planned: Dict[str, Any]) -> Dict[str, Any]:
    p5_req = json.loads((PROTOCOL5 / "requirement-draft.json").read_text(encoding="utf-8"))
    return dict(
        record="paper2-requirement/protocol-6",
        status="draft",
        id="REQ-P6-SYMPY-BUGFIX",
        stakeholder_role=(
            "Engineering tooling lead choosing one unsupervised coding assistant to generate Python bug-fix "
            "drafts on a team's SymPy codebase before human code review."
        ),
        population=(
            "Single-issue SymPy bug reports paired with maintainer regression tests: source pool from SWE-bench "
            "Verified SymPy instances (issues 2016-2023); target pool from SymPy PRs created and merged with all "
            f"closing issues created on or after {ep.CUTOFF_ISO}."
        ),
        fit_criterion=(
            "Without internet access or oracle leakage and without modifying any test runner or test configuration "
            "file, the agent's patch cleanly applies to the base commit and passes every maintainer test that checks "
            "behavior stated in the bug report, within 900 seconds. Removing tasks with confirmed B05 or B07 test "
            "defects implements this fit criterion directly rather than revising the requirement."
        ),
        text=(
            "Working alone in a local SymPy checkout without network access or test-runner modifications, the coding "
            "agent resolves bug reports by passing maintainer tests that check stated bug-report behavior, with one-sided "
            "95% exact binomial lower bound at least 0.70 within 15 minutes per bug report."
        ),
        decision_rule_spec=dict(
            rule=DECISION_RULE,
            confidence=CONFIDENCE,
            one_sided=True,
            threshold=THRESHOLD,
            accept_condition="One-sided 95% exact binomial lower bound >= 0.70 (P(X >= k | n, 0.70) <= 0.05)",
            reject_condition="One-sided 95% exact binomial upper bound < 0.70 (P(X <= k | n, 0.70) < 0.05)",
            otherwise="Inconclusive",
        ),
        decision_rule=DECISION_RULE,
        confidence=CONFIDENCE,
        threshold=THRESHOLD,
        time_limit_seconds=900,
        target_repository=s.REPOSITORY,
        n_min=N_MIN,
        n_min_reason=(
            "Smallest sample under exact one-sided 95% binomial bounds where Accept is possible: "
            "9/9 gives upper-tail p = 0.0404 <= 0.05 (8/8 gives 0.0576 > 0.05)."
        ),
        values_note=(
            "70% matches the study threshold carried from earlier protocols so an assistant solves roughly seven of ten "
            "issues without setup; 15 minutes (900 s) is the unattended run budget per ticket before human takeover. "
            "Neither value was empirically calibrated from a field productivity study."
        ),
        sample_size=dict(
            chosen=SAMPLE,
            max_sessions=MAX_SESSIONS,
            note=SUBMISSION_LIMITS["sample_size_note"],
            exact_power_table=power_table(),
        ),
        criteria=list(ev.SELECTED_CRITERIA),
        policies=["POLICY-P5-STRICT", "POLICY-P5-LENIENT", "POLICY-P6-CONTROLLED"],
        controlled_policy_history=SUBMISSION_LIMITS["policy_defined_before_sessions"],
        rubric=p5_req["rubric"],
        configurations=list(CONFIGURATIONS),
        standby_fallback_configuration="CONFIG_01_GEMINI_FLASH_MED",
        standby_fallback_rule=(
            "CONFIG_02_SOL_MED runs alone; only if Sol exhausts weekly Codex credits without resetting in time, "
            "a formal contingency amendment re-freezes CONFIG_01_GEMINI_FLASH_MED for a separate complete 1+44+44 run."
        ),
        transfer={c: p5_req["transfer"][c] for c in CONFIGURATIONS},
        task_set=dict(
            pilot=planned["pilot"],
            source=planned["source"],
            target_post_cutoff=planned["target"],
        ),
        target_issues_before_cutoff=[],
        target_issues_before_cutoff_note="Empty by Protocol 6 construction: every selected target issue and PR is >= 2026-05-01.",
        drafted_by="Protocol 6 generator (based on Protocol 5 draft and P6 plan)",
    )


def task_check_ledger(planned: Dict[str, Any], results: Dict[str, Any]) -> Dict[str, Any]:
    """Per-task explicit check ledger on both 44 source and 44 target tasks (P6-5)."""
    probe_entries = ep.ProbeLedger(PROTOCOL / "probe_ledger").load_all()
    probe_keys = {(e["split"], e["task_id"]) for e in probe_entries}
    b05_path = PROTOCOL / "audit_checks" / "b05-counterexamples"
    b07_path = PROTOCOL / "audit_checks" / "b07-counterexamples"

    def _row(split: str, tid: str) -> Dict[str, Any]:
        st = "recorded" if tid in results else "not_performed"
        b05_st = "recorded" if (b05_path / f"{tid}.json").exists() else "not_performed"
        att_path = b07_path / tid / "attempt.json"
        if not att_path.exists():
            b07_entry = dict(status="not_performed", reason="missing")
        else:
            att = json.loads(att_path.read_text(encoding="utf-8"))
            outcome = att.get("outcome")
            if outcome in ("check invalid", "no candidate"):
                b07_entry = dict(
                    status="not_performed",
                    reason=outcome,
                    retained=True,
                    attempt=str(att_path.relative_to(ROOT)),
                )
            else:
                b07_entry = dict(status="recorded", outcome=outcome)
        prob_st = "recorded" if (split, tid) in probe_keys else "not_performed"
        return dict(
            task_id=tid,
            split=split,
            eligibility=dict(status=st, result=(results[tid]["status"] if tid in results else None)),
            b05_check=dict(status=b05_st),
            b07_incomplete_patch=b07_entry,
            b14b_exposure_probe=dict(status=prob_st),
        )

    rows = [_row("pilot", tid) for tid in planned["pilot"]]
    rows += [_row("source", tid) for tid in planned["source"]]
    rows += [_row("target", tid) for tid in planned["target"]]
    return dict(
        record="paper2-task-checks/protocol-6",
        updated_at=s.now(),
        rule=(
            "Checks missing on disk, plus invalid B07 checks and no-candidate B07 attempts, are marked "
            "'not_performed' with their reason; invalid/no-candidate B07 tasks remain in the retained set."
        ),
        summary={
            split: {
                **{
                    chk: sum(1 for r in rows if r["split"] == split and r[chk]["status"] == "recorded")
                    for chk in ("eligibility", "b05_check", "b07_incomplete_patch", "b14b_exposure_probe")
                },
                "b07_not_performed_by_reason": {
                    reason: sum(
                        1 for r in rows
                        if r["split"] == split and r["b07_incomplete_patch"].get("reason") == reason
                    )
                    for reason in ("check invalid", "no candidate", "missing")
                    if any(
                        r["split"] == split and r["b07_incomplete_patch"].get("reason") == reason
                        for r in rows
                    )
                },
            }
            for split in ("pilot", "source", "target")
        },
        tasks=rows,
    )


def blind_b07_template(task_ids: List[str], candidates: Optional[Dict[str, Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Generate a blind human B07 behavior-judgment sheet hiding model identity and pass/fail conclusions."""
    items = []
    for tid in task_ids:
        cand = (candidates or {}).get(tid) or {}
        items.append(
            dict(
                task_id=tid,
                issue_excerpt=cand.get("issue_excerpt", ""),
                claimed_broken_behavior=cand.get("behavior", ""),
                model_label_hidden=True,
                author_judgment=None,  # allowed: "states_broken_behavior", "does_not_state", "unclear"
                author_note="",
                model_judgments={},  # populated with {"family1_runA": ..., "family1_runB": ..., "family2_run": ...}
            )
        )
    return dict(
        schema="paper2-blind-b07/1",
        status="pending_human_rating",
        options=["states_broken_behavior", "does_not_state", "unclear"],
        items=items,
    )


def _pair_agreement(a_vals: List[Optional[str]], b_vals: List[Optional[str]], positive: str = "states_broken_behavior") -> Dict[str, Any]:
    allowed = {"states_broken_behavior", "does_not_state", "unclear"}
    pairs = [(a == positive, b == positive) for a, b in zip(a_vals, b_vals) if a in allowed and b in allowed]
    n = len(pairs)
    if not n:
        return dict(rated=0, agreements=0, raw_agreement=None, kappa=None)
    agree = sum(a == b for a, b in pairs)
    p0 = agree / n
    pa = sum(a for a, _ in pairs) / n
    pb = sum(b for _, b in pairs) / n
    pe = pa * pb + (1.0 - pa) * (1.0 - pb)
    kappa = (p0 - pe) / (1.0 - pe) if not math.isclose(pe, 1.0) else None
    exact_3way = sum(a == b for a, b in zip(a_vals, b_vals) if a in allowed and b in allowed)
    return dict(rated=n, exact_3way=exact_3way, agreements=agree, raw_agreement=p0, kappa=kappa)


def apply_b07_scope_rule(
    sheet: Dict[str, Any],
    model_labels: Dict[str, Any],
    source_ids: Optional[List[str]] = None,
    target_ids: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Apply the pre-freeze Protocol 6 B07 scope rule across `blind_b07_sheet.json` items.

    Rule: a task counts as an in-scope B07 defect iff (a) Stage 3 demonstrated a failing check against a candidate
    incomplete patch (`model_demonstrated` True), AND (b) both same-family rating runs (`family1_runA` and
    `family1_runB`) agree on `states_broken_behavior`. Disagreements stay in the retained set and are reported;
    `family2_run` is reported as an agreement check only. `author_judgment` stays empty (`None`).
    """
    src_set = set(source_ids) if source_ids is not None else None
    tgt_set = set(target_ids) if target_ids is not None else None
    tasks_info = model_labels.get("tasks", model_labels)

    runA_vals, runB_vals, fam1_consensus_vals, fam2_vals = [], [], [], []
    agreed_defects, disagreed_kept, not_stated_kept = [], [], []
    all_demonstrated = []
    per_task = {}

    for item in sheet.get("items") or []:
        tid = item["task_id"]
        mj = item.get("model_judgments") or {}
        rA = mj.get("family1_runA")
        rB = mj.get("family1_runB")
        r2 = mj.get("family2_run")
        runA_vals.append(rA)
        runB_vals.append(rB)
        fam2_vals.append(r2)
        f1_agree_broken = (rA == "states_broken_behavior" and rB == "states_broken_behavior")
        fam1_consensus_vals.append("states_broken_behavior" if f1_agree_broken else "does_not_state")

        info = tasks_info.get(tid)
        demonstrated = bool(info["model_demonstrated"]) if isinstance(info, dict) else bool(info)
        if demonstrated:
            all_demonstrated.append(tid)
        disagreed = bool(rA and rB and rA != rB)
        if demonstrated and f1_agree_broken:
            agreed_defects.append(tid)
            status = "agreed_defect_removed"
        elif demonstrated and disagreed:
            disagreed_kept.append(tid)
            status = "family1_disagreed_retained"
        elif demonstrated:
            not_stated_kept.append(tid)
            status = "not_stated_retained"
        else:
            status = "no_demonstrated_defect_retained"
        per_task[tid] = dict(
            demonstrated=demonstrated,
            family1_runA=rA,
            family1_runB=rB,
            family2_run=r2,
            disagreed=disagreed,
            agreed_defect=(demonstrated and f1_agree_broken),
            status=status,
        )

    def _by_split(tids: List[str]) -> Dict[str, List[str]]:
        if src_set is None and tgt_set is None:
            return dict(all=sorted(tids))
        return dict(
            source=sorted(t for t in tids if src_set and t in src_set),
            target=sorted(t for t in tids if tgt_set and t in tgt_set),
            all=sorted(tids),
        )

    return dict(
        schema="paper2-b07-scope-rule/1",
        rule="agreed_defect iff model_demonstrated and family1_runA == family1_runB == 'states_broken_behavior'",
        author_judgment_empty=all(item.get("author_judgment") is None for item in (sheet.get("items") or [])),
        items_rated=len(sheet.get("items") or []),
        agreement=dict(
            family1_runA_vs_runB=_pair_agreement(runA_vals, runB_vals),
            family1_consensus_vs_family2=_pair_agreement(fam1_consensus_vals, fam2_vals),
            family1_runA_vs_family2=_pair_agreement(runA_vals, fam2_vals),
            family1_runB_vs_family2=_pair_agreement(runB_vals, fam2_vals),
        ),
        agreed_defects=_by_split(agreed_defects),
        disagreed_retained=_by_split(disagreed_kept),
        not_stated_retained=_by_split(not_stated_kept),
        all_demonstrated=_by_split(all_demonstrated),
        per_task=per_task,
    )


def score_blind_b07(sheet: Dict[str, Any], model_labels: Dict[str, bool]) -> Dict[str, Any]:
    """Compute raw agreement and Cohen's kappa between human B07 judgments and model labels."""
    allowed = {"states_broken_behavior", "does_not_state"}
    pairs: List[Tuple[bool, bool]] = []
    skipped = []
    for item in sheet.get("items") or []:
        tid = item["task_id"]
        judg = item.get("author_judgment")
        if judg not in allowed or tid not in model_labels:
            skipped.append(tid)
            continue
        pairs.append((judg == "states_broken_behavior", bool(model_labels[tid])))
    n = len(pairs)
    if not n:
        return dict(rated=0, skipped=len(skipped), raw_agreement=None, kappa=None)
    agree = sum(a == b for a, b in pairs)
    p0 = agree / n
    pa_true = sum(a for a, _ in pairs) / n
    pb_true = sum(b for _, b in pairs) / n
    pe = pa_true * pb_true + (1.0 - pa_true) * (1.0 - pb_true)
    kappa = (p0 - pe) / (1.0 - pe) if not math.isclose(pe, 1.0) else None
    return dict(rated=n, skipped=len(skipped), exact_agreements=agree, raw_agreement=p0, kappa=kappa)


def per_field_form_agreement(runs: Dict[str, Dict[str, Dict[str, Any]]]) -> Dict[str, Any]:
    """Compare named rating runs (e.g. run_A, run_B, family_2) field by field across criteria (P6-7)."""
    names = sorted(runs)
    criteria = sorted({c for r in runs.values() for c in r})
    fields = ("anchor", "check.kind", "check.outcome", "applicability.applies", "scope.level")

    def _get(rec, dotted):
        cur = rec
        for part in dotted.split("."):
            if not isinstance(cur, dict):
                return None
            cur = cur.get(part)
        return cur

    pair_reports = {}
    for i, a_name in enumerate(names):
        for b_name in names[i + 1 :]:
            key = f"{a_name}__vs__{b_name}"
            per_field = {}
            for fld in fields:
                matched = 0
                for c in criteria:
                    if _get(runs[a_name].get(c), fld) == _get(runs[b_name].get(c), fld):
                        matched += 1
                per_field[fld] = dict(matched=matched, total=len(criteria), rate=matched / len(criteria) if criteria else None)
            defects_match = sum(
                sorted(d["task_id"] for d in (runs[a_name].get(c) or {}).get("task_defects") or [])
                == sorted(d["task_id"] for d in (runs[b_name].get(c) or {}).get("task_defects") or [])
                for c in criteria
            )
            per_field["task_defects_ids"] = dict(
                matched=defects_match,
                total=len(criteria),
                rate=defects_match / len(criteria) if criteria else None,
            )
            pair_reports[key] = per_field
    return dict(runs=names, criteria_count=len(criteria), pairwise=pair_reports)


def build_gate_outcomes_demo(out_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Verify all four Paper 2 gate statuses using signed P5 forms + clearly-labeled synthetic fixtures (P6-4)."""
    import tempfile

    p5_completed = PROTOCOL5 / "audit_forms" / "completed"
    signed_forms = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(p5_completed.glob("*.json"))}
    req_src = json.loads((PROTOCOL5 / "requirement-draft.json").read_text(encoding="utf-8"))
    cfg = "CONFIG_01_GEMINI_FLASH_MED"
    tasks = list(req_src["task_set"]["source"][:12])  # 2 tasks are left out by signed B07 -> 10 retained (>= n_min=9)
    req = dict(
        id="REQ-P6-GATE-DEMO",
        text=req_src["text"],
        target_repository=s.REPOSITORY,
        threshold=THRESHOLD,
        decision_rule=DECISION_RULE,
        confidence=CONFIDENCE,
        n_min=N_MIN,
    )

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        obs = []
        for idx, tid in enumerate(tasks):
            patch = root / f"{tid}.diff"
            log = root / f"{tid}.log"
            patch.write_text(f"diff --git a/sympy/core/expr.py b/sympy/core/expr.py\n# clean {tid}\n", encoding="utf-8")
            log.write_text(f"clean log {tid}\n", encoding="utf-8")
            obs.append(
                dict(
                    task_id=tid,
                    config_id=cfg,
                    repository=s.REPOSITORY,
                    resolved=True,
                    patch=dict(task_id=tid, path=str(patch), sha256=ev.sha256_file(patch)),
                    provenance=dict(
                        session_id=f"demo-{idx:02d}",
                        log=str(log),
                        log_sha256=ev.sha256_file(log),
                        controls=dict(no_scoring_file_changes=dict(passed=True, changed_files=[])),
                    ),
                )
            )
        evidence_all = [
            s.form_to_evidence(signed_forms[name], tasks)
            for name in ("B05-release", "B07-release", "B12-release", "B14a-release", "B28a-release", "B28b-release", f"B14b-{cfg}")
        ]
        evidence_lenient = [
            s.form_to_evidence(signed_forms[name], tasks)
            for name in ("B05-release", "B07-release", "B28a-release", "B28b-release")
        ]

        def _mk(case_id, policy, evidence):
            return dict(
                schema_version=ev.CASE_SCHEMA,
                case_id=case_id,
                kind="constructed_variant",
                config_id=cfg,
                source_repository=s.REPOSITORY,
                task_ids=tasks,
                requirement=req,
                observations=obs,
                policy=policy,
                evidence=evidence,
                transfer=dict(req_src["transfer"][cfg], author="gate-demo-fixture"),
            )

        res_admissible = ev.evaluate_controlled_case(_mk("demo-admissible", ev.controlled_policy(), evidence_lenient))
        res_inadmissible = ev.evaluate_study_case(_mk("demo-inadmissible", ev.default_policy(), evidence_all))
        inquiry_case = make_variant(_mk("demo-inquiry", ev.controlled_policy(), evidence_lenient), "provenance_removed", tasks[0])
        res_inquiry = ev.evaluate(inquiry_case)
        rejected_case = make_variant(_mk("demo-rejected", ev.controlled_policy(), evidence_lenient), "identity_mismatch", tasks[0])
        res_rejected = ev.evaluate(rejected_case)

    payload = dict(
        schema="paper2-gate-outcomes-demo/1",
        status="software_fixture_using_signed_p5_forms_plus_synthetic_clean_observations",
        outcomes=dict(
            admissible=dict(
                policy="POLICY-P6-CONTROLLED",
                input_integrity=res_admissible["input_integrity"],
                evidence_status=res_admissible["evidence_status"],
                score_decision=res_admissible["score_decision"],
                requirement_decision=res_admissible["requirement_decision"],
            ),
            inadmissible=dict(
                policy="POLICY-P5-STRICT",
                input_integrity=res_inadmissible["input_integrity"],
                evidence_status=res_inadmissible["evidence_status"],
                requirement_decision=res_inadmissible["requirement_decision"],
                blocking_reasons=res_inadmissible["reasons"],
            ),
            inquiry_required=dict(
                condition="provenance_removed",
                input_integrity=res_inquiry["input_integrity"],
                evidence_status=res_inquiry["evidence_status"],
                requirement_decision=res_inquiry["requirement_decision"],
                blocking_reasons=res_inquiry["reasons"],
            ),
            rejected_level_1=dict(
                condition="identity_mismatch",
                input_integrity=res_rejected["input_integrity"],
                evidence_status=res_rejected["evidence_status"],
                reasons=res_rejected["reasons"],
            ),
        ),
    )
    if out_dir is not None:
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        (Path(out_dir) / "gate_outcomes_demo.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def write_prompts_and_configs(planned: Dict[str, Any]) -> None:
    src_list = "\n".join(f"- `{tid}`" for tid in planned["source"])
    tgt_list = "\n".join(f"- `{tid}`" for tid in planned["target"])
    pilot_list = "\n".join(f"- `{tid}`" for tid in planned["pilot"])

    p5_cfg = json.loads((PROTOCOL5 / "configurations.json").read_text(encoding="utf-8"))
    active_cfgs = [c for c in p5_cfg["configurations"] if c["config_id"] in CONFIGURATIONS]
    standby_cfgs = [c for c in p5_cfg["configurations"] if c["config_id"] not in CONFIGURATIONS]
    p6_cfg = dict(p5_cfg)
    p6_cfg["record"] = "paper2-configurations/protocol-6"
    p6_cfg["replaces_for_protocol_6"] = "paper2/preparation/protocol-5/configurations.json (preserved unchanged)"
    p6_cfg["selection_note"] = (
        "Active Protocol 6 study sessions use CONFIG_02_SOL_MED only (chosen for runtime after rehearsal and source "
        "exposure probe records existed). CONFIG_01_GEMINI_FLASH_MED stays in standby only if Sol exhausts weekly "
        "Codex credits without a timely reset (requiring a formal contingency amendment before running Gemini)."
    )
    p6_cfg["configurations"] = active_cfgs
    p6_cfg["standby_configurations"] = standby_cfgs
    (PROTOCOL / "configurations.json").write_text(json.dumps(p6_cfg, indent=2) + "\n", encoding="utf-8")

    for fname in ("agy-agent.md", "agy-session-settings.json", "agy-gate.py"):
        shutil.copyfile(PROTOCOL5 / fname, PROTOCOL / fname)
    hooks = json.loads((PROTOCOL5 / "agy-hooks.json").read_text(encoding="utf-8"))
    if "protocol-5-gate" in hooks:
        hooks = {"protocol-6-gate": hooks["protocol-5-gate"]}
    (PROTOCOL / "agy-hooks.json").write_text(json.dumps(hooks, indent=2) + "\n", encoding="utf-8")

    abc_prompt = "\n".join([
        "# Prompt for the ABC run (protocol 6)",
        "",
        "Fixed before the run. The reviewer receives this text and no MESA rules or definitions.",
        "",
        "---",
        "",
        "You review SWE-bench Verified (SymPy subset) with the Agentic Benchmark Checklist (ABC; Zhu et al., NeurIPS 2025).",
        "",
        "## Tasks (1 pilot + 44 source tasks)",
        "",
        pilot_list,
        src_list,
        "",
        "Answer every item in `paper2/preparation/protocol-6/abc-items.json` and write `ABC-release.json` with `status: \"draft\"` and empty `roles`.",
        "Do NOT read MESA rubric files, MESA forms, `paper2/method/`, `cases.py`, or manuscript drafts.",
        "",
    ])
    (PROTOCOL / "abc-prompt.md").write_text(abc_prompt, encoding="utf-8")

    reviewer_prompt = "\n".join([
        "# Prompt for Protocol 6 MESA rating runs (v5.1 rubric)",
        "",
        "To run independently in three isolated scratch output folders (`rating-run-p6-A`, `rating-run-p6-B` on family 1; `rating-run-p6-family2` on family 2).",
        "",
        "---",
        "",
        "Rate SWE-bench Verified (SymPy scope) under `v5/rubric/rubric-v5.1.md` across B05, B07, B12, B14a, B14b, B28a, and B28b.",
        "",
        "## Protocol 6 specifics",
        "",
        "- **B07 verification separation:** incomplete candidate patches and verification `check.py` scripts are produced by different model families. In addition to completing the seven MESA forms, rate every item in `paper2/preparation/protocol-6/blind_b07_sheet.json` blindly (`states_broken_behavior`, `does_not_state`, or `unclear`) into `b07_scope_judgments.json` in your scratch folder without inspecting `audit_checks/b07_model_labels.json`, `audit_checks/b07-counterexamples/`, candidate diffs, or other rating runs.",
        "- **B14b exposure evidence:** combine stated training-cutoff checks with the repository-free exposure probe ledger in `paper2/preparation/protocol-6/probe_ledger/` for `CONFIG_02_SOL_MED` and state its detection limits.",
        "- **B28a session control:** cite `paper2/preparation/protocol-6/audit_checks/b28a-scoring-check/` (`B28a-release`) and state clearly whether release-level test-runner mutability exists AND whether `POLICY-P6-CONTROLLED` (`no_scoring_file_changes`) applies per case.",
        "- **Output:** write the seven MESA draft JSON forms (`status: \"draft\"`, empty `roles`) from `paper2/preparation/protocol-6/audit_forms/` (`B05-release`, `B07-release`, `B12-release`, `B14a-release`, `B14b-CONFIG_02_SOL_MED`, `B28a-release`, `B28b-release`) plus `b07_scope_judgments.json` into your assigned isolated scratch folder.",
        "",
        "## Tasks in scope (1 pilot + 44 source + 44 post-cutoff target)",
        "",
        "### Pilot",
        pilot_list,
        "",
        "### Source (44)",
        src_list,
        "",
        "### Post-cutoff target (44)",
        tgt_list,
        "",
    ])
    (PROTOCOL / "reviewer-prompt-p6.md").write_text(reviewer_prompt, encoding="utf-8")

    b07_prompt = "\n".join([
        "# Prompt for Protocol 6 B07 incomplete-patch and verification-test separation",
        "",
        "## Role separation rule",
        "",
        "- **Stage 1 (Model Family A - Incomplete Patch Author):** Given issue text and source checkout, produce candidate incomplete patches (`candidate-N.diff`) and state violated behaviors (`behaviors.md`). Never edit or write `check.py`.",
        "- **Stage 2 (Model Family B - Second Model Family Test Writer):** Without viewing Model Family A's rationale, write independent verification test `check.py` strictly from the issue text and `behaviors.md`, failing any candidate that omits stated behavior while passing the reference fix.",
        "",
        "## Tasks requiring B07 checks (44 source + 44 target)",
        "",
        src_list,
        tgt_list,
        "",
    ])
    (PROTOCOL / "b07-attempt-prompt-p6.md").write_text(b07_prompt, encoding="utf-8")
    if not (PROTOCOL / "b28a-check-prompt.md").exists():
        shutil.copyfile(PROTOCOL5 / "b28a-check-prompt.md", PROTOCOL / "b28a-check-prompt.md")


def protocol_markdown(planned: Dict[str, Any]) -> str:
    return "\n".join([
        "# Protocol 6 (REFSQ 2027 revision)",
        "",
        "Supersedes Protocol 5 while keeping `paper2/preparation/protocol-4/` and `paper2/preparation/protocol-5/` byte for byte.",
        "",
        "## Key changes from Protocol 5",
        "",
        f"1. **Single configuration & sample size (`44 + 44`):** Active sessions use `CONFIG_02_SOL_MED` only (`1` pilot + `{SAMPLE['source']}` source + `{SAMPLE['target']}` post-cutoff target + `10` reserve = `{MAX_SESSIONS}` max slots). Target tasks require issue creation, PR creation, and PR merge on or after `{ep.CUTOFF_ISO}`.",
        "2. **Standby Gemini contingency rule:** `CONFIG_01_GEMINI_FLASH_MED` has no pre-freeze target checks or sessions under this freeze. Only if `CONFIG_02_SOL_MED` exhausts its Codex weekly quota mid-experiment without resetting in time, a formal contingency amendment preserves any partial Sol sessions separately and re-freezes `CONFIG_01_GEMINI_FLASH_MED` for a complete separate `1 + 44 + 44` study.",
        "3. **Exact binomial decision rule (`REQ-P6-SYMPY-BUGFIX`):** Accept when one-sided 95% exact binomial lower bound >= `0.70` (`k >= 37` at `n=44`); Reject when one-sided 95% exact binomial upper bound < `0.70` (`k <= 25` at `n=44`); otherwise Inconclusive (`n_min = 9`).",
        f"4. **Controlled policy (`POLICY-P6-CONTROLLED`):** {SUBMISSION_LIMITS['policy_defined_before_sessions']}",
        "5. **Symmetry across source and target:** Eligibility and B07 checks run identically on all 44 source and 44 target tasks, tracked explicitly in `task_checks.json` (`not_performed` for missing, invalid-check, and no-candidate tasks, all retained since no defect was shown).",
        "6. **Exposure probe (`B14b`):** Repository-free bug-to-file probe logged separately in `probe_ledger/` (not SessionLedger slots).",
        "7. **Model-family separation & B07 scope rule (`P6-7`):** Two isolated family-1 review runs (`Claude Sonnet 5.5`) plus one second-family run (`GPT-6.1 Sol`); incomplete patches (`GPT-6.1 Sol`) and verification tests (`Gemini 3.8 Flash Medium`) come from different model families. Models judge all 82 blind B07 items (`author_judgment` stays empty); a task counts as a B07 defect iff both family-1 runs agree `states_broken_behavior`. Disagreements stay in and are reported alongside three-way sensitivity (`with_scope_rule`, `all_flagged`, `none_removed`).",
        "8. **Power disclosure:** " + SUBMISSION_LIMITS["sample_size_note"],
        "",
        "## Planned tasks (`order_key` order)",
        "",
        f"- Pilot: `{', '.join(planned['pilot'])}`",
        f"- Source eligibility: `{planned['eligibility_counts']['source']}`",
        f"- Target eligibility: `{planned['eligibility_counts']['target']}` ({len(planned['pending_target_ids'])} pending Docker derivation)",
        "",
    ])


def prepare(run_tests: bool = False) -> Path:
    from paper2.preparation import harness
    saved_cfgs = s.CONFIGURATIONS
    s.CONFIGURATIONS = CONFIGURATIONS
    try:
        return _prepare_inner(run_tests=run_tests)
    finally:
        s.CONFIGURATIONS = saved_cfgs


def _prepare_inner(run_tests: bool = False) -> Path:
    from paper2.preparation import harness
    pools = build_pools()
    results = harness.load_results()
    planned = planned_task_lists(pools, results)
    chosen = s.select(pools, results, sample=SAMPLE)

    PROTOCOL.mkdir(parents=True, exist_ok=True)
    s.abc_items(PROTOCOL / "abc-items.json")

    manifest_path = PROTOCOL / "study_manifest.json"
    frozen_done = (PROTOCOL / "frozen_manifest.json").exists()
    if manifest_path.exists() and any(json.loads(manifest_path.read_text(encoding="utf-8")).get("selected", {}).values()) and not frozen_done:
        raise RuntimeError("Protocol 6 manifest already records a finalized selection")

    overlaps = s.separation_problems(
        dict(source=pools["source"], target=pools["target"], fixture=pools["excluded_fixtures"],
             historical=pools["excluded_historical"])
    )
    manifest = dict(
        protocol=f"{PROTOCOL_NUMBER} ({'frozen' if frozen_done else 'draft, not frozen'})",
        status="frozen; see frozen_manifest.json" if frozen_done else "draft; frozen manifest written by sessions freeze once pending checks and reviews complete",
        repository=s.REPOSITORY,
        configurations=list(CONFIGURATIONS),
        threshold=THRESHOLD,
        confidence=CONFIDENCE,
        decision_rule=DECISION_RULE,
        cutoff=ep.CUTOFF_ISO,
        selected_criteria=list(ev.SELECTED_CRITERIA),
        session_budget={p: dict(slots=[r.start, r.stop - 1], count=len(r)) for p, r in PHASES.items()},
        maximum_sessions=MAX_SESSIONS,
        selection=dict(
            order=f"ascending sha256('{s.ORDER_SALT}|' + task_id)",
            sample=SAMPLE,
            target_filter=f"included PRs with createdAt, mergedAt, and all closingIssuesReferences createdAt >= {ep.CUTOFF_ISO}",
            planned=planned,
            eligibility_status=chosen["status"],
            blockers=chosen["blockers"],
        ),
        pools=pools,
        selected=chosen["selected"] if not chosen["blockers"] else dict(pilot=[], source=[], target=[]),
        historical_overlaps=dict(found=overlaps),
    )
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    (PROTOCOL / "requirement-draft.json").write_text(
        json.dumps(requirement_draft(planned), indent=2) + "\n", encoding="utf-8"
    )
    (PROTOCOL / "protocol.md").write_text(protocol_markdown(planned), encoding="utf-8")
    write_prompts_and_configs(planned)

    forms = s.audit_forms()
    forms["B28a-release"]["session_control"] = dict(
        kind="no_scoring_file_changes",
        description="Code confirms for every retained observation that its patch modifies no SCORING_FILE runner or config.",
    )
    for name, form in forms.items():
        with contextlib.suppress(FileExistsError):
            s.save_new(PROTOCOL / "audit_forms" / f"{name}.json", form)
    gemini_form = PROTOCOL / "audit_forms" / "B14b-CONFIG_01_GEMINI_FLASH_MED.json"
    if gemini_form.exists() and "CONFIG_01_GEMINI_FLASH_MED" not in CONFIGURATIONS:
        sup = PROTOCOL / "audit_forms" / "superseded"
        sup.mkdir(parents=True, exist_ok=True)
        gemini_form.rename(sup / gemini_form.name)
        reason_path = sup / "B14b-CONFIG_01_GEMINI_FLASH_MED.reason.json"
        if not reason_path.exists():
            s.save_new(
                reason_path,
                dict(
                    form="B14b-CONFIG_01_GEMINI_FLASH_MED",
                    moved_at=s.now(),
                    reason="Single-configuration Protocol 6 uses CONFIG_02_SOL_MED only (standby template preserved).",
                ),
            )
    with contextlib.suppress(FileExistsError):
        s.save_new(PROTOCOL / "audit_forms" / "ABC-release.json", s.abc_blank(PROTOCOL / "abc-items.json"))

    (PROTOCOL / "task_checks.json").write_text(
        json.dumps(task_check_ledger(planned, results), indent=2) + "\n", encoding="utf-8"
    )
    with contextlib.suppress(FileExistsError):
        s.save_new(PROTOCOL / "blind_b07_sheet.json", blind_b07_template(planned["source"] + planned["target"]))

    build_gate_outcomes_demo(PROTOCOL)

    templates = s.result_templates(sample=SAMPLE)
    for name, data in templates.items():
        with contextlib.suppress(FileExistsError):
            s.save_new(PROTOCOL / "templates" / f"{name}.json", data)
    tables_md = [
        "# Protocol 6 result templates (no agent sessions run)",
        "",
        "## Planned arms",
        "",
        "M1, M2, Audit only, ABA, All-passing-incomplete, M3_strict, M3_lenient, M3_controlled, ABC, ABC_with_gate, Target (before & after removal).",
        "",
        s.markdown_table(
            templates["decisions"]["rows"],
            ["config_id", "source_n", "M2_decision", "M3_strict_status", "M3_controlled_status", "M3_controlled_decision",
             "ABC_decision", "ABC_with_gate_status", "target_n", "target_decision"],
        ),
    ]
    tables_path = PROTOCOL / "templates" / "result_tables.md"
    if not tables_path.exists():
        tables_path.write_text("\n".join(tables_md) + "\n", encoding="utf-8")

    ledger_summary = make_ledger().summary()
    caps = s.capability_report({})
    probe_count = len(ep.ProbeLedger(PROTOCOL / "probe_ledger").load_all())
    readiness_lines = [
        "# Protocol 6 readiness",
        "",
        "Generated by `python -m paper2.preparation.protocol6 prepare`.",
        "",
        "## Sample & Eligibility",
        "",
        f"- Source pool (`swe_bench_verified_release.json`): `{len(pools['source'])}` tasks; pilot `{planned['pilot']}`, source planned `{len(planned['source'])}` (`{planned['eligibility_counts']['source']}`).",
        f"- Strict post-cutoff target pool (`>= {ep.CUTOFF_ISO}`): `{len(pools['target'])}` tasks (`{len(pools['excluded_pre_cutoff'])}` pre-cutoff excluded); target planned `{len(planned['target'])}` (`{planned['eligibility_counts']['target']}`).",
        f"- Current selection state: `{chosen['status']}`" + (f" (`{'; '.join(chosen['blockers'])}`)" if chosen["blockers"] else ""),
        "",
        "## Controls & Pending Execution",
        "",
        f"- Sessions recorded: `{ledger_summary['used']}` of `{MAX_SESSIONS}`.",
        f"- B14b exposure probes recorded: `{probe_count}`.",
        "- Pre-freeze gates remaining before live agent sessions: B28a Protocol 6 check, isolated MESA rating runs + model B07 scope judgments + `sign-form`, `sign-requirement`, `freeze`, and phase authorizations.",
        "- Offline components verified: `POLICY-P6-CONTROLLED`, `exact_binomial` cut points, `abc_with_gate`, `exposure_probe.py`, forms, task check ledger (`task_checks.json`), blind B07 sheet (`blind_b07_sheet.json`), and `gate_outcomes_demo.json`.",
        "",
        "## Session budget",
        "",
        s.markdown_table(
            [dict(phase=p, slots=f"{r.start}-{r.stop - 1}", count=len(r)) for p, r in PHASES.items()],
            ["phase", "slots", "count"],
        ),
        "",
        "## Runtime capabilities",
        "",
        s.markdown_table([dict(capability=k, **v) for k, v in caps.items()], ["capability", "configuration_check", "runtime"]),
    ]
    (PROTOCOL / "readiness.md").write_text("\n".join(readiness_lines) + "\n", encoding="utf-8")
    return PROTOCOL / "readiness.md"


def refresh_checks() -> Path:
    """Refresh task_checks.json and readiness.md without disturbing a finalized selection."""
    from paper2.preparation import harness
    pools = build_pools()
    results = harness.load_results()
    planned = planned_task_lists(pools, results)
    chosen = s.select(pools, results, sample=SAMPLE)
    checks_path = PROTOCOL / "task_checks.json"
    checks_path.write_text(json.dumps(task_check_ledger(planned, results), indent=2) + "\n", encoding="utf-8")
    prepare_allowed = not ((PROTOCOL / "study_manifest.json").exists() and any(
        json.loads((PROTOCOL / "study_manifest.json").read_text(encoding="utf-8")).get("selected", {}).values()
    ))
    if prepare_allowed:
        return prepare()
    return checks_path


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare Protocol 6 (44+44 sample).")
    parser.add_argument("stage", choices=("prepare", "refresh-checks", "gate-demo", "launch"))
    parser.add_argument("--run-tests", action="store_true")
    args = parser.parse_args(argv)
    if args.stage == "launch":
        parser.error("Provider execution is disabled during Protocol 6 preparation; use sessions.py open/close.")
    if args.stage == "gate-demo":
        print(json.dumps(build_gate_outcomes_demo(PROTOCOL), indent=2))
        return 0
    if args.stage == "refresh-checks":
        print(refresh_checks())
        return 0
    print(prepare(run_tests=args.run_tests))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

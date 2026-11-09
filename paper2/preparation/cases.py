"""Case assembly for protocol 5 of Paper 2. Nothing here runs a model.

For each coding agent it builds one paper2-case/1 record from the source sessions, the signed rating forms, the
signed requirement, and that agent's transfer justification. RQ1: it gives the decision from the source tasks with
no review (M2), with an audit only (the tasks the checks flag left out, no criteria gate; also ABA's flags when
given), with MESA under the strict and the lenient policy (M3), and with ABC. RQ2: it compares each with the direct
test, the agent's results on the target tasks.

Session rules (protocol 5):
  - a completed session gives the observation that `sessions.py close` wrote; an invalid session is not resolved;
  - a reserve session replaces the session whose infrastructure failure it follows;
  - a session that did not complete and was not replaced counts as not resolved; its patch and provenance are the
    slot's ledger outcome record, which states the status;
  - every selected task needs a session; an open slot or a task without a session stops the analysis.
"""
import json
from pathlib import Path

from paper2.method import evidence as ev
from paper2.method.decision_engine import compute_wilson_score_interval, evaluate_decision_from_bounds
from paper2.preparation import study_controls as s

ROOT = Path(__file__).resolve().parents[2]
BASE = s.PROTOCOL
SESSIONS, LEDGER = BASE / "sessions", BASE / "ledger"
FORMS = BASE / "audit_forms" / "completed"
REQUIREMENT = BASE / "requirement.json"
RELEASE_FORMS = ("B05-release", "B07-release", "B12-release", "B14a-release", "B28a-release", "B28b-release")


def _rel(path):
    path = Path(path).resolve()
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def _origin_phase(ledger, slot):
    while slot["phase"] == "reserve":
        slot = ledger.slot(slot["replaces"])
    return slot["phase"]


def phase_observations(phase, config_id, ledger, sessions=SESSIONS):
    """One observation per task of the phase, from the last session for that task."""
    last = {}
    for n in range(1, s.MAX_SESSIONS + 1):
        slot = ledger.slot(n)
        if slot and slot["config_id"] == config_id and _origin_phase(ledger, slot) == phase:
            last[slot["task_id"]] = n  # a reserve slot has a higher number than the slot it replaces
    out = []
    for task_id, n in last.items():
        state = ledger.state(n)
        if state == "completed":
            out.append(json.loads((Path(sessions) / f"{n:02d}" / "session.json").read_text())["observation"])
        elif state in ("reserved", "started"):
            raise RuntimeError(f"Slot {n} ({task_id}) is still open; close or fail it first")
        else:
            record = Path(ledger.root) / f"{n:02d}.outcome.json"
            ref = dict(path=_rel(record), sha256=ev.sha256_file(record), task_id=task_id)
            out.append(dict(task_id=task_id, config_id=config_id, repository=s.REPOSITORY, resolved=False,
                            not_completed=ledger.outcome(n)["status"], patch=ref,
                            provenance=dict(session_id=f"protocol-{s.PROTOCOL_NUMBER}-slot-{n:02d}",
                                            log=ref["path"], log_sha256=ref["sha256"])))
    return out


def rate_difference(k1, n1, k2, n2):
    """95% interval of p1 - p2 for two independent proportions (Newcombe's hybrid score method, from Wilson bounds)."""
    if not (n1 and n2):
        return None
    p1, p2 = k1 / n1, k2 / n2
    (l1, u1), (l2, u2) = compute_wilson_score_interval(k1, n1), compute_wilson_score_interval(k2, n2)
    d = p1 - p2
    return [d - ((p1 - l1) ** 2 + (u2 - p2) ** 2) ** 0.5, d, d + ((u1 - p1) ** 2 + (p2 - l2) ** 2) ** 0.5]


def counts(observations, key="resolved"):
    k, n = sum(bool(o.get(key)) for o in observations), len(observations)
    lb, ub = compute_wilson_score_interval(k, n)
    return dict(n=n, successes=k, interval=[lb, ub])


def decision(c, threshold):
    return ev.rate_decision(c["successes"], c["n"], threshold)[0] if c["n"] else None


def agreement(source_decision, target_decision):
    """How a decision from the source tasks compares with the direct test's decision on the target tasks (RQ2)."""
    if source_decision is None or target_decision is None:
        return "No decision"
    if ev.INCONCLUSIVE in (source_decision, target_decision):
        return "Inconclusive"
    return "Agreement" if source_decision == target_decision else "Discrepancy"


INVALID_KINDS = (("study material", "study material"), ("oracle content", "oracle content"),
                 ("network commands", "network"), ("tools outside", "tools outside the agent's set"),
                 ("after the prompt", "message after the prompt"), ("agy files", "agent files changed"),
                 ("grading files", "grading files changed"))


def invalid_counts(observations):
    """A control: sessions whose transcript or patch shows an attempt to reach answers outside the task or to change
    the grading, by kind. Such sessions count as not resolved."""
    kinds = {}
    for o in observations:
        for reason in o.get("invalid_reasons") or []:
            label = next((name for key, name in INVALID_KINDS if key in reason), "other")
            kinds[label] = kinds.get(label, 0) + 1
    return dict(sessions=sum(1 for o in observations if o.get("invalid_reasons")), by_kind=kinds)


def abc_decision(record, observations, threshold):
    """ABC as its paper describes it (Zhu et al. 2025, Section 3 and Appendix F): each item scores 1 when met and 0
    otherwise, averaged over the applicable items of each part (T, O, R); the result is reported with its interval,
    and each unmet or unknown item is a caveat. ABC has no rule to withhold a result, so it always decides, on all
    source tasks (it has no rule for single tasks)."""
    scores = {}
    for i in record["items"]:
        if i["answer"] != "not_applicable":
            part = i["item_id"].split("-")[-1].split(".")[0]
            met, n = scores.get(part, (0, 0))
            scores[part] = (met + (i["answer"] == "met"), n + 1)
    caveats = [f"{i['item_id']} ({', '.join(i['concerns'])}): {i['answer'].replace('_', ' ')}" for i in record["items"]
               if i["answer"] in ("not_met", "unknown")]
    c = counts(observations)
    return dict(tasks=c, decision=decision(c, threshold), caveats=caveats,
                scores={part: dict(met=m, applicable=n, score=m / n) for part, (m, n) in sorted(scores.items())})


def _left_out_decision(observations, left_out, threshold):
    kept = [o for o in observations if o["task_id"] not in left_out]
    c = counts(kept)
    return dict(left_out=sorted(t for t in left_out if t in {o["task_id"] for o in observations}), tasks=c,
                decision=decision(c, threshold))


def build_case(config_id, policy, selection, requirement, forms, ledger, sessions=SESSIONS):
    tasks = selection["source"]
    observations = [o for o in phase_observations("source", config_id, ledger, sessions) if o["task_id"] in tasks]
    missing = [t for t in tasks if t not in {o["task_id"] for o in observations}]
    if missing:
        raise RuntimeError(f"{config_id}: source tasks without a session: {', '.join(missing)}")
    names = (*RELEASE_FORMS, f"B14b-{config_id}")
    return dict(schema_version=ev.CASE_SCHEMA, case_id=f"protocol-{s.PROTOCOL_NUMBER}-{config_id}-source-{policy['id']}",
                kind="upstream", config_id=config_id, source_repository=s.REPOSITORY, task_ids=list(tasks),
                requirement=dict(id=requirement["id"], text=requirement["text"],
                                 target_repository=requirement["target_repository"],
                                 threshold=requirement["threshold"], n_min=requirement.get("n_min")),
                observations=observations, policy=policy,
                evidence=[s.form_to_evidence(forms[name], list(tasks)) for name in names],
                transfer=requirement["transfer"][config_id])


def analyse(selection, requirement, forms, ledger, sessions=SESSIONS, abc=None, aba_flags=None):
    """One row per coding agent. RQ1: the decision from the source tasks with no review (M2), with an audit only
    (the tasks the checks flag left out, no criteria gate), with ABA's flags if given, with MESA (M3, strict and
    lenient: evidence status, what each blocking criterion is missing, and the decision on the kept tasks), and with
    ABC. RQ2: each against the direct test (the target tasks), with the difference in resolve rates; the direct test is
    also given without the target tasks whose issues were opened before the stated training cutoffs. The invalid
    sessions by kind and the resolve rate by test result alone are a control."""
    rows = []
    theta = requirement["threshold"]
    early = set(requirement.get("target_issues_before_cutoff") or [])
    for config_id in s.CONFIGURATIONS:
        strict = build_case(config_id, ev.default_policy(), selection, requirement, forms, ledger, sessions)
        lenient = build_case(config_id, ev.exploratory_policy(), selection, requirement, forms, ledger, sessions)
        methods = ev.compare_methods(strict)
        if "M1" not in methods:
            raise RuntimeError(f"{config_id}: the case was rejected: {methods['M3']['reasons']}")
        m3 = dict(strict=ev.evaluate_study_case(strict), lenient=ev.evaluate_exploratory_case(lenient))
        source_obs = strict["observations"]
        target = [o for o in phase_observations("target", config_id, ledger, sessions) if o["task_id"] in selection["target"]]
        missing = [t for t in selection["target"] if t not in {o["task_id"] for o in target}]
        target_counts = counts(target)
        target_decision = decision(target_counts, theta) if not missing else None
        every = source_obs + target + [o for o in phase_observations("pilot", config_id, ledger, sessions)]
        tests_only = counts(source_obs, key="tests_resolved")
        kept = m3["strict"]["observations"]  # both policies leave out the same tasks (task_defects reads the forms)
        row = dict(config_id=config_id,
                   source=dict(n=methods["M2"]["n"], successes=methods["M2"]["successes"], interval=methods["M2"]["interval"]),
                   M1=methods["M1"]["decision"], M2=methods["M2"]["decision"],
                   audit_only=dict(left_out=kept["left_out"], tasks=dict(n=kept["n"], successes=kept["successes"],
                                                                        interval=kept["interval"]),
                                   decision=m3["strict"]["performance_decision"]),
                   tests_only=dict(tests_only, decision=decision(tests_only, theta)),
                   invalid=invalid_counts(every),
                   target=dict(target_counts, decision=target_decision, tasks_without_session=missing))
        if aba_flags is not None:
            row["ABA"] = _left_out_decision(source_obs, set(aba_flags), theta)
        for policy, res in m3.items():
            case = strict if policy == "strict" else lenient
            missing_text = {ev.normalize_criterion(r["criterion"])[0]: r.get("missing") for r in case["evidence"]}
            blocking = {c: missing_text.get(c) for c, v in (res["criteria"] or {}).items()
                        if v["status"] in (ev.INADMISSIBLE, ev.INQUIRY)}
            every_task = (res["observations"] or {}).get("with_left_out") or {}
            row[f"M3_{policy}"] = dict(input_integrity=res["input_integrity"], evidence_status=res["evidence_status"],
                                       tasks=res["observations"], performance_decision=res["performance_decision"],
                                       decision_on_all_tasks=decision(every_task, theta) if every_task else None,
                                       score_decision=res["score_decision"], to_reach_decision=blocking,
                                       requirement_decision=res["requirement_decision"], reasons=res["reasons"])
        if abc is not None:
            row["ABC"] = abc_decision(abc, source_obs, theta)
        (slo, shi), (tlo, thi) = row["source"]["interval"], target_counts["interval"]
        row["intervals_overlap"] = bool(target_counts["n"]) and not (shi < tlo or thi < slo)
        k_t, n_t = target_counts["successes"], target_counts["n"]
        row["difference"] = dict(all_source_tasks=rate_difference(row["source"]["successes"], row["source"]["n"], k_t, n_t),
                                 kept_tasks=rate_difference(kept["successes"], kept["n"], k_t, n_t))
        if early:
            row["target_without_early"] = _left_out_decision(target, early, theta)
        row["agreement"] = dict(M2=agreement(row["M2"], target_decision),
                                audit_only=agreement(row["audit_only"]["decision"], target_decision),
                                M3_strict=agreement(row["M3_strict"]["requirement_decision"], target_decision),
                                M3_lenient=agreement(row["M3_lenient"]["requirement_decision"], target_decision),
                                M3_withheld=agreement(row["M3_strict"]["performance_decision"], target_decision),
                                **({"ABC": agreement(row["ABC"]["decision"], target_decision)} if abc is not None else {}),
                                **({"ABA": agreement(row["ABA"]["decision"], target_decision)} if aba_flags is not None else {}))
        rows.append(row)
    return rows


def main():
    manifest = json.loads((BASE / "frozen_manifest.json").read_text())
    requirement = json.loads(REQUIREMENT.read_text())
    forms = {p.stem: json.loads(p.read_text()) for p in sorted(FORMS.glob("*.json")) if p.stem != "ABC-release"}
    abc, aba = FORMS / "ABC-release.json", BASE / "audit_checks" / "aba-overlap.json"
    aba_flags = json.loads(aba.read_text())["flagged_source_tasks"] if aba.exists() else None
    print(json.dumps(analyse(manifest["selection"], requirement, forms, s.SessionLedger(LEDGER),
                             abc=json.loads(abc.read_text()) if abc.exists() else None, aba_flags=aba_flags), indent=2))


if __name__ == "__main__":
    main()

"""Evidence records that apply MESA ratings to requirement decisions (MESA rubric version 5).

A case record links a requirement, its evidence conditions, one coding agent (configuration), source observations
with artifact hashes, and one rating form per selected MESA criterion. Evaluation keeps three levels apart:

1. input integrity: valid or rejected (identity and hash checks, before capability);
2. evidence status: admissible, inadmissible, inquiry required, or not applicable;
3. decision: Accept, Reject, or Inconclusive from the resolve rate, made only when the evidence is admissible;
   otherwise no decision, with every blocking reason. The decision on the requirement also needs the
   transfer justification.

MESA levels are kept as labels. Nothing is scored or averaged. The earlier rule in
decision_engine.method3_task_matching_mesa is kept unchanged so that historical outputs keep their meaning.
"""
import hashlib
import json
import re
from pathlib import Path

from paper2.method.decision_engine import (
    compute_exact_binomial_interval,
    compute_wilson_score_interval,
    evaluate_decision_from_bounds,
)

ROOT = Path(__file__).resolve().parents[2]
CASE_SCHEMA = "paper2-case/1"
DECISION_SCHEMA = "paper2-decision/1"

# Frozen MESA v4 definitions. Rubric question Bnn answers shared concern Cnn for the
# five selected criteria (same wording in v4/rubric/rubric-draft.md and v4/mapping/concerns.md).
FROZEN_DEFINITIONS = {
    "v5/rubric/rubric-v5.1.md": "023058fcfa3190a5ab17b55f71990d33c661b0c606a6f76b9b55d46611420cdf",  # mesa-rubric-v5.1
    "v5/rubric/rubric.md": "8d60dee59cba49d8c6ec9f27c13c4acb8d2983cce4c0b908df424159002a14ba",  # mesa-rubric-v5
    "v4/rubric/rubric-draft.md": "7ac2ed6e02230af818fc0ccde0105837c81bba5491e2d351d6f1f41205850c74",
    "v4/mapping/concerns.md": "ed9865c47429ae71244641c8b77b850ea8aab708de067da5e30d55705234f2f8",
}
RUBRIC = "v5/rubric/rubric-v5.1.md"  # the MESA rubric Paper 2 cites (v5 plus the outcome rule of feedback item 15)
SELECTED_CRITERIA = ("B05", "B07", "B12", "B14a", "B14b", "B28a", "B28b")  # MESA rubric version 5
CRITERION_CONCERN = {"B05": "C05", "B07": "C07", "B12": "C12", "B14a": "C14", "B14b": "C14", "B28a": "C28",
                     "B28b": "C28"}
# Earlier records name concerns (C05 ...) or the version 4 criteria B14 and B28; they are read as history only.
CONCERN_ALIASES = {"C05": "B05", "C07": "B07", "C12": "B12", "C14": "B14b", "C28": "B28a", "B14": "B14b",
                   "B28": "B28a"}

# Paper 1 labels are used here. The frozen rubric names the same anchors differently.
ANCHOR_ALIASES = {"Stated": "Claimed", "Shown": "Documented", "Checked": "Verified",
                  "Insufficient evidence": "Undocumented"}
ANCHORS = ("Claimed", "Documented", "Verified", "Contradicted", "Undocumented", "Not applicable")
POSITIVE_ORDER = ("Claimed", "Documented", "Verified")  # only used to compare with a required minimum
# Frozen rubric "Applies when" column: these criteria apply always and cannot be marked not applicable.
ALWAYS_APPLIES = ("B05", "B12", "B14a", "B14b")  # B14b applies whenever a configuration is named
SCOPE_LEVELS = ("release", "configuration", "task", "subset")
CHECK_OUTCOMES = ("passed", "failed", "not_performed", "not_recorded")
CHECK_KINDS = ("reported_by_sources", "run_by_reviewer", "both", "none")
TASK_DEFECT_DIRECTIONS = {"B05": "rejects_correct_solution", "B07": "accepts_wrong_solution"}
CASE_KINDS = ("upstream", "synthetic_fixture", "historical_record", "constructed_variant")

VALID, REJECTED = "valid", "rejected"
ADMISSIBLE, INADMISSIBLE = "admissible", "inadmissible"
INQUIRY, NOT_APPLICABLE = "inquiry required", "not applicable"
# MESA's score decision, made only when the evidence status is admissible; otherwise there is no decision (None).
ACCEPT, REJECT, INCONCLUSIVE = "Accept", "Reject", "Inconclusive"
DECISION_NAMES = {"Supported": ACCEPT, "Contradicted": REJECT, "Unresolved": INCONCLUSIVE}  # decision_engine's names


def sha256_file(path):
    return hashlib.sha256(resolve(path).read_bytes()).hexdigest()


def resolve(path):
    p = Path(path)
    return p if p.is_absolute() else ROOT / p


def case_digest(case):
    return hashlib.sha256(json.dumps(case, sort_keys=True).encode()).hexdigest()


def normalize_criterion(identifier):
    """Return (Bnn, historical identifier or None). Unknown identifiers raise."""
    if identifier in CRITERION_CONCERN:
        return identifier, None
    if identifier in CONCERN_ALIASES:
        return CONCERN_ALIASES[identifier], identifier
    raise ValueError(f"Unknown MESA criterion {identifier!r}")


def normalize_anchor(anchor):
    return ANCHOR_ALIASES.get(anchor, anchor)


def policy_digest(policy):
    return hashlib.sha256(json.dumps(policy, sort_keys=True).encode()).hexdigest()


def counterexample_demonstrated(cx):
    """True only for an executed counterexample: the oracle accepted a patch that an
    independent behavior check rejected, and the saved log still matches its hash."""
    if not cx or not cx.get("result"):
        return False
    res = cx["result"]
    if res.get("oracle_outcome") != "pass" or res.get("behavior_check") != "fail":
        return False
    log = res.get("log") or {}
    try:
        return bool(log.get("path")) and sha256_file(log["path"]) == log.get("sha256")
    except OSError:
        return False


def _task_defect_shown(defect, crit):
    """A defect on one task counts when it names the direction its criterion covers (B05: the tests reject a correct
    solution; B07: they accept a wrong one), cites a location and a quote, and, if it carries a patch, that patch was
    executed and its log still matches (MESA rubric version 5)."""
    cx = defect.get("counterexample")
    return (defect.get("direction") == TASK_DEFECT_DIRECTIONS.get(crit) and bool(defect.get("task_id"))
            and bool(defect.get("evidence_location")) and bool(defect.get("quote"))
            and (cx is None or counterexample_demonstrated(cx)))


def task_defects(case):
    """Tasks that a rating form shows to have defective tests (B05: tests reject a correct fix; B07: tests accept a
    patch that breaks the issue). Returns {task: [reason]}. MESA rubric version 5 leaves these tasks out before any
    score is seen and reports the score with and without them."""
    shown = {}
    for rec in case["evidence"]:
        crit = normalize_criterion(rec.get("criterion"))[0]
        for d in rec.get("task_defects") or []:
            if _task_defect_shown(d, crit):
                shown.setdefault(d["task_id"], []).append(
                    f"{crit}: {d.get('summary') or 'defective tests'} ({d['evidence_location']})")
    return shown


def has_provenance(obs):
    prov = obs.get("provenance") or {}
    return all(prov.get(k) for k in ("session_id", "log", "log_sha256"))


def default_policy(policy_id="POLICY-P5-STRICT"):
    """Strict policy: every selected criterion needs a passed check at Verified within scope."""
    condition = dict(min_anchor="Verified", check_outcome="passed",
                     scope_levels=["release", "configuration", "task", "subset"],
                     required_fields=["procedure", "kind", "evidence_location", "detection_limits"])
    return dict(id=policy_id, conditions={c: dict(condition) for c in SELECTED_CRITERIA},
                require_execution_provenance=True)


def exploratory_policy(policy_id="POLICY-P5-LENIENT"):
    """Lenient policy: test quality, scoring, and both environments; B07 may be Documented. It leaves out B12 and
    the two exposure criteria (B14a, B14b)."""
    fields = ["procedure", "kind", "evidence_location", "detection_limits"]
    scopes = ["release", "configuration", "task", "subset"]
    conditions = {c: dict(min_anchor="Documented" if c == "B07" else "Verified", check_outcome="passed",
                          scope_levels=scopes, required_fields=fields) for c in ("B05", "B07", "B28a", "B28b")}
    return dict(id=policy_id, conditions=conditions, require_execution_provenance=True)


# Files that run or configure SymPy's tests. The harness runs the patched repository's own runner, so a patch that
# changes one of these can change its own grade (rubric B28a); no reference fix of the selected tasks touches them.
SCORING_FILE = re.compile(r"(^bin/test$|(^|/)runtests\.py$|(^|/)conftest\.py$|^pytest\.ini$|^setup\.cfg$|^tox\.ini$"
                          r"|^sympy/(testing|utilities)/pytest\.py$)")


def scoring_files(patch):
    """The test-running files a patch changes (both sides of every diff header)."""
    files = re.findall(r"^diff --git a/(\S+) b/(\S+)$", patch or "", re.M)
    return sorted({f for pair in files for f in pair if SCORING_FILE.search(f)})


def controlled_policy(policy_id="POLICY-P6-CONTROLLED"):
    """Protocol 6 controlled policy: treats B12, B14a, and B14b as the lenient policy does, and makes B28a
    Admissible for a case when code confirms, for every retained observation, that the patch changes no test
    runner and no test configuration file."""
    policy = exploratory_policy(policy_id=policy_id)
    policy["conditions"]["B28a"]["session_control"] = dict(
        kind="no_scoring_file_changes",
        check="no_test_runner_or_config_modified",
    )
    return policy


# ---------------------------------------------------------------- level 1

def _check_hash(path, expected, label, reasons):
    try:
        actual = sha256_file(path)
    except OSError:
        reasons.append(f"{label}: artifact {path} is missing")
        return
    if actual != expected:
        reasons.append(f"{label}: stale artifact hash for {path}")


def check_integrity(case, required_policy=None):
    """Return reasons for rejection. An empty list means the input is valid."""
    reasons = []
    if required_policy is not None and policy_digest(case.get("policy") or {}) != policy_digest(required_policy):
        reasons.append("Case policy differs from the pinned study policy")
    if case.get("schema_version") != CASE_SCHEMA:
        return [f"Unknown case schema {case.get('schema_version')!r}"]
    for key in ("case_id", "kind", "requirement", "config_id", "source_repository",
                "task_ids", "observations", "policy", "evidence"):
        if key not in case:
            reasons.append(f"Missing field {key}")
    if reasons:
        return reasons
    if case["kind"] not in CASE_KINDS:
        reasons.append(f"Unknown case kind {case['kind']!r}")
    req = case["requirement"]
    if not req.get("id") or not req.get("target_repository"):
        reasons.append("Requirement identifier or target repository missing")
    if not isinstance(req.get("threshold"), (int, float)) or not 0 < req["threshold"] < 1:
        reasons.append("Requirement threshold must lie in (0, 1)")

    conditions = case["policy"].get("conditions") or {}
    if not conditions:
        reasons.append("Policy lists no evidence conditions")
    for name, cond in conditions.items():
        try:
            normalize_criterion(name)
        except ValueError as e:
            reasons.append(str(e))
        if cond.get("min_anchor") not in POSITIVE_ORDER:
            reasons.append(f"{name}: policy minimum anchor must be one of {POSITIVE_ORDER}")
        if cond.get("check_outcome") != "passed":
            reasons.append(f"{name}: policy must require a passed check")

    declared = case["task_ids"]
    if len(set(declared)) != len(declared):
        reasons.append("Duplicate declared task identifiers")
    seen, patches = [], []
    for obs in case["observations"]:
        tid = obs.get("task_id")
        if obs.get("config_id") != case["config_id"]:
            reasons.append(f"Identity mismatch: observation {tid} belongs to configuration {obs.get('config_id')!r}")
        if tid not in declared:
            reasons.append(f"Identity mismatch: observation task {tid!r} is not declared for this case")
        if obs.get("repository") != case["source_repository"]:
            reasons.append(f"Identity mismatch: observation {tid} comes from {obs.get('repository')!r}")
        if not isinstance(obs.get("resolved"), bool):
            reasons.append(f"Observation {tid} lacks a resolved outcome")
        patch = obs.get("patch") or {}
        if not patch.get("path") or not patch.get("sha256"):
            reasons.append(f"Observation {tid} lacks patch identity")
        else:
            if patch.get("task_id") != tid:
                reasons.append(f"Identity mismatch: observation {tid} cites the patch of task {patch.get('task_id')!r}")
            _check_hash(patch["path"], patch["sha256"], f"Observation {tid} patch", reasons)
            patches.append(patch["sha256"])
        for path, expected in (obs.get("artifacts") or {}).items():
            _check_hash(path, expected, f"Observation {tid}", reasons)
        prov = obs.get("provenance") or {}
        if prov.get("log_sha256"):  # a log without its hash counts as missing provenance (level 2)
            _check_hash(prov.get("log") or "", prov["log_sha256"], f"Observation {tid} execution log", reasons)
        seen.append(tid)
    if len(set(seen)) != len(seen):
        reasons.append("Duplicate observations for one task")
    if len(set(patches)) != len(patches):
        reasons.append("Identity mismatch: two observations cite the same patch")
    missing = [t for t in declared if t not in seen]
    if missing:
        reasons.append(f"Declared tasks without observations: {', '.join(missing)}")

    by_criterion = {}
    for rec in case["evidence"]:
        try:
            crit, _ = normalize_criterion(rec.get("criterion"))
        except ValueError as e:
            reasons.append(str(e))
            continue
        if rec.get("concern") != CRITERION_CONCERN[crit]:
            reasons.append(f"{crit} record cites concern {rec.get('concern')!r}; expected {CRITERION_CONCERN[crit]}")
        ref = rec.get("definition") or {}
        if ref.get("path") not in FROZEN_DEFINITIONS or FROZEN_DEFINITIONS[ref["path"]] != ref.get("sha256"):
            reasons.append(f"{crit} record does not cite a frozen MESA definition")
        elif sha256_file(ref["path"]) != ref["sha256"]:
            reasons.append(f"{crit} frozen definition file changed")
        if normalize_anchor(rec.get("anchor")) not in ANCHORS + (None,):
            reasons.append(f"{crit} record has unknown anchor {rec.get('anchor')!r}")
        if (rec.get("check") or {}).get("outcome") not in CHECK_OUTCOMES + (None,):
            reasons.append(f"{crit} record has unknown check outcome")
        if (rec.get("check") or {}).get("kind") not in CHECK_KINDS + (None,):
            reasons.append(f"{crit} record has unknown check kind")
        for path, expected in (rec.get("artifacts") or {}).items():
            _check_hash(path, expected, f"{crit} record", reasons)
        for d in rec.get("task_defects") or []:
            for path, expected in (d.get("artifacts") or {}).items():
                _check_hash(path, expected, f"{crit} task defect {d.get('task_id')}", reasons)
        if crit in by_criterion:
            reasons.append(f"More than one review record for {crit}")
        by_criterion[crit] = rec
    return reasons


# ---------------------------------------------------------------- level 2

def _covers(scope, case):
    gaps = []
    configs = scope.get("config_ids") or []
    if "*" not in configs and case["config_id"] not in configs:
        gaps.append(f"scope does not cover configuration {case['config_id']}")
    tasks = scope.get("task_ids") or []
    if "*" not in tasks:
        outside = [t for t in case["task_ids"] if t not in tasks]
        if outside:
            gaps.append(f"scope does not cover tasks {', '.join(outside)}")
    return gaps


def _record_metadata_gaps(crit, cond, rec, case):
    """Check scope, required fields, roles, and cited task defects for one criterion record."""
    check = rec.get("check") or {}
    unmet = []
    scope = rec.get("scope") or {}
    if scope.get("level") not in cond.get("scope_levels", SCOPE_LEVELS):
        unmet.append(f"scope level {scope.get('level')!r} not accepted")
    unmet += _covers(scope, case)
    unmet += [f"missing {f}" for f in cond.get("required_fields", []) if not check.get(f)]
    roles = rec.get("roles") or {}
    if not roles.get("author") or "assistant" not in roles:
        unmet.append("author or assistant role not recorded")
    unmet += [f"defect claimed for {d.get('task_id')} without its direction, a cited location and quote, or an executed patch"
              for d in rec.get("task_defects") or [] if not _task_defect_shown(d, crit)]
    return unmet


def _verify_session_control(crit, ctrl, rec, case):
    """Verify a case-level control over every retained observation (observations matched to target and not left out).

    Returns (violation_reasons, unmet_reasons, retained_count).
    """
    violations, unmet = [], []
    if "session_control" in rec:
        form_ctrl = rec.get("session_control")
        if not isinstance(form_ctrl, dict) or form_ctrl.get("kind") != ctrl.get("kind") or not (
                form_ctrl.get("description") or form_ctrl.get("control")):
            unmet.append(f"session_control does not match {ctrl.get('kind')}")
    defects = task_defects(case)
    retained = [o for o in matched_observations(case) if o.get("task_id") not in defects]
    for obs in retained:
        tid = obs.get("task_id")
        prov_ctrl = ((obs.get("provenance") or {}).get("controls") or {}).get(ctrl["kind"])
        if isinstance(prov_ctrl, dict):
            if prov_ctrl.get("passed") is False or prov_ctrl.get("changed_files"):
                files = ", ".join(prov_ctrl.get("changed_files") or ["recorded control failure"])
                violations.append(f"{tid} ({files})")
                continue
            if not isinstance(prov_ctrl.get("passed"), bool):
                unmet.append(f"session control record invalid for {tid}")
        patch_path = (obs.get("patch") or {}).get("path")
        if not patch_path:
            unmet.append(f"patch missing for {tid} to verify {ctrl['kind']}")
            continue
        try:
            patch_text = resolve(patch_path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            unmet.append(f"patch unreadable for {tid} to verify {ctrl['kind']}")
            continue
        hits = scoring_files(patch_text)
        if hits:
            violations.append(f"{tid} ({', '.join(hits)})")
    return violations, unmet, len(retained)


def criterion_status(crit, cond, rec, case):
    """Evidence status and reasons for one criterion under the requirement's conditions."""
    if rec is None:
        return INQUIRY, [f"{crit}: no review record"]
    applicability = rec.get("applicability") or {}
    anchor = normalize_anchor(rec.get("anchor"))
    check = rec.get("check") or {}
    if applicability.get("applies") is False or anchor == "Not applicable":
        if crit in ALWAYS_APPLIES:
            return INQUIRY, [f"{crit}: marked not applicable, but the frozen rubric applies it always"]
        if applicability.get("applies") is False and anchor in ("Not applicable", None) and applicability.get("reason"):
            return NOT_APPLICABLE, [f"{crit}: not applicable ({applicability['reason']})"]
        return INQUIRY, [f"{crit}: not applicable without a consistent recorded reason"]
    ctrl = cond.get("session_control")
    if anchor == "Contradicted" or check.get("outcome") == "failed":
        if "counterexample" in rec and not counterexample_demonstrated(rec["counterexample"]):
            return INQUIRY, [f"{crit}: defect claimed, but its counterexample has not been executed and preserved"]
        if not check.get("evidence_location"):
            return INQUIRY, [f"{crit}: defect reported without a cited location"]
        if not ctrl:
            return INADMISSIBLE, [f"{crit}: demonstrated defect at {check['evidence_location']}"]
        unmet = _record_metadata_gaps(crit, cond, rec, case)
        violations, ctrl_unmet, n_retained = _verify_session_control(crit, ctrl, rec, case)
        if violations:
            return INADMISSIBLE, [f"{crit}: session control {ctrl['kind']} violated by " + "; ".join(violations)]
        unmet += ctrl_unmet
        if unmet:
            return INQUIRY, [f"{crit}: {u}" for u in unmet]
        return ADMISSIBLE, [f"{crit}: {ctrl['kind']} confirmed for {n_retained} retained observations within recorded detection limits"]
    unmet = []
    minimum = cond["min_anchor"]
    if anchor not in POSITIVE_ORDER or POSITIVE_ORDER.index(anchor) < POSITIVE_ORDER.index(minimum):
        unmet.append(f"rating {anchor or 'missing'} is below the required {minimum}")
    if check.get("outcome") != cond["check_outcome"]:
        unmet.append(f"check outcome {check.get('outcome') or 'not recorded'}; requirement needs {cond['check_outcome']}")
    unmet += _record_metadata_gaps(crit, cond, rec, case)
    if ctrl:
        violations, ctrl_unmet, _ = _verify_session_control(crit, ctrl, rec, case)
        if violations:
            return INADMISSIBLE, [f"{crit}: session control {ctrl['kind']} violated by " + "; ".join(violations)]
        unmet += ctrl_unmet
    if unmet:
        return INQUIRY, [f"{crit}: {u}" for u in unmet]
    return ADMISSIBLE, [f"{crit}: conditions met within recorded detection limits"]


def evidence_status(case):
    criteria = {}
    records = {normalize_criterion(r["criterion"])[0]: r for r in case["evidence"]}
    for name, cond in case["policy"]["conditions"].items():
        crit, historical = normalize_criterion(name)
        status, reasons = criterion_status(crit, cond, records.get(crit), case)
        criteria[crit] = dict(status=status, reasons=reasons)
        if historical:
            criteria[crit]["historical_id"] = historical
    blocking = [r for c in criteria.values() if c["status"] in (INADMISSIBLE, INQUIRY) for r in c["reasons"]]
    provenance_missing = [o["task_id"] for o in case["observations"] if not has_provenance(o)]
    if case["policy"].get("require_execution_provenance") and provenance_missing:
        blocking.append("Execution provenance missing for tasks " + ", ".join(provenance_missing))
    statuses = [c["status"] for c in criteria.values()]
    if INADMISSIBLE in statuses:
        aggregate = INADMISSIBLE  # defect takes precedence; missing information stays in the reasons
    elif INQUIRY in statuses or (case["policy"].get("require_execution_provenance") and provenance_missing):
        aggregate = INQUIRY
    elif all(s == NOT_APPLICABLE for s in statuses):
        aggregate = NOT_APPLICABLE
        blocking.append("No applicable criterion; the policy cannot establish admissibility")
    else:
        aggregate = ADMISSIBLE
    return aggregate, criteria, blocking


# ---------------------------------------------------------------- level 3

def transfer_reasons(case):
    """Reasons that block applying the source decision to the requirement."""
    t = case.get("transfer")
    if not t:
        return ["No transfer justification from source tasks to the target requirement"]
    reasons = []
    if not t.get("justification") or not t.get("author"):
        reasons.append("Transfer justification or author missing")
    target = t.get("target_scope") or {}
    if target.get("repository") != case["requirement"]["target_repository"]:
        reasons.append("Transfer target scope does not match the requirement repository")
    if target.get("config_id") != case["config_id"]:
        reasons.append("Transfer target scope does not match the configuration")
    if (t.get("source_scope") or {}).get("repository") != case["source_repository"]:
        reasons.append("Transfer source scope does not match the source observations")
    return reasons


def matched_observations(case):
    """M2's subset: source observations from the requirement's repository. M3 uses the same, less the tasks whose
    tests a rating form shows to be defective (task_defects)."""
    return [o for o in case["observations"] if o["repository"] == case["requirement"]["target_repository"]]


def compute_interval(successes, total, confidence=0.95, decision_rule="wilson"):
    """Confidence bounds under the configured decision rule ('wilson' or 'exact_binomial')."""
    if decision_rule == "wilson":
        return compute_wilson_score_interval(successes, total, confidence=confidence)
    if decision_rule == "exact_binomial":
        return compute_exact_binomial_interval(successes, total, confidence=confidence, one_sided=True)
    if decision_rule == "exact_binomial_two_sided":
        return compute_exact_binomial_interval(successes, total, confidence=confidence, one_sided=False)
    raise ValueError(f"Unknown decision_rule {decision_rule!r}")


def rate_decision(k, n, theta, confidence=0.95, decision_rule="wilson"):
    """Resolve rate decision from confidence bounds: Accept, Reject, or Inconclusive (the interval holds theta)."""
    lb, ub = compute_interval(k, n, confidence=confidence, decision_rule=decision_rule)
    return (DECISION_NAMES[evaluate_decision_from_bounds(lb, ub, theta).value] if n else INCONCLUSIVE), [lb, ub]


def evaluate(case, required_policy=None):
    """Evaluate one case record (MESA rubric version 5 rules). Returns input integrity, the evidence status, the
    resolve rate decision on the tasks the decision uses, the score decision (only when the evidence is admissible;
    otherwise None, with every blocking reason), the requirement decision through the transfer justification, and
    the score with and without the tasks left out for broken tests."""
    out = dict(schema_version=DECISION_SCHEMA, case_id=case.get("case_id"), kind=case.get("kind"))
    rejected = check_integrity(case, required_policy)
    if rejected:
        out.update(input_integrity=REJECTED, reasons=rejected, evidence_status=None, criteria=None,
                   observations=None, performance_decision=None, score_decision=None, requirement_decision=None)
        return out
    aggregate, criteria, blocking = evidence_status(case)
    defects = task_defects(case)
    everything = matched_observations(case)
    left_out = {o["task_id"]: defects[o["task_id"]] for o in everything if o["task_id"] in defects}
    matched = [o for o in everything if o["task_id"] not in defects]
    k, n = sum(o["resolved"] for o in matched), len(matched)
    req = case["requirement"]
    theta = req["threshold"]
    rule = req.get("decision_rule", "wilson")
    conf = req.get("confidence", 0.95)
    performance, (lb, ub) = rate_decision(k, n, theta, confidence=conf, decision_rule=rule)
    reasons = list(blocking) + [f"Left out {t}: {'; '.join(r)}" for t, r in left_out.items()]
    n_min = req.get("n_min") or 1
    if aggregate == ADMISSIBLE and n < n_min:
        aggregate = INQUIRY
        reasons.append(f"Only {n} tasks remain after leaving out broken ones; the requirement needs at least {n_min}")
    if performance == INCONCLUSIVE:
        reasons.append(f"Interval [{lb:.3f}, {ub:.3f}] from {k}/{n} contains threshold {theta:.2f}" if n
                       else "No source observations match the requirement's repository")
    score = performance if aggregate == ADMISSIBLE else None
    transfer = transfer_reasons(case)
    if score is not None and transfer:
        reasons += transfer
    k_all = sum(o["resolved"] for o in everything)
    out.update(input_integrity=VALID, evidence_status=aggregate, criteria=criteria,
               observations=dict(n=n, successes=k, interval=[lb, ub], left_out=sorted(left_out),
                                 with_left_out=dict(n=len(everything), successes=k_all,
                                                    interval=list(compute_interval(
                                                        k_all, len(everything), confidence=conf, decision_rule=rule)))),
               performance_decision=performance, score_decision=score,
               requirement_decision=score if not transfer else None, transfer_reasons=transfer, reasons=reasons)
    return out


def evaluate_study_case(case):
    """Protocol 5, strict policy: the case must carry exactly the pinned strict (study) policy."""
    return evaluate(case, required_policy=default_policy())


def evaluate_exploratory_case(case):
    """Protocol 5, lenient policy: the case must carry exactly the pinned lenient (exploratory) policy."""
    return evaluate(case, required_policy=exploratory_policy())


def evaluate_controlled_case(case):
    """Protocol 6, controlled policy: the case must carry exactly the pinned controlled policy."""
    return evaluate(case, required_policy=controlled_policy())


def _bounds_decision(observations, theta, confidence=0.95, decision_rule="wilson"):
    k, n = sum(o["resolved"] for o in observations), len(observations)
    decision, interval = rate_decision(k, n, theta, confidence=confidence, decision_rule=decision_rule)
    return dict(decision=decision, n=n, successes=k, interval=interval)


def compare_methods(case):
    """M1 uses all source observations, M2 those from the requirement's repository (each a resolve rate decision
    without an evidence status), and M3 M2's observations less the tasks with broken tests, plus the evidence status.
    M1 equals M2 when every source observation is from the requirement's repository (the selected SymPy scope)."""
    result = evaluate(case)
    if result["input_integrity"] != VALID:
        return dict(M3=result)
    req = case["requirement"]
    theta = req["threshold"]
    rule = req.get("decision_rule", "wilson")
    conf = req.get("confidence", 0.95)
    return dict(M1=_bounds_decision(case["observations"], theta, confidence=conf, decision_rule=rule),
                M2=_bounds_decision(matched_observations(case), theta, confidence=conf, decision_rule=rule), M3=result)


# ---------------------------------------------------------------- migration

def migrate_v3_review(record, affected_configs=None):
    """Read a protocol 3 review record as an evidence record without changing its meaning.

    Protocol 3 records name concerns C05...C28 and do not record a check outcome, so the
    outcome stays 'not_recorded'. The original identifier and judgment are kept.
    """
    crit, historical = normalize_criterion(record["criterion"])
    configs = affected_configs or sorted({c.split("/")[0] for c in record.get("affected_cases", [])}) or ["*"]
    return dict(
        record_id=f"migrated-v3-{record['criterion']}-{record.get('scope')}",
        criterion=crit, concern=CRITERION_CONCERN[crit],
        definition=dict(path="v4/rubric/rubric-draft.md", sha256=FROZEN_DEFINITIONS["v4/rubric/rubric-draft.md"]),
        applicability=dict(applies=record["judgment"] != "Not applicable",
                           reason=record["rationale"] if record["judgment"] == "Not applicable" else ""),
        anchor=record["judgment"],
        scope=dict(level=record.get("scope"), config_ids=configs, task_ids=["*"]),
        check=dict(procedure=record.get("audit_execution", ""), outcome="not_recorded",
                   evidence_location=record.get("evidence_location", ""),
                   detection_limits=record.get("detection_limits", "")),
        reasons=record.get("rationale", ""),
        roles=dict(author=record.get("author", ""), assistant=record.get("assistant_role", "")),
        historical=dict(schema="paper2-review/v3", criterion=historical or record["criterion"],
                        judgment=record["judgment"], interpretation="Verified treated as supported by method3_task_matching_mesa"),
    )


def historical_ratings(records):
    """The rating dictionary the earlier engine read, keyed by the original C identifiers."""
    return {r["criterion"]: r["judgment"] for r in records}


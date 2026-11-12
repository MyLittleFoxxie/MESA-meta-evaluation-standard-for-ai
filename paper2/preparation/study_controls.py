"""Protocol 5 preparation for Paper 2: SymPy, two configurations, at most 90 sessions.

This module prepares the evaluation; it does not conduct it. Provider execution is
refused. It writes selection rules and pools, blank audit forms, result templates,
and a readiness report. No eligibility check, audit finding, replay, or session is
produced here.
"""
import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from paper2.method.evidence import (CHECK_KINDS, CRITERION_CONCERN, FROZEN_DEFINITIONS, RUBRIC, SCORING_FILE,
                                    SELECTED_CRITERIA, TASK_DEFECT_DIRECTIONS, ROOT, scoring_files, sha256_file)
from paper2.preparation.repository_runner import overlap
from paper2.preparation.replay import CONDITIONS, REPEATED_MEASURES_NOTE

PROTOCOL_NUMBER = "5"
# Protocol 5 amends protocol 4 (provenance/paper2-pilot-protocol-4-2026-11-06.md). Eligibility results, harness runs,
# and auditor checks stay in protocol-4/ and are shared; forms, freeze, ledger, and sessions are per protocol.
PROTOCOL = Path(__file__).resolve().parent / f"protocol-{PROTOCOL_NUMBER}"
PREPARATION_ONLY = True  # provider execution stays disabled until a frozen protocol enables it
REPOSITORY = "sympy/sympy"
CONFIGURATIONS = ("CONFIG_01_GEMINI_FLASH_MED", "CONFIG_02_SOL_MED")
# Fixed slot ranges make phase limits atomic: a phase can only create its own slot files.
PHASES = {"pilot": range(1, 3), "source": range(3, 43), "target": range(43, 83), "reserve": range(83, 91)}
MAX_SESSIONS = 90
SAMPLE = dict(pilot=1, source=20, target=20)
ORDER_SALT = "paper2-protocol-4"  # unchanged in protocol 5, so the selection does not move
TASK_KINDS = ("upstream", "synthetic_fixture", "historical_record", "constructed_variant")
SESSION_OUTCOMES = ("completed", "failed_start", "interrupted", "infrastructure_failure")
RUNTIME_CAPABILITIES = ("observed_model_identity", "timeout_900_seconds",
                        "oracle_isolation", "network_isolation", "operator_intervention", "resource_limits")
RUNTIME_RESULTS = ("enforced", "held", "violated", "not_observable")


def now():
    return datetime.now(timezone.utc).isoformat()


def save_new(path, data):
    """Create path with complete content or not at all; never replace an existing file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".tmp-")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        os.link(tmp, path)  # atomic; raises FileExistsError if path exists
    finally:
        os.unlink(tmp)


# ---------------------------------------------------------------- sessions

class BudgetExceeded(RuntimeError):
    pass


class SessionLedger:
    """Append-only ledger. Every reserved slot counts, whatever happens after it."""

    def __init__(self, root, phases=None, max_sessions=None):
        self.root = Path(root)
        self.phases = phases or PHASES
        self.max_sessions = max_sessions or MAX_SESSIONS

    def _path(self, n, suffix=""):
        return self.root / f"{n:02d}{suffix}.json"

    def _read(self, path):
        return json.loads(path.read_text()) if path.exists() else None

    def slot(self, n):
        return self._read(self._path(n))

    def outcome(self, n):
        return self._read(self._path(n, ".outcome"))

    def reserve(self, phase, config_id=None, task_id=None, replaces=None):
        if phase not in self.phases:
            raise ValueError(f"Unknown phase {phase!r}")
        marker = None
        if phase == "reserve":
            failed = self.outcome(replaces) if replaces else None
            if not failed or failed["status"] != "infrastructure_failure" or not failed.get("description"):
                raise ValueError("A reserve slot requires a recorded infrastructure failure")
            original = self.slot(replaces)
            config_id, task_id = original["config_id"], original["task_id"]
            marker = self.root / f"replaces-{replaces:02d}.json"
            try:
                save_new(marker, dict(replaces=replaces, timestamp=now()))
            except FileExistsError:
                raise ValueError(f"Session {replaces} has already been replaced") from None
        if config_id not in CONFIGURATIONS or not task_id:
            raise ValueError("Configuration and task are required")
        if phase != "reserve":  # a second launch of the same task is a retry and needs the reserve route
            marker = self.root / f"claim-{phase}-{config_id}-{hashlib.sha256(task_id.encode()).hexdigest()[:16]}.json"
            try:
                save_new(marker, dict(phase=phase, config_id=config_id, task_id=task_id, timestamp=now()))
            except FileExistsError:
                raise ValueError(f"{task_id} already has a {phase} session for {config_id}") from None
        for n in self.phases[phase]:
            try:
                save_new(self._path(n), dict(slot=n, phase=phase, config_id=config_id, task_id=task_id,
                                             replaces=replaces, reserved_at=now()))
                return n
            except FileExistsError:
                continue
        if marker:
            marker.unlink()
        raise BudgetExceeded(f"No {phase} slot left; the study allows at most {self.max_sessions} sessions")

    def claimed(self, phase, config_id, task_id):
        """True when this task already has a session in this phase for this configuration."""
        return (self.root / f"claim-{phase}-{config_id}-{hashlib.sha256(task_id.encode()).hexdigest()[:16]}.json").exists()

    def start(self, n):
        save_new(self._path(n, ".started"), dict(slot=n, started_at=now()))

    def finish(self, n, status, description=""):
        if not self._path(n).exists():
            raise ValueError(f"Session {n} was never reserved")
        if status not in SESSION_OUTCOMES:
            raise ValueError(f"Unknown session outcome {status!r}")
        if status == "infrastructure_failure" and not description:
            raise ValueError("Infrastructure failures need a description")
        save_new(self._path(n, ".outcome"), dict(slot=n, status=status, description=description, ended_at=now()))

    def state(self, n):
        if not self._path(n).exists():
            return None
        out = self.outcome(n)
        if out:
            return out["status"]
        return "started" if self._path(n, ".started").exists() else "reserved"

    def open_slots(self):
        """Slots reserved or started without a recorded outcome, e.g. after a restart.
        They stay counted and are never reused; classify them with finish()."""
        return [n for n in range(1, self.max_sessions + 1) if self.state(n) in ("reserved", "started")]

    def summary(self):
        states = {n: self.state(n) for n in range(1, self.max_sessions + 1) if self.state(n)}
        by_phase = {p: sum(1 for n in states if n in r) for p, r in self.phases.items()}
        return dict(used=len(states), maximum=self.max_sessions, by_phase=by_phase,
                    remaining={p: len(r) - by_phase[p] for p, r in self.phases.items()},
                    failed_starts=sum(s == "failed_start" for s in states.values()),
                    interruptions=sum(s == "interrupted" for s in states.values()),
                    infrastructure_failures=sum(s == "infrastructure_failure" for s in states.values()),
                    open=self.open_slots(), retries=by_phase["reserve"])


class OfflineStub:
    """The only adapter accepted during preparation."""

    def __init__(self, error=None):
        self.error = error

    def run(self, task_id, config_id):
        if self.error:
            raise RuntimeError(self.error)
        return dict(task_id=task_id, config_id=config_id, provider_called=False)


def launch(ledger, phase, config_id, task_id, adapter, replaces=None):
    """Reserve, start, run once, record. No automatic retry. An exception leaves the slot
    open; a person classifies it with finish(), because only a recorded infrastructure
    failure may use a reserve slot."""
    if PREPARATION_ONLY and type(adapter) is not OfflineStub:
        raise RuntimeError("Provider execution is disabled during preparation")
    n = ledger.reserve(phase, config_id, task_id, replaces)
    ledger.start(n)
    result = adapter.run(task_id, config_id)
    ledger.finish(n, "completed")
    return n, result


# ---------------------------------------------------------------- capabilities

def capability_report(configuration_checks, runtime_observations=(), ledger=None):
    """Configuration checks (file locations, telemetry fields, container flags) are reported
    but never establish a runtime capability. Runtime status needs an observation tied to a
    completed session in the ledger."""
    report = {}
    for cap in RUNTIME_CAPABILITIES:
        observed = [o for o in runtime_observations
                    if o.get("capability") == cap and o.get("kind") == "runtime_observation"
                    and ledger is not None and ledger.state(o.get("session_slot") or 0) == "completed"
                    and o.get("result") in RUNTIME_RESULTS]
        results = {o["result"] for o in observed}
        # enforced: a mechanism shown in the log; held: within the limit without enforcement
        runtime = ("awaiting experimental verification" if not observed else
                   "violated" if "violated" in results else
                   "not observable in some sessions" if "not_observable" in results else
                   "held in observed sessions" if "held" in results else "enforced in observed sessions")
        report[cap] = dict(configuration_check=configuration_checks.get(cap, "not checked"), runtime=runtime)
    return report


# ---------------------------------------------------------------- tasks

def order_key(task_id):
    return hashlib.sha256(f"{ORDER_SALT}|{task_id}".encode()).hexdigest()


def eligibility_state(task, result=None):
    """No result is pending, not a pass or failure. Only upstream tasks with a verified
    identity and a matching result can count toward repository eligibility."""
    if task.get("kind") != "upstream":
        return f"not countable ({task.get('kind')})"
    if task.get("identity_verified") is not True:
        return "identity not confirmed" if task.get("identity_checked") else "pending identity verification"
    if result is None:
        return "pending"
    if result.get("task_id") != task["task_id"] or result.get("task_kind") != "upstream":
        return "not countable (result does not belong to this upstream task)"
    return result["status"] if result.get("status") in ("eligible", "ineligible") else "pending"


def first_eligible(pool, results, need):
    """The first `need` eligible tasks in order_key order. A task before them that is still undecided (pending, or a
    harness failure) blocks, because deciding it could change the selection."""
    taken, blockers = [], []
    for t in sorted(pool, key=lambda t: t["order_key"]):
        if len(taken) == need:
            break
        state = eligibility_state(t, results.get(t["task_id"]))
        if state == "eligible":
            taken.append(t)
        elif state.startswith("pending"):
            blockers.append(f"{t['task_id']} is undecided ({state}) before the first {need} eligible tasks")
            break  # the selection cannot be known past an undecided task
    return taken, blockers


def select(pools, results, sample=None):
    """Deterministic and blind to model results: tasks in order_key order; pilot then source
    from the source pool, target from the target pool. Shortfalls and undecided earlier tasks block; nothing is
    substituted."""
    sample = sample or SAMPLE
    chosen = dict(pilot=[], source=[], target=[])
    source, blockers = first_eligible(pools["source"], results, sample["pilot"] + sample["source"])
    target, more = first_eligible(pools["target"], results, sample["target"])
    blockers += more
    chosen["pilot"] = [t["task_id"] for t in source[:sample["pilot"]]]
    chosen["source"] = [t["task_id"] for t in source[sample["pilot"]:sample["pilot"] + sample["source"]]]
    chosen["target"] = [t["task_id"] for t in target[:sample["target"]]]
    for role, need in sample.items():
        if len(chosen[role]) < need:
            blockers.append(f"{role}: {len(chosen[role])} of {need} eligible tasks")
    by_id = {t["task_id"]: t for t in pools["source"] + pools["target"]}
    shared = separation_problems({r: [by_id[i] for i in ids] for r, ids in chosen.items()})
    blockers += [f"{p['a']} ({p['a_role']}) and {p['b']} ({p['b_role']}) share {', '.join(p['reasons'])}" for p in shared]
    return dict(selected=chosen, blockers=blockers, status="blocked" if blockers else "selected")


def separation_problems(roles):
    """roles: {role: [task dicts]}. Reports shared identities across pilot, source, and target."""
    problems, names = [], list(roles)
    for i, a_role in enumerate(names):
        for b_role in names[i + 1:]:
            for a in roles[a_role]:
                for b in roles[b_role]:
                    found = overlap(a, b)
                    if found:
                        problems.append(dict(a=a["task_id"], a_role=a_role, b=b["task_id"], b_role=b_role, reasons=found))
    return problems


def build_pools():
    from tools.extract_swe_bench_verified import verify_local_release
    with contextlib.redirect_stdout(io.StringIO()):
        if not verify_local_release():
            raise RuntimeError("Pinned source release failed verification")
    release = json.loads((ROOT / "paper2/records/swe_bench_verified_release.json").read_text())
    # SWE-bench identifiers end in a pull request number. GitHub numbers issues and pull requests in one
    # sequence, so equal numbers denote one item; a pull request that fixes a target issue is only caught
    # once linked issues are recorded (pending).
    from tools.extract_swe_bench_verified import ROWS_DATASET, ROWS_REVISION
    source = [dict(task_id=x["instance_id"], repo=x["repo"], issue_id=x["instance_id"].rsplit("-", 1)[-1],
                   base_commit=x["base_commit"], kind="upstream", identity_verified=True,
                   origin=f"SWE-bench Verified, {ROWS_DATASET} revision {ROWS_REVISION}",
                   order_key=order_key(x["instance_id"]))  # eligibility comes from the saved results, not the pool
              for x in release["instances"] if x["repo"] == REPOSITORY]
    ledger = json.loads((ROOT / "paper2/preparation/v3/target_candidates.json").read_text())
    historical = [dict(task_id=t["task_id"], repo=t["repo"], issue_id=t["issue_id"], base_commit=t["base_commit"],
                       related_issues=t.get("related_issues", []), kind="historical_record", identity_verified=False,
                       origin="protocol 3 candidate ledger; constructed records, excluded from every role")
                  for t in ledger["tasks"] if t["repo"] == REPOSITORY]
    from paper2.preparation import targets
    pool = targets.load_pool() if targets.POOL.exists() else dict(prs=[])
    rows = targets.load_rows()
    target = []
    for pr in pool["prs"]:
        if not pr["included"]:
            continue
        row = rows.get(pr["task_id"]) or {}
        checks = row.get("identity_checks") or {}
        issues = [str(i["number"]) for i in pr["closingIssuesReferences"]["nodes"]]
        target.append(dict(task_id=pr["task_id"], repo=REPOSITORY, issue_id=issues[0],
                           related_issues=issues[1:] + [str(pr["number"])], base_commit=pr["baseRefOid"],
                           kind="upstream", identity_checked=bool(checks),
                           identity_verified=bool(checks) and all(v for k, v in checks.items() if k != "checked_at"),
                           origin=f"GitHub pull request {pr['url']}, merged {pr['mergedAt']}",
                           order_key=pr["order_key"]))
    specs = json.loads((ROOT / "paper2/preparation/v3/task_specs/pilot_tasks_manifest.json").read_text())["tasks"]
    fixtures = [dict(task_id=t["task_id"], repo=t["repo"], issue_id=t.get("issue_id"),
                     reference_patch_sha256=t.get("reference_patch_sha256"), kind="synthetic_fixture",
                     origin="protocol 3 micro-repository fixture; excluded from every study role")
                for t in specs]
    return dict(source=source, target=target, excluded_fixtures=fixtures, excluded_historical=historical)


# ---------------------------------------------------------------- audit forms

def rubric_rows():
    path = RUBRIC  # MESA rubric version 5; same table layout as version 4
    if sha256_file(path) != FROZEN_DEFINITIONS[path]:
        raise RuntimeError("Frozen rubric changed")
    rows = {}
    for line in (ROOT / path).read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] in SELECTED_CRITERIA:
            rows[cells[0]] = dict(question=cells[1], shown=cells[2], checked=cells[3], applies_when=cells[4])
    return rows


def blank_form(criterion, scope_level, config_ids):
    q = rubric_rows()[criterion]
    return dict(
        form_version="paper2-audit-form/1", status="pending", criterion=criterion,
        concern=CRITERION_CONCERN[criterion], definition=dict(path=RUBRIC, sha256=FROZEN_DEFINITIONS[RUBRIC]),
        question=q["question"], shown_means=q["shown"], checked_means=q["checked"], applies_when=q["applies_when"],
        repository=REPOSITORY, scope=dict(level=scope_level, config_ids=list(config_ids), task_ids=[]),
        applicability=dict(applies=None, reason=""),
        check=dict(procedure="", kind="", outcome="not_recorded", evidence_location="", detection_limits=""),
        evidence=[], anchor=None, reasons="", missing="", checks_performed=[], task_defects=[],
        roles=dict(author="", assistant=""),
        instructions=("Record evidence locations with short quotes, the check performed, its outcome, detection "
                      "limits, and reasons. The check outcome is the result of the check described in the procedure; "
                      "state whether the benchmark sources report it or the auditor performed it. A rating without "
                      "evidence and reasons is incomplete. Missing evidence is not a defect; a defect needs a cited "
                      "location, and an oracle defect needs an executed counterexample."))


# SCORING_FILE and scoring_files live in paper2.method.evidence so policies and preparation share one pattern.
ABC_ITEMS = PROTOCOL / "abc-items.json"
ABC_ANSWERS = ("met", "not_met", "not_applicable", "unknown")


def abc_items(out_path=None):
    """The ABC (Agentic Benchmark Checklist) items that the frozen v4 mapping assigns to the concerns of the five
    selected MESA concerns (C05, C07, C12, C14, C28). Written once to abc-items.json."""
    target = Path(out_path or ABC_ITEMS)
    if target.exists():
        return json.loads(target.read_text())
    import csv
    import re
    concerns = set(CRITERION_CONCERN.values())
    items = []
    for row in csv.DictReader(open(ROOT / "v4" / "mapping" / "mapping.csv")):
        hit = sorted(set(re.findall(r"C\d\d", row["final"] or "")) & concerns)
        if row["framework"] == "ABC" and hit:
            items.append(dict(item_id=row["item_id"], text=row["text"], concerns=hit))
    record = dict(record="paper2-abc-items/1", source="v4/mapping/mapping.csv (frozen MESA v4 mapping)",
                  framework="ABC: Agentic Benchmark Checklist (Zhu et al., NeurIPS 2025)",
                  rule="items mapped to C05, C07, C12, C14, or C28", items=items)
    save_new(target, record)
    return record


def abc_blank(items_path=None):
    return dict(form_version="paper2-abc-record/1", status="pending", criterion="ABC", benchmark="SWE-bench Verified",
                items=[dict(item_id=i["item_id"], concerns=i["concerns"], text=i["text"], answer=None, location="",
                            quote="", note="") for i in abc_items(items_path)["items"]],
                roles=dict(author="", assistant=""))


def validate_abc_record(form, items_path=None):
    """An ABC record answers every listed item: met or not met with a location and a quote; not applicable or
    unknown with a note."""
    listed = [i["item_id"] for i in abc_items(items_path)["items"]]
    problems = []
    if [i.get("item_id") for i in form.get("items") or []] != listed:
        problems.append("items differ from abc-items.json")
    if form.get("status") == "pending":
        return "pending"
    for i in form.get("items") or []:
        if i.get("answer") not in ABC_ANSWERS:
            problems.append(f"{i.get('item_id')}: answer")
        elif i["answer"] in ("met", "not_met") and not (i.get("location") and i.get("quote")):
            problems.append(f"{i['item_id']}: location and quote")
        elif i["answer"] in ("not_applicable", "unknown") and not i.get("note"):
            problems.append(f"{i['item_id']}: note")
    if not form.get("roles", {}).get("author"):
        problems.append("author")
    if problems:
        raise ValueError("Incomplete ABC record: " + ", ".join(problems))
    return "complete"


def audit_forms():
    forms = {f"{c}-release": blank_form(c, "release", ["*"]) for c in SELECTED_CRITERIA if c != "B14b"}
    forms.update({f"B14b-{cfg}": blank_form("B14b", "configuration", [cfg]) for cfg in CONFIGURATIONS})
    return forms


def validate_form(form):
    """Pending forms are valid as pending. A completed form must carry evidence and reasons."""
    if form.get("form_version") == "paper2-abc-record/1":
        return validate_abc_record(form)
    if form.get("status") == "pending":
        if form.get("anchor") or form.get("evidence") or form["check"].get("outcome") != "not_recorded":
            raise ValueError("A pending form must not contain findings")
        return "pending"
    problems = []
    if form.get("anchor") not in ("Claimed", "Documented", "Verified", "Contradicted", "Undocumented", "Not applicable"):
        problems.append("anchor")
    if not form.get("reasons"):
        problems.append("reasons")
    if not form.get("evidence") or not all(e.get("location") and e.get("quote") for e in form["evidence"]):
        problems.append("evidence locations with quotes")
    for key in ("procedure", "evidence_location", "detection_limits"):
        if not form["check"].get(key):
            problems.append(f"check {key}")
    if form["check"].get("outcome") not in ("passed", "failed", "not_performed"):
        problems.append("check outcome")
    if form["check"].get("kind") not in CHECK_KINDS:
        problems.append("check kind")
    for d in form.get("task_defects") or []:
        if d.get("direction") != TASK_DEFECT_DIRECTIONS.get(form.get("criterion")) or not (
                d.get("task_id") and d.get("evidence_location") and d.get("quote")):
            problems.append(f"task defect {d.get('task_id')}: direction, location, or quote")
    if form.get("applicability", {}).get("applies") is None:
        problems.append("applicability")
    if "session_control" in form:
        ctrl = form.get("session_control")
        if not isinstance(ctrl, dict) or not ctrl.get("kind") or not (ctrl.get("description") or ctrl.get("control")):
            problems.append("session_control")
    if not form.get("roles", {}).get("author"):
        problems.append("author")
    if problems:
        raise ValueError("Incomplete audit form: " + ", ".join(problems))
    return "complete"


def form_to_evidence(form, task_ids):
    validate_form(form)
    if form["status"] == "pending":
        raise ValueError("Pending forms supply no evidence")
    return dict(record_id=f"audit-{form['criterion']}-{form['scope']['level']}", criterion=form["criterion"],
                concern=form["concern"], definition=form["definition"], applicability=form["applicability"],
                anchor=form["anchor"], scope=dict(form["scope"], task_ids=form["scope"]["task_ids"] or task_ids),
                check=form["check"], reasons=form["reasons"], roles=form["roles"], evidence=form["evidence"],
                missing=form["missing"], repository=form["repository"],
                **{k: form[k] for k in ("counterexample", "task_defects", "session_control") if form.get(k)})


IGNORED_FIELDS = ("status", "roles", "signed_at")


def _field_changes(before, after, path=""):
    if isinstance(before, dict) and isinstance(after, dict):
        out = []
        for k in sorted(set(before) | set(after)):
            if path or k not in IGNORED_FIELDS:
                out += _field_changes(before.get(k), after.get(k), f"{path}.{k}" if path else k)
        return out
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after) and all(
            isinstance(x, dict) for x in before + after):
        return [c for i, (x, y) in enumerate(zip(before, after)) for c in _field_changes(x, y, f"{path}[{i}]")]
    return [] if before == after else [dict(field=path, run=before, signed=after)]


def signing_changes(runs=None, signed=None, out=None):
    """Field by field, where the forms the author signs differ from what the model runs wrote (a validation record,
    rewritten on each call). Before signing it compares the drafts; afterwards the completed forms."""
    base = PROTOCOL / "audit_forms"
    runs = runs or {**{p.stem: p for p in sorted((base / "rating-run-v5-A").glob("*.json"))},
                    "ABC-release": base / "abc-run" / "ABC-release.json"}
    signed = Path(signed or (base / "completed" if any((base / "completed").glob("*.json")) else base / "drafts"))
    forms = {}
    for name, path in runs.items():
        target = signed / f"{name}.json"
        if target.exists():
            forms[name] = _field_changes(json.loads(Path(path).read_text()), json.loads(target.read_text()))
    record = dict(record="paper2-signing-changes/1", compared=str(signed.relative_to(ROOT)) if signed.is_relative_to(ROOT)
                  else str(signed), made_at=now(), forms=forms,
                  changed_fields=sum(len(v) for v in forms.values()))
    out = Path(out or PROTOCOL / "audit_checks" / "signing-changes.json")
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return record


# ---------------------------------------------------------------- templates and report

def result_templates(sample=None):
    sample = sample or SAMPLE
    columns = ("source_n", "source_successes", "source_interval", "M2_decision",
               "audit_only_tasks", "audit_only_decision", "ABA_left_out", "ABA_decision",
               "M3_strict_status", "M3_strict_decision", "M3_lenient_status", "M3_lenient_decision",
               "M3_controlled_status", "M3_controlled_decision",
               "all_passing_incomplete_left_out", "all_passing_incomplete_decision",
               "M3_to_reach_decision", "M3_tasks_used", "M3_left_out", "M3_decision_before_status",
               "M3_decision_on_all_tasks", "ABC_decision", "ABC_scores", "ABC_caveats",
               "ABC_with_gate_status", "ABC_with_gate_decision",
               "tests_only_successes", "tests_only_decision", "invalid_sessions",
               "target_n", "target_successes", "target_interval", "target_decision", "target_without_early_decision",
               "target_after_removal_n", "target_after_removal_successes", "target_after_removal_decision",
               "difference_all_tasks", "difference_kept_tasks", "intervals_overlap",
               "agreement_M2", "agreement_audit_only", "agreement_ABA", "agreement_M3_strict", "agreement_M3_lenient",
               "agreement_M3_controlled", "agreement_M3_withheld", "agreement_ABC", "agreement_ABC_with_gate",
               "agreement_all_passing_incomplete", "reasons")
    decision_rows = [dict(config_id=c, **{k: "pending" for k in columns}) for c in CONFIGURATIONS]
    replay_rows = [dict(config_id=c, task=f"source task {i}", condition=k, input_integrity="pending",
                        evidence_status="pending", score_decision="pending", changed="pending", reasons="pending")
                   for c in CONFIGURATIONS for i in range(1, sample["source"] + 1) for k in CONDITIONS]
    notes = ["M1 and M2 coincide because every source task comes from SymPy; M2 is the resolve rate alone (no review).",
             "Decisions: Accept (lower bound at or above 0.70), Reject (upper bound below 0.70), or Inconclusive. MESA "
             "makes a score decision only when the evidence status is admissible; otherwise no decision, with what each "
             "blocking criterion is missing.",
             "With 20 tasks, Accept needs 19 or 20 resolved and Reject 9 or fewer; the requirement's minimum is 9 tasks.",
             "RQ1. Audit only: the tasks the checks show to be broken are left out, with no criteria gate (as automated "
             "audits use their findings); ABA: the tasks ABA flags with a major finding are left out. M3 leaves out the "
             "same tasks as the audit and adds the criteria; its decision before the evidence status equals the audit-only "
             "decision. ABC follows its paper: item scores per part, the decision on all source tasks, unmet or unknown "
             "items as caveats; it never withholds.",
             "RQ2. The direct test is the coding agent on the target tasks. Agreement compares each decision from the "
             "source tasks with the direct test's decision: Agreement, Discrepancy, Inconclusive (either is "
             "Inconclusive), or No decision. M3 withheld: MESA's decision before the evidence status against the direct "
             "test. The difference is source minus target resolve rate with a 95% Newcombe interval. The direct test is "
             "also given without the target tasks whose issues were opened before the stated training cutoffs.",
             "Control: invalid sessions by kind, and the resolve rate if they were counted by their test result.",
             "Built by paper2/preparation/cases.py."]
    return dict(decisions=dict(status="template; no results", notes=notes, rows=decision_rows),
                replay=dict(status="template; no results", note=REPEATED_MEASURES_NOTE, rows=replay_rows))


def markdown_table(rows, columns):
    lines = ["| " + " | ".join(columns) + " |", "|" + " --- |" * len(columns)]
    lines += ["| " + " | ".join(str(r[c]) for c in columns) + " |" for r in rows]
    return "\n".join(lines)


IMPLEMENTED_CHECKS = [
    ("paper2.method.evidence.check_integrity", "rejects schema errors, identity mismatches, patches cited by the wrong task, stale artifact and log hashes, unfrozen or missing definitions, empty policies"),
    ("paper2.method.evidence.evaluate_study_case", "rejects any case whose policy differs from the pinned study policy"),
    ("paper2.method.evidence.criterion_status", "admissible only with required rating, passed check, accepted and covering scope, required fields, and recorded roles; B05, B12, B14 cannot be not applicable; a defect with an unexecuted counterexample needs inquiry"),
    ("paper2.method.evidence.evidence_status", "defects take precedence; all blocking reasons returned; all not applicable never admissible"),
    ("paper2.method.evidence.evaluate", "M3 uses M2's observations less tasks with shown broken tests; input integrity, evidence status, and the decision kept apart; a decision (Accept, Reject, Inconclusive) only when the evidence is admissible, otherwise none with every reason; the minimum number of tasks; the score with and without the removed tasks"),
    ("paper2.method.evidence.migrate_v3_review", "reads C-numbered protocol 3 records without inventing check outcomes"),
    ("paper2.preparation.replay.make_variant", "three conditions per task (original, provenance removed, identity mismatch); parent digest and changes kept"),
    ("paper2.preparation.counterexamples.run", "B07 cheating attempt: the check must fail before the fix and pass with the real fix; each patch graded by the harness and checked; a defect only when the harness resolves a patch the check rejects; written once"),
    ("paper2.preparation.cases.analyse", "one case per agent from the sessions, signed rating forms, and signed requirement; reserve sessions replace failed ones; unreplaced failures count as not resolved; M1, M2, M3 under both policies and the target comparison"),
    ("paper2.preparation.replay.replay_rows", "verifies parent digests; reports level changes and added or removed reasons"),
    ("paper2.preparation.study_controls.SessionLedger", "atomic slot reservation and complete writes, phase limits, one session per task, configuration and phase, reserve only after a recorded infrastructure failure, no session after the 90th"),
    ("paper2.preparation.study_controls.launch", "refuses provider adapters during preparation; no automatic retry; failures stay open for a person to classify"),
    ("paper2.preparation.study_controls.select", "ordered, blind to model results, blocked by shortfalls, shared identities, or an undecided task before the selected ones"),
    ("paper2.preparation.study_controls.eligibility_state", "fixtures and unverified identities never count; no result stays pending"),
    ("paper2.preparation.study_controls.capability_report", "configuration checks never mark a runtime capability as verified; runtime results are enforced, held, violated, or not observable"),
    ("paper2.preparation.harness.eligibility_record", "eligible only when the unchanged source fails every FAIL_TO_PASS test and passes every PASS_TO_PASS test and the reference patch passes all; a missing report is a harness failure kept as an attempt"),
    ("paper2.preparation.targets.test_lists", "FAIL_TO_PASS and PASS_TO_PASS follow the grader's rule: PASSED or XFAIL has passed; a missing test has not"),
    ("paper2.preparation.targets.process", "candidates checked in order; stops only when the first eligible places the selection needs are decided"),
    ("paper2.preparation.sessions.check_authorization", "no session opens without the frozen manifest and the author's authorization naming its hash"),
    ("paper2.preparation.sessions.make_workspace", "workspace at the base commit with no later commits, tags, remote, or unreachable objects"),
    ("paper2.preparation.sessions.open_session", "refuses while the workspace folder holds anything, while launch settings or the frozen tool version are missing, or without a Codex sign-in; writes run.sh (clean environment, fixed flags, frozen tool version, no input after the prompt, watchdog at 900 seconds, a fresh Codex home or agy memory moved to the archive) and opened.json with its hashes"),
    ("paper2.preparation.sessions.close_session", "configuration, task, and workspace from the ledger and opened.json; refuses a changed run.sh or prompt and logs that start more than 1 second before the reservation; resolved only when all tests pass, the session stayed within its limits, its commands and paths touched no study material, its outputs show no oracle content, it ran no network command, it called only local tools, and it received no message after the prompt; the workspace is archived"),
    ("paper2.preparation.sessions.frozen_drift", "names any change since the freeze in the protocol, configurations, prompt, policy, code, signed forms, Codex configuration, agy settings, or tool versions"),
    ("paper2.preparation.replay.targeted_change", "judges each replay condition on the criterion or reason it targets, not on the aggregate status"),
]


def run_fixture_tests():
    suite = unittest.defaultTestLoader.discover(str(ROOT / "paper2/tests"), pattern="test_*.py")
    names = []

    def walk(s):
        for t in s:
            if isinstance(t, unittest.TestSuite):
                walk(t)
            else:
                names.append(t.id())
    walk(suite)
    result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    return dict(run_at=now(), total=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                names=sorted(n for n in names if n.split(".")[0] in ("test_evidence", "test_study_controls")))


def pending_lines(pools):
    """State of the pools, selection, forms, and freeze, read from the saved records."""
    from paper2.preparation import harness
    results = harness.load_results()
    def count(pool):
        states = [eligibility_state(t, results.get(t["task_id"])) for t in pool]
        return {k: states.count(k) for k in sorted(set(states))}
    chosen = select(pools, results)
    drafts = sorted(p.stem for p in (PROTOCOL / "audit_forms" / "drafts").glob("*.json"))
    signed = sorted(p.stem for p in (PROTOCOL / "audit_forms" / "completed").glob("*.json"))
    return [f"- Source pool: {len(pools['source'])} SymPy tasks of SWE-bench Verified; eligibility {count(pools['source'])}.",
            f"- Target pool: {len(pools['target'])} pull requests meeting the rule; checked in order: {count(pools['target'])}.",
            f"- Excluded: {len(pools['excluded_fixtures'])} synthetic fixtures and {len(pools['excluded_historical'])} "
            "protocol 3 target candidates.",
            f"- Selection: {chosen['status']}" + (f" ({'; '.join(chosen['blockers'])})" if chosen["blockers"] else
                                                  f": pilot {chosen['selected']['pilot']}, source {chosen['selected']['source']}, "
                                                  f"target {chosen['selected']['target']}."),
            f"- Audit forms: {len(drafts)} drafts awaiting the author's review; {len(signed)} signed.",
            f"- Freeze: {'written' if (PROTOCOL / 'frozen_manifest.json').exists() else 'not yet'}; pilot authorization: "
            f"{'written' if (PROTOCOL / 'authorizations' / 'pilot.json').exists() else 'not yet'}."]


def readiness(pools, tests=None):
    forms = audit_forms()
    sessions = SessionLedger(PROTOCOL / "ledger").summary()
    caps = capability_report({})
    lines = [f"# Protocol {PROTOCOL_NUMBER} readiness", "",
             "Generated by `python3 -m paper2.preparation.study_controls prepare`. This report names checks and their "
             "scope. It does not establish that the evaluation is ready, complete, or accepted.", "",
             "It summarizes saved records and runs nothing except, with `--run-tests`, the fixture tests. "
             f"Sessions under protocol {PROTOCOL_NUMBER}: {sessions['used']}; see `sessions/` and the ledger.", "",
             "## Implemented checks", ""]
    lines += [f"- `{name}`: {what}" for name, what in IMPLEMENTED_CHECKS]
    lines += ["", "## Tests on software fixtures", ""]
    if tests:
        lines += [f"Last run {tests['run_at']}: {tests['total']} tests in `paper2/tests`, "
                  f"{tests['failures']} failures, {tests['errors']} errors. These use constructed fixtures and stub "
                  "adapters; they check software behavior, not study outcomes.", "",
                  "Tests for this protocol:", ""]
        lines += [f"- `{n.split('.', 2)[-1]}`" for n in tests["names"]]
    else:
        lines += ["Not run by this command. Run `python3 -m paper2.preparation.study_controls prepare --run-tests`."]
    lines += ["", "## Awaiting experimental verification", "",
              "Configuration checks such as file locations, telemetry fields, or container flags do not establish "
              "these capabilities. Each needs an observation from a recorded session.", "",
              markdown_table([dict(capability=k, **v) for k, v in caps.items()],
                             ["capability", "configuration_check", "runtime"]), "",
              "## Pending work", "",
              *pending_lines(pools),
              f"- B07 cheating attempts: {len(list((PROTOCOL / 'audit_checks' / 'b07-counterexamples').glob('*/attempt.json')))} "
              f"of {SAMPLE['source']} source tasks recorded.",
              f"- Sessions: {sessions['used']} of {MAX_SESSIONS} used.",
              "",
              "## Session budget", "",
              markdown_table([dict(phase=p, slots=f"{r.start}-{r.stop - 1}", count=len(r)) for p, r in PHASES.items()],
                             ["phase", "slots", "count"])]
    return "\n".join(lines) + "\n"


def manifest(pools):
    overlaps = separation_problems(dict(source=pools["source"], target=pools["target"], fixture=pools["excluded_fixtures"],
                                        historical=pools["excluded_historical"]))
    return dict(
        protocol=f"{PROTOCOL_NUMBER} (draft, not frozen)", status="draft; the selection is recorded only in the frozen manifest (sessions.py freeze); eligibility results are in protocol-4/eligibility/, shared with protocol 5",
        repository=REPOSITORY, configurations=list(CONFIGURATIONS), threshold=0.70, confidence=0.95,
        selected_criteria=list(SELECTED_CRITERIA),
        session_budget={p: dict(slots=[r.start, r.stop - 1], count=len(r)) for p, r in PHASES.items()},
        maximum_sessions=MAX_SESSIONS,
        selection=dict(order=f"ascending sha256('{ORDER_SALT}|' + task_id)", sample=SAMPLE,
                       rule="pilot then source from the source pool, target from the target pool; first eligible "
                            "upstream tasks in order; model results are never consulted",
                       shortfall="blocks selection; no repository or task substitution",
                       eligibility="only upstream tasks with confirmed identity and a matching result count; "
                                   "no result is pending, not a pass or failure"),
        pools=pools, selected=dict(pilot=[], source=[], target=[]),
        historical_overlaps=dict(
            note="Shared identities among the source pool, target pool, excluded fixtures, and excluded protocol 3 "
                 "candidates. Fixtures and protocol 3 candidates never enter a study role.", found=overlaps),
    )


def prepare(run_tests=False):
    pools = build_pools()
    PROTOCOL.mkdir(parents=True, exist_ok=True)
    path = PROTOCOL / "study_manifest.json"
    if path.exists() and any(json.loads(path.read_text())["selected"].values()):
        raise RuntimeError("The manifest records a selection; it is not regenerated")
    path.write_text(json.dumps(manifest(pools), indent=2) + "\n")
    for name, form in audit_forms().items():
        with contextlib.suppress(FileExistsError):  # never overwrite a form that may hold findings
            save_new(PROTOCOL / "audit_forms" / f"{name}.json", form)
    templates = result_templates()
    for name, data in templates.items():
        with contextlib.suppress(FileExistsError):
            save_new(PROTOCOL / "templates" / f"{name}.json", data)
    md = ["# Result templates (no results)", "", "## Source and target decisions", "",
          *[f"- {n}" for n in templates["decisions"]["notes"]], "",
          markdown_table(templates["decisions"]["rows"], ["config_id", "source_n", "source_successes", "M2_decision",
                                                         "M3_strict_decision", "M3_lenient_decision", "ABC_decision",
                                                         "tests_only_decision", "target_successes", "target_decision",
                                                         "agreement_M2", "agreement_M3_strict", "agreement_M3_lenient",
                                                         "agreement_ABC"]),
          "", "## Controlled replay", "", templates["replay"]["note"], "",
          markdown_table(templates["replay"]["rows"], ["config_id", "task", "condition", "input_integrity",
                                                       "evidence_status", "score_decision", "changed", "reasons"])]
    tables = PROTOCOL / "templates" / "result_tables.md"
    if not tables.exists():
        tables.write_text("\n".join(md) + "\n")
    (PROTOCOL / "readiness.md").write_text(readiness(pools, run_fixture_tests() if run_tests else None))
    return PROTOCOL / "readiness.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["prepare", "launch"])
    parser.add_argument("--run-tests", action="store_true")
    args = parser.parse_args()
    if args.stage == "launch":
        parser.error("Provider execution is disabled during preparation")
    print(prepare(args.run_tests))


if __name__ == "__main__":
    main()

"""Controlled replay definitions for Paper 2. Nothing here runs a model or the study.

The replay is a test of the implementation on real records. The replay unit is one source case (one
configuration and its source tasks). Each source task is replayed under three conditions, each changing only
that task's evidence:
  original            the case record as collected;
  provenance_removed  that task's execution provenance removed;
  identity_mismatch   that task's identifier changed, or its observation cites another task's patch.

B07 cheating attempts enter the B07 rating form itself (protocol 5), so the replay has no oracle defect condition.
Variants keep the parent case digest and list every change. Rows are repeated observations on the same tasks.
"""
import copy
import json
from pathlib import Path

from paper2.method.evidence import case_digest, evaluate

CONDITIONS = ("original", "provenance_removed", "identity_mismatch")
REPEATED_MEASURES_NOTE = ("Rows are repeated observations on the same source tasks under three conditions; "
                          "they are not independent tasks.")


def make_variant(parent, condition, task_id=None, mismatch="patch"):
    if condition not in CONDITIONS:
        raise ValueError(f"Unknown replay condition {condition!r}")
    child = copy.deepcopy(parent)
    task_id = task_id or child["observations"][0]["task_id"]
    index = next((i for i, o in enumerate(child["observations"]) if o["task_id"] == task_id), None)
    if index is None:
        raise ValueError(f"Task {task_id!r} has no observation in the parent case")
    child.update(case_id=f"{parent['case_id']}--{task_id}--{condition}", kind="constructed_variant",
                 parent=dict(case_id=parent["case_id"], sha256=case_digest(parent), kind=parent["kind"]),
                 condition=condition, replay_task=task_id)
    obs = child["observations"][index]
    changes = []
    if condition == "provenance_removed":
        if obs.pop("provenance", None) is not None:
            changes.append(f"{task_id}: provenance removed")
    elif condition == "identity_mismatch":
        if mismatch == "task":
            obs["task_id"] = task_id + "-mismatch"
            changes.append(f"{task_id}: task identifier changed to {obs['task_id']}")
        elif mismatch == "patch":
            other = child["observations"][(index + 1) % len(child["observations"])]
            if other is obs:
                raise ValueError("A patch mismatch needs a second observation")
            obs["patch"] = copy.deepcopy(other["patch"])
            changes.append(f"{task_id}: cites the patch of {other['task_id']}")
        else:
            raise ValueError("mismatch must be 'task' or 'patch'")
    child["changes"] = changes
    return child


def verify_parent(child, parent):
    return child.get("parent", {}).get("sha256") == case_digest(parent)


def write_variant(child, directory):
    """Exclusive creation; an existing variant is never replaced."""
    path = Path(directory) / f"{child['case_id']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as f:
        json.dump(child, f, indent=2)
        f.write("\n")
    return path


def targeted_change(condition, task, res, base):
    """Whether the variant changed what its condition targets, judged per criterion and reason rather than on the
    aggregate status, which other criteria may already fix: provenance removed adds the provenance reason for the
    task; identity mismatch rejects the case. None for the original."""
    if condition == "original":
        return None
    if condition == "provenance_removed":
        return any("provenance missing" in r and task in r for r in res["reasons"] if r not in base["reasons"])
    if condition == "identity_mismatch":
        return res["input_integrity"] == "rejected"
    raise ValueError(f"Unknown condition {condition!r}")


def replay_rows(original, variants):
    """original: the parent case; variants: {task: {condition: variant}}. Returns rows with
    the changes in each level and in the reasons relative to the original evidence."""
    base = evaluate(original)
    rows = []
    for task, by_condition in variants.items():
        for condition in CONDITIONS:
            if condition == "original":
                res = base
            elif condition not in by_condition:
                rows.append(dict(task=task, condition=condition, status="pending"))
                continue
            else:
                if not verify_parent(by_condition[condition], original):
                    raise ValueError(f"{task}/{condition}: variant does not derive from this original")
                res = evaluate(by_condition[condition])
            criteria = {c: v["status"] for c, v in (res.get("criteria") or {}).items()}
            rows.append(dict(
                task=task, condition=condition, status="evaluated",
                input_integrity=res["input_integrity"], evidence_status=res["evidence_status"],
                score_decision=res["score_decision"], criteria=criteria,
                changed=[k for k in ("input_integrity", "evidence_status", "score_decision") if res[k] != base[k]],
                reasons_added=[r for r in res["reasons"] if r not in base["reasons"]],
                reasons_removed=[r for r in base["reasons"] if r not in res["reasons"]],
                targeted_change=targeted_change(condition, task, res, base)))
    return dict(note=REPEATED_MEASURES_NOTE, tasks=len(variants), rows=rows)

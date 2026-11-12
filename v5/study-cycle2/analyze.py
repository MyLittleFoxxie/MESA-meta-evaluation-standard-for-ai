"""Analyze Study Cycle 2 responses alongside Study 1 (v4) and Cycle 1 (v5 Claude) records. Never calls a model or repairs output.

Computes:
- C2-1 & C2-6: Full reliability with 10,000-resample bootstrap 95% CIs (seed 20261111) and per-field Part A agreement for Claude (v5/study/) and Gemini (v5/study-cycle2/), plus cross-family agreement.
- C2-6: Chance-corrected agreement (Krippendorff's alpha and pairwise kappa) for the 302 Study 1 framework pairs with a cluster bootstrap over (benchmark, concern) cells.
- C2-6: Same-measure Tier 2 comparison (Satisfied/favorable, Unsatisfied/unfavorable, Open/unresolved) on HumanEval only (concern by concern against BetterBench and Scorecard repeats) and across all 4 benchmarks.
- C2-2: Detection rate (sensitivity) and false-alarm rate per criterion and model family on the 6 seeded AddTwo fixtures.
- C2-3: Recall of pre-registered known defects from the literature across the four benchmarks.

Run from the repository root: python v5/study-cycle2/analyze.py
"""
import argparse
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
V4 = ROOT / "v4/study"
V5_C1 = ROOT / "v5/study"
sys.path.insert(0, str(HERE))
from reliability import (
    BOOTSTRAP_RESAMPLES,
    BOOTSTRAP_SEED,
    alpha_with_ci,
    cohen_kappa,
    cohen_kappa_with_ci,
    nominal_distance,
    part_a_category,
    part_b_ordinal_distance,
    summarize_reliability,
)
from validate import rule_findings, validate

BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]
FRAMEWORKS = ["BB", "ECBD", "SC", "H2B", "ABC", "CAL", "OECD"]


def norm(s):
    return " ".join(s.split())


def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def parse_claude_events(path):
    tools = other = 0
    in_tok = out_tok = 0
    cost = 0.0
    model = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "assistant":
            msg = e.get("message", {})
            model = msg.get("model") or model
            for c in msg.get("content", []) or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") != "StructuredOutput":
                    if c.get("name", "").startswith("mcp__benchmark__"):
                        tools += 1
                    else:
                        other += 1
        if e.get("type") == "result":
            u = e.get("usage", {})
            in_tok = u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
            out_tok = u.get("output_tokens", 0)
            cost = e.get("total_cost_usd", 0.0)
    return tools, other, in_tok, out_tok, round(cost, 4), model


def parse_agy_events(path):
    tools = other = 0
    in_tok = out_tok = 0
    model = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("event") == "init":
            model = e.get("init", {}).get("model") or model
        elif e.get("event") == "step_update":
            su = e.get("step_update", {})
            if su.get("step_type") == "tool" and su.get("state") == "DONE":
                tname = su.get("tool_name", "")
                tinfo = su.get("tool_info", {})
                params = tinfo.get("parameters", {}) if isinstance(tinfo, dict) else {}
                if tname == "call_mcp_tool" and params.get("ServerName") == "benchmark":
                    tools += 1
                elif tname in ("read_file", "view_file") and "antigravity-cli/mcp/benchmark" in str(params.get("Path", "")).replace("\\", "/"):
                    pass
                else:
                    other += 1
        elif e.get("event") == "result":
            u = e.get("result", {}).get("usage", {})
            in_tok = u.get("input_tokens", 0) + u.get("cache_read_tokens", 0)
            out_tok = u.get("output_tokens", 0)
    return tools, other, in_tok, out_tok, 0.0, model


def check_evidence(entries, src_dir):
    rows = []
    for e in entries:
        source, quote, locator = e["source"].replace("\\", "/"), e["quote"], e["locator"]
        p = (
            src_dir / "paper.txt"
            if source in ("paper.txt", "paper")
            else (src_dir / source if source == "dataset-card.md" or source.startswith("repository/") else None)
        )
        exists = bool(p and p.is_file() and p.resolve().is_relative_to(src_dir.resolve()))
        text = p.read_text(encoding="utf-8", errors="replace") if exists and b"\0" not in p.read_bytes() else ""
        found = bool(quote.strip()) and (quote in text or norm(quote) in norm(text))
        rows.append(
            {
                "source": source,
                "exists": exists,
                "quote_found": found,
                "has_locator": bool(locator.strip()),
            }
        )
    return rows


def recode_rubric_level(level):
    """Recode a v5 rubric level to the three Study 1 outcomes and marker per v4/mapping/recoding-rules.md."""
    if level == "verified":
        return "favorable", ""
    if level in ("documented", "claimed"):
        return "favorable", "partial"
    if level == "contradicted":
        return "unfavorable", ""
    if level == "not_applicable":
        return "unresolved", "not_applicable"
    return "unresolved", ""


def concern_outcome(items):
    """Aggregate item outcomes for one framework/rubric on one benchmark and concern."""
    outs = [o for o, _ in items if o != "not_recoded"]
    if not outs:
        return "not_recoded", ""
    if "unfavorable" in outs:
        marked = all(m == "unresolved_by_rule" for o, m in items if o == "unfavorable")
        return "unfavorable", "unresolved_by_rule" if marked else ""
    if all(o == "favorable" for o in outs) and not any(m == "partial" for o, m in items):
        return "favorable", ""
    if any(o == "favorable" for o in outs):
        return "favorable", "partial"
    return "unresolved", ""


def item_to_concern(item_id):
    m = re.match(r"B(\d+)", item_id)
    return f"C{m.group(1)}" if m else item_id


def analyze_rubric_set(responses, citations, findings, runs):
    rel = summarize_reliability(responses, BENCHMARKS)
    levels = Counter()
    outcomes = Counter()
    kinds = Counter()
    scopes = Counter()
    absence_levels = Counter()
    contra_total = contra_located = na_total = defect_total = 0

    for (b, rep), data in sorted(responses.items()):
        if b not in BENCHMARKS:
            continue
        for j in data["judgments"]:
            levels[j["level"]] += 1
            outcomes[j["outcome"]] += 1
            kinds[j["check_kind"]] += 1
            scopes[j["scope"]["level"]] += 1
            if j["basis"] == "absence_of_information":
                absence_levels[j["level"]] += 1
            if j["level"] == "contradicted":
                contra_total += 1
                contra_located += bool(j["evidence"]) and all(e["locator"].strip() for e in j["evidence"])
            if j["level"] == "not_applicable":
                na_total += 1
            defect_total += len(j["task_defects"])

    same_outcome = same_kind = same_scope = same_level_and_outcome = 0
    n_pairs = 0
    for b in BENCHMARKS:
        if (b, 1) not in responses or (b, 2) not in responses:
            continue
        j1 = {j["item_id"]: j for j in responses[(b, 1)]["judgments"]}
        j2 = {j["item_id"]: j for j in responses[(b, 2)]["judgments"]}
        for i in j1:
            n_pairs += 1
            same_outcome += j1[i]["outcome"] == j2[i]["outcome"]
            same_kind += j1[i]["check_kind"] == j2[i]["check_kind"]
            same_scope += j1[i]["scope"]["level"] == j2[i]["scope"]["level"]
            same_level_and_outcome += (j1[i]["level"], j1[i]["outcome"]) == (j2[i]["level"], j2[i]["outcome"])

    return {
        "sessions": len([r for r in runs if r["phase"] == "main"]),
        "valid": sum(int(r["valid"]) for r in runs if r["phase"] == "main"),
        "cost_usd": round(sum(r["cost_usd"] for r in runs if r["phase"] == "main"), 2),
        "returned_models": sorted({r["model"] for r in runs if r["phase"] == "main" and r["model"]}),
        "other_tools_used": sum(r["other_tools"] for r in runs if r["phase"] == "main"),
        "reliability": rel,
        "field_agreement": {
            "pairs": n_pairs,
            "same_outcome": same_outcome,
            "same_check_kind": same_kind,
            "same_scope": same_scope,
            "same_level_and_outcome": same_level_and_outcome,
        },
        "levels": dict(levels),
        "outcomes": dict(outcomes),
        "check_kinds": dict(kinds),
        "scopes": dict(scopes),
        "absence": dict(absence_levels),
        "contradicted": {"ratings": contra_total, "with_location": contra_located},
        "not_applicable": na_total,
        "task_defects": defect_total,
        "rule_findings": dict(Counter(f["rule"] for f in findings)),
        "citations": {
            "evidence": len(citations),
            "source_exists": sum(int(c["exists"]) for c in citations),
            "quote_found": sum(int(c["quote_found"]) for c in citations),
        },
    }


def load_claude_cycle1():
    jobs = {j["id"]: j for j in json.loads((V5_C1 / "jobs.json").read_text(encoding="utf-8"))["jobs"] if j["phase"] == "main"}
    responses, citations, findings, runs = {}, [], [], []
    for jid, job in jobs.items():
        for att in sorted((V5_C1 / "outputs" / jid).glob("attempt-*")):
            meta = json.loads((att / "metadata.json").read_text(encoding="utf-8"))
            tools, other, in_tok, out_tok, cost, model = parse_claude_events(att / "events.jsonl")
            data = json.loads((att / "response.txt").read_text(encoding="utf-8"))
            errors = validate(data)
            runs.append(
                {
                    "job": jid,
                    "benchmark": job["benchmark"],
                    "repeat": job["repeat"],
                    "phase": "main",
                    "attempt": att.name,
                    "status": meta["status"],
                    "valid": not errors,
                    "tool_calls": tools,
                    "other_tools": other,
                    "input_tokens": in_tok,
                    "output_tokens": out_tok,
                    "cost_usd": cost,
                    "model": model,
                    "elapsed_seconds": meta["elapsed_seconds"],
                }
            )
            if not errors:
                responses[(job["benchmark"], job["repeat"])] = data
                src = V4 / "sources" / job["benchmark"]
                for rf_item, rf_rule in rule_findings(data):
                    findings.append({"benchmark": job["benchmark"], "repeat": job["repeat"], "item_id": rf_item, "rule": rf_rule})
                for d in data["description"]:
                    citations.extend(check_evidence(d["evidence"], src))
                for j in data["judgments"]:
                    citations.extend(check_evidence(j["evidence"], src))
    return responses, citations, findings, runs


def compute_study1_chance_corrected():
    """C2-6: Chance-corrected agreement for the 302 Study 1 framework pairs with a cluster bootstrap over (benchmark, concern) cells."""
    rows = list(csv.DictReader((V4 / "analysis/concern-outcomes.csv").open(encoding="utf-8")))
    cells_3 = defaultdict(dict)
    cells_strict = defaultdict(dict)
    for r in rows:
        if r["repeat"] != "1" or r["framework"] == "RUBRIC" or r["outcome"] == "not_recoded":
            continue
        key = (r["benchmark"], r["concern"])
        cells_3[key][r["framework"]] = r["outcome"]
        cells_strict[key][r["framework"]] = f"{r['outcome']}|{'partial' if r['marker'] == 'partial' else 'full'}"

    multi_keys = sorted(k for k, v in cells_3.items() if len(v) >= 2)
    units_3 = [list(cells_3[k].values()) for k in multi_keys]
    units_strict = [list(cells_strict[k].values()) for k in multi_keys]

    alpha_3 = alpha_with_ci(units_3, nominal_distance, seed=BOOTSTRAP_SEED + 10, n_boot=BOOTSTRAP_RESAMPLES)
    alpha_strict = alpha_with_ci(units_strict, nominal_distance, seed=BOOTSTRAP_SEED + 11, n_boot=BOOTSTRAP_RESAMPLES)

    def pairs_from_keys(key_list, cell_map):
        out = []
        for k in key_list:
            fws = sorted(cell_map[k])
            for f1, f2 in combinations(fws, 2):
                out.append((cell_map[k][f1], cell_map[k][f2]))
        return out

    all_pairs_3 = pairs_from_keys(multi_keys, cells_3)
    all_pairs_strict = pairs_from_keys(multi_keys, cells_strict)
    kappa_3_point = cohen_kappa(all_pairs_3)
    kappa_strict_point = cohen_kappa(all_pairs_strict)

    rng = random.Random(BOOTSTRAP_SEED + 12)
    n_cells = len(multi_keys)
    boot_k3, boot_ks, boot_raw3, boot_raws = [], [], [], []
    for _ in range(BOOTSTRAP_RESAMPLES):
        draw_keys = [multi_keys[rng.randrange(n_cells)] for _ in range(n_cells)]
        p3 = pairs_from_keys(draw_keys, cells_3)
        ps = pairs_from_keys(draw_keys, cells_strict)
        if p3:
            boot_k3.append(cohen_kappa(p3))
            boot_raw3.append(sum(1 for a, b in p3 if a == b) / len(p3))
        if ps:
            boot_ks.append(cohen_kappa(ps))
            boot_raws.append(sum(1 for a, b in ps if a == b) / len(ps))
    boot_k3.sort()
    boot_ks.sort()
    boot_raw3.sort()
    boot_raws.sort()
    lo_idx = int(0.025 * BOOTSTRAP_RESAMPLES)
    hi_idx = int(0.975 * BOOTSTRAP_RESAMPLES)

    return {
        "n_cells": n_cells,
        "n_pairs": len(all_pairs_3),
        "same_3_verdict": sum(1 for a, b in all_pairs_3 if a == b),
        "raw_3_verdict": round(sum(1 for a, b in all_pairs_3 if a == b) / len(all_pairs_3), 3),
        "raw_3_verdict_ci95": [round(boot_raw3[lo_idx], 3), round(boot_raw3[hi_idx], 3)],
        "alpha_3_verdict": alpha_3["alpha"],
        "alpha_3_verdict_ci95": alpha_3["ci95"],
        "pairwise_kappa_3_verdict": kappa_3_point,
        "pairwise_kappa_3_verdict_ci95": [round(boot_k3[lo_idx], 3), round(boot_k3[hi_idx], 3)],
        "same_strict_partial": sum(1 for a, b in all_pairs_strict if a == b),
        "raw_strict_partial": round(sum(1 for a, b in all_pairs_strict if a == b) / len(all_pairs_strict), 3),
        "raw_strict_partial_ci95": [round(boot_raws[lo_idx], 3), round(boot_raws[hi_idx], 3)],
        "alpha_strict_partial": alpha_strict["alpha"],
        "alpha_strict_partial_ci95": alpha_strict["ci95"],
        "pairwise_kappa_strict_partial": kappa_strict_point,
        "pairwise_kappa_strict_partial_ci95": [round(boot_ks[lo_idx], 3), round(boot_ks[hi_idx], 3)],
    }


def compute_same_measure_comparison(claude_resp, gemini_resp):
    """C2-6: Compare rubric repeats recoded to the three framework verdicts against BB and SC repeats on HumanEval only (concern by concern) and across all 4 benchmarks."""
    add_rep = json.loads((V4 / "analysis/addition-repeat.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((V4 / "analysis/concern-outcomes.csv").open(encoding="utf-8")))
    bb_he_concerns = sorted(
        r["concern"]
        for r in rows
        if r["benchmark"] == "humaneval" and r["framework"] == "BB" and r["repeat"] == "1" and r["outcome"] != "not_recoded"
    )
    sc_he_concerns = sorted(
        r["concern"]
        for r in rows
        if r["benchmark"] == "humaneval" and r["framework"] == "SC" and r["repeat"] == "1" and r["outcome"] != "not_recoded"
    )

    def summarize_rubric_recoded(resp_map):
        if not resp_map:
            return None
        item_pairs_3, item_pairs_strict = [], []
        concern_grid = defaultdict(lambda: defaultdict(list))
        for b in BENCHMARKS:
            if (b, 1) not in resp_map or (b, 2) not in resp_map:
                continue
            j1 = {j["item_id"]: j["level"] for j in resp_map[(b, 1)]["judgments"]}
            j2 = {j["item_id"]: j["level"] for j in resp_map[(b, 2)]["judgments"]}
            for iid in sorted(j1):
                o1, m1 = recode_rubric_level(j1[iid])
                o2, m2 = recode_rubric_level(j2[iid])
                item_pairs_3.append((o1, o2))
                item_pairs_strict.append(((o1, m1 == "partial"), (o2, m2 == "partial")))
                c = item_to_concern(iid)
                concern_grid[(b, 1)][c].append((o1, m1))
                concern_grid[(b, 2)][c].append((o2, m2))

        concern_outcomes = {
            k: {c: concern_outcome(items) for c, items in cs.items()} for k, cs in concern_grid.items()
        }

        def compare_subset(benchmarks_sub, concerns_filter=None):
            p3, ps, diff = [], [], {}
            for b in benchmarks_sub:
                if (b, 1) not in concern_outcomes or (b, 2) not in concern_outcomes:
                    continue
                c1, c2 = concern_outcomes[(b, 1)], concern_outcomes[(b, 2)]
                shared = sorted(set(c1) & set(c2))
                if concerns_filter is not None:
                    shared = [c for c in shared if c in concerns_filter]
                for c in shared:
                    o1, m1 = c1[c]
                    o2, m2 = c2[c]
                    p3.append((o1, o2))
                    ps.append(((o1, m1 == "partial"), (o2, m2 == "partial")))
                    if o1 != o2 or (m1 == "partial") != (m2 == "partial"):
                        diff[f"{b}:{c}"] = [[o1, m1], [o2, m2]]
            return {
                "concerns": len(p3),
                "same_3_verdict": sum(1 for a, b in p3 if a == b),
                "same_3_verdict_and_partial": sum(1 for a, b in ps if a == b),
                "kappa_3_verdict": cohen_kappa(p3),
                "differing": diff,
            }

        return {
            "humaneval_all_29_concerns": compare_subset(["humaneval"]),
            "humaneval_on_BB_21_concerns": compare_subset(["humaneval"], set(bb_he_concerns)),
            "humaneval_on_SC_22_concerns": compare_subset(["humaneval"], set(sc_he_concerns)),
            "four_benchmarks_concern_level_116": compare_subset(BENCHMARKS),
            "four_benchmarks_item_level_124": {
                "items": len(item_pairs_3),
                "same_3_verdict": sum(1 for a, b in item_pairs_3 if a == b),
                "same_3_verdict_and_partial": sum(1 for a, b in item_pairs_strict if a == b),
                "kappa_3_verdict": cohen_kappa(item_pairs_3),
            },
        }

    return {
        "analysis_provenance": (
            "Recoding rubric ratings to the three Study 1 verdicts (favorable, unfavorable, unresolved) and comparing "
            "concern-by-concern on HumanEval against the BetterBench and Scorecard repeats was designed after the Claude "
            "Cycle 1 results were known (post-hoc for Claude) and frozen before the Gemini Cycle 2 sessions ran (prospective for Gemini)."
        ),
        "humaneval_framework_repeats": {
            "BB": {
                "concerns": add_rep["BB"]["concerns"],
                "same_3_verdict": add_rep["BB"]["same_concern_outcome"],
                "same_3_verdict_and_partial": add_rep["BB"]["same_concern_outcome_and_partial"],
                "items": add_rep["BB"]["items"],
                "same_item_3_verdict": add_rep["BB"]["same_item_outcome"],
            },
            "SC": {
                "concerns": add_rep["SC"]["concerns"],
                "same_3_verdict": add_rep["SC"]["same_concern_outcome"],
                "same_3_verdict_and_partial": add_rep["SC"]["same_concern_outcome_and_partial"],
                "items": add_rep["SC"]["items"],
                "same_item_3_verdict": add_rep["SC"]["same_item_outcome"],
            },
        },
        "claude_cycle1": summarize_rubric_recoded(claude_resp),
        "gemini_cycle2": summarize_rubric_recoded(gemini_resp),
    }


def compute_cross_family(claude_resp, gemini_resp):
    """C2-1 & C2-6: Cross-family agreement between Claude Sonnet 5.5 and Gemini 3.8 Flash (Medium)."""
    if not claude_resp or not gemini_resp:
        return None
    pa_units_4, pa_pairs_cross = [], []
    pa_per_facet = {}
    pb_units_4_all, pb_units_4_app = [], []
    pb_pairs_cross_6, pb_pairs_cross_3, pb_pairs_cross_strict = [], [], []
    pb_units_4_3 = []

    for b in BENCHMARKS:
        if not all((b, r) in claude_resp and (b, r) in gemini_resp for r in (1, 2)):
            continue
        c1, c2 = claude_resp[(b, 1)], claude_resp[(b, 2)]
        g1, g2 = gemini_resp[(b, 1)], gemini_resp[(b, 2)]

        dc1 = {d["facet"]: part_a_category(d["value"]) for d in c1["description"]}
        dc2 = {d["facet"]: part_a_category(d["value"]) for d in c2["description"]}
        dg1 = {d["facet"]: part_a_category(d["value"]) for d in g1["description"]}
        dg2 = {d["facet"]: part_a_category(d["value"]) for d in g2["description"]}
        for f in dc1:
            u = [dc1[f], dc2[f], dg1[f], dg2[f]]
            pa_units_4.append(u)
            cross = [(dc1[f], dg1[f]), (dc1[f], dg2[f]), (dc2[f], dg1[f]), (dc2[f], dg2[f])]
            pa_pairs_cross.extend(cross)
            slot = pa_per_facet.setdefault(f, {"cross_pairs": 0, "same_category": 0, "r1_vs_r1_same": 0})
            slot["cross_pairs"] += 4
            slot["same_category"] += sum(int(x == y) for x, y in cross)
            slot["r1_vs_r1_same"] += int(dc1[f] == dg1[f])

        jc1 = {j["item_id"]: j["level"] for j in c1["judgments"]}
        jc2 = {j["item_id"]: j["level"] for j in c2["judgments"]}
        jg1 = {j["item_id"]: j["level"] for j in g1["judgments"]}
        jg2 = {j["item_id"]: j["level"] for j in g2["judgments"]}
        for iid in sorted(jc1):
            u = [jc1[iid], jc2[iid], jg1[iid], jg2[iid]]
            pb_units_4_all.append(u)
            app_u = [x for x in u if x != "not_applicable"]
            if len(app_u) >= 2:
                pb_units_4_app.append(app_u)
            for cl_lv in (jc1[iid], jc2[iid]):
                for gm_lv in (jg1[iid], jg2[iid]):
                    pb_pairs_cross_6.append((cl_lv, gm_lv))
                    o_c, m_c = recode_rubric_level(cl_lv)
                    o_g, m_g = recode_rubric_level(gm_lv)
                    pb_pairs_cross_3.append((o_c, o_g))
                    pb_pairs_cross_strict.append(((o_c, m_c == "partial"), (o_g, m_g == "partial")))
            pb_units_4_3.append([recode_rubric_level(x)[0] for x in u])

    if not pb_units_4_all:
        return None

    return {
        "part_a": {
            "units_4_raters": len(pa_units_4),
            "cross_pairs": len(pa_pairs_cross),
            "cross_same_category": sum(1 for a, b in pa_pairs_cross if a == b),
            "cross_raw_agreement": round(sum(1 for a, b in pa_pairs_cross if a == b) / len(pa_pairs_cross), 3),
            "alpha_4_raters": alpha_with_ci(pa_units_4, nominal_distance, seed=BOOTSTRAP_SEED + 20),
            "per_facet": pa_per_facet,
        },
        "part_b_6_level": {
            "units_4_raters": len(pb_units_4_all),
            "cross_pairs": len(pb_pairs_cross_6),
            "cross_same_level": sum(1 for a, b in pb_pairs_cross_6 if a == b),
            "cross_raw_agreement": round(sum(1 for a, b in pb_pairs_cross_6 if a == b) / len(pb_pairs_cross_6), 3),
            "alpha_ordinal_4_raters": alpha_with_ci(pb_units_4_app, part_b_ordinal_distance, seed=BOOTSTRAP_SEED + 21),
            "alpha_nominal_4_raters": alpha_with_ci(pb_units_4_all, nominal_distance, seed=BOOTSTRAP_SEED + 22),
        },
        "part_b_3_verdict": {
            "cross_pairs": len(pb_pairs_cross_3),
            "cross_same_3_verdict": sum(1 for a, b in pb_pairs_cross_3 if a == b),
            "cross_raw_3_verdict": round(sum(1 for a, b in pb_pairs_cross_3 if a == b) / len(pb_pairs_cross_3), 3),
            "cross_same_3_verdict_and_partial": sum(1 for a, b in pb_pairs_cross_strict if a == b),
            "cross_raw_3_verdict_and_partial": round(
                sum(1 for a, b in pb_pairs_cross_strict if a == b) / len(pb_pairs_cross_strict), 3
            ),
            "alpha_3_verdict_4_raters": alpha_with_ci(pb_units_4_3, nominal_distance, seed=BOOTSTRAP_SEED + 23),
        },
    }


def evaluate_seeded_fixtures(seeded_resp):
    """C2-2: Evaluate sensitivity and false-alarm rate per planted criterion and model family on the 6 AddTwo copies."""
    truth = json.loads((HERE / "seeded_truth.json").read_text(encoding="utf-8"))
    criteria = truth["criteria_evaluated"]
    fixtures = list(truth["fixtures"].keys())
    rows = []
    by_family = {}

    def is_flagged(j, crit_id):
        if crit_id == "B04":
            return j["level"] == "undocumented" and j["basis"] == "absence_of_information"
        return j["level"] == "contradicted" or j["outcome"] == "failed"

    for family in ("claude", "gemini"):
        per_crit = {}
        tp_total = fn_total = fp_total = tn_total = 0
        for cspec in criteria:
            cid = cspec["criterion"]
            pos_fix = cspec["positive_fixture"]
            tp = fn = fp = tn = 0
            for fix in fixtures:
                for rep in (1, 2):
                    key = (fix, family, rep)
                    if key not in seeded_resp:
                        continue
                    data = seeded_resp[key]
                    jmap = {j["item_id"]: j for j in data["judgments"]}
                    j = jmap[cid]
                    flagged = is_flagged(j, cid)
                    has_loc = bool(j["evidence"]) and all(e["locator"].strip() for e in j["evidence"])
                    is_pos = fix == pos_fix
                    if is_pos:
                        if flagged:
                            tp += 1
                        else:
                            fn += 1
                    else:
                        if flagged:
                            fp += 1
                        else:
                            tn += 1
                    rows.append(
                        {
                            "family": family,
                            "fixture": fix,
                            "repeat": rep,
                            "criterion": cid,
                            "planted": is_pos,
                            "level": j["level"],
                            "outcome": j["outcome"],
                            "basis": j["basis"],
                            "flagged": flagged,
                            "has_location": has_loc,
                        }
                    )
            tp_total += tp
            fn_total += fn
            fp_total += fp
            tn_total += tn
            per_crit[cid] = {
                "positive_runs": tp + fn,
                "true_positives": tp,
                "sensitivity": round(tp / (tp + fn), 3) if (tp + fn) else None,
                "negative_runs": fp + tn,
                "false_positives": fp,
                "false_alarm_rate": round(fp / (fp + tn), 3) if (fp + tn) else None,
            }
        by_family[family] = {
            "per_criterion": per_crit,
            "pooled_positive_runs": tp_total + fn_total,
            "pooled_true_positives": tp_total,
            "pooled_sensitivity": round(tp_total / (tp_total + fn_total), 3) if (tp_total + fn_total) else None,
            "pooled_negative_runs": fp_total + tn_total,
            "pooled_false_positives": fp_total,
            "pooled_false_alarm_rate": round(fp_total / (fp_total + tn_total), 3) if (fp_total + tn_total) else None,
        }
    return by_family, rows


def evaluate_known_defects(claude_resp, gemini_resp):
    """C2-3: Evaluate detection of pre-registered known defects from the literature."""
    known = json.loads((HERE / "known_defects.json").read_text(encoding="utf-8"))["defects"]
    rows = []
    summary = {}
    for family, rmap in (("claude", claude_resp), ("gemini", gemini_resp)):
        found_r1 = found_r2 = found_either = 0
        total_eval = 0
        for d in known:
            b = d["benchmark"]
            if (b, 1) not in rmap and (b, 2) not in rmap:
                continue
            total_eval += 1
            hits = {}
            for rep in (1, 2):
                if (b, rep) not in rmap:
                    hits[rep] = False
                    continue
                jmap = {j["item_id"]: j for j in rmap[(b, rep)]["judgments"]}
                hit = False
                matched_items = []
                for iid in d["item_ids"]:
                    j = jmap.get(iid)
                    if not j:
                        continue
                    ev_text = " ".join(f"{e['source']} {e['locator']} {e['quote']}" for e in j["evidence"])
                    combined = f"{j['reason']} {j['checks']} {ev_text}".lower()
                    loc_match = any(sub.lower() in combined for sub in d["locator_substrings"])
                    if j["level"] == "contradicted" or j["outcome"] == "failed":
                        if loc_match:
                            hit = True
                            matched_items.append(f"{iid}:{j['level']}/{j['outcome']}")
                    elif d["id"] in ("TB-2", "TB-3", "TQA-2") and loc_match and (
                        j["level"] == "undocumented" or "outdated" in combined or "error" in combined or "89.5" in combined
                    ):
                        hit = True
                        matched_items.append(f"{iid}:{j['level']}/{j['outcome']}")
                hits[rep] = hit
                rows.append(
                    {
                        "family": family,
                        "defect_id": d["id"],
                        "benchmark": b,
                        "repeat": rep,
                        "detected": hit,
                        "matched": ";".join(matched_items),
                    }
                )
            found_r1 += int(hits.get(1, False))
            found_r2 += int(hits.get(2, False))
            found_either += int(hits.get(1, False) or hits.get(2, False))
        summary[family] = {
            "known_defects_total": total_eval,
            "detected_repeat_1": found_r1,
            "detected_repeat_2": found_r2,
            "detected_either_repeat": found_either,
        }
    return summary, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs", default=str(HERE / "outputs"))
    ap.add_argument("--analysis", default=str(HERE / "analysis"))
    a = ap.parse_args()
    out_dir, analysis_dir = Path(a.outputs), Path(a.analysis)
    analysis_dir.mkdir(exist_ok=True)

    claude_resp, claude_cit, claude_find, claude_runs = load_claude_cycle1()
    claude_summary = analyze_rubric_set(claude_resp, claude_cit, claude_find, claude_runs)

    jobs = {j["id"]: j for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))["jobs"]}
    gemini_resp, gemini_cit, gemini_find, c2_runs = {}, [], [], []
    seeded_resp = {}
    judgment_rows = []

    for jid, job in jobs.items():
        jdir = out_dir / jid
        if not jdir.exists():
            continue
        for att in sorted(jdir.glob("attempt-*")):
            meta = json.loads((att / "metadata.json").read_text(encoding="utf-8"))
            if job["family"] == "gemini":
                tools, other, in_tok, out_tok, cost, model = parse_agy_events(att / "events.jsonl")
            else:
                tools, other, in_tok, out_tok, cost, model = parse_claude_events(att / "events.jsonl")
            rp = att / "response.txt"
            try:
                data = json.loads(rp.read_text(encoding="utf-8"))
                errors = validate(data)
            except Exception as e:
                data, errors = None, [str(e)]
            c2_runs.append(
                {
                    "job": jid,
                    "benchmark": job["benchmark"],
                    "family": job["family"],
                    "repeat": job["repeat"],
                    "phase": job["phase"],
                    "attempt": att.name,
                    "status": meta["status"],
                    "valid": not errors,
                    "errors": "; ".join(errors),
                    "tool_calls": tools,
                    "other_tools": other,
                    "input_tokens": in_tok,
                    "output_tokens": out_tok,
                    "cost_usd": cost,
                    "model": model,
                    "elapsed_seconds": meta["elapsed_seconds"],
                }
            )
            if data and not errors:
                src = ROOT / job["source_root"]
                if job["phase"] == "main" and job["family"] == "gemini":
                    gemini_resp[(job["benchmark"], job["repeat"])] = data
                    for rf_item, rf_rule in rule_findings(data):
                        gemini_find.append(
                            {"benchmark": job["benchmark"], "repeat": job["repeat"], "item_id": rf_item, "rule": rf_rule}
                        )
                    for d in data["description"]:
                        gemini_cit.extend(check_evidence(d["evidence"], src))
                    for j in data["judgments"]:
                        gemini_cit.extend(check_evidence(j["evidence"], src))
                        judgment_rows.append(
                            {
                                "benchmark": job["benchmark"],
                                "family": job["family"],
                                "repeat": job["repeat"],
                                "item_id": j["item_id"],
                                "level": j["level"],
                                "basis": j["basis"],
                                "outcome": j["outcome"],
                                "check_kind": j["check_kind"],
                                "scope": j["scope"]["level"],
                                "evidence": len(j["evidence"]),
                                "task_defects": len(j["task_defects"]),
                            }
                        )
                elif job["phase"] == "seeded":
                    seeded_resp[(job["benchmark"], job["family"], job["repeat"])] = data

    if c2_runs:
        write_csv(
            analysis_dir / "runs.csv",
            c2_runs,
            [
                "job",
                "benchmark",
                "family",
                "repeat",
                "phase",
                "attempt",
                "status",
                "valid",
                "errors",
                "tool_calls",
                "other_tools",
                "input_tokens",
                "output_tokens",
                "cost_usd",
                "model",
                "elapsed_seconds",
            ],
        )
    if judgment_rows:
        write_csv(
            analysis_dir / "judgments.csv",
            judgment_rows,
            ["benchmark", "family", "repeat", "item_id", "level", "basis", "outcome", "check_kind", "scope", "evidence", "task_defects"],
        )

    gemini_summary = analyze_rubric_set(
        gemini_resp, gemini_cit, gemini_find, [r for r in c2_runs if r["family"] == "gemini" and r["phase"] == "main"]
    )
    study1_cc = compute_study1_chance_corrected()
    same_measure = compute_same_measure_comparison(claude_resp, gemini_resp)
    cross_family = compute_cross_family(claude_resp, gemini_resp)
    seeded_summary, seeded_rows = evaluate_seeded_fixtures(seeded_resp)
    if seeded_rows:
        write_csv(
            analysis_dir / "seeded-results.csv",
            seeded_rows,
            ["family", "fixture", "repeat", "criterion", "planted", "level", "outcome", "basis", "flagged", "has_location"],
        )
    known_summary, known_rows = evaluate_known_defects(claude_resp, gemini_resp)
    if known_rows:
        write_csv(
            analysis_dir / "known-defects-results.csv",
            known_rows,
            ["family", "defect_id", "benchmark", "repeat", "detected", "matched"],
        )

    full_summary = {
        "study1_chance_corrected_302_pairs": study1_cc,
        "claude_cycle1": claude_summary,
        "gemini_cycle2": gemini_summary,
        "cross_family": cross_family,
        "same_measure_comparison": same_measure,
        "seeded_fixtures": seeded_summary,
        "known_defects": known_summary,
    }
    (analysis_dir / "summary.json").write_text(json.dumps(full_summary, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(full_summary, indent=2))


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Decision-Power & Coverage Simulation for Paper 2.

Simulates requirements decision mechanics, statistical power, error rates,
and decision coverage across methods using pure Python standard library:
- Method 1: Scores Alone (Aggregate Source Wilson Bounds)
- Method 2: Task Matching Alone (Matched Source Wilson Bounds)
- Control 1: Random Abstention Baseline (Matching M3 coverage exactly)
- Control 2: Threshold-Proximity Abstention Baseline (Matching M3 coverage exactly)
- Method 3: Task Matching + MESA Admissibility Gate (Review-based abstention)

Outputs serialized to paper2/protocol/decision_power_simulation.json.
"""

import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.abspath("."))
from paper2.method.decision_engine import compute_wilson_score_interval as wilson_score_interval


def simulate_binomial_decisions(n, p, theta=0.70):
    """Computes exact binomial distribution of decisions under Wilson bounds."""
    p_supported = 0.0
    p_contradicted = 0.0
    p_unresolved = 0.0

    for k in range(n + 1):
        prob_k = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        lb, ub = wilson_score_interval(k, n, confidence=0.95)
        if lb >= theta:
            p_supported += prob_k
        elif ub < theta:
            p_contradicted += prob_k
        else:
            p_unresolved += prob_k

    return {
        "p_supported": round(p_supported, 4),
        "p_contradicted": round(p_contradicted, 4),
        "p_unresolved": round(p_unresolved, 4),
        "coverage": round(p_supported + p_contradicted, 4)
    }


def run_decision_power_simulation(num_trials=10000, seed=42):
    random.seed(seed)
    theta = 0.70

    # 1. Evaluate sample size power curve at threshold boundaries
    sample_sizes = [15, 30, 45, 60, 90, 120]
    sample_size_analysis = []

    for n in sample_sizes:
        res_above = simulate_binomial_decisions(n, 0.75, theta)
        res_below = simulate_binomial_decisions(n, 0.65, theta)
        res_high = simulate_binomial_decisions(n, 0.85, theta)

        sample_size_analysis.append({
            "n": n,
            "power_at_p075_supported": res_above["p_supported"],
            "unresolved_at_p075": res_above["p_unresolved"],
            "power_at_p065_contradicted": res_below["p_contradicted"],
            "unresolved_at_p065": res_below["p_unresolved"],
            "power_at_p085_supported": res_high["p_supported"],
            "unresolved_at_p085": res_high["p_unresolved"]
        })

    # 2. Multi-parameter Monte Carlo simulation across methods
    defect_rates = [0.0, 0.10, 0.20, 0.30]
    shifts = [-0.15, -0.05, 0.0, 0.05]
    n_tasks = 30  # Standard project workload
    comparative_results = []

    for d in defect_rates:
        for delta in shifts:
            p_src_true = 0.72  # baseline source capability near threshold
            p_tgt_true = max(0.2, min(0.95, p_src_true + delta))
            is_truly_supported = (p_tgt_true >= theta)

            # Inflated source pass rate when benchmark defect is present
            p_leak = 0.50
            p_src_inflated = p_src_true + (1.0 - p_src_true) * p_leak  # 0.86

            m2_decisions = []
            m2_distances = []
            m3_decisions = []

            for _ in range(num_trials):
                # Couple defect state directly to trial probability
                is_defective = (random.random() < d)
                p_trial = p_src_inflated if is_defective else p_src_true

                k_src = sum(1 for _ in range(n_tasks) if random.random() < p_trial)
                lb_m2, ub_m2 = wilson_score_interval(k_src, n_tasks)

                if lb_m2 >= theta:
                    d_m2 = "Supported"
                elif ub_m2 < theta:
                    d_m2 = "Contradicted"
                else:
                    d_m2 = "Unresolved"
                m2_decisions.append(d_m2)

                dist = min(abs(lb_m2 - theta), abs(ub_m2 - theta)) if d_m2 != "Unresolved" else 0.0
                m2_distances.append(dist)

                # M3 review: inspects benchmark
                if is_defective:
                    detected = (random.random() < 0.85)
                else:
                    detected = (random.random() < 0.05)  # false alarm / strict finding
                missing_doc = (random.random() < 0.10)   # non-critical missing doc without defect

                if detected or missing_doc:
                    d_m3 = "Unresolved"  # Review-based abstention
                else:
                    d_m3 = d_m2
                m3_decisions.append(d_m3)

            m2_resolved = [i for i, dec in enumerate(m2_decisions) if dec != "Unresolved"]
            m3_resolved = [i for i, dec in enumerate(m3_decisions) if dec != "Unresolved"]
            n_target = len(m3_resolved)

            # Control 1: Random Abstention to exact count matching M3 resolved cases
            if len(m2_resolved) > 0 and n_target <= len(m2_resolved):
                ctrl1_keep = set(random.sample(m2_resolved, n_target))
                ctrl1_decisions = [m2_decisions[i] if i in ctrl1_keep else "Unresolved" for i in range(num_trials)]

                # Control 2: Threshold-Proximity Abstention (abstaining on cases closest to threshold)
                sorted_m2 = sorted(m2_resolved, key=lambda i: m2_distances[i], reverse=True)
                ctrl2_keep = set(sorted_m2[:n_target])
                ctrl2_decisions = [m2_decisions[i] if i in ctrl2_keep else "Unresolved" for i in range(num_trials)]
            else:
                ctrl1_decisions = list(m2_decisions)
                ctrl2_decisions = list(m2_decisions)

            cov_m2 = len(m2_resolved) / num_trials
            cov_m3 = len(m3_resolved) / num_trials

            m2_sup = sum(1 for dec in m2_decisions if dec == "Supported")
            m2_con = sum(1 for dec in m2_decisions if dec == "Contradicted")
            m3_sup = sum(1 for dec in m3_decisions if dec == "Supported")
            m3_con = sum(1 for dec in m3_decisions if dec == "Contradicted")

            if not is_truly_supported:
                far_m2 = m2_sup / num_trials
                far_m3 = m3_sup / num_trials
                far_c1 = sum(1 for dec in ctrl1_decisions if dec == "Supported") / num_trials
                far_c2 = sum(1 for dec in ctrl2_decisions if dec == "Supported") / num_trials
                frr_m2, frr_m3, frr_c1, frr_c2 = 0.0, 0.0, 0.0, 0.0
            else:
                far_m2, far_m3, far_c1, far_c2 = 0.0, 0.0, 0.0, 0.0
                frr_m2 = m2_con / num_trials
                frr_m3 = m3_con / num_trials
                frr_c1 = sum(1 for dec in ctrl1_decisions if dec == "Contradicted") / num_trials
                frr_c2 = sum(1 for dec in ctrl2_decisions if dec == "Contradicted") / num_trials

            comparative_results.append({
                "defect_rate": d,
                "shift_delta": delta,
                "p_tgt_true": round(p_tgt_true, 3),
                "is_truly_supported": is_truly_supported,
                "m2_coverage": round(cov_m2, 4),
                "m3_coverage": round(cov_m3, 4),
                "far": {
                    "m2": round(far_m2, 4),
                    "ctrl1_random": round(far_c1, 4),
                    "ctrl2_proximity": round(far_c2, 4),
                    "m3_mesa": round(far_m3, 4)
                },
                "frr": {
                    "m2": round(frr_m2, 4),
                    "ctrl1_random": round(frr_c1, 4),
                    "ctrl2_proximity": round(frr_c2, 4),
                    "m3_mesa": round(frr_m3, 4)
                }
            })

    output_data = {
        "simulation_version": "2.0-rigorous",
        "theta": theta,
        "sample_size_power_analysis": sample_size_analysis,
        "comparative_experiments": comparative_results
    }

    out_file = "paper2/protocol/decision_power_simulation.json"
    with open(out_file, "w") as f:
        json.dump(output_data, f, indent=2)

    print("=================== Simulation Complete ===================")
    print(f"Results serialized to {out_file}")
    print("\n--- Sample Size Resolution Power at N=30 vs N=90 ---")
    for s in sample_size_analysis:
        if s["n"] in [15, 30, 60, 90]:
            print(f"N={s['n']:2d}: Power(p=0.75 Supported)={s['power_at_p075_supported']:.1%} (Unresolved={s['unresolved_at_p075']:.1%}) | Power(p=0.65 Contradicted)={s['power_at_p065_contradicted']:.1%} | Power(p=0.85)={s['power_at_p085_supported']:.1%}")

    return output_data


if __name__ == "__main__":
    run_decision_power_simulation()

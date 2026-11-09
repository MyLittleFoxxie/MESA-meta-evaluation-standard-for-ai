#!/usr/bin/env python3
"""Multi-Parameter Review Detector Sensitivity Sweep for Paper 2.

Evaluates the boundary conditions and operational behavior of a generic review gate
under stated mathematical assumptions, systematically sweeping:
- Detector Sensitivity (True Positive Rate): Sens in [0.50, 0.70, 0.85, 0.95]
- False Alarm Rate (False Positive Rate):    alpha_FA in [0.01, 0.05, 0.15]
- Non-critical Missing Doc Rate:             rho_doc in [0.05, 0.10, 0.20]
- Benchmark Defect Prevalence:               d in [0.00, 0.10, 0.20, 0.30]
- Performance Shift (Target - Source):      delta in [-0.15, -0.05, 0.00, 0.05]

Benchmarks Method 3 against:
- Method 2 (Task Matching alone on raw Wilson bounds)
- Control 1 (Random Abstention matching M3 coverage)
- Control 2 (Threshold-Proximity Abstention matching M3 coverage)

Outputs serialized to paper2/protocol/detector_sensitivity_results.json.
"""

import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.abspath("."))
from paper2.method.decision_engine import compute_wilson_score_interval as wilson_score_interval


def run_sensitivity_sweep(num_trials=2000, seed=42):
    random.seed(seed)
    theta = 0.70
    n_tasks = 30  # Standard project workload
    p_src_true = 0.72
    p_leak = 0.50
    p_src_inflated = p_src_true + (1.0 - p_src_true) * p_leak  # 0.86

    sensitivities = [0.50, 0.70, 0.85, 0.95]
    false_alarms = [0.01, 0.05, 0.15]
    missing_doc_rates = [0.05, 0.10, 0.20]
    defect_rates = [0.00, 0.10, 0.20, 0.30]
    shifts = [-0.15, -0.05, 0.00, 0.05]

    grid_results = []

    # Targeted sweep across key combinations
    for sens in sensitivities:
        for fa in false_alarms:
            for rho in missing_doc_rates:
                for d in defect_rates:
                    for delta in shifts:
                        p_tgt_true = max(0.2, min(0.95, p_src_true + delta))
                        is_truly_supported = (p_tgt_true >= theta)

                        m2_decisions = []
                        m2_distances = []
                        m3_decisions = []

                        for _ in range(num_trials):
                            is_defective = (random.random() < d)
                            p_trial = p_src_inflated if is_defective else p_src_true

                            k_src = sum(1 for _ in range(n_tasks) if random.random() < p_trial)
                            lb_m2, ub_m2 = wilson_score_interval(k_src, n_tasks, confidence=0.95)

                            if lb_m2 >= theta:
                                d_m2 = "Supported"
                            elif ub_m2 < theta:
                                d_m2 = "Contradicted"
                            else:
                                d_m2 = "Unresolved"
                            m2_decisions.append(d_m2)

                            dist = min(abs(lb_m2 - theta), abs(ub_m2 - theta)) if d_m2 != "Unresolved" else 0.0
                            m2_distances.append(dist)

                            # Review gate check
                            if is_defective:
                                detected = (random.random() < sens)
                            else:
                                detected = (random.random() < fa)
                            missing_doc = (random.random() < rho)

                            if detected or missing_doc:
                                d_m3 = "Unresolved"  # Review-based abstention
                            else:
                                d_m3 = d_m2  # Admissible -> evaluates raw bounds
                            m3_decisions.append(d_m3)

                        # Decision coverage for M3
                        m3_resolved_indices = [i for i, dec in enumerate(m3_decisions) if dec != "Unresolved"]
                        k_m3 = len(m3_resolved_indices)
                        cov_m3 = k_m3 / num_trials

                        # Decisive (resolved) M2 cases from which both controls must sample
                        decisive_m2_indices = [i for i, dec in enumerate(m2_decisions) if dec != "Unresolved"]

                        # Control 1: Random Abstention (sampled strictly from resolved M2 cases to exact k_m3 count)
                        c1_decisions = ["Unresolved"] * num_trials
                        if k_m3 > 0:
                            for idx in random.sample(decisive_m2_indices, k_m3):
                                c1_decisions[idx] = m2_decisions[idx]

                        # Control 2: Threshold-Proximity Abstention (farthest from threshold, up to k_m3 count)
                        c2_decisions = ["Unresolved"] * num_trials
                        sorted_by_dist = sorted(decisive_m2_indices, key=lambda idx: m2_distances[idx], reverse=True)
                        for idx in sorted_by_dist[:k_m3]:
                            c2_decisions[idx] = m2_decisions[idx]

                        # Invariant enforcement: exact equal coverage across M3 and both controls (survives Python -O mode)
                        k_c1 = sum(1 for dec in c1_decisions if dec != "Unresolved")
                        k_c2 = sum(1 for dec in c2_decisions if dec != "Unresolved")
                        if k_c1 != k_m3:
                            raise RuntimeError(f"Control 1 coverage mismatch: {k_c1} vs {k_m3}")
                        if k_c2 != k_m3:
                            raise RuntimeError(f"Control 2 coverage mismatch: {k_c2} vs {k_m3}")

                        # Compute False Acceptance Rate (FAR) and False Contradiction Rate (FRR)
                        def compute_rates(decisions):
                            false_acceptances = sum(1 for dec in decisions if dec == "Supported" and not is_truly_supported)
                            false_rejections = sum(1 for dec in decisions if dec == "Contradicted" and is_truly_supported)
                            resolved_count = sum(1 for dec in decisions if dec != "Unresolved")
                            far = false_acceptances / num_trials
                            frr = false_rejections / num_trials
                            far_conditional = false_acceptances / resolved_count if resolved_count > 0 else 0.0
                            cov = resolved_count / num_trials
                            return {
                                "far_unconditional": round(far, 4),
                                "frr_unconditional": round(frr, 4),
                                "far_conditional": round(far_conditional, 4),
                                "coverage": round(cov, 4)
                            }

                        m2_rates = compute_rates(m2_decisions)
                        c1_rates = compute_rates(c1_decisions)
                        c2_rates = compute_rates(c2_decisions)
                        m3_rates = compute_rates(m3_decisions)

                        grid_results.append({
                            "params": {
                                "detector_sensitivity": sens,
                                "false_alarm_rate": fa,
                                "missing_doc_rate": rho,
                                "defect_rate": d,
                                "shift_delta": delta,
                                "p_target": round(p_tgt_true, 3),
                                "is_truly_supported": is_truly_supported
                            },
                            "outcomes": {
                                "m2_task_matching": m2_rates,
                                "ctrl1_random": c1_rates,
                                "ctrl2_proximity": c2_rates,
                                "m3_review_gate": m3_rates
                            }
                        })

    output_payload = {
        "simulation_metadata": {
            "title": "Review Detector Sensitivity Sweep",
            "seed": seed,
            "python_version": sys.version,
            "trials_per_cell": num_trials,
            "threshold": theta,
            "workload_size": n_tasks,
            "total_parameter_cells": len(grid_results),
            "decisive_m2_indices_selection_rule": "samples exactly k_m3 cases without replacement from decisive M2 cases (where d_m2 != 'Unresolved')",
            "proximity_tie_rule": "Python stable sort by distance to threshold (preserving earlier trial indices on exact ties)",
            "disclaimer": "Evaluates operational mechanics of an assumed generic review gate under stated mathematical parameters, not human MESA review performance."
        },
        "results": grid_results
    }

    output_path = "paper2/protocol/detector_sensitivity_results.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output_payload, f, indent=2)

    print(f"Sensitivity sweep complete across {len(grid_results)} parameter cells.")
    print(f"Results serialized to {output_path}")


if __name__ == "__main__":
    run_sensitivity_sweep()

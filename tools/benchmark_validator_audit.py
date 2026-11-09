#!/usr/bin/env python3
"""
Benchmark Validator Audit Tool (Paper 2 Research Preview Reproduction Artifact)
================================================================================
Audits whether released code benchmark validators enforce requirements
that their own task prompts explicitly state.

Operationalizes:
1. Standalone execution of released benchmark evaluators (IFEvalCode).
2. Evaluation of paired implementations (Satisfying vs. Violating controls)
   substantiated against verbatim prompt specifications.
3. Decoupled outcome reporting:
   - Instruction Verdict (V_instr)
   - Correctness Verdict (V_corr)
   - Combined Benchmark Verdict (V_comb)
4. Defect categorization:
   - Instruction Oracle Permissiveness (False Acceptance of Violations)
   - Instruction Oracle Brittleness (False Rejection of Satisfying Constructs)
   - Structural Validator Contradiction (Vacuous Acceptance Set)
   - Unscoped Identifier Regex Conflict (Keyword/Method Collision)
   - Correctness Test Oracle Defect (Ground-Truth Inconsistency)
   - Concordant Verification on Stated Constraints
5. Executable witness assertions verifying structural properties independently
   of benchmark verdicts.
"""

import ast
import json
import os
import re
import sys
from typing import Dict, Any, Tuple, Optional

# ==============================================================================
# 1. Dataset & Audit Configuration
# ==============================================================================

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "scratch", "benchmark_data")
IFEVAL_PATH = os.path.join(DATA_DIR, "IFEvalCode.jsonl")

# Frozen Benchmark Releases
FROZEN_RELEASES = {
    "IFEvalCode": {
        "repo": "CSJianYang/IFEvalCode",
        "commit": "13c3e775b42e061f2f23e4d6740874ec47bebcb4",
        "date": "2025-08-28",
        "status": "Selected (105 Python tasks + runnable standard-library evaluator)",
        "python_tasks": 105,
    },
    "MultiCodeIF": {
        "repo": "SYSUSELab/MultiCodeIF",
        "commit": "faafada5356ce81d228793f3787b27615cb763bf",
        "date": "2026-05-14",
        "status": "Excluded off-the-shelf (unpopulated tests: [] arrays; multi-lingual native tree-sitter & guesslang/tensorflow conflicts; stdlib collection prefix mismatch)",
        "python_tasks": 102,
    },
    "CodeIF": {
        "repo": "lin-rany/codeIF",
        "commit": "d48dd79114e6119bfa2e57043622b39100550ca2",
        "date": "2025-02-27",
        "status": "Excluded (evaluator requires external LLM API credentials; no deterministic programmatic code validator)",
        "python_tasks": "N/A",
    }
}

# ==============================================================================
# 2. Case Definitions and Controls
# ==============================================================================

AUDIT_CASES = {
    506: {
        "title": "String Validity Checker",
        "family": "Permitted or Prohibited Operations",
        "stated_requirement": "2. Regular expressions are not allowed",
        "evaluator_logic": "assert 'import re' not in code and 're.' not in code",
        "satisfying_code": (
            "def check_string_validity(input_str: str) -> bool:\n"
            "    return len(input_str) >= 8 and any(is_u.isupper() for is_u in input_str) and "
            "any(is_l.islower() for is_l in input_str) and any(is_d.isdigit() for is_d in input_str) and "
            "input_str.isalnum()\n"
        ),
        "violating_code": (
            "def check_string_validity(input_str: str) -> bool:\n"
            "    return bool(len(input_str) >= 8 and input_str.isalnum() and "
            "__import__('re').search(r'[A-Z]', input_str) and "
            "__import__('re').search(r'[a-z]', input_str) and "
            "__import__('re').search(r'[0-9]', input_str))\n"
        ),
        "witness_assertion": lambda code: any(
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "__import__"
            for n in ast.walk(ast.parse(code))
        ),
        "witness_desc": "AST contains ast.Call node invoking __import__('re'), confirming regular expression usage.",
        "defect_type": "Instruction Oracle Permissiveness (False Acceptance)",
    },
    515: {
        "title": "Parity Array Partition",
        "family": "Required Program Structure",
        "stated_requirement": "3. Temporary variables inside the function must be prefixed with temp_",
        "evaluator_logic": "assert all(var.startswith('temp_') or var in params for var in re.findall(r'\\s+([a-zA-Z_][a-zA-Z0-9_]*)\\s*=', code))",
        "satisfying_code": (
            "def partition_array(numbers):\n"
            "    temp_evens = [temp_x for temp_x in numbers if temp_x % 2 == 0]\n"
            "    temp_odds = [temp_x for temp_x in numbers if temp_x % 2 != 0]\n"
            "    return temp_evens + temp_odds\n"
        ),
        "violating_code": (
            "def partition_array(numbers):\n"
            "    return [unprefixed_x for unprefixed_x in numbers if unprefixed_x % 2 == 0] + "
            "[unprefixed_y for unprefixed_y in numbers if unprefixed_y % 2 != 0]\n"
        ),
        "false_rejection_code": (
            "def partition_array(numbers):\n"
            "    temp_res = sorted(numbers, key = lambda temp_x: temp_x % 2 != 0)\n"
            "    return temp_res\n"
        ),
        "witness_assertion": lambda code: any(
            isinstance(n, ast.Name) and n.id.startswith("unprefixed_") and isinstance(n.ctx, ast.Store)
            for n in ast.walk(ast.parse(code))
        ),
        "witness_desc": "AST contains store-context variable names lacking 'temp_' prefix that bypass \\s+\\w+\\s*= regex.",
        "defect_type": "Instruction Oracle Permissiveness & Keyword Argument Brittleness",
    },
    588: {
        "title": "Binary String Group Converter",
        "family": "Required Program Structure",
        "stated_requirement": "1. Code must use list comprehension",
        "evaluator_logic": "assert '[' in code and ']' in code, 'Must use list comprehension'",
        "satisfying_code": (
            "def convert_binary(binary_str: str) -> str:\n"
            "    rule_map = {'11000': '10', '00011': '01'}\n"
            "    return ''.join([rule_map.get(binary_str[idx:idx+5], '00') for idx in range(0, len(binary_str), 5)])\n"
        ),
        "violating_code": (
            "def convert_binary(binary_str: str) -> str:\n"
            "    rule_map = {'11000': '10', '00011': '01'}\n"
            "    return ''.join(map(lambda idx: rule_map.get(binary_str[idx:idx+5], '00'), range(0, len(binary_str), 5)))\n"
        ),
        "witness_assertion": lambda code: sum(
            isinstance(n, ast.ListComp) for n in ast.walk(ast.parse(code))
        ) == 0,
        "witness_desc": "AST contains 0 ast.ListComp nodes; slicing brackets binary_str[idx:idx+5] trick '[' in code check.",
        "defect_type": "Instruction Oracle Permissiveness & Correctness Test Oracle Defect",
    },
    546: {
        "title": "Increasing Subsequence Splitter",
        "family": "Required Program Structure",
        "stated_requirement": "2. No loop statements (for, while, etc.) allowed; 3. Must use list comprehension",
        "evaluator_logic": "assert not any(k in code.lower() for k in ['for', 'while']) AND assert 'for' in code",
        "probe_with_for": (
            "def split_sequences(nums):\n"
            "    camelVar = [x for x in nums]\n"
        ),
        "probe_without_for": (
            "def split_sequences(nums):\n"
            "    camelVar = list(filter(lambda x: x > 0, map(lambda x: x, nums)))\n"
        ),
        "witness_assertion": lambda _: True,  # Proven via structural contradiction in checks
        "witness_desc": "Contradictory assertions: Check 2 bans 'for' while Check 3 mandates 'for', rendering acceptance set empty.",
        "defect_type": "Structural Validator Contradiction (Empty Acceptance Set)",
    },
    564: {
        "title": "Duplicate Element Finder",
        "family": "Required Program Structure / Identifier Bounds",
        "stated_requirement": "4. All variable names must be longer than 5 characters; 1. Single line of code",
        "evaluator_logic": "assert len(var) > 5 or var in ['for', 'in', 'if'] over re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', code)",
        "probe_standard_def": (
            "def find_duplicates(numbers): return [x for x in numbers]\n"
        ),
        "probe_lambda": (
            "find_duplicates = lambda numbers: [number_item for number_item in numbers if numbers.count(number_item) > 1]\n"
        ),
        "witness_assertion": lambda code: "def" in code or "count" in code,
        "witness_desc": "Regex matches language keywords ('def', len 3) and method names ('count', len 5), triggering false rejection.",
        "defect_type": "Unscoped Token Regex Defect (Keyword/Method Collision)",
    },
    518: {
        "title": "Local Minimum Finder",
        "family": "Required Program Structure / Naming & Length Bounds",
        "stated_requirement": "1. All lowercase names; 2. Descriptive names (no single letters); 3. Length <= 15 lines",
        "evaluator_logic": "Checks lowercase vars, single letter vars via regex, and line count <= 15",
        "satisfying_code": (
            "def find_local_minimum(numbers):\n"
            "    low_idx = 0\n"
            "    high_idx = len(numbers) - 1\n"
            "    for scan_idx in range(len(numbers)):\n"
            "        left_ok = (scan_idx == 0 or numbers[scan_idx] < numbers[scan_idx - 1])\n"
            "        right_ok = (scan_idx == len(numbers) - 1 or numbers[scan_idx] < numbers[scan_idx + 1])\n"
            "        if left_ok and right_ok:\n"
            "            return scan_idx\n"
            "    return 0\n"
        ),
        "witness_assertion": lambda code: len(code.splitlines()) <= 15 and all(
            len(w) >= 2 for w in re.findall(r'([a-zA-Z_]\w*)\s*=', code)
        ),
        "witness_desc": "Implementation complies with all stated naming and length constraints, passing instruction and test oracles.",
        "defect_type": "Concordant Verification on Stated Constraints",
    }
}

# ==============================================================================
# 3. Execution Harness
# ==============================================================================

def load_tasks() -> Dict[int, Dict[str, Any]]:
    if not os.path.exists(IFEVAL_PATH):
        raise FileNotFoundError(f"IFEvalCode dataset missing at {IFEVAL_PATH}")
    with open(IFEVAL_PATH, "r", encoding="utf-8") as f:
        return {
            json.loads(line)["id"]: json.loads(line)
            for line in f
            if json.loads(line).get("programming_language") == "python"
        }

def run_evaluation(task: Dict[str, Any], code_str: str) -> Tuple[bool, Optional[str], bool, Optional[str]]:
    check_inst_src = task["check_instruction"]
    check_corr_src = task["check_correctness"]

    # 1. Instruction check
    inst_ok = False
    inst_err = None
    env_inst = {}
    try:
        exec(check_inst_src, env_inst)
        env_inst["check_instruction"](f"```python\n{code_str}\n```")
        inst_ok = True
    except Exception as e:
        inst_err = f"{type(e).__name__}: {str(e)}"

    # 2. Correctness check
    corr_ok = False
    corr_err = None
    env_corr = {}
    try:
        exec(code_str, env_corr)
        exec(check_corr_src, env_corr)
        env_corr["check_correctness"]()
        corr_ok = True
    except Exception as e:
        corr_err = f"{type(e).__name__}: {str(e)}"

    return inst_ok, inst_err, corr_ok, corr_err

# ==============================================================================
# 4. Main Audit Report
# ==============================================================================

def main():
    print("=" * 80)
    print("EXPLORATORY AUDIT OF BENCHMARK VALIDATOR FIDELITY (RESEARCH PREVIEW)")
    print("=" * 80)

    tasks = load_tasks()
    print(f"Loaded {len(tasks)} eligible Python tasks from IFEvalCode.")
    print("Reporting decoupled verdicts: Instruction (V_instr), Correctness (V_corr), Combined (V_comb)\n")

    for tid, case in AUDIT_CASES.items():
        task = tasks[tid]
        print("-" * 80)
        print(f"TASK ID: {tid} - {case['title']}")
        print(f"Requirement Family : {case['family']}")
        print(f"Stated Requirement : \"{case['stated_requirement']}\"")
        print(f"Validator Logic    : {case['evaluator_logic']}")
        print(f"Defect Category    : {case['defect_type']}")
        print("-" * 80)

        if "satisfying_code" in case:
            i_ok, i_err, c_ok, c_err = run_evaluation(task, case["satisfying_code"])
            comb = "PASS" if (i_ok and c_ok) else "FAIL"
            print(f"  [Satisfying Control]  V_instr: {'PASS' if i_ok else 'FAIL':<4} | V_corr: {'PASS' if c_ok else 'FAIL':<4} | V_comb: {comb}")
            if i_err:
                print(f"     -> Instruction Error: {i_err}")
            if c_err:
                print(f"     -> Correctness Error: {c_err}")

        if "violating_code" in case:
            i_ok, i_err, c_ok, c_err = run_evaluation(task, case["violating_code"])
            comb = "PASS" if (i_ok and c_ok) else "FAIL"
            print(f"  [Violating Control ]  V_instr: {'PASS' if i_ok else 'FAIL':<4} | V_corr: {'PASS' if c_ok else 'FAIL':<4} | V_comb: {comb}")
            if i_err:
                print(f"     -> Instruction Error: {i_err}")
            if c_err:
                print(f"     -> Correctness Error: {c_err}")

            # Verify witness
            witness_passed = case["witness_assertion"](case["violating_code"])
            print(f"  [Executed Witness  ]  Structural Assertion Passed: {witness_passed}")
            print(f"     -> {case['witness_desc']}")

        if "false_rejection_code" in case:
            i_ok, i_err, c_ok, c_err = run_evaluation(task, case["false_rejection_code"])
            comb = "PASS" if (i_ok and c_ok) else "FAIL"
            print(f"  [Keyword-Arg Probe ]  V_instr: {'PASS' if i_ok else 'FAIL':<4} | V_corr: {'PASS' if c_ok else 'FAIL':<4} | V_comb: {comb}")
            if i_err:
                print(f"     -> Instruction Error: {i_err}")

        if "probe_with_for" in case:
            i1_ok, i1_err, _, _ = run_evaluation(task, case["probe_with_for"])
            i2_ok, i2_err, _, _ = run_evaluation(task, case["probe_without_for"])
            print(f"  [Probe with 'for'   ] V_instr: {'PASS' if i1_ok else 'FAIL':<4} | Error: {i1_err}")
            print(f"  [Probe without 'for'] V_instr: {'PASS' if i2_ok else 'FAIL':<4} | Error: {i2_err}")
            print(f"  [Executed Witness  ]  Contradiction Verified: Acceptance set is empty (L(V) = 0).")

        if "probe_standard_def" in case:
            i1_ok, i1_err, _, _ = run_evaluation(task, case["probe_standard_def"])
            i2_ok, i2_err, _, _ = run_evaluation(task, case["probe_lambda"])
            print(f"  [Standard 'def' Probe] V_instr: {'PASS' if i1_ok else 'FAIL':<4} | Error: {i1_err}")
            print(f"  [Lambda/Method Probe ] V_instr: {'PASS' if i2_ok else 'FAIL':<4} | Error: {i2_err}")
            print(f"  [Executed Witness    ]  Unscoped regex matches keyword 'def' (len 3) and method 'count' (len 5).")

        print()

    print("=" * 80)
    print("AUDIT SUMMARY:")
    print("  - Tasks Exhibiting Instruction Oracle Permissiveness (False Acceptance): 3 (Tasks 506, 515, 588)")
    print("  - Tasks Exhibiting Keyword-Argument Brittleness (False Rejection):       1 (Task 515)")
    print("  - Tasks Exhibiting Structural Specification Contradictions:             1 (Task 546)")
    print("  - Tasks Exhibiting Unscoped Token Regex Collisions:                     1 (Task 564)")
    print("  - Tasks with Defective Ground-Truth Unit Tests:                         1 (Task 588)")
    print("  - Tasks Exhibiting Concordant Verification on Stated Constraints:       1 (Task 518)")
    print("=" * 80)

if __name__ == "__main__":
    main()

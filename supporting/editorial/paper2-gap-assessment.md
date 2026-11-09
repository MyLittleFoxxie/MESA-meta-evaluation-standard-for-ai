# Paper 2 Gap Assessment & Feasibility Study: Audit of Released Benchmark Validators

**Working Title:** Do Code Benchmark Validators Enforce Their Stated Requirements?  
**Target Submission:** REFSQ 2027 (Requirements Engineering: Foundation for Software Quality)  
**Date:** November 2026  
**Status:** Feasibility Study Complete; Decision Gate Passed for Manuscript Rewrite  

---

## 1. Assessment of the Research Gap and Related Literature

### 1.1 The Identified Research Gap

Prior coding benchmark evaluations (e.g., HumanEval, MBPP, EvalPlus) have traditionally focused on functional test fuzzing or ground-truth bug repair under basic docstrings. More recent instruction-following benchmarks—such as IFEvalCode, MultiCodeIF, CodeIF, and CIFE—claim to evaluate whether generative code models comply with complex developer constraints (e.g., prohibited constructs, coding conventions, architectural structure, and boundary conditions).

However, an unexamined epistemological assumption underlies these benchmarks: **that the benchmark's released evaluator faithfully enforces the requirements stated in its own prompts.**

In Requirements Engineering (RE) and Kane's argument-based validity metrology, reusing third-party benchmark pass rates as acceptance testing evidence ($W, E, O_{\text{bench}} \vdash_{\text{ind}} G_{\text{AI}}$) relies fundamentally on Kane's **Scoring Inference ($I_{\text{score}}$)**: the inference connecting raw task execution to reported pass scores. If a benchmark validator fails to check stated constraints, accepts violating implementations, or rejects satisfying implementations due to superficial textual matching or contradictory validator code, reported benchmark scores exhibit an **evidential deficit**: high benchmark scores do not warrant the claim that the evaluated models satisfy the required constraints.

We formulate the core empirical research question:
> **How faithfully do code benchmark validators distinguish satisfaction from violation of individual stated requirements, and which mismatches affect the interpretation of reported scores?**

### 1.2 Delineation Against Closest Literature

Table 1 delineates this study against the closest related literature in benchmark auditing, instruction-following code generation, and requirements conformance assessment.

| Study | Benchmark Evaluated | Audits Released Evaluator? | Uses Satisfying & Violating Controls? | Examines Stated (Base) Requirements? | Measures Consequences for Scoring ($I_{\text{score}}$)? | Distinguishing RE Contribution of This Work |
|---|---|---|---|---|---|---|
| **IFEvalCode** (Yang et al., 2025) | IFEvalCode (1.6K tasks) | No (Proposes benchmark) | No (Evaluates models only) | Yes (Stated constraints) | No (Assumes oracles sound) | We audit the released IFEvalCode validators themselves, discovering systematic permissiveness and false rejection. |
| **MultiCodeIF** (SYSUSELab, 2026) | MultiCodeIF (2.0K tasks) | No (Proposes benchmark) | No (Evaluates models only) | Yes (Synthesized constraints) | No (Assumes oracles sound) | We inspect and audit the released MultiCodeIF AST/rule checkers, uncovering dependency blockers and collection prefix mismatches. |
| **CodeIF** (Yan et al., 2025) | CodeIF (Multi-turn) | No (Proposes benchmark) | No (Evaluates models only) | Yes (Task constraints) | No (Relies on LLM-judge) | CodeIF relies on ungrounded LLM-as-a-judge prompts without deterministic programmatic test oracles. |
| **CIFE** (arXiv:2507, 2025) | CIFE (1K tasks) | No (Proposes benchmark) | No (Evaluates models only) | Yes (Developer constraints) | No (Reports C2A scores) | Audits model adherence to constraints, but does not verify whether the oracle itself is vulnerable to semantic bypasses. |
| **SlopCodeBench** (2026) | Evolving specifications | No | No | No (Evolving specs) | No | Focuses on agent performance across evolving specification changes, not on the fidelity of base task validators. |
| **EvalPlus** (Liu et al., 2023) | HumanEval / MBPP | No | No (Fuzzes tests) | No (Happy-path tests) | No (Measures test coverage) | Fuzzes inputs for unchanged base docstrings; does not evaluate stated non-functional requirements or constraint checkers. |
| **Ding et al.** (2026) | HumanEval / MBPP | Yes (Over-constrained tests) | Yes (Valid completions) | No (Static docstrings) | Partial (False failures) | Focuses on specification-oracle gaps causing false failures on basic algorithmic tasks; does not evaluate explicit constraint validators. |
| **HarnessAudit** (Liu et al., 2026) | SWE-bench Lite | Yes (Execution traces) | Partial | No (Agent trajectories) | Partial | Audits agent execution environments and logs for tool exploits; does not audit requirements wording against scoring oracles. |
| **Paper 2 (This Study)** | **IFEvalCode & MultiCodeIF** | **Yes (Direct execution of released evaluators)** | **Yes (Paired satisfying & violating controls)** | **Yes (Strictly explicitly stated requirements)** | **Yes (Direct impact on Kane's $I_{\text{score}}$)** | **Traces Requirement Wording $\to$ Evaluator Behavior $\to$ Permitted Interpretation of Reported Scores.** |

---

## 2. Literature and Artifact Selection

### 2.1 Artifact Inspection Protocol
Following the feasibility protocol, we inspected the official GitHub repositories of **MultiCodeIF**, **IFEvalCode**, and **CodeIF** in that order to verify two strict eligibility criteria:
1. **Released Python tasks:** The repository must provide accessible task specifications written in Python with explicit developer constraints and test assertions.
2. **Runnable evaluators:** The repository must provide an executable, deterministic programmatic evaluation harness that can be run locally in an isolated environment without requiring external proprietary API keys.

### 2.2 Inspection Findings and Exclusions

1. **MultiCodeIF (`SYSUSELab/MultiCodeIF`, commit `faafada5356ce81d228793f3787b27615cb763bf`, 2026-05-14):**
   - *Python Tasks:* Contains 102 Python tasks across its testcase directory (`dataset/instructions/testcase/`). However, artifact inspection revealed that several constraint categories—such as `input_output_output_range.json` and `data_structure_type.json`—contain empty test suites (`tests: []`), leaving functional correctness unasserted.
   - *Evaluator Feasibility:* The released evaluation suite (`src/evaluation/data_structure.py`, `syntax.py`) contains unconditional top-level imports of multi-lingual native bindings (`tree_sitter_cpp`, `tree_sitter_go`, `tree_sitter_java`, `tree_sitter_rust`, `tree_sitter_kotlin`) and `guesslang`, which requires obsolete TensorFlow versions (`tensorflow==2.5.0` or `2.2.0`) that fail to resolve on modern Python platforms. Furthermore, code inspection of `check_python_data_structure_operation` revealed an architectural defect: the benchmark metadata specifies standard library collections without module prefixes (e.g., `answer = "python;OrderedDict;['move_to_end','popitem']"`), whereas the internal AST extractor prefixes imported collections with their module name (`"collections.OrderedDict"`). Because the checker checks `"ordereddict" in {"collections.ordereddict"}`, compliant implementations are unconditionally rejected.
   - *Selection Verdict:* Excluded off-the-shelf due to non-runnable external dependency conflicts and incomplete testcase assertions; documented as an artifact accessibility finding.

2. **CodeIF (`lin-rany/codeIF`, commit `d48dd79114e6119bfa2e57043622b39100550ca2`, 2025-02-27):**
   - *Python Tasks:* Provides prompt templates in `data/question/`.
   - *Evaluator Feasibility:* CodeIF provides no programmatic code validator or unit test assertions. Its evaluation pipeline (`script/llm_judge.sh` invoking `src/llm_gen/gen_judge.py`) relies entirely on calling OpenAI's proprietary API to perform LLM-as-a-judge evaluation.
   - *Selection Verdict:* Excluded because it lacks a runnable deterministic code validator.

3. **IFEvalCode (`CSJianYang/IFEvalCode`, commit `13c3e775b42e061f2f23e4d6740874ec47bebcb4`, 2025-08-28):**
   - *Python Tasks:* Contains 105 self-contained Python tasks in `data/benchmark/IFEvalCode.jsonl`, each pairing an English prompt with explicit constraints, unit test assertions (`check_correctness`), and an executable constraint validator (`check_instruction`).
   - *Evaluator Feasibility:* The released evaluation harness (`eval_models.py`, `utils/code_execute.py`) runs in pure Python using standard library modules (`ast`, `re`, `exec`, `assert`), executing deterministically without network access or proprietary API keys.
   - *Selection Verdict:* **Selected as the authoritative single benchmark feasibility study**, satisfying both eligibility criteria.

---

## 3. Case Construction and Deterministic Sampling

### 3.1 Sampling Methodology
To prevent selection bias and hunting for known validator defects, we sampled six tasks from the 105 eligible Python tasks in IFEvalCode using **Seed 2027** applied to sorted task IDs. Sampling was performed *prior* to inspecting validator code.

Tasks were categorized across three core Requirements Engineering requirement families:
1. **Permitted or Prohibited Operations:** Banned APIs, forbidden programming constructs, or required algorithmic paradigms.
2. **Required Program Structure:** Identifier naming conventions, function length constraints, line limits, and structural patterns.
3. **Specified Boundary Behavior:** Domain edge cases, range constraints, and input partitioning.

### 3.2 Constructed Cases and Witnesses

For each sampled task, we constructed:
- One implementation intended to **satisfy** the stated prompt requirements and functional tests.
- One implementation intended to **violate only that specific requirement** while preserving all other functional and non-functional obligations.

The six sampled cases are:

#### Case 1: Task 506 (String Validity Checker)
- **Requirement Family:** Permitted or Prohibited Operations
- **Exact Requirement Quote:** `"2. Regular expressions are not allowed"`
- **Evaluator Logic:** `assert 'import re' not in code and 're.' not in code`
- **Satisfying Implementation:** Implements character checking via string methods (`c.isupper()`, `c.islower()`, `c.isdigit()`, `input_str.isalnum()`) without regular expressions.
- **Violating Implementation:** Implements validation using regular expressions invoked via `__import__('re').search(...)`.
- **Implementation Difference:** Invokes the Python regex engine while satisfying the 1-line constraint and variable naming rules.
- **Executable Witness:** AST contains `Call` node with `__import__('re')`.
- **Expected Verdict:** Satisfying $\to$ PASS; Violating $\to$ FAIL.
- **Observed Verdict:** Satisfying $\to$ PASS; Violating $\to$ **PASS** (Violating implementation accepted).
- **Failure Cause:** Naive substring checking fails to catch `__import__('re')` or aliased imports (`from re import match`). Furthermore, if a compliant implementation contains a comment with `re.` (e.g., `# Ensure.`), the validator falsely rejects compliant code.

#### Case 2: Task 588 (Binary String Group Converter)
- **Requirement Family:** Required Program Structure
- **Exact Requirement Quote:** `"1. Code must use list comprehension"`
- **Evaluator Logic:** `assert '[' in code and ']' in code, 'Must use list comprehension'`
- **Satisfying Implementation:** Maps 5-character binary slices to dictionary codes using `[rule_map.get(...) for idx in range(0, len(binary_str), 5)]`.
- **Violating Implementation:** Maps slices using `map(lambda idx: rule_map.get(...), range(0, len(binary_str), 5))` with 0 list comprehensions.
- **Implementation Difference:** Employs higher-order functional `map()` instead of list comprehension syntax; preserves 3-line limit, snake_case, and no-if requirements.
- **Executable Witness:** AST inspection confirms 0 `ast.ListComp` nodes exist.
- **Expected Verdict:** Satisfying $\to$ PASS; Violating $\to$ FAIL.
- **Observed Verdict:** Satisfying $\to$ FAIL (Functional Test); Violating $\to$ **PASS (Instruction Validator)** (Violating implementation accepted).
- **Failure Cause:** The validator asserts `'[' in code and ']' in code`; slice indexing `binary_str[idx:idx+5]` satisfies the bracket check, allowing code with zero list comprehensions to pass. Concurrently, ground-truth test case 4 in `check_correctness` expects a 7-character output (`'1010110'`) for a 25-character input, contradicting the prompt's mathematical rule that every 5 digits yield 2 digits (which requires 10 output characters).

#### Case 3: Task 518 (Local Minimum Finder)
- **Requirement Family:** Required Program Structure / Naming & Length Bounds
- **Exact Requirement Quote:** `"1. All variable and function names must be lowercase; 2. All variable and function names must be descriptive (no single letters); 3. The function must not exceed 15 lines of code"`
- **Evaluator Logic:** Validates lowercase variables, checks single-letter variables via regex `\b[a-z]\b`, and asserts line count $\le 15$.
- **Satisfying Implementation:** Implements local minimum search with lowercase, descriptive identifiers (`low_idx`, `high_idx`, `scan_idx`, `left_ok`, `right_ok`) in 11 lines.
- **Implementation Difference:** Fully satisfies verbatim prompt constraints; passes instruction check and functional unit tests ($V_{\text{instr}}=\text{PASS}, V_{\text{corr}}=\text{PASS}, V_{\text{comb}}=\text{PASS}$).
- **Executable Witness:** AST verification confirms line count $\le 15$ and all variable names have length $\ge 2$.
- **Expected Verdict:** Satisfying $\to$ PASS.
- **Observed Verdict:** Satisfying $\to$ PASS ($V_{\text{instr}}=\text{PASS}, V_{\text{corr}}=\text{PASS}, V_{\text{comb}}=\text{PASS}$).
- **Methodological Significance:** In earlier drafting, this task was erroneously cataloged as an algorithmic failure under the assumption that it required binary search and $O(\log n)$ complexity. Inspecting the verbatim prompt reveals that neither binary search nor logarithmic complexity is stated. Withdrawing this misclassification demonstrates the core RE principle: requirements conformance must be evaluated against verbatim stated requirements rather than unstated algorithmic assumptions. Task 518 is an instance of **Concordant Verification on Stated Constraints**.

#### Case 4: Task 546 (Increasing Subsequence Splitter)
- **Requirement Family:** Required Program Structure
- **Exact Requirement Quote:** `"2. No loop statements (for, while, etc.) allowed; 3. Must use list comprehension and at least two functions from filter/map/reduce"`
- **Evaluator Logic:** `assert not any(k in code.lower() for k in ['for', 'while'])` AND `assert '[' in code and 'for' in code and 'in' in code and ']' in code`
- **Probe with 'for':** `def split_sequences(nums): camelVar = [x for x in nums]` $\to$ raises `AssertionError: Explicit loop statements are not allowed`.
- **Probe without 'for':** `def split_sequences(nums): camelVar = list(filter(lambda x: x > 0, map(lambda x: x, nums)))` $\to$ raises `AssertionError: List comprehension is required`.
- **Executable Witness:** Mutual exclusion of assertions renders the validator's acceptance set mathematically empty: $L(V_{\text{instr}}) = \emptyset$.
- **Expected Verdict:** Satisfying $\to$ PASS; Violating $\to$ FAIL.
- **Observed Verdict:** Probe with 'for' $\to$ FAIL ($V_{\text{instr}}$); Probe without 'for' $\to$ FAIL ($V_{\text{instr}}$).
- **Failure Cause:** Structural contradiction in the benchmark validator. Check 2 bans the token `'for'` while Check 3 mandates the token `'for'`. No valid Python implementation can ever satisfy both checks.

#### Case 5: Task 564 (Duplicate Element Finder)
- **Requirement Family:** Required Program Structure / Identifier Bounds
- **Exact Requirement Quote:** `"4. All variable names must be longer than 5 characters; 1. entire function body can only have one line of code"`
- **Evaluator Logic:** `re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', code)` checked with `assert len(var) > 5 or var in ['for', 'in', 'if']`
- **Standard 'def' Probe:** `def find_duplicates(numbers): return [x for x in numbers]` $\to$ raises `AssertionError: Variable 'def' is too short`.
- **Lambda / Method Probe:** `find_duplicates = lambda numbers: [number_item for number_item in numbers if numbers.count(number_item) > 1]` $\to$ raises `AssertionError: Variable 'count' is too short`.
- **Executable Witness:** Regex matches language keywords (`def`, length 3) and standard methods (`count`, length 5), none of which are in the 3-word exemption list.
- **Expected Verdict:** Satisfying $\to$ PASS; Violating $\to$ FAIL.
- **Observed Verdict:** Standard 'def' $\to$ FAIL ($V_{\text{instr}}$); Lambda $\to$ FAIL ($V_{\text{instr}}$).
- **Failure Cause:** Unscoped token regex defect. The validator treats all lexical word tokens as variable names, causing keyword and method collisions that reject standard Python function syntax.

#### Case 6: Task 515 (Parity Array Partition)
- **Requirement Family:** Required Program Structure / Naming Prefix
- **Exact Requirement Quote:** `"3. Temporary variables inside the function must be prefixed with temp_"`
- **Evaluator Logic:** `re.findall(r'\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code)` checked with `assert all(var.startswith('temp_') or var in params for var in temp_vars)`
- **Satisfying Implementation:** Allocates comprehension variables with prefix: `temp_evens = [temp_x for temp_x in numbers if temp_x % 2 == 0]` $\to$ $V_{\text{instr}}=\text{PASS}, V_{\text{corr}}=\text{PASS}, V_{\text{comb}}=\text{PASS}$.
- **Violating Implementation:** Allocates comprehension variables without prefix: `return [unprefixed_x for unprefixed_x in numbers if unprefixed_x % 2 == 0] + ...` $\to$ $V_{\text{instr}}=\text{PASS}, V_{\text{corr}}=\text{PASS}, V_{\text{comb}}=\text{PASS}$.
- **Executable Witness:** AST confirms store-context variable names lacking `temp_` prefix bypass the regex because comprehension assignments use `in` rather than `=`.
- **Keyword-Argument Probe (False Rejection):** `def partition_array(numbers): temp_res = sorted(numbers, key = lambda temp_x: temp_x % 2 != 0); return temp_res` $\to$ raises `AssertionError: Temporary variables should have temp_ prefix` on `key =`.
- **Observed Verdict:** Satisfying $\to$ PASS; Violating $\to$ **PASS** ($V_{\text{instr}}$); Keyword-Arg Probe $\to$ **FAIL** ($V_{\text{instr}}$).
- **Defect Classification:** Instruction Oracle Permissiveness (False Acceptance of un-prefixed comprehension variables) and Keyword-Argument Brittleness (False Rejection on `key=`).

---

## 4. Execution Results and Empirical Findings

The empirical audit tool (`tools/benchmark_validator_audit.py`) executed all six sampled pairs directly against the released IFEvalCode evaluation harness. Table 2 summarizes the decoupled audit outcomes.

### Table 2: Decoupled Audit Outcomes across Sampled IFEvalCode Tasks ($N = 6$, Seed 2027)

| Task ID | Requirement Family | Stated Requirement Summary | Validator Strategy | Control / Probe | $V_{\text{instr}}$ | $V_{\text{corr}}$ | $V_{\text{comb}}$ | Defect Classification / Evidential Consequence |
|---|---|---|---|---|:---:|:---:|:---:|---|
| **506** | Permitted/Prohibited | Banned regular expressions | Substring check (`'import re' not in code`) | Satisfying<br>Violating | PASS<br>**PASS** | PASS<br>PASS | PASS<br>**PASS** | **Instruction False Acceptance:** `__import__('re')` bypasses check. (Comments with `re.` trigger false rejection). |
| **515** | Program Structure | Temporary variable `temp_` prefix | Assignment regex (`\s+\w+\s*=`) | Satisfying<br>Violating<br>Keyword-Arg | PASS<br>**PASS**<br>**FAIL** | PASS<br>PASS<br>PASS | PASS<br>**PASS**<br>**FAIL** | **Instruction False Acceptance:** Comprehension variables bypass regex.<br>**Keyword Brittleness:** `key=` triggers false rejection. |
| **588** | Program Structure | Required list comprehension | Bracket presence (`'[' in code and ']' in code`) | Satisfying<br>Violating | PASS<br>**PASS** | **FAIL\***<br>**FAIL\*** | **FAIL**<br>**FAIL** | **Instruction False Acceptance:** Slicing `s[i:i+5]` bypasses list comp check.<br>**Correctness Oracle Defect:\*** Ground truth expects 7 chars for 25 input digits (requires 10). |
| **546** | Program Structure | Ban loops but require list comp | Contradictory assertions (`not 'for'` AND `'for' in code`) | Probe w/ `for`<br>Probe w/o `for` | **FAIL**<br>**FAIL** | N/A<br>N/A | **FAIL**<br>**FAIL** | **Structural Contradiction:** Empty acceptance set ($L(V_{\text{instr}})=\emptyset$). Check 2 bans `'for'` while Check 3 mandates `'for'`. |
| **564** | Program Structure | Variable length $> 5$ chars | Token regex without keyword filtering | Standard `def`<br>Lambda probe | **FAIL**<br>**FAIL** | N/A<br>N/A | **FAIL**<br>**FAIL** | **Unscoped Token Regex Defect:** Regex matches keywords (`def`, len 3) and methods (`count`, len 5), rejecting all standard functions. |
| **518** | Program Structure / Naming | Lowercase, descriptive names, $\le 15$ lines | Checks lowercase, single-letter vars, line count $\le 15$ | Satisfying | PASS | PASS | PASS | **Concordant Verification on Stated Constraints:** Verbatim constraints verified; binary search was unstated. |

### Summary of Audit Findings ($N = 6$):
- **Tasks Exhibiting Instruction Oracle Permissiveness (False Acceptance):** 3 / 6 (Tasks 506, 515, 588)
- **Tasks Exhibiting Keyword-Argument Brittleness (False Rejection):** 1 / 6 (Task 515)
- **Tasks Exhibiting Structural Specification Contradictions:** 1 / 6 (Task 546, $L(V_{\text{instr}})=\emptyset$)
- **Tasks Exhibiting Unscoped Token Regex Collisions:** 1 / 6 (Task 564)
- **Tasks with Defective Ground-Truth Unit Tests:** 1 / 6 (Task 588)
- **Tasks Exhibiting Concordant Verification on Stated Constraints:** 1 / 6 (Task 518)

---

## 5. Traceability: Requirement Wording $\to$ Evaluator Behavior $\to$ Score Interpretation

The core Requirements Engineering contribution is not simply an inventory of bugs, but a formal trace from specification language to scoring validity:

```
[Requirement Wording]  ->  [Evaluator Implementation Strategy]  ->  [Permitted Score Interpretation]
"No regular expressions"     Substring search for 'import re'       Pass implies: code avoided exact string
                                                                    Does NOT imply: regex was not used.

"Variables length > 5"       Regex on all word tokens               Pass implies: impossible (def is 3 chars)
                                                                    Score is degenerate 0%.

"Must use list comp"         String search for '[' and ']'          Pass implies: code contained square brackets
                                                                    Does NOT imply: list comprehension used.

"Prefix temp variables"      Regex matching \s+\w+\s*=              Pass implies: avoided top-level assignments
                                                                    Does NOT imply: comprehension vars prefixed.

"Lowercase, descriptive      Checks lowercase, single-letter        Pass implies: naming and length constraints
 names, <= 15 lines"         regex, line count <= 15                concordantly satisfied.
```

Under Kane's validation framework, **Kane's Scoring Inference ($I_{\text{score}}$)** is a necessary pre-condition for requirements-driven model selection:
$$\neg\text{Sound}(V) \implies \text{Score Inadmissible}$$
However, validator soundness alone is not sufficient to guarantee operational adequacy ($\text{Sound}(V) \not\implies \text{Admissible}$), because a benchmark task may not align with deployment requirements ($I_{\text{extrap}}$) or safety cases ($I_{\text{dec}}$). When benchmark scores are ingested into an enterprise Requirements Traceability Matrix (RTM), accepting models based on un-audited benchmarks introduces false warrants of compliance into software supply chains.

---

## 6. Decision Gate Evaluation and Manuscript Transition Plan

### 6.1 Evaluation Against Decision Gate Criteria

| Decision Gate Criterion | Feasibility Evidence | Status |
|---|---|---|
| **1. Distinction from closest auditing studies** | Unlike EvalPlus/Ding et al. (fuzzing unchanged base tests) or MultiCodeIF/IFEvalCode (evaluating models assuming oracles are sound), we audit the released evaluators themselves against explicitly stated prompt requirements. | **PASSED** |
| **2. Reproducible cases with defended expected verdicts** | Six deterministic cases sampled under Seed 2027; expected verdicts verified via executable witnesses independent of the audited benchmark's verdict. | **PASSED** |
| **3. Recurring mismatch between wording and validation strategy** | Identified three systemic recurring patterns: (a) naive substring matching for semantic constraints, (b) total omission of algorithmic complexity checks, and (c) un-scoped regexes catching Python keywords. | **PASSED** |
| **4. Feasible sampling and reporting method** | Deterministic Seed 2027 protocol over eligible Python tasks; 4-state outcome categorization accommodating both correct and unresolved cases. | **PASSED** |

### 6.2 Manuscript Transition Plan for `paper2_preview.tex`

1. **Title:** **Do Code Benchmark Validators Enforce Their Stated Requirements? A Research Preview on Validator Fidelity and Evidential Deficits**
2. **Abstract:** Reframe as a Research Preview for REFSQ 2027:
   - Establish context: Foundation model procurement, benchmark pass rates as acceptance testing evidence ($W, E, O_{\text{bench}} \vdash_{\text{ind}} G_{\text{AI}}$), Kane's Scoring Inference ($I_{\text{score}}$).
   - Problem: Do released benchmark validators enforce explicitly stated constraints?
   - Principal results: Decoupled evaluation ($V_{\text{instr}}$, $V_{\text{corr}}$, $V_{\text{comb}}$); exploratory audit of 6 tasks across IFEvalCode; 3 tasks show instruction false acceptance (`__import__('re')`, list comp slicing bypass, comprehension variable regex bypass); 1 task has a structural validator contradiction ($L(V_{\text{instr}})=\emptyset$); 1 task has unscoped regex collisions on keywords (`def`); 1 task has a defective ground-truth testcase; 1 task demonstrates concordant verification on verbatim stated constraints.
   - Contributions: Audit methodology tracing requirement wording $\to$ evaluator behavior $\to$ score interpretation; artifact accessibility findings; programmatic witness assertions; roadmap and sampling frame for full-scale audit; implications for evidence reuse in AI assurance cases.
3. **Research Questions:**
   - **RQ1 (Traceability & Support):** Which stated requirements can be traced to checks in the released evaluator, and which remain ambiguous or unsupported?
   - **RQ2 (Validator Fidelity):** For selected requirements, does the evaluator accept violating implementations (false positives) or reject satisfying implementations (false negatives)?
   - **RQ3 (Score Interpretation & Evidential Warrants):** How do confirmed mismatches affect what a passing benchmark result can legitimately support under Kane's scoring inference?
4. **Methodology:**
   - Formalize unit of analysis as $u = (t, r, V)$.
   - Decoupled verdicts ($V_{\text{instr}}$, $V_{\text{corr}}$, $V_{\text{comb}}$).
   - Six distinct defect / outcome categories (Instruction False Acceptance, Instruction False Rejection / Brittleness, Structural Contradiction, Unscoped Token Regex Defect, Correctness Test Oracle Defect, Concordant Verification).
   - Position cases as an exploratory case series across requirement families; detail sampling frame (all 105 Python tasks in IFEvalCode) and stratification for the expanded study.
5. **Empirical Results:**
   - Table 2 with decoupled columns ($V_{\text{instr}}$, $V_{\text{corr}}$, $V_{\text{comb}}$).
   - Detailed analysis of Tasks 506, 515, 588, 546, 564, and 518 (withdrawing the binary search misclassification and explaining concordant verification).
6. **Discussion:**
   - Traceability table from requirement wording to permitted score interpretation.
   - Kane's validity framework: validator soundness is a necessary condition ($\neg\text{Sound}(V) \implies \text{Inadmissible}$), but not sufficient ($\text{Sound}(V) \not\implies \text{Admissible}$).
   - Disclose assistant's role in case construction and analysis.
7. **Verification:**
   - Run `python3 verify_manuscripts.py`.
   - Do NOT compile LaTeX or open automatic PDF previews. Layout and page length reported as unchecked.

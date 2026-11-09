# Target Project Repository Selection & Task Eligibility

**Study Target:** Using AI Benchmark Results as Requirements Evidence  
**Protocol Phase:** Phase 2 — Artifact Feasibility & Inventory  

---

## 1. Selected Repositories Overview

We selected three mature, open-source Python repositories represented in the SWE-bench benchmark ecosystem. Projects were ranked by:
1. The volume of candidate pull requests / resolved issues with deterministic unit test coverage;
2. Clean separation of test dependencies (zero required Docker daemons, external cloud credentials, or native C-compiler toolchains);
3. Alphabetical repository name among eligible candidates.

| Project | Organization / Repository | Primary Domain | Test Framework | Base Feasibility Score | Selected Target Issue Sample Size |
|---|---|---|---|---|---|
| **P1: Requests** | `psf/requests` | HTTP networking library | `pytest` + `pytest-mock` | High (pure Python, fast mocks) | $N = 30$ |
| **P2: Flask** | `pallets/flask` | Web WSGI microframework | `pytest` | High (standard library dependent) | $N = 30$ |
| **P3: SymPy** | `sympy/sympy` | Symbolic mathematics engine | `sympy.testing` / `pytest` | High (pure Python, rich issue logs) | $N = 30$ |

Total target project workload: **90 target issues** ($30 \times 3$).

*Note on Task Scaffolding:* The 90 entries in `paper2/records/target_workloads.json` define the **prospective sampling frame specification schema** for these repositories (allocating 30 candidate slots per project with requirements and step ceilings). Live candidate task extraction, commit-level provenance, and automated eligibility pre-checks will precede prospective target model execution in accordance with the frozen 6-stage protocol.

---

## 2. Strict Task Eligibility Criteria

For each target issue, the following six eligibility conditions must be verified before inclusion into the target evaluation workload:

1. **Checkable by Execution:** The issue specification describes a concrete defect or behavioral requirement checkable via an executable test assertion (e.g., `assert response.status_code == 200` or `assert simplify(expr) == expected`).
2. **Recoverable Repository State:** The repository can be checked out cleanly at the exact commit immediately preceding the maintainer's bug-fix pull request (`git checkout <base_commit>`).
3. **Paired Maintainer Fix & Test Oracles:** The repository commit history provides:
   - A maintainer fix patch ($\Delta_{\text{fix}}$);
   - A maintainer test patch ($\Delta_{\text{test}}$) containing new or updated test cases that fail on the base commit ($V(\text{base}, \Delta_{\text{test}}) = \text{FAIL}$) and pass on the fixed commit ($V(\text{base} \oplus \Delta_{\text{fix}}, \Delta_{\text{test}}) = \text{PASS}$).
4. **Strict Split Separation (Absence from Source Benchmark Sets):** The issue ID and pull request number must be strictly absent from the source benchmark evaluation sets (SWE-bench Lite and SWE-bench Verified task registries).
5. **Tool & Limit Compatibility:** The task must be resolvable using standard file search and text editing tools within a 30-step interaction budget and 128k context window.
6. **Zero External Dependencies / Isolation:** The task execution environment must not require network connectivity, API access tokens, live HTTP endpoints, or non-Python system daemons. All network interactions must be mocked in-memory.

---

## 3. Contamination Analysis & Timeline Exposure Risk

To transparently document contamination and data exposure risks without making unverifiable claims of "purely uncontaminated" data:

- **SWE-bench Base Cutoff:** August 2023.
- **Model Training Data Cutoffs:**
  - Claude Sonnet 5.5: Q2 2025 – Q1 2026.
  - GPT-6.1 Luna / Sol: Mid-2025 – Early 2026.
  - Gemini 3.8 Flash High: Late 2025 – Mid 2026.
- **Target Issue Sampling Windows:**
  - Selected target issues span both pre-cutoff and post-cutoff GitHub pull requests.
  - For pre-cutoff issues, we document that models may have observed repository source files during pre-training, but note that resolving a specific bug from an open issue still requires navigating the repository state and synthesizing a localized patch.
  - We record issue submission timestamps and pull request merge dates for all 90 tasks in `paper2/records/target_workloads.json`.
  - In our Threats to Validity (Section 6), we explicitly analyze contamination sensitivity rather than assuming zero exposure.

---

## 4. Containerless Virtual Environment Feasibility

SWE-bench historically provides Docker images for each repository environment. However, running a Docker daemon is often impractical or prohibited in locked CI/CD runners or user workstations.

We verified that all three selected repositories (`requests`, `flask`, `sympy`) can be executed inside **isolated Python virtual environments (`venv`)** directly in the host OS:
1. `requests`: Requires `pytest`, `urllib3`, `certifi`, `idna`, `charset-normalizer`. Installs and runs in $<15$ seconds.
2. `flask`: Requires `pytest`, `werkzeug`, `click`, `itsdangerous`, `jinja2`. Installs and runs in $<20$ seconds.
3. `sympy`: Pure Python symbolic mathematics library with zero external runtime dependencies. Runs directly with `pytest sympy/core` in $<30$ seconds.

This confirms the feasibility of executing acceptance tests and patch verification in local git worktrees without requiring Docker daemon virtualization.

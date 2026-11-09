# Repository readiness — protocol 3 draft

Status: BLOCKED. No provider calls were made. Verified eligibility counts appear below; pending tasks have not been evaluated.
The source inventory is metadata, not an executable sample. Pending tasks are not exclusions.

| Repository | Candidates | Verified eligible | Source attempts if all eligible |
| --- | ---: | ---: | ---: |
| sympy/sympy | 75 | 0 | 300 |
| django/django | 231 | 0 | 924 |
| sphinx-doc/sphinx | 44 | 0 | 176 |

The attempt column is a candidate ceiling (two configurations, two repetitions), not a budget or frozen sample. Target counts and total main attempts remain undefined. Use the verified sample size for precision planning. sample_planning.json reports illustrative binomial probabilities at candidate counts and at the verified sample size; these are assumptions, not performance estimates.

## Blockers

- Retrieve reference patches, test artifacts, environment specifications, and executable checkouts at pinned commits. Environment failures are unmeasured, not zero. Upstream acquisition plan: 350 candidate instances require container base images (Python 3.9/3.10/3.11) with pinned dependencies (wheel caches) mapped to SWE-bench Verified commit hashes.
- Candidate target tasks: Sixty post-cutoff candidate tasks (20 SymPy, 20 Django, 20 Sphinx) selected in target_candidates.json with verified syntactic overlap checks (21,000 pairwise comparisons returning zero overlap); semantic description review and local checkouts remain pending.
- Evidential review records for C05, C07, C12, C14, and C28 recorded in review_records.json with detection limits. Dual evaluation on C14 distinguishes closed proprietary models (Documented/unresolved) from open-weight models (Verified with auditable pre-training disclosures), demonstrating Missing Evidence Neutrality.
- Runtime model identities, multi-turn step ceilings (S <= 30), timeouts (<= 900s), and token usage accounting empirically verified across CONFIG_01 (Gemini 3.8 Flash Medium) and CONFIG_02 (GPT-6.1 Sol Light) in paper2/pilot/adapter_validation_results.json. Telemetry note: CONFIG_02 parses dynamic per-run event streams from Codex CLI; CONFIG_01 logs Antigravity ACI subagent session accounting envelopes.
- Establish an OS or container boundary (Docker or Podman with --network none and read-only root mounts) denying agents access to evaluation oracles and reference fixes. Container invocation generator and boundary verifier (verify_container_boundary) are implemented; container daemon deployment remains pending.
- Pilot manifest unblocked (status: prepared_not_executed): 6 candidate tasks verified eligible (2 SymPy, 2 Django, 2 Sphinx) across controlled synthetic micro-repository fixtures in paper2/preparation/checkouts/, 12 planned attempts. These micro-repository checkouts validate harness plumbing, oracle isolation, and patch application offline, while full upstream build trees remain prospective. Live execution requires explicit pilot authorization.
- Costs and usage ceilings remain unknown until an authorized repository pilot. Main execution is disabled.

## Offline checks

Use `python3 -m unittest discover -s paper2/tests` for controlled fixture tests. These are software checks, not repository feasibility evidence. Use `python3 -m paper2.preparation.repository_runner prepare` to regenerate the metadata inventory. The execution command refuses provider calls. Eligibility accepts an explicit local task specification and writes a new result without overwriting prior attempts.

## Freeze sequence

Eligibility and audit records → repository pilot (separate authorization) → cost and sample review → protocol, tasks and policy freeze → source runs → locked source verdicts → target runs → paired case reporting. No threshold, policy, repository, or configuration substitution based on observed performance.

## Latest eligibility checks

6 specifications checked; 6 eligible. Each result is preserved under eligibility/.

- pilot__sympy-01: eligible; baseline and reference checks passed
- pilot__sympy-02: eligible; baseline and reference checks passed
- pilot__django-01: eligible; baseline and reference checks passed
- pilot__django-02: eligible; baseline and reference checks passed
- pilot__sphinx-01: eligible; baseline and reference checks passed
- pilot__sphinx-02: eligible; baseline and reference checks passed

## Binomial planning assumptions

| Repository | Candidate n | Unresolved at p=.65 | Unresolved at p=.75 | Unresolved at p=.85 |
| --- | ---: | ---: | ---: | ---: |
| sympy/sympy | 75 | 0.8466 | 0.8717 | 0.1469 |
| django/django | 231 | 0.5924 | 0.6294 | 0.0002 |
| sphinx-doc/sphinx | 44 | 0.8967 | 0.8894 | 0.3366 |

Candidate probabilities assume every candidate is eligible and sampled; they do not authorize this sample size.

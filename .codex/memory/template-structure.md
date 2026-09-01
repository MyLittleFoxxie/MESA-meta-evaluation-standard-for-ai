# MESA Template Structure Reference (v2)

This file mirrors the current structure of `MESA EFPA template official.md` (repo root) as a
condensed heading map with one-line descriptions, so a reviewer agent (or anyone drafting/auditing
a review) can quickly confirm what a complete review needs without re-reading or re-deriving the
full ~2,600-line template every time.

**Keep this in sync with the template.** If `MESA EFPA template official.md` changes (headings
added, removed, renamed, or reordered), regenerate this file from the template in the same change.
This file is descriptive of the template, not a second source of truth — when in doubt, the
template wins. **This mirror is the declared name authority for section names:** the template
Summary of Ratings rows, the paper's Tables II-III, and the README section list are regenerated
from the headings recorded here.

Numbering is exact and load-bearing: reviews cite items by number (e.g. "6.1.9"), and MESA's own
tooling (the site's PDF export, the review-heading-consistency checks) depends on numbered headings
matching the template verbatim. Do not paraphrase a numbered heading when writing a review — copy it
exactly as it appears in the template.

**v2 migration note (retire, don't renumber).** Template v2 (2026-08) merged four items; the
absorbed IDs are retired with tombstones in the template and must not be used in new reviews:
2.6 → merged into 2.9; 4.10 → merged into 2.4; 10.6.2 → merged into 10.6.1; 11.3.2 → merged into
11.3.1. No surviving item changed its number. Reviews produced against v1 (89 rated items) are frozen as dated evidence; see `feedback/95-mesa-core-plan.md` Part 3 for the v1→v2
mapping.

## Part A vs. Part B — the boundary that must never blur

- **Part A (General Description, Source Inventory, Sections 1-5) is descriptive only.** Record
  facts, sources, and evidence gaps. No ratings, no quality judgments, no "this is good/bad"
  language.
- **Part B (Sections 6-12 + Final Evaluation) is evaluative.** Every numbered Part B item gets an
  EFPA-style rating (`n/a` or `0`-`4`), each with evidence, missing evidence, reviewer rationale, and
  an interpretation caution. To assign `1`-`3`, apply the Rating Scale meanings to the item's
  Excellent anchor (`2` = core function met with stated limitations; `1` = not met; `3` = met with
  minor gaps). Do not mechanically average ratings — every "Overall ..." roll-up item is explicit
  reviewer judgment across its sub-items, not an arithmetic mean.
- Missing documentation is an **evidence gap**, not automatic proof the benchmark is poor.
- A benchmark with one or more `0`/`1` ratings on attributes critical to its stated use falls
  below the minimum standard for that use; the Final Evaluation must say so, and critical-attribute
  ratings are marked in **bold** in the completed review.

---

## Front Matter

- **Introduction** — states MESA's purpose: a structured description/evaluation model treating AI
  benchmarks as measurement instruments, adapting the EFPA Test Review Model 2025 [4] and the AERA
  Standards test definition [6]. Contains the canonical reviewed-entity list: original benchmark,
  derived benchmark, subset, evaluation slice, hosted leaderboard, private form, rolling cohort,
  suite component, task environment, evaluator-specific implementation.
- **How the MESA Model Should Be Used** — usage guidance: keep Part A descriptive and Part B
  evaluative, treat missing documentation as an evidence gap, don't inherit ratings from a parent
  benchmark, prefer authoritative sources over independent commentary.
- **Glossary** — ten entries: capability domain, claim proportionality, construct validity,
  construct-irrelevant variance, evidence gap, gameability, model-as-judge, reference
  interpretation, run conditions, supported-use / non-use statement.
- **Figure 1** — structure of the MESA Test Review Model (General Description standalone box,
  Part A sections 1-5, Part B sections 6-12, Final Evaluation).

## Part A. Description of the Benchmark — *descriptive, no ratings*

### General Description of the Benchmark
Short stand-alone non-evaluative description (200-400 words): what the benchmark is, what it
claims to measure, task and score structure, reference points, intended users, versions/forms,
unusual features or history. Formerly Appendix A; this is the "short stand-alone description" box
in Figure 1. (Free text.)

### Source Inventory
Table of every source consulted (Source ID, source citation/URL, access date, what it was used
for). Formerly a house convention in completed reviews; now a template section.

### Section 1. Factual Description
Identifies the review event, the exact reviewed entity, and the materials inspected.

- **1.1 Review Administration** — reviewer name, date of current review, date of previous review.
- **1.2 Benchmark Identity & Provenance** — reviewed entity name, short name, entity type (closed vocabulary from the canonical list), parent/source benchmark, version/split, implementation/scorer version, creators/maintainers, host organization, release dates, license, persistent identifier.
- **1.3 Materials, Sources, & Access Tracking** — inventory of paper, website, code repo, dataset, harness, leaderboard, guides, changelog, announcements, contextual literature, and contact channels, each with a URL/location and access date.

### Section 2. Classification
Classifies the benchmark's intended measurement domain, target AI systems, users, task structure, and administration conditions. Introduces the ten CHC-inspired capability domains (K, RW, M, R, WM, MS, MR, V, A, S).

- **2.1 Claimed Capability Domains** — at most three primary domains (CHC layer + applied labels with a combination rule), plus the "Claimed construct in the benchmark's own words" fill-in table (construct, definition, subcomponents, excluded scope).
- **2.2 Area of Use** — documented use contexts (model comparison, leaderboard ranking, safety evaluation, procurement, policy analysis, etc.).
- **2.3 Intended AI Systems** — which system classes the benchmark targets.
- **2.4 Intended Users and Recipients of Benchmark Outputs** — who consumes results, plus per-recipient-class interpretive-competence table. Absorbs the retired 4.10.
- **2.5 Task Families, Subdomains, and Splits** — unit families, unit sources, unit sampling, unit selection/filtering, splits, primary score name (definitions live in 3.2; construct rows moved to 2.1).
- **2.6** — *retired; merged into 2.9.*
- **2.7 Prerequisites for Evaluated Systems** — what a system must have to participate, marked irrelevant/necessary/missing.
- **2.8 Evaluation Conditions** — run conditions: prompting protocol, system prompt, sampling settings, runs policy (pass@k), tool permissions, time limits, human-intervention rules, hardware, etc.
- **2.9 Task Interaction, Response Types, and Observable Evidence** — task interaction pattern, response formats (absorbs the retired 2.6), and observable process data; four checkbox groups, each with an "Other" escape.
- **2.10 Input Stimulus Type** — kinds of input presented.
- **2.11 Number of Items or Measurement Points** — five core rows always, breakdown rows only where documented; item counts and count uncertainty.
- **2.12 Mode of Evaluation** — venue / openness and submission route / cadence and interaction groups, plus the identity-and-condition-control spectrum with per-level definitions.
- **2.13 Technological Arrangements** — available (A) vs. required (R) technology matrix.
- **2.14 Time and Resource Requirements** — documented estimates only; mark missing if not stated.
- **2.15 Benchmark Forms, Versions, and Variants** — forms/variants with stated score-comparability, multi-row.
- **2.16 Static or Dynamic Task Determination** — static/sampled/generated/adaptive/rolling task determination.
- **2.17 Evidence Sources Used in Scoring** — only evidence the scoring procedure consumes (2.9 records what the evaluation generates).
- **2.18 Broad-Claim Flags for Later Evaluation** — descriptive screen for AGI/general-intelligence/agency-style claims (a claim of "reasoning" alone does not count): term used, breadth/depth implied, capability-domain coverage/exclusions, caveats to carry into Part B.

### Section 3. Measurement and Scoring
Describes how model behavior becomes a score, separating scoring *procedure* from *scores*.

- **3.1 Scoring Procedure** — scoring method classes grouped as answer matching / execution or environment verification / judge-based or human scoring / preference, ranking, or platform. Distinguishes LLM equality-checker (answer-match only) from LLM judge (rubric-rated quality).
- **3.2 Scores and Metrics** — the single home for score definitions: primary/subscores/derived scores/qualitative bands table, the parsing/extraction step, and treatment of missing/refused/failed responses and run failures.
- **3.3 Scale or Metric Types** — the metric family used.
- **3.4 Score Transformation** — linear/non-linear transformation, weighting, plus combining-formula documentation status prompt.
- **3.5 Documented Reference Groups, Baselines, and Comparators** — single fill-in table of reference points (chance, human, expert, contest population, model cohort, commercial/open-weight system, domain group, split contrast, prior version, boundary), each with construction method and intended interpretation.
- **3.6 Score Uncertainty and Stability** — descriptive record of reported uncertainty estimates and stability evidence.
- **3.7 Documented Metric Rationale and Stated Score Interpretation** — metric rationale, floor/ceiling limits, score effects from outside the target capability, scorer validation, sensitivity, non-use statements (domain-linkage rows live in 3.2).

### Section 4. Benchmark Outputs and Reports
Adapts EFPA's "digitally generated reports" to AI benchmark outputs. Intended recipients are recorded in 2.4.

- **4.1 Output Availability** — what's publicly available.
- **4.2 Output Name or Description** — per-output inventory table (three rows; complete 4.2-4.9 per output, or state which single output is described).
- **4.3 Output Design or Presentation** — presentation format.
- **4.4 Output Structure** — organizing principle, eight defined options.
- **4.5 Sensitivity to Context** — fixed vs. user-definable vs. audience-adapted output.
- **4.6 Development of Outputs** — how report content was produced.
- **4.7 Modifiability** — whether outputs can be modified.
- **4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels** — clear / mixed / black box / no documentation.
- **4.9 Output Content** — what the output contains.
- **4.10** — *retired; merged into 2.4.*

### Section 5. Benchmark Access, Materials, and Lifecycle
Records distribution, access, reproduction, and maintenance — informed by BetterBench [3].

- **5.1 Supporting Documentation Provided to Users** — documentation artifacts (technical report, user guide, README, API docs, dataset card, scoring docs, rubric, FAQ, changelog). *(Retitled in v2; formerly shared 5.2's heading.)*
- **5.2 Distribution and Access Model** — the access model (fully public, hidden answer keys, controlled-access, private evaluation service, leaderboard-only, etc.).
- **5.3 Methods of Publication** — publication channels used.
- **5.4 User Requirements or Qualifications** — requirements to run/submit/interpret/maintain; write "none (stated)" vs. "not documented", never blank.
- **5.5 Dataset and Item Access** — public/restricted/hidden/unavailable status matrix.
- **5.6 Provenance and Contamination Documentation** — item *integrity* (origin, exposure, leaks): provenance, release timing, dedup checks, prior-exposure screening, canaries, leak response, hash commitments, disclosure reporting.
- **5.7 Reproducibility Materials** — replication assets (task data, prompts, scoring code, pinned environment, seeds, replication script, fixtures, CI signal).
- **5.8 Maintenance and Versioning** — *operations* (who maintains what, versioning, comparability): maintainer/owner/operator identities, rerun and stale-score policies, item rotation, deprecation/archival/retired-item policy, score comparability across versions/cohorts/refreshes, archival plan.

*(Appendix A no longer exists; its content moved to the General Description at the head of Part A.)*

---

## Part B front matter (boilerplate — copy verbatim into every full review, not benchmark-specific)

- **Information Sources** — what may inform Part B: official materials, public benchmark materials, academic/critique literature (context only), maintainer-provided material (disclose if a rating depends on it), and confidential information including tuning data for model-based scorers, which should be sought where another model scores responses.
- **Explanation of Ratings** — the `n/a`/`0`-`4` scale; the `1`-`3` interpolation rule against each item's Excellent anchor; the below-minimum-standard verdict rule with bold-marking of critical ratings; the claims pipeline (2.18 collects → 10.6 rates proportionality → 11.5 rates use guidance → 12.3-12.4 rate communication).
- **Rating Scale** — `n/a` not applicable; `0` no/insufficient info; `1` inadequate; `2` adequate for cautious use; `3` good, minor gaps; `4` excellent/comprehensive.
- **General Guidance on Assigning Ratings** — adequacy is relative to the intended score meaning; broad claims require stronger breadth/validity evidence.

## Part B. Evaluation of the Benchmark — *evaluative, every numbered item rated `n/a`/`0`-`4`*

### Section 6. Rationale, Development, Documentation, and Task/Item Quality
Whether the benchmark defines the real capability of interest, justifies its tasks/scoring, documents development, and gives users enough procedural information. Revisit checkpoint lives in the Final Evaluation.

- **6.1 Rationale and Development**
  - **6.1.1 Rationale and construct definition** — is the target capability clearly defined, bounded, and distinguished from broader interpretations?
  - **6.1.2 Summary of prior research and benchmark context** — does documentation situate the benchmark and state what gap it fills?
  - **6.1.3 Phenomenon-task-metric-claim chain** — is the real capability explicitly linked through task design, scoring rule, and intended score meaning (confounds as supporting analysis)?
  - **6.1.4 Task or item design** — are task formats, difficulty range, and scoring protocol justified?
  - **6.1.5 Procedures for developing task or item content** — expert-informed content development with clear criteria?
  - **6.1.6 Thoroughness of the final task or item selection process** — defensible sampling strategy and coverage analysis?
  - **6.1.7 Quantitative evidence of task or item quality** — difficulty, discrimination, redundancy, etc.; `n/a` only for non-item-based benchmarks, else absence is `0`.
  - **6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice** — documented adaptation process with equivalence checks.
  - **6.1.9 Overall Rationale, development, and task or item quality** — roll-up of 6.1.1-6.1.8.
- **6.2 Adequacy of Documentation Available to Users**
  - **6.2.1 Documentation of benchmark purpose and intended use**.
  - **6.2.2 Documentation of development process**.
  - **6.2.3 Documentation of scoring and metrics** — parsing, scoring rules, aggregation, failure handling documented?
  - **6.2.4 Documentation of reliability, stability, and uncertainty** — stability/variance/uncertainty assessment documented?
  - **6.2.5 Documentation of validity evidence**.
  - **6.2.6 Documentation of fair use and comparability** — existence/usability of fair-use docs (11.1.2 rates substantive adequacy).
  - **6.2.7 Documentation of maintenance and versioning** — version history, release/refresh policy, comparability guidance (rest is supporting detail).
  - **6.2.8 Adequacy of documentation available to users** — roll-up of 6.2.1-6.2.7.
- **6.3 Quality of Procedural Instructions**
  - **6.3.1 Evaluation setup and administration** — complete, reproducible setup instructions (core: environment/dependencies, credentials, compute, sampling/seeds, failure handling).
  - **6.3.2 Scoring procedure and error handling**.
  - **6.3.3 Interpretation and reporting guidance**.
  - **6.3.4 Restrictions, prerequisites, and appropriate use**.
  - **6.3.5 Technical support and implementation guidance**.
  - **6.3.6 References and supporting materials**.
  - **6.3.7 Quality of procedural instructions** — roll-up of 6.3.1-6.3.6.
- **6.4 Overall Adequacy of Rationale and Documentation** — roll-up across 6.1-6.3.

### Section 7. Quality and Usability of Benchmark Materials
Whether datasets, prompts, rubrics, scoring code, harnesses, and interfaces are complete and usable to inspect/run/score/reproduce/audit.

- **7.1 Quality of Benchmark Materials**
  - **7.1.1 Dataset, task set, or evaluation environment availability**.
  - **7.1.2 Prompts, instructions, and input materials**.
  - **7.1.3 Rubrics, reference answers, and response format requirements**.
  - **7.1.4 Evaluation harness, scorer, and implementation quality**.
  - **7.1.5 Interface and workflow usability**.
  - **7.1.6 Accessibility across modalities, languages, and system types** — evaluated-system coverage plus human-operator workflow.
  - **7.1.7 Licensing, use requirements, and risk warnings**.
  - **7.1.8 Overall quality of benchmark materials** — roll-up of 7.1.1-7.1.7.

### Section 8. Baselines, Comparators, and Reference Interpretation
Reference points used to make scores interpretable — chance floors, human/expert performance, model cohorts, prior versions, score bands. Rate the weakest anchor the intended interpretation depends on when families diverge.

- **8.1 Baseline and Comparator Interpretation**
  - **8.1.1 Random, chance, floor, and ceiling baselines**.
  - **8.1.2 Human or expert baselines** — sampling/qualification, condition comparability, uncertainty; domain coverage escalates when human-level claims are made.
  - **8.1.3 Model comparator cohort** — identity/version/date, access mode, run conditions, uncertainty.
  - **8.1.4 Historical, version, or benchmark-family comparators**.
  - **8.1.5 Criterion thresholds, score bands, or performance categories**.
  - **8.1.6 Representativeness of reference groups**.
  - **8.1.7 Currency and maintenance of baseline evidence**.
- **8.2 Overall Adequacy of Baselines and Reference Interpretation** — roll-up across 8.1; absence of any reference point is rated here via `0`/`1` semantics.

### Section 9. Reliability, Precision, and Score Stability
Whether scores are stable enough for their intended use across runs, prompts, seeds, forms, raters, judges, and versions.

- **9.1 Data Provided About Reliability, Precision, and Stability**
  - **9.1.1 Coverage of reliability and stability evidence** — the inventory: does evidence exist for each material source of variation (per 9.2-9.5), with missing sources explicitly stated?
- **9.2 Run-to-Run Stability and Uncertainty**
  - **9.2.1 Run-to-run stability, seeds, and sampling settings**.
  - **9.2.2 Score uncertainty, confidence intervals, or standard errors**.
- **9.3 Scorer, Judge, Parser, and Rater Reliability**
  - **9.3.1 Automated scorer or parser reliability**.
  - **9.3.2 Human rater or expert scorer agreement**.
  - **9.3.3 Model-as-judge reliability and validity checks**.
- **9.4 Form, Version, Prompt, and Environment Stability**
  - **9.4.1 Prompt, instruction, or formatting sensitivity**.
  - **9.4.2 Form, split, version, or refresh equivalence**.
  - **9.4.3 Execution environment and dependency stability**.
- **9.5 Statistical Comparison Quality**
  - **9.5.1 Meaningfulness of score differences** — statistically justified guidance on when differences are meaningful; distinguish statistical significance, practical significance, and leaderboard convenience.
- **9.6 Overall Reliability, Precision, and Score Stability** — roll-up across 9.1-9.5.

### Section 10. Validity Evidence
The construct-validity chain: real capability → task → metric → claim. Uses Bean et al.'s *Measuring what Matters* [2] as the primary source; BetterBench [3] informs contamination/gameability.

- **10.1 Validity Evidence Based on Benchmark Content**
  - **10.1.1 Content validity and task representativeness** — coverage analysis matching the claimed capability space, documented exclusions, limits on generalization.
  - **10.1.2 Construct breadth and capability-domain coverage**.
- **10.2 Validity Evidence Based on Internal Structure**
  - **10.2.1 Internal structure, subscores, or dimensionality**.
  - **10.2.2 Item or task behavior across the score scale**.
  - **10.2.3 Failure modes and error analysis**.
- **10.3 Validity Evidence Based on Metrics and Scoring**
  - **10.3.1 Metric, scorer, and aggregation validity** — the scoring pathway rewards the intended capability, not formatting/parser strictness/prior exposure; judge validation is required for a rating above `2` where another model scores responses.
  - **10.3.2 Sensitivity to shortcuts and construct-irrelevant variance**.
- **10.4 Validity Evidence Based on Relations to Other Variables**
  - **10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings**.
  - **10.4.2 Convergent and discriminant evidence**.
  - **10.4.3 Ecological or predictive relevance**.
- **10.5 Contamination, Leakage, and Gameability**
  - **10.5.1 Contamination and leakage controls** — two-tier anchor; the stronger evidence is required rather than optional where the benchmark uses private, hidden, or rolling forms.
  - **10.5.2 Gameability and benchmark-specific tuning controls**.
- **10.6 Claim Proportionality**
  - **10.6.1 Proportionality of score interpretations** — score interpretations bounded by evidence; the broad-claims condition (evidence across relevant capability domains, or explicit rejection/limits) is required rather than optional where broad claims are made. *(Absorbs the retired 10.6.2.)*
- **10.7 Overall Validity Support** — roll-up across 10.1-10.6.

### Section 11. Fair Use, Comparability, and Appropriate Use
Whether the benchmark can be used and compared fairly across relevant systems, modalities, languages, and contexts — broader than demographic fairness alone. Cross-reference table (not a figure) lists related ratings per sub-section.

- **11.1 Rationale and Documentation for Fair Use**
  - **11.1.1 Relevance of the construct across systems, groups, and contexts**.
  - **11.1.2 Documentation of fair-use considerations** — substantive adequacy of documented fairness considerations (6.2.6 rates existence/usability).
- **11.2 Development, Design, and Accessibility**
  - **11.2.1 Inclusive and accessible benchmark design**.
  - **11.2.2 Domain, language, modality, and subgroup coverage**.
- **11.3 Cross-System and Evaluation-Condition Comparability**
  - **11.3.1 Cross-system and access-condition comparability** — run conditions and access constraints documented and managed for undistorted comparison; condition labels or separate cohorts where differences matter. *(Absorbs the retired 11.3.2.)*
  - **11.3.3 Temporal comparability for rolling or live benchmarks**.
- **11.4 Evidence for Fairness and Bias**
  - **11.4.1 Differential performance or bias analysis**.
  - **11.4.2 Reliability and validity across relevant subgroups or contexts**.
- **11.5 Appropriate Use and Restrictions**
  - **11.5.1 Appropriate-use guidance and non-use cases**.
  - **11.5.2 Release rules and sensitive-content handling**.
- **11.6 Overall Fair Use, Comparability, and Appropriate Use** — roll-up across 11.1-11.5.

### Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims
Whether reporting surfaces make clear what a score means, under what run conditions, with what uncertainty. Informed by BetterBench [3] and The Leaderboard Illusion [5]. Rate each item against the most consequential public surface; note materially divergent surfaces in that item's Reviewer comments (per-item comment fields exist at 12.2.1 and 12.4.3).

- **12.1 Scope and Coverage**
  - **12.1.1 Report, leaderboard, dashboard, or reporting-material scope**.
  - **12.1.2 Score granularity and level of detail**.
- **12.2 Reliability and Traceability of Reports**
  - **12.2.1 Uncertainty, version labeling, and evaluation-condition labeling** — version, date, cohort label, run conditions, uncertainty, cross-date comparability.
  - **12.2.2 Reproducibility and traceability of reported scores**.
- **12.3 Relevance and Validity of Reports**
  - **12.3.1 Linkage from scores to interpretations and public claims**.
  - **12.3.2 Raw outputs, per-item data, or trace availability**.
- **12.4 Fairness, Acceptability, and Public Communication**
  - **12.4.1 Fairness and freedom from bias in reports**.
  - **12.4.2 Acceptability and usability for intended audiences**.
  - **12.4.3 Public communication and leaderboard governance**.
- **12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims** — roll-up across 12.1-12.4.

## Final Evaluation

- **Evaluative Report of the Benchmark** — free-text overall judgment. Must state explicitly: (1) the interpretations the scores support; (2) the interpretations they do not support; (3) the run conditions that must be held fixed for comparisons to be meaningful. Must apply the below-minimum-standard rule for `0`/`1` on critical attributes, and re-check 6.1.1, 6.1.3, and 6.2.5 against Section 8-10 findings before concluding. (Free text.)
- **Conclusions** — one-to-two-sentence summary of quality, supported use(s), and the expertise level needed. (Free text.)
- **Recommendations** — what users/maintainers/future reviewers should do next, tied to findings. (Free text.)
- **Summary of Ratings** — table with the overall rating (`n/a`/`0`-`4`) for Sections 6-12, using the section headings verbatim.
- **Gap Register** — multi-row table of missing/inaccessible evidence: what's missing, affected entity/surface, affected interpretation, affected rating(s), why it matters, and what's needed for a higher rating.

## Bibliography
Numbered citation list: [1] Hendrycks et al., *A Definition of AGI*; [2] Bean et al., *Measuring what Matters*; [3] Reuel et al., *BetterBench*; [4] EFPA, *EFPA Test Review Model — Version 2025*; [5] Singh et al., *The Leaderboard Illusion*; [6] AERA/APA/NCME, *Standards for Educational and Psychological Testing* — cited via `[n]` markers in the front matter and Sections 2, 5, 6, 7, 9, 10, 12.

# MESA Template Structure Reference

This file mirrors the current structure of `MESA EFPA template official.md` (repo root) as a
condensed heading map with one-line descriptions, so a reviewer agent (or anyone drafting/auditing
a review) can quickly confirm what a complete review needs without re-reading or re-deriving the
full ~2,500-line template every time.

**Keep this in sync with the template.** If `MESA EFPA template official.md` changes (headings
added, removed, renamed, or reordered), update this file to match in the same change. This file is
descriptive of the template, not a second source of truth — when in doubt, the template wins.

Numbering is exact and load-bearing: reviews cite items by number (e.g. "6.1.9"), and MESA's own
tooling (the site's PDF export, the review-heading-consistency checks) depends on numbered headings
matching the template verbatim. Do not paraphrase a numbered heading when writing a review — copy it
exactly as it appears in the template.

## Part A vs. Part B — the boundary that must never blur

- **Part A (Sections 1-5 + Appendix A) is descriptive only.** Record facts, sources, and evidence
  gaps. No ratings, no quality judgments, no "this is good/bad" language.
- **Part B (Sections 6-12 + Final Evaluation) is evaluative.** Every numbered Part B item gets an
  EFPA-style rating (`n/a` or `0`-`4`), each with evidence, missing evidence, reviewer rationale, and
  an interpretation caution. Do not mechanically average ratings — every "Overall ..." roll-up item
  is explicit reviewer judgment across its sub-items, not an arithmetic mean.
- Missing documentation is missing **evidence**, not automatic proof the benchmark is poor.

## House-convention sections (not in the canonical template)

Every review in `reviews/` also carries two sections that are **not** part of
`MESA EFPA template official.md` itself — they are a house convention layered on top of the
template. Do not go looking for them in the template; their absence there is expected:

- **Short Stand-Alone Non-Evaluative Benchmark Description** — a short, non-evaluative paragraph
  summarizing the benchmark, placed near the top of the review (before Part A begins).
- **Source Inventory** — a table of every source consulted (ID, source, access date, use in this
  review), placed immediately after the Short Stand-Alone description, before Part A begins.

---

## Front Matter

- **Introduction** — states MESA's purpose: a structured description/evaluation model treating AI
  benchmarks as measurement instruments, adapting the EFPA Test Review Model 2025.
- **How the MESA Model Should Be Used** — usage guidance: keep Part A descriptive and Part B
  evaluative, don't inherit ratings from a parent benchmark for slices/variants, prefer authoritative
  sources over independent commentary.

## Part A. Description of the Benchmark — *descriptive, no ratings*

### Section 1. Factual Description
Identifies the review event, the exact reviewed entity, and the materials inspected.

- **1.1 Review Administration** — reviewer name, date of current review, date of previous review (if applicable).
- **1.2 Benchmark Identity & Provenance** — reviewed entity name, short name, entity type, parent/source benchmark, version/split, implementation/scorer version, creators/maintainers, host organization, release dates, license, persistent identifier.
- **1.3 Materials, Sources, & Access Tracking** — inventory of paper, website, code repo, dataset, harness, leaderboard, guides, changelog, announcements, contextual literature, and contact channels, each with a URL/location and access date.

### Section 2. Classification
Classifies the benchmark's intended measurement domain, target AI systems, users, task structure, and administration conditions. Introduces the ten CHC-inspired capability domains (K, RW, M, R, WM, MS, MR, V, A, S) used throughout MESA.

- **2.1 Claimed Capability Domains** — which capabilities/phenomena the benchmark claims to measure, using the CHC-inspired domains plus benchmark-specific categories (coding, tool use, agency, safety, etc.).
- **2.2 Area of Use** — documented use contexts (model comparison, leaderboard ranking, safety evaluation, procurement, policy analysis, etc.).
- **2.3 Intended AI Systems** — which system classes the benchmark targets (frontier LLMs, chat models, code models, multimodal, agentic, API-hosted, open-weight, etc.).
- **2.4 Intended Users of Benchmark Outputs** — who is meant to consume results (researchers, developers, safety evaluators, policy actors, public leaderboard users, etc.).
- **2.5 Task Families, Subdomains, and Scores** — descriptive table of the claimed construct, its definition, subcomponents, excluded scope, item/task families, sourcing, sampling, splits, primary/subscores/derived scores, and score-interpretation boundaries.
- **2.6 Model Response Mode** — what form of output the model must produce (multiple choice, code, tool call, image, video, environment interaction, etc.).
- **2.7 Prerequisites for Evaluated Systems** — what a system must have to participate (language support, context length, multimodal input, tool/API access, compute budget, etc.), marked irrelevant/necessary/missing.
- **2.8 Evaluation Conditions** — prompting protocol, system prompt, sampling settings, tool permissions, time limits, human-intervention rules, hardware, and other administration conditions.
- **2.9 Task Interaction and Observable Evidence Types** — task interaction pattern (selection, production, interaction/environment) and observable process data (latency, tool traces, reasoning traces, logs, etc.).
- **2.10 Input Stimulus Type** — what kinds of input the benchmark presents (text, code, images, audio, video, documents, dynamic environment state, etc.).
- **2.11 Number of Items or Measurement Points** — counts of public/private/dev/test items, by split, language, domain, difficulty, and access status, plus count uncertainty.
- **2.12 Mode of Evaluation** — how evaluation is run (local batch, hosted platform, leaderboard submission, competition, etc.) and the degree of control over submitted systems.
- **2.13 Technological Arrangements** — available (A) vs. required (R) technology: API access, local inference, GPU, Docker, browser, external tools, hosted scoring, simulator, etc.
- **2.14 Time and Resource Requirements** — documented time/compute/cost estimates for setup, inference, scoring, human adjudication, and a full run.
- **2.15 Benchmark Forms, Versions, and Variants** — public/private forms, alternate/short forms, language variants, slices, rolling cohorts, and whether the documentation treats them as score-comparable.
- **2.16 Static or Dynamic Task Determination** — whether tasks are a static fixed set, random sample, procedurally generated, adaptive, rolling/refreshed, or otherwise dynamic.
- **2.17 Evidence Sources Used in Scoring** — what evidence feeds the score (final answer, intermediate trace, tool trace, environment state, human/model judge, unit test, etc.).
- **2.18 Broad-Claim Flags for Later Evaluation** — descriptive screen for AGI/general-intelligence/reasoning/agency-style claims: term used, breadth/depth implied, capability-domain coverage/exclusions, and caveats to carry into Part B.

### Section 3. Measurement and Scoring
Describes how model behavior becomes a score, separating scoring *procedure* from *scores*.

- **3.1 Scoring Procedure** — scoring method classes only (exact-match, LLM-as-judge, unit-test-based, rule-based, human rating, etc.) — not the pipeline itself.
- **3.2 Scores and Metrics** — the scoring pipeline: primary/subscores/derived scores/qualitative bands, their definitions, combination rules, capability-domain linkage, stated interpretation, and treatment of failed/refused/malformed responses.
- **3.3 Scale or Metric Types** — the metric family used (accuracy, pass@k, Elo, reward, cost-adjusted score, calibration score, etc.).
- **3.4 Score Transformation** — whether/how scores are transformed (linear/non-linear, normalized, weighted across domains, aggregation formula documented or not).
- **3.5 Documented Reference Groups, Baselines, and Comparators** — what reference points exist (chance, human, expert, model cohort, prior version, etc.) and how each is constructed and intended to be interpreted.
- **3.6 Score Uncertainty and Stability** — descriptive record of whether uncertainty/repeat-run consistency is reported (standard errors, bootstrap intervals, multiple seeds, sensitivity analyses, etc.).
- **3.7 Documented Metric Rationale and Stated Score Interpretation** — why the scoring rule was chosen, whether limits/non-target rewarded behavior/format burden/sensitivity/uncertainty are documented, and what users are told not to infer.

### Section 4. Benchmark Outputs and Reports
Adapts EFPA's "digitally generated reports" to AI benchmark outputs: papers, leaderboards, dashboards, result files, APIs.

- **4.1 Output Availability** — what's publicly available (leaderboard, aggregate scores, domain scores, per-item data, traces, confidence intervals, private-only reports, etc.).
- **4.2 Output Name or Description** — inventory table of each output surface: description, public/private status, and responsible operator.
- **4.3 Output Design or Presentation** — presentation format (static report, tables, graphs, leaderboard, dashboard, downloadable file, API, paper-only).
- **4.4 Output Structure** — organizing principle of the output (aggregate-score, capability-domain, task-family, rank, cost-adjusted, split/cohort based, etc.).
- **4.5 Sensitivity to Context** — whether there's one fixed output format, user-definable contexts, or pre-defined audience-adapted versions.
- **4.6 Development of Outputs** — how report content was produced (author design, empirical/actuarial relationships, expert judgment, human annotation, another model, automated platform generation).
- **4.7 Modifiability** — whether outputs/reports can be modified by the submitter or user, and how much.
- **4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels** — whether the link from tasks → scores → report labels/capability-domain labels is clear, partial, or undocumented.
- **4.9 Output Content** — what the output actually contains (domain profiles, rankings, coverage maps, error categories, cost/latency data, caveats, etc.).
- **4.10 Intended Recipients** — who each output surface is meant for (maintainers, developers, researchers, policy actors, public audience, etc.).

### Section 5. Benchmark Access, Materials, and Lifecycle
Records distribution, access, reproduction, and maintenance — informed by BetterBench's design/implementation/documentation/maintenance/usability framing.

- **5.1 Distribution and Access Model** — what documentation artifacts exist (technical report, user guide, README, API docs, dataset card, scoring docs, rubric, FAQ, changelog).
- **5.2 Distribution and Access Model** — the access model itself (fully public, public with hidden answer keys, controlled-access host, private evaluation service, leaderboard-only, competition distribution, etc.). *(Note: 5.1 and 5.2 share the same heading text in the canonical template by design — 5.1 covers documentation artifacts, 5.2 covers the access/distribution route.)*
- **5.3 Methods of Publication** — publication channels used (academic paper, website, git repo, package registry, dataset platform, leaderboard platform, controlled-access host, etc.).
- **5.4 User Requirements or Qualifications** — requirements to run/submit/interpret/maintain the benchmark: technical skill, model/dataset access, compute/budget, credentials, human expertise, eligibility, ethical/safety obligations.
- **5.5 Dataset and Item Access** — public/restricted/hidden/unavailable status of training items, eval items, private/secret items, answer keys, annotations, raw outputs, and task-registry/tool config.
- **5.6 Provenance and Contamination Documentation** — documented/partial/undocumented status of data origin, release timing, dedup/overlap checks, prior-exposure screening, canary strings, leak response policy, hash commitments, item-rotation rules, and disclosure reporting.
- **5.7 Reproducibility Materials** — what's available to reproduce results (task data, prompt templates, scoring code, environment/container specs, seeds, replication scripts, CI/build status, etc.).
- **5.8 Maintenance and Versioning** — maintainer identity, private-set owner, leaderboard operator, rerun/stale-score/model-version-update policy, versioning of scorer/judge/harness, retirement/archival policy, changelog, issue process, item correction process, and long-term archival plan.

### Appendix A. General Description of the Benchmark
A concise, non-evaluative descriptive summary of the benchmark for readers who haven't inspected the materials, deferring all evaluation to Part B. (Free text.)

---

## Part B front matter (boilerplate — copy verbatim into every full review, not benchmark-specific)

- **Information Sources** — what kinds of sources may inform Part B: official materials, public benchmark materials, academic/critique literature (context only, not a replacement for official facts), maintainer-provided/access-controlled material (disclose if a rating depends on it), and confidential/restricted technical information (describe rating implications without disclosing restricted content).
- **Explanation of Ratings** — the EFPA-style `n/a`/`0`-`4` scale applies everywhere unless a section overrides it; ratings are reviewer judgment (not mechanical), and a `0`/`1` on a critical attribute should trigger a limited-use caution.
- **Rating Scale** (table under Explanation of Ratings) — `n/a` not applicable; `0` no/insufficient info; `1` inadequate; `2` adequate for cautious use; `3` good, minor gaps; `4` excellent/comprehensive.
- **General Guidance on Assigning Ratings** — adequacy of evidence is relative to the benchmark's actual stated use and score interpretation, not a fixed universal bar; broad AGI/intelligence-style claims require stronger breadth/validity evidence than narrow claims.

## Part B. Evaluation of the Benchmark — *evaluative, every numbered item rated `n/a`/`0`-`4`*

### Section 6. Rationale, Development, Documentation, and Task/Item Quality
Whether the benchmark defines the real capability of interest, justifies its tasks/scoring as operationalizing that phenomenon, documents development, and gives users enough procedural information for cautious use. Revisit after Sections 8-12.

- **6.1 Rationale and Development**
  - **6.1.1 Rationale and construct definition** — is the target capability clearly defined, bounded, and distinguished from adjacent/broader interpretations?
  - **6.1.2 Summary of prior research and benchmark context** — does documentation situate the benchmark in prior research and state what gap it fills?
  - **6.1.3 Phenomenon-task-metric-claim chain** — is the real capability explicitly linked through task design, scoring rule, and intended score meaning, with confounds considered?
  - **6.1.4 Task or item design** — are task formats, difficulty range, and scoring protocol justified as fit for the measurement aim?
  - **6.1.5 Procedures for developing task or item content** — was content development expert-informed, with clear inclusion/exclusion criteria and quality checks?
  - **6.1.6 Thoroughness of the final task or item selection process** — is the final item pool justified by a defensible sampling strategy and coverage analysis?
  - **6.1.7 Quantitative evidence of task or item quality** — is quantitative item-quality evidence reported (difficulty, discrimination, redundancy, etc.)?
  - **6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice** — for any adapted/derived/reused/sliced entity, is the process documented with equivalence checks and comparability limits?
  - **6.1.9 Overall Rationale, development, and task or item quality** — reviewer-judgment roll-up of 6.1.1-6.1.8 (not a mechanical average).
- **6.2 Adequacy of Documentation Available to Users**
  - **6.2.1 Documentation of benchmark purpose and intended use** — is what the benchmark does/doesn't measure, and its suitable/unsuitable uses, documented?
  - **6.2.2 Documentation of development process** — are data sources, sampling, construction, filtering, and design-decision rationale documented?
  - **6.2.3 Documentation of scoring and metrics** — is output parsing, scoring rules, aggregation, and failure-mode handling documented?
  - **6.2.4 Documentation of reliability, stability, and uncertainty** — is score stability/variance assessment documented?
  - **6.2.5 Documentation of validity evidence** — is a validity argument for the intended score meaning documented?
  - **6.2.6 Documentation of fair use and comparability** — are fairness, accessibility, and comparability considerations documented?
  - **6.2.7 Documentation of maintenance and versioning** — is version history, changelog, and comparability-across-versions guidance documented?
  - **6.2.8 Adequacy of documentation available to users** — reviewer-judgment roll-up of 6.2.1-6.2.7.
- **6.3 Quality of Procedural Instructions**
  - **6.3.1 Evaluation setup and administration** — are setup/run instructions complete and reproducible?
  - **6.3.2 Scoring procedure and error handling** — are scoring instructions clear, with parser/judge failure handling documented?
  - **6.3.3 Interpretation and reporting guidance** — do users get guidance on interpreting scores, uncertainty, and comparisons?
  - **6.3.4 Restrictions, prerequisites, and appropriate use** — are prerequisites, unsupported systems, and prohibited uses clearly stated?
  - **6.3.5 Technical support and implementation guidance** — is troubleshooting/support documentation available?
  - **6.3.6 References and supporting materials** — are source-linked references to papers/data/code provided?
  - **6.3.7 Quality of procedural instructions** — reviewer-judgment roll-up of 6.3.1-6.3.6.
- **6.4 Overall Adequacy of Rationale and Documentation** — reviewer-judgment roll-up across 6.1-6.3.

### Section 7. Quality and Usability of Benchmark Materials
Whether datasets, prompts, rubrics, scoring code, harnesses, and interfaces are complete and usable for intended users to inspect/run/score/reproduce/audit.

- **7.1 Quality of Benchmark Materials**
  - **7.1.1 Dataset, task set, or evaluation environment availability** — is the dataset/environment/registry entry complete, versioned, and appropriately accessible?
  - **7.1.2 Prompts, instructions, and input materials** — are prompts/instructions/input assets documented or controlled to support reproducible evaluation?
  - **7.1.3 Rubrics, reference answers, and response format requirements** — are rubrics/answer keys/response schemas clear and versioned?
  - **7.1.4 Evaluation harness, scorer, and implementation quality** — is the harness/scorer runnable, tested, and reproducible?
  - **7.1.5 Interface and workflow usability** — is the workflow easy for intended users to operate without hidden steps?
  - **7.1.6 Accessibility across modalities, languages, and system types** — are materials usable across relevant modalities/languages/deployment modes?
  - **7.1.7 Licensing, use requirements, and risk warnings** — are licenses, terms, and content/safety warnings explicit and compatible with use?
  - **7.1.8 Overall quality of benchmark materials** — reviewer-judgment roll-up of 7.1.1-7.1.7.

### Section 8. Baselines, Comparators, and Reference Interpretation
Reference points used to make scores interpretable — chance floors, human/expert performance, model cohorts, prior versions, score bands.

- **8.1 Baseline and Comparator Interpretation**
  - **8.1.1 Random, chance, floor, and ceiling baselines** — are chance/trivial-strategy/ceiling reference points reported and integrated?
  - **8.1.2 Human or expert baselines** — is human/expert performance collected with clear sampling, conditions, and comparability limits to AI systems?
  - **8.1.3 Model comparator cohort** — are documented model comparison groups (identity, version, conditions, uncertainty) selected to support the score meaning?
  - **8.1.4 Historical, version, or benchmark-family comparators** — are comparisons to prior versions/related benchmarks documented and caveated?
  - **8.1.5 Criterion thresholds, score bands, or performance categories** — are score boundaries/tier labels empirically justified rather than arbitrary?
  - **8.1.6 Representativeness of reference groups** — are reference groups representative, with documented inclusion criteria and known gaps?
  - **8.1.7 Currency and maintenance of baseline evidence** — is baseline evidence current, with guidance on when it's outdated?
- **8.2 Overall Adequacy of Baselines and Reference Interpretation** — reviewer-judgment roll-up across 8.1.

### Section 9. Reliability, Precision, and Score Stability
Whether scores are stable enough for their intended use across runs, prompts, seeds, forms, raters, judges, and versions.

- **9.1 Data Provided About Reliability, Precision, and Stability**
  - **9.1.1 Coverage of reliability and stability evidence** — does the benchmark report reliability evidence across the major relevant sources of score variation?
- **9.2 Run-to-Run Stability and Uncertainty**
  - **9.2.1 Run-to-run stability, seeds, and sampling settings** — do repeat-run studies quantify stability across seeds/sampling/tool-use/environment?
  - **9.2.2 Score uncertainty, confidence intervals, or standard errors** — are scores accompanied by appropriate uncertainty estimates?
- **9.3 Scorer, Judge, Parser, and Rater Reliability**
  - **9.3.1 Automated scorer or parser reliability** — is automated scoring/parsing validated against representative outputs and edge cases?
  - **9.3.2 Human rater or expert scorer agreement** — is human scoring validated via rubrics, training, and reported rater agreement?
  - **9.3.3 Model-as-judge reliability and validity checks** — is scoring-by-another-model validated against human judgment and monitored for drift/bias?
- **9.4 Form, Version, Prompt, and Environment Stability**
  - **9.4.1 Prompt, instruction, or formatting sensitivity** — is sensitivity to prompt wording/formatting variation assessed?
  - **9.4.2 Form, split, version, or refresh equivalence** — is equivalence across alternate forms/splits/versions documented?
  - **9.4.3 Execution environment and dependency stability** — is environment/dependency/API variation controlled or tested?
- **9.5 Statistical Comparison Quality**
  - **9.5.1 Meaningfulness of score differences** — is there statistically justified guidance for when model-score differences are meaningful?
- **9.6 Overall Reliability, Precision, and Score Stability** — reviewer-judgment roll-up across 9.1-9.5.

### Section 10. Validity Evidence
The construct-validity chain: real capability → task → metric → claim. Uses Bean et al.'s *Measuring what Matters* as the primary source; BetterBench informs contamination/gameability.

- **10.1 Validity Evidence Based on Benchmark Content**
  - **10.1.1 Content validity and task representativeness** — does the task sample comprehensively represent the intended capability domain, with coverage analysis?
  - **10.1.2 Construct breadth and capability-domain coverage** — is the score meaning supported across the claimed breadth, not isolated task performance?
- **10.2 Validity Evidence Based on Internal Structure**
  - **10.2.1 Internal structure, subscores, or dimensionality** — are subscores/domain profiles empirically and conceptually supported?
  - **10.2.2 Item or task behavior across the score scale** — does task behavior show appropriate difficulty spread and lack of dominant non-target effects?
  - **10.2.3 Failure modes and error analysis** — does error analysis show failures reflect the target capability, not confounders?
- **10.3 Validity Evidence Based on Metrics and Scoring**
  - **10.3.1 Metric, scorer, and aggregation validity** — are scoring rules/rubrics/judges validated as measuring the intended capability, not irrelevant behavior?
  - **10.3.2 Sensitivity to shortcuts and construct-irrelevant variance** — are non-target tactics/shortcuts/format effects tested or mitigated?
- **10.4 Validity Evidence Based on Relations to Other Variables**
  - **10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings** — are expected relationships with other evidence hypothesized and empirically examined?
  - **10.4.2 Convergent and discriminant evidence** — does the benchmark show expected convergence with similar measures and separation from different ones?
  - **10.4.3 Ecological or predictive relevance** — is benchmark performance's relevance to real-world/deployment interpretations supported?
- **10.5 Contamination, Leakage, and Gameability**
  - **10.5.1 Contamination and leakage controls** — are data provenance, release timing, and prior-exposure controls documented?
  - **10.5.2 Gameability and benchmark-specific tuning controls** — are risks from benchmark-specific optimization/gaming identified and mitigated?
- **10.6 Claim Proportionality**
  - **10.6.1 Proportionality of stated benchmark claims** — are score interpretations explicitly bounded to what the evidence supports?
  - **10.6.2 Broad intelligence, AGI, agency, or autonomy claims** — if broad claims are made, is there evidence across relevant domains/modalities/horizons, or are such claims explicitly limited?
- **10.7 Overall Validity Support** — reviewer-judgment roll-up across 10.1-10.6.

### Section 11. Fair Use, Comparability, and Appropriate Use
Whether the benchmark can be used and compared fairly across relevant systems, modalities, languages, and contexts — broader than demographic fairness alone.

- **11.1 Rationale and Documentation for Fair Use**
  - **11.1.1 Relevance of the construct across systems, groups, and contexts** — is the construct's relevance across intended systems/groups/contexts explained, with justified exclusions?
  - **11.1.2 Documentation of fair-use considerations** — are fairness/accessibility/bias considerations documented?
- **11.2 Development, Design, and Accessibility**
  - **11.2.1 Inclusive and accessible benchmark design** — was accessibility considered during design, with adaptations documented?
  - **11.2.2 Domain, language, modality, and subgroup coverage** — is coverage across languages/modalities/cultures/subgroups analyzed, with gaps stated?
- **11.3 Cross-System and Evaluation-Condition Comparability**
  - **11.3.1 Cross-system comparability** — do conditions support fair comparison across intended AI systems (versions, access modes, tools, etc.)?
  - **11.3.2 Access, compute, tooling, and API or local comparability** — are access/compute/tooling differences documented so comparisons aren't distorted?
  - **11.3.3 Temporal comparability for rolling or live benchmarks** — for rolling/live benchmarks, are cohort/date/stale-score comparison limits documented?
- **11.4 Evidence for Fairness and Bias**
  - **11.4.1 Differential performance or bias analysis** — does the benchmark investigate performance differences/bias across relevant systems, languages, or groups?
  - **11.4.2 Reliability and validity across relevant subgroups or contexts** — are reliability/validity examined across relevant subgroups, with differences tied to interpretation limits?
- **11.5 Appropriate Use and Restrictions**
  - **11.5.1 Appropriate-use guidance and non-use cases** — is there clear guidance on supported vs. prohibited/unsupported uses?
  - **11.5.2 Release rules and sensitive-content handling** — do release rules and content warnings support responsible use?
- **11.6 Overall Fair Use, Comparability, and Appropriate Use** — reviewer-judgment roll-up across 11.1-11.5.

### Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims
Whether reporting surfaces (papers, leaderboards, dashboards, public claims) make clear what a score means, under what conditions, with what uncertainty.

- **12.1 Scope and Coverage**
  - **12.1.1 Report, leaderboard, dashboard, or reporting-material scope** — do reports cover relevant scores/subscores/domain profiles without implying unsupported precision?
  - **12.1.2 Score granularity and level of detail** — is the level of reported detail justified by measurement precision and task coverage?
- **12.2 Reliability and Traceability of Reports**
  - **12.2.1 Uncertainty, version labeling, and evaluation-condition labeling** — do reports identify version, date, conditions, and uncertainty?
  - **12.2.2 Reproducibility and traceability of reported scores** — can reported scores be traced to documented runs/configurations?
- **12.3 Relevance and Validity of Reports**
  - **12.3.1 Linkage from scores to interpretations and public claims** — do reports explain what each score does/doesn't support?
  - **12.3.2 Raw outputs, per-item data, or trace availability** — are raw outputs/traces available or access-controlled for independent scrutiny?
- **12.4 Fairness, Acceptability, and Public Communication**
  - **12.4.1 Fairness and freedom from bias in reports** — do reports use non-misleading language and identify coverage/bias gaps?
  - **12.4.2 Acceptability and usability for intended audiences** — are reports understandable and suited to their intended audience?
  - **12.4.3 Public communication and leaderboard governance** — are public claims, leaderboard rules, and governance transparent and resistant to overinterpretation?
- **12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims** — reviewer-judgment roll-up across 12.1-12.4.

## Final Evaluation

- **Evaluative Report of the Benchmark** — free-text overall judgment: strengths, limitations, use recommendations, warnings, and notes on ongoing maintainer work. (Free text.)
- **Conclusions** — one-to-two-sentence summary of quality, supported use(s), and the expertise level needed to use the entity responsibly. (Free text.)
- **Recommendations** — what users/maintainers/future reviewers should do next, tied to findings. (Free text.)
- **Summary of Ratings** — table rolling up the overall rating (`n/a`/`0`-`4`) for Sections 6-12.
- **Gap Register** — table of missing/inaccessible evidence: what's missing, what it affects, why it matters, and what's needed for a higher rating.

## Bibliography
Numbered citation list ([1] Hendrycks et al., *A Definition of AGI*; [2] Bean et al., *Measuring what Matters*; [3] Reuel et al., *BetterBench*) — cited throughout Sections 2, 5, 6, 7, 9, 10 via `[1]`/`[2]`/`[3]` markers.

# Check of MESA questions

Prepared by the AI assistant on 2026-09-25. This is a first-pass explanation of the current design, written now. It is not proof of the original author’s process or an independent expert review.

## Sources and reading guide

- **EFPA:** [local source](../literature/EFPA_Test_Review_Model_2025_Markdown.md), section numbers below.
- **BetterBench:** [local source](../literature/betterbench.md), benchmark design, implementation, documentation and maintenance criteria.
- **Measuring what Matters:** [local source](../literature/Measuring_what_Matters.md), the relationship between claimed ability, task, metric and claim; Appendix B supplies the paper’s coding questions.
- **AGI/CHC:** [local source](../literature/A_Definition_of_AGI.md), cognitive breadth as a basis for broad-intelligence claims.

The [earlier mapping](../feedback/95-mesa-core-plan.md) supplies more detailed EFPA correspondences. Source entries below identify a related review function, not an assertion that identical wording appears in the source. MESA’s exact questions and rating thresholds are design choices.

## Decisions

Retain the 87 rated items for this revision. The available work supports clearer instructions, not a defensible new item count. Keep the four already retired IDs retired. Share source notes rather than repeat them. Clarify 0 versus 1 and 9.2.1, as explained in [pilot lessons](pilot-lessons.md).

Two source-mapping claims need caution. The earlier plan says internal-consistency questions are absorbed into score uncertainty and that item-response modeling has no AI counterpart. Neither follows merely from replacing people with models. Internal consistency and uncertainty are different questions. The current MESA questions allow item/structure evidence at 6.1.7 and 10.2, but whether that is enough remains unresolved. Do not cite those earlier exclusions as settled results.

The following table covers each active numbered Part A unit and each rated Part B item. The group notes explain what to inspect and when it applies. Retention is provisional; the table does not establish completeness. General Description summarizes Part A; Source Inventory records the consulted sources; Final Evaluation combines the findings without a total score.

## Item map

| Item | Question | Source group | Decision |
| --- | --- | --- | --- |
| 1.1 | Review Administration | 1 | Keep; reuse existing source notes |
| 1.2 | Benchmark Identity & Provenance | 1 | Keep; reuse existing source notes |
| 1.3 | Materials, Sources, & Access Tracking | 1 | Keep; reuse existing source notes |
| 2.1 | Claimed Capability Domains | 2.1 | Keep; reuse existing source notes |
| 2.2 | Area of Use | 2.2 | Keep; reuse existing source notes |
| 2.3 | Intended AI Systems | 2.3 | Keep; reuse existing source notes |
| 2.4 | Intended Users and Recipients of Benchmark Outputs | 2.4 | Keep; reuse existing source notes |
| 2.5 | Task Families, Subdomains, and Splits | 2.5 | Keep; reuse existing source notes |
| 2.7 | Prerequisites for Evaluated Systems | 2.7 | Keep; reuse existing source notes |
| 2.8 | Evaluation Conditions | 2.8 | Keep; reuse existing source notes |
| 2.9 | Task Interaction, Response Types, and Observable Evidence | 2.9 | Keep; reuse existing source notes |
| 2.10 | Input Stimulus Type | 2.10 | Keep; reuse existing source notes |
| 2.11 | Number of Items or Measurement Points | 2.11 | Keep; reuse existing source notes |
| 2.12 | Mode of Evaluation | 2.12 | Keep; reuse existing source notes |
| 2.13 | Technological Arrangements | 2.13 | Keep; reuse existing source notes |
| 2.14 | Time and Resource Requirements | 2.14 | Keep; reuse existing source notes |
| 2.15 | Benchmark Forms, Versions, and Variants | 2.15 | Keep; reuse existing source notes |
| 2.16 | Static or Dynamic Task Determination | 2.16 | Keep; reuse existing source notes |
| 2.17 | Evidence Sources Used in Scoring | 2.17 | Keep; reuse existing source notes |
| 2.18 | Broad-Claim Flags for Later Evaluation | 2.18 | Keep; reuse existing source notes |
| 3.1 | Scoring Procedure | 3.1 | Keep; reuse existing source notes |
| 3.2 | Scores and Metrics | 3.2 | Keep; reuse existing source notes |
| 3.3 | Scale or Metric Types | 3.3 | Keep; reuse existing source notes |
| 3.4 | Score Transformation | 3.4 | Keep; reuse existing source notes |
| 3.5 | Documented Reference Groups, Baselines, and Comparators | 3.5 | Keep; reuse existing source notes |
| 3.6 | Score Uncertainty and Stability | 3.6 | Keep; reuse existing source notes |
| 3.7 | Documented Metric Rationale and Stated Score Interpretation | 3.7 | Keep; reuse existing source notes |
| 4.1 | Output Availability | 4 | Keep; reuse existing source notes |
| 4.2 | Output Name or Description | 4 | Keep; reuse existing source notes |
| 4.3 | Output Design or Presentation | 4 | Keep; reuse existing source notes |
| 4.4 | Output Structure | 4 | Keep; reuse existing source notes |
| 4.5 | Sensitivity to Context | 4 | Keep; reuse existing source notes |
| 4.6 | Development of Outputs | 4 | Keep; reuse existing source notes |
| 4.7 | Modifiability | 4 | Keep; reuse existing source notes |
| 4.8 | Documented Linkage Status Between Tasks, Scoring, and Report Labels | 4 | Keep; reuse existing source notes |
| 4.9 | Output Content | 4 | Keep; reuse existing source notes |
| 5.1 | Supporting Documentation Provided to Users | 5.1 | Keep; reuse existing source notes |
| 5.2 | Distribution and Access Model | 5.2 | Keep; reuse existing source notes |
| 5.3 | Methods of Publication | 5.3 | Keep; reuse existing source notes |
| 5.4 | User Requirements or Qualifications | 5.4 | Keep; reuse existing source notes |
| 5.5 | Dataset and Item Access | 5.5 | Keep; reuse existing source notes |
| 5.6 | Provenance and Contamination Documentation | 5.6 | Keep; reuse existing source notes |
| 5.7 | Reproducibility Materials | 5.7 | Keep; reuse existing source notes |
| 5.8 | Maintenance and Versioning | 5.8 | Keep; reuse existing source notes |
| 6.1.1 | Rationale and construct definition | 6.1 | Keep; reuse existing source notes |
| 6.1.2 | Summary of prior research and benchmark context | 6.1 | Keep; reuse existing source notes |
| 6.1.3 | Phenomenon-task-metric-claim chain | 10.6 | Keep; reuse existing source notes |
| 6.1.4 | Task or item design | 6.1 | Keep; reuse existing source notes |
| 6.1.5 | Procedures for developing task or item content | 6.1 | Keep; reuse existing source notes |
| 6.1.6 | Thoroughness of the final task or item selection process | 6.1 | Keep; reuse existing source notes |
| 6.1.7 | Quantitative evidence of task or item quality | 6.1 | Keep; reuse existing source notes |
| 6.1.8 | Adaptation, translation, source reuse, derived entity, or benchmark slice | 6.1 | Keep; reuse existing source notes |
| 6.1.9 | Overall Rationale, development, and task or item quality | 6.1 | Keep; reuse existing source notes |
| 6.2.1 | Documentation of benchmark purpose and intended use | 6.2 | Keep; reuse existing source notes |
| 6.2.2 | Documentation of development process | 6.2 | Keep; reuse existing source notes |
| 6.2.3 | Documentation of scoring and metrics | 6.2 | Keep; reuse existing source notes |
| 6.2.4 | Documentation of reliability, stability, and uncertainty | 6.2 | Keep; reuse existing source notes |
| 6.2.5 | Documentation of validity evidence | 6.2 | Keep; reuse existing source notes |
| 6.2.6 | Documentation of fair use and comparability | 6.2 | Keep; reuse existing source notes |
| 6.2.7 | Documentation of maintenance and versioning | 6.2 | Keep; reuse existing source notes |
| 6.2.8 | Adequacy of documentation available to users | 6.2 | Keep; reuse existing source notes |
| 6.3.1 | Evaluation setup and administration | 6.3 | Keep; reuse existing source notes |
| 6.3.2 | Scoring procedure and error handling | 6.3 | Keep; reuse existing source notes |
| 6.3.3 | Interpretation and reporting guidance | 6.3 | Keep; reuse existing source notes |
| 6.3.4 | Restrictions, prerequisites, and appropriate use | 6.3 | Keep; reuse existing source notes |
| 6.3.5 | Technical support and implementation guidance | 6.3 | Keep; reuse existing source notes |
| 6.3.6 | References and supporting materials | 6.3 | Keep; reuse existing source notes |
| 6.3.7 | Quality of procedural instructions | 6.3 | Keep; reuse existing source notes |
| 6.4 | Overall Adequacy of Rationale and Documentation | 6.4 | Keep; reuse existing source notes |
| 7.1.1 | Dataset, task set, or evaluation environment availability | 7 | Keep; reuse existing source notes |
| 7.1.2 | Prompts, instructions, and input materials | 7 | Keep; reuse existing source notes |
| 7.1.3 | Rubrics, reference answers, and response format requirements | 7 | Keep; reuse existing source notes |
| 7.1.4 | Evaluation harness, scorer, and implementation quality | 7 | Keep; reuse existing source notes |
| 7.1.5 | Interface and workflow usability | 7 | Keep; reuse existing source notes |
| 7.1.6 | Accessibility across modalities, languages, and system types | 7 | Keep; reuse existing source notes |
| 7.1.7 | Licensing, use requirements, and risk warnings | 7 | Keep; reuse existing source notes |
| 7.1.8 | Overall quality of benchmark materials | 7 | Keep; reuse existing source notes |
| 8.1.1 | Random, chance, floor, and ceiling baselines | 8 | Keep; reuse existing source notes |
| 8.1.2 | Human or expert baselines | 8 | Keep; reuse existing source notes |
| 8.1.3 | Model comparator cohort | 8 | Keep; reuse existing source notes |
| 8.1.4 | Historical, version, or benchmark-family comparators | 8 | Keep; reuse existing source notes |
| 8.1.5 | Criterion thresholds, score bands, or performance categories | 8 | Keep; reuse existing source notes |
| 8.1.6 | Representativeness of reference groups | 8 | Keep; reuse existing source notes |
| 8.1.7 | Currency and maintenance of baseline evidence | 8 | Keep; reuse existing source notes |
| 8.2 | Overall Adequacy of Baselines and Reference Interpretation | 8 | Keep; reuse existing source notes |
| 9.1.1 | Coverage of reliability and stability evidence | 9 | Keep; reuse existing source notes |
| 9.2.1 | Run-to-run stability, seeds, and sampling settings | 9 | Clarify rating evidence |
| 9.2.2 | Score uncertainty, confidence intervals, or standard errors | 9 | Keep; reuse existing source notes |
| 9.3.1 | Automated scorer or parser reliability | 9 | Keep; reuse existing source notes |
| 9.3.2 | Human rater or expert scorer agreement | 9 | Keep; reuse existing source notes |
| 9.3.3 | Model-as-judge reliability and validity checks | 9 | Keep; reuse existing source notes |
| 9.4.1 | Prompt, instruction, or formatting sensitivity | 9 | Keep; reuse existing source notes |
| 9.4.2 | Form, split, version, or refresh equivalence | 9 | Keep; reuse existing source notes |
| 9.4.3 | Execution environment and dependency stability | 9 | Keep; reuse existing source notes |
| 9.5.1 | Meaningfulness of score differences | 9 | Keep; reuse existing source notes |
| 9.6 | Overall Reliability, Precision, and Score Stability | 9 | Keep; reuse existing source notes |
| 10.1.1 | Content validity and task representativeness | 10.1 | Keep; reuse existing source notes |
| 10.1.2 | Construct breadth and capability-domain coverage | 10.1 | Keep; reuse existing source notes |
| 10.2.1 | Internal structure, subscores, or dimensionality | 10.2 | Keep; reuse existing source notes |
| 10.2.2 | Item or task behavior across the score scale | 10.2 | Keep; reuse existing source notes |
| 10.2.3 | Failure modes and error analysis | 10.2 | Keep; reuse existing source notes |
| 10.3.1 | Metric, scorer, and aggregation validity | 10.3 | Keep; reuse existing source notes |
| 10.3.2 | Sensitivity to shortcuts and construct-irrelevant variance | 10.3 | Keep; reuse existing source notes |
| 10.4.1 | Relations with other benchmarks, humans, criteria, or realistic settings | 10.4 | Keep; reuse existing source notes |
| 10.4.2 | Convergent and discriminant evidence | 10.4 | Keep; reuse existing source notes |
| 10.4.3 | Ecological or predictive relevance | 10.4 | Keep; reuse existing source notes |
| 10.5.1 | Contamination and leakage controls | 10.5 | Keep; reuse existing source notes |
| 10.5.2 | Gameability and benchmark-specific tuning controls | 10.5 | Keep; reuse existing source notes |
| 10.6.1 | Proportionality of score interpretations | 10.6 | Keep; reuse existing source notes |
| 10.7 | Overall Validity Support | 10.7 | Keep; reuse existing source notes |
| 11.1.1 | Relevance of the construct across systems, groups, and contexts | 11 | Keep; reuse existing source notes |
| 11.1.2 | Documentation of fair-use considerations | 11 | Keep; reuse existing source notes |
| 11.2.1 | Inclusive and accessible benchmark design | 11 | Keep; reuse existing source notes |
| 11.2.2 | Domain, language, modality, and subgroup coverage | 11 | Keep; reuse existing source notes |
| 11.3.1 | Cross-system and access-condition comparability | 11 | Keep; reuse existing source notes |
| 11.3.3 | Temporal comparability for rolling or live benchmarks | 11 | Keep; reuse existing source notes |
| 11.4.1 | Differential performance or bias analysis | 11 | Keep; reuse existing source notes |
| 11.4.2 | Reliability and validity across relevant subgroups or contexts | 11 | Keep; reuse existing source notes |
| 11.5.1 | Appropriate-use guidance and non-use cases | 11 | Keep; reuse existing source notes |
| 11.5.2 | Release rules and sensitive-content handling | 11 | Keep; reuse existing source notes |
| 11.6 | Overall Fair Use, Comparability, and Appropriate Use | 11 | Keep; reuse existing source notes |
| 12.1.1 | Report, leaderboard, dashboard, or reporting-material scope | 12 | Keep; reuse existing source notes |
| 12.1.2 | Score granularity and level of detail | 12 | Keep; reuse existing source notes |
| 12.2.1 | Uncertainty, version labeling, and evaluation-condition labeling | 12 | Keep; reuse existing source notes |
| 12.2.2 | Reproducibility and traceability of reported scores | 12 | Keep; reuse existing source notes |
| 12.3.1 | Linkage from scores to interpretations and public claims | 12 | Keep; reuse existing source notes |
| 12.3.2 | Raw outputs, per-item data, or trace availability | 12 | Keep; reuse existing source notes |
| 12.4.1 | Fairness and freedom from bias in reports | 12 | Keep; reuse existing source notes |
| 12.4.2 | Acceptability and usability for intended audiences | 12 | Keep; reuse existing source notes |
| 12.4.3 | Public communication and leaderboard governance | 12 | Keep; reuse existing source notes |
| 12.5 | Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims | 12 | Keep; reuse existing source notes |

## Source groups

| Group | Source | Change | Reason and material to inspect | When it applies |
| --- | --- | --- | --- | --- |
| 1 | EFPA §1 | Rename | Identify the benchmark and inspected version; use review dates, repository tags and source records. | All reviews |
| 2.1 | EFPA §2.1; AGI/CHC | Replace | Describe the claimed abilities using AI-relevant domains; inspect the paper’s definitions. | Rate breadth only against the actual claim |
| 2.2 | EFPA §2.2 | Rename | Record the intended use from the paper or site. | All reviews |
| 2.3 | EFPA §2.3 | Replace | Replace human populations with intended AI systems; inspect eligibility rules. | All reviews |
| 2.4 | EFPA §§2.4, 4.10 | Combine | Record users and readers once; inspect intended audiences. | All reviews |
| 2.5 | EFPA §2.5 | Replace | Record task families and splits; keep score definitions in 3.2. | All reviews |
| 2.7 | EFPA §2.7 | Replace | Replace human demands with system prerequisites; inspect task and tool requirements. | Document actual prerequisites |
| 2.8 | EFPA §2.8; BetterBench | Replace | Record prompts, tools and run limits for later comparison. | All reviews |
| 2.9 | EFPA §§2.6, 2.9 | Combine | Describe interaction and output format together; inspect task examples. | All reviews |
| 2.10 | EFPA §2.10 | Rename | Record input modalities from task examples. | All reviews |
| 2.11 | EFPA §2.11 | Replace | Count tasks, splits and other measurement units from dataset records. | Use units appropriate to the benchmark |
| 2.12 | EFPA §2.12 | Replace | Describe hosted, local and supervised evaluation arrangements. | All reviews |
| 2.13 | EFPA §2.13; BetterBench | Replace | Record the harness, services and dependencies needed to run tasks. | Actual execution pathway |
| 2.14 | EFPA §2.14 | Replace | Record documented time and compute; do not invent estimates. | Mark unreported costs unknown |
| 2.15 | EFPA §2.15 | Rename | List versions and forms from release records. | Include a single form when that is all that exists |
| 2.16 | EFPA §2.16 | Rename | Record whether tasks change during or between evaluations. | All reviews |
| 2.17 | EFPA §2.17 | Replace | Replace human informants with sources used in scoring; inspect scoring inputs. | Keep scoring inputs separate from reported outputs |
| 2.18 | AGI/CHC; Measuring what Matters | Add | Collect broad public claims for later examination in 10.6.1. | No broad claim is a valid answer |
| 3.1 | EFPA §3.1; BetterBench | Replace | Describe human, automated and model-based scoring from the actual procedure. | Actual scoring pathway |
| 3.2 | EFPA §3.2 | Rename | Define each reported score once using formulas or scoring code. | All scores under review |
| 3.3 | EFPA §3.3 | Replace | Describe score scales such as accuracy or rank rather than assuming human test scales. | Actual reported scales |
| 3.4 | EFPA §3.4 | Preserve | Record score transformations and their purpose. | Only when transformations exist |
| 3.5 | EFPA §3.5; BetterBench | Replace | Expand norms into chance, human, model and historical reference points. | Reference points relevant to the intended claim |
| 3.6 | EFPA §9; BetterBench | Add | Record reported uncertainty before evaluating it in Section 9. | Missing results remain unknown |
| 3.7 | Measuring what Matters | Add | Record why the metric was chosen and what authors say it means. | All reviews |
| 4 | EFPA §4 | Replace | Replace individual test reports with papers, result files and leaderboards; inspect each relevant output. | Actual reporting surfaces |
| 5.1 | EFPA §5.1 | Rename | Record user documentation and support routes. | All reviews |
| 5.2 | BetterBench | Add | Record open, restricted or paid access and licenses. | Actual distribution route |
| 5.3 | EFPA §5.2 | Rename | Describe how materials are published. | All reviews |
| 5.4 | EFPA §5.3 | Replace | Record user qualifications and access requirements. | Distinguish none stated from unknown |
| 5.5 | BetterBench | Add | Record which task splits and answers are accessible. | Actual data and task access |
| 5.6 | BetterBench | Add | Record item origin and exposure controls from documentation. | Use-specific contamination risks |
| 5.7 | BetterBench | Add | List replication assets without assuming their presence proves successful replication. | Actual execution pathway |
| 5.8 | BetterBench | Add | Record maintenance, releases and score-comparison rules. | Static benchmarks still need clear version identity |
| 6.1 | EFPA §6.1; Measuring what Matters | Adapt | Check the claimed ability and why these tasks test it; use design and item-development records. | Actual claim; adaptation item only for reused or derived content |
| 6.2 | EFPA §6.2; BetterBench | Adapt | Judge whether users can find and understand relevant documentation. | Distinct from judging the underlying method |
| 6.3 | EFPA §6.3; BetterBench | Adapt | Judge whether setup, scoring and interpretation instructions can guide a reviewer. | Actual evaluation pathway |
| 6.4 | EFPA §6.4 | Preserve | Explain the overall rationale/documentation judgment using the findings in Section 6. | No arithmetic average |
| 7 | EFPA §7; BetterBench | Adapt | Judge the usability of data, prompts, scoring materials and interfaces. | Existing materials and required access; no paper-and-pencil duplicate section |
| 8 | EFPA §8; BetterBench | Replace | Judge reference points rather than require human population norms; inspect baseline methods and cohorts. | Only reference points needed for the intended claim |
| 9 | EFPA §9; BetterBench | Adapt | Separate variation across runs, scorers, forms and environments; inspect relevant studies. | See the item-level Section 9 notes below |
| 10.1 | EFPA §10.1; AGI/CHC; Measuring what Matters | Adapt | Check whether task sampling covers the claimed ability; use sampling and coverage analyses. | Narrow claims require narrow coverage |
| 10.2 | EFPA §10.2; Measuring what Matters | Adapt | Examine score structure and item failures from item-level analyses. | Subscore structure only when it is claimed; task analysis where meaningful |
| 10.3 | EFPA §10.4; Measuring what Matters | Add | Check whether the scoring rule rewards intended behavior rather than shortcuts; inspect score validation. | Actual metric and scorer |
| 10.4 | EFPA §10.3; Measuring what Matters | Adapt | Look for relationships with other tests or real tasks to support claims of transfer. | Do not demand broad transfer for a score limited to a fixed task set |
| 10.5 | BetterBench | Add | Judge exposure and tuning controls using access rules and audits. | Risks relevant to the intended interpretation |
| 10.6 | EFPA §10.4.3; AGI/CHC; Measuring what Matters | Adapt | Compare public interpretations with the evidence recorded in Part A. | Do not require every benchmark to measure AGI |
| 10.7 | EFPA §10.5 | Preserve | Explain which interpretations are supported using Section 10 findings. | No arithmetic average |
| 11 | EFPA §11; BetterBench | Adapt | Expand fair use to system types, access, language and run conditions; use subgroup studies and comparison rules. | Relevant groups and uses, not every conceivable group |
| 12 | EFPA §12; BetterBench | Adapt | Judge whether public reports communicate scores, limits and conditions accurately. | Inspect the most consequential actual reporting surface |

## Section 9: closer check

| Item | EFPA function or AI addition | Decision and boundary |
| --- | --- | --- |
| 9.1.1 | EFPA 9.1, inventory of reliability information | Keep as a list of covered and missing sources of variation; do not repeat the overall judgment. |
| 9.2.1 | EFPA 9.3, test-retest stability; AI run settings | Clarify that published settings or pass@k alone are not measured repeat-run stability. |
| 9.2.2 | EFPA Section 9 precision; BetterBench uncertainty reporting | Keep uncertainty estimates; do not describe this as equivalent to internal consistency. |
| 9.3.1 | AI scoring/parser addition; EFPA scoring consistency and BetterBench implementation | Inspect tests and error analysis. A deterministic rule does not establish a correct implementation. |
| 9.3.2 | EFPA 9.6, agreement between raters | Keep; apply when human judgment affects scoring. |
| 9.3.3 | Extend rater checks to model-based scoring | Keep; human-scoring agreement and judge drift matter when another model scores answers. |
| 9.4.1 | AI prompt/format sensitivity; related to alternate-form questions | Keep; inspect plausible prompt variants, not arbitrary changes to the task. |
| 9.4.2 | EFPA 9.4, alternate-form equivalence | Keep; one static form may be n/a; multiple unstudied forms require an unknown judgment. |
| 9.4.3 | EFPA temporal stability plus AI dependencies | Keep; environments and external services can change; configuration files alone are not stability studies. |
| 9.5.1 | BetterBench statistical comparisons; EFPA precision | Keep; absent uncertainty does not prove a score difference is noise. |
| 9.6 | EFPA 9.8, overall adequacy | Keep; state the particular comparison/use being judged. Do not average item ratings. |

## Open questions

- Does 9.1.1 need a rating in addition to the per-source ratings and 9.6? The current distinction is explicit but its usefulness is untested.
- Do 6.2.6 and 11.1.2 work as distinct judgments in practice? One asks about available documentation, the other about the fairness work it describes.
- The scorecard omits 9.3, including model-based scorer checks. A reviewer must consult the full template when that omission matters. Equivalence of the two forms has not been established.
- Decisions to keep items are based on their different intended purposes, not observed human completion times.

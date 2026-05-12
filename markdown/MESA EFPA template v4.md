# MESA EFPA Template v4

This template adapts EFPA Test Review Model 2025 Parts A and B for AI benchmark review. Part A describes the benchmark as a measurement instrument. Part B evaluates how well the benchmark supports its stated interpretation using EFPA-style `n/a` and `0`-`4` ratings with AI-specific evidence anchors.

Keep the boundary explicit: Part A records what the available sources state and marks missing documentation; Part B contains reviewer judgments, each tied to evidence, missing evidence, rationale, and interpretation caution.

Use `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md` as the source structure, `markdown/MESA EFPA adaptation map.md` as the adaptation rationale, and `markdown/MESA Part B literature synthesis.md` as the local synthesis for Part B.

## Information Sources

Record the sources used for this review. Prefer official benchmark materials before independent commentary.

| Source type | Source details | Access date | Notes |
| :--- | :--- | :--- | :--- |
| Official paper or technical report |  |  |  |
| Benchmark website |  |  |  |
| Repository |  |  |  |
| Dataset card or data host |  |  |  |
| Leaderboard or results page |  |  |  |
| Evaluation harness or package |  |  |  |
| Documentation or user guide |  |  |  |
| Release notes or changelog |  |  |  |
| Maintainer statements |  |  |  |
| Independent sources used for context |  |  |  |

Documentation status options used throughout:

- [ ] Documented
- [ ] Partially documented
- [ ] Not documented
- [ ] Not applicable
- [ ] Unclear from available sources

Part B rating scale:

| Rating | Meaning |
| :--- | :--- |
| `n/a` | Criterion is not applicable to this benchmark or intended use. |
| `0` | Cannot rate because the available evidence is insufficient. |
| `1` | Inadequate evidence or practice for the intended interpretation. |
| `2` | Adequate for cautious use within a clearly bounded interpretation. |
| `3` | Good evidence or practice, with meaningful but non-fatal gaps. |
| `4` | Excellent evidence or practice, comprehensive and well matched to the intended use. |

Each Part B rating must include evidence, missing evidence, reviewer rationale, and interpretation caution. Do not mechanically average section ratings.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Information

| Prompt | Response |
| :--- | :--- |
| Reviewer |  |
| Date of current review |  |
| Date of previous review, if applicable |  |
| Review scope |  |
| Sources reviewed |  |

### 1.2 Benchmark Information

| Prompt | Response |
| :--- | :--- |
| Benchmark name |  |
| Short name or acronym |  |
| Benchmark version, edition, or release |  |
| Original benchmark name, if this is an adaptation |  |
| Benchmark creators or authors |  |
| Current maintainers |  |
| Host organization, publisher, or distributor |  |
| Date of original release |  |
| Date of current release or revision |  |
| License or access terms |  |
| Persistent identifier, citation, or DOI |  |

### 1.3 Public Artifacts

| Artifact | URL or location | Access status | Notes |
| :--- | :--- | :--- | :--- |
| Paper or technical report |  |  |  |
| Benchmark website |  |  |  |
| Code repository |  |  |  |
| Evaluation harness |  |  |  |
| Dataset or task set |  |  |  |
| Prompt set |  |  |  |
| Rubric or scoring guide |  |  |  |
| Leaderboard |  |  |  |
| Changelog or release notes |  |  |  |
| Contact or issue channel |  |  |  |

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

Specify what the benchmark claims to measure using up to five keywords. Select all that apply.

- [ ] Not explicitly stated
- [ ] General capability or intelligence
- [ ] Reasoning
- [ ] Knowledge
- [ ] Language understanding
- [ ] Writing or generation quality
- [ ] Mathematics
- [ ] Coding or software engineering
- [ ] Scientific or technical expertise
- [ ] Domain-specific professional expertise
- [ ] Multimodal perception
- [ ] Audio or speech
- [ ] Video understanding
- [ ] Tool use
- [ ] Planning or agency
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [ ] Calibration or uncertainty
- [ ] Other:

Reviewer notes:

### 2.2 Area of Use

Select all documented use contexts.

- [ ] Not explicitly stated
- [ ] Model comparison
- [ ] Leaderboard ranking
- [ ] Capability profiling
- [ ] Research diagnostics
- [ ] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison
- [ ] Internal regression testing
- [ ] Public communication or marketing
- [ ] Policy or governance analysis
- [ ] Other:

Reviewer notes:

### 2.3 Intended AI Systems

Only record systems stated or clearly implied by benchmark documentation.

- [ ] Not explicitly stated
- [ ] Frontier general-purpose language models
- [ ] Chat or instruction-following models
- [ ] Base language models
- [ ] Code models
- [ ] Multimodal models
- [ ] Audio or speech models
- [ ] Agentic systems
- [ ] Tool-using systems
- [ ] Retrieval-augmented systems
- [ ] Domain-specialized models
- [ ] Open-weight local models
- [ ] API-hosted models
- [ ] Other:

Free text description:

### 2.4 Intended Users of Benchmark Outputs

Select all that apply.

- [ ] Not explicitly stated
- [ ] Benchmark creators or maintainers
- [ ] AI researchers
- [ ] Model developers
- [ ] Product teams
- [ ] Safety evaluators
- [ ] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [ ] Educators or academic reviewers
- [ ] Public leaderboard users
- [ ] Other:

Reviewer notes:

### 2.5 Task Families, Subdomains, and Scores

Describe the number and meaning of task families, subdomains, splits, score families, aggregate metrics, subscores, or derived outputs.

| Component | Description | Source |
| :--- | :--- | :--- |
| Claimed construct or phenomenon |  |  |
| Construct subcomponents |  |  |
| Task families or subdomains |  |  |
| Task sampling or selection logic |  |  |
| Splits or partitions |  |  |
| Primary score |  |  |
| Subscores |  |  |
| Derived or aggregate scores |  |  |
| Qualitative labels or bands |  |  |
| Claim boundaries or caveats |  |  |

### 2.6 Model Response Mode

Select all that apply.

- [ ] Not explicitly stated
- [ ] Multiple choice
- [ ] Short text
- [ ] Long-form text
- [ ] Structured output, such as JSON or XML
- [ ] Code
- [ ] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or artifact generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment
- [ ] Other:

Required output format, if any:

### 2.7 Prerequisites for Evaluated Systems

Classify each requirement based on benchmark documentation.

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Language support | - [ ] | - [ ] | - [ ] |  |
| Context length | - [ ] | - [ ] | - [ ] |  |
| Multimodal input support | - [ ] | - [ ] | - [ ] |  |
| Structured output support | - [ ] | - [ ] | - [ ] |  |
| Tool access | - [ ] | - [ ] | - [ ] |  |
| Browser or internet access | - [ ] | - [ ] | - [ ] |  |
| Code execution | - [ ] | - [ ] | - [ ] |  |
| Memory or persistent state | - [ ] | - [ ] | - [ ] |  |
| API compatibility | - [ ] | - [ ] | - [ ] |  |
| Latency or time budget | - [ ] | - [ ] | - [ ] |  |
| Cost or compute budget | - [ ] | - [ ] | - [ ] |  |

Other requirements:

### 2.8 Evaluation Conditions

Describe the conditions required to run the benchmark as intended.

| Condition | Description | Source |
| :--- | :--- | :--- |
| Prompting protocol |  |  |
| System prompt |  |  |
| Few-shot examples |  |  |
| Sampling settings |  |  |
| Tool permissions |  |  |
| Time limits |  |  |
| Human intervention rules |  |  |
| Hardware or hosted service |  |  |
| Network requirements |  |  |
| Sandbox or security constraints |  |  |
| Other special conditions |  |  |

### 2.9 Task and Response Types

Select all that apply.

Selection-based responses:

- [ ] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [ ] Ranking
- [ ] Classification
- [ ] Pairwise preference

Production-based responses:

- [ ] Open-ended text
- [ ] Code generation
- [ ] Proof, derivation, or explanation
- [ ] Structured data
- [ ] Generated media
- [ ] Artifact production

Interaction-based responses:

- [ ] Tool use
- [ ] Browser or web navigation
- [ ] API interaction
- [ ] Computer-use interaction
- [ ] Simulated environment task
- [ ] Real or external environment task

Process data:

- [ ] Response latency
- [ ] Token usage
- [ ] Cost
- [ ] Tool traces
- [ ] Intermediate reasoning traces
- [ ] Execution logs
- [ ] Other:

### 2.10 Input Stimulus Type

Select all that apply.

- [ ] Not explicitly stated
- [ ] Text
- [ ] Code
- [ ] Tables or structured data
- [ ] Images
- [ ] Audio
- [ ] Video
- [ ] Documents
- [ ] Web pages
- [ ] APIs or tools
- [ ] Dynamic environment
- [ ] Other:

### 2.11 Number of Items or Measurement Points

Where the benchmark is dynamic, record minimum, maximum, and typical task counts.

| Prompt | Response |
| :--- | :--- |
| Total public items or tasks |  |
| Total private or hidden items |  |
| Development or example items |  |
| Test items |  |
| Dynamic or generated tasks |  |
| Episodes, trials, or measurement points |  |
| Notes on item count uncertainty |  |

### 2.12 Mode of Evaluation

Select all that apply.

- [ ] Not indicated
- [ ] Local batch evaluation
- [ ] Hosted benchmark platform
- [ ] Leaderboard submission
- [ ] Private controlled evaluation
- [ ] Public open evaluation
- [ ] Interactive agent evaluation
- [ ] Human-in-the-loop evaluation
- [ ] Continuous or rolling evaluation
- [ ] Other:

Identity and condition controls:

- [ ] No control over submitted systems
- [ ] Some control over submitted systems
- [ ] Controlled model access or audit
- [ ] Controlled evaluation center or private harness
- [ ] Not documented

### 2.13 Technological Arrangements

Mark A for available and R for required where documentation permits.

| Technology | A | R | Notes |
| :--- | :---: | :---: | :--- |
| API access | - [ ] | - [ ] |  |
| Local inference | - [ ] | - [ ] |  |
| GPU | - [ ] | - [ ] |  |
| CPU-only execution | - [ ] | - [ ] |  |
| Docker or container | - [ ] | - [ ] |  |
| Python package or CLI | - [ ] | - [ ] |  |
| Browser | - [ ] | - [ ] |  |
| External tools | - [ ] | - [ ] |  |
| Internet access | - [ ] | - [ ] |  |
| Proprietary platform | - [ ] | - [ ] |  |
| Other | - [ ] | - [ ] |  |

### 2.14 Time and Resource Requirements

Record documented estimates. Mark missing if not stated.

| Activity | Time, compute, or cost estimate | Source |
| :--- | :--- | :--- |
| Setup |  |  |
| Model inference or task completion |  |  |
| Scoring |  |  |
| Human adjudication |  |  |
| Analysis or reporting |  |  |
| Full benchmark run |  |  |
| API or compute cost |  |  |

### 2.15 Benchmark Forms, Versions, and Variants

Describe public/private forms, alternate forms, short forms, language variants, domain subsets, and deprecated versions.

| Form or variant | Purpose | Equivalence claim | Status | Source |
| :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |

### 2.16 Static or Dynamic Task Determination

Select all that apply.

- [ ] Static fixed task set
- [ ] Random sample from fixed pool
- [ ] Hidden test set selected by maintainers
- [ ] Procedurally generated tasks
- [ ] Adaptive routing based on performance
- [ ] Dynamic environment generation
- [ ] Rolling or periodically refreshed task set
- [ ] Not explicitly stated
- [ ] Other:

Describe task selection method:

### 2.17 Evidence Sources Used in Scoring

Select all that apply.

- [ ] Model final answer
- [ ] Model intermediate trace
- [ ] Tool-use trace
- [ ] Code execution result
- [ ] Environment state
- [ ] Reference answer
- [ ] Unit test
- [ ] Human judge
- [ ] Model judge
- [ ] Ensemble or panel adjudication
- [ ] External verifier
- [ ] Other:

Reviewer notes:

### 2.18 Broad Claim and CHC/AGI Cautions

Complete this descriptive screen when the benchmark title, paper, website, or leaderboard uses terms such as intelligence, general intelligence, AGI, reasoning, agency, autonomy, broad capability, expert capability, or cross-domain competence.

| Prompt | Response | Source |
| :--- | :--- | :--- |
| Broad claim term used |  |  |
| Claimed breadth across domains |  |  |
| Claimed depth or proficiency level |  |  |
| Sub-abilities explicitly covered |  |  |
| Sub-abilities explicitly excluded or not tested |  |  |
| Evidence across modalities, tools, memory, planning, or speed |  |  |
| Stated AGI, autonomy, or agency caveats |  |  |
| Relation to CHC-like broad/narrow abilities, if claimed |  |  |
| Descriptive caution for Part B |  |  |

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

Select all that apply.

- [ ] Not explicitly stated
- [ ] Automated exact-match scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] Unit-test or execution-based scoring
- [ ] Rule-based scoring
- [ ] Human rating
- [ ] Model-as-judge scoring
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [ ] Leaderboard service scoring
- [ ] Manual adjudication
- [ ] Other:

Describe the scoring pipeline:

### 3.2 Scores and Metrics

Briefly describe how global and partial scores are produced.

| Score or metric | Definition | Aggregation | Interpretation stated by authors |
| :--- | :--- | :--- | :--- |
| Primary score |  |  |  |
| Subscore |  |  |  |
| Derived score |  |  |  |
| Qualitative band |  |  |  |

Treatment of invalid, missing, malformed, or refused responses:

### 3.3 Scale or Metric Types

Select all that apply.

- [ ] Raw score
- [ ] Accuracy
- [ ] Success rate
- [ ] Pass rate or pass@k
- [ ] Unit-test pass rate
- [ ] Win rate
- [ ] Elo or ranking score
- [ ] Pairwise preference score
- [ ] Reward or return
- [ ] Cost-adjusted score
- [ ] Calibration or uncertainty score
- [ ] Percentile or normalized score
- [ ] Threshold or decision index
- [ ] Other:

### 3.4 Score Transformation

Select all that apply.

- [ ] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against baseline
- [ ] Weighting across subdomains
- [ ] Aggregation formula documented
- [ ] Aggregation formula partially documented
- [ ] Aggregation formula not documented
- [ ] Not applicable

Formula or transformation notes:

### 3.5 Reference Groups, Baselines, and Comparators

Select all that apply.

- [ ] No baseline or comparator documented
- [ ] Random or chance baseline
- [ ] Human baseline
- [ ] Expert human baseline
- [ ] Model baseline
- [ ] Previous model cohort
- [ ] Commercial system comparator
- [ ] Open-weight model comparator
- [ ] Domain-specific reference group
- [ ] Other:

Describe comparator construction and source:

| Comparator or baseline | Construction method | Intended interpretation | Source |
| :--- | :--- | :--- | :--- |
| Random or chance baseline |  |  |  |
| Human baseline |  |  |  |
| Expert baseline |  |  |  |
| Model cohort |  |  |  |
| Prior benchmark or version |  |  |  |
| Criterion threshold or floor/ceiling |  |  |  |

### 3.6 Score Uncertainty and Stability

This remains descriptive in Part A. Record whether uncertainty or run-to-run stability is reported.

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [ ] Sensitivity analyses
- [ ] Not reported
- [ ] Other:

Notes:

### 3.7 Metric-to-Claim Linkage

This remains descriptive in Part A. Record the documented link between metric behavior and benchmark claims.

| Prompt | Response | Source |
| :--- | :--- | :--- |
| Why the primary metric was chosen |  |  |
| Whether metric floors or ceilings are documented |  |  |
| Whether the metric may reward non-target behavior named by the source |  |  |
| Whether parsing, judge, or scorer validation is documented |  |  |
| Whether score uncertainty affects claim interpretation |  |  |
| Whether score differences are interpreted statistically |  |  |
| Whether benchmark reports state what users should not infer |  |  |

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [ ] Public leaderboard available
- [ ] Public aggregate scores available
- [ ] Public per-domain scores available
- [ ] Public per-item scores available
- [ ] Public raw model outputs available
- [ ] Public traces or logs available
- [ ] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

### 4.2 Output Name or Description

| Output | Description | Public/private | Source |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

### 4.3 Output Design or Presentation

Select all that apply.

- [ ] Static text report
- [ ] Tables
- [ ] Graphs or visualizations
- [ ] Leaderboard
- [ ] Interactive dashboard
- [ ] Downloadable CSV or JSON
- [ ] API output
- [ ] Paper-only results
- [ ] Other:

### 4.4 Output Structure

Select all that apply.

- [ ] Aggregate-score based
- [ ] Capability-domain based
- [ ] Task-family based
- [ ] Criterion-threshold based
- [ ] Pairwise-comparison based
- [ ] Rank based
- [ ] Cost or efficiency adjusted
- [ ] Error-analysis based
- [ ] Trace or process based
- [ ] Other:

### 4.5 Sensitivity to Context

Select one.

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [ ] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts:

### 4.6 Development of Outputs

Select all that apply.

- [ ] Based on benchmark authors' design
- [ ] Based on empirical or actuarial relationships
- [ ] Based on expert judgment
- [ ] Based on human annotation
- [ ] Based on model-as-judge outputs
- [ ] Automatically generated by benchmark platform
- [ ] Other:

Describe source of report content:

### 4.7 Modifiability

Select one.

- [ ] Not modifiable
- [ ] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

### 4.8 Transparency

Select one.

- [ ] Clear linkage between tasks, scores, and reported claims
- [ ] Partial linkage between tasks, scores, and reported claims
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Notes:

### 4.9 Output Content

Select all that apply.

- [ ] Capability descriptions
- [ ] Aggregate rankings
- [ ] Subdomain comparisons
- [ ] Error categories
- [ ] Examples of successes or failures
- [ ] Cost, latency, or efficiency data
- [ ] Process traces
- [ ] Recommendations or interpretation notes
- [ ] Warnings or caveats
- [ ] Other:

### 4.10 Intended Recipients

Select all that apply.

- [ ] Benchmark maintainers
- [ ] Model developers
- [ ] AI researchers
- [ ] Safety evaluators
- [ ] Policy or governance actors
- [ ] Product or deployment teams
- [ ] Procurement teams
- [ ] Public audience
- [ ] Other:

---

## Section 5. Supply Arrangements and Materials

### 5.1 Supporting Information Provided

Select all that apply.

- [ ] Technical report
- [ ] User guide
- [ ] Repository README
- [ ] API documentation
- [ ] Dataset card
- [ ] Model submission instructions
- [ ] Scoring documentation
- [ ] Rubric or annotation guide
- [ ] Evaluation examples
- [ ] FAQ or discussion forum
- [ ] Changelog or release notes
- [ ] Other:

### 5.2 Methods of Publication

Select all that apply.

- [ ] Academic paper
- [ ] Benchmark website
- [ ] Git repository
- [ ] Package registry
- [ ] Dataset hosting platform
- [ ] Leaderboard platform
- [ ] Downloadable documents
- [ ] Private distribution
- [ ] Other:

### 5.3 User Requirements or Qualifications

Describe any requirements specified for running, submitting to, or interpreting the benchmark.

| Requirement type | Requirement | Source |
| :--- | :--- | :--- |
| Technical expertise |  |  |
| Compute or infrastructure |  |  |
| Account or access approval |  |  |
| Legal or license terms |  |  |
| Cost or fee |  |  |
| Security or privacy requirements |  |  |
| Other |  |  |

### 5.4 Dataset and Item Access

| Component | Public | Restricted | Hidden | Not available | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Training or example data | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Development set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Test set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Private holdout set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Prompt templates | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Reference answers | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Rubrics | - [ ] | - [ ] | - [ ] | - [ ] |  |

### 5.5 Provenance and Contamination Documentation

This section records documentation only. It does not evaluate adequacy.

| Topic | Documented | Partially documented | Not documented | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Data source provenance | - [ ] | - [ ] | - [ ] |  |
| Collection procedure | - [ ] | - [ ] | - [ ] |  |
| Filtering or quality control | - [ ] | - [ ] | - [ ] |  |
| Licensing or rights | - [ ] | - [ ] | - [ ] |  |
| Deduplication | - [ ] | - [ ] | - [ ] |  |
| Contamination controls | - [ ] | - [ ] | - [ ] |  |
| Searchability or source-exposure checks | - [ ] | - [ ] | - [ ] |  |
| Canary, GUID, encryption, or anti-scraping method | - [ ] | - [ ] | - [ ] |  |
| Training-on-test diagnostic task | - [ ] | - [ ] | - [ ] |  |
| Public/private split rationale | - [ ] | - [ ] | - [ ] |  |
| Update or refresh policy | - [ ] | - [ ] | - [ ] |  |
| Release rules or anti-gaming terms | - [ ] | - [ ] | - [ ] |  |

### 5.6 Reproducibility Materials

Select all that are available.

- [ ] Complete evaluation code
- [ ] Scoring scripts
- [ ] Environment file or dependency list
- [ ] Container or reproducible runtime
- [ ] Prompt templates
- [ ] Example submissions
- [ ] Raw outputs from reported models
- [ ] Random seeds
- [ ] Configuration files
- [ ] Expected outputs or tests
- [ ] Result replication script
- [ ] Build status or continuous integration check
- [ ] None documented

Access or setup notes:

### 5.7 Maintenance and Versioning

| Prompt | Response |
| :--- | :--- |
| Current maintenance status |  |
| Latest documented release |  |
| Changelog available |  |
| Versioning scheme |  |
| Deprecated versions |  |
| Issue tracker or feedback channel |  |
| Response policy for user feedback |  |
| Known planned updates |  |
| Retirement or archival plan |  |
| Archival status |  |

---

## Appendix A. General Description of the Benchmark

Provide a concise non-evaluative description of the benchmark. Describe what the benchmark claims to be, what capability areas it covers, what systems it is intended to evaluate, how it is administered, how it is scored, what outputs it produces, what materials are available, and what versions or variants are in scope. Note major documentation gaps without turning them into evaluative criticism.

Suggested length: 200 to 600 words, depending on benchmark complexity.

Draft:

---

## Appendix B. EFPA-to-MESA Adaptation Notes

Use this section to document any adaptation decisions that matter for this review.

| EFPA concept | MESA adaptation used in this review | Rationale |
| :--- | :--- | :--- |
| Instrument | Benchmark | AI benchmarks function as instruments that produce measurements or rankings of AI systems. |
| Test taker | AI system under evaluation | The evaluated entity is a model, agent, or AI system rather than a person. |
| Test user | Benchmark output user | The consumer of scores may be a researcher, developer, policy actor, product team, or public audience. |
| Administration | Evaluation protocol | Benchmark behavior depends on prompts, settings, tools, infrastructure, and submission conditions. |
| Scales and scores | Metrics, subscores, and aggregate indices | AI benchmarks often report accuracy, pass rates, rankings, or task-family scores instead of psychometric scales. |
| Norms | Baselines, comparators, or reference groups | AI benchmarks may compare models to humans, experts, prior models, chance, or other system cohorts. |
| Reports | Leaderboards, scorecards, dashboards, traces, or paper tables | Benchmark outputs often appear as public rankings or structured result artifacts. |
| Test materials | Dataset, prompts, rubrics, code, harness, and documentation | Review requires access to benchmark implementation and data artifacts. |

Additional notes:

---

## Appendix C. Part B Evidence Preparation Notes

Use this section to summarize issues from Part A before assigning Part B ratings. Do not assign ratings here; use it as the bridge from descriptive facts to evaluative evidence.

| Part B area | Part A evidence available | Missing evidence | Source fields |
| :--- | :--- | :--- | :--- |
| Construct validity |  |  |  |
| Task or item quality |  |  |  |
| Scoring validity |  |  |  |
| Reliability or run stability |  |  |  |
| Baselines and comparators |  |  |  |
| Fairness or comparability |  |  |  |
| Reproducibility |  |  |  |
| Contamination and gameability |  |  |  |
| Maintenance and benchmark drift |  |  |  |
| Interpretation limits |  |  |  |
| Leaderboard or public-claim risk |  |  |  |
| Other |  |  |  |

---

# Part B. Evaluation of the Benchmark

Part B evaluates how well the benchmark supports its stated purpose and score interpretation. Use Part A evidence as the factual base. Add outside literature only when needed to interpret benchmark-quality criteria, and cite it in the evidence fields.

For every rating, complete all four evidence fields:

- Evidence used
- Missing evidence
- Reviewer rationale
- Interpretation caution

Do not treat missing documentation as proof of poor benchmark quality. Treat it as an evidence gap unless there is source-grounded evidence of a defect.

## Part B Information Sources

| Source type | Source details | Used for | Notes |
| :--- | :--- | :--- | :--- |
| Part A evidence |  |  |  |
| EFPA Part B source | `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md` |  |  |
| BetterBench | `markdown/Papers/betterbench.md` |  |  |
| Measuring what Matters | `markdown/Papers/Measuring_what_Matters.md` |  |  |
| AGI/CHC source | `markdown/Papers/A_Definition_of_AGI.md` |  |  |
| Benchmark-specific sources |  |  |  |
| Other local sources |  |  |  |

## Rating Record Template

Use this table format for additional item-level ratings when needed.

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |

---

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

MESA adaptation: evaluate whether the benchmark explains what it is designed to measure, why the task and metric are appropriate, how task or item content was developed, and whether documentation supports qualified use.

### 6.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Rationale and construct definition | No usable evidence about the target phenomenon or purpose. | Purpose is vague, overbroad, or disconnected from the task. | Target phenomenon is named and bounded enough for cautious interpretation. | Clear operational definition with source-grounded rationale and stated limits. | Comprehensive, literature-grounded definition with subcomponents, exclusions, and intended uses clearly linked to score interpretation. |
| Phenomenon-task-metric-claim chain | No evidence connecting claim, task, metric, and interpretation. | Chain is implicit or contains obvious unsupported leaps. | Basic chain is documented but important assumptions remain. | Chain is explicit, with trade-offs and likely confounders discussed. | Chain is explicit, empirically supported, and includes safeguards against construct-irrelevant variance. |
| Task/item development quality | No evidence about task or item development. | Development process is weak, undocumented, or lacks relevant expertise. | Development process includes basic review, criteria, and item/task rationale. | Strong process with domain expertise, documented criteria, and quality checks. | Comprehensive process with expert review, quantitative or structured item evidence, representative sampling, and revision history. |
| Documentation and procedural instructions | No usable documentation. | Documentation is too incomplete for qualified use. | Core documentation supports cautious use, with notable gaps. | Documentation is clear, structured, and covers most setup, scoring, interpretation, and limitation needs. | Documentation is comprehensive, current, source-linked, and sufficient for independent qualified use. |

### 6.2 Section 6 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 6.1 Rationale and construct definition |  |  |  |  |  |
| 6.2 Phenomenon-task-metric-claim chain |  |  |  |  |  |
| 6.3 Development process and task/item quality |  |  |  |  |  |
| 6.4 Documentation available to users |  |  |  |  |  |
| 6.5 Procedural instructions for administration, scoring, and interpretation |  |  |  |  |  |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality |  |  |  |  |  |

Reviewer comments on Section 6:

---

## Section 7. Quality of Benchmark Materials and Usability

MESA adaptation: evaluate the quality, accessibility, and usability of benchmark materials, including datasets, prompts, rubrics, harnesses, scoring code, interfaces, documentation, and setup paths.

### 7.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Materials availability | No usable information about materials. | Key materials are missing or inaccessible for stated use. | Core materials are available or described, but replication requires additional information. | Most materials are available with clear access notes and restrictions. | Complete materials are available, versioned, licensed, and linked to documentation. |
| Evaluation harness and scoring tools | No evidence of executable harness or scorer. | Harness/scorer is absent, opaque, or unusable for intended users. | Basic scoring path is documented, but some implementation details are missing. | Runnable harness or scorer is available with clear setup and examples. | Harness is robust, tested, documented, supports expected model access modes, and includes reproducibility checks. |
| Prompts, rubrics, and response formats | No prompts, rubrics, or response requirements are documented. | Instructions or rubrics are ambiguous or impose unsupported format burdens. | Core prompts and rubrics are documented with some gaps. | Instructions, rubrics, and format handling are clear and mostly validated. | Prompts, rubrics, parsers, and format constraints are fully documented, validated, and tested for construct-irrelevant effects. |
| Accessibility and usability | No usability information. | Materials are difficult to use or exclude relevant systems without justification. | Usable by skilled reviewers with documented constraints. | Good usability with quick starts, dependencies, and support paths. | Excellent usability across relevant model types and user contexts, including accessibility and support. |

### 7.2 Section 7 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 7.1 Dataset, task set, or environment availability |  |  |  |  |  |
| 7.2 Prompts, instructions, rubrics, and response format |  |  |  |  |  |
| 7.3 Evaluation harness, scorer, and implementation usability |  |  |  |  |  |
| 7.4 Accessibility across relevant modalities, languages, and system types |  |  |  |  |  |
| 7.5 Licensing, usage requirements, and sensitive-content warnings |  |  |  |  |  |
| 7.6 Overall quality of benchmark materials |  |  |  |  |  |

Reviewer comments on Section 7:

---

## Section 8. Baselines, Comparators, and Reference Interpretation

MESA adaptation: adapt EFPA norms to AI benchmark baselines, comparator groups, human or expert reference levels, chance/random floors, model cohorts, ceilings, and criterion thresholds.

### 8.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline construction | No baseline information. | Baselines are absent, inappropriate, or unsupported. | Basic baselines are documented and usable with caution. | Baselines are meaningful, described, and relevant to intended interpretation. | Baselines are comprehensive, representative, uncertainty-aware, and tied to score interpretation. |
| Human/expert comparators | No evidence. | Human or expert claims are made without method. | Human/expert comparison is described but limited. | Comparator selection, qualifications, and procedures are well documented. | Human/expert comparator evidence is rigorous, representative, and supports the stated interpretation. |
| Model comparators | No model comparison evidence. | Model cohort is cherry-picked or poorly specified. | Model comparisons are documented but limited in version or condition detail. | Model cohort, versions, and conditions are well specified. | Model comparisons are comprehensive, current for review date, uncertainty-aware, and clearly bounded. |
| Floors, ceilings, thresholds | No evidence. | Score floors, ceilings, chance levels, or thresholds are ignored despite relevance. | Some floors, ceilings, or thresholds are documented. | Relevant floors, ceilings, thresholds, and saturation risks are explained. | Floors, ceilings, thresholds, and saturation/refresh policies are empirically supported and integrated into interpretation. |

### 8.2 Section 8 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 8.1 Random, chance, floor, and ceiling baselines |  |  |  |  |  |
| 8.2 Human or expert baselines |  |  |  |  |  |
| 8.3 Model comparator cohort |  |  |  |  |  |
| 8.4 Criterion thresholds or score bands |  |  |  |  |  |
| 8.5 Overall adequacy of baselines and reference interpretation |  |  |  |  |  |

Reviewer comments on Section 8:

---

## Section 9. Reliability, Precision, and Score Stability

MESA adaptation: evaluate whether scores are stable and precise enough for the intended use across runs, prompts, seeds, raters, judges, scorers, benchmark forms, versions, and model-access conditions.

### 9.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Run stability and uncertainty | No stability or uncertainty information. | Known stochasticity is not addressed or only anecdotal evidence is provided. | Some uncertainty, repeat-run, or deterministic-condition evidence is provided. | Stability is assessed across relevant settings with useful uncertainty reporting. | Comprehensive stability evidence supports all main score interpretations and comparisons. |
| Scorer, judge, or rater reliability | No scoring reliability evidence. | Judgmental scoring is used without validation or agreement evidence. | Basic validation or agreement evidence is provided. | Strong validation of scorers, judges, raters, parsers, or adjudication rules. | Comprehensive reliability evidence across domains, formats, raters/judges, and edge cases. |
| Form, version, and prompt stability | No evidence. | Alternate forms, versions, or prompts are mixed without equivalence evidence. | Basic version or prompt conditions are documented. | Stability or equivalence is tested for important forms, prompts, or versions. | Strong equivalence and drift evidence supports comparisons across forms, prompts, and time. |
| Statistical comparison quality | No evidence. | Model differences are reported without uncertainty where it matters. | Some statistical or variance information is available. | Model comparisons include uncertainty or significance methods. | Comparisons are uncertainty-aware, statistically justified, and matched to intended claims. |

### 9.2 Section 9 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 9.1 Run-to-run stability, seeds, and sampling settings |  |  |  |  |  |
| 9.2 Score uncertainty, confidence intervals, or standard errors |  |  |  |  |  |
| 9.3 Human rater, scorer, parser, or model-judge agreement |  |  |  |  |  |
| 9.4 Prompt, form, version, and environment stability |  |  |  |  |  |
| 9.5 Overall reliability and precision |  |  |  |  |  |

Reviewer comments on Section 9:

---

## Section 10. Validity Evidence

MESA adaptation: evaluate whether the evidence supports the intended score interpretation. The central MESA validity question is whether the phenomenon-task-metric-claim chain is justified.

### 10.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Content and representativeness | No evidence about content coverage or task sampling. | Task sample is poorly justified for the claim. | Content coverage is plausible and partly documented. | Content evidence is strong, with expert input and stated coverage limits. | Content evidence is comprehensive, representative, and empirically or systematically justified. |
| Metric and scoring validity | No evidence about metric fit. | Metric likely rewards construct-irrelevant behavior or is opaque. | Metric is plausible and documented but has unresolved confounds. | Metric choice is justified and known confounds are tested or mitigated. | Metric, scorer, aggregation, and interpretation are validated against the intended construct. |
| Relations with other evidence | No convergent, discriminant, criterion, or real-world evidence. | Comparisons are absent or misleading. | Some relevant comparisons or criteria are provided. | Comparisons and criteria are meaningful and interpreted cautiously. | Strong convergent, discriminant, criterion, or ecological evidence supports the intended claim. |
| Contamination and gameability | No evidence. | Contamination or gameability risks are ignored despite relevance. | Basic controls or caveats are documented. | Strong controls, audits, private splits, canaries, or release rules are used. | Comprehensive contamination/gameability strategy supports ongoing valid interpretation. |
| Claim proportionality, including AGI/agency | No evidence connecting claim breadth to measurement breadth. | Claims exceed task, metric, or evidence. | Claims are mostly bounded, with caveats for broad interpretations. | Claims are well bounded and broad-claim cautions are explicit. | Claims are fully proportional to evidence, with broad intelligence or AGI claims supported across relevant sub-abilities or explicitly rejected. |

### 10.2 Section 10 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 10.1 Content validity and task representativeness |  |  |  |  |  |
| 10.2 Internal structure, subscores, or dimensionality |  |  |  |  |  |
| 10.3 Metric, scorer, and aggregation validity |  |  |  |  |  |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings |  |  |  |  |  |
| 10.5 Contamination, leakage, and gameability controls |  |  |  |  |  |
| 10.6 Claim proportionality and broad-capability cautions |  |  |  |  |  |
| 10.7 Overall validity evidence |  |  |  |  |  |

Reviewer comments on Section 10:

---

## Section 11. Fair Use, Comparability, and Appropriate Use

MESA adaptation: evaluate whether benchmark use and interpretation are fair and comparable across relevant systems, modalities, domains, languages, access modes, and user contexts.

### 11.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cross-system comparability | No evidence about comparable conditions. | Comparisons are likely unfair or conditions are unclear. | Core conditions are documented enough for cautious comparison. | Conditions are well specified and important differences are handled. | Comparability is actively supported across relevant system classes and access modes. |
| Domain, language, modality, and subgroup coverage | No evidence. | Coverage gaps are ignored despite relevance. | Coverage and major limitations are documented. | Coverage is analyzed and limitations are tied to interpretation. | Coverage evidence supports fair interpretation across relevant domains, languages, modalities, and subgroups. |
| Access, compute, and usability fairness | No evidence. | Access or compute requirements distort use without warning. | Requirements are documented, with some comparability caveats. | Requirements and constraints are clear and usable for intended users. | Access paths are inclusive for intended users and support fair replication/comparison. |
| Appropriate-use guidance | No guidance. | Public use guidance invites overinterpretation. | Basic intended-use and non-use guidance is available. | Guidance is clear, prominent, and tied to evidence limits. | Guidance comprehensively prevents foreseeable misuse and supports responsible interpretation. |

### 11.2 Section 11 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 11.1 Cross-system and evaluation-condition comparability |  |  |  |  |  |
| 11.2 Domain, language, modality, and subgroup fairness |  |  |  |  |  |
| 11.3 Access, compute, tooling, and API/local comparability |  |  |  |  |  |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance |  |  |  |  |  |
| 11.5 Overall fair use and comparability |  |  |  |  |  |

Reviewer comments on Section 11:

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

MESA adaptation: evaluate benchmark outputs as reports: paper tables, scorecards, dashboards, leaderboards, downloadable results, raw traces, public claims, and score interpretations.

### 12.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Report scope and granularity | No report information. | Reports omit essential scores or overstate unsupported detail. | Reports provide core scores with limited granularity. | Reports provide useful aggregate and subscore detail matched to claims. | Reports provide comprehensive, interpretable, uncertainty-aware detail without overclaiming. |
| Leaderboard or dashboard quality | No leaderboard/dashboard evidence. | Rankings are opaque or unstable without caveats. | Basic ranking or result display is available. | Versioned, documented, and interpretable result display is available. | Result display is robust, versioned, reproducible, uncertainty-aware, and clear about update policies. |
| Report reliability and validity | No evidence linking reports to scores. | Reports or claims diverge from what scores support. | Reports are mostly linked to benchmark scores, with gaps. | Reports explain score-to-claim links and important limitations. | Reports clearly and consistently communicate defensible interpretations, uncertainty, and non-uses. |
| Public communication and acceptability | No evidence. | Public claims encourage overinterpretation. | Public claims include basic caveats. | Public claims are mostly proportional and audience-appropriate. | Public communication is transparent, cautious, accessible, and strongly aligned with evidence. |

### 12.2 Section 12 Ratings

| Criterion | Rating (`n/a`, `0`-`4`) | Evidence used | Missing evidence | Reviewer rationale | Interpretation caution |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 12.1 Report, leaderboard, dashboard, or result artifact scope |  |  |  |  |  |
| 12.2 Score granularity, uncertainty, and version labeling |  |  |  |  |  |
| 12.3 Linkage from scores to public claims |  |  |  |  |  |
| 12.4 Raw outputs, per-item data, or trace availability |  |  |  |  |  |
| 12.5 Overall quality of reports and public claims |  |  |  |  |  |

Reviewer comments on Section 12:

---

## Final Evaluation

### Evaluative Report of the Benchmark

Provide a concise, source-grounded judgment about the benchmark for its stated purpose. Identify strengths, evidence gaps, and appropriate-use limits. Do not mechanically average ratings; explain the judgment.

Draft:

### Conclusions

Summarize the quality of the benchmark as a measurement instrument, the uses it can support, the uses requiring caution, and the expertise needed to interpret it responsibly.

Draft:

### Recommendations

Provide source-grounded recommendations for benchmark users, benchmark maintainers, and future reviewers. Recommendations should follow from the evidence and ratings above without introducing new unsupported claims.

Draft:

### Summary of Ratings

| Section or area | Rating (`n/a`, `0`-`4`) | Reviewer comments |
| :--- | :---: | :--- |
| Section 6. Rationale, documentation, and task/item quality |  |  |
| Section 7. Benchmark materials and usability |  |  |
| Section 8. Baselines and comparators |  |  |
| Section 9. Reliability and precision |  |  |
| Section 10. Validity evidence |  |  |
| Section 11. Fair use and comparability |  |  |
| Section 12. Reports, leaderboards, and public claims |  |  |
| Construct definition and claim scope |  |  |
| Scoring validity |  |  |
| Reproducibility and implementation transparency |  |  |
| Contamination and gameability controls |  |  |
| Maintenance and versioning |  |  |
| Overall claim-bounded measurement quality |  |  |

Reviewer comments on Summary of Ratings:

### Reviewer Caution Statement

State the narrowest defensible interpretation of the benchmark scores, the main overclaim risks, and the conditions under which ratings should be revisited.

Draft:

---


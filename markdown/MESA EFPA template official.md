# MESA EFPA Template Official

## Introduction

MESA is a structured description and evaluation model for AI benchmarks treated as measurement instruments. It adapts the EFPA Test Review Model 2025 from human psychological and educational testing to AI benchmark review. It provides a structure for describing and evaluating AI benchmarks, task suites, leaderboards, evaluation harnesses that administer tasks and often run scoring, score reports, and benchmark materials needed to inspect, run, score, reproduce, or audit evaluations used in research, model development, safety evaluation, deployment governance, procurement, policy analysis, and public communication.

In MESA, an AI benchmark is treated as a structured measurement instrument: it samples the behavior of an AI system in a specified domain, then quantifies, scores, interprets, and reports that behavior through a standardized or documented process for evaluative or comparative conclusions. This includes benchmarks for language, reasoning, knowledge, coding, multimodality, tool use, agency, safety, robustness, calibration, domain expertise, or other capabilities or qualities the benchmark claims to measure.

Review information presented in this structure should support benchmark developers, maintainers, suppliers, platform hosts, evaluators, auditors, trainers, policy makers, model developers, procurement teams, and benchmark users. It should help improve benchmark design and evaluation practice, support standards for benchmark review, and give users a more authoritative, unbiased, and consistent basis for interpreting score-based benchmark claims.

This model is divided into two main review parts plus supporting appendices. Part A describes the benchmark in detail: what it is, what capability or quality it claims to measure, how it is administered and scored, what materials exist, and what inspectable or reproducible benchmark materials are available. Part B evaluates whether the benchmark supports the specific meaning users are supposed to draw from a score, using EFPA-style ratings translated for AI benchmark concerns such as evidence that scores support the intended capability interpretation, whether scoring rewards the target capability rather than irrelevant score effects, reproducibility, prior model exposure to benchmark items or answers, maintenance, fair comparison, and public reporting. The appendices and checklists support review discipline and template validation.

## How the MESA Model Should Be Used

Use this template as a review instrument, not as a scoring shortcut. Effective implementation depends on expert judgment, source-grounded interpretation, and careful separation between description and evaluation. Part A should remain descriptive: record facts, uncertainty, access limits, and documentation gaps without assigning quality ratings. Part B should remain evaluative: use Part A as the factual base, then judge adequacy for the benchmark's stated use.

This model is designed to guide reviewers, not to provide a closed set of rules. It should be adapted to the benchmark's domain, modality, evaluation setting, and scope of score interpretation while preserving the core review logic: first describe the benchmark as a measurement instrument, then evaluate whether the available evidence supports the specific meaning users are supposed to draw from a score. Missing documentation is missing or inaccessible information needed for interpretation, not automatic proof that the benchmark is poor. Do not mechanically average ratings; the final judgment should explain how the strongest support and most consequential gaps affect the intended score meaning.

MESA reviews evaluate benchmarks and the technical information supporting them. A completed MESA review does not imply endorsement, approval, or recommendation by MESA or by the reviewer unless this is stated explicitly. Public descriptions of a reviewed benchmark should not imply such endorsement; they should reference the review model and the evidence basis of the review.

Before completing the review, inspect the most authoritative available materials. Prefer official benchmark papers, websites, repositories, data hosts, leaderboards, harnesses, changelogs, and maintainer statements. Independent commentary should be used only for context, external critique, or disputed claims, and should not replace official benchmark facts.

### Figure 1. Structure of the MESA Review Model

```mermaid
flowchart TD

    %% Main Header
    Main("SECTION: MESA Review Process")

    %% Standalone Box for Short Description
    ShortDesc("Short stand-alone non-evaluative benchmark description")

    %% Left Side Group: Description of the Benchmark
    subgraph G_DESC ["Description of the benchmark"]
        direction TB
        A1("1. Factual description")
        A2("2. Classification")
        A3("3. Measurement and scoring")
        A4("4. Benchmark outputs and reports")
        A5("5. Benchmark access, artifacts, and lifecycle")
        AA("Appendix A. General description")

        %% Invisible links for vertical stacking
        A1 ~~~ A2
        A2 ~~~ A3
        A3 ~~~ A4
        A4 ~~~ A5
        A5 ~~~ AA
    end

    %% Right Side Group: Evaluation of the Benchmark
    subgraph G_EVAL ["Evaluation of the benchmark"]
        direction TB
        B6("6. Rationale, development,<br/>documentation, and task quality")
        B7("7. Benchmark artifacts<br/>and usability")
        B8("8. Baselines, comparators,<br/>and reference interpretation")
        B9("9. Reliability, precision,<br/>and score stability")
        B10("10. Validity evidence")
        B11("11. Fair use, comparability,<br/>and appropriate use")
        B12("12. Reports, leaderboards,<br/>dashboards, and public claims")

        %% Invisible links for vertical stacking
        B6 ~~~ B7
        B7 ~~~ B8
        B8 ~~~ B9
        B9 ~~~ B10
        B10 ~~~ B11
        B11 ~~~ B12
    end

    %% Bottom Box
    Final("Final evaluation")

    %% Layout positioning
    Main ~~~ ShortDesc
    Main ~~~ G_DESC
    Main ~~~ G_EVAL

    G_DESC ~~~ Final
    G_EVAL ~~~ Final

    %% Styling to match the EFPA figures
    style Main fill:#B0C4DE,color:#000,stroke:#D2691E,stroke-width:2px
    style Final fill:#B0C4DE,color:#000,stroke:#004771,stroke-width:2px
    style ShortDesc fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px

    %% Style for the internal list items
    classDef detail fill:#004771,color:#fff,stroke:#D2691E,stroke-dasharray: 5 5;
    class A1,A2,A3,A4,A5,AA,B6,B7,B8,B9,B10,B11,B12 detail;
```

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

Section 1 identifies the review event, the benchmark, and the public materials inspected. EFPA begins with factual identification of the instrument and the information available to reviewers. MESA keeps that function but moves the inventory of reviewed materials into this section so later descriptive and evaluative judgments can be traced to the review base.

### 1.1 Review Information

| Prompt                                 | Response |
| :------------------------------------- | :------- |
| Reviewer                               |          |
| Date of current review                 |          |
| Date of previous review, if applicable |          |
| Review scope                           |          |
| Review boundary                        |          |

Review notes:

### 1.2 Information Sources Reviewed

Record the materials inspected for this review. Include access dates and distinguish official benchmark materials from contextual literature. Use this inventory to support later review notes rather than adding citation columns to every table.

| Material type                                   | Artifact reviewed | Access date | Role in review |
| :---------------------------------------------- | :---------------- | :---------- | :------------- |
| Official paper or technical report              |                   |             |                |
| Benchmark website or documentation hub          |                   |             |                |
| Repository                                      |                   |             |                |
| Dataset card, data host, or task host           |                   |             |                |
| Leaderboard, dashboard, or results page         |                   |             |                |
| Evaluation harness, package, or hosted runner   |                   |             |                |
| User guide, scoring guide, or contributor guide |                   |             |                |
| Release log, changelog, or maintenance record   |                   |             |                |
| Maintainer statement or official announcement   |                   |             |                |
| Contextual literature                           |                   |             |                |

Additional materials comments:

### 1.3 Benchmark Information

| Prompt                                                             | Response |
| :----------------------------------------------------------------- | :------- |
| Benchmark name                                                     |          |
| Short name or acronym                                              |          |
| Benchmark version, edition, or release                             |          |
| Original benchmark name, if this is an adaptation                  |          |
| Benchmark creators or authors                                      |          |
| Current maintainers                                                |          |
| Host organization, platform host, repository owner, or distributor |          |
| Date of original release                                           |          |
| Date of current release or revision                                |          |
| License or access terms                                            |          |
| Persistent identifier, citation, or DOI                            |          |

Review notes:

### 1.4 Public Artifacts

Record whether benchmark materials exist and how they can be accessed. Evaluate their quality later in Part B.

| Artifact                                  | URL or location | Access status | Review detail |
| :---------------------------------------- | :-------------- | :------------ | :------------ |
| Paper or technical report                 |                 |               |               |
| Benchmark website                         |                 |               |               |
| Code repository                           |                 |               |               |
| Evaluation harness                        |                 |               |               |
| Dataset or task set                       |                 |               |               |
| Prompt set                                |                 |               |               |
| Rubric or scoring guide                   |                 |               |               |
| Leaderboard or result display             |                 |               |               |
| Release log or changelog                  |                 |               |               |
| Contact, issue channel, or feedback route |                 |               |               |

Additional comments on benchmark materials:

---

## Section 2. Classification

Section 2 classifies the benchmark's intended measurement domain, target AI systems, users, item/task structure, and administration conditions. EFPA uses this section to clarify who and what the test is for. MESA translates that into benchmark-use context: what systems are evaluated, what forms of model output are required, and which prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules shape interpretation.

### 2.1 Claimed Capability Domains

Specify the capabilities, phenomena, or qualities the benchmark claims to measure using up to five keywords. Select all that apply.

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

Additional capability domain comments:

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

Additional area-of-use comments:

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

Additional evaluated-system comments:

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

Additional user comments:

### 2.5 Task Families, Subdomains, and Scores

Describe the number and meaning of task families, subdomains, splits, score families, aggregate scoring rules, subscores, or derived outputs. This section is descriptive; do not judge representativeness here.

| Component                                                                                          | Description |
| :------------------------------------------------------------------------------------------------- | :---------- |
| Capability, phenomenon, or quality the benchmark claims to measure                                 |             |
| Definition of the capability or quality being measured                                             |             |
| Subcomponents of the claimed capability, phenomenon, or quality                                    |             |
| Excluded scope or non-target abilities                                                             |             |
| Benchmark item, prompt, episode, environment, or interaction families or subdomains                |             |
| Sources for benchmark items, prompts, episodes, environments, or interactions                      |             |
| Sampling method for benchmark items, prompts, episodes, environments, or interactions              |             |
| Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions |             |
| Splits or partitions                                                                               |             |
| Primary score                                                                                      |             |
| Subscores                                                                                          |             |
| Derived scores or scores combined from item, task-family, or subscore results                      |             |
| Qualitative score ranges such as low/medium/high or novice/expert                                  |             |
| Boundaries or caveats for interpretations made from benchmark scores                               |             |

Review notes:

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
- [ ] File, document, or other output generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment

Additional comments on the form of model output:

### 2.7 Prerequisites for Evaluated Systems

EFPA asks about demands placed on the person being assessed. MESA translates this into prerequisites placed on the evaluated AI system. Record what capabilities, interfaces, resources, or access conditions a system must have to participate as intended. Distinguish a true requirement from a convenience or from information that is simply missing.

| Requirement                                                     | Irrelevant or not necessary | Necessary information given | Information missing |
| :-------------------------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: |
| Language support                                                |             [ ]             |             [ ]             |         [ ]         |
| Context length                                                  |             [ ]             |             [ ]             |         [ ]         |
| Multimodal input support                                        |             [ ]             |             [ ]             |         [ ]         |
| Structured output support                                       |             [ ]             |             [ ]             |         [ ]         |
| Exact format, schema, or parser compatibility                   |             [ ]             |             [ ]             |         [ ]         |
| Retry, repair, or correction-loop support for malformed outputs |             [ ]             |             [ ]             |         [ ]         |
| Tool access                                                     |             [ ]             |             [ ]             |         [ ]         |
| Browser or internet access                                      |             [ ]             |             [ ]             |         [ ]         |
| Code execution                                                  |             [ ]             |             [ ]             |         [ ]         |
| Memory or persistent state                                      |             [ ]             |             [ ]             |         [ ]         |
| API compatibility                                               |             [ ]             |             [ ]             |         [ ]         |
| Latency or time budget                                          |             [ ]             |             [ ]             |         [ ]         |
| Cost or compute budget                                          |             [ ]             |             [ ]             |         [ ]         |

Additional requirement comments:

### 2.8 Evaluation Conditions

EFPA records special testing conditions because scores can change when administration changes. MESA records the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules under which AI systems are evaluated. These conditions are part of the benchmark definition, not implementation trivia.

| Condition                         | Description |
| :-------------------------------- | :---------- |
| Prompting protocol                |             |
| System prompt                     |             |
| Few-shot examples                 |             |
| Sampling settings                 |             |
| Tool permissions                  |             |
| Time limits                       |             |
| Human intervention rules          |             |
| Hardware or hosted service        |             |
| Network requirements              |             |
| Sandbox or security constraints   |             |
| Special administration conditions |             |

Additional comments on prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules:

### 2.9 Task and Response Types

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

Other task/response types:

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

Additional stimulus type comments:

### 2.11 Number of Items or Measurement Points

Where the benchmark is dynamic, record minimum, maximum, and typical task counts.

| Prompt                                  | Response |
| :-------------------------------------- | :------- |
| Total public items or tasks             |          |
| Total private or hidden items           |          |
| Development or example items            |          |
| Test items                              |          |
| Dynamic or generated tasks              |          |
| Episodes, trials, or measurement points |          |
| Item count uncertainty                  |          |

Review notes:

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

Additional evaluation mode comments:

Identity and condition controls:

- [ ] No control over submitted systems
- [ ] Some control over submitted systems
- [ ] Controlled model access or audit
- [ ] Controlled evaluation center or private harness
- [ ] Not documented

Additional identity and control comments:

### 2.13 Technological Arrangements

Mark A for available and R for required where documentation permits.

| Technology            |  A  |  R  |
| :-------------------- | :-: | :-: |
| API access            | [ ] | [ ] |
| Local inference       | [ ] | [ ] |
| GPU                   | [ ] | [ ] |
| CPU-only execution    | [ ] | [ ] |
| Docker or container   | [ ] | [ ] |
| Python package or CLI | [ ] | [ ] |
| Browser               | [ ] | [ ] |
| External tools        | [ ] | [ ] |
| Internet access       | [ ] | [ ] |
| Proprietary platform  | [ ] | [ ] |

Additional technology comments:

### 2.14 Time and Resource Requirements

Record documented estimates. Mark missing if not stated.

| Activity                           | Time, compute, or cost estimate |
| :--------------------------------- | :------------------------------ |
| Setup                              |                                 |
| Model inference or task completion |                                 |
| Scoring                            |                                 |
| Human adjudication                 |                                 |
| Analysis or reporting              |                                 |
| Full benchmark run                 |                                 |
| API or compute cost                |                                 |

Additional requirement comments:

### 2.15 Benchmark Forms, Versions, and Variants

Describe public/private forms, alternate forms, short forms, language variants, domain subsets, and deprecated versions.

| Form or variant | Purpose | Stated score-comparability interpretation | Status |
| :-------------- | :------ | :---------------------------------------- | :----- |
|                 |         |                                           |        |

Additional form and variant comments:

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

Additional task selection comments:

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

Additional scoring input comments:

### 2.18 Broad Claim and CHC/AGI Cautions

Complete this descriptive screen when the benchmark title, paper, website, or leaderboard uses terms such as intelligence, general intelligence, AGI, reasoning, agency, autonomy, broad capability, expert capability, or cross-domain competence. Record only interpretations made or clearly implied from benchmark scores; put reviewer cautions in the final row and Part B.

| Prompt                                                         | Response |
| :------------------------------------------------------------- | :------- |
| Term used for broad interpretation from benchmark scores       |          |
| Breadth implied by the score interpretation across domains     |          |
| Depth or proficiency level implied by the score interpretation |          |
| Sub-abilities explicitly covered                               |          |
| Sub-abilities explicitly excluded or not tested                |          |
| Coverage across modalities, tools, memory, planning, or speed  |          |
| Stated AGI, autonomy, or agency caveats                        |          |
| Relation to CHC-like broad/narrow abilities, if stated         |          |
| Descriptive caution for Part B                                 |          |

Review notes:

---

## Section 3. Measurement and Scoring

Section 3 describes how model behavior becomes a score. EFPA separates scoring procedure from scores. MESA keeps that distinction: 3.1 identifies scoring method classes, while 3.2 describes the scoring pipeline and the meaning of global and partial rules or quantities used to convert model behavior into scores.

### 3.1 Scoring Procedure

Select scoring methods only. Do not describe the scoring pipeline in this subsection.

- [ ] Not explicitly stated
- [ ] Automated exact-match scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] Unit-test or execution-based scoring
- [ ] Rule-based scoring
- [ ] Human rating
- [ ] Scoring by another model that evaluates outputs
- [ ] Output parser or extractor that turns model responses into scoreable values
- [ ] Fuzzy, schema-aware, or admissible-variant parsing
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [ ] Leaderboard service scoring
- [ ] Manual adjudication

Additional scoring method comments:

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or scoring rule/quantity | Definition | How item, task-family, or subscore results are combined | Interpretation stated by authors |
| :----------------------------- | :--------- | :------------------------------------------------------ | :------------------------------- |
| Primary score                  |            |                                                         |                                  |
| Subscore                       |            |                                                         |                                  |
| Derived score                  |            |                                                         |                                  |
| Qualitative band               |            |                                                         |                                  |

Treatment of responses that fail format, schema, refusal, completion, or parsing requirements, or are missing or refused:

Retry, repair, parser fallback, or manual adjudication policy for response-format problems:

Review notes:

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

Additional comments on score-rule types:

### 3.4 Score Transformation

Select all that apply.

- [ ] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against a reference point used to interpret scores
- [ ] Weighting across subdomains
- [ ] Formula for combining item, task-family, or subscore results documented
- [ ] Formula for combining item, task-family, or subscore results partially documented
- [ ] Formula for combining item, task-family, or subscore results not documented
- [ ] Not applicable

Formula, weighting, scaling, normalization, or conversion comments:

### 3.5 Reference Groups, Baselines, and Comparators

Select all that apply.

- [ ] No reference point or documented comparison group used to interpret scores
- [ ] Expected performance from random guessing or trivial selection
- [ ] Performance from human participants under documented conditions
- [ ] Performance from qualified domain experts
- [ ] Performance from a reference model used to interpret scores
- [ ] Previous model cohort
- [ ] Commercial system used as a documented comparison point
- [ ] Open-weight model used as a documented comparison point
- [ ] Domain-specific reference group

Additional comments on reference points or documented comparison groups used to interpret scores:

| Reference point or documented comparison group            | Construction method | Intended score interpretation |
| :-------------------------------------------------------- | :------------------ | :---------------------------- |
| Random guessing or trivial-selection reference point      |                     |                               |
| Human-participant performance under documented conditions |                     |                               |
| Qualified domain-expert performance                       |                     |                               |
| Documented group of models used for comparison            |                     |                               |
| Prior benchmark or version                                |                     |                               |
| Score boundary or lower/upper reference point             |                     |                               |

Review notes:

### 3.6 Score Uncertainty and Stability

This remains descriptive in Part A. Record whether uncertainty or similar scores across repeated evaluations under documented conditions are reported.

- [ ] Reported ranges expressing uncertainty around a score or comparison
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Hierarchical, clustered, or item-level bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Statistics on consistency across judges
- [ ] Evidence that human or expert scorers apply rubrics consistently
- [ ] Sensitivity analyses
- [ ] Score changes caused by prompt wording, small input changes, ordering, phrasing, format, or response schema
- [ ] IRT, adaptive testing, or item-parameter precision estimates
- [ ] Not reported

Additional uncertainty and repeated-run stability comments:

### 3.7 Metric-to-Claim Linkage

This remains descriptive in Part A. Record the documented link between scoring-rule behavior and interpretations made from benchmark scores.

| Prompt                                                                                  | Response |
| :-------------------------------------------------------------------------------------- | :------- |
| Why the primary rule or quantity used to convert model behavior into a score was chosen |          |
| Whether lower or upper limits of the score rule are documented                          |          |
| Whether the scoring rule may reward behavior outside the target capability              |          |
| Whether parser, judge, or scorer validation is documented                               |          |
| Whether response-format burden is separated from the target capability                  |          |
| Whether score changes from small item or prompt changes affect the score interpretation |          |
| Whether score uncertainty affects interpretation                                        |          |
| Whether score differences are interpreted statistically                                 |          |
| Whether benchmark reports state what users should not infer                             |          |

Review notes:

---

## Section 4. Benchmark Outputs and Reports

Section 4 adapts EFPA's digitally generated reports to AI benchmark outputs: papers, leaderboards, dashboards, result files, scorecards, APIs, raw traces, and public interpretations made from benchmark scores. Record what reports exist and how they present scores; evaluate report quality in Part B.

### 4.1 Output Availability

- [ ] Public leaderboard available
- [ ] Public aggregate scores available
- [ ] Public per-domain scores available
- [ ] Public per-item scores available
- [ ] Public model responses, traces, logs, judge rationales, or per-item data available
- [ ] Public traces or logs available
- [ ] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

Additional output availability comments:

### 4.2 Output Name or Description

| Output | Description | Public/private |
| :----- | :---------- | :------------- |
|        |             |                |

Review notes:

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

Additional presentation comments:

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

Additional output structure comments:

### 4.5 Sensitivity to Context

Select one.

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [ ] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts:

Review notes:

### 4.6 Development of Outputs

Select all that apply.

- [ ] Based on benchmark authors' design
- [ ] Based on empirical or actuarial relationships
- [ ] Based on expert judgment
- [ ] Based on human annotation
- [ ] Based on outputs scored by another model
- [ ] Automatically generated by benchmark platform

Additional development basis comments:

Describe origin of report content:

### 4.7 Modifiability

Select one.

- [ ] Not modifiable
- [ ] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

Review notes:

### 4.8 Transparency

Select one.

- [ ] Clear linkage between benchmark tasks, scores, and reported score interpretations
- [ ] Partial linkage between benchmark tasks, scores, and reported score interpretations
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Review notes:

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

Additional output content comments:

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

Additional recipient comments:

---

## Section 5. Benchmark Access, Artifacts, and Lifecycle

Section 5 records how benchmark artifacts are distributed, accessed, reproduced, and maintained. MESA expands EFPA's supply-arrangement fields to include repositories, datasets, hidden or restricted evaluation items, controls for prior model exposure to benchmark items or answers, artifacts needed to replicate results, licenses, and maintenance policies.

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

Additional supporting material comments:

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

Additional publication method comments:

### 5.3 User Requirements or Qualifications

Describe any requirements specified for running, submitting to, interpreting, or maintaining the benchmark.

| Requirement type                             | Requirement |
| :------------------------------------------- | :---------- |
| Technical skill                              |             |
| Model access                                 |             |
| Dataset access                               |             |
| Compute or budget                            |             |
| Human expertise                              |             |
| Account, license, or competition eligibility |             |
| Ethical, safety, or data-use obligations     |             |

Additional requirement comments:

### 5.4 Dataset and Item Access

| Component                                      | Public | Restricted | Hidden | Not available |
| :--------------------------------------------- | :----: | :--------: | :----: | :-----------: |
| Training or development items                  |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Public evaluation items                        |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Private or held-out evaluation items           |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Secret, encrypted, or reserve evaluation items |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Retired or archived evaluation items           |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Answer keys or reference solutions             |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Metadata or annotations                        |  [ ]   |    [ ]     |  [ ]   |      [ ]      |
| Raw model outputs or logs                      |  [ ]   |    [ ]     |  [ ]   |      [ ]      |

Additional access comments:

### 5.5 Provenance and Contamination Documentation

| Topic                                                                        | Documented | Partially documented | Not documented |
| :--------------------------------------------------------------------------- | :--------: | :------------------: | :------------: |
| Data origin or task creation                                                 |    [ ]     |         [ ]          |      [ ]       |
| Persistent dataset or benchmark-material identifier                          |    [ ]     |         [ ]          |      [ ]       |
| Author or contributor qualifications                                         |    [ ]     |         [ ]          |      [ ]       |
| Deduplication or overlap checks                                              |    [ ]     |         [ ]          |      [ ]       |
| Rationale for public items and hidden or restricted evaluation items         |    [ ]     |         [ ]          |      [ ]       |
| Screening for prior model exposure to benchmark items, answers, or sources   |    [ ]     |         [ ]          |      [ ]       |
| Canary strings or training-data warnings                                     |    [ ]     |         [ ]          |      [ ]       |
| Diagnostic task for performance driven by prior exposure to items or answers |    [ ]     |         [ ]          |      [ ]       |
| Pre-exposure or source-material searchability checks                         |    [ ]     |         [ ]          |      [ ]       |
| Hash commitments, signatures, or tamper-evident audit logs                   |    [ ]     |         [ ]          |      [ ]       |
| Encrypted, secret, or controlled-release item reserve                        |    [ ]     |         [ ]          |      [ ]       |
| Rules for updating, rotating, replacing, or adding benchmark items over time |    [ ]     |         [ ]          |      [ ]       |
| Reporting of known unintended disclosures or deprecated/archived items       |    [ ]     |         [ ]          |      [ ]       |

Additional provenance and prior-exposure comments:

### 5.6 Reproducibility Materials

Select all that apply.

- [ ] Complete task data
- [ ] Complete prompt templates
- [ ] Code or platform that administers tasks, collects outputs, and often runs scoring
- [ ] Scoring code
- [ ] Environment file or dependency list
- [ ] Container or reproducible environment
- [ ] Version pinning
- [ ] Random seeds or deterministic settings
- [ ] Model responses, traces, logs, judge rationales, or per-item data
- [ ] Reproduction script for published results
- [ ] Push-button replication script or single documented command
- [ ] Expected-output fixtures or smoke-test example
- [ ] Continuous integration or test suite
- [ ] Public build status or equivalent passing-test signal

Additional reproducibility comments:

### 5.7 Maintenance and Versioning

| Topic                                                                                               | Response |
| :-------------------------------------------------------------------------------------------------- | :------- |
| Maintainer identity                                                                                 |          |
| Documented release names, tags, changes, and score-comparability implications                       |          |
| Changelog or update record                                                                          |          |
| Issue or feedback process                                                                           |          |
| Item correction process                                                                             |          |
| Deprecated item handling                                                                            |          |
| Rules for updating, rotating, replacing, or adding hidden evaluation items over time                |          |
| Last code-usability or harness health check                                                         |          |
| Build, CI, or smoke-test status                                                                     |          |
| Score-ceiling threshold or criteria for deprecating, archiving, or ending use                       |          |
| Policy for deprecating, archiving, or ending use of items, versions, leaderboards, or the benchmark |          |
| Retired-item publication or audit policy                                                            |          |
| Score comparability across versions                                                                 |          |
| Policy for comparing scores across dates, cohorts, refreshes, or rolling windows                    |          |
| Long-term archival plan                                                                             |          |

Review notes:

---

## Appendix A. General Description of the Benchmark

Write a concise descriptive summary of the benchmark for readers who have not inspected the materials. Keep this descriptive and defer evaluation to Part B.

Free Text:

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether the benchmark is adequate as a measurement instrument for its intended use. Use Part A as the factual base. Use EFPA Part B as the structural model, BetterBench for benchmark lifecycle quality and reproducibility, Measuring what Matters for evidence that scores support the intended capability interpretation and the chain from real capability or behavior to task design, scoring, and score interpretation, and AGI/CHC literature when broad intelligence claims are made.

Part B should be completed only after the Part A description is sufficiently grounded. Descriptive facts, access limits, and missing materials should be recorded before assigning ratings. When evidence is incomplete, identify the missing evidence and its consequence for interpretation; do not treat absence of documentation as proof of poor benchmark quality.

## Information Sources

Information sources that might inform Part B include:

- Official benchmark papers, technical reports, model cards, dataset cards, websites, documentation hubs, repositories, leaderboards, scorecards, dashboards, and changelogs supplied or maintained by benchmark creators.
- Public benchmark materials such as task files, prompts, rubrics, reference answers, scorer code, harness code, examples, raw outputs, submission rules, issue trackers, release notes, and archived versions.
- Open information in academic literature, benchmark-quality literature, audit reports, replication studies, analyses of prior model exposure to benchmark items or answers, validation studies, and independent technical commentary. Use these sources to contextualize or challenge score interpretations, not to replace official facts.
- Maintainer-provided or access-controlled information that is not normally supplied to users. If such material affects a rating, state clearly in the review notes that the rating depends on non-public material inspected by the reviewer.
- Confidential or restricted technical information, such as hidden test splits, item provenance, audits for prior exposure to benchmark items or answers, scorer validation reports, calibration data for scoring by another model, or security details. If reviewed under access restrictions, describe only the rating implication and the access status, without disclosing restricted content.

## Explanation of Ratings

All rating items use the EFPA-style scale below unless a section states otherwise. Detailed "Excellent" anchors identify what a rating of `4` would require for that item. Lower ratings should be assigned by reviewer judgment, considering the benchmark's intended use, scope of score interpretation, decision stakes, technical complexity, evidence quality, and consequences of misinterpretation.

Where a `0` or `1` rating is assigned to an attribute that is critical for the benchmark's stated purpose, the review should caution that the benchmark is suitable only for limited exploratory, research, or expert-qualified use unless stronger evidence is supplied. Critical attributes will vary by benchmark: for example, controls for prior model exposure to benchmark items or answers may be critical for public knowledge benchmarks, scorer consistency may be critical for open-ended generation benchmarks, and reference points used to interpret scores may be critical for leaderboards used in procurement or policy.

Overall ratings must be based on reviewer judgment rather than mechanical averaging. A single severe gap may dominate the overall rating when it undermines the intended score meaning; conversely, a narrow gap may be less consequential when the benchmark's score interpretation is modest and clearly bounded.

### Rating Scale

| Rating  | Meaning                                                                                |
| :-----: | :------------------------------------------------------------------------------------- |
| **n/a** | This attribute is not applicable to this benchmark or its stated use.                  |
|  **0**  | Not possible to rate because no, or insufficient, information is provided.             |
|  **1**  | Inadequate for the benchmark's stated purpose or intended interpretation.              |
|  **2**  | Adequate: sufficient for cautious use, with limitations that should be stated.         |
|  **3**  | Good: clear, relevant, and mostly complete support, with no major interpretive threat. |
|  **4**  | Excellent: comprehensive, well-documented, and strongly aligned with the item anchor.  |

## General Guidance on Assigning Ratings

It is difficult to set universal thresholds for benchmark quality. The adequacy of evidence depends on what capability or quality the benchmark claims to measure, how scores are used, whether comparisons are high stakes, whether tasks are public or hidden, whether scoring is deterministic or judgment-based, and whether the benchmark is stable or regularly refreshed. Ratings should therefore be anchored in the intended score meaning, not in a generic expectation that every benchmark must supply every possible form of evidence.

For descriptive gaps, first ask what evidence would be needed to support the benchmark's actual score interpretation. A missing human reference point, for example, may be serious for a benchmark claiming expert-level performance but less central for a narrow regression test. A missing audit for prior model exposure may be serious for public web-derived knowledge tasks but less central for a private live-environment evaluation with documented release controls.

For broad interpretations made from benchmark scores about intelligence, AGI, reasoning, agency, autonomy, or cross-domain competence, require stronger breadth and validity evidence than for narrow capability interpretations. Isolated high performance on one task family should be treated as evidence about that task family unless the benchmark supplies a validity argument for broader interpretation.

Ratings should be based on the information available, with comments explaining consequential evidence, limitations, and rating rationale where needed.

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

EFPA Section 6 asks whether the test explains its rationale, development, documentation, and item quality. MESA asks whether the benchmark defines the real capability or behavior of interest, explains why its tasks and scoring rules operationalize that phenomenon, documents task development, supports item quality, and gives users enough procedural information for cautious qualified use.

This section should be revisited after completing Sections 8-12, because later evidence about reference points, reliability, validity, responsible use, and reporting may reveal strengths or weaknesses in the original rationale and documentation. A benchmark can have useful tasks but still receive a low rating here if users cannot determine what the tasks are meant to support, how they were selected, or what interpretations should be avoided.

When rating this section, distinguish the quality of the benchmark's design argument from the benchmark's observed performance results. High model scores, leaderboard popularity, or broad adoption do not by themselves establish a clear definition of the capability or quality being measured, defensible task-development process, or adequate documentation. Conversely, a benchmark with modest scope can rate well if its score interpretation is precise, its materials are traceable, and its limitations are explicit.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                |
| :----: | :-------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable rationale, development account, documentation, or procedural information is available.                                        |
|   1    | Core score interpretations, task-development procedures, or user instructions are too unclear for responsible interpretation.           |
|   2    | The benchmark is documented well enough for cautious use, but important design, development, or procedural gaps remain.                 |
|   3    | Rationale, development, documentation, and instructions are clear and mostly complete, with only limited gaps.                          |
|   4    | The benchmark gives comprehensive, traceable, and well-justified support for its rationale, development, documentation, and procedures. |

### 6.1 Rationale and Development

- This sub-section concerns the benchmark's rationale, definition of the capability or quality being measured, task or item development, and evidence that the benchmark content was built to support the intended score meaning.
- Consider whether reviewers can trace the benchmark from the claimed capability to task design, item sources, scoring decisions, score combination, and intended use. For broad score interpretations, check whether the rationale covers the relevant subdomains rather than relying on a benchmark title or leaderboard framing.
- Items to be rated `n/a` or `0`-`4`.

#### 6.1.1 Rationale and construct definition

- Excellent: The benchmark gives a clear, theoretically grounded account of the real capability, behavior, or quality of interest, explains why the benchmark was constructed, defines boundaries and exclusions for what is being measured, identifies whether the phenomenon is contested or composite, and distinguishes the target capability from adjacent or broader score interpretations.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.2 Summary of prior research and benchmark context

- Excellent: The benchmark documentation situates the benchmark in relevant research and prior evaluations, explains what gap it addresses, and identifies how prior findings, benchmark failures, or measurement limitations informed the design.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.3 Phenomenon-task-metric-claim chain

- Excellent: The documentation explicitly links the real capability or behavior being measured to task design, response requirements, the rule or quantity used to convert behavior into a score, the method for combining scores, and the intended score meaning, with plausible confounds, non-target tactics, formatting effects, parser effects, prior exposure to items or answers, sensitivity to small item changes, and benchmark-specific tuning considered.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.4 Task or item design

- Excellent: Task formats, item types, forms of model output, difficulty range, scoring protocols, time or tool constraints, and score-combination choices are clearly justified as appropriate for the stated measurement aims and intended AI systems.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.5 Procedures for developing task or item content

- Excellent: Content development used relevant domain expertise, benchmark design expertise, qualitative review, clear inclusion and exclusion criteria, documented sampling or sourcing procedures, and task-quality checks to ensure task content represents the intended capability space.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.6 Thoroughness of the final task or item selection process

- Excellent: The final task or item pool is justified through documented selection decisions, a defensible sampling strategy such as random, stratified, criterion, targeted, or well-justified mixed sampling, review evidence, pilot results where available, coverage analysis, removal of unsuitable items, and explanation of tradeoffs between breadth, depth, difficulty, and feasibility. Convenience sampling is not automatically disqualifying when its limits are explicit and score interpretations are narrow.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.7 Quantitative evidence of task or item quality

- Excellent: Quantitative item or task evidence is reported where appropriate, such as difficulty, discrimination, ceiling and floor effects, domain coverage, inter-item redundancy, scorer behavior, model cohort performance, human or expert performance, or other benchmark-relevant indicators.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.8 Adaptation, translation, or benchmark version derivation

- Excellent: Any adaptation, translation, domain transfer, dataset reuse, synthetic data generation, benchmark refresh, or derived version follows a documented process with expert review, source-limit analysis, equivalence checks, cultural or domain considerations where relevant, and clear limits on comparability with prior versions.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.1.9 Overall quality of rationale, development, and task or item quality

- Excellent: Reviewer judgment, based on items 6.1.1-6.1.8, supports the conclusion that the benchmark rationale, definition of what is being measured, development process, and task or item quality are comprehensive and fit for the intended score meaning. Do not mechanically average ratings.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 6.2 Adequacy of Documentation Available to Users

- This sub-section covers the comprehensiveness, clarity, currency, and ability to connect reported scores to source materials, run conditions, outputs, scoring code, and versions in documentation available to benchmark users, reviewers, and maintainers.
- Documentation should be evaluated as a user-facing support for responsible benchmark use. Private evidence may inform a rating if inspected, but lack of public access should be described because it affects independent auditability and ordinary user interpretation.
- Items to be rated `n/a` or `0`-`4`.

#### 6.2.1 Documentation of benchmark purpose and intended use

- Excellent: Documentation clearly explains what capability or quality the benchmark is designed to measure, what it is not designed to measure, intended users, intended AI systems, suitable use cases, and explicit uses that should not be supported.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.2 Documentation of development process

- Excellent: Documentation gives full details of data or item sources, sampling method, task construction, filtering, review, piloting, scoring design, reused-dataset limitations, changes during development, and reasons for major design decisions.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.3 Documentation of scoring and metrics

- Excellent: Documentation clearly explains output parsing, scoring rules, definitions of the quantities used to convert behavior into scores, how item or subscore results are combined, treatment of outputs that fail format, schema, refusal, completion, or parsing requirements, tie handling, uncertainty reporting, and how scores should be interpreted.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- Excellent: Documentation clearly explains how score stability, run variance, scorer or judge agreement, parser handling of valid and malformed responses, sensitivity to prompt wording or small item changes, form or version equivalence, and statistical uncertainty were assessed and how these affect interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.5 Documentation of validity evidence

- Excellent: Documentation presents a clear validity argument for the intended score meanings, including content support, task representativeness, evidence that scoring rewards the target capability, relations with other evidence, controls for prior model exposure to benchmark items or answers, and limits of inference.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.6 Documentation of fair use and comparability

- Excellent: Documentation describes fairness, accessibility, language or domain coverage, cross-system comparability, evaluation-condition comparability, and any restrictions needed to interpret results responsibly.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.7 Documentation of maintenance and versioning

- Excellent: Documentation provides version history, changelog, release rules, refresh policy, deprecation or retirement policy, saturation or archival criteria where relevant, data or task updates, leaderboard update practices, and clear guidance on comparability across versions or temporal cohorts.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.2.8 Adequacy of documentation available to users

- Excellent: Reviewer judgment, based on items 6.2.1-6.2.7, supports the conclusion that documentation is comprehensive, current, traceable, and sufficient for qualified users to run, inspect, score, and interpret the benchmark responsibly. Do not mechanically average ratings.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 6.3 Quality of Procedural Instructions

- This sub-section covers instructions for administering, running, scoring, interpreting, and maintaining the benchmark.
- Procedural quality includes reproducibility and error handling, not only whether a benchmark can be run by its creators. Instructions should make prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules explicit enough that qualified users can reproduce or audit scores and understand when runs are no longer comparable.
- Items to be rated `n/a` or `0`-`4`.

#### 6.3.1 Evaluation setup and administration

- Excellent: Step-by-step setup and administration instructions are complete, reproducible, and include required environment, dependencies, credentials, compute assumptions, seeds, sampling settings, tool permissions, smoke-test or replication commands where relevant, and handling of expected failures.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.2 Scoring procedure and error handling

- Excellent: Scoring instructions are clear and include checks for parser failures, malformed outputs, format retries or repairs, judge failures, missing responses, duplicate submissions, manual overrides, and audit trails for any corrections.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.3 Interpretation and reporting guidance

- Excellent: Users receive detailed guidance on interpreting aggregate scores, subscores, uncertainty, comparisons against reference points, version differences, upper or lower reference-point effects, and common risks of interpreting beyond what evidence supports.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- Excellent: The benchmark clearly states system prerequisites, access requirements, tool-use assumptions, modality requirements, unsupported system classes, prohibited uses, and the consequences of violating prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.5 Technical support and implementation guidance

- Excellent: Technical instructions cover software and hardware requirements, known failure modes, troubleshooting, test runs, expected outputs, dependency versions, issue-reporting channels, and support for reproducibility.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.6 References and supporting materials

- Excellent: Documentation provides source-linked references to benchmark papers, datasets, task sources, code repositories, validation materials, related benchmarks, and supporting literature needed for informed review.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 6.3.7 Quality of procedural instructions

- Excellent: Reviewer judgment, based on items 6.3.1-6.3.6, supports the conclusion that procedural instructions are complete, reproducible, and sufficient for qualified users to run and interpret the benchmark without hidden procedural knowledge. Do not mechanically average ratings.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 6.4 Overall Adequacy of Rationale and Documentation

- This overall rating is based on reviewer judgment across sub-sections 6.1, 6.2, and 6.3. Do not mechanically average ratings.
- Excellent: The benchmark provides a comprehensive, source-grounded rationale, a defensible development account, strong task or item quality evidence, complete documentation, and procedural instructions sufficient for responsible qualified use.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 7. Quality and Usability of Benchmark Artifacts

MESA evaluates benchmark materials needed to inspect, run, score, reproduce, or audit the evaluation: datasets, task files, prompts, rubrics, scoring code, harnesses, interfaces, access routes, setup instructions, accessibility, and usability. Material quality includes both what is available and whether intended users can run or inspect it without hidden procedural knowledge.

Rate benchmark materials in relation to the benchmark's intended users and access model. Fully public materials are not always required, especially when hidden or restricted evaluation items are needed to reduce prior exposure or leaderboard gaming, but the access route, restrictions, auditability, and consequences for reproducibility should be clear. A benchmark with controlled access can rate well when the controls are justified and reviewers can inspect enough information to judge quality.

For open-ended, interactive, tool-use, multimodal, or environment-based benchmarks, benchmark materials include more than item text. They also include system prompts, environment state, dependency versions, assets, scoring scripts, judge prompts, rubrics, examples, failure handling, and any infrastructure needed to produce comparable scores.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                |
| :----: | :-------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | Benchmark materials cannot be inspected or used well enough to judge or reproduce the benchmark.                                        |
|   1    | Benchmark materials are incomplete, inaccessible, unstable, or too poorly specified for the intended use.                               |
|   2    | Benchmark materials support cautious use but require substantial assumptions, workarounds, or controlled access caveats.                |
|   3    | Benchmark materials are usable, traceable, and mostly reproducible, with minor access or usability limitations.                         |
|   4    | Benchmark materials are complete, accessible or access-controlled with justification, reproducible, well documented, and fit for audit. |

### 7.1 Quality of Benchmark Artifacts

- This sub-section concerns the benchmark materials that users need to inspect, run, score, reproduce, or audit the evaluation.
- Judge both completeness and usability. These materials should be understandable by intended users, robust to ordinary execution errors, and specific enough to prevent hidden evaluator choices from changing the score interpretation.
- Items to be rated `n/a` or `0`-`4`.

#### 7.1.1 Dataset, task set, or evaluation environment availability

- Excellent: The dataset, task set, environment, or access route is complete, versioned, licensed where applicable, clearly linked, and available in a form that supports independent inspection or justified controlled access.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.2 Prompts, instructions, and input artifacts

- Excellent: Prompts, task instructions, examples, system messages, input files, context windows, multimodal assets, and any hidden or private instructions are documented or controlled in a way that supports reproducible evaluation and fair interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.3 Rubrics, reference answers, and response format requirements

- Excellent: Rubrics, answer keys, reference outputs, response schemas, parsing rules, admissible variants, retry or repair rules, and invalid-response handling are clear, versioned, tested where relevant, and appropriate for the capability or quality being measured.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- Excellent: The harness and scoring tools are runnable, documented, tested, robust to common errors and malformed outputs, version-pinned where needed, covered by smoke tests or CI/build status where relevant, and include a replication script or examples that reproduce expected outputs.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.5 Interface and workflow usability

- Excellent: The benchmark workflow is easy for intended users to understand and operate, with clear command paths, expected inputs and outputs, progress or failure signals, and no hidden procedural steps.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.6 Accessibility across modalities, languages, and system types

- Excellent: Benchmark materials and workflows are usable by design for relevant modalities, languages, deployment modes, API or local systems, and assistive or alternate interaction needs, with justified adaptations when usability is limited.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.7 Licensing, use requirements, and risk warnings

- Excellent: Licenses, terms of use, redistribution limits, privacy constraints, sensitive-content warnings, safety restrictions, and required user qualifications are explicit and compatible with the benchmark's intended use.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 7.1.8 Overall quality of benchmark artifacts

- Excellent: Reviewer judgment, based on items 7.1.1-7.1.7, supports the conclusion that benchmark materials are complete, usable, accessible, reproducible, and appropriate for the intended evaluation. Do not mechanically average ratings.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 8. Baselines, Comparators, and Reference Interpretation

EFPA Section 8 evaluates reference distributions and criterion interpretation. MESA translates that logic into reference points used to interpret AI benchmark scores: random or chance floors, human or expert performance, documented groups of models, previous benchmark versions, score boundaries for pass/fail or tier claims, score-ceiling evidence, and qualitative score bands. A benchmark can be useful without human reference samples, but the interpretation of scores should be anchored somehow.

The figure below visualizes the structure of possible steps in reviewing reference points, documented comparison groups, and score interpretation.

#### Figure 2: Structure of Section 8 on Baselines, Comparators, and Reference Interpretation

```mermaid
flowchart LR

    %% Main Header
    Main("SECTION 8: Baselines, Comparators,<br/>and Reference Interpretation")

    %% Tier 1: Main categories
    S81("8.1 Baseline and comparator<br/>interpretation")
    S82("8.2 Overall adequacy")

    %% Tier 2: Reference anchors
    subgraph G81 ["Reference anchors"]
        direction TB
        S81a("Random, chance, floor,<br/>and ceiling baselines")
        S81b("Human or expert baselines")
        S81c("Model comparator cohort")
        S81d("Historical, version, or<br/>benchmark-family comparators")
        S81a ~~~ S81b ~~~ S81c ~~~ S81d
    end

    %% Tier 3: Interpretation requirements
    subgraph G82 ["Interpretation requirements"]
        direction TB
        S82a("Criterion thresholds,<br/>score bands, or categories")
        S82b("Representativeness of<br/>reference groups")
        S82c("Currency and maintenance<br/>of baseline evidence")
        S82a ~~~ S82b ~~~ S82c
    end

    %% Tier 4: Final checks
    subgraph G83 ["Final checks"]
        direction TB
        C1("Anchors support the<br/>intended score interpretation")
        C2("Uncertainty and limits<br/>are documented")
        C3("Comparisons are current<br/>and evaluation conditions are comparable")
        C1 ~~~ C2 ~~~ C3
    end

    %% Tier 5: Final evaluation
    Overall("Overall adequacy regarding<br/>'Baselines and Reference Interpretation' & comments")

    %% Horizontal Connections
    Main --> S81
    Main --> S82

    S81 --> G81
    S81 --> G82
    S82 --> Overall

    G81 --> G83
    G82 --> G83
    G83 --> Overall

    %% Styling to match the EFPA figures
    style Main fill:#B0C4DE,color:#000,stroke:#D2691E,stroke-width:2px
    style Overall fill:#B0C4DE,color:#000,stroke:#004771,stroke-width:2px
    style S81 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S82 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px

    %% Style for the internal list items
    classDef detail fill:#004771,color:#fff,stroke:#D2691E,stroke-dasharray: 5 5;
    class S81a,S81b,S81c,S81d,S82a,S82b,S82c,C1,C2,C3 detail;
```

Reference interpretation should be rated in relation to the meanings users are expected to draw from scores. If a benchmark only supports within-benchmark ordering under fixed conditions, then reference points and documented comparison groups should make that narrow use clear. If a benchmark supports interpretations about expert performance, real-world readiness, general capability, or scores approaching a ceiling, stronger reference evidence is required.

Reference points and documented comparison groups are not interchangeable. Chance and trivial-strategy references help detect whether tasks are meaningful; human and expert performance helps interpret difficulty and score-claim scope; model cohorts support relative comparison; score boundaries or qualitative bands support categorical interpretations. Reviewers should note which kinds of reference evidence are available and which are missing for the intended score meaning.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                  |
| :----: | :---------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable reference information is available for interpreting scores.                                                                     |
|   1    | Available reference points or documented comparison groups are inappropriate, undocumented, stale, or misleading for the intended use.    |
|   2    | Reference information supports cautious interpretation but leaves important gaps in comparison-group selection, uncertainty, or currency. |
|   3    | Reference points and documented comparison groups are relevant, documented, and mostly sufficient for the intended score meaning.         |
|   4    | Score interpretation is comprehensive, current, uncertainty-aware, and clearly tied to score claims and comparison limits.                |

### 8.1 Baseline and Comparator Interpretation

- This sub-section concerns the reference information used to make benchmark scores interpretable.
- Repeat or qualify ratings where the benchmark has multiple task families, subscores, model cohorts, or versions with different reference anchors. A strong reference point for one subdomain should not be assumed to support another without evidence.
- Items to be rated `n/a` or `0`-`4`.

#### 8.1.1 Random, chance, floor, and ceiling baselines

- Excellent: Random, chance, lower reference point, upper reference point, score-ceiling, and trivial-strategy reference points are reported where relevant, empirically checked when possible, and integrated into score interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.2 Human or expert baselines

- Excellent: Human or expert performance is collected or reported with clear sampling, qualification, task exposure, instructions, timing, tools, uncertainty, and limits on comparability to AI systems.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.3 Model comparator cohort

- Excellent: Documented model comparison groups are selected and documented to support the intended score meaning, including model identity, version, date, access mode, prompting, sampling settings, tools, compute conditions, and uncertainty.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.4 Historical, version, or benchmark-family comparators

- Excellent: Comparisons to previous benchmark versions, related benchmarks, earlier model generations, or reference suites are clearly documented, justified, and caveated for differences in task content, scoring, risk of unintended disclosure, and prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- Excellent: Any score boundaries, qualitative bands, pass/fail points, capability labels, score-ceiling interpretations, or tier labels are empirically justified, uncertainty-aware, and tied to intended use rather than arbitrary leaderboard convenience.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.6 Representativeness of reference groups

- Excellent: Reference points and documented comparison groups are representative of the intended score interpretation, with documented inclusion criteria, known gaps, subgroup coverage, and implications for interpreting benchmark results.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 8.1.7 Currency and maintenance of baseline evidence

- Excellent: Evidence from reference points and documented comparison groups is current for the benchmark's intended use, with clear update practices, dates, model-version tracking, and guidance on when outdated comparisons should no longer be used.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- This overall rating is based on reviewer judgment across sub-section 8.1. Do not mechanically average ratings.
- Excellent: Reference-based score interpretation is comprehensive, relevant, current, uncertainty-aware, and sufficient to support cautious interpretations of benchmark scores and comparisons.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 9. Reliability, Precision, and Score Stability

EFPA Section 9 evaluates reliability and precision. MESA asks whether benchmark scores are stable enough for their intended use across runs, prompts, seeds, forms, raters, judges, scorers, benchmark versions, and execution environments. Reliability is especially important when public leaderboards encourage small score differences to be interpreted as meaningful.

Reliability and precision refer to the consistency and uncertainty of benchmark scores across replications of the evaluation procedure. For AI benchmarks, the relevant sources of variation may include stochastic decoding, API or model-version changes, tool calls, execution environments, prompt wording, response parsing, judge models, human raters, task sampling, hidden/public splits, and dependency versions.

There is no single reliability coefficient that fits all AI benchmarks. Deterministic exact-match tests, open-ended generation evaluations, interactive environments, evaluations scored by another model, and human-rated tasks require different evidence. Reviewers should judge whether the methods used are appropriate for the benchmark design and whether the reported uncertainty is sufficient for the intended comparison or decision.

The figure below visualizes the structure of the possible steps in the review of reliability, precision, and score stability.

#### Figure 3: Structure of Section 9 on Reliability, Precision, and Score Stability

```mermaid
flowchart TD

    %% Main Header
    Main("SECTION 9: Reliability, Precision,<br/>and Score Stability")

    %% 9.1 standalone box
    S91("9.1 Data provided?")

    %% Grouped boxes
    subgraph G92 ["9.2 Run-to-run stability and uncertainty"]
        direction TB
        S92a("Seeds, sampling settings,<br/>and repeated runs")
        S92b("Confidence intervals,<br/>standard errors, or precision estimates")
        S92a ~~~ S92b
    end

    subgraph G93 ["9.3 Scorer, judge, parser, and rater reliability"]
        direction TB
        S93a("Automated scorer or parser reliability")
        S93b("Human rater or expert scorer agreement")
        S93c("Model-as-judge reliability<br/>and validity checks")
        S93a ~~~ S93b ~~~ S93c
    end

    subgraph G94 ["9.4 Form, version, prompt, and environment stability"]
        direction TB
        S94a("Prompt, instruction,<br/>or formatting sensitivity")
        S94b("Form, split, version,<br/>or refresh equivalence")
        S94c("Execution environment<br/>and dependency stability")
        S94a ~~~ S94b ~~~ S94c
    end

    subgraph G95 ["9.5 Statistical comparison quality"]
        direction TB
        S95a("Meaningfulness of score differences")
        S95b("Practical significance and<br/>multiple-comparison cautions")
        S95a ~~~ S95b
    end

    %% Bottom Box
    Overall("Overall adequacy regarding<br/>'Reliability, Precision, and Score Stability' & comments")

    %% Layout
    Main ~~~ S91
    Main ~~~ G92
    Main ~~~ G93
    Main ~~~ G94
    Main ~~~ G95

    S91 ~~~ Overall
    G92 ~~~ Overall
    G93 ~~~ Overall
    G94 ~~~ Overall
    G95 ~~~ Overall

    %% Styling
    style Main fill:#B0C4DE,color:#000,stroke:#D2691E,stroke-width:2px
    style Overall fill:#B0C4DE,color:#000,stroke:#004771,stroke-width:2px
    style S91 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px

    %% Style for the grouped internal items
    classDef detail fill:#004771,color:#fff,stroke:#D2691E,stroke-dasharray: 5 5;
    class S92a,S92b,S93a,S93b,S93c,S94a,S94b,S94c,S95a,S95b detail;
```

When ratings depend on numerical evidence, reviewers should consider the benchmark's stakes and score use. A small amount of instability may be acceptable for exploratory research but unacceptable when leaderboards rank systems by narrow margins, when procurement or policy decisions rely on the scores, or when public score interpretations imply meaningful superiority.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                     |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable evidence about reliability, precision, score uncertainty, or stability is available.                                               |
|   1    | Evidence is too limited or mismatched to support the intended comparisons or score interpretation.                                           |
|   2    | Evidence supports cautious interpretation but leaves important sources of score variation unexamined.                                        |
|   3    | Major sources of variation are examined with appropriate methods and clear interpretation guidance.                                          |
|   4    | Reliability, precision, and stability evidence comprehensively supports the intended score use, including uncertainty and comparison limits. |

### 9.1 Data Provided About Reliability, Precision, and Stability

- This sub-section concerns the evidence available for judging whether benchmark scores are stable enough for the intended use.
- Selectively note which sources of variation have evidence and which do not. A benchmark may have strong repeat-run evidence but weak scorer evidence, or strong scorer agreement but no evidence about prompt sensitivity or model-version drift.
- Items to be rated `n/a` or `0`-`4`.

#### 9.1.1 Coverage of reliability and stability evidence

- Excellent: The benchmark reports reliability, precision, or stability evidence across the major sources of score variation relevant to the benchmark, including repeated runs, prompt wording, small item changes, scorers, judges, parsers, versions, forms, temporal cohorts, environments, and model settings.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 9.2 Run-to-Run Stability and Uncertainty

This sub-section concerns score variation when the same benchmark is run repeatedly under documented prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules. Reviewers should check whether repeat-run evidence covers the settings that materially affect the benchmark, including temperature, sampling, seeds, tool use, API state, and environment variation.

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- Excellent: Repeat-run studies or equivalent analyses quantify whether repeated evaluations under documented conditions produce similar scores across relevant seeds, sampling settings, temperatures, tool-use conditions, and execution environments, with settings fully documented.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- Excellent: Scores and score differences are accompanied by appropriate uncertainty estimates, reported ranges expressing uncertainty around scores or comparisons, standard errors, bootstrap intervals, clustered or hierarchical bootstrap intervals where the design requires them, or other justified precision estimates suitable for the benchmark design.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 9.3 Scorer, Judge, Parser, and Rater Reliability

This sub-section concerns consistency introduced by the mechanism that converts model behavior into scores. For open-ended responses, human scoring, rubric scoring, parsers, and scoring by another model should be treated as measurement components requiring evidence, not as neutral implementation details.

#### 9.3.1 Automated scorer or parser reliability

- Excellent: Automated scoring and parsing are validated against representative outputs, edge cases, responses that fail format or schema requirements, admissible variants, and failure modes, with documented error rates, regression tests, and procedures for resolving ambiguous cases.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 9.3.2 Human rater or expert scorer agreement

- Excellent: Human or expert scoring uses clear rubrics, training, representative response samples, adequate numbers of raters, evidence that raters apply rubrics consistently, adjudication procedures, and reporting of residual disagreement.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 9.3.3 Model-as-judge reliability and validity checks

- Excellent: Scoring by another model is validated against human or expert judgments, tested for bias and score changes caused by prompt wording or format, checked across domains and response styles, and monitored for drift when judge models change.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 9.4 Form, Version, Prompt, and Environment Stability

This sub-section concerns whether scores remain comparable when benchmark forms, prompts, versions, item updates, dependencies, execution environments, or external tools change. If comparability is not established, reviewers should treat cross-version or cross-condition comparisons as limited.

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- Excellent: The benchmark assesses whether plausible prompt wording, instructions, examples, item phrasing, answer order, formatting, or response-schema variations materially affect scores, reports sensitivity evidence where relevant, and documents which variants are official or comparable.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 9.4.2 Form, split, version, or refresh equivalence

- Excellent: Alternate forms, public and hidden splits, benchmark item updates, translated versions, rolling cohorts, and version updates have documented equivalence evidence, score normalization or equating where needed, or clear warnings about non-comparability.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 9.4.3 Execution environment and dependency stability

- Excellent: Environment, dependency, API, hardware, external-tool, and data-access variation is controlled or tested, with guidance on how such variation affects reproducibility and score interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 9.5 Statistical Comparison Quality

This sub-section concerns whether reported score differences are large enough and well-estimated enough to support rank ordering or comparative score interpretations. Reviewers should distinguish statistical significance, practical significance, and leaderboard convenience.

#### 9.5.1 Meaningfulness of score differences

- Excellent: The benchmark provides statistically justified guidance for interpreting model differences, including uncertainty, multiple comparisons where relevant, practical significance, limits on comparing scores across dates or cohorts, and cases where rank differences should not be treated as meaningful.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 9.6 Overall Reliability, Precision, and Score Stability

- This overall rating is based on reviewer judgment across sub-sections 9.1-9.5. Do not mechanically average ratings.
- Excellent: Reliability, precision, and stability evidence is comprehensive enough to support the intended score interpretation and comparisons across systems, conditions, and benchmark versions.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 10. Validity Evidence

EFPA Section 10 evaluates validity support for intended score interpretation. MESA centers the chain from real capability or behavior to task design, scoring, and score interpretation: what capability or behavior is claimed, how tasks operationalize it, what rule or quantity converts behavior into a score, and what interpretation the score is used to support. For broad intelligence, AGI, reasoning, autonomy, or agency interpretations, validity review must check breadth, depth, modality, tools, memory, planning, and speed rather than treating isolated performance as broad capability.

Validity is not a property of a score in isolation; it is the degree to which evidence and theory support the interpretations and uses made from benchmark scores. The same benchmark may have strong validity support for a narrow interpretation and weak support for a broader public interpretation. Reviewers should therefore identify the specific meaning users are supposed to draw from a score before rating each source of validity evidence.

MESA validity review should consider both psychometric-style evidence and AI-specific threats. Content coverage, internal structure, relations with other evidence, and response-process logic remain central, but benchmark review must also examine whether scoring rewards the target capability, score effects caused by scorers or parsers, prior exposure to benchmark items or answers, unintended disclosure of hidden materials, benchmark-specific tuning, public/hidden split design, and whether public interpretations are proportional to the evidence.

The figure below visualizes the structure of the possible steps in the review of validity evidence.

#### Figure 4: Structure of Section 10 on Validity Evidence

```mermaid
flowchart TD

    %% Main Header
    Main("SECTION 10: Validity Evidence")

    %% Main sub-sections
    S101("10.1 Benchmark content")
    S102("10.2 Internal structure")
    S103("10.3 Metrics and scoring")
    S104("10.4 Relations to<br/>other variables")
    S105("10.5 Contamination,<br/>leakage, and gameability")
    S106("10.6 Claim proportionality")

    %% Details
    subgraph G101 [" "]
        direction TB
        D101a("Content validity and<br/>task representativeness")
        D101b("Construct breadth and<br/>sub-ability coverage")
        D101a ~~~ D101b
    end

    subgraph G102 [" "]
        direction TB
        D102a("Subscores, domains,<br/>clusters, or dimensionality")
        D102b("Item or task behavior<br/>across the score scale")
        D102c("Failure modes and<br/>error analysis")
        D102a ~~~ D102b ~~~ D102c
    end

    subgraph G103 [" "]
        direction TB
        D103a("Metric, scorer,<br/>and aggregation validity")
        D103b("Shortcuts and<br/>construct-irrelevant variance")
        D103a ~~~ D103b
    end

    subgraph G104 [" "]
        direction TB
        D104a("Relations with benchmarks,<br/>humans, criteria, or settings")
        D104b("Convergent and<br/>discriminant evidence")
        D104c("Ecological or predictive relevance")
        D104a ~~~ D104b ~~~ D104c
    end

    subgraph G105 [" "]
        direction TB
        D105a("Contamination and leakage controls")
        D105b("Gameability and benchmark-specific<br/>tuning controls")
        D105a ~~~ D105b
    end

    subgraph G106 [" "]
        direction TB
        D106a("Proportionality of<br/>stated benchmark claims")
        D106b("Broad intelligence, AGI,<br/>agency, or autonomy claims")
        D106a ~~~ D106b
    end

    %% Final Bottom Box
    Overall("Overall adequacy regarding<br/>'Validity Evidence' & comments")

    %% Alignment Connections
    Main ~~~ S101
    Main ~~~ S102
    Main ~~~ S103
    Main ~~~ S104
    Main ~~~ S105
    Main ~~~ S106

    S101 ~~~ G101
    S102 ~~~ G102
    S103 ~~~ G103
    S104 ~~~ G104
    S105 ~~~ G105
    S106 ~~~ G106

    G101 ~~~ Overall
    G102 ~~~ Overall
    G103 ~~~ Overall
    G104 ~~~ Overall
    G105 ~~~ Overall
    G106 ~~~ Overall

    %% Styling to match the EFPA figures
    style Main fill:#B0C4DE,color:#000,stroke:#D2691E,stroke-width:2px
    style Overall fill:#B0C4DE,color:#000,stroke:#004771,stroke-width:2px

    style S101 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S102 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S103 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S104 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S105 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S106 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px

    %% Dashed styling for internal list items
    classDef detail fill:#004771,color:#fff,stroke:#D2691E,stroke-dasharray: 5 5;
    class D101a,D101b,D102a,D102b,D102c,D103a,D103b,D104a,D104b,D104c,D105a,D105b,D106a,D106b detail;
```

Ratings in this section should not be inferred from benchmark popularity, leaderboard difficulty, or whether current models perform poorly. Difficulty can be useful, but validity depends on whether task performance supports the intended score meaning and whether the scoring rule rewards the target capability rather than non-target tactics, prior exposure to items or answers, formatting compliance, or benchmark-specific optimization.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                                                 |
| :----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable validity argument or validity evidence is available for the intended interpretation.                                                                           |
|   1    | Evidence does not support the stated score interpretation, or major threats such as scorer/parser effects, prior exposure, or overbroad interpretation are unresolved.   |
|   2    | Evidence supports a limited or cautious interpretation, but important validity threats or score-interpretation scope gaps remain.                                        |
|   3    | Multiple relevant validity sources support the intended interpretation, with clear caveats and manageable threats.                                                       |
|   4    | A comprehensive validity argument links the real capability or behavior, tasks, scoring rules, evidence, threat controls, and score interpretations in a defensible way. |

### 10.1 Validity Evidence Based on Benchmark Content

- This sub-section concerns whether the benchmark content represents the capability domain or use context the benchmark claims to measure.
- Consider the match between the intended capability space and the sampled tasks, domains, modalities, difficulty levels, and contexts. For broad score interpretations, the review should look for explicit coverage analysis and evidence across relevant sub-abilities.
- Items to be rated `n/a` or `0`-`4`.

#### 10.1.1 Content validity and task representativeness

- Excellent: The task sample comprehensively represents the intended capability domain or use context, with explicit coverage analysis, expert review where relevant, documented exclusions, and clear limits on generalization.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.1.2 Construct breadth and sub-ability coverage

- Excellent: The benchmark identifies relevant subdomains, sub-abilities, modalities, difficulty levels, and contexts, and shows that the score meaning is supported across that breadth rather than by isolated task performance.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.2 Validity Evidence Based on Internal Structure

This sub-section concerns whether the benchmark's internal organization supports the way scores and subscores are interpreted. Domain labels, task clusters, aggregate scores, and capability profiles should have conceptual or empirical support rather than being assumed from task labels alone.

#### 10.2.1 Internal structure, subscores, or dimensionality

- Excellent: Subscores, domains, clusters, task families, or dimensional interpretations are empirically and conceptually supported, with evidence that score combination does not hide incompatible capabilities or misleadingly combine unrelated abilities.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.2.2 Item or task behavior across the score scale

- Excellent: Task behavior supports the intended measurement structure, including appropriate difficulty spread, discriminative value, absence of severe redundancy, and lack of dominant non-target effects such as formatting tactics, score changes caused by prompt wording, parser effects, or performance driven by prior exposure to items.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.2.3 Failure modes and error analysis

- Excellent: Qualitative and quantitative error analysis shows that common failure modes plausibly reflect the capability or quality being measured rather than non-target confounders such as format compliance, parser behavior, memorized source material, instruction complexity, rater or judge bias, or non-target tactics that earn points.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.3 Validity Evidence Based on Metrics and Scoring

This sub-section concerns the score-production step in the chain from real capability or behavior to task design, scoring, and score interpretation. Reviewers should check whether the scoring rule rewards the intended capability or whether it can be driven by score variation caused by factors outside the target capability, such as formatting, verbosity, refusal style, memorized strings, judge preferences, or tool-specific advantages.

#### 10.3.1 Metric, scorer, and aggregation validity

- Excellent: Scoring rules, scorers, rubrics, parsers, models used as judges, and score-combination rules are justified and validated as measuring the intended capability rather than irrelevant behavior, output format compliance, parser strictness, verbosity, prior exposure to items or answers, or benchmark-specific tactics; strict formats are tested, relaxed, retried, or justified when they are not part of the target capability.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- Excellent: The benchmark tests or convincingly mitigates non-target tactics, superficial cues, score effects caused by response-format compliance, judge preferences, unintended disclosure through prompts, score changes caused by small item changes, prior exposure to items or answers, tool-specific advantages, and other score variation caused by factors outside the target capability.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.4 Validity Evidence Based on Relations to Other Variables

This sub-section concerns whether benchmark results behave as expected in relation to other relevant evidence. Expected relations should be stated before interpreting results: for example, relations with related benchmarks, expert judgments, human performance, real-world criteria, model capability profiles, or deliberately different capabilities or qualities being measured.

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- Excellent: Relationships with relevant benchmarks, human or expert performance, real-world tasks, external criteria, or expected model differences are hypothesized, justified, empirically examined, and interpreted with appropriate caution.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.4.2 Convergent and discriminant evidence

- Excellent: The benchmark shows expected relationships with measures of similar capabilities and appropriate separation from measures of different capabilities, with explanations for unexpected convergence or divergence.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.4.3 Ecological or predictive relevance

- Excellent: Evidence supports the relevance of benchmark performance to intended real-world, deployment, scientific, or policy interpretations, with limits clearly stated when the benchmark is abstract, synthetic, or narrow.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.5 Contamination, Leakage, and Gameability

This sub-section concerns whether scores can be inflated by prior exposure, public availability, unintended disclosure of test content or answers, overfitting, reverse engineering, or repeated optimization against the benchmark. The seriousness of these threats depends on release model, task source, public/hidden split design, and how the benchmark is used.

#### 10.5.1 Contamination and leakage controls

- Excellent: The benchmark documents data provenance, public/hidden splits, release rules, canaries or audits where appropriate, searchability risks, training-data exposure risks, diagnostics for prior exposure to benchmark items or answers, and procedures for responding to suspected prior exposure. For benchmarks with high risk of unintended disclosure, live benchmarks, or certification-style benchmarks, stronger evidence may include secret or encrypted reserves, hash commitments, signed logs, synchronized evaluation, post-retirement release, or tasks that test whether performance is driven by prior exposure to items or answers.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.5.2 Gameability and benchmark-specific tuning controls

- Excellent: The benchmark identifies and mitigates risks from training, prompting, or optimization targeted narrowly at the benchmark, tuning prompts or systems to exploit known benchmark quirks, leaderboard gaming, reverse engineering, repeated submissions, and optimization against known scorer, rubric, parser, judge, or score-combination effects.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.6 Claim Proportionality

This sub-section concerns whether interpretations made from benchmark scores are bounded by the evidence. The broader the interpretation, the stronger and broader the evidence required; claims about general intelligence, AGI, agency, autonomy, or broad reasoning require more than high performance on a narrow task set.

#### 10.6.1 Proportionality of stated benchmark claims

- Excellent: Score interpretations are explicitly bounded to what the task sample, scoring rule, validation evidence, and uncertainty support, and public language avoids unsupported extrapolation from scores to broad capability.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- Excellent: If broad score interpretations are made, the benchmark provides evidence across relevant subdomains, modalities, planning horizons, memory demands, tool-use conditions, and transfer contexts; otherwise it explicitly rejects or limits such interpretations.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 10.7 Overall Validity Support

- This overall rating is based on reviewer judgment across sub-sections 10.1-10.6. Do not mechanically average ratings.
- Excellent: The total validity argument convincingly supports the intended score meaning, including content, structure, error analysis, scoring, relations with other evidence, controls for prior exposure, controls against benchmark-specific tactics, and proportionality of score interpretations.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 11. Fair Use, Comparability, and Appropriate Use

EFPA Section 11 evaluates responsible use across groups and contexts. MESA evaluates whether benchmark use is fair and comparable across relevant AI systems, modalities, domains, languages, access modes, compute budgets, and user contexts. The question is not only whether a score can be produced, but whether it can be compared and interpreted responsibly.

Responsible use in AI benchmark review includes, but is broader than, demographic fairness. It covers whether tasks, inputs, languages, modalities, domains, infrastructure, access rules, scoring, and reporting allow intended systems and users to be evaluated under comparable and appropriate conditions. It also covers whether users are warned when scores should not be compared or should not be used for a particular decision.

Relevant information for this section may also have been rated in other sections. The figure below shows sections where ratings will have particular relevance to responsible use across intended systems and contexts, comparability, and use cases or restrictions that bound interpretation. Ratings in this section may still take a broader perspective and therefore need not be identical to the referenced ratings.

#### Figure 5: Relevant Ratings for Fair Use, Comparability, and Appropriate Use from Other Sections

```mermaid
flowchart TD

    %% Main Header
    Main("SECTION 11 Fair Use, Comparability,<br/>and Appropriate Use")

    %% Row 1: Sub-section Headers
    S111("11.1 Rationale and<br/>documentation")
    S112("11.2 Development,<br/>design, and accessibility")
    S113("11.3 Cross-system and<br/>evaluation-condition comparability")
    S114("11.4 Fairness and<br/>bias evidence")
    S115("11.5 Appropriate use<br/>and restrictions")
    S116("Reports and<br/>public communication")

    %% Column 1 Ratings
    subgraph G111 [" "]
        direction TB
        D111a("6.1.1")
        D111b("6.2.1")
        D111c("6.2.6")
        D111d("6.3.4")
        D111a ~~~ D111b ~~~ D111c ~~~ D111d
    end

    %% Column 2 Ratings
    subgraph G112 [" "]
        direction TB
        D112a("6.1.5")
        D112b("7.1.2")
        D112c("7.1.5")
        D112d("7.1.6")
        D112a ~~~ D112b ~~~ D112c ~~~ D112d
    end

    %% Column 3 Ratings
    subgraph G113 [" "]
        direction TB
        D113a("8.1.2")
        D113b("8.1.3")
        D113c("8.1.6")
        D113d("9.4.3")
        D113a ~~~ D113b ~~~ D113c ~~~ D113d
    end

    %% Column 4 Ratings
    subgraph G114 [" "]
        direction TB
        D114a("9.3.3")
        D114b("10.2.2")
        D114c("10.3.2")
        D114d("10.4.2")
        D114a ~~~ D114b ~~~ D114c ~~~ D114d
    end

    %% Column 5 Ratings
    subgraph G115 [" "]
        direction TB
        D115a("5.4")
        D115b("5.5")
        D115c("7.1.7")
        D115d("10.5")
        D115a ~~~ D115b ~~~ D115c ~~~ D115d
    end

    %% Column 6 Ratings
    subgraph G116 [" "]
        direction TB
        D116a("12.3.1")
        D116b("12.4.1")
        D116c("12.4.2")
        D116d("12.4.3")
        D116a ~~~ D116b ~~~ D116c ~~~ D116d
    end

    %% Final Bottom Box
    Overall("Overall adequacy<br/>Fair Use, Comparability, and Appropriate Use")

    %% Layout Connections
    Main ~~~ S111 & S112 & S113 & S114 & S115 & S116

    S111 ~~~ G111
    S112 ~~~ G112
    S113 ~~~ G113
    S114 ~~~ G114
    S115 ~~~ G115
    S116 ~~~ G116

    G111 & G112 & G113 & G114 & G115 & G116 ~~~ Overall

    %% Styling
    style Main fill:#B0C4DE,color:#000,stroke:#D2691E,stroke-width:2px
    style Overall fill:#B0C4DE,color:#000,stroke:#004771,stroke-width:2px

    style S111 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S112 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S113 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S114 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S115 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px
    style S116 fill:#004771,color:#fff,stroke:#D2691E,stroke-width:2px

    %% Class definition for dashed internal items
    classDef detail fill:#004771,color:#fff,stroke:#D2691E,stroke-dasharray: 5 5;
    class D111a,D111b,D111c,D111d,D112a,D112b,D112c,D112d,D113a,D113b,D113c,D113d,D114a,D114b,D114c,D114d,D115a,D115b,D115c,D115d,D116a,D116b,D116c,D116d detail;
```

Groups, contexts, and systems should be defined by the benchmark's intended use. Relevant differences may include model family, language, modality, API versus local deployment, context window, tool access, refusal behavior, safety policy, compute budget, domain expertise, geographic or cultural coverage, user population, and accessibility needs. A benchmark may be fair for one intended context and not for another.

Section-level rating guidance:

| Rating | Guidance                                                                                                                      |
| :----: | :---------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable information is available about responsible use, comparability, accessibility, or appropriate-use limits.            |
|   1    | Benchmark conditions or documentation create serious risks of unfair, incomparable, or unsupported use.                       |
|   2    | Responsible use and comparability are partly supported, but important contexts, systems, or restrictions remain unclear.      |
|   3    | The benchmark gives clear guidance and evidence for fair, comparable use across most intended contexts.                       |
|   4    | Responsible use, accessibility, comparability, bias evidence, and appropriate-use restrictions are comprehensively addressed. |

### 11.1 Rationale and Documentation for Fair Use

This sub-section concerns whether the benchmark explains the contexts, systems, users, languages, modalities, and domains for which responsible use is intended. Reviewers should note whether exclusions are justified and visible to users.

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- Excellent: The benchmark explains whether the capability or quality it claims to measure is relevant across intended AI system classes, domains, languages, modalities, deployment contexts, and user groups, with limits and exclusions clearly justified.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.1.2 Documentation of fair-use considerations

- Excellent: Documentation gives clear details of fairness, accessibility, bias, language, domain, modality, sensitive-content, and comparability issues considered during benchmark design, evaluation, and interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 11.2 Development, Design, and Accessibility

This sub-section concerns whether fairness, accessibility, and coverage were considered during benchmark design rather than added only as post-hoc caveats. Relevant adaptations should be documented together with their consequences for score interpretation.

#### 11.2.1 Inclusive and accessible benchmark design

- Excellent: Tasks, prompts, interfaces, rubrics, and evaluation materials are designed to avoid unnecessary exclusion of relevant systems or users, with adaptations and their consequences for score interpretation documented.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.2.2 Domain, language, modality, and subgroup coverage

- Excellent: Coverage across relevant domains, languages, modalities, cultures, and subgroups is analyzed and linked to the interpretation of scores, with coverage gaps explicitly stated.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 11.3 Cross-System and Evaluation-Condition Comparability

This sub-section concerns whether different systems can be compared under conditions that preserve the intended interpretation. Differences in context length, tools, API access, local hardware, safety policies, latency limits, multimodal affordances, benchmark version, or evaluation cohort should be documented and managed.

#### 11.3.1 Cross-system comparability

- Excellent: Prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules support fair comparison across intended AI systems, including model versions, access modes, tool availability, context limits, multimodal inputs, refusals, latency constraints, and system-specific affordances.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.3.2 Access, compute, tooling, and API or local comparability

- Excellent: Access routes, compute requirements, hardware assumptions, API limitations, local execution constraints, and tool-use differences are documented and managed so that score comparisons are not distorted without warning.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- Excellent: Rolling, refreshed, or live benchmarks document evaluation dates, cohort identifiers, item-retirement rules, score normalization or equating methods where used, stale-score handling, and direct-comparison limits between models evaluated on different item sets or time windows.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 11.4 Evidence for Fairness and Bias

This sub-section concerns evidence about differential performance, scorer bias, judge bias, coverage gaps, or unequal measurement quality across relevant systems, domains, languages, modalities, user groups, or use contexts.

#### 11.4.1 Differential performance or bias analysis

- Excellent: The benchmark investigates performance differences, scorer bias, model-judge bias, language or domain bias, accessibility effects, and other differential impacts relevant to the intended use, with implications clearly explained.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- Excellent: Reliability, score stability, and validity evidence are examined across relevant subgroups, domains, languages, modalities, or system classes, and any differences are tied to interpretation limits.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 11.5 Appropriate Use and Restrictions

This sub-section concerns whether users are given clear boundaries for responsible use. Restrictions should cover both technical limits, such as unsupported systems or conditions, and interpretive limits, such as unsupported policy, procurement, safety, or broad-capability score interpretations.

#### 11.5.1 Appropriate-use guidance and non-use cases

- Excellent: The benchmark provides clear guidance about supported uses, prohibited or unsupported uses, interpretation limits, broad-score-interpretation cautions, and conditions under which comparison or deployment decisions would be inappropriate.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 11.5.2 Release rules and sensitive-content handling

- Excellent: Release rules, data access restrictions, sensitive-content warnings, privacy considerations, safety constraints, and benchmark refresh practices support fair and responsible use.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- This overall rating is based on reviewer judgment across sub-sections 11.1-11.5. Do not mechanically average ratings.
- Excellent: The benchmark actively supports fair, accessible, comparable, and appropriately bounded use across its intended systems, users, contexts, domains, languages, and modalities.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

EFPA Section 12 evaluates digitally generated reports. MESA applies that logic to AI benchmark outputs: paper tables, scorecards, leaderboards, dashboards, downloadable result files, raw traces, public interpretations made from benchmark scores, and score interpretations. A reporting output should make clear what score was produced, under what prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules, with what uncertainty, and what users should and should not infer.

This section should be completed for any reporting material that translates benchmark runs into a result used by others, even when there is no formal generated report. A static paper table, public leaderboard, hosted dashboard, badge, press release, downloadable CSV, benchmark card, or model score page can all shape interpretation and should be reviewed when it is part of the benchmark's public use.

Ratings should consider whether reports support the level of inference they invite. Rank-ordered leaderboards need clear release/version labeling, eligibility rules, uncertainty, prompts and settings, and caveats about meaningful differences. Technical score reports need enough detail for audit and reproduction. Public-facing score interpretations need stronger safeguards against overinterpretation, especially when the benchmark title implies broad intelligence or real-world readiness.

Section-level rating guidance:

| Rating | Guidance                                                                                                                                                                               |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   0    | No usable report, leaderboard, dashboard, score material, or public interpretation guidance is available.                                                                              |
|   1    | Reporting is misleading, insufficiently traceable, or likely to support unsupported interpretations.                                                                                   |
|   2    | Reporting supports cautious use but lacks important detail about uncertainty, conditions, score-to-source traceability, or interpretation limits.                                      |
|   3    | Reports are clear, traceable, and mostly sufficient for intended users, with only limited gaps.                                                                                        |
|   4    | Reporting comprehensively communicates scores, conditions, uncertainty, score-to-source traceability, validity limits, responsible-use caveats, and governance of public score claims. |

### 12.1 Scope and Coverage

This sub-section concerns whether reporting materials cover the scores, subscores, traces, and contextual information needed for the intended use without implying unsupported precision or unsupported granularity.

#### 12.1.1 Report, leaderboard, dashboard, or result artifact scope

- Excellent: Reports, leaderboards, dashboards, tables, scorecards, downloadable files, or papers cover the scores and subscores relevant to the benchmark's intended use without omitting essential context or implying unsupported granularity.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 12.1.2 Score granularity and level of detail

- Excellent: The level of detail in reported scores, subscores, item-level outputs, rankings, and qualitative labels is justified by the measurement precision, task coverage, and intended interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 12.2 Reliability and Traceability of Reports

This sub-section concerns whether a reported score can be traced to the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules that produced it and whether users can tell when differences are stable enough to interpret.

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- Excellent: Reports identify benchmark version, model version, evaluation date, cohort or rolling-window label where relevant, prompts, settings, tools, time limits, access rules, hardware, human-intervention rules, uncertainty, confidence or variability information, and whether differences are meaningful or comparable across dates or cohorts.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 12.2.2 Reproducibility and traceability of reported scores

- Excellent: Reported scores can be traced to documented runs, configurations, raw outputs or sufficient summaries, scoring code, scorer versions, build or replication status where relevant, and data or task versions needed to reproduce or audit the result.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 12.3 Relevance and Validity of Reports

This sub-section concerns whether reports connect scores to justified interpretations and avoid converting narrow task performance into unsupported score claims.

#### 12.3.1 Linkage from scores to interpretations and public claims

- Excellent: Reports clearly explain what each score supports, what it does not support, how scores relate to score interpretations, and where uncertainty, validity limits, prior-exposure risk, limits on comparing scores across time, stale scores, or score ceilings affect interpretation.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 12.3.2 Raw outputs, per-item data, or trace availability

- Excellent: Raw outputs, per-item results, traces, judge rationales, error categories, retired-item materials, signed logs, or sufficiently detailed audit materials are available or access-controlled in a way that supports independent scrutiny while respecting privacy and release limits.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 12.4 Fairness, Acceptability, and Public Communication

This sub-section concerns whether reporting language, design, access, and governance support responsible use by intended audiences and avoid misleading or unfair comparisons.

#### 12.4.1 Fairness and freedom from bias in reports

- Excellent: Reports and public materials use inclusive, non-misleading language; identify potential bias or coverage limits; and avoid interpretations that would be unfair across relevant systems, domains, languages, or user groups.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 12.4.2 Acceptability and usability for intended audiences

- Excellent: Reports are understandable, appropriately detailed, accessible, and suited to intended audiences, including technical reviewers, benchmark users, model developers, decision-makers, or the public as applicable.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

#### 12.4.3 Public communication and leaderboard governance

- Excellent: Public score interpretations, rankings, badges, headlines, and rules for leaderboard submissions, eligibility, updates, versions, ranking, audits, and public score claims are transparent, cautious, versioned, resistant to overinterpretation, and clear about update rules, eligibility, cohort or refresh labels, deprecation or archival rules, and known limitations.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

---

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- This overall rating is based on reviewer judgment across sub-sections 12.1-12.4. Do not mechanically average ratings.
- Excellent: Reporting materials make the benchmark's scores, conditions, uncertainty, validity limits, supported interpretations, unsupported uses, and public score claims clear enough for responsible use by intended audiences.
- Rating: [n/a | 0 | 1 | 2 | 3 | 4]

Review notes:

---

## Final Evaluation

### Evaluative Report of the Benchmark

This section should contain a concise, clearly argued judgment about the benchmark as a measurement instrument. It should describe its strengths and limitations, give general recommendations about how and when it may be used, and include warnings where necessary about when it should not be used. Include relevant positive or negative points about adapted, translated, derived, rolling, or versioned benchmark forms. Include comments on known ongoing research, maintenance plans, planned revisions, or future developments by the benchmark creators, maintainers, platform hosts, or suppliers.

Free Text:

### Conclusions

This section provides a summary evaluation and recommendation for use. It should consist of one or two sentences indicating the quality of the benchmark, its main supported use(s), and any important strengths or caveats. A further sentence should indicate the type and level of expertise required to administer, audit, reproduce, or interpret the benchmark responsibly, and whether this matches the benchmark creators’ or maintainers’ stated recommendations and practices.

Free Text:

### Recommendations

State what users, maintainers, or future reviewers should do next. Keep recommendations tied to the review findings.

Free Text:

### Summary of Ratings

| Section                                                      | Overall Rating (`n/a`, `0`-`4`) |
| :----------------------------------------------------------- | :-----------------------------: |
| Section 6. Rationale, documentation, and task/item quality   |                                 |
| Section 7. Benchmark materials and usability                 |                                 |
| Section 8. Reference points and documented comparison groups |                                 |
| Section 9. Reliability and precision                         |                                 |
| Section 10. Validity support                                 |                                 |
| Section 11. Fair use and comparability                       |                                 |
| Section 12. Reports, leaderboards, and public score claims   |                                 |

Review notes:

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected rating(s) | Why it matters | Needed for a higher rating |
| :------------------------------------------------------------ | :----------------- | :------------- | :------------------------- |
|                                                               |                    |                |                            |

# Editor's Prefatory Notes

## Editor Reconciliation Note

As the MESA Supervising Editor Agent, I have reconciled two independently generated draft MESA reviews for the DesignQA benchmark into a single, authoritative, source-grounded evaluation. Both reviewers operated from the same source packet and produced high-quality, comprehensive drafts. Reviewer 1 (R1) meticulously documented the automated scorer's formatting sensitivities and lexical metrics. Reviewer 2 (R2) provided a rigorous measurement-centric critique, highlighting the absence of score uncertainty reporting on subsets as small as 16 items, the legal ambiguity of the repository's missing license, and the severe validation risk posed by the authors' recommendation to fine-tune models directly on the public test set.

This final evaluation reconciles the drafts by adopting R2's more disciplined measurement perspective. We have adjusted several ratings downwards (e.g., Section 7, Section 10, and Section 12) where R1 had rated the benchmark a `3` ("mostly adequate") but R2 correctly identified important or serious evidence gaps (ratings of `2` or `1`), such as format-compliance confounding, public test leakage, and opaque leaderboard governance. The final review integrates R1's procedural precision with R2's psychometric and statistical rigor, applying the *BetterBench*, *Measuring what Matters*, and *A Definition of AGI* literature to establish a balanced and auditable benchmark profile.

## Discrepancy Summary

The following major discrepancies between the drafts were resolved based on source-grounded editorial judgment:

1. **Evaluation Setup and Instructions (Sections 6.3.1, 6.3.7):** R1 rated these a `3` due to the presence of a setup README and basic evaluation commands. R2 rated them a `2` because there are no environment lockfiles/containers, seeds, or smoke-test fixtures, requiring evaluators to reconstruct the harness and LlamaIndex dependencies. *Resolution:* Adjusted to `2`. For a reproducible benchmark, the lack of pinned dependencies and test fixtures is a significant barrier to reliable audit.
2. **Scoring Procedure and Error Handling (Section 6.3.2):** R1 rated this a `3` because the python code runs deterministically. R2 rated it a `2` because the scorer lacks error handling or format fallbacks; minor formatting deviations (e.g., a missing comma in Compilation or a recitation block in Gemini) are penalized as outright failures. *Resolution:* Adjusted to `2`. The lack of a format-recovery layer introduces substantial construct-irrelevant variance.
3. **Usability of Rubrics and Reference Answers (Section 7.1.3):** R1 rated this a `3`. R2 rated it a `2` because the Compliance subsets use only a single human-written reference explanation per item, meaning automated similarity metrics (BLEU-2/ROUGE-L) heavily penalize correct but alternative semantic descriptions. *Resolution:* Adjusted to `2`. A single reference explanation is statistically insufficient to capture the semantic space of valid engineering reasoning.
4. **License Status and Material Usability (Section 7.1.8):** R1 rated overall materials a `3` based on public GitHub availability. R2 rated them a `2` because there is no LICENSE file (live check: raw `LICENSE` returns 404, API reports `license: null`). *Resolution:* Adjusted to `2`. Under *BetterBench*, the absence of clear licensing makes reuse legally undefined, representing an important lifecycle gap that caps the usability of materials.
5. **Shortcuts and Gameability (Sections 10.3.2, 10.5.2):** R1 rated these a `2`. R2 rated them a `1`, noting that the test set is completely public and the authors explicitly recommend fine-tuning models on the Retrieval QAs (optimizing on test). *Resolution:* Adjusted to `1`. Recommending fine-tuning on the test set directly violates machine learning train/test separation, and unmitigated format strictness means scores heavily reflect formatting rather than engineering capabilities.
6. **Stated Claims Proportionality (Section 10.6.1):** R1 rated this a `2` due to the broad "engineering documentation understanding" title. R2 rated it a `3` because the paper itself is exceptionally transparent about limitations (single document, limited tasks, metric weaknesses) and makes no AGI claims. *Resolution:* Adjusted to `3`. Stated claims in the core paper are highly disciplined and bounded, even if some public-facing dashboard context could be improved.
7. **Leaderboard Governance (Section 12.4.3):** R1 rated this a `2`. R2 rated it a `1` due to the manual update mechanism, lack of eligibility rules, and the fact that the live results table was unrenderable at access time. *Resolution:* Adjusted to `1`. The lack of formal governance, uncertainty reporting, and transparent submission tracking makes the leaderboard weak as a comparison tool.

## Unresolved Evidence Gaps

1. **Licensing Status:** There is no LICENSE file in the official repository. Legal reuse and redistribution rights remain unresolved.
2. **Human Performance Baseline:** No human or expert accuracy scores are provided for any of the benchmark subsets, preventing comparison between AI models and human engineers.
3. **Score Uncertainty:** There are no confidence intervals, standard errors, or multi-run variance reports for the main model cohort (GPT-4o, GPT-4, Claude-Opus, Gemini-1.0) under the AllRules or RAG conditions.
4. **Leaderboard Governance and Opaque Dashboard:** The live leaderboard's results table and submission tracking details were unrenderable at the access date, and no formal rules exist for handling stale scores, model updates, or fine-tuned-on-test entries.
5. **Semantic Explanation Validation:** The automatic explanation metrics (BLEU-2, ROUGE-L, Sentence-BERT) have not been validated against human ratings of explanation correctness.

## Interpretation Cautions

1. **Bounded Construct Validity:** DesignQA does not measure general intelligence, AGI, or broad engineering design competence. It measures a model's ability to locate, recognize, and check compliance of specific Formula SAE rules and vehicle-design artifacts. Do not generalize scores beyond this context.
2. **Statistical Noise on Small Subsets:** Subsets such as Functional Performance (16 items), Compilation (30 items), and Definition (31 items) are extremely small. A single item in Functional Performance changes accuracy by 6.25 percentage points. Differences of less than 10-15 percentage points on these subsets should be treated as noise rather than meaningful model differences.
3. **Format and Verbosity Bias:** Scores are highly sensitive to response formatting (such as comma-separated lists) and explanation length (BLEU/ROUGE penalize long answers and reward brief summaries). Score differences may reflect format-following capability rather than engineering comprehension.
4. **Contamination and Tuning Risks:** The dataset is fully public, and the rules are web-searchable. High Retrieval scores, in particular, may reflect prior exposure or test-set tuning rather than generalized search capability.

---

# MESA Review: DesignQA

## Short Stand-Alone Non-Evaluative Benchmark Description

DesignQA is a public multimodal question-answering benchmark for evaluating multimodal large language models (MLLMs) on understanding and applying engineering requirements in technical documentation. Developed by researchers at MIT and Autodesk Research (Doris et al., 2024), the benchmark uses the 140-page Formula SAE (FSAE) 2024 rule document alongside 3D CAD models and test data from the MIT Motorsports team. It consists of 1,451 question-answer pairs divided into three segments: Rule Extraction, Rule Comprehension, and Rule Compliance. These segments are further split into six subsets: Retrieval (1,192 QAs), Compilation (30), Definition (31), Presence (62), Dimension (120), and Functional Performance (16). Its defining feature is document-grounded, multi-source visual question-answering: the input images (CAD views or engineering drawings) and input rules are from different sources, and the images are novel to the models. Every subset is scored automatically using metrics such as F1 variants, accuracy, and BLEU-2/ROUGE-L/Sentence-BERT similarity for compliance explanations.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt | Description |
| :--- | :--- |
| Reviewer Name | MESA Supervising Editor Agent (Reconciled Evaluation) |
| Date of Current Review | 2026-06-28 |
| Date of Previous Review | n/a |

### 1.2 Benchmark Identity & Provenance

| Prompt | Description |
| :--- | :--- |
| Reviewed Entity Name | DesignQA public benchmark: paper-described dataset, public GitHub repository, and official website leaderboard. |
| Short Name / Acronym | DesignQA |
| Entity Type | Original multimodal benchmark dataset with public evaluation code and manually maintained leaderboard. |
| Parent / Source Benchmark | n/a. Constructed from 2024 Formula SAE rules and MIT Motorsports CAD data. |
| Exact Version / Release Split | arXiv:2404.07917v2 (August 23, 2024); public GitHub `main` branch. No separate public train/dev/test splits. |
| Implementation / Scorer Version | Public repository evaluation scripts: `eval/full_evaluation.py` and `eval/metrics/metrics.py`. No package version or release tag. |
| Creators & Current Maintainers | Anna C. Doris, Daniele Grandi, Ryan Tomich, Md Ferdous Alam, Mohammadmehdi Ataei, Hyunmin Cheong, and Faez Ahmed. |
| Host Organization / Repository Owner | Official repository: `anniedoris/design_qa`; website: `design-qa.github.io`. Affiliations: MIT, Autodesk Research, MIT Motorsports. |
| Release Dates | arXiv v1: April 11, 2024; arXiv v2: August 23, 2024. Last repository push: 2025-08-10. |
| License & Access Terms | Public GitHub repository. No LICENSE file is present (raw `LICENSE` returns 404, GitHub API reports `license: null`). |
| Persistent Identifier / DOI / Citation | arXiv:2404.07917. Journal: Doris et al., Journal of Computing and Information Science in Engineering, 25(2), 021009, 2025. |

### 1.3 Materials, Sources, & Access Tracking

| Material / Source Type | URL, Location, or Identifier | Access Date |
| :--- | :--- | :--- |
| Paper / Technical Report | `literature/DesignQA.md`; `Papers/DesignQA.pdf`; <https://arxiv.org/abs/2404.07917> | 2026-06-28 |
| Website / Documentation Hub | <https://design-qa.github.io/> | 2026-06-28 |
| Code Repository | <https://github.com/anniedoris/design_qa/> | 2026-06-28 |
| Dataset / Task / Prompt Set | GitHub repository `dataset/` subfolders (`rule_extraction/`, `rule_comprehension/`, `rule_compliance/`) | 2026-06-28 |
| Evaluation Harness / Runner | `eval/full_evaluation.py` (produces `results.txt`); `eval/metrics/metrics.py` | 2026-06-28 |
| Leaderboard / Results Portal | `design-qa.github.io` leaderboard; submission via GitHub issue. | 2026-06-28 |
| Guides (User/Scoring/Rubric) | Repository README setup and evaluation instructions; paper Section 3.2 | 2026-06-28 |
| Contextual Literature | `literature/betterbench.md`, `literature/Measuring_what_Matters.md`, `literature/A_Definition_of_AGI.md` | 2026-06-28 |
| Feedback / Contact Channels | GitHub issues on `anniedoris/design_qa`; corresponding author email: adoris@mit.edu | 2026-06-28 |

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

- [ ] Not explicitly stated
- [ ] General Knowledge (K)
- [x] Reading and Writing Ability (RW) *(Comprehension and rule extraction)*
- [x] On-the-Spot Reasoning (R) *(Applying rules to drawings)*
- [ ] Working Memory (WM)
- [ ] Long-Term Memory Storage (MS)
- [ ] Long-Term Memory Retrieval (MR)
- [x] Visual Processing (V) *(CAD views, engineering drawings, performance charts)*
- [ ] Auditory Processing (A)
- [ ] Speed (S)
- [ ] Coding or software engineering
- [x] Specialized scientific or technical expertise *(Multimodal engineering requirements QA)*
- [x] Domain-specific professional expertise *(Vehicle design compliance)*
- [ ] Tool use
- [ ] Agency or autonomy
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [x] Factuality or grounding *(Verbatim rule retrieval and compliance checking)*
- [ ] Multilingual or cross-cultural capability
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [ ] Calibration or uncertainty

*Reviewer comments:* The benchmark targets the synthesis of visual design artifacts (CAD/drawings) and long-context rules from different sources, where the images are novel to the models. Stated claims map strictly to requirements-engineering subskills; the authors make no general intelligence or AGI claims.

### 2.2 Area of Use

- [ ] Not explicitly stated
- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [ ] Public communication or marketing

### 2.3 Intended AI Systems

- [ ] Not explicitly stated
- [x] Frontier general-purpose language models
- [x] Multimodal models
- [x] Chat or instruction-following models
- [x] Retrieval-augmented systems *(RAG is an explicit evaluation condition)*
- [x] Open-weight local models *(e.g., LLaVA-1.5)*
- [x] API-hosted models

### 2.4 Intended Users of Benchmark Outputs

- [ ] Not explicitly stated
- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [x] Public leaderboard users

### 2.5 Task Families, Subdomains, and Scores

| Component | Description |
| :--- | :--- |
| Capability the benchmark claims to measure | Multimodal engineering documentation understanding and requirements compliance reasoning. |
| Definition of the capability being measured | Locating relevant rule text, recognizing component terminology in CAD images, and checking design compliance with dimensional and functional rules. |
| Subcomponents of the capability | Rule Extraction (Retrieval, Compilation); Rule Comprehension (Definition, Presence); Rule Compliance (Dimension, Functional Performance). |
| Excluded scope or non-target abilities | Non-design rule sections (administrative, document format) are excluded; no claim to general world knowledge, autonomy, or multi-document synthesis. |
| Benchmark item families or subdomains | Verbatim rule text QA, rule-compilation-by-topic QA, component-naming VQA, component-presence yes/no VQA, dimensional-compliance VQA, and functional-performance compliance VQA. |
| Sources for benchmark items | Formula SAE 2024 rule document; four MIT Motorsports CAD models (vehicle, aero, wheel, powertrain); MIT Motorsports test and FEA data. |
| Sampling method | Programmatic regex extraction for Retrieval/Compilation; manual expert authoring and cross-review by MIT Motorsports, industry, and academic authors for other subsets. |
| Splits or partitions | Single fully public static split. No hidden dev/test or private splits. |
| Primary score | Per-subset automatic metrics. Scorer writes results to `results.txt`. README describes overall score as a simple average of the six subsets. |
| Subscores | Retrieval F1 BoW; Compilation F1 Rules; Definition F1 BoC; Presence ACC; Dimension ACC; Functional Performance ACC; and Compliance explanation BLEU-2, ROUGE-L, and SBERT Similarity. |
| Qualitative score ranges | None defined. |
| Boundaries or caveats | Authors caveat that the benchmark uses a single rule document, has small subsets, and is sensitive to prompt/image formats and automatic metric limits. |

### 2.6 Model Response Mode

- [ ] Not explicitly stated
- [x] Short text *(rule text, lists, component names, yes/no)*
- [x] Long-form text *(compliance explanations)*
- [x] Structured output *(comma-separated lists of rules)*
- [x] Yes/no decision

### 2.7 Prerequisites for Evaluated Systems

| Requirement | Irrelevant / Not necessary | Necessary information given | Information missing |
| :--- | :---: | :---: | :---: |
| Long-context support (for AllRules) | [ ] | [x] | [ ] |
| Multimodal input capability | [ ] | [x] | [ ] |
| Exact response-format following | [ ] | [x] | [ ] |
| API or local inference procedure | [ ] | [x] | [ ] |
| Cost and compute budget | [ ] | [ ] | [x] |

### 2.8 Evaluation Conditions

| Condition | Description |
| :--- | :--- |
| Prompting protocol | Zero-shot, using fixed prompt templates per subset appended to a shared student-engineering preamble. |
| Context provision | AllRules (full rule document in context, ~70,091 tokens) or simple LlamaIndex RAG (top-15/top-12 chunks embedded via OpenAI `text-embedding-3-large`). |
| Sampling settings | LlamaIndex defaults: temperature 0.1 for closed models; 0.75 and top_p 0.9 for LLaVA-1.5. max_new_tokens: 250 (Extraction), 100 (Comprehension), 1500 (Compliance). |
| Tool permissions | None. RAG context is injected directly into prompts. |
| Special administration conditions | Claude-Opus tested RAG-only due to input cost. Gemini-1.0-RAG scored 0 on Retrieval due to a RECITATION block. Definition subset: RAG models received no retrieved context. |

### 2.9 Task Interaction and Observable Evidence Types

- [x] Static item or prompt response
- [x] Document-grounded QA
- [x] Visual QA
- [x] Response text
- [x] Structured or constrained output
- [x] Per-item predictions in CSV form

### 2.10 Input Stimulus Type

- [x] Long-form technical text *(FSAE rules)*
- [x] CAD-derived images *(multi-view, close-ups)*
- [x] Engineering drawings *(direct-dimensioned, scale-bar)*
- [x] Functional performance visuals or charts *(FEA stress plots, anthropometric charts)*

### 2.11 Number of Items or Measurement Points

- Total public tasks: 1,451 static items.
- Item counts by subset: Retrieval 1,192; Compilation 30; Definition 31; Presence 62; Dimension 120; Functional Performance 16.

### 2.12 Mode of Evaluation

Local offline scoring scripts evaluate predictions and write `results.txt`. The public leaderboard submission route is manual, mediated by filing a GitHub issue.

### 2.13 Technological Arrangements

Orchestration is Python-based using LlamaIndex. Embeddings for RAG are generated using OpenAI's `text-embedding-3-large`.

### 2.14 Time and Resource Requirements

AllRules context injection requires a window of at least 70,091 tokens. API costs are substantial (>10x simple RAG). RAG limits context to ~8,700–10,900 characters on average.

### 2.15 Benchmark Forms, Versions, and Variants

Single static public form. Context-delivery conditions (AllRules, simple RAG, GuaranteedRAG) represent evaluation settings, not separate forms.

### 2.16 Static or Dynamic Task Determination

Static. The task set remains fixed.

### 2.17 Evidence Sources Used in Scoring

automated scoring comparing model outputs to ground-truth answers (text, rule lists, component names, yes/no labels, human-written explanations).

### 2.18 Broad-Claim Flags for Later Evaluation

Stated claims include "understanding engineering documentation" and "real-world engineering design compliance checking". DesignQA makes no claims regarding AGI or general intelligence.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

Scoring is automated. Predictions are provided in subset-specific CSVs. The python scorer calculates F1 Bag-of-Words (Retrieval), F1 Rules (Compilation), F1 Bag-of-Characters (Definition), Accuracy (Presence, Dimension, Functional Compliance), and similarity metrics (BLEU-2, ROUGE-L, SBERT Cosine Similarity) for explanations. Submissions to the leaderboard are manually verified.

### 3.2 Scores and Metrics

- **Retrieval:** F1 Bag-of-Words after lowercasing and punctuation removal.
- **Compilation:** F1 over rule-number lists.
- **Definition:** F1 Bag-of-Characters (max score over component synonyms).
- **Presence:** Accuracy on yes/no.
- **Dimension & Functional Compliance:** Accuracy on yes/no; BLEU-2, ROUGE-L, and SBERT embedding cosine similarity are reported for explanations.
- **Overall:** Simple average across subset scores (README specification).

Format errors are not handled dynamically; format failures (e.g., missing commas or recitation blocks) result in a score of 0.

### 3.3 Scale or Metric Types

All metrics are bounded in [0,1], with higher scores representing closer matches. F1 and similarity metrics allow partial credit; accuracy is binary.

### 3.4 Score Transformation

No score transformations (such as standardization, Equating, or norming) are applied. Macro-averages within subsets and a simple overall average are reported.

### 3.5 Documented Reference Groups, Baselines, and Comparators

- **Naive Baselines:** Random rule selection (Retrieval, Compilation), random words (Definition), and 50% random guessing (Accuracy subsets).
- **Model Cohort:** Baseline results for GPT-4o, GPT-4, Claude-Opus, Gemini-1.0, and LLaVA-1.5 are reported.
- **Human Baseline:** Absent. No human baseline is provided to anchor scores.

### 3.6 Score Uncertainty and Stability

Point estimates only. No confidence intervals or standard errors are reported for the main model cohort. Standard deviation is reported only for the 5-run LLaVA-1.5 GuaranteedRAG diagnostic.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

Scores represent a model's capacity to handle the specific tasks and formatting rules of the DesignQA subsets. The authors explicitly identify automatic metric limits, such as format penalties, child-rule false negatives, and BLEU/ROUGE brevity bias.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

Granular paper tables and local `results.txt` files containing subset and per-question scores are available. Complete raw model responses for the paper runs are not released as a dataset. The leaderboard is hosted at `design-qa.github.io`. No confidence intervals, error bars, submission-metadata catalogue, or leaderboard snapshot export is published.

### 4.2 Output Name or Description

| Output | Description | Public/private | Maintainer / host |
| :--- | :--- | :--- | :--- |
| Paper Tables 2-5 (arXiv v2) | Per-subset model and baseline scores; GuaranteedRAG diagnostic; component-mention-type breakdown; dimensioning-system effect | Public | Authors |
| `results.txt` (scorer output) | Overall simple-average score plus per-question diagnostic scores for a submitted run | Local, submitter-generated | Evaluator |
| DesignQA leaderboard | Community-submitted model scores at `design-qa.github.io` | Public | Maintainers, issue-mediated and manually verified |

### 4.3 Output Design or Presentation

The paper presents static tables by subset and model condition. The repository scorer produces a plain-text results file. The official website presents public benchmark information and a leaderboard route. Dataset CSVs and `results.txt` are downloadable. There is no interactive dashboard, results API, or graph-based primary output surface.

### 4.4 Output Structure

Results are reported by task family (per-subset scores) and broken down by diagnostic parameters in the paper (mention type, dimensioning system, and context). Reporting is additionally error-analysis based (qualitative failure modes per subset) and rank based (best-performer comparisons). No capability-domain profile, criterion threshold, cost-adjusted, or difficulty-band reporting is defined.

### 4.5 Sensitivity to Context

No context-dependent reporting formatting is defined; a single leaderboard represents all model types. The paper does study sensitivity to rule-context delivery, contrasting AllRules, simple RAG, and GuaranteedRAG, along with drawing dimensioning type and additional image or prompt context, but these are paper diagnostics rather than a formal uncertainty model applied to all submissions.

### 4.6 Development of Outputs

Outputs derive from the benchmark authors' design and from automated scoring scripts, with human annotation supplying the manually authored QA items and the human reference explanations. Leaderboard entries require manual verification by the maintainers according to the repository README. No model-as-judge or platform-generated scoring is used.

### 4.7 Modifiability

Users may run the public scorer against their own prediction CSVs, and the scoring logic can be inspected and modified locally. Modification is therefore limited to the submitter's own run. No formal versioning policy governs modified scorers or forked benchmark forms.

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

The paper and README link each subset to a specific task family, scoring metric, and engineering-skill interpretation, giving clear task-to-score-to-label traceability. The overall score is documented as a simple average across the six segments, which is transparent but material to interpretation because segment item counts differ by nearly two orders of magnitude (1,192 versus 16).

### 4.9 Output Content

Outputs include numeric subset scores, per-subset diagnostics, per-question scores, aggregate best-performer rankings, error categories, worked success and failure examples (Figure 3), explicit caveats in the Limitations section, and future-work interpretation notes. No model card, benchmark card, capability-domain profile, confidence-interval report, cost or latency data, or signed audit log was identified.

### 4.10 Intended Recipients

Primary recipients are AI researchers, model developers, benchmark maintainers, engineering-design researchers, and public leaderboard readers. Safety evaluators, policy actors, and procurement audiences are not named as intended recipients.

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

Fully public repository and website. No hidden splits or private scorers. Materials present are the arXiv technical report, the repository README, scoring documentation in the README and metric code, and worked evaluation examples. No user guide, API documentation, dataset card, rubric or annotation guide, FAQ, or changelog was identified.

### 5.2 Distribution and Access Model

Access is fully public, with a leaderboard-only submission route mediated by filing a GitHub issue with results and code for manual verification. No private, semi-private, or controlled-access split was identified, and all items, answers, and the source rule text are public.

### 5.3 Methods of Publication

| Publication route | Description |
| :--- | :--- |
| arXiv | Public paper at arXiv:2404.07917. |
| Journal | Journal of Computing and Information Science in Engineering, 25(2), 021009, 2025. |
| GitHub repository | Dataset, evaluation code, README, and scripts. |
| Official website | Project page and leaderboard route at `design-qa.github.io`. |

### 5.4 User Requirements or Qualifications

Users need Python and command-line ability, access to a model capable of handling the relevant text and visual inputs (provider API keys for closed models, or local weights for LLaVA-1.5), OpenAI embedding credentials for the RAG condition, the ability to format predictions into the expected CSV files, and a GitHub account to file a leaderboard issue. Engineering-domain familiarity is helpful for interpreting results but is not required to run the benchmark. No formal user qualification, licence acceptance, eligibility term, or data-use obligation was identified.

### 5.5 Dataset and Item Access

Public evaluation items, answer keys, metadata, and human verification labels are all openly available in the repository, together with the dataset CSVs and image folders. No training or development split, private or held-out evaluation set, secret reserve, private leaderboard set, or retired-item archive exists. Raw model outputs from the paper runs are not released as a dataset, and submitted model traces are not centrally archived. The Formula SAE rules serve as the source document, extracted and filtered from the published PDF.

### 5.6 Provenance and Contamination Documentation

Provenance is well-documented (Formula SAE rules and MIT Motorsports CAD data), including source-material dating, contributor qualifications, and the authors' statement that the visual inputs were not seen by models during pre-training in the same form. Contamination audits, canary strings, deduplication or overlap checks, prior-exposure screening, and training-data filters are absent. There is no dataset DOI, no leak-response or rerun policy, and no training-use prohibition. The rules are public and web-searchable, and the paper recommends using the Retrieval QAs for model fine-tuning, which amounts to optimising directly against released test items.

### 5.7 Reproducibility Materials

| Material | Availability |
| :--- | :--- |
| Dataset files | Public in repository. |
| Prompt templates | Public in paper and README. |
| Administration and scoring code | Public (`eval/full_evaluation.py`, `eval/metrics/metrics.py`). |
| Setup instructions | Public README with conda and Python 3.10 setup. |
| Example evaluation command | Public README includes the full evaluation command and a LLaVA example. |
| Model-generation code for all paper results | Not established from the inspected sources. |
| Exact model API versions and settings | Paper appendix documents model identifiers and some LlamaIndex defaults. |
| Environment lockfile or container | Requirements file exists; no container or lockfile identified. |
| Random seeds or deterministic settings | Absent. |
| Smoke-test fixtures, expected outputs, or CI | Absent. |
| One-command reproduction of published tables | Absent. |

### 5.8 Maintenance and Versioning

No formal release tags, changelogs, or deprecation rules are provided. The leaderboard is updated manually via GitHub issues, with no documented submission eligibility, rerun, stale-score, or model-version update policy. Maintainer identity is the corresponding author (`anniedoris`) and co-authors, with no named ongoing maintenance team. The repository has no GitHub Releases and no CI or build status, and presents 166 commits with an active issue queue (13 open at access date). Last repository push occurred on 2025-08-10, and a README note referencing an IDETC Hackathon 2025 indicates continuing use beyond the original paper. Long-term archival rests on arXiv for the paper and GitHub for data and code, with no DOI archive or mirror identified.

---

## Appendix A. General Description of the Benchmark

DesignQA is a public multimodal question-answering benchmark that tests whether multimodal large language models can locate, interpret, and apply engineering requirements drawn from a real technical document. It pairs the 140-page Formula SAE 2024 rule document with CAD models, engineering drawings, and test data from the MIT Motorsports team, producing 1,451 question-answer pairs across three segments (Rule Extraction, Rule Comprehension, Rule Compliance) and six subsets (Retrieval, Compilation, Definition, Presence, Dimension, Functional Performance). Its distinguishing feature is multi-source visual question answering: the input image and the governing rule text come from different sources, and the images were not part of model pre-training in the same form. Every subset is scored automatically, using F1 variants, accuracy, and BLEU-2/ROUGE-L/Sentence-BERT similarity for compliance explanations, so new systems can be scored without human raters. Models are evaluated under two context-delivery conditions, full rules in context (AllRules) and a LlamaIndex retrieval pipeline (RAG), with a keyword-matched GuaranteedRAG diagnostic. The benchmark, its answer keys, and its scorer are distributed publicly through the `anniedoris/design_qa` repository and an official website carrying a manually maintained, issue-mediated leaderboard.

---

# Part B. Evaluation of the Benchmark

## Section 6. Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition
- **Rating:** 3
- **Evidence:** The paper defines a clear, domain-specific construct: applying engineering requirements from technical documentation. It decomposes this into a logical extraction → comprehension → compliance workflow, and justifies the multi-source VQA gap (Table 1).
- **Missing evidence:** The capability is operationalized through a single rulebook (Formula SAE), leaving the broader construct "engineering requirements understanding" defined primarily by this document.
- **Reviewer/editor rationale:** The construct is well-defined and bounded, but the single-document scope holds it short of a 4.
- **Interpretation caution:** Read scores as performance on FSAE-style requirements QA, not engineering design understanding in general.

#### 6.1.2 Summary of prior research and benchmark context
- **Rating:** 3
- **Evidence:** Section 2 situates DesignQA against reference-dependent text QA, VQA benchmarks, and the PURE requirement dataset, establishing a clear classification of reference types.
- **Missing evidence:** Lack of integration with psychometric or measurement-quality literature.
- **Reviewer/editor rationale:** Strong contextualization within the contemporary AI benchmark landscape.

#### 6.1.3 Phenomenon-task-metric-claim chain
- **Rating:** 3
- **Evidence:** The chain from engineering workflow to subsets to metrics is explicit. The authors identify key metric limitations, such as formatting penalties, child-rule inclusion, and BLEU/ROUGE brevity bias.
- **Missing evidence:** Confounds are acknowledged but not corrected or statistically modeled.
- **Reviewer/editor rationale:** The chain is coherent and highly self-aware, though weakened by unmitigated metric artifacts.
- **Interpretation caution:** Some score variation reflects formatting and verbosity style rather than the target engineering capability.

#### 6.1.4 Task or item design
- **Rating:** 3
- **Evidence:** Items are purpose-built (multi-view CAD, close-ups, direct and scale-bar drawings, positive/negative compliance pairs).
- **Missing evidence:** No scale-bar-violating drawings were created because the source CAD was inherently rule-compliant, resulting in a design asymmetry in the Dimension subset.
- **Reviewer/editor rationale:** Bounded but highly thoughtful, domain-grounded task designs.

#### 6.1.5 Procedures for developing task or item content
- **Rating:** 3
- **Evidence:** Retrieval/Compilation ground truths were generated programmatically. Comprehension/Compliance items were authored by MIT Motorsports members, Autodesk engineers, and academic researchers, with cross-review by two non-authoring parties.
- **Missing evidence:** Quantitative inter-annotator agreement statistics are absent, and compliance explanations were not extensively reviewed.
- **Reviewer/editor rationale:** The manual review process by domain experts represents a major strength compared to typical synthetic datasets, but the lack of agreement statistics is a gap.

#### 6.1.6 Thoroughness of the final task or item selection process
- **Rating:** 2
- **Evidence:** The selection rules are described (filtering rules, 30 compilation terms, 31 components, 20 dimension rules).
- **Missing evidence:** The manual subsets are small convenience samples limited by test-data availability (Functional Performance has only 16 items). No systematic coverage matrix is provided.
- **Reviewer/editor rationale:** Bounded by material availability; small sample sizes require strict uncertainty caveats.
- **Interpretation caution:** Small subsets sample a very narrow slice of possible requirements tasks.

#### 6.1.7 Quantitative evidence of task or item quality
- **Rating:** 2
- **Evidence:** Naive baselines establish floor difficulty. Subsets near chance (Compilation, Definition, Presence) are highlighted.
- **Missing evidence:** No item difficulty parameters, item discrimination, or IRT-style statistics are reported.
- **Reviewer/editor rationale:** Floor behavior is established, but formal psychometric item validation is absent.

#### 6.1.8 Adaptation, translation, source reuse, or benchmark slice
- **Rating:** n/a
- **Evidence:** DesignQA is a newly constructed benchmark, not an adaptation or slice of a prior benchmark.

#### 6.1.9 Overall Rationale, development, and task or item quality
- **Rating:** 3
- **Reviewer/editor rationale:** Clear construct, expert-driven authoring, and custom multimodal designs support qualified diagnostic use. Small convenience samples and absent item statistics are minor gaps that constrain but do not void the section.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use
- **Rating:** 3
- **Evidence:** Stated purpose, intended systems, and per-subset skill interpretations are documented in the paper and README.
- **Missing evidence:** No explicit list of non-use cases or safety restrictions.

#### 6.2.2 Documentation of development process
- **Rating:** 3
- **Evidence:** Sections 3.1.1–3.1.4 describe item generation, CAD representation, and the cross-review protocol.
- **Missing evidence:** Detailed annotator guidelines or review logs are missing.

#### 6.2.3 Documentation of scoring and metrics
- **Rating:** 3
- **Evidence:** Metric formulas and scoring examples are public. Scorer code is open and inspectable.
- **Missing evidence:** Standalone scoring specification detailing edge-case handling is missing.

#### 6.2.4 Documentation of reliability, stability, and uncertainty
- **Rating:** 1
- **Evidence:** Run-to-run variance is reported only for the LLaVA-1.5 GuaranteedRAG diagnostic experiment.
- **Missing evidence:** No confidence intervals, standard errors, or multi-run variance are reported for the main model cohort (GPT-4o, GPT-4, Claude-Opus, Gemini-1.0).
- **Reviewer/editor rationale:** Point estimates reported on subsets of 16 to 31 items without uncertainty representation are a major evidence gap.
- **Interpretation caution:** Do not treat minor score differences as meaningful.

#### 6.2.5 Documentation of validity evidence
- **Rating:** 2
- **Evidence:** Face/content validity via expert authoring is strong; qualitative error analyses are provided.
- **Missing evidence:** No convergent/discriminant validity study or external criterion correlation.

#### 6.2.6 Documentation of fair use and comparability
- **Rating:** 2
- **Evidence:** Exact model IDs, default parameters, and context-delivery conditions are documented.
- **Missing evidence:** Omission of Claude-Opus AllRules (cost) and Gemini's RECITATION zero are noted but not normalized. No comparability guidelines are provided.

#### 6.2.7 Documentation of maintenance and versioning
- **Rating:** 2
- **Evidence:** The public repository is maintained, and issues are monitored. The website hosts a manually updated leaderboard.
- **Missing evidence:** No release tags, versioned branches, or deprecation policies. Last push occurred in August 2025.
- **Reviewer/editor rationale:** Maintenance is active but informal, lacking standard version control tags.

#### 6.2.8 Adequacy of documentation overall
- **Rating:** 2
- **Reviewer/editor rationale:** Strong on purpose and scoring; weak on uncertainty, validity limits, and lifecycle tags.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration
- **Rating:** 2
- **Evidence:** README documents dataset paths and the `full_evaluation.py` command.
- **Missing evidence:** No dependency lockfiles, containers, or random seed configurations are provided. Evaluators must build their own model integration wrappers.
- **Reviewer/editor rationale:** Setup is runnable by research users, but lacks reproducibility guards.

#### 6.3.2 Scoring procedure and error handling
- **Rating:** 2
- **Evidence:** Deterministic python scoring code is public.
- **Missing evidence:** No format recovery or fallback retries; format errors are penalized as failures.
- **Reviewer/editor rationale:** Strict format scoring introduces construct-irrelevant variance.

#### 6.3.3 Interpretation and reporting guidance
- **Rating:** 2
- **Evidence:** Qualitative failure modes and an explicit Limitations section are provided.
- **Missing evidence:** No statistical guidance on significant score thresholds.

#### 6.3.4 Restrictions, prerequisites, and appropriate use
- **Rating:** 2
- **Evidence:** Hardware limits (AllRules cost) and modality requirements are stated.
- **Missing evidence:** No legal license is provided, and no explicit appropriate-use boundaries are documented.

#### 6.3.5 Technical support and implementation guidance
- **Rating:** 2
- **Evidence:** GitHub issue tracker and corresponding author email are available.
- **Missing evidence:** No troubleshooting FAQ or test fixtures.

#### 6.3.6 References and supporting materials
- **Rating:** 3
- **Evidence:** Standard academic citations are thorough and cross-linked.

#### 6.3.7 Quality of procedural instructions overall
- **Rating:** 2
- **Reviewer/editor rationale:** Usable for research replication, but requires unguided environment reconstruction.

### 6.4 Overall Adequacy of Rationale and Documentation
- **Rating:** 3
- **Reviewer/editor rationale:** Clear construct, expert-driven authoring, and transparent limitations represent a solid foundation. The rating is limited to a 3 by thin uncertainty documentation and the lack of version control and licensing.

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability
- **Rating:** 3
- **Evidence:** Complete CSV data, CAD images, engineering drawings, and answers are public.
- **Missing evidence:** No dataset card, dataset DOI, or license is provided.
- **Reviewer/editor rationale:** Materials are highly accessible, but the lack of a license creates legal ambiguity.

#### 7.1.2 Prompts, instructions, and input materials
- **Rating:** 3
- **Evidence:** Zero-shot prompt templates and image inputs are clearly specified.

#### 7.1.3 Rubrics, reference answers, and response format requirements
- **Rating:** 2
- **Evidence:** Exact answer keys are provided for closed subsets. Format requirements are explicit.
- **Missing evidence:** Compliance explanations use only a single human-written reference explanation, making BLEU-2/ROUGE-L scoring highly sensitive to phrasing.
- **Reviewer/editor rationale:** Strict formatting rules and single-reference explanation keys introduce significant scoring noise.
- **Interpretation caution:** Explanation scores measure similarity to a single human's phrasing, not semantic correctness.

#### 7.1.4 Evaluation harness, scorer, and implementation quality
- **Rating:** 2
- **Evidence:** Python scripts evaluate predictions and output a results file.
- **Missing evidence:** No CI checks, container, unit tests, or scorer version tags.
- **Reviewer/editor rationale:** Usable but lacks validation and environment pinning.

#### 7.1.5 Interface and workflow usability
- **Rating:** 3
- **Evidence:** A simple command executes scoring. Dataset folders are logically organized.

#### 7.1.6 Accessibility across modalities, languages, and system types
- **Rating:** 2
- **Evidence:** Harness supports API-based and local models. Text-only items use null images.
- **Missing evidence:** English-only; models with small context windows are structurally disadvantaged without a RAG pipeline.

#### 7.1.7 Licensing, use requirements, and risk warnings
- **Rating:** 1
- **Evidence:** Fully public files.
- **Missing evidence:** The repository lacks a LICENSE file (`license: null`).
- **Reviewer/editor rationale:** For a public benchmark soliciting community submissions, the complete absence of a license is a serious compliance gap.
- **Interpretation caution:** Redistribution and reuse rights are legally undefined.

#### 7.1.8 Overall quality of benchmark materials
- **Rating:** 2
- **Reviewer/editor rationale:** Materials are organized and functional, but limited by the lack of licensing, absence of containers/CI, and single-reference explanation rubrics.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines
- **Rating:** 3
- **Evidence:** Naive baselines are empirically computed and reported for each subset.
- **Missing evidence:** No empirical upper ceiling (e.g., human expert accuracy or oracle context) is provided.

#### 8.1.2 Human or expert baselines
- **Rating:** 1
- **Evidence:** Experts created and reviewed the items.
- **Missing evidence:** No human or expert accuracy baseline was run or reported.
- **Reviewer/editor rationale:** Without human scores on the same task, model performance cannot be calibrated against human competence.
- **Interpretation caution:** Do not interpret accuracy scores as relative to human engineering performance.

#### 8.1.3 Model comparator cohort
- **Rating:** 3
- **Evidence:** Five contemporary models (GPT-4o, GPT-4, Claude-Opus, Gemini-1.0, LLaVA-1.5) are evaluated under documented conditions.
- **Missing evidence:** Claude-Opus was tested RAG-only. Standard errors are missing.

#### 8.1.4 Historical, version, or benchmark-family comparators
- **Rating:** n/a
- **Evidence:** DesignQA is a first-release benchmark; no historical versions exist.

#### 8.1.5 Criterion thresholds, score bands, or performance categories
- **Rating:** n/a
- **Evidence:** No pass/fail thresholds or qualitative competence bands are defined.

#### 8.1.6 Representativeness of reference groups
- **Rating:** 2
- **Evidence:** Cohort includes major 2024 frontier models.
- **Missing evidence:** No human reference groups or systematic model sampling.

#### 8.1.7 Currency and maintenance of baseline evidence
- **Rating:** 2
- **Evidence:** Cohort was current at publication; leaderboard permits new entries.
- **Missing evidence:** No documented schedule for re-running baseline models or handling model decay.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation
- **Rating:** 2
- **Reviewer/editor rationale:** Naive floors and a diverse model cohort are useful. The rating is held to 2 by the complete absence of human baseline scores and score uncertainty.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence
- **Rating:** 1
- **Evidence:** Standard deviation is reported only for the 5-run LLaVA-1.5 GuaranteedRAG diagnostic experiment.
- **Missing evidence:** No multi-run or prompt stability reports for the main cohort under AllRules or RAG conditions.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings
- **Rating:** 1
- **Evidence:** Temperatures (0.1 / 0.75) are documented.
- **Missing evidence:** No seeds are provided, and no repeated runs exist for the main cohort. Single-run scores carry unquantified decoding variance.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors
- **Rating:** 1
- **Evidence:** Standard deviations exist only for the LLaVA diagnostic.
- **Missing evidence:** No confidence intervals or standard errors are reported.
- **Reviewer/editor rationale:** On subsets of 16 items, a single task error changes accuracy by 6.25 percentage points. Point estimates are statistically under-powered.
- **Interpretation caution:** Treat small score gaps as noise.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability
- **Rating:** 2
- **Evidence:** Scorer is deterministic and public.
- **Missing evidence:** No parser error rate is reported; format strictness is a known confound.

#### 9.3.2 Human rater or expert scorer agreement
- **Rating:** n/a
- **Evidence:** Scoring is automated; human agreement is not applicable.

#### 9.3.3 Model-as-judge reliability and validity checks
- **Rating:** n/a
- **Evidence:** No LLM-as-judge is utilized.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity
- **Rating:** 1
- **Evidence:** Authors state that results may not generalize if prompts or images are tweaked.
- **Missing evidence:** No empirical prompt-robustness data.

#### 9.4.2 Form, split, version, or refresh equivalence
- **Rating:** n/a
- **Evidence:** Single static form.

#### 9.4.3 Execution environment and dependency stability
- **Rating:** 1
- **Evidence:** LlamaIndex defaults and API embedding calls are used.
- **Missing evidence:** External APIs and embedding weights drift; no lockfile or container insulates scores from this drift.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences
- **Rating:** 1
- **Evidence:** Model differences are reported as simple deltas in paper tables.
- **Missing evidence:** No significance testing or error bands.

### 9.6 Overall Reliability, Precision, and Score Stability
- **Rating:** 1
- **Reviewer/editor rationale:** Reliability is the benchmark's weakest dimension. Small subsets and single-run point estimates, combined with external API drift and prompt sensitivity, mean only large score gaps are interpretable.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness
- **Rating:** 3
- **Evidence:** Items are derived from real Formula SAE rules and MIT Motorsports CAD data, and cross-reviewed by domain experts.
- **Missing evidence:** Narrowly focused on a single vehicle and rule document.

#### 10.1.2 Construct breadth and capability-domain coverage
- **Rating:** 2
- **Evidence:** Covers rule retrieval, component definition, presence, and compliance.
- **Missing evidence:** Excludes many requirements-engineering tasks, such as change-impact analysis, standards reconciliation, or collaborative design review.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality
- **Rating:** 2
- **Evidence:** Workflow segments are conceptually logical.
- **Missing evidence:** No empirical factor analysis or correlation metrics between subsets are reported.

#### 10.2.2 Item or task behavior across the score scale
- **Rating:** 2
- **Evidence:** Floors are defined by random baselines. Component mention types show different difficulty patterns.
- **Missing evidence:** No psychometric calibration or discrimination values.

#### 10.2.3 Failure modes and error analysis
- **Rating:** 3
- **Evidence:** The paper provides detailed qualitative failure analyses (OCR extraction, scale-bar math, multi-view coordinate mapping, and chart comparison).

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity
- **Rating:** 2
- **Evidence:** Metrics are standard in QA/VQA literature.
- **Missing evidence:** Compliance explanation scores (BLEU-2/ROUGE-L) have not been validated against human ratings.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance
- **Rating:** 1
- **Evidence:** Format compliance, short-explanation biases in BLEU/ROUGE, and Gemini recitation blocks alter scores.
- **Missing evidence:** None of these confounds are mitigated or statistically controlled.
- **Reviewer/editor rationale:** Construct-irrelevant variance represents a serious threat to score validity.
- **Interpretation caution:** Score differences may reflect format compliance rather than engineering capability.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks or realistic settings
- **Rating:** 1
- **Evidence:** None. No empirical correlation with other benchmarks or human engineering tasks.

#### 10.4.2 Convergent and discriminant evidence
- **Rating:** 1
- **Evidence:** None.

#### 10.4.3 Ecological or predictive relevance
- **Rating:** 2
- **Evidence:** Real-world FSAE and MIT Motorsports data provide strong ecological motivation.
- **Missing evidence:** No evidence that scores predict engineering design success.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls
- **Rating:** 1
- **Evidence:** Some CAD data is proprietary.
- **Missing evidence:** No canary strings, hidden splits, or contamination audits. Rules are fully public and web-searchable.

#### 10.5.2 Gameability and benchmark-specific tuning controls
- **Rating:** 1
- **Evidence:** None.
- **Missing evidence:** The authors explicitly recommend fine-tuning models on the Retrieval QAs, encouraging optimization directly against test items.
- **Reviewer/editor rationale:** Encouraging test-set tuning is a serious validation risk that invites overfitting.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims
- **Rating:** 3
- **Evidence:** Stated claims in the paper are highly disciplined; the authors frame the benchmark as a diagnostic "first step" and detail limitations.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims
- **Rating:** n/a
- **Evidence:** DesignQA makes no such claims.

### 10.7 Overall Validity Support
- **Rating:** 2
- **Reviewer/editor rationale:** Strong content validity is offset by unmitigated format shortcuts, public test exposure (with optimization recommended), and absent human or external validation.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance across systems, groups, and contexts
- **Rating:** 2
- **Evidence:** Relevant for MLLMs intended for engineering assistance.
- **Missing evidence:** Relevance across different multimodal interface types is not analyzed.

#### 11.1.2 Documentation of fair-use considerations
- **Rating:** 1
- **Evidence:** None. No dedicated fairness or bias documentation.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design
- **Rating:** 2
- **Evidence:** Uniform zero-shot prompts; RAG accommodates small-context windows.
- **Missing evidence:** English-only; models without image inputs are excluded.

#### 11.2.2 Domain, language, modality, and subgroup coverage
- **Rating:** 1
- **Evidence:** One rule document, one language, one engineering discipline.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability
- **Rating:** 2
- **Evidence:** Model versions and prompts are uniform.
- **Missing evidence:** Cohort includes different context conditions (AllRules vs RAG) and missing entries (Claude-Opus RAG-only). Gemini's RECITATION zero is an interface artifact.
- **Interpretation caution:** Do not directly compare AllRules and RAG scores.

#### 11.3.2 Access, compute, tooling, and API or local comparability
- **Rating:** 2
- **Evidence:** High cost of AllRules compared to RAG is disclosed.
- **Missing evidence:** Compute normalizations are absent.

#### 11.3.3 Temporal comparability for rolling or live benchmarks
- **Rating:** 2
- **Evidence:** Static item set is stable.
- **Missing evidence:** External API drift is unchecked, and no stale-score policy governs the leaderboard.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis
- **Rating:** 2
- **Evidence:** Paper breaks down performance by component mention type and drawing dimension type.

#### 11.4.2 Reliability and validity across subgroups
- **Rating:** 1
- **Evidence:** None.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases
- **Rating:** 2
- **Evidence:** Limitations section bounds interpretation.
- **Missing evidence:** No explicit list of restricted use cases.

#### 11.5.2 Release rules and sensitive-content handling
- **Rating:** 2
- **Evidence:** Open dataset release.
- **Missing evidence:** Lack of licensing and restrictions on test-set tuning.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use
- **Rating:** 2
- **Reviewer/editor rationale:** Within-condition testing is comparable, but condition heterogeneity and API drift represent significant comparability threats.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, or reporting-material scope
- **Rating:** 3
- **Evidence:** The paper provides detailed subset tables, and the scorer writes per-question results locally.

#### 12.1.2 Score granularity and level of detail
- **Rating:** 2
- **Evidence:** Granular reporting helps identify subset-level failure modes.
- **Missing evidence:** Score reporting (three decimal places) implies precision that small sample sizes cannot statistically support without confidence intervals.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling
- **Rating:** 2
- **Evidence:** Model versions and context conditions are explicitly labeled in the paper.
- **Missing evidence:** Leaderboard labels and uncertainty intervals are absent.

#### 12.2.2 Reproducibility and traceability of reported scores
- **Rating:** 2
- **Evidence:** Public dataset and scorer support traceability.
- **Missing evidence:** No pinned dependencies, and hosted model API versions drift limits exact reproducibility.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims
- **Rating:** 2
- **Evidence:** The paper limits public claims and links scores to failure modes.
- **Missing evidence:** Public website/leaderboard does not carry these caveats.

#### 12.3.2 Raw outputs, per-item data, or trace availability
- **Rating:** 2
- **Evidence:** Local run outputs are inspectable.
- **Missing evidence:** Paper runs and leaderboard submissions are not centrally archived for public audit.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports
- **Rating:** 3
- **Evidence:** Paper is objective and details scorer/metric biases.

#### 12.4.2 Acceptability and usability for intended audiences
- **Rating:** 3
- **Evidence:** Structured tables and error analyses are clear for technical users.

#### 12.4.3 Public communication and leaderboard governance
- **Rating:** 1
- **Evidence:** Manual verification is requested.
- **Missing evidence:** Opaque, currently unrenderable leaderboard table; lack of formal submission rules, stale policies, or test-set tuning disclosures.
- **Reviewer/editor rationale:** Leaderboard lacks formal governance controls.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Claims
- **Rating:** 2
- **Reviewer/editor rationale:** Paper reporting is clear and transparent, but overall reporting is capped at a 2 due to the un-governed leaderboard, lack of uncertainty reporting, and over-precise point estimates.

---

## Final Evaluation

### Evaluative Report of the Benchmark

DesignQA is a valuable and highly domain-grounded benchmark for diagnosing MLLM performance on requirements engineering tasks that combine long-context rule documents with novel, CAD-derived visual artifacts. Its main strengths reside in its authentic source materials (Formula SAE rules, MIT Motorsports CAD data), expert manual authoring process (with cross-review), and detailed qualitative error analysis. It is exceptionally useful as a research diagnostic for capability profiling, revealing that contemporary MLLMs face significant challenges in rule extraction, technical component recognition, and engineering drawing analysis.

As a measurement instrument, its primary limitations cluster in reliability, validation rigor, and lifecycle governance. Point estimates are reported on tiny subsets (as small as 16 items) without confidence intervals or repeated-run statistics. The dataset is fully public with no hidden splits, and the recommendation to fine-tune directly on test items introduces a significant gameability risk. Automatic scoring is highly sensitive to formatting and verbosity, and the repository lacks standard versioning and a LICENSE file.

DesignQA is therefore best suited to qualitative and coarse-quantitative capability diagnosis in research contexts. It should not be used for fine-grained ranking, procurement decisions, or as evidence of broad engineering competence.

### Conclusions

DesignQA is a well-designed and transparent diagnostic benchmark, but it is evidentially under-powered for comparative rankings due to the absence of score uncertainty. Responsible use requires keeping context-delivery conditions constant, analyzing per-subset performance rather than a simple average, and treating small score differences as noise.

### Recommendations

1. **Maintainers (Reliability):** Publish binomial/bootstrap confidence intervals for all subset scores and report multi-run standard deviations for API-based models.
2. **Maintainers (Validity):** Collect human/expert accuracy baseline scores to anchor model performance, and relax or report format-strict parser penalties.
3. **Maintainers (Contamination):** Create a hidden held-out split, and restrict leaderboard submissions from models fine-tuned on the test set.
4. **Maintainers (Lifecycle):** Add an explicit open-source LICENSE file, publish versioned releases, and establish a formal leaderboard governance policy.
5. **Users:** Report exact model versions, context conditions, and confidence intervals; do not compare AllRules and RAG scores directly.

### Summary of Ratings

| Section | Overall Rating (`n/a`, `0`–`4`) |
| :--- | :---: |
| Section 6. Rationale, development, and task/item quality | 3 |
| Section 7. Benchmark materials and usability | 2 |
| Section 8. Reference points and documented comparison groups | 2 |
| Section 9. Reliability and precision | 1 |
| Section 10. Validity support | 2 |
| Section 11. Fair use and comparability | 2 |
| Section 12. Reports, leaderboards, and public score claims | 2 |

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected entity or reporting surface | Affected capability domain or score interpretation | Affected rating(s) | Why it matters | Needed for a higher rating |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Confidence intervals / standard errors on reported scores | Paper tables, leaderboard | All per-subset score comparisons | 6.2.4, 9.2.2, 9.5.1, 12.1.2 | Small subsets mean a single task error shifts scores by 3-6pp, rendering small differences statistically insignificant. | Binomial/bootstrap intervals reported with every score. |
| Multi-run / seed variance for main model cohort | Paper tables, leaderboard | Score stability | 9.2.1, 9.4.3 | Non-zero temperatures introduce unquantified decoding variance in point estimates. | Published multi-run standard deviations. |
| Human / expert accuracy baseline | Paper tables, leaderboard | Anchoring scores to human competence | 8.1.2, 10.4.1 | Stated claims invoke "engineer-like" work but lack any human score context. | A human accuracy baseline on the smallest subsets. |
| Held-out split or contamination controls | Dataset, repository | Contamination and gameability | 5.6, 10.5.1, 10.5.2 | The fully public test set and recommendation to fine-tune on Retrieval items invite overfitting. | A hidden test set and a policy prohibiting test-set tuning. |
| Metric validation and format fallbacks | Scorer | Scoring validity | 7.1.3, 9.3.1, 10.3.1, 10.3.2 | Format errors and single-reference explanation comparisons penalize semantic correctness. | Human-validated explanation scorer and format-tolerant parsing. |
| License and dataset card | Repository | Lawful reuse, auditable redistribution | 1.2, 7.1.1, 7.1.7 | No LICENSE file (`license: null`) leaves reuse rights legally unstated. | An explicit open-source license and dataset card. |
| Versioning, changelog, releases, and reproducibility code | Repository, harness | Reproducibility, lifecycle | 5.7, 5.8, 6.2.7, 7.1.4, 12.2.2 | Inability to pin repository state or hosted API versions limits exact replication. | Version tags, changelog, environment lockfile, and smoke-test fixtures. |
| Governed, transparent leaderboard | `design-qa.github.io` leaderboard | Public comparison validity | 12.4.3 | Leaderboard is manually updated, lacks clear rules, and was unrenderable at access. | A public, governed leaderboard with condition filters and uncertainty bars. |

## Bibliography

1. Anna C. Doris, Daniele Grandi, Ryan Tomich, Md Ferdous Alam, Mohammadmehdi Ataei, Hyunmin Cheong, and Faez Ahmed. "DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation." arXiv:2404.07917v2, 2024. Local transcript: `literature/DesignQA.md`; original PDF: `Papers/DesignQA.pdf`; arXiv: <https://arxiv.org/abs/2404.07917>.
2. D. Hendrycks et al., "A Definition of AGI," arXiv:2510.18212, 2025. Local transcript: `literature/A_Definition_of_AGI.md`.
3. A. M. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," arXiv:2511.04703, 2025. Local transcript: `literature/Measuring_what_Matters.md`.
4. A. Reuel et al., "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices," arXiv:2411.12990, 2024. Local transcript: `literature/betterbench.md`.
5. EFPA. "EFPA Test Review Model - Version 2025." Local transcription used through `literature/EFPA_Test_Review_Model_2025_Markdown.md`.

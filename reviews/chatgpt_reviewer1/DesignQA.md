# MESA Review: DesignQA

Review status: full Part A + Part B MESA review  
Reviewed entity: DesignQA public benchmark, including the paper-described dataset, the official GitHub repository with dataset and evaluation code, the official project website, and the manually maintained leaderboard  
Reviewer profile: `.codex/agents/benchmark-reviewer.md`  
Date of current review: 2026-06-28

## Short Stand-Alone Non-Evaluative Benchmark Description

DesignQA is a public multimodal benchmark for evaluating multimodal large language models on engineering requirements question answering. It is based on the 2024 Formula SAE rules and MIT Motorsports design artifacts, including CAD-derived images, engineering drawings, and functional performance visuals. The benchmark contains 1,451 question-answer pairs across Rule Extraction, Rule Comprehension, and Rule Compliance tasks. Its public materials include the DesignQA paper, an official GitHub repository with dataset and evaluation code, an official project website, and a manually maintained leaderboard.

## Source Inventory

| ID | Source | Access date | Use in this review |
| :-- | :-- | :-- | :-- |
| S01 | Doris et al., [DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation](https://arxiv.org/abs/2404.07917), arXiv:2404.07917v2, and local transcription `literature/DesignQA.md` | 2026-06-28 | Main benchmark paper: item construction, subset structure, scoring metrics, evaluation conditions, baseline results, limitations. |
| S02 | DesignQA official repository, [`anniedoris/design_qa`](https://github.com/anniedoris/design_qa/) | 2026-06-28 | Dataset directories, evaluation code, README setup and submission instructions, license status. |
| S03 | DesignQA official website and leaderboard route, <https://design-qa.github.io/> | 2026-06-28 | Public reporting surface, leaderboard presentation, submission route. |
| S04 | DesignQA repository `dataset/` directory | 2026-06-28 | Public task set and the 1,451 QA items across the six subsets. |
| S05 | DesignQA repository `eval/full_evaluation.py` and `eval/metrics/metrics.py` | 2026-06-28 | Scoring procedure, metric implementations, error handling, results output. |
| S06 | Original PDF source, `Papers/DesignQA.pdf` | 2026-06-28 | Figures, tables, and appendix material supporting the paper transcript. |
| S07 | MESA template, `MESA EFPA template official.md` | 2026-06-28 | Required review structure, field guidance, rating scale. |
| S08 | EFPA Test Review Model, `literature/EFPA_Test_Review_Model_2025_Markdown.md` | 2026-06-28 | Review architecture and descriptive/evaluative separation. |
| S09 | BetterBench, `literature/betterbench.md` | 2026-06-28 | Benchmark lifecycle, documentation, reproducibility, contamination, usability, and maintenance criteria. |
| S10 | Measuring what Matters, `literature/Measuring_what_Matters.md` | 2026-06-28 | Construct-validity chain: phenomenon, task, metric, claim. |
| S11 | Repository report, `benchmark_official_documentation_inventory.md` | 2026-06-28 | Local source-inventory starting point for DesignQA. |

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt | Description |
| :-- | :-- |
| Reviewer Name | Codex using the MESA benchmark-reviewer profile |
| Date of Current Review | 2026-06-28 |
| Date of Previous Review | n/a |

### 1.2 Benchmark Identity & Provenance

| Prompt | Description |
| :-- | :-- |
| Reviewed Entity Name | DesignQA public benchmark: paper-described dataset, public GitHub dataset and scorer, official website, and official leaderboard route. |
| Short Name / Acronym | DesignQA |
| Entity Type | Original multimodal benchmark dataset with public evaluation code and manually maintained leaderboard. |
| Parent / Source Benchmark | n/a. The benchmark uses the 2024 Formula SAE rules and MIT Motorsports design data as source materials, but is not a derived variant of a prior benchmark. |
| Exact Version / Release Split | arXiv:2404.07917v2 dated 2024-08-23; public GitHub `main` branch as inspected 2026-06-28. No separate public train/dev/test split or GitHub release tag was identified in the inspected sources. |
| Implementation / Scorer Version | Public repository evaluation scripts, including `eval/full_evaluation.py` and metrics in `eval/metrics/metrics.py`, as described by the official README. No package version or immutable scorer release was identified. |
| Creators & Current Maintainers | Anna C. Doris, Daniele Grandi, Ryan Tomich, Md Ferdous Alam, Mohammadmehdi Ataei, Hyunmin Cheong, and Faez Ahmed. The repository owner is `anniedoris`; current maintainer status is inferred from the official GitHub repository and issue route. |
| Host Organization / Repository Owner | Official repository: `anniedoris/design_qa`; official website: `design-qa.github.io`; paper affiliations include MIT, Autodesk Research, and MIT Motorsports. |
| Release Dates | arXiv v1: 2024-04-11; arXiv v2: 2024-08-23. The repository README cites a 2025 Journal of Computing and Information Science in Engineering article. |
| License & Access Terms | Public GitHub repository and public project website. A clear license file or explicit benchmark license was not visible in the inspected repository landing page or local transcript. |
| Persistent Identifier / DOI / Citation | arXiv:2404.07917. Repository README citation: Doris et al., "DesignQA: A multimodal benchmark for evaluating large language models' understanding of engineering documentation," Journal of Computing and Information Science in Engineering, 25(2), 021009, 2025. |

### 1.3 Materials, Sources, & Access Tracking

| Material / Source Type | URL, Location, or Identifier | Access Date |
| :-- | :-- | :-- |
| Paper / Technical Report | `literature/DesignQA.md`; `Papers/DesignQA.pdf`; <https://arxiv.org/abs/2404.07917> | 2026-06-28 |
| Website / Documentation Hub | <https://design-qa.github.io/> | 2026-06-28 |
| Code Repository | <https://github.com/anniedoris/design_qa/> | 2026-06-28 |
| Dataset / Task / Prompt Set | GitHub repository `dataset/` directory; paper-described 1,451 QA items | 2026-06-28 |
| Evaluation Harness / Runner | GitHub repository `eval/` directory; `eval/full_evaluation.py`; `eval/metrics/metrics.py` | 2026-06-28 |
| Leaderboard / Results Portal | Official website and leaderboard route at <https://design-qa.github.io/>; README describes submission by GitHub issue | 2026-06-28 |
| Guides (User/Scoring/Rubric) | Repository README setup and evaluation instructions; paper Section 3.2 evaluation metrics | 2026-06-28 |
| Changelog / Release Logs | No release tag, changelog, or immutable version log identified in inspected public landing page. | 2026-06-28 |
| Official Announcements | Paper, project website, and repository README | 2026-06-28 |
| Contextual Literature | `literature/EFPA_Test_Review_Model_2025_Markdown.md`; `literature/betterbench.md`; `literature/Measuring_what_Matters.md` | 2026-06-28 |
| Feedback / Contact Channels | Repository issue tracker; corresponding-author email in local paper transcript | 2026-06-28 |

Reviewer comments: The local literature transcript is the primary source for the paper-described benchmark. The official repository and website were used to update current access, submission, and implementation details. No existing `reviews/DesignQA.md` file was present before this review was drafted.

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

- [ ] Not explicitly stated
- [ ] General Knowledge (K)
- [x] Reading and Writing Ability (RW)
- [x] Mathematical Ability (M)
- [x] On-the-Spot Reasoning (R)
- [x] Working Memory (WM)
- [ ] Long-Term Memory Storage (MS)
- [x] Long-Term Memory Retrieval (MR)
- [x] Visual Processing (V)
- [ ] Auditory Processing (A)
- [ ] Speed (S)
- [ ] Coding or software engineering
- [x] Specialized scientific or technical expertise
- [x] Domain-specific professional expertise
- [ ] Tool use
- [ ] Agency or autonomy
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [x] Factuality or grounding
- [ ] Multilingual or cross-cultural capability
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [ ] Calibration or uncertainty

Reviewer comments: The benchmark primarily targets multimodal engineering documentation understanding: long-document retrieval, technical terminology recognition, engineering drawing interpretation, and design-rule compliance. It should not be classified as a general intelligence or AGI benchmark. Mathematical ability is implicated narrowly through dimensional and functional-compliance questions rather than broad mathematics.

### 2.2 Area of Use

- [ ] Not explicitly stated
- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [ ] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison
- [x] Internal regression testing
- [x] Public communication or marketing
- [ ] Policy or governance analysis

Reviewer comments: The paper uses DesignQA to compare contemporary MLLMs and diagnose failure modes. The repository and website support future submissions and leaderboard posting, but the reviewed materials do not frame the benchmark as a deployment gate or policy benchmark.

### 2.3 Intended AI Systems

- [ ] Not explicitly stated
- [x] Frontier general-purpose language models
- [x] Chat or instruction-following models
- [ ] Base language models
- [ ] Code models
- [x] Multimodal models
- [ ] Audio or speech models
- [ ] Agentic systems
- [ ] Tool-using systems
- [x] Retrieval-augmented systems
- [x] Domain-specialized models
- [x] Open-weight local models
- [x] API-hosted models

Reviewer comments: The paper evaluates GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, and LLaVA-1.5 variants, including full-rule-context and RAG conditions. The repository evaluation path accepts CSV predictions from any system able to produce responses in the expected formats.

### 2.4 Intended Users of Benchmark Outputs

- [ ] Not explicitly stated
- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [x] Product teams
- [ ] Safety evaluators
- [ ] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [x] Educators or academic reviewers
- [x] Public leaderboard users

Reviewer comments: Intended users are mainly AI and engineering-design researchers, model developers, and benchmark users interested in MLLM performance on engineering documentation. Product and enterprise users could find the results relevant, but procurement or deployment decisions are not an explicit supported use in the inspected materials.

### 2.5 Task Families, Subdomains, and Scores

| Component | Description |
| :-- | :-- |
| Capability, phenomenon, or quality the benchmark claims to measure | MLLM proficiency in comprehending and applying engineering requirements in technical documentation. |
| Definition of the capability or quality being measured | The paper operationalizes this as answering questions that require locating, understanding, and applying Formula SAE rules together with CAD-derived and engineering drawing information. |
| Subcomponents of the claimed capability | Rule Extraction, Rule Comprehension, and Rule Compliance. These are divided into Retrieval, Compilation, Definition, Presence, Dimension, and Functional Performance subsets. |
| Excluded scope or non-target abilities | The benchmark does not claim to cover all engineering documentation, all CAD tasks, all standards, all forms of design automation, or broad general intelligence. |
| Benchmark item families or subdomains | Retrieval QAs, Compilation QAs, Definition VQAs, Presence VQAs, Dimension VQAs, and Functional Performance VQAs. |
| Sources for benchmark items | 2024 Formula SAE rules, MIT Motorsports CAD models and data, engineering drawings, and manually authored/reviewed QA pairs by MIT Motorsports members, industry professionals, and engineering researchers. |
| Sampling method | Mixed programmatic and expert-curated construction. Retrieval items are generated from extracted rule text. Other subsets are manually generated or curated from selected components, rules, images, and test data. |
| Selection or filtering logic | The paper describes excluding non-design sections from retrieval rules, manually curating terms/components/rules, generating positive and negative examples where applicable, and review of most manually generated QAs by parties who did not author them. |
| Splits or partitions | Public dataset organized by task subset. No hidden private split, training split, validation split, or retired split was identified in the inspected sources. |
| Primary score | Repository README states that `results.txt` reports an overall score as a simple average across the six benchmark segments. |
| Subscores | Subset-level scores for Retrieval, Compilation, Definition, Presence, Dimension, and Functional Performance; explanation metrics for Rule Compliance subsets. |
| Derived scores | For Dimension, context and detailed-context scores are run and averaged together according to repository README. Paper reports model-condition comparisons, including AllRules, simple RAG, and GuaranteedRAG for selected experiments. |
| Qualitative score ranges | No formal qualitative bands such as low/medium/high or pass/fail thresholds were identified. |
| Boundaries or caveats | The paper explicitly notes limitations from one rule document, limited task families, prompt/image-format choices, small subset sizes, and automatic scoring limitations. |

### 2.6 Model Response Mode

- [ ] Not explicitly stated
- [ ] Multiple choice
- [x] Short text
- [x] Long-form text
- [x] Structured output, such as JSON or XML
- [ ] Code
- [ ] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or other output generation
- [ ] Image output
- [x] Yes/no decision

Reviewer comments: Required responses include exact rule text, comma-separated rule numbers, component names, yes/no answers, and explanations prefixed according to the prompt in compliance tasks. The repository scorer consumes CSVs with `ground_truth` and `model_prediction` columns rather than directly administering an API protocol.

### 2.7 Prerequisites for Evaluated Systems

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing |
| :-- | :--: | :--: | :--: |
| Long-context or retrieval over a rule document | [ ] | [x] | [ ] |
| Image input | [ ] | [x] | [ ] |
| CAD-image and drawing interpretation capability | [ ] | [x] | [ ] |
| Exact response-format following | [ ] | [x] | [ ] |
| Ability to process CSV output for scoring | [ ] | [x] | [ ] |
| API or local inference procedure | [ ] | [x] | [x] |
| Fixed generation parameters for new submissions | [ ] | [ ] | [x] |
| Hardware, cost, and runtime budget | [ ] | [ ] | [x] |

Reviewer comments: The benchmark requires multimodal input capability for most subsets and document-grounded retrieval or long-context ingestion. The official repository documents scoring inputs but does not fully standardize how future models should be prompted, sampled, or run before producing CSV predictions.

### 2.8 Evaluation Conditions

| Condition | Description |
| :-- | :-- |
| Prompting protocol | The paper provides task-specific prompts and a shared preamble: "We are a student engineering team designing a vehicle for the FSAE competition. Attached is the FSAE rules document." |
| Few-shot examples | No few-shot demonstration protocol is described for the main benchmark administration. |
| Context provision | Paper experiments use either full rule text in context for selected closed models or simple LlamaIndex RAG for other model conditions. GuaranteedRAG is used for LLaVA-1.5 in a diagnostic experiment. |
| Sampling settings | Appendix A states LlamaIndex default settings; temperature 0.75 and top_p 0.9 for LLaVA-1.5, temperature 0.1 for the closed-source models, and max_new_tokens of 250, 100, or 1500 by segment. |
| Tool permissions | No general tool-use protocol is specified. RAG experiments use LlamaIndex retrieval. |
| Time limits | No universal time limit for benchmark submissions was identified. |
| Cost or compute limits | The paper notes cost constraints affected which model-condition combinations were run; the repository does not specify a standard budget. |
| Human intervention | QA creation and review involve humans. Future leaderboard submissions are manually verified according to the repository README. |
| Evaluation route | Users generate predictions, place them in CSV files, and run the evaluation script. |

### 2.9 Task Interaction and Observable Evidence Types

- [x] Static item or prompt response
- [x] Document-grounded QA
- [x] Visual QA
- [x] Engineering drawing interpretation
- [x] Response text
- [x] Structured or constrained output
- [x] Per-item predictions in CSV form
- [x] Subscore outputs
- [ ] Multi-turn interaction
- [ ] Tool trace
- [ ] Browser trace
- [ ] Agent trajectory

Reviewer comments: The benchmark is a static QA benchmark rather than an interactive design environment. Observable evidence is the model prediction and resulting score, not a trace of design actions.

### 2.10 Input Stimulus Type

- [x] Long-form technical text
- [x] CAD-derived images
- [x] Engineering drawings
- [x] Functional performance visuals or charts
- [x] Tables or structured data in source rules/results
- [ ] Audio
- [ ] Video
- [ ] Browser state
- [ ] Executable environment

### 2.11 Number of Items or Measurement Points

| Segment | Subset | Item count | Primary response type |
| :-- | :-- | --: | :-- |
| Rule Extraction | Retrieval | 1,192 | Exact rule text |
| Rule Extraction | Compilation | 30 | Rule-number list |
| Rule Comprehension | Definition | 31 | Component name |
| Rule Comprehension | Presence | 62 | Yes/no |
| Rule Compliance | Dimension | 120 | Yes/no plus explanation |
| Rule Compliance | Functional Performance | 16 | Yes/no plus explanation |
| Total | All subsets | 1,451 | Mixed constrained text and explanations |

Reviewer comments: The distribution is highly imbalanced across subsets. This is descriptive here; implications for interpretation are evaluated in Part B.

### 2.12 Mode of Evaluation

| Mode | Description |
| :-- | :-- |
| Local/offline scoring | Public Python scorer accepts CSV files with ground truth and model predictions. |
| Paper benchmark run | Authors report runs for selected MLLMs under full-rule-context, simple RAG, and GuaranteedRAG conditions. |
| Hosted/public leaderboard | Official README states that users can submit results via GitHub issue for manual verification and leaderboard posting. |
| Private adjudication | No hidden private benchmark form or private scorer was identified. |

### 2.13 Technological Arrangements

| Arrangement | Description |
| :-- | :-- |
| Repository language | GitHub page reports Python as the repository language. |
| Setup | README instructs users to create a Python 3.10 conda environment and install `requirements.txt`. |
| Dataset layout | `dataset/rule_extraction`, `dataset/rule_comprehension`, and `dataset/rule_compliance` directories, with CSV files and image folders. |
| Scoring layout | `eval/full_evaluation.py` with task-specific CSV paths; metrics in `eval/metrics/metrics.py`. |
| Retrieval infrastructure in paper experiments | LlamaIndex simple RAG; `text-embedding-3-large` is mentioned in the local paper transcript for retrieval conditions. |

### 2.14 Time and Resource Requirements

| Resource | Description |
| :-- | :-- |
| Human preparation | Users must run their model over all item subsets and format predictions into expected CSV files. |
| Compute | Depends on model and whether full rule document, RAG, or other retrieval methods are used. No standard compute budget is specified. |
| Context length | Full-rule-context runs require sufficiently large context windows. RAG runs reduce context but introduce retrieval dependence. |
| Cost | Paper notes cost constraints limited some closed-model experiments; no cost-normalized public scoring rule was identified. |
| Manual verification | Leaderboard submissions require filing a GitHub issue and including results and evaluation code for manual verification. |

### 2.15 Benchmark Forms, Versions, and Variants

| Form or Variant | Description |
| :-- | :-- |
| Paper-described DesignQA | Main 1,451-item benchmark described in arXiv v2 / journal article. |
| Public GitHub dataset | Current public dataset files as organized in the repository. |
| Full-rule-context condition | Paper evaluation condition where selected models receive the full FSAE rules text. |
| Simple RAG condition | Paper evaluation condition using LlamaIndex retrieval. |
| GuaranteedRAG diagnostic condition | Diagnostic condition generated to contain relevant rule context for LLaVA-1.5 only. |
| IDETC Hackathon 2025 use | Repository README frames DesignQA as a hackathon problem; no separate MESA-reviewed benchmark variant is evaluated here. |

### 2.16 Static or Dynamic Task Determination

DesignQA is a static public benchmark in the inspected materials. The same public task files can be used repeatedly. No rolling item refresh, hidden test set, item retirement rule, or dynamic task generation policy was identified.

### 2.17 Evidence Sources Used in Scoring

| Evidence source | Use in scoring |
| :-- | :-- |
| Ground-truth answer text | Used for exact/soft text comparison in Retrieval and Definition. |
| Ground-truth rule-number lists | Used for Compilation F1 over rule numbers. |
| Ground-truth yes/no labels | Used for Presence, Dimension, and Functional Performance accuracy. |
| Human-written explanations | Used for BLEU-2, ROUGE-L, and SBERT similarity for Rule Compliance explanations. |
| Synonym lists | Used for Definition component scoring. |
| Model predictions | Supplied by the user in CSV files for scoring. |

### 2.18 Broad-Claim Flags for Later Evaluation

| Claim Type | Present? | Description |
| :-- | :--: | :-- |
| AGI or general intelligence | No | The inspected DesignQA sources do not claim DesignQA measures AGI or general intelligence. |
| Broad multimodal engineering-documentation understanding | Yes | The title and abstract frame the benchmark as evaluating MLLMs' understanding of engineering documentation. |
| Real-world engineering design assistance | Yes | The paper motivates DesignQA by reference to real engineering design tasks and AI-assisted engineering design processes. |
| Deployment readiness or safety certification | No | No deployment, procurement, or certification claim was identified. |

Reviewer comments: Part B treats the broadest relevant claim as a bounded construct-validity issue: whether a benchmark built around one Formula SAE rulebook and one vehicle-design context supports claims about engineering documentation understanding more generally.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

DesignQA scoring is automated. Users run `eval/full_evaluation.py` with paths to CSV prediction files for each subset. The README states that each CSV should contain `ground_truth` and `model_prediction` columns. The scorer calculates subset metrics and writes `results.txt`. The official README states that the overall score is a simple average across the six benchmark segments rather than an item-weighted average.

### 3.2 Scores and Metrics

| Subset | Metric(s) | Score meaning |
| :-- | :-- | :-- |
| Retrieval | F1 Bag of Words | Overlap between predicted rule text and ground-truth rule text after normalization. |
| Compilation | F1 Rules | Overlap between predicted and ground-truth rule-number lists. |
| Definition | F1 Bag of Characters | Character-level F1 over predicted component names, using synonyms where available. |
| Presence | Accuracy | Correct yes/no identification of component presence in a close-up CAD image. |
| Dimension | Accuracy plus BLEU-2, ROUGE-L, and SBERT similarity for explanations | Correct yes/no compliance judgment plus similarity between generated and human-written explanations. |
| Functional Performance | Accuracy plus BLEU-2, ROUGE-L, and SBERT similarity for explanations | Correct yes/no compliance judgment plus explanation similarity. |
| Overall | Simple average across six subset scores | Aggregate score reported by repository README. |

### 3.3 Scale or Metric Types

Metrics are bounded between 0 and 1, with higher values indicating greater match to the reference answer or explanation. F1 metrics provide partial credit; accuracy is binary at the item level; BLEU-2, ROUGE-L, and SBERT cosine similarity are similarity scores for explanations.

### 3.4 Score Transformation

The repository README describes a simple average across the six segments for the overall score. The paper reports macro-averages within subsets for F1 metrics. No norming, equating, standardization, confidence interval transformation, percentile, or qualitative banding process was identified.

### 3.5 Documented Reference Groups, Baselines, and Comparators

| Comparator type | Description |
| :-- | :-- |
| Naive baselines | Paper reports simple baselines for the benchmark subsets. |
| Contemporary MLLMs | Paper reports GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, and LLaVA-1.5 variants. |
| Retrieval conditions | Paper compares AllRules, simple RAG, and GuaranteedRAG conditions for selected models. |
| Human or expert baseline | No full human performance baseline on the benchmark was identified. Expert involvement is used for item design/review, not as a reported benchmark score. |
| Chance/floor/ceiling interpretation | No formal chance model, floor/ceiling study, or score-band interpretation was identified beyond naive baselines. |

### 3.6 Score Uncertainty and Stability

The paper reports some variation in the GuaranteedRAG experiment for LLaVA-1.5 across five generated GuaranteedRAG contexts. No general confidence intervals, bootstrap intervals, repeated-run variance, API-version stability analysis, prompt sensitivity study, or inter-rater agreement statistic for item creation/review was identified.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

The paper explains why each metric was selected for the relevant subset: F1 variants for text or rule-list overlap, accuracy for yes/no decisions, and BLEU-2/ROUGE-L/SBERT similarity for explanation comparison. The authors also explicitly note limitations of automatic metrics, including formatting penalties, child-rule inclusion issues, and weak semantic adequacy of BLEU/ROUGE for explanations.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

| Output | Availability |
| :-- | :-- |
| Paper tables | Public in the paper transcript and arXiv/JCISE article. |
| Local scoring output | `results.txt` generated by the public evaluation script. |
| Subset-level scores | Produced by the scorer and reported in the paper. |
| Per-item scores | README states `results.txt` contains scores for each individual question. |
| Leaderboard | Public website route with manual submission through GitHub issue. |
| Raw model outputs from paper runs | Some evaluation CSVs for LLaVA are referenced in the README. Complete raw outputs for all paper model runs were not confirmed in the inspected summary. |

### 4.2 Output Name or Description

The main outputs are subset scores, an overall simple-average score, paper comparison tables, diagnostic analyses by retrieval/context condition, and leaderboard postings for submitted systems.

### 4.3 Output Design or Presentation

The paper presents detailed tables by subset and model condition. The repository scorer produces a text results file. The website presents public-facing benchmark information and a leaderboard route.

### 4.4 Output Structure

| Output component | Description |
| :-- | :-- |
| Overall score | Simple average across six segments. |
| Subset scores | Individual metrics for Retrieval, Compilation, Definition, Presence, Dimension, and Functional Performance. |
| Explanation metrics | BLEU-2, ROUGE-L, and SBERT similarity for compliance explanations. |
| Diagnostic breakdowns | Paper analyses RAG condition, vehicle component mention type, drawing dimensioning type, and additional context effects. |

### 4.5 Sensitivity to Context

The paper explicitly studies sensitivity to rule-context delivery, contrasting full-rule-context, simple RAG, and GuaranteedRAG. It also studies drawing dimensioning type and additional context in images/prompts. These sensitivity analyses are paper diagnostics, not a formal uncertainty model for all benchmark submissions.

### 4.6 Development of Outputs

Outputs are derived from automated scoring scripts and paper analyses. Leaderboard outputs require manual verification according to the repository README.

### 4.7 Modifiability

The public repository allows users to run the scorer with their own prediction CSVs. The scoring logic can be inspected and modified locally. No formal versioning policy for modified scorers or forked benchmark forms was identified.

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

The paper and README link each subset to a specific task family and scoring metric. The overall score linkage is described as a simple average across segments, which is transparent but important because segment item counts differ.

### 4.9 Output Content

Outputs include numeric scores, per-subset diagnostics, per-question scores, and in the paper, qualitative discussion of model failure modes. No standard model card, benchmark card, confidence interval report, or signed audit log was identified.

### 4.10 Intended Recipients

Primary recipients are benchmark users, AI researchers, model developers, engineering-design researchers, and public leaderboard readers.

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

DesignQA is distributed through a public GitHub repository and official website. The paper states the benchmark is publicly available. The repository includes dataset, documentation, evaluation, and scripts directories.

### 5.2 Distribution and Access Model

No private, semi-private, or controlled-access split was identified. Leaderboard posting is mediated by manual verification after users file a GitHub issue with results and code.

### 5.3 Methods of Publication

| Publication route | Description |
| :-- | :-- |
| arXiv | Public paper at arXiv:2404.07917. |
| Journal citation | Repository README cites Journal of Computing and Information Science in Engineering, 25(2), 021009, 2025. |
| GitHub repository | Dataset, evaluation code, README, and scripts. |
| Official website | Project page and leaderboard route. |

### 5.4 User Requirements or Qualifications

Users need Python/conda setup ability, access to a model capable of handling the relevant text and visual inputs, and the ability to format model predictions into the expected CSV files. No formal user qualification or access gate was identified.

### 5.5 Dataset and Item Access

The public repository includes dataset CSVs and image folders. The Formula SAE rules are used as the source document; the paper describes extracting and filtering rules from the PDF. No hidden test items were identified.

### 5.6 Provenance and Contamination Documentation

The paper gives unusually concrete provenance for an AI benchmark: Formula SAE rules, MIT Motorsports CAD/test data, and expert/human QA authorship/review. It also states that the visual inputs were not seen by the model during pre-training in the same form. However, no systematic contamination audit, canary mechanism, public/private split, or training-set overlap analysis was identified.

### 5.7 Reproducibility Materials

| Material | Availability |
| :-- | :-- |
| Dataset files | Public in repository. |
| Scoring code | Public in repository. |
| Setup instructions | Public README with conda/Python 3.10 setup. |
| Example evaluation command | Public README includes full evaluation command and LLaVA example. |
| Model prompts | Paper and README include task prompts and examples. |
| Model-generation code for all paper results | Not fully established from inspected sources. |
| Exact model API versions/settings | Paper appendix documents model identifiers and some LlamaIndex defaults. |
| Environment lockfile/container | Requirements file exists; no container or lockfile was identified in the inspected summary. |

### 5.8 Maintenance and Versioning

The repository is public and currently presents 166 commits on the inspected GitHub landing page. It has no GitHub releases published. No changelog, benchmark version policy, item refresh policy, deprecation policy, or scorer compatibility policy was identified. The README includes an IDETC Hackathon 2025 note, indicating some continuing use beyond the original paper.

---

## Appendix A. General Description of the Benchmark

DesignQA is a requirements-engineering-oriented multimodal benchmark. Its central measurement chain is:

| Element | Description |
| :-- | :-- |
| Phenomenon | MLLM ability to understand and apply engineering requirements from technical documentation. |
| Task operationalization | Answer static QA items grounded in Formula SAE rules, CAD-derived images, engineering drawings, and functional performance visuals. |
| Metric | Subset-specific automatic metrics, including F1 variants, accuracy, BLEU-2, ROUGE-L, and SBERT similarity. |
| Claim supported by benchmark framing | Model performance indicates how well a system performs on this set of engineering design documentation tasks under the documented context-delivery conditions. |
| Interpretation limit | Performance should not be generalized without caution to all engineering documentation, all design standards, all CAD-native workflows, or deployed engineering-assistant safety. |

---

# Part B. Evaluation of the Benchmark

## Information Sources

Part B judgments use the Part A evidence above plus the MESA template, EFPA review logic, BetterBench lifecycle/reproducibility criteria, and Measuring what Matters construct-validity framing. Missing documentation is treated as an evidence gap, not proof of poor benchmark quality.

## Explanation of Ratings

Ratings use the MESA/EFPA-style scale: `n/a`, `0`, `1`, `2`, `3`, and `4`. A rating of `3` indicates mostly adequate support with limited gaps; `2` indicates cautious use with important gaps; `1` indicates serious evidence limitations; `0` indicates absent or unusable support; `4` indicates comprehensive support.

## General Guidance on Assigning Ratings

Missing documentation is treated as an evidence gap, not as proof of poor quality. Ratings are not mechanically averaged. The overall rating in each section reflects the strength of evidence for DesignQA's intended score meaning: multimodal engineering documentation understanding and requirements compliance reasoning under documented DesignQA conditions.

---

## Section 6. Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition

- **Rating:** 3
- **Evidence:** The paper defines a specific motivation: MLLMs need to synthesize long technical documentation and visual design artifacts for engineering design according to requirements. It decomposes this into extraction, comprehension, and compliance tasks.
- **Missing evidence:** The target phenomenon "understanding engineering documentation" is broader than the paper's single Formula SAE rulebook and vehicle-design context.
- **Reviewer rationale:** The construct is substantially clearer than many broad MLLM benchmarks, but the title-level wording remains broader than the operational sample.
- **Interpretation caution:** Treat DesignQA as measuring a specific form of Formula SAE engineering-requirements QA, not engineering documentation understanding in general.

#### 6.1.2 Summary of prior research and benchmark context

- **Rating:** 3
- **Evidence:** The paper situates DesignQA against engineering-design AI work, reference-dependent QA, document-grounded VQA, and MLLM benchmarks such as QASPER, ZeroScrolls, MMMU, ScienceQA, and InfoSeek.
- **Missing evidence:** The related-work comparison is qualitative; no systematic benchmark landscape audit or formal gap analysis is provided.
- **Reviewer rationale:** The benchmark context is well motivated for a research paper and identifies a plausible underrepresented domain.
- **Interpretation caution:** The claim of novelty should be interpreted within the paper's cited benchmark set and not as exhaustive proof that no comparable engineering-documentation benchmark exists.

#### 6.1.3 Phenomenon-task-metric-claim chain

- **Rating:** 3
- **Evidence:** The benchmark links engineering-requirements understanding to tasks that require retrieving rules, recognizing rule-defined components, and checking design compliance. Each subset has a documented metric.
- **Missing evidence:** The paper does not fully validate whether each automatic metric preserves the intended meaning of "understanding" or "compliance reasoning."
- **Reviewer rationale:** The chain is visible and defensible for a benchmark prototype, but some metric links are weaker than the task design.
- **Interpretation caution:** High scores support task-level performance under the scoring rules, not unqualified evidence of robust engineering understanding.

#### 6.1.4 Task or item design

- **Rating:** 3
- **Evidence:** Items are grounded in real Formula SAE rules, CAD artifacts, engineering drawings, and functional performance examples. The task taxonomy maps to plausible engineering workflows.
- **Missing evidence:** The sampling frame for rules, components, CAD artifacts, and performance examples is not documented in enough detail to establish representativeness across engineering documentation tasks.
- **Reviewer rationale:** Item design is a clear strength because tasks are concrete, domain-specific, and expert-informed.
- **Interpretation caution:** Strong face validity for Formula SAE-style requirements does not guarantee broad task coverage across engineering sectors or documentation formats.

#### 6.1.5 Procedures for developing task or item content

- **Rating:** 3
- **Evidence:** The paper describes programmatic rule extraction, manually curated terms/components, expert/human QA creation, and review by parties other than the author for most manually generated QAs.
- **Missing evidence:** Full annotation guidelines, reviewer training, disagreement resolution logs, and item rejection counts are not documented in the inspected sources.
- **Reviewer rationale:** The development procedure is stronger than synthetic or crowdsourced-only benchmark construction, but not fully auditable.
- **Interpretation caution:** Users should credit the expert provenance while recognizing that the item-development process cannot be independently reconstructed in full.

#### 6.1.6 Thoroughness of the final task or item selection process

- **Rating:** 2
- **Evidence:** The paper describes filtering non-design rule sections, selecting 30 common terms, selecting 31 components, selecting 20 dimension rules, and constructing a small functional performance subset from available data.
- **Missing evidence:** No full item-selection protocol, sampling audit, rejected-item register, or coverage matrix is provided.
- **Reviewer rationale:** Item selection is purposeful but only partly transparent.
- **Interpretation caution:** Subset composition may reflect available Formula SAE and MIT Motorsports materials as much as the broader target construct.

#### 6.1.7 Quantitative evidence of task or item quality

- **Rating:** 2
- **Evidence:** The paper reports model results, failure modes, and diagnostic analyses by RAG condition, component mention type, dimensioning type, and additional context.
- **Missing evidence:** No item difficulty distribution for humans, item discrimination analysis, inter-reviewer agreement, confidence intervals, or formal psychometric item analysis is provided.
- **Reviewer rationale:** There is useful empirical item behavior evidence, but it is mostly model-performance analysis rather than measurement-quality analysis.
- **Interpretation caution:** The paper's model failures help understand task difficulty but do not by themselves establish item reliability or validity.

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice

- **Rating:** 2
- **Evidence:** The benchmark reuses Formula SAE rules and MIT Motorsports artifacts to create new QA items. It is not a translation or benchmark slice.
- **Missing evidence:** Licensing and reuse terms for all source artifacts and generated dataset materials are not fully visible in the inspected sources.
- **Reviewer rationale:** Source reuse is central and well described technically, but legal/licensing and long-term provenance metadata are incomplete.
- **Interpretation caution:** Users should verify source-material permissions before commercial or high-stakes reuse.

#### 6.1.9 Overall Rationale, development, and task or item quality

- **Rating:** 3
- **Evidence:** Clear rationale, expert-informed item creation, real engineering materials, and explicit task decomposition.
- **Missing evidence:** Full selection protocol, coverage analysis, annotation agreement, and formal item-quality statistics.
- **Reviewer rationale:** DesignQA is well motivated and carefully built for a research benchmark, though not fully documented as a mature measurement instrument.
- **Interpretation caution:** The strongest supported interpretation is narrow: performance on a curated Formula SAE engineering-requirements QA benchmark.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- **Rating:** 3
- **Evidence:** The paper, website, and README clearly describe the purpose and domain.
- **Missing evidence:** Unsupported uses and non-use cases are not stated in a dedicated benchmark card.
- **Reviewer rationale:** Purpose documentation is clear for research use.
- **Interpretation caution:** Users must infer many boundaries from the limitations section rather than from formal use guidance.

#### 6.2.2 Documentation of development process

- **Rating:** 3
- **Evidence:** The paper describes rule extraction, CAD representation, QA generation, and human review.
- **Missing evidence:** Detailed annotation manuals, review rubrics, and full provenance records are not included.
- **Reviewer rationale:** Development is documented at paper level but not at audit-reconstruction level.
- **Interpretation caution:** Independent replication of item creation would require additional maintainer information.

#### 6.2.3 Documentation of scoring and metrics

- **Rating:** 3
- **Evidence:** Metrics are described in the paper and implemented in public code.
- **Missing evidence:** Some edge-case behavior and parser failure modes are not summarized in a standalone scoring specification.
- **Reviewer rationale:** Scoring documentation is mostly adequate for research users.
- **Interpretation caution:** Users should inspect the metric code before interpreting close score differences or unusual prediction formats.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- **Rating:** 1
- **Evidence:** The GuaranteedRAG experiment reports repeated generated contexts for LLaVA-1.5, and the paper discusses sensitivity to context and image design choices.
- **Missing evidence:** No general repeated-run variance, confidence intervals, standard errors, scorer stability audit, or API-version sensitivity report is provided.
- **Reviewer rationale:** Reliability evidence is limited and mostly diagnostic.
- **Interpretation caution:** Small score differences, especially on small subsets, should not be interpreted as stable model differences.

#### 6.2.5 Documentation of validity evidence

- **Rating:** 2
- **Evidence:** The paper gives strong face/content rationale and explicitly discusses validity limitations of automatic metrics and subset sizes.
- **Missing evidence:** No convergent, discriminant, predictive, or external criterion validity study is provided.
- **Reviewer rationale:** Validity discussion is honest but preliminary.
- **Interpretation caution:** DesignQA supports exploratory validity claims better than settled measurement claims.

#### 6.2.6 Documentation of fair use and comparability

- **Rating:** 2
- **Evidence:** The paper distinguishes model versions and context/RAG conditions.
- **Missing evidence:** It does not provide a formal comparability policy covering context windows, retrieval methods, compute, cost, API access, local execution, or safety/refusal policies.
- **Reviewer rationale:** Comparability is documented for the paper's experiments but not governed for future submissions.
- **Interpretation caution:** Leaderboard or external results may not be comparable unless evaluation conditions are reported in detail.

#### 6.2.7 Documentation of maintenance and versioning

- **Rating:** 1
- **Evidence:** A public repository exists and shows ongoing use through a hackathon note.
- **Missing evidence:** No releases, changelog, version policy, scorer version pin, issue-response policy, or item update policy was identified.
- **Reviewer rationale:** Maintenance evidence exists but version governance is weak.
- **Interpretation caution:** Users should cite exact commit/date and avoid treating "DesignQA" as a stable immutable version unless they archive the materials used.

#### 6.2.8 Adequacy of documentation available to users

- **Rating:** 2
- **Evidence:** Paper and README provide usable purpose, dataset, prompt, setup, and scoring documentation.
- **Missing evidence:** Formal benchmark card, license clarity, uncertainty reporting, maintenance policy, and comparability policy.
- **Reviewer rationale:** Documentation supports competent research use but is incomplete for audit-grade benchmark governance.
- **Interpretation caution:** Responsible use requires reading the paper limitations and inspecting code, not just using the overall score.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- **Rating:** 3
- **Evidence:** README gives clone, conda, requirements, and full evaluation command instructions.
- **Missing evidence:** No container, lockfile, or fully pinned environment was identified.
- **Reviewer rationale:** Setup is clear enough for typical research users.
- **Interpretation caution:** Environment drift could affect reproducibility over time.

#### 6.3.2 Scoring procedure and error handling

- **Rating:** 3
- **Evidence:** README specifies required CSV columns and the evaluation command; paper describes metrics.
- **Missing evidence:** Error handling for malformed outputs, missing predictions, extra text, and parser edge cases is not fully documented outside code.
- **Reviewer rationale:** Scoring is operationally documented but not fully specified as a standard.
- **Interpretation caution:** Format-following failures can become score artifacts.

#### 6.3.3 Interpretation and reporting guidance

- **Rating:** 2
- **Evidence:** Paper discusses limitations and failure modes.
- **Missing evidence:** No standalone interpretation guide explains appropriate score use, uncertainty, or minimum report contents for third-party submissions.
- **Reviewer rationale:** Interpretation support is present but not standardized.
- **Interpretation caution:** Users could overread the overall score without the subset-level caveats.

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- **Rating:** 2
- **Evidence:** The paper and README imply required modalities, context access, and output formats.
- **Missing evidence:** Explicit restrictions and non-use cases are limited.
- **Reviewer rationale:** Technical prerequisites are visible; responsible-use boundaries are not.
- **Interpretation caution:** Do not use DesignQA alone to certify engineering-assistant readiness.

#### 6.3.5 Technical support and implementation guidance

- **Rating:** 2
- **Evidence:** GitHub issues and corresponding-author email provide contact routes.
- **Missing evidence:** No support SLA, maintainer policy, or troubleshooting guide was identified.
- **Reviewer rationale:** Support exists in normal academic open-source form but not as governed benchmark infrastructure.
- **Interpretation caution:** Users may need to resolve environment or data-format issues independently.

#### 6.3.6 References and supporting materials

- **Rating:** 3
- **Evidence:** The paper contains a substantial reference list and explains benchmark context.
- **Missing evidence:** Source-material licensing and standardized metadata references are incomplete.
- **Reviewer rationale:** Academic references are strong; dataset governance references are less complete.
- **Interpretation caution:** Bibliographic support should not be confused with complete dataset documentation.

#### 6.3.7 Quality of procedural instructions

- **Rating:** 3
- **Evidence:** Public setup, dataset, and scorer instructions are sufficient for running the benchmark.
- **Missing evidence:** Stronger environment pinning, edge-case scoring docs, and submission reporting requirements.
- **Reviewer rationale:** Procedural instructions are good for research replication but not fully production-grade.
- **Interpretation caution:** Report evaluation conditions explicitly when publishing DesignQA scores.

### 6.4 Overall Adequacy of Rationale and Documentation

- **Rating:** 3
- **Evidence:** DesignQA has a clear research rationale, public paper, public repository, documented task design, and public scoring implementation.
- **Missing evidence:** Versioning, uncertainty, licensing, formal validity, formal comparability, and maintenance documentation are incomplete.
- **Reviewer rationale:** The benchmark is well documented relative to many research benchmarks, but not fully documented as a long-lived measurement instrument.
- **Interpretation caution:** The review supports cautious research use, not unqualified high-stakes interpretation.

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability

- **Rating:** 3
- **Evidence:** Dataset and scorer are publicly available in the GitHub repository.
- **Missing evidence:** No immutable release artifact, dataset DOI, or versioned package was identified.
- **Reviewer rationale:** Material availability is strong but not archivally robust.
- **Interpretation caution:** Cite commit/date when using the benchmark.

#### 7.1.2 Prompts, instructions, and input materials

- **Rating:** 3
- **Evidence:** Paper and README provide task prompts, examples, and input descriptions.
- **Missing evidence:** A single machine-readable prompt manifest for all items was not confirmed.
- **Reviewer rationale:** Prompts are sufficiently documented for inspection and use.
- **Interpretation caution:** Prompt or image-format modifications may change score meaning.

#### 7.1.3 Rubrics, reference answers, and response format requirements

- **Rating:** 3
- **Evidence:** Ground truth answers and response formats are described; CSVs include answer fields.
- **Missing evidence:** Human explanation scoring rubric and adjudication rules for ambiguous answers are not fully documented.
- **Reviewer rationale:** Reference answers are usable, but some semantic equivalence issues are acknowledged by authors.
- **Interpretation caution:** Automatic reference matching can penalize acceptable but differently formatted answers.

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- **Rating:** 3
- **Evidence:** Public Python scorer, metrics module, and example commands are available.
- **Missing evidence:** No formal test suite, code quality audit, container, or scorer release policy was identified.
- **Reviewer rationale:** The harness is usable and inspectable, but not fully governed.
- **Interpretation caution:** Users should inspect scorer implementation before using results for close comparisons.

#### 7.1.5 Interface and workflow usability

- **Rating:** 3
- **Evidence:** Workflow is simple: generate predictions, add them to CSVs, and run `full_evaluation.py`.
- **Missing evidence:** No hosted evaluator or automated submission pipeline was identified; leaderboard verification is manual.
- **Reviewer rationale:** Usability is good for technical users.
- **Interpretation caution:** Nontechnical users may misformat predictions or misunderstand subset weighting.

#### 7.1.6 Accessibility across modalities, languages, and system types

- **Rating:** 2
- **Evidence:** The benchmark is designed for MLLMs and includes both text-only and visual tasks.
- **Missing evidence:** No alternative modality route, accessibility analysis, non-English adaptation, or support for non-visual systems is documented.
- **Reviewer rationale:** The benchmark is intentionally modality-specific, but accessibility and cross-system analysis are limited.
- **Interpretation caution:** Text-only or non-image-capable systems are not comparable on the full benchmark.

#### 7.1.7 Licensing, use requirements, and risk warnings

- **Rating:** 1
- **Evidence:** The repository is public and the paper is public.
- **Missing evidence:** Clear license terms, source-artifact reuse terms, risk warnings, and commercial-use guidance were not identified in the inspected sources.
- **Reviewer rationale:** Public availability does not substitute for license clarity.
- **Interpretation caution:** Users should verify license and source-material reuse conditions before redistribution or commercial use.

#### 7.1.8 Overall quality of benchmark materials

- **Rating:** 3
- **Evidence:** Public dataset, prompts, images, scorer, and README support practical use.
- **Missing evidence:** License clarity, release tags, containerization, test suite, and standardized metadata.
- **Reviewer rationale:** Materials are high quality for an academic research benchmark, with lifecycle/governance gaps.
- **Interpretation caution:** Reproducibility is feasible but depends on users pinning the exact repository state and evaluation conditions.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- **Rating:** 2
- **Evidence:** The paper reports naive baselines and compares model results to them.
- **Missing evidence:** Formal chance levels, floor/ceiling analysis, and statistical uncertainty around baseline differences are not comprehensively documented.
- **Reviewer rationale:** Baselines help contextualize performance but do not fully anchor the score scale.
- **Interpretation caution:** A model's advantage over naive baselines should not be equated with expert-level engineering understanding.

#### 8.1.2 Human or expert baselines

- **Rating:** 1
- **Evidence:** Experts and engineers helped create and review items.
- **Missing evidence:** No full human, expert, student-engineer, or professional-engineer performance baseline was identified.
- **Reviewer rationale:** Expert involvement supports item quality but not score interpretation against human ability.
- **Interpretation caution:** Do not interpret model scores as above or below human engineering performance without a human baseline.

#### 8.1.3 Model comparator cohort

- **Rating:** 3
- **Evidence:** The paper compares GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, and LLaVA-1.5 under documented conditions.
- **Missing evidence:** Model cohort is time-bound to April-August 2024; no ongoing standardized cohort policy was identified.
- **Reviewer rationale:** The comparator cohort is useful and diverse for the paper's time.
- **Interpretation caution:** Historical rankings may become stale quickly as MLLMs and context windows change.

#### 8.1.4 Historical, version, or benchmark-family comparators

- **Rating:** 2
- **Evidence:** The paper compares DesignQA conceptually to related QA and MLLM benchmarks.
- **Missing evidence:** No empirical cross-benchmark correlation or longitudinal tracking study is provided.
- **Reviewer rationale:** Literature comparators clarify novelty but do not calibrate score meaning.
- **Interpretation caution:** Users cannot infer how DesignQA scores translate to MMMU, InfoSeek, QASPER, or real engineering task performance.

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- **Rating:** 1
- **Evidence:** The benchmark reports numeric scores.
- **Missing evidence:** No criterion thresholds or qualitative score categories are defined.
- **Reviewer rationale:** No evidence supports threshold-based interpretation.
- **Interpretation caution:** Avoid labels such as "competent engineering assistant" based on score alone.

#### 8.1.6 Representativeness of reference groups

- **Rating:** 2
- **Evidence:** Model comparators include major closed and open models from the paper period.
- **Missing evidence:** Comparator selection is not a systematic sample of model families, model sizes, retrieval systems, or domain-specialized systems.
- **Reviewer rationale:** Comparators are appropriate examples, not a complete reference population.
- **Interpretation caution:** Rankings are illustrative of selected systems and conditions.

#### 8.1.7 Currency and maintenance of baseline evidence

- **Rating:** 2
- **Evidence:** The repository includes a leaderboard route for future results.
- **Missing evidence:** No documented schedule for refreshing baselines, retiring stale model versions, or re-running old submissions.
- **Reviewer rationale:** The public route can support currency, but governance is unclear.
- **Interpretation caution:** Compare models by evaluation date and condition, not just leaderboard position.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- **Rating:** 2
- **Evidence:** The paper includes naive baselines, multiple MLLM comparators, and diagnostic conditions.
- **Missing evidence:** Human baselines, formal score thresholds, uncertainty intervals, and ongoing baseline governance.
- **Reviewer rationale:** Reference interpretation is adequate for exploratory research but limited for strong comparative claims.
- **Interpretation caution:** DesignQA scores should be reported as benchmark-condition results, not as calibrated engineering competence levels.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- **Rating:** 1
- **Evidence:** Some sensitivity analyses are reported, including context/RAG effects and drawing dimensioning effects.
- **Missing evidence:** No broad reliability plan, repeated-run protocol, inter-reviewer agreement, confidence intervals, or score precision model.
- **Reviewer rationale:** Reliability is discussed indirectly but not systematically measured.
- **Interpretation caution:** Use subset scores and large differences more confidently than small aggregate differences.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- **Rating:** 1
- **Evidence:** Appendix A reports some model settings; GuaranteedRAG is generated five times for one LLaVA experiment.
- **Missing evidence:** Repeated stochastic runs across all model conditions and fixed seed policies are absent.
- **Reviewer rationale:** Stability evidence is too narrow to support robust rank comparisons.
- **Interpretation caution:** Re-running models with different seeds, API versions, or retrieval outputs may change scores.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- **Rating:** 1
- **Evidence:** Some standard deviation is reported for the GuaranteedRAG experiment.
- **Missing evidence:** No confidence intervals or standard errors for headline subset or overall scores.
- **Reviewer rationale:** Uncertainty reporting is materially incomplete, especially for small subsets.
- **Interpretation caution:** Functional Performance has only 16 items; one item changes accuracy by 6.25 percentage points.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- **Rating:** 2
- **Evidence:** Scorer code is public and metrics are deterministic once predictions are provided.
- **Missing evidence:** No scorer unit tests, parser validation report, or edge-case audit was identified.
- **Reviewer rationale:** Determinism helps reliability, but metric validity and parser edge cases remain documented concerns.
- **Interpretation caution:** Output-format differences can create score differences unrelated to engineering understanding.

#### 9.3.2 Human rater or expert scorer agreement

- **Rating:** 1
- **Evidence:** Manually generated QAs were reviewed by other parties.
- **Missing evidence:** No inter-rater agreement statistics, adjudication logs, or expert-review reliability data.
- **Reviewer rationale:** Human review improves confidence but is not quantified.
- **Interpretation caution:** Ground-truth ambiguity cannot be estimated from available agreement evidence.

#### 9.3.3 Model-as-judge reliability and validity checks

- **Rating:** n/a
- **Evidence:** DesignQA does not use an LLM-as-judge as the primary scorer.
- **Missing evidence:** n/a.
- **Reviewer rationale:** Automated lexical, accuracy, and embedding metrics are used instead.
- **Interpretation caution:** n/a.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- **Rating:** 2
- **Evidence:** The authors discuss prompt and image-format choices as limitations and analyze additional context in some Dimension questions.
- **Missing evidence:** No systematic prompt-variant or response-format robustness study across all subsets.
- **Reviewer rationale:** Sensitivity is acknowledged but not fully quantified.
- **Interpretation caution:** Prompt changes may create nontrivial score changes.

#### 9.4.2 Form, split, version, or refresh equivalence

- **Rating:** 1
- **Evidence:** The benchmark appears to have one public form.
- **Missing evidence:** No alternate-form equivalence, hidden split, refresh policy, or version equivalence evidence.
- **Reviewer rationale:** Form equivalence is not established.
- **Interpretation caution:** Future modified forms should not be compared to the original without equating evidence.

#### 9.4.3 Execution environment and dependency stability

- **Rating:** 2
- **Evidence:** Setup uses Python 3.10 and `requirements.txt`.
- **Missing evidence:** No container, lockfile, or annual reproducibility check was identified.
- **Reviewer rationale:** Environment documentation exists but could drift.
- **Interpretation caution:** Archive dependencies or use a controlled environment for reproducible studies.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- **Rating:** 1
- **Evidence:** Paper tables compare model scores, and the authors discuss qualitative differences.
- **Missing evidence:** No statistical tests or uncertainty intervals for model comparisons are reported.
- **Reviewer rationale:** Score differences are interpretable directionally, but statistical precision is unsupported.
- **Interpretation caution:** Do not make strong claims from small score gaps, especially on small subsets or mixed evaluation conditions.

### 9.6 Overall Reliability, Precision, and Score Stability

- **Rating:** 1
- **Evidence:** Deterministic scoring code, documented model settings, and some sensitivity diagnostics.
- **Missing evidence:** Confidence intervals, repeated-run variance, item reliability, human agreement, prompt stability, and environment stability evidence.
- **Reviewer rationale:** Reliability is the benchmark's weakest measurement area.
- **Interpretation caution:** Use DesignQA mainly for diagnostic profiles and large performance differences unless additional uncertainty analysis is performed.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- **Rating:** 3
- **Evidence:** Items are built from real Formula SAE rules, real CAD-related artifacts, engineering drawings, and expert-designed QA tasks.
- **Missing evidence:** Coverage is limited to one rulebook, one design competition context, and six task types.
- **Reviewer rationale:** Content validity is strong for the narrow Formula SAE requirements-interpretation domain.
- **Interpretation caution:** Do not generalize directly to all engineering documentation or all design standards.

#### 10.1.2 Construct breadth and capability-domain coverage

- **Rating:** 2
- **Evidence:** The benchmark covers retrieval, terminology recognition, component presence, dimensional compliance, and functional compliance.
- **Missing evidence:** It does not cover many engineering documentation tasks such as change impact analysis, multi-document standards conflicts, CAD-native interaction, design generation, certification workflows, or collaborative engineering review.
- **Reviewer rationale:** The covered subskills are plausible but incomplete for the broader construct.
- **Interpretation caution:** The benchmark is best viewed as a sampled capability profile, not a complete engineering-documentation measure.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- **Rating:** 2
- **Evidence:** Six task subsets provide a meaningful internal structure.
- **Missing evidence:** No factor analysis, reliability by subdomain, or empirical dimensionality study is provided.
- **Reviewer rationale:** The designed structure is interpretable but not psychometrically validated.
- **Interpretation caution:** Subsets should be interpreted as designed task families, not validated latent dimensions.

#### 10.2.2 Item or task behavior across the score scale

- **Rating:** 2
- **Evidence:** The paper analyzes failure modes and reports different performance levels by subset and condition.
- **Missing evidence:** No item difficulty calibration, discrimination analysis, or score-scale coverage analysis.
- **Reviewer rationale:** Item behavior evidence exists but is not formal.
- **Interpretation caution:** Score scale coverage and ceiling/floor properties remain uncertain for future models.

#### 10.2.3 Failure modes and error analysis

- **Rating:** 3
- **Evidence:** The paper gives concrete failure analyses for retrieval, compilation, component recognition, scale-bar interpretation, dimensional reasoning, and functional performance questions.
- **Missing evidence:** Error categories are not provided as a complete coded dataset.
- **Reviewer rationale:** Failure-mode discussion is a strength and supports diagnostic use.
- **Interpretation caution:** Qualitative failure examples should not be treated as prevalence estimates without coded counts.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- **Rating:** 2
- **Evidence:** Metrics are matched to subset response types and implemented publicly.
- **Missing evidence:** The authors themselves note automatic metric limitations; no human-equivalence validation is provided for BLEU/ROUGE/SBERT explanation scores or format-sensitive cases.
- **Reviewer rationale:** Metrics are practical and transparent but only partly valid for semantic understanding.
- **Interpretation caution:** A lower score can reflect formatting or reference mismatch rather than a false engineering judgment.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- **Rating:** 2
- **Evidence:** The paper identifies potential effects of RAG quality, component mention type, dimensioning style, and prompt/image format.
- **Missing evidence:** No complete shortcut audit, contamination audit, or response-format robustness study.
- **Reviewer rationale:** The authors recognize construct-irrelevant variance, but controls remain limited.
- **Interpretation caution:** Scores may partly reflect retrieval pipeline quality, context window size, formatting compliance, or visual OCR ability.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- **Rating:** 1
- **Evidence:** The paper compares DesignQA conceptually with related benchmarks and uses real engineering artifacts.
- **Missing evidence:** No empirical correlation with human engineering performance, real design workflow success, or other benchmark scores.
- **Reviewer rationale:** External validity evidence is minimal.
- **Interpretation caution:** It is unknown whether DesignQA predicts performance in practical engineering-documentation workflows.

#### 10.4.2 Convergent and discriminant evidence

- **Rating:** 1
- **Evidence:** DesignQA is contrasted with other benchmark types in related work.
- **Missing evidence:** No convergent/discriminant validation against other multimodal, long-document, or engineering benchmarks.
- **Reviewer rationale:** Conceptual comparison does not establish empirical relations.
- **Interpretation caution:** High DesignQA performance may or may not align with broad multimodal reasoning or long-context benchmark performance.

#### 10.4.3 Ecological or predictive relevance

- **Rating:** 2
- **Evidence:** The use of Formula SAE rules and MIT Motorsports data gives strong ecological flavor relative to synthetic benchmarks.
- **Missing evidence:** No study shows that DesignQA scores predict assistance quality in actual engineering design workflows.
- **Reviewer rationale:** Ecological plausibility is good, predictive evidence is absent.
- **Interpretation caution:** Treat DesignQA as a proxy for parts of engineering requirements work, not a validated deployment predictor.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- **Rating:** 1
- **Evidence:** Authors state that some visual inputs were not seen by models during pre-training in the same form; dataset uses MIT Motorsports artifacts not readily available from engineering companies.
- **Missing evidence:** No systematic contamination audit, public/private split, canary, or training-data overlap test.
- **Reviewer rationale:** The source design reduces some passive exposure risk, but controls are limited after public release.
- **Interpretation caution:** Public dataset exposure makes future leaderboard results vulnerable to contamination or overfitting.

#### 10.5.2 Gameability and benchmark-specific tuning controls

- **Rating:** 2
- **Evidence:** Automatic scoring and public data enable transparent testing; manual leaderboard verification asks for results and code.
- **Missing evidence:** No hidden test set, submission limits, anti-overfitting protocol, or benchmark-specific tuning disclosure policy was identified.
- **Reviewer rationale:** The benchmark is usable for research but not strongly protected against adaptive tuning.
- **Interpretation caution:** Leaderboard results should disclose whether systems were tuned on public DesignQA items.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- **Rating:** 2
- **Evidence:** The paper acknowledges limitations: one rule document, limited task types, prompt/image choices, automatic metric limits, and small subsets.
- **Missing evidence:** Public-facing title and summaries still use broad "engineering documentation understanding" language without a formal benchmark card.
- **Reviewer rationale:** The paper is appropriately cautious in limitations, but the headline construct remains broad.
- **Interpretation caution:** Claims should be phrased as "DesignQA-style Formula SAE engineering requirements QA" unless additional evidence is provided.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- **Rating:** n/a
- **Evidence:** The inspected DesignQA sources do not claim to measure AGI, agency, autonomy, or broad general intelligence.
- **Missing evidence:** n/a.
- **Reviewer rationale:** AGI-specific evaluation is not applicable.
- **Interpretation caution:** DesignQA results should not be repurposed as evidence for AGI or autonomous engineering capability.

### 10.7 Overall Validity Support

- **Rating:** 2
- **Evidence:** Strong face/content validity for a narrow, real-world-inspired engineering requirements benchmark; explicit task decomposition; public metrics; author-discussed limitations.
- **Missing evidence:** External validity, human baseline, convergent/discriminant evidence, uncertainty, contamination controls, and robust semantic metric validation.
- **Reviewer rationale:** Validity support is promising but preliminary. The benchmark supports diagnostic research use better than broad capability claims.
- **Interpretation caution:** The valid score interpretation is bounded to performance on the DesignQA task set and documented evaluation conditions.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- **Rating:** 2
- **Evidence:** The construct is relevant for MLLMs intended to assist with technical documentation and engineering design.
- **Missing evidence:** No explicit analysis of relevance across model classes, domains, languages, engineering disciplines, or user groups.
- **Reviewer rationale:** Relevance is plausible but not broadly documented.
- **Interpretation caution:** Full benchmark scores are only meaningful for systems capable of both visual and long-document inputs.

#### 11.1.2 Documentation of fair-use considerations

- **Rating:** 1
- **Evidence:** The paper identifies benchmark limitations and some context sensitivity.
- **Missing evidence:** No dedicated fairness, accessibility, bias, or responsible-use section was identified.
- **Reviewer rationale:** Fair-use documentation is minimal.
- **Interpretation caution:** Users must supply their own responsible-use framing when reporting results.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- **Rating:** 2
- **Evidence:** Public materials and automatic scoring support broad research access.
- **Missing evidence:** No accessibility analysis for systems lacking image input, users with limited compute, or non-English/non-FSAE contexts.
- **Reviewer rationale:** The benchmark is accessible as code/data but limited by intended modality and domain.
- **Interpretation caution:** Comparisons excluding text-only models or low-context models should state why the benchmark requires these capacities.

#### 11.2.2 Domain, language, modality, and subgroup coverage

- **Rating:** 1
- **Evidence:** The benchmark covers English Formula SAE documentation and vehicle-design visuals.
- **Missing evidence:** No coverage across languages, engineering domains, cultures, document standards, or user groups.
- **Reviewer rationale:** Coverage is intentionally narrow.
- **Interpretation caution:** Do not infer cross-domain or multilingual engineering-documentation competence.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- **Rating:** 2
- **Evidence:** The paper distinguishes exact model versions and conditions; the scorer is common across prediction files.
- **Missing evidence:** No standardized future-submission prompting, sampling, context, retrieval, compute, or cost policy.
- **Reviewer rationale:** Scoring is comparable, but administration conditions can vary substantially.
- **Interpretation caution:** Full-context and RAG systems should not be compared without condition labels.

#### 11.3.2 Access, compute, tooling, and API or local comparability

- **Rating:** 2
- **Evidence:** The paper describes AllRules, RAG, and GuaranteedRAG conditions; repository users can run any system and score predictions.
- **Missing evidence:** No policy normalizes context-window differences, retrieval tools, closed-API vs local access, cost, or hardware.
- **Reviewer rationale:** The benchmark can compare systems, but condition heterogeneity is a major interpretive risk.
- **Interpretation caution:** A high score may reflect a superior retrieval/scaffolding setup rather than only base MLLM capability.

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- **Rating:** 1
- **Evidence:** Public leaderboard route exists.
- **Missing evidence:** No stale-score handling, model re-run policy, date-based cohort labeling, or benchmark refresh policy was identified.
- **Reviewer rationale:** Temporal comparability is not governed.
- **Interpretation caution:** Results from different dates may reflect different model versions, API behavior, or repository state.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- **Rating:** 1
- **Evidence:** The paper examines performance by component mention type and drawing dimensioning system.
- **Missing evidence:** No broader bias, language, domain, user-group, or modality fairness analysis.
- **Reviewer rationale:** The diagnostic analyses are relevant but not fairness analyses.
- **Interpretation caution:** Performance differences may exist across engineering domains or visual styles not sampled by DesignQA.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- **Rating:** 1
- **Evidence:** Some context and subset analyses are reported.
- **Missing evidence:** No reliability/validity evidence by domain subgroup, document type, language, model class, or engineering discipline.
- **Reviewer rationale:** Subgroup measurement quality is not established.
- **Interpretation caution:** Use subset diagnostics, but avoid subgroup-level claims.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- **Rating:** 2
- **Evidence:** The paper limitations help bound interpretation.
- **Missing evidence:** No explicit non-use cases, deployment cautions, procurement warnings, or model-certification restrictions.
- **Reviewer rationale:** Limits are visible but not operationalized as guidance.
- **Interpretation caution:** DesignQA should not be used alone for engineering safety certification or procurement decisions.

#### 11.5.2 Release rules and sensitive-content handling

- **Rating:** 2
- **Evidence:** Public release through GitHub and manual leaderboard verification are documented.
- **Missing evidence:** No privacy, sensitive-content, data-use, or release governance policy was identified.
- **Reviewer rationale:** Sensitive content risk appears low, but release governance is underdocumented.
- **Interpretation caution:** Public item release increases contamination risk for leaderboard use.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- **Rating:** 2
- **Evidence:** Public materials, common scoring code, and documented model conditions support cautious comparisons.
- **Missing evidence:** Fairness analysis, standardized administration policy, temporal governance, and explicit non-use guidance.
- **Reviewer rationale:** Appropriate for research diagnostics, weaker for public rankings or cross-system claims.
- **Interpretation caution:** Report context provision, retrieval method, model version, date, and scorer state with every score.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope

- **Rating:** 3
- **Evidence:** The paper reports detailed subset scores and diagnostic analyses. The repository generates per-question and subset information. The website provides public benchmark communication.
- **Missing evidence:** Leaderboard detail, update policy, and full audit traces for submitted systems are not fully documented in inspected sources.
- **Reviewer rationale:** Paper reporting is strong; leaderboard/reporting governance is lighter.
- **Interpretation caution:** Use paper tables for detailed interpretation; leaderboard summaries may omit needed conditions.

#### 12.1.2 Score granularity and level of detail

- **Rating:** 2
- **Evidence:** Subset scores are granular and diagnostically useful.
- **Missing evidence:** Overall simple averaging across highly unequal subsets can obscure item-count imbalance; no uncertainty accompanies granular scores.
- **Reviewer rationale:** Granularity helps, but precision is not quantified.
- **Interpretation caution:** Do not rank systems by small differences in the overall score.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- **Rating:** 2
- **Evidence:** Paper reports model versions and AllRules/RAG conditions.
- **Missing evidence:** No confidence intervals, complete run metadata standard, scorer version tag, or leaderboard cohort policy.
- **Reviewer rationale:** Basic traceability exists for the paper runs, but uncertainty and current leaderboard governance are incomplete.
- **Interpretation caution:** Public score claims should include condition and date labels.

#### 12.2.2 Reproducibility and traceability of reported scores

- **Rating:** 2
- **Evidence:** Dataset and scorer are public, and the README gives example evaluation commands.
- **Missing evidence:** Complete raw outputs/configs for all paper model runs and immutable scorer releases were not confirmed.
- **Reviewer rationale:** Reproducibility is plausible for new runs, less complete for exact paper reproduction.
- **Interpretation caution:** Reproductions may differ if model APIs or dependencies changed.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- **Rating:** 2
- **Evidence:** The paper links subset scores to task interpretations and includes a limitations section.
- **Missing evidence:** The website/leaderboard framing does not appear to include a detailed score-interpretation guide or claim-limit statement.
- **Reviewer rationale:** Technical reporting is responsible, but public-facing reporting could more clearly constrain claims.
- **Interpretation caution:** Public readers may overgeneralize "engineering documentation understanding" from benchmark scores.

#### 12.3.2 Raw outputs, per-item data, or trace availability

- **Rating:** 2
- **Evidence:** The repository scorer can produce per-question scores, and the README references example LLaVA evaluation CSVs.
- **Missing evidence:** Full raw outputs/traces for all reported models and all leaderboard submissions are not clearly available.
- **Reviewer rationale:** Auditability is partial.
- **Interpretation caution:** Independent auditing of reported scores may require additional submitted code/results.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- **Rating:** 2
- **Evidence:** The paper states limitations and reports subset results rather than only an overall score.
- **Missing evidence:** No explicit bias/fairness caveats for domain, language, model class, or modality.
- **Reviewer rationale:** Reporting is not misleading in the paper, but fairness caveats are limited.
- **Interpretation caution:** Reports should state that DesignQA is English, Formula SAE-specific, and multimodal.

#### 12.4.2 Acceptability and usability for intended audiences

- **Rating:** 3
- **Evidence:** Paper tables, README examples, and website summaries are understandable for technical audiences.
- **Missing evidence:** No simplified benchmark card or structured metadata was identified.
- **Reviewer rationale:** Usability is good for researchers and developers.
- **Interpretation caution:** Non-expert readers need additional cautions about score uncertainty and construct scope.

#### 12.4.3 Public communication and leaderboard governance

- **Rating:** 2
- **Evidence:** README states that leaderboard submissions should be made through GitHub issues with results and code for manual verification.
- **Missing evidence:** No public eligibility rules, versioning rules, uncertainty rules, stale-score policy, or tuning disclosure policy was identified.
- **Reviewer rationale:** Manual verification is useful but governance remains informal.
- **Interpretation caution:** Leaderboard readers should not assume scores are directly comparable without condition metadata.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- **Rating:** 2
- **Evidence:** Paper reporting is detailed and the public repository supports reproducible scoring.
- **Missing evidence:** Uncertainty reporting, leaderboard governance, raw-output auditability, version labeling, and public interpretation guidance.
- **Reviewer rationale:** Reports support cautious technical use, but public ranking and public claims require stronger safeguards.
- **Interpretation caution:** Publish subset scores, conditions, and limitations alongside any headline DesignQA score.

---

## Final Evaluation

### Evaluative Report of the Benchmark

DesignQA is a valuable and unusually domain-grounded benchmark for probing MLLMs on engineering requirements tasks that combine long technical text with CAD-derived and engineering-drawing visuals. Its main strengths are its real source materials, expert-informed item construction, granular task decomposition, public dataset, and public automated scorer. It is especially useful as a diagnostic research benchmark for identifying whether systems can retrieve relevant rules, recognize technical components, interpret drawings, and make constrained compliance judgments under documented context-delivery conditions.

As a measurement instrument, its current limitations are concentrated in reliability, generalizability, score interpretation, and lifecycle governance. The benchmark is based on one rulebook and one vehicle-design context; the subsets are highly imbalanced; the smallest subset has only 16 items; the automatic metrics can penalize formatting or fail to capture semantic equivalence; and the official materials do not provide general confidence intervals, human baselines, contamination controls, immutable releases, or formal leaderboard governance. These gaps do not make DesignQA a poor benchmark, but they restrict the interpretation of its scores.

DesignQA is therefore best used for research diagnostics and model-development comparisons when users report model version, date, context/RAG condition, prompts, sampling settings, and scorer version. It should not be used alone to claim broad engineering competence, deployment readiness, engineering safety assurance, or general intelligence.

### Conclusions

DesignQA is a strong early benchmark for Formula SAE-style multimodal engineering-requirements QA, with good task design and public materials but limited reliability, validity, and lifecycle evidence for broad claims. Responsible administration and interpretation require technical familiarity with MLLM evaluation, retrieval/context effects, automatic text metrics, and the benchmark's domain-specific limitations.

### Recommendations

1. **Benchmark maintainers:** Publish immutable releases with dataset/scorer version tags, release notes, and a clear license.
2. **Benchmark maintainers:** Add a benchmark card documenting intended uses, non-use cases, source provenance, contamination risks, and submission requirements.
3. **Benchmark maintainers:** Add uncertainty reporting for paper and leaderboard scores, including confidence intervals or bootstrap intervals by subset.
4. **Benchmark maintainers:** Provide a standardized submission template requiring model version, date, prompts, context/RAG method, sampling settings, hardware/API route, and tuning disclosure.
5. **Benchmark maintainers:** Add a human or expert baseline, especially for compliance subsets, to calibrate score interpretation.
6. **Benchmark maintainers:** Validate explanation scoring against human judgments or provide a human-audited subset for semantic equivalence checks.
7. **Benchmark users:** Report subset scores, not only the simple-average overall score, because item counts and metric meanings differ sharply across subsets.
8. **Benchmark users:** Avoid broad claims such as "understands engineering documentation" unless the claim is explicitly bounded to DesignQA's Formula SAE task sample.

### Summary of Ratings

| Section | Overall Rating (`n/a`, `0`-`4`) |
| :-- | :--: |
| Section 6. Rationale, documentation, and task/item quality | 3 |
| Section 7. Benchmark materials and usability | 3 |
| Section 8. Reference points and documented comparison groups | 2 |
| Section 9. Reliability and precision | 1 |
| Section 10. Validity support | 2 |
| Section 11. Fair use and comparability | 2 |
| Section 12. Reports, leaderboards, and public score claims | 2 |

Reviewer comments: The highest ratings reflect DesignQA's concrete domain rationale, expert-informed item construction, and public materials. Lower ratings reflect missing uncertainty, human baselines, external validity evidence, contamination controls, and formal lifecycle/leaderboard governance.

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected entity or reporting surface | Affected capability domain or score interpretation | Affected rating(s) | Why it matters | Needed for a higher rating |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Confidence intervals, standard errors, or repeated-run variance | Paper tables, repository scorer, leaderboard | Meaningfulness of score differences and rankings | 6.2.4, 9.2.2, 9.5.1, 12.2.1 | Users cannot tell whether close model differences are stable. | Publish uncertainty intervals by subset and overall score. |
| Human or expert performance baseline | Paper and benchmark reports | Calibration against engineering users | 8.1.2, 10.4.1 | Model scores lack a human reference point. | Run student-engineer and/or professional-engineer baselines. |
| Formal scoring edge-case specification | Evaluation harness and README | Validity of automatic metrics and format-sensitive scoring | 6.2.3, 7.1.3, 10.3.1 | Format issues, child-rule inclusion, and semantic equivalence can distort scores. | Add parser/metric specification, tests, and adjudication examples. |
| Complete item-development documentation | Dataset provenance and item quality | Item quality, coverage, and review reliability | 6.1.5, 6.1.6, 6.1.7 | Expert review is valuable but not fully auditable. | Publish annotation guidelines, review protocol, and agreement/adjudication statistics. |
| Construct coverage matrix | Paper and dataset documentation | Generalization beyond Formula SAE | 10.1.1, 10.1.2, 10.6.1 | The target claim is broader than one rulebook and vehicle context. | Map items to requirements-engineering task taxonomy and document excluded tasks. |
| Contamination and overfitting controls | Public dataset and leaderboard | Future leaderboard validity | 10.5.1, 10.5.2, 11.5.2 | Public items can be trained on or tuned against. | Add hidden/held-out set, tuning disclosure, submission limits, or contamination audit. |
| Versioning and release policy | Repository and scorer | Reproducibility and temporal comparison | 5.8, 6.2.7, 7.1.1, 12.2.1 | Scores may refer to different repository states or scorer behavior. | Publish release tags, changelog, scorer version IDs, and archival DOI. |
| Leaderboard governance and submission metadata | Official leaderboard | Public comparability and score claims | 8.1.7, 11.3.1, 12.4.3 | Manual verification is not enough to ensure comparable public rankings. | Require standardized metadata and publish eligibility, update, and stale-score rules. |
| License and source-artifact reuse terms | Repository, dataset, source CAD/rules | Reuse, redistribution, and commercial use | 6.1.8, 7.1.7 | Users may not know what rights apply to code, data, images, or source materials. | Add explicit licenses and source-material reuse notes. |

### Validation Notes

| Check | Result |
| :-- | :-- |
| Existing review overwrite check | `reviews/DesignQA.md` did not exist before drafting. |
| Part A descriptive boundary | Part A records facts, source limits, and missing documentation without ratings. |
| Part B evidence discipline | Each rating includes evidence, missing evidence, reviewer rationale, and interpretation caution. |
| Major template coverage | Sections 1-12, final evaluation, summary ratings, gap register, and bibliography are represented. |
| Rating consistency | Overall ratings align with the detailed subsection evidence. |
| Local validation script | No visible `tools/` validation script was present in this checkout; validation is manual/static. |

---

## Bibliography

1. Anna C. Doris, Daniele Grandi, Ryan Tomich, Md Ferdous Alam, Mohammadmehdi Ataei, Hyunmin Cheong, and Faez Ahmed. "DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation." arXiv:2404.07917v2, 2024. Local transcript: `literature/DesignQA.md`; original PDF: `Papers/DesignQA.pdf`; arXiv: <https://arxiv.org/abs/2404.07917>.
2. DesignQA official repository. `anniedoris/design_qa`. <https://github.com/anniedoris/design_qa/>. Accessed 2026-06-28.
3. DesignQA official website and leaderboard route. <https://design-qa.github.io/>. Accessed 2026-06-28.
4. EFPA. "EFPA Test Review Model - Version 2025." Local transcription used through `literature/EFPA_Test_Review_Model_2025_Markdown.md`.
5. A. Reuel et al. "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices." Local transcription used through `literature/betterbench.md`.
6. A. M. Bean et al. "Measuring what Matters: Construct Validity in Large Language Model Benchmarks." Local transcription used through `literature/Measuring_what_Matters.md`.

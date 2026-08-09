# MESA Review: DesignQA

Reviewer: Claude (Opus 4.8), as MESA benchmark reviewer agent (reviewer 2)
Date of review: 2026-06-28
Template: `MESA EFPA template official.md` (MESA EFPA Template)

---

## Short Stand-Alone Non-Evaluative Benchmark Description

DesignQA is a multimodal question-answering benchmark for evaluating multimodal large language models (MLLMs) on understanding and applying engineering design requirements in technical documentation. It was developed by researchers at MIT and Autodesk Research (Doris et al., arXiv:2404.07917v2, 23 August 2024) using the 140-page Formula SAE (FSAE) 2024 rule document together with real CAD models and test data supplied by the MIT Motorsports team. The benchmark contains 1,451 question-answer pairs grouped into three segments that mirror tasks engineers perform when designing to a requirement document - Rule Extraction, Rule Comprehension, and Rule Compliance - each split into two subsets: Retrieval (1,192 QAs), Compilation (30), Definition (31), Presence (62), Dimension (120), and Functional Performance (16). Its defining characteristic is that it poses document-grounded "multi-source" visual question-answers, in which the input image (a CAD view or engineering drawing) and the input document (the FSAE rules) come from different sources and the image was not seen during model pre-training. Every subset has a fully automatic evaluation metric (variants of F1, accuracy, and BLEU-2/ROUGE-L/Sentence-BERT similarity for compliance explanations), so new models can be scored without human raters. The authors evaluate GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, and LLaVA-1.5 under several context-delivery conditions (full rules in context, simple LlamaIndex RAG, and a keyword-matched GuaranteedRAG diagnostic). The benchmark is publicly distributed via the GitHub repository `anniedoris/design_qa`, with a manually maintained, issue-mediated leaderboard.

---

## Source Inventory

| Material / Source Type      | URL, Location, or Identifier                                                                                                                              | Access Date |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| Paper / Technical Report    | Doris, Grandi, Tomich, Alam, Ataei, Cheong, Ahmed, "DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation," arXiv:2404.07917v2, 23 Aug 2024 (PRIMARY) | 2026-06-28  |
| Code Repository             | `https://github.com/anniedoris/design_qa/` (default branch `main`)                                                                                       | 2026-06-28  |
| Dataset / Task / Prompt Set | `dataset/` subfolders: `rule_extraction/`, `rule_comprehension/`, `rule_compliance/` (CSV + image folders)                                               | 2026-06-28  |
| Evaluation Harness / Runner | `eval/full_evaluation.py` (produces `results.txt`); metrics in `eval/metrics/metrics.py`                                                                 | 2026-06-28  |
| Leaderboard / Results Portal| `https://design-qa.github.io/` (project page); submissions via GitHub issue + `.txt` results + code, manually verified                                    | 2026-06-28  |
| License                     | No `LICENSE` file (raw `LICENSE` path returns HTTP 404); GitHub API reports `license: null`                                                               | 2026-06-28  |
| Changelog / Release Logs    | None located; repository has no GitHub Releases and no CI/build status                                                                                    | 2026-06-28  |
| Repository Metadata         | Created 2023-11-28; last push 2025-08-10; 13 open issues at access date; `has_pages: false` (site served via `design-qa.github.io`); no homepage field    | 2026-06-28  |
| Contextual Literature       | `literature/Measuring_what_Matters.md` (construct validity); `literature/betterbench.md` (lifecycle quality); `literature/A_Definition_of_AGI.md` (CHC domains) | 2026-06-28  |
| Feedback / Contact Channels | GitHub issue tracker on `anniedoris/design_qa`; corresponding author email (adoris@mit.edu)                                                              | 2026-06-28  |

Reviewer comments: All Part A numeric and structural facts trace to the verbatim paper transcription in `literature/DesignQA.md`. Repository-state facts (license, scorer paths, folder layout, leaderboard mechanism, issue count, dates) were re-verified live on 2026-06-28. The leaderboard site `design-qa.github.io` exists and renders the project landing page with navigation, but the live results-table contents and any governance text could not be rendered at access time and are flagged as unresolved rather than asserted. Interpretive literature is used only to discipline Part B reasoning, not as a source of Part A facts.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt                                    | Description                                       |
| :---------------------------------------- | :------------------------------------------------ |
| Reviewer Name                             | Claude (Opus 4.8), MESA benchmark-reviewer role (reviewer 2) |
| Date of Current Review                    | 2026-06-28                                        |
| Date of Previous Review _(if applicable)_ | n/a                                               |

### 1.2 Benchmark Identity & Provenance

| Prompt                                 | Description                                                                                                                              |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Reviewed Entity Name                   | DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation                        |
| Short Name / Acronym                   | DesignQA                                                                                                                               |
| Entity Type                            | Original benchmark with a public GitHub repository, an automatic evaluation harness, and a manually maintained issue-mediated leaderboard |
| Parent / Source Benchmark              | None. The benchmark is newly constructed from the FSAE 2024 rule document and MIT Motorsports CAD/test data; it is methodologically situated against InfoSeek, MMMU, ScienceQA, QASPER, ZeroScrolls, and similar QA/VQA benchmarks but does not derive items from them |
| Exact Version / Release Split          | Single static release tied to arXiv:2404.07917v2 (23 Aug 2024); repository `dataset/` provides one fully public form; no versioned splits or alternate forms documented |
| Implementation / Scorer Version        | `eval/full_evaluation.py` → `results.txt`; metric implementations in `eval/metrics/metrics.py`; no harness version tag, no CI, no release pinning located |
| Creators & Current Maintainers         | Anna C. Doris (corresponding author, MIT), Daniele Grandi (Autodesk Research), Ryan Tomich (MIT Motorsports), Md Ferdous Alam (MIT), Mohammadmehdi Ataei (Autodesk Research), Hyunmin Cheong (Autodesk Research), Faez Ahmed (MIT) |
| Host Organization / Repository Owner   | GitHub user `anniedoris` (Anna C. Doris); project page `design-qa.github.io`                                                            |
| Release Dates                          | Original arXiv v1 April 2024; v2 revision 23 Aug 2024. Repository created 2023-11-28; last push 2025-08-10                              |
| License & Access Terms                 | Fully public materials. No `LICENSE` file present (raw `LICENSE` URL returns HTTP 404; GitHub API reports `license: null`). License/redistribution terms are therefore unavailable (recorded as a documentation gap, not as an asserted restriction) |
| Persistent Identifier / DOI / Citation | arXiv:2404.07917v2 (doi: 10.48550/arXiv.2404.07917)                                                                                     |

### 1.3 Materials, Sources, & Access Tracking

See the Source Inventory above; that table is the canonical 1.3 record for this review.

Reviewer comments: The reviewed entity is the original DesignQA benchmark. The three context-delivery conditions named in the paper - AllRules (full rule document in the context window), simple LlamaIndex RAG, and GuaranteedRAG - are treated throughout this review as **evaluation conditions** applied to a fixed item set, not as separate benchmark entities. The model comparator cohort (GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, LLaVA-1.5) is likewise a reported baseline cohort, not part of the instrument.

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

- [x] Visual Processing (V)
- [x] On-the-Spot Reasoning (R)
- [x] Reading and Writing Ability (RW)
- [x] Specialized scientific or technical expertise (engineering design / domain-specific technical expertise)
- [x] General Knowledge (K) - only in the narrow sense of specialized engineering domain knowledge, not broad world knowledge
- [x] Factuality or grounding (verbatim rule retrieval and document-grounded compliance checking)
- [x] Multimodal models (multimodal + long-context document-grounded multi-source VQA)
- [ ] Mathematical Ability (M) - dimensional arithmetic is required for the Dimension subset but is not framed as the target construct
- [ ] Working Memory (WM)
- [ ] Long-Term Memory Storage (MS) / Long-Term Memory Retrieval (MR)
- [ ] Auditory Processing (A); Speed (S); Coding; Tool use; Agency; Web interaction; Embodied interaction; Multilingual; Safety; Robustness; Calibration

Reviewer comments: The authors frame the construct as MLLMs' ability to "comprehend and apply engineering requirements in technical documentation," operationalized as design-according-to-requirements. In CHC terms this composite spans Visual Processing (CAD images, engineering drawings), On-the-Spot Reasoning (applying a rule to a novel drawing), Reading and Writing (parsing and reproducing rule text), and domain-specific technical/engineering expertise. The benchmark is distinctive in requiring synthesis across an image and a long text from **different sources**, with the image absent from pre-training. The authors make **no AGI or general-intelligence claim**.

### 2.2 Area of Use

- [x] Model comparison
- [x] Research diagnostics
- [x] Capability profiling (segment/subset-level strengths and weaknesses)
- [x] Leaderboard ranking (manually maintained issue-mediated leaderboard)
- [ ] Safety evaluation; Deployment gating; Procurement; Internal regression testing; Public marketing; Policy/governance

Reviewer comments: The stated purpose is to measure and track MLLM progress on engineering-documentation tasks and to "encourage other researchers to build and train better AI models and frameworks." It is positioned as a research diagnostic, not a procurement or deployment instrument.

### 2.3 Intended AI Systems

- [x] Multimodal models
- [x] Frontier general-purpose language models
- [x] Chat or instruction-following models
- [x] Retrieval-augmented systems (RAG is an explicit evaluation condition for small-context models)
- [x] Open-weight local models (LLaVA-1.5)
- [x] API-hosted models (GPT-4o, GPT-4, Gemini-1.0, Claude-Opus)
- [ ] Base language models; Code models; Audio/speech models; Agentic systems; Tool-using systems; Domain-specialized models

Reviewer comments: Models must accept image inputs; text-only Retrieval and Compilation questions are posed with a null image so that a single multimodal interface is used throughout. Small-context models (LLaVA-1.5, Gemini-1.0) require a RAG pathway because the ~70,091-token rule text exceeds their windows.

### 2.4 Intended Users of Benchmark Outputs

- [x] AI researchers
- [x] Model developers
- [x] Benchmark creators or maintainers
- [x] Public leaderboard users
- [ ] Product teams; Safety evaluators; Policy actors; Procurement; Educators

Reviewer comments: The audience is primarily the engineering-AI and MLLM research community; the authors explicitly solicit community submissions for new models.

### 2.5 Task Families, Subdomains, and Scores

| Component | Description |
| :-------- | :---------- |
| Capability, phenomenon, or quality the benchmark claims to measure | MLLMs' ability to understand and apply engineering design requirements stated in technical documentation, by synthesizing long-text rules with CAD/drawing images |
| Definition of the capability or quality being measured | Operationalized as performance on six subsets reflecting the engineering workflow of designing to a requirement document: extract relevant rules, comprehend component terminology in visual designs, and check design compliance with dimensional and functional rules |
| Subcomponents of the claimed capability, phenomenon, or quality | Three segments (Rule Extraction, Rule Comprehension, Rule Compliance), each with two subsets: Retrieval, Compilation; Definition, Presence; Dimension, Functional Performance |
| Excluded scope or non-target abilities | Non-design FSAE content (Administrative Regulations, Document Requirements) is excluded; no claim to general world knowledge, autonomy, or cross-document generalization; authors state DesignQA uses a single rule document |
| Benchmark item / prompt families or subdomains | Verbatim rule retrieval QAs; rule-compilation-by-topic QAs; component-naming VQAs; component-presence yes/no VQAs; dimensional-compliance yes/no VQAs (+ explanation); functional-performance compliance yes/no VQAs (+ explanation) |
| Sources for benchmark items | FSAE 2024 rule document (140 pages, ~70,091 extracted tokens); four MIT Motorsports CAD models (vehicle, vehicle+aero, rear wheel package, powertrain); MIT Motorsports test/FEA data |
| Sampling method for benchmark items | Retrieval/Compilation: programmatic extraction via scripts + regex over the rule document; Comprehension/Compliance: manual, expert-authored items curated from a fixed component and rule list |
| Selection or filtering logic | Retrieval: drop empty-text rules and non-design sections, keep child rules; Compilation: 30 manually curated terms (9 with synonyms/acronyms/plurals); Definition/Presence: a 31-component list; Dimension: 20 dimension rules → 3 drawings each (no scale-bar-violating examples generated); Functional Performance: limited by availability of relevant test data |
| Splits or partitions | Single fully public form; no train/dev/test or public/hidden split. Authors suggest fine-tuning on the Retrieval QAs as a model-improvement avenue |
| Primary score | Per-subset automatic metric (no single aggregate DesignQA score is defined); each subset reports a macro-average where applicable |
| Subscores | Retrieval F1 Bag-of-Words; Compilation F1 Rules; Definition F1 Bag-of-Characters; Presence/Dimension/Functional Performance Accuracy; Rule-Compliance explanation BLEU-2, ROUGE-L, Sentence-BERT cosine Similarity |
| Derived scores | None beyond per-subset macro-averages; the GuaranteedRAG experiment reports means ± standard deviation over five runs (LLaVA-1.5 only) |
| Qualitative score ranges | None defined (no low/medium/high or novice/expert bands) |
| Boundaries or caveats for interpretations | Authors caveat: single rule document; results may not generalize to tweaked prompts/images; automatic metrics can artificially penalize format deviations and child-rule inclusion; small subset sizes affect validity |

Reviewer comments: There is no single headline DesignQA number; the benchmark is explicitly designed for fine-grained, per-subset diagnosis.

### 2.6 Model Response Mode

- [x] Short text (rule text, rule-number lists, component names, yes/no)
- [x] Long-form text (Rule Compliance explanations)
- [ ] Multiple choice; Structured output; Code; Mathematical expression; Tool call; other generation/interaction modes

Reviewer comments: Compliance items require an explanation prefixed with "Explanation:" followed by a yes/no prefixed with "Answer:".

### 2.7 Prerequisites for Evaluated Systems

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing |
| :---------- | :-------------------------: | :-------------------------: | :-----------------: |
| Language support | | [x] | |
| Context length | | [x] (≥70,091-token text for AllRules; RAG path documented for small windows) | |
| Multimodal input support | | [x] | |
| Structured output support | [x] | | |
| Exact format, schema, or parser compatibility | | [x] (comma-separated rule lists; "Explanation:"/"Answer:" prefixes) | |
| Retry, repair, or correction-loop support | [x] | | |
| Tool access | [x] | | |
| Browser or internet access | [x] | | |
| Code execution | [x] | | |
| External API or tool credentials | | [x] (provider API keys for closed models) | |
| Memory or persistent state | [x] | | |
| Environment/simulator/task-registry compatibility | [x] | | |
| API compatibility | | [x] (models invoked via LlamaIndex) | |
| Latency or time budget | [x] | | |
| Cost or compute budget | | | [x] (AllRules ~10x cost of RAG noted, but no per-run total) |

Reviewer comments: Format compliance is a genuine prerequisite because several metrics penalize format deviation directly (e.g., Compilation comma separation).

### 2.8 Evaluation Conditions

| Condition | Description |
| :-------- | :---------- |
| Prompting protocol | Fixed per-subset prompt templates appended to a shared preamble ("We are a student engineering team designing a vehicle for the FSAE competition. Attached is the FSAE rules document."); zero-shot |
| System prompt | None specified; each model's default system prompt was used |
| Few-shot examples | None (zero-shot benchmark) |
| Sampling settings | LlamaIndex defaults: temperature 0.1 for GPT-4o/GPT-4/Gemini-1.0/Claude-Opus; temperature 0.75 and top_p 0.9 for LLaVA-1.5; top_p left at each model's default for the others. max_new_tokens: 250 (Rule Extraction), 100 (Rule Comprehension), 1500 (Rule Compliance) |
| Tool permissions | None beyond the provided rule context |
| Tool/API credential policy | Evaluator supplies provider credentials; not standardized in the repo |
| Time limits | None documented |
| Human intervention rules | None during scoring (fully automatic) |
| Official rerun/retry/repair policy | None documented (GuaranteedRAG reports 5 repeats for LLaVA-1.5 to estimate variance) |
| Hardware or hosted service | Models invoked through the LlamaIndex framework; hardware not specified |
| Network requirements | API access for closed models; embeddings via OpenAI `text-embedding-3-large` for RAG |
| Sandbox or security constraints | None documented |
| Model identity and version-label requirements | Exact model IDs recorded: gpt-4o, gpt-4-1106-vision-preview, models/gemini-1.0-pro-vision, claude-3-opus-20240229, llava-1.5-13b |
| Special administration conditions | Context delivery via AllRules (full rules in context), simple LlamaIndex RAG (250-token chunks, 50-token overlap, top-15 / top-12 for Compliance, `text-embedding-3-large`), or GuaranteedRAG (8,716-character keyword-matched context, LLaVA-1.5 only, 5 repeats with std dev). Definition subset: *-RAG models received no retrieved context (RAG always returned the same section) |

Reviewer comments: The context-delivery condition materially changes scores (AllRules generally >> RAG for GPT-4o/GPT-4) and is part of the score's meaning. Claude-Opus was tested only under RAG (not AllRules) due to its input-token cost; Gemini-1.0-RAG scored 0 on Retrieval because of a "RECITATION" error that halted verbatim repetition.

### 2.9 Task Interaction and Observable Evidence Types

Selection or judgment tasks:
- [x] Classification (yes/no Presence, Dimension, Functional Performance)

Production or construction tasks:
- [x] Open-ended text (rule text, component names, compliance explanations)
- [x] Proof, derivation, or explanation (Rule Compliance explanations)
- [x] Document parsing / extraction (verbatim rule retrieval; rule compilation)

Interaction or environment tasks:
- [ ] None

Observable evidence or process data:
- [x] Raw output (model responses scored automatically)
- [ ] Latency; Token usage; Cost; Tool traces; Retrieval transcript; Reasoning traces; Execution logs; Verifier results; Environment state; Leaderboard submission metadata (results `.txt` files are submitted but per-item traces are not centrally published)

### 2.10 Input Stimulus Type

- [x] Text (FSAE rules; ~70,091 tokens for AllRules; RAG chunks otherwise)
- [x] Images (multi-view CAD images; close-up CAD images)
- [x] Charts or figures (FEA/anthropometric charts in Functional Performance)
- [x] PDF or document pages (source 140-page rule PDF)
- [x] Long-context transcript or retrieved corpus (AllRules / RAG context)
- [x] Documents (engineering drawings: direct-dimensioned and scale-bar)
- [ ] Code; Tables (only as flattened PDF text); GUI screenshots; Audio; Video; Web pages; Terminal state; APIs/tools; Dynamic environment; Simulation state; External search results

Reviewer comments: Text-only Retrieval/Compilation questions are posed with a null image. Engineering drawings use two dimensioning systems: direct dimensions and scale bars.

### 2.11 Number of Items or Measurement Points

| Prompt | Response |
| :----- | :------- |
| Total public items or tasks | 1,451 QAs |
| Total private or hidden items | 0 (no hidden split) |
| Development or example items | None separately defined |
| Test items | All 1,451 scored |
| Dynamic or generated tasks | Retrieval (1,192) and Compilation (30) ground truths generated programmatically; the rest manual |
| Episodes/trials/measurement points | Single pass per item; GuaranteedRAG: 5 repeats (LLaVA-1.5) |
| Counts by subset | Retrieval 1,192; Compilation 30; Definition 31; Presence 62; Dimension 120; Functional Performance 16 |
| Counts by segment | Rule Extraction 1,222; Rule Comprehension 93; Rule Compliance 136 |
| Counts by capability domain | Not separately tabulated to CHC domains |
| Counts by context-length bin | Not documented |
| Counts by difficulty band | Not documented |
| Counts by access status | All public |
| Item count uncertainty | Low for totals (explicitly stated); the small manual subsets are exact small counts |

Reviewer comments: The three smallest scored subsets are Functional Performance (16), Compilation (30), and Definition (31). Dimension's 120 comprise 60 base items each rendered with and without additional CAD-highlight context.

### 2.12 Mode of Evaluation

- [x] Local batch evaluation (`eval/full_evaluation.py`)
- [x] Leaderboard submission (issue-mediated, manually verified)
- [x] Public open evaluation
- [ ] Hosted platform; Private controlled evaluation; Interactive; Human-in-the-loop; Continuous/rolling; Suite/sub-leaderboard; Competition; Third-party evaluator; Registry task pack

Identity and condition controls:
- [x] No control over submitted systems (submissions are self-reported `.txt` results + code, manually verified by maintainers)
- [ ] Some control; Controlled access/audit; Controlled center; Not documented

### 2.13 Technological Arrangements

| Technology | A | R |
| :--------- | :-: | :-: |
| API access | [x] | [x] (for closed models) |
| Local inference | [x] | [ ] |
| GPU | [x] | [ ] |
| CPU-only execution | [ ] | [ ] |
| Docker or container | [ ] | [ ] |
| Python package or CLI | [x] | [x] (evaluation scripts) |
| Browser | [ ] | [ ] |
| External tools | [ ] | [ ] |
| Internet access | [x] | [x] (provider APIs, embedding API) |
| Proprietary platform | [ ] | [ ] |
| Hosted scoring service | [ ] | [ ] |
| Benchmark registry / task environment | [ ] | [ ] |
| Simulator or user simulator | [ ] | [ ] |
| Filesystem/terminal/sandbox state | [ ] | [ ] |

### 2.14 Time and Resource Requirements

| Activity | Time, compute, or cost estimate |
| :------- | :------------------------------ |
| Setup | Not quantified (clone repo, supply API keys, install dependencies) |
| Model inference or task completion | Not quantified per item |
| Token or context-window use | ~70,091 tokens for full rule text (AllRules); RAG top-15 ≈ 10,895 chars avg, top-12 ≈ 8,716 chars avg |
| Scoring | Fully automatic; runtime not quantified |
| Human adjudication | None for scoring; manual verification for leaderboard submissions |
| Analysis or reporting | Not quantified |
| Full benchmark run | Not quantified |
| API or compute cost | AllRules feeding cost stated as >10x the RAG cost; Claude-Opus AllRules omitted for cost; no dollar totals |
| External tool/service/search cost | OpenAI embedding API for RAG; not quantified |

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant | Purpose | Stated score-comparability interpretation | Status |
| :-------------- | :------ | :---------------------------------------- | :----- |
| Single public form (arXiv v2) | Sole release | n/a (no alternate forms) | Active |
| Context-delivery conditions (AllRules / simple RAG / GuaranteedRAG) | Disentangle inherent model skill from context-delivery efficacy | Not interchangeable; AllRules and RAG scores are explicitly contrasted, not equated | Reporting conditions, not forms |

Reviewer comments: The conditions are evaluation settings on a fixed item set, not separate benchmark forms.

### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [ ] All other options

Describe task selection method: A fixed 1,451-QA set built once from the FSAE 2024 rule document and MIT Motorsports data. Retrieval/Compilation answers are programmatically derived; Comprehension/Compliance items are expert-authored and reviewed.

### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [x] Reference answer (ground-truth rule text, rule lists, component names, yes/no labels, human-written explanations)
- [ ] Intermediate trace; Tool-use trace; Search transcript; Code execution; Environment/simulator state; Unit test; Patch/verifier; Coordinate/GUI target; Document-layout target; Human judge; Model judge; Ensemble; External verifier; Leaderboard submission metadata

Reviewer comments: Compliance explanation scoring compares the model explanation against a **single** human-written reference per item via BLEU-2/ROUGE-L/Similarity.

### 2.18 Broad-Claim Flags for Later Evaluation

| Prompt | Response |
| :----- | :------- |
| Term used for broad interpretation from benchmark scores | None. The benchmark uses "real-world engineering design" framing but does not invoke AGI, general intelligence, or agency |
| Breadth implied by the score interpretation across domains | Implicit generalization from one FSAE rulebook to engineering-design-requirement tasks broadly; the authors note the F1 Technical Regulations and NASA memoranda share the enumerated-rule structure |
| Depth or proficiency level implied | "Engineer designing to requirements"; no human-level or expert-parity claim is asserted as evidence |
| Capability domains from 2.1 explicitly covered | Visual Processing, On-the-Spot Reasoning, Reading and Writing, domain-specific engineering expertise |
| Capability domains explicitly excluded or not tested | Auditory, Speed, broad general knowledge, autonomy/agency, multilingual |
| Coverage across modalities, tools, memory, planning, speed | Image + long text; no tools, no planning, no speed measurement |
| Whether aggregate scores preserve capability-domain caveats | No aggregate; per-subset scores keep diagnosis granular |
| Stated AGI, autonomy, or agency caveats | None needed; no such claim is made |
| Documented broad-claim limits or non-use statements | Authors explicitly state the single-document limitation and generalizability caveat |
| Documented caveats to carry forward into Part B | Single-document generalization; automatic-metric validity; small-subset uncertainty |

Reviewer comments: DesignQA is disciplined in its claims. The only breadth flag worth carrying into Part B is the implicit move from one rulebook to "real-world engineering design," which is treated in Section 10.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

- [x] Automated semantic or embedding-based scoring (Sentence-BERT Similarity for explanations)
- [x] String-similarity scoring (F1 Bag-of-Words, F1 Bag-of-Characters, BLEU-2, ROUGE-L)
- [x] Rule-based scoring (F1 Rules over rule-number lists; accuracy on yes/no)
- [x] Output parser or extractor that turns model responses into scoreable values
- [x] Automated exact-match scoring (yes/no accuracy after extraction)
- [ ] LLM equality-checker; Unit-test; Patch/verifier; Coordinate; Layout/OCR; State-based reward; Simulator; Human rating; Model judge; Fuzzy schema-aware parsing; Pairwise; Hybrid; Leaderboard service scoring; Multi-run pass@k; Manual adjudication

### 3.2 Scores and Metrics

| Score or scoring rule/quantity | Definition | How results are combined | Capability-domain linkage stated by authors | Interpretation stated by authors |
| :----------------------------- | :--------- | :----------------------- | :------------------------------------------ | :------------------------------- |
| Retrieval | F1 Bag-of-Words between predicted and ground-truth rule text after lowercasing, whitespace/punctuation/article removal, word tokenization | Macro-average over 1,192 QAs | Document extraction / Reading | Higher = better verbatim rule retrieval from a long document |
| Compilation | F1 Rules: F1 over lists of rule numbers | Macro-average over 30 QAs | Long-document search/synthesis | Higher = better identification of all rules relevant to a topic |
| Definition | F1 Bag-of-Characters (character-level tokenization), max over synonyms | Macro-average over 31 QAs (highest per-QA score) | Visual component recognition + terminology | Higher = better naming of a highlighted CAD component |
| Presence | Accuracy on yes/no | Mean over 62 QAs | Visual presence detection | Higher = better component-presence judgment |
| Dimension | Accuracy on yes/no | Mean over 120 QAs | Drawing analysis + dimensional reasoning | Higher = better dimensional-compliance checking |
| Functional Performance | Accuracy on yes/no | Mean over 16 QAs | Functional-rule compliance | Higher = better functional-compliance checking |
| Compliance explanations | BLEU-2, ROUGE-L, Sentence-BERT cosine Similarity vs one human reference | Reported per Compliance subset | Explanation quality | Higher = closer to the human-written explanation |

Treatment of responses that fail format, schema, refusal, completion, or parsing requirements: No retry/repair. Format deviations are scored as-is - e.g., Claude-Opus-RAG's non-comma-separated Compilation answers and its "The rules relevant..." preamble lowered its F1 Rules; Gemini-1.0-RAG's RECITATION refusal yielded a 0 on Retrieval. Authors acknowledge these as artificial penalties.

Treatment of eligibility failures, API/tool blocks, timeouts, environment crashes, duplicate submissions, and other run failures: Not separately defined; a refusal/error simply scores low on the affected metric.

Retry, repair, parser fallback, platform rerun, or manual adjudication policy: None for model scoring. Leaderboard submissions are manually verified by maintainers.

### 3.3 Scale or Metric Types

- [x] Accuracy
- [x] BLEU, METEOR, or text-similarity metric (BLEU-2, Sentence-BERT Similarity)
- [x] Sequence-matcher / longest-common-subsequence ratio (ROUGE-L)
- [x] Raw score (F1 variants)
- [ ] Success rate; pass@k; unit-test pass rate; edit distance; TEDS; coordinate accuracy; win rate; Elo; pairwise; reward/return; gain score; aggregated suite score; cost-adjusted; calibration; percentile; threshold index

### 3.4 Score Transformation

- [x] No transformation (raw per-subset metrics; macro-averaging within a subset)
- [x] Formula for combining item, task-family, or subscore results documented (per-subset macro-average)
- [ ] Linear/non-linear transformation; normalization against a reference; weighting across subdomains/domains; cross-domain aggregation
- [ ] Not applicable

Reviewer comments: There is no cross-subset aggregate, so no domain-weighting question arises.

### 3.5 Documented Reference Groups, Baselines, and Comparators

- [x] Expected performance from random guessing or trivial selection (per-subset naive baselines)
- [x] Performance from a reference model used to interpret scores (GPT-4o-AllRules is the de facto best-performer anchor)
- [x] Previous model cohort (five models across multiple conditions)
- [x] Commercial system used as a documented comparison point (GPT-4o, GPT-4, Gemini-1.0, Claude-Opus)
- [x] Open-weight model used as a documented comparison point (LLaVA-1.5)
- [x] Tool-enabled versus no-tool comparator (AllRules vs RAG vs GuaranteedRAG context-delivery contrast)
- [ ] Human participant performance; Qualified domain experts; Contest human population; Professional annotator; Domain-specific reference group; Public/private split comparator; Suite component comparator

| Reference point or documented comparison group | Construction method | Intended score interpretation |
| :--------------------------------------------- | :------------------ | :---------------------------- |
| Random/trivial baseline | Retrieval: random rule from the 1,192; Compilation: 10 random rules; Definition: two consecutive random words; Presence/Dimension/Functional Performance: 50/50 yes/no | Lower threshold / chance floor per subset |
| Reported model cohort | GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, LLaVA-1.5, in AllRules and/or RAG conditions | Relative model and condition comparison; GPT-4o-AllRules best across nearly all subsets |
| Context-delivery contrast | AllRules vs simple RAG vs GuaranteedRAG | Isolates inherent model skill from context-delivery efficacy |
| Human reference | None for yes/no or retrieval scoring; only single human-written **explanations** for Compliance similarity metrics | No human accuracy baseline; no expert-parity claim |

Reviewer comments: There is no human or expert **performance** baseline against which model accuracy is interpreted; the only human artifacts are single reference explanations used by the similarity metrics.

### 3.6 Score Uncertainty and Stability

- [x] Multiple runs or seeds - only for LLaVA-1.5 GuaranteedRAG (5 runs, mean ± std dev; e.g., Retrieval 0.699 ± 0.00590)
- [ ] Reported ranges around scores; Standard errors; Bootstrap intervals; Per-subscore confidence intervals; Small-sample sensitivity; Statistics on judge consistency; Rubric-application consistency; Sensitivity analyses; Prompt-perturbation sensitivity; IRT
- [x] Not reported (for the main model cohort)

Reviewer comments: The principal model cohort (GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, LLaVA-1.5 under AllRules/RAG) is reported as point estimates with **no** confidence intervals, standard errors, or repeat-run variance. Only the LLaVA-1.5 GuaranteedRAG diagnostic carries a 5-run standard deviation. Given subset sizes of 16, 30, and 31, this is a consequential gap for Part B Section 9.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

| Prompt | Response |
| :----- | :------- |
| Why the primary rule was chosen | F1 BoW/BoC and Accuracy chosen for automatic, reproducible scoring (BoW follows SQuAD-style verbatim QA; BoC tolerates minor spelling/ending differences in component names); BLEU/ROUGE/Similarity follow ScienceQA for explanation scoring |
| Whether lower/upper limits are documented | Yes - all metrics in [0,1], 1.0 is perfect |
| Whether documentation identifies possible non-target rewarded behavior | Yes - authors flag format-following penalties, child-rule false negatives, and BLEU/ROUGE length sensitivity (shorter explanations score higher) |
| Whether parser/judge/scorer validation is documented | Partially - Figure 3 shows worked scoring examples; no formal scorer-validation study |
| Whether response-format burden is separated from target capability | Acknowledged but not separated - format errors are scored as failures (authors call this an artificial penalty) |
| Whether score changes from small item/prompt changes affect interpretation | Acknowledged as a generalizability limitation; not empirically quantified |
| Whether score uncertainty affects interpretation | Only addressed for LLaVA-1.5 GuaranteedRAG; otherwise not |
| Whether score differences are interpreted statistically | No - differences are discussed qualitatively (e.g., "smallest difference from naive baseline") with no significance tests |
| Whether interpretations are linked to capability domains from 2.1 | Yes - each subset maps to a described engineering skill |
| Whether aggregate interpretations preserve domain caveats | n/a (no aggregate) |
| Whether reports state what users should not infer | Yes - explicit single-document and generalizability limitations |

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [x] Public leaderboard available (`design-qa.github.io`, manually maintained)
- [x] Public aggregate scores available (paper Tables 2-5)
- [x] Public per-item scores available (the harness writes per-question scores to `results.txt`)
- [x] Public model responses, traces, logs, judge rationales, or per-item data available (dataset and metric code are public; full per-item model outputs from the paper's runs are not centrally published as a release)
- [ ] Public capability-domain profiles; Leaderboard snapshot/export; Submission metadata catalog; Confidence intervals/error bars; Raw submissions under controlled access; Retired-item releases; Private submitter reports
- [ ] No formal report or leaderboard documented

### 4.2 Output Name or Description

| Output | Description | Public/private | Maintainer / host |
| :----- | :---------- | :------------- | :---------------- |
| Paper Tables 2-5 (arXiv v2) | Per-subset model/baseline scores; GuaranteedRAG; component-mention-type breakdown; dimensioning-system effect | Public | Authors |
| `results.txt` (from harness) | Overall score plus per-question diagnostic scores for a submitted run | Local / submitter-generated | Evaluator |
| DesignQA leaderboard (`design-qa.github.io`) | Community-submitted model scores | Public | Maintainers (issue-mediated, manually verified) |

### 4.3 Output Design or Presentation

- [x] Static text report (paper)
- [x] Tables
- [x] Leaderboard
- [x] Downloadable CSV or JSON (dataset CSVs; `results.txt`)
- [ ] Graphs/visualizations as a primary output surface; Interactive dashboard; API output; Paper-only results

### 4.4 Output Structure

- [x] Task-family based (per-subset scores)
- [x] Error-analysis based (qualitative failure-mode analysis per subset)
- [x] Rank based (best-performer comparisons)
- [ ] Aggregate-score based; Capability-domain profile based; Criterion-threshold; Pairwise; Cost-adjusted; Trace-based; Suite-aggregate; Split/cohort; Version-window; Environment-episode; Difficulty-band

### 4.5 Sensitivity to Context

- [x] One output format for all contexts

List available contexts: Per-subset metric tables in the paper; a single leaderboard surface.

### 4.6 Development of Outputs

- [x] Based on benchmark authors' design
- [x] Based on human annotation (manual QA authoring/review; human reference explanations)
- [ ] Empirical/actuarial; Expert judgment as a scoring panel; Model-scored; Platform-generated

### 4.7 Modifiability

- [x] Limited modification by submitter or user (users run the harness to produce their own `results.txt`)
- [ ] Not modifiable; Fully user-generated; Not documented

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

- [x] Clear linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels
- [ ] Partial; Not obvious; Mixture; Not documented

Reviewer comments: Each subset's task, metric, and engineering-skill interpretation are clearly linked in the paper.

### 4.9 Output Content

- [x] Aggregate rankings (best-performer per subset)
- [x] Subdomain comparisons (per-subset)
- [x] Error categories (qualitative failure analysis)
- [x] Examples of successes or failures (Figure 3)
- [x] Warnings or caveats (Limitations section)
- [x] Recommendations or interpretation notes (future-work suggestions)
- [ ] Capability-domain profiles; Coverage map; Excluded-domain caveats panel; Aggregate-score warnings; Cost/latency data; Process traces

### 4.10 Intended Recipients

- [x] AI researchers
- [x] Model developers
- [x] Benchmark maintainers
- [ ] Safety evaluators; Policy actors; Product/deployment teams; Procurement; Public audience

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

- [x] Technical report (arXiv paper)
- [x] Repository README
- [x] Scoring documentation (README + metric code)
- [x] Evaluation examples (Figure 3; worked scoring examples)
- [ ] User guide; API documentation; Dataset card; Model submission instructions (beyond "file a GitHub issue"); Rubric/annotation guide; FAQ/forum; Changelog/release notes

### 5.2 Distribution and Access Model

- [x] Fully public materials
- [x] Leaderboard-only submission route (issue-mediated)
- [ ] Public with restricted answer keys; Controlled-access host; Private/held-out service; Hosted scoring service; Registry distribution; Competition distribution; Private maintainer-mediated distribution; Retired/archived materials; Access model not documented

Reviewer comments: All items, answers, and the source rule text are fully public. There is no hidden test split.

### 5.3 Methods of Publication

- [x] Academic paper
- [x] Benchmark website (`design-qa.github.io`)
- [x] Git repository
- [x] Downloadable documents (dataset CSVs and images)
- [ ] Package registry; Dataset hosting platform; Leaderboard platform (third-party); Hosted evaluation service; Benchmark registry; Contest organizer source; Controlled-access host; Private distribution

### 5.4 User Requirements or Qualifications

| Requirement type | Requirement |
| :--------------- | :---------- |
| Technical skill | Python/CLI; ability to call multimodal model APIs or run LLaVA locally |
| Model access | Provider API keys (closed models) or local weights (LLaVA-1.5) |
| Dataset access | Public download from the repository |
| Compute or budget | API/embedding cost; AllRules ~10x RAG cost (not quantified in dollars) |
| Tool/API credentials | OpenAI embeddings for RAG; provider credentials for models |
| Hosted submission account | GitHub account to file a leaderboard issue |
| Human expertise | Engineering-domain familiarity helpful for interpreting results; not required to run |
| Account/license/eligibility | No stated license or eligibility terms (license absent) |
| Ethical/safety/data-use obligations | None documented |

### 5.5 Dataset and Item Access

| Component | Public | Restricted | Hidden | Not available |
| :-------- | :----: | :--------: | :----: | :-----------: |
| Training or development items | | | | [x] (none defined) |
| Public evaluation items | [x] | | | |
| Private or held-out evaluation items | | | | [x] (none) |
| Secret/encrypted reserve items | | | | [x] |
| Private leaderboard set | | | | [x] |
| Retired or archived items | | | | [x] |
| Answer keys or reference solutions | [x] | | | |
| Metadata or annotations | [x] | | | |
| Human annotations / verification labels | [x] | | | |
| Raw model outputs or logs | | | | [x] (paper-run outputs not released as a dataset) |
| Model submissions and traces | | [x] | | (submitted via issue, not centrally archived) |
| Hosted scoring service | | | | [x] |
| Simulator or environment state | | | | [x] |
| Task registry entry | | | | [x] |
| Tool/API credentials or config | | | | [x] |

### 5.6 Provenance and Contamination Documentation

| Topic | Documented | Partially documented | Not documented |
| :---- | :--------: | :------------------: | :------------: |
| Data origin or task creation | [x] | | |
| Source-material release date | [x] | | (FSAE 2024 rules) |
| Contest or problem-source timing | [x] | | |
| Persistent dataset identifier | | [x] | (arXiv ID; no dataset DOI) |
| Author or contributor qualifications | [x] | | |
| Deduplication or overlap checks | | | [x] |
| Rationale for public vs hidden items | | [x] | (all public by design) |
| Screening for prior model exposure | | | [x] |
| Canary strings or training-data warnings | | | [x] |
| Diagnostic task for prior-exposure-driven performance | | [x] | (component-mention-type analysis notes likely pre-training exposure to definition-component images) |
| Pre-exposure / searchability checks | | | [x] |
| Public-source searchability | | [x] | (FSAE rules are public on the web) |
| Post-release contamination risk | | [x] | (authors suggest fine-tuning on Retrieval QAs) |
| Training-use prohibition | | | [x] (none; fine-tuning is suggested) |
| Private-set owner | | | [x] (no private set) |
| Leak response policy | | | [x] |
| Rerun or replacement trigger | | | [x] |
| Hash commitments / tamper-evident logs | | | [x] |
| Encrypted/secret reserve | | | [x] |
| Rules for updating/rotating items | | | [x] |
| Reporting of known disclosures / deprecated items | | | [x] |

Reviewer comments: The dataset and the underlying FSAE rule text are fully public and web-searchable, and the authors explicitly recommend fine-tuning on the Retrieval QAs. There is no contamination control, no canary, and no held-out reserve. This is consistent with the benchmark's self-positioning as a diagnostic, but it is a live gameability/contamination consideration for Part B.

### 5.7 Reproducibility Materials

- [x] Complete task data
- [x] Complete prompt templates
- [x] Code or platform that administers tasks and runs scoring (`eval/full_evaluation.py`)
- [x] Scoring code (`eval/metrics/metrics.py`)
- [x] Model responses examples (Figure 3 worked examples)
- [ ] Environment file / dependency list (not confirmed present)
- [ ] Container / reproducible environment; Container image; Task registry; Simulator; Evaluation adapter; Judge model/prompt version; Version pinning; Random seeds/deterministic settings; Full per-item paper-run outputs as a release; Reproduction script for published results; Push-button replication; Expected-output fixtures; Scorer fixtures; Known-good baseline run; Task-level expected outputs; CI/test suite; Public build status

Reviewer comments: Data, prompts, and scorers are present and runnable, but there is no pinned environment, no seeds, no smoke-test fixtures, no CI, and no one-command reproduction of the paper's tables.

### 5.8 Maintenance and Versioning

| Topic | Response |
| :---- | :------- |
| Maintainer identity | Anna C. Doris (`anniedoris`) and co-authors; no named ongoing maintenance team |
| Private/held-out set owner | n/a (no private set) |
| Leaderboard operator | Maintainers, via GitHub issues + manual verification |
| Submission eligibility rules | "File a GitHub issue" with `.txt` results and code; no formal eligibility policy |
| Rerun policy | Not documented |
| Stale-score policy | Not documented |
| Model-version update policy | Not documented |
| Scorer/judge/parser/harness versioning | None (no tags/releases) |
| Cohort/evaluation-window labels | None |
| Public/private aggregation policy | n/a |
| Retirement/archival policy | Not documented |
| Documented release names/tags/changes | None (no GitHub Releases) |
| Changelog or update record | None located |
| Issue or feedback process | GitHub issues (13 open at access date) |
| Item correction process | Not formally documented (would proceed via issues) |
| Deprecated item handling | Not documented |
| Rules for updating hidden items | n/a |
| Last code-usability/harness health check | Unknown; last repository push 2025-08-10 |
| Build, CI, or smoke-test status | None |
| Score-ceiling/deprecation criteria | Not documented |
| End-of-life policy | Not documented |
| Retired-item publication/audit policy | Not documented |
| Score comparability across versions | n/a (single version) |
| Policy for comparing across dates/cohorts | Not documented |
| Long-term archival plan | arXiv (paper); GitHub (data/code); no DOI archive or mirror noted |

Reviewer comments: The repository remained active into 2025 (last push 2025-08-10) with an open issue queue and a manually maintained leaderboard, indicating non-trivial ongoing attention, but there is no formal versioning, changelog, release, or CI infrastructure.

---

## Appendix A. General Description of the Benchmark

DesignQA is a static, fully public multimodal QA benchmark that tests whether MLLMs can understand and apply engineering design requirements drawn from a real technical document. Built by MIT and Autodesk researchers around the 140-page Formula SAE 2024 rule document and CAD/test data from the MIT Motorsports team, it contains 1,451 question-answer pairs across three engineering-workflow segments (Rule Extraction, Rule Comprehension, Rule Compliance) and six subsets (Retrieval, Compilation, Definition, Presence, Dimension, Functional Performance). Its signature property is document-grounded, multi-source visual question-answering: the input image (a CAD view or engineering drawing) and the input document (the rules) come from different sources, and the images were not seen by models during pre-training. Every subset is scored automatically - F1 Bag-of-Words for verbatim Retrieval, F1 Rules for Compilation, F1 Bag-of-Characters for component Definition, accuracy for the yes/no Presence/Dimension/Functional Performance subsets, and BLEU-2/ROUGE-L/Sentence-BERT similarity for Rule-Compliance explanations - so that future models can be tested without human raters. The authors evaluate GPT-4o, GPT-4, Gemini-1.0, Claude-Opus, and LLaVA-1.5 under three context-delivery conditions (full rules in context, simple LlamaIndex RAG, and a keyword-matched GuaranteedRAG diagnostic) and find GPT-4o-AllRules best on nearly all subsets while documenting persistent gaps in rule retrieval, technical-component recognition, and engineering-drawing analysis. Materials (dataset, prompts, scorer) are distributed via GitHub with an issue-mediated, manually verified leaderboard; the benchmark makes no AGI or general-intelligence claim and explicitly notes its single-document scope.

---

# Part B. Evaluation of the Benchmark

Part B evaluates DesignQA against the meaning users are expected to draw from its scores: a fine-grained, per-subset diagnosis of whether an MLLM can extract, comprehend, and apply engineering requirements from one real rule document, under a stated context-delivery condition. Ratings are anchored to that modest, well-bounded interpretation. Interpretive criteria are disciplined with `literature/Measuring_what_Matters.md` (construct validity), `literature/betterbench.md` (lifecycle quality, reproducibility, contamination, usability, maintenance), and `literature/A_Definition_of_AGI.md` (CHC domain mapping). Each item carries evidence, missing evidence, reviewer rationale, and an interpretation caution where consequential.

## Information Sources

Information sources that might inform Part B include:

- Official benchmark papers, technical reports, model cards, dataset cards, websites, documentation hubs, repositories, leaderboards, scorecards, dashboards, and changelogs supplied or maintained by benchmark creators.
- Public benchmark materials such as task files, prompts, rubrics, reference answers, scorer code, harness code, examples, raw outputs, submission rules, issue trackers, release notes, and archived versions.
- Open information in academic literature, benchmark-quality literature, audit reports, replication studies, analyses of prior model exposure to benchmark items or answers, validation studies, and independent technical commentary. Use these sources to contextualize or challenge score interpretations, not to replace official facts.
- Maintainer-provided or access-controlled information that is not normally supplied to users. If such material affects a rating, state clearly in the Reviewer notes that the rating depends on non-public material inspected by the reviewer.
- Confidential or restricted technical information, such as hidden test splits, item provenance, audits for prior exposure to benchmark items or answers, scorer validation reports, calibration data for scoring by another model, or security details. If reviewed under access restrictions, describe only the rating implication and the access status, without disclosing restricted content.

## Explanation of Ratings

All rating items use the EFPA-style scale below unless a section states otherwise. Detailed "Excellent" anchors identify what a rating of `4` would require for that item. Lower ratings should be assigned by reviewer judgment, considering the benchmark's intended use, scope of score interpretation, decision stakes, technical complexity, evidence quality, and consequences of misinterpretation.

Where a `0` or `1` rating is assigned to an attribute that is critical for the benchmark's stated purpose, the review should caution that the benchmark is suitable only for limited exploratory, research, or expert-qualified use unless stronger evidence is supplied. Critical attributes will vary by benchmark: for example, controls for prior model exposure to benchmark items or answers may be critical for public knowledge benchmarks, scorer consistency may be critical for open-ended generation benchmarks, and reference points used to interpret scores may be critical for leaderboards used in procurement or policy.

Overall ratings must be based on reviewer judgment rather than mechanical averaging. A single severe gap may dominate the overall rating when it undermines the intended score meaning; conversely, a narrow gap may be less consequential when the benchmark's score interpretation is modest and clearly bounded.

### Rating Scale

| Rating | Meaning                                                                                |
| :----: | :------------------------------------------------------------------------------------- |
|  n/a   | This attribute is not applicable to this benchmark or its stated use.                  |
|   0    | Not possible to rate because no, or insufficient, information is provided.             |
|   1    | Inadequate for the benchmark's stated purpose or intended interpretation.              |
|   2    | Adequate: sufficient for cautious use, with limitations that should be stated.         |
|   3    | Good: clear, relevant, and mostly complete support, with no major interpretive threat. |
|   4    | Excellent: comprehensive, well-documented, and strongly aligned with the item anchor.  |

## General Guidance on Assigning Ratings

It is difficult to set universal thresholds for benchmark quality. The adequacy of evidence depends on what capability or quality the benchmark claims to measure, how scores are used, whether comparisons are high stakes, whether tasks are public or hidden, whether scoring is deterministic or judgment-based, and whether the benchmark is stable or regularly refreshed. Ratings should therefore be anchored in the intended score meaning, not in a generic expectation that every benchmark must supply every possible form of evidence.

For descriptive gaps, first ask what evidence would be needed to support the benchmark's actual score interpretation. A missing human reference point, for example, may be serious for a benchmark claiming expert-level performance but less central for a narrow regression test. A missing audit for prior model exposure may be serious for public web-derived knowledge tasks but less central for a private live-environment evaluation with documented release controls.

For broad interpretations made from benchmark scores about intelligence, AGI, reasoning, agency, autonomy, or cross-domain competence, require stronger breadth and validity evidence than for narrow capability interpretations.

Ratings should be based on the information available, with comments explaining consequential evidence, limitations, and rating rationale where needed.

## Section 6. Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition
- Rating: 3
- Evidence: The paper defines a clear, well-motivated construct - applying engineering requirements from technical documentation - and decomposes it into a defensible workflow (extract → comprehend → comply). The document-grounded multi-source VQA framing is explicitly distinguished from self-contained and single-source benchmarks (Table 1).
- Missing evidence: The construct is operationalized through a single rule document, so "engineering requirements understanding" is defined more by the task workflow than by an independent theory of the capability space.
- Reviewer rationale: Clear, bounded, and honestly scoped construct; the single-document operationalization holds it short of a 4.
- Interpretation caution: Read scores as evidence about FSAE-style requirement tasks, not about engineering-design competence in general.

#### 6.1.2 Summary of prior research and benchmark context
- Rating: 3
- Evidence: Section 2 situates DesignQA against reference-dependent text QA (SQuAD, WikiQA, QASPER, ZeroScrolls), VQA (MME, MMBench, MMMU, ScienceQA, InfoSeek), engineering-AI work, and the PURE requirements dataset, with a reference-type taxonomy that motivates the multi-source gap it fills.
- Missing evidence: Light engagement with benchmark-quality/measurement literature (contamination, uncertainty).
- Reviewer rationale: Strong domain and benchmark-landscape contextualization.

#### 6.1.3 Phenomenon-task-metric-claim chain
- Rating: 3
- Evidence: The chain from engineering workflow → six subsets → per-subset automatic metric → per-skill interpretation is explicit, and the authors themselves identify several confounds (format penalties, child-rule false negatives, BLEU/ROUGE length sensitivity).
- Missing evidence: The confounds are acknowledged but not measured or corrected; the metric-to-claim link is therefore partially compromised by construct-irrelevant variance the authors describe but do not quantify.
- Reviewer rationale: Coherent and unusually self-aware chain, with the weak link at the metric stage.
- Interpretation caution: Some score differences reflect formatting/verbosity behavior rather than the target engineering skill.

#### 6.1.4 Task or item design
- Rating: 3
- Evidence: Item designs are purpose-built: multi-view + close-up CAD images, two dimensioning systems (direct vs scale-bar), null images for text-only items, paired positive/negative compliance examples, and a context/detailed-context split for Dimension. Prompt templates are fixed and reported.
- Missing evidence: No scale-bar-violating compliance items were created (because the source CAD is rule-compliant), leaving an asymmetry in the Dimension design.
- Reviewer rationale: Thoughtful, engineering-grounded design with one documented coverage asymmetry.

#### 6.1.5 Procedures for developing task or item content
- Rating: 3
- Evidence: Retrieval/Compilation ground truths were generated programmatically (scripts + regex over the rule document); Comprehension/Compliance items were authored by MIT Motorsports members, an industry (Autodesk) author, and academic researchers, with cross-review by the two parties who did not write each item (except derivatives and compliance explanations).
- Missing evidence: Inter-annotator agreement statistics, the full review protocol, and explanation-review depth (explanations were "not extensively reviewed") are limited.
- Reviewer rationale: A credible, expertise-grounded manual process - a genuine strength relative to crowdsourced/synthetic benchmarks.

#### 6.1.6 Thoroughness of the final task or item selection process
- Rating: 2
- Evidence: Selection logic is documented (drop empty/non-design rules, keep children; 30 curated Compilation terms; 31-component list; 20 dimension rules).
- Missing evidence: The manual subsets are small convenience samples constrained by data availability (Functional Performance limited to 16 by test-data scarcity); no coverage analysis or pilot statistics.
- Reviewer rationale: Defensible but limited; small, availability-driven samples are acceptable for diagnosis only with explicit uncertainty caveats.
- Interpretation caution: The small subsets sample a narrow slice of possible requirement tasks.

#### 6.1.7 Quantitative evidence of task or item quality
- Rating: 2
- Evidence: Naive baselines per subset contextualize difficulty; the paper notes which subsets sit closest to chance (Compilation, Definition, Presence).
- Missing evidence: No item difficulty/discrimination parameters, no ceiling/floor analysis, no inter-item redundancy or IRT-style statistics.
- Reviewer rationale: Baseline contrasts are useful; per-item psychometric evidence is absent.

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice
- Rating: n/a
- Evidence: DesignQA is an original construction, not an adaptation or slice of a prior benchmark.

#### 6.1.9 Overall Rationale, development, and task or item quality
- Rating: 3
- Reviewer rationale: A clearly defined, honestly bounded construct; an expertise-driven, cross-reviewed manual authoring process; and purpose-built multimodal item designs support qualified diagnostic use. The residual gaps are small-sample thoroughness and absent per-item quality statistics, which constrain - but do not undermine - the rationale.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use — Rating: 3
- Evidence: Paper and README state the purpose, intended systems, and per-subset interpretation clearly.
- Missing evidence: No enumerated non-use list (e.g., procurement/deployment), though no broad claim invites one.

#### 6.2.2 Documentation of development process — Rating: 3
- Evidence: Sections 3.1.1-3.1.4 detail item construction, image generation, and review.
- Missing evidence: Annotator agreement and explanation-review protocol detail.

#### 6.2.3 Documentation of scoring and metrics — Rating: 3
- Evidence: Each metric is defined with formulas and worked examples (Figure 3); scorer code is public.
- Missing evidence: No formal treatment of malformed-output handling beyond "scored as-is."

#### 6.2.4 Documentation of reliability, stability, and uncertainty — Rating: 1
- Evidence: Only the LLaVA-1.5 GuaranteedRAG diagnostic reports run-to-run variance.
- Missing evidence: No confidence intervals, standard errors, or repeat-run variance for the main model cohort; no prompt-sensitivity study.
- Reviewer rationale: For subsets of 16-31 items reported as bare point estimates, the absence of uncertainty documentation is a serious interpretive gap.

#### 6.2.5 Documentation of validity evidence — Rating: 2
- Evidence: Content-validity argument via expert authoring and a real rulebook; qualitative error analyses support face validity.
- Missing evidence: No convergent/discriminant evidence, no human-performance baseline, no external-criterion link.

#### 6.2.6 Documentation of fair use and comparability — Rating: 2
- Evidence: Exact model IDs, sampling settings, and context-delivery conditions are documented, supporting condition-aware comparison.
- Missing evidence: Claude-Opus tested RAG-only and Gemini's RECITATION zero are noted but not normalized; no formal cross-condition comparability guidance.

#### 6.2.7 Documentation of maintenance and versioning — Rating: 2
- Evidence: Active repository and issue-mediated leaderboard.
- Missing evidence: No changelog, releases, version tags, or deprecation policy.

#### 6.2.8 Adequacy of documentation available to users — Rating: 2
- Reviewer rationale: Strong on purpose, development, and scoring; weak on uncertainty, validity breadth, and lifecycle. Sufficient for cautious research use, short of audit-grade.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration — Rating: 2
- Evidence: README documents the `full_evaluation.py` invocation and dataset paths; prompts and sampling settings are in the paper.
- Missing evidence: No dependency/environment file confirmed, no seeds, no smoke test; an evaluator must reconstruct the LlamaIndex wiring.

#### 6.3.2 Scoring procedure and error handling — Rating: 2
- Evidence: Scorer is public and deterministic; worked examples aid interpretation.
- Missing evidence: No documented handling of malformed outputs, refusals (cf. Gemini RECITATION), or format-recovery retries.

#### 6.3.3 Interpretation and reporting guidance — Rating: 3
- Evidence: The paper gives per-subset interpretation, qualitative failure modes, and an explicit Limitations section.
- Missing evidence: No statistical guidance on which score differences are meaningful.

#### 6.3.4 Restrictions, prerequisites, and appropriate use — Rating: 2
- Evidence: Multimodal input, context length, and RAG prerequisites are clear.
- Missing evidence: No license/terms; no formal appropriate-use statement.

#### 6.3.5 Technical support and implementation guidance — Rating: 2
- Evidence: GitHub issues serve as the support channel; the leaderboard submission path is described.
- Missing evidence: No troubleshooting page, no expected-output fixtures, no dependency versions.

#### 6.3.6 References and supporting materials — Rating: 3
- Evidence: Paper, repo, project page, and metric sources are cross-linked and well-cited.

#### 6.3.7 Quality of procedural instructions — Rating: 2
- Reviewer rationale: Runnable by a competent researcher, but reproduction depends on reconstructing un-pinned environment and harness details.

### 6.4 Overall Adequacy of Rationale and Documentation
- Rating: 3
- Reviewer comments: Section 6 is the benchmark's strongest area. The construct is clear and honestly bounded, the manual authoring process is expertise-driven and cross-reviewed, scoring is transparent, and the authors document their own confounds and limitations. The rating is held to 3 by thin uncertainty/validity documentation and the absence of versioning and pinned reproduction materials.

Reviewer comments: Revisited after Sections 8-12, the rationale remains sound; the documentation gaps that most affect downstream interpretation are uncertainty (6.2.4) and lifecycle (6.2.7).

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability — Rating: 3
- Evidence: The complete dataset (CSVs + CAD/drawing image folders) is public and organized by segment/subset; answer keys are included.
- Missing evidence: No license (raw `LICENSE` 404; API `license: null`), no dataset card, no version tag or DOI.
- Reviewer rationale: Highly available and well-organized, but the absent license and versioning limit auditable reuse.
- Interpretation caution: Without a license, redistribution/derivative terms are legally unstated, not permissive by assertion.

#### 7.1.2 Prompts, instructions, and input materials — Rating: 3
- Evidence: Fixed prompt templates per subset are reported in the paper and embedded in the data; image assets (multi-view, close-up, engineering drawings) are provided.
- Missing evidence: The exact in-repo prompt-construction code path is less fully documented than the templates themselves.

#### 7.1.3 Rubrics, reference answers, and response format requirements — Rating: 2
- Evidence: Ground-truth answers and (for Compliance) single human reference explanations are provided; format requirements (comma-separated lists; "Explanation:"/"Answer:") are explicit.
- Missing evidence: Only one reference explanation per compliance item; no admissible-variant handling; no retry/repair for format deviations, which the authors note artificially penalize models.
- Reviewer rationale: Adequate keys for the closed-form subsets; the single-reference, format-strict explanation scoring is a known weakness.

#### 7.1.4 Evaluation harness, scorer, and implementation quality — Rating: 2
- Evidence: `eval/full_evaluation.py` + `eval/metrics/metrics.py` produce `results.txt` with per-question diagnostics; runnable end-to-end.
- Missing evidence: No CI, no version pinning, no smoke-test fixtures, no known-good baseline run, no container; the model-invocation side relies on external LlamaIndex/provider state.
- Reviewer rationale: A real, usable scorer, but not hardened for reproducible audit.

#### 7.1.5 Interface and workflow usability — Rating: 3
- Evidence: A single CLI command scores a run; folder layout is intuitive; the leaderboard submission path is described.
- Missing evidence: No progress/failure signaling documentation.

#### 7.1.6 Accessibility across modalities, languages, and system types — Rating: 2
- Evidence: Works for any image-capable model via API or local weights; a RAG path supports small-context models.
- Missing evidence: English-only; no accessibility adaptations; small-context models are structurally disadvantaged without RAG.

#### 7.1.7 Licensing, use requirements, and risk warnings — Rating: 1
- Evidence: None - no LICENSE file is present.
- Missing evidence: Any license, terms of use, redistribution terms, or data-use statement.
- Reviewer rationale: For a benchmark intended for community reuse and submission, the complete absence of license terms is a material usability and compliance gap.
- Interpretation caution: Treat licensing as unresolved; the 404/`null` are recorded facts, not an inferred grant of rights.

#### 7.1.8 Overall quality of benchmark materials — Rating: 2
- Reviewer comments: Materials are complete, well-organized, and runnable, supporting cautious use; they fall short of audit-grade because of the missing license, absent versioning/CI, single-reference explanation keys, and lack of reproducibility fixtures.

Reviewer comments: The materials would move toward a 3-4 with a license, a dataset card/version tag, pinned dependencies, and smoke-test fixtures.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines — Rating: 3
- Evidence: Each subset has an explicit naive baseline (random rule; 10 random rules; two random words; 50/50 yes/no), empirically computed and reported alongside model scores; the paper uses these to flag near-chance subsets.
- Missing evidence: No empirical ceiling (e.g., human or oracle-context upper bound) for the accuracy subsets.
- Reviewer rationale: Floors are well-handled; the absence of a ceiling limits interpretation of "how much headroom remains."

#### 8.1.2 Human or expert baselines — Rating: 1
- Evidence: None for task performance. The only human artifacts are single reference explanations used by the similarity metrics.
- Missing evidence: A human/expert accuracy baseline on any subset.
- Reviewer rationale: Without a human baseline, scores can be compared across models but not interpreted against human competence on the same tasks - relevant because the framing invokes engineer-like work.
- Interpretation caution: Do not read subset accuracies as relative to human engineers; no such anchor exists.

#### 8.1.3 Model comparator cohort — Rating: 3
- Evidence: Five models with exact version IDs, documented sampling settings, and explicit context-delivery conditions; GPT-4o-AllRules functions as the best-performer anchor; the AllRules/RAG/GuaranteedRAG contrast is informative.
- Missing evidence: No uncertainty on any cohort score; Claude-Opus AllRules omitted (cost); Gemini Retrieval zero is an artifact not a capability estimate.
- Reviewer rationale: A well-specified cohort that supports large-gap comparisons; gaps in coverage and uncertainty prevent a 4.

#### 8.1.4 Historical, version, or benchmark-family comparators — Rating: n/a
- Evidence: Single version, no prior DesignQA release; cross-benchmark comparisons in Section 2 are descriptive, not score-linked.

#### 8.1.5 Criterion thresholds, score bands, or performance categories — Rating: n/a
- Evidence: No pass/fail thresholds or qualitative bands are defined.

#### 8.1.6 Representativeness of reference groups — Rating: 2
- Evidence: The model cohort represents the strong contemporary (April-August 2024) closed/open MLLMs; baselines are subset-appropriate.
- Missing evidence: No human reference group; the model cohort is a small convenience set.
- Reviewer rationale: Representative of 2024 frontier MLLMs but not of human performance.

#### 8.1.7 Currency and maintenance of baseline evidence — Rating: 2
- Evidence: The cohort was current at writing; the leaderboard mechanism allows new models to be added.
- Missing evidence: No documented refresh cadence; the paper's cohort is now dated, and no rule exists for retiring stale comparisons.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation
- Rating: 2
- Reviewer comments: Chance floors and a well-specified model cohort support cautious within-benchmark, large-gap comparisons. The decisive limitations are the absence of any human/expert performance baseline and the lack of score uncertainty, which together mean scores can be ordered but not anchored to human competence or treated as stable fine-grained rankings.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence — Rating: 1
- Evidence: Reliability evidence exists only for one model under one condition: LLaVA-1.5 GuaranteedRAG, reported as mean ± std dev over 5 runs (e.g., Retrieval 0.699 ± 0.00590).
- Missing evidence: No repeat-run, seed, prompt-sensitivity, scorer-robustness, or split-equivalence evidence for the main cohort; no confidence intervals on any headline score.
- Reviewer rationale: Coverage is minimal relative to the stochastic, small-subset design.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings — Rating: 1
- Evidence: Sampling settings are documented (temperatures 0.1/0.75); GuaranteedRAG repeats give one stability snapshot.
- Missing evidence: No seeds; no multi-run evidence for the AllRules/RAG cohort despite non-zero temperatures, so single-run point estimates carry unquantified decoding variance.
- Reviewer rationale: Settings are reproducible in principle but stability is essentially unmeasured for the reported numbers.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors — Rating: 1
- Evidence: Standard deviation reported only for LLaVA-1.5 GuaranteedRAG.
- Missing evidence: No CIs/SEs anywhere else. On 16-, 30-, and 31-item subsets, a single item shifts accuracy by 6.25, 3.3, and 3.2 percentage points respectively.
- Reviewer rationale: This is the binding constraint of the review: small subsets plus point estimates make most fine-grained rankings statistically indistinguishable.
- Interpretation caution: Only large score gaps are interpretable; small-margin orderings on Functional Performance, Compilation, and Definition should not be treated as real differences.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability — Rating: 2
- Evidence: Scorers are deterministic and public; Figure 3 documents how representative outputs map to scores.
- Missing evidence: No quantified parser error rate on malformed/edge-case outputs; format-strict parsing visibly penalizes valid-but-misformatted answers (Claude-Opus Compilation).
- Reviewer rationale: Deterministic and inspectable, but construct-irrelevant parser strictness is unquantified.

#### 9.3.2 Human rater or expert scorer agreement — Rating: n/a
- Evidence: Scoring is fully automatic; human input is limited to authoring reference explanations, not scoring runs.

#### 9.3.3 Model-as-judge reliability and validity checks — Rating: n/a
- Evidence: No model-as-judge is used.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity — Rating: 1
- Evidence: The authors acknowledge results "may not generalize to similar questions where the prompts or images are tweaked."
- Missing evidence: No empirical prompt-perturbation or image-format sensitivity study.
- Reviewer rationale: A self-identified sensitivity that is left unmeasured.

#### 9.4.2 Form, split, version, or refresh equivalence — Rating: n/a
- Evidence: Single static form; no alternate forms or refresh.

#### 9.4.3 Execution environment and dependency stability — Rating: 1
- Evidence: Models invoked via LlamaIndex defaults; embedding via `text-embedding-3-large`.
- Missing evidence: Hosted-API and embedding endpoints drift over time; no version pinning, container, or environment file insulates reported scores from this drift.
- Reviewer rationale: Reported scores depend on external services whose stability is uncontrolled and undocumented.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences — Rating: 1
- Evidence: The paper interprets differences qualitatively (e.g., which subsets sit near the naive baseline).
- Missing evidence: No significance tests, no uncertainty bands, no guidance on which deltas are meaningful.
- Reviewer rationale: Differences are presented without the statistical apparatus needed to license rankings, especially on tiny subsets.

### 9.6 Overall Reliability, Precision, and Score Stability
- Rating: 1
- Reviewer comments: This is the benchmark's weakest dimension and the binding constraint on the overall assessment. The main model cohort is reported as single-run point estimates with no confidence intervals on subsets as small as 16, 30, and 31 items; only LLaVA-1.5 GuaranteedRAG carries a standard deviation. Combined with self-acknowledged prompt sensitivity and uncontrolled API/embedding drift, this means DesignQA reliably supports only coarse, large-gap conclusions. The benchmark remains useful as a diagnostic, but any small-margin ranking or leaderboard ordering by narrow differences should be treated as noise.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness — Rating: 3
- Evidence: Items derive from a real rulebook and real CAD/test data; subsets map to genuine engineering activities; expert authoring and cross-review support content validity. The authors argue the enumerated-rule structure generalizes to other standards (F1 regulations, NASA memoranda).
- Missing evidence: A single rulebook and small manual subsets limit representativeness of the broader requirements-engineering space; no coverage analysis.
- Reviewer rationale: Strong face/content validity for FSAE-style tasks; representativeness beyond that is argued, not demonstrated.
- Interpretation caution: Discipline the implicit "real-world engineering design" reading per `Measuring_what_Matters.md`; content supports FSAE-requirement tasks specifically.

#### 10.1.2 Construct breadth and capability-domain coverage — Rating: 2
- Evidence: The benchmark deliberately spans a multi-skill composite (visual recognition, long-text extraction, dimensional reasoning, technical knowledge), and the per-subset structure exposes that breadth.
- Missing evidence: The composite is sampled from one document; coverage across documents, domains, and requirement types is not established.
- Reviewer rationale: Reasonable within-document breadth; cross-domain breadth is unproven and not claimed.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality — Rating: 2
- Evidence: The three-segment/six-subset structure is conceptually motivated by the engineering workflow; Tables 4-5 provide internal analyses (component-mention type; dimensioning system).
- Missing evidence: No empirical analysis (e.g., correlation among subsets) confirming the subsets measure distinct skills; no aggregate to validate.
- Reviewer rationale: Conceptually coherent structure with limited empirical confirmation.

#### 10.2.2 Item or task behavior across the score scale — Rating: 2
- Evidence: Naive-baseline contrasts show some subsets sit near chance (Compilation, Definition, Presence), indicating difficulty spread; the component-mention-type analysis links score patterns to plausible exposure effects.
- Missing evidence: No per-item difficulty/discrimination; the near-chance subsets may reflect floor effects plus metric artifacts rather than pure capability.
- Reviewer rationale: Some informative behavior, confounded by metric and small-sample effects.

#### 10.2.3 Failure modes and error analysis — Rating: 3
- Evidence: The paper provides detailed, subset-specific qualitative error analyses (nearby-rule retrieval, missed verbatim/child rules in Compilation, steering-component misidentification, scale-bar arithmetic failures, single-row chart comparison) and Figure 3 examples.
- Missing evidence: Error categories are not quantified into frequencies.
- Reviewer rationale: Unusually thorough qualitative error analysis is a genuine validity strength.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity — Rating: 2
- Evidence: Metrics are borrowed from established QA/VQA/explanation literature (SQuAD-style F1, ScienceQA's BLEU/ROUGE/Similarity) and justified per subset; BoC is specifically motivated to tolerate minor spelling errors.
- Missing evidence: The metrics are not validated against human correctness judgments on DesignQA outputs; single-reference BLEU/ROUGE is acknowledged to reward brevity over correctness.
- Reviewer rationale: Reasonable metric choices whose validity for *this* content is asserted by analogy, not demonstrated.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance — Rating: 1
- Evidence: The authors candidly document multiple construct-irrelevant effects: format-following penalties (Compilation commas), child-rule false negatives (Retrieval), BLEU/ROUGE length sensitivity (Gemini's short explanations score higher), and the Gemini RECITATION zero.
- Missing evidence: None of these are corrected, quantified, or ablated; format compliance and verbosity demonstrably move scores independently of the target skill.
- Reviewer rationale: The threat is well-characterized but unmitigated, so a meaningful share of score variance is construct-irrelevant.
- Interpretation caution: Treat cross-model score differences partly as differences in format/verbosity behavior, not solely engineering skill.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings — Rating: 1
- Evidence: The paper notes the models' strong standing on MMMU as cohort-selection rationale.
- Missing evidence: No empirical correlation between DesignQA scores and any other benchmark, human performance, or real engineering outcome.
- Reviewer rationale: Essentially no relational validity evidence.

#### 10.4.2 Convergent and discriminant evidence — Rating: 1
- Evidence: None.
- Missing evidence: No evidence that DesignQA subsets converge with related measures or discriminate from unrelated ones.

#### 10.4.3 Ecological or predictive relevance — Rating: 2
- Evidence: The use of a real rulebook and real CAD data gives strong ecological *motivation*; the authors explicitly caveat single-document generalization.
- Missing evidence: No demonstration that DesignQA performance predicts performance on other requirement documents or real engineering tasks.
- Reviewer rationale: Ecologically motivated by construction, but predictive relevance is asserted and bounded, not shown.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls — Rating: 1
- Evidence: The dataset and the FSAE rule text are fully public and web-searchable; the component-mention-type analysis itself suggests definition-component images may have been seen in pre-training.
- Missing evidence: No canary, no held-out reserve, no contamination audit, no training-use prohibition.
- Reviewer rationale: A fully public test set with a public source document and no controls is highly exposed to contamination.
- Interpretation caution: Strong scores on a publicly available rulebook may partly reflect prior exposure rather than reasoning.

#### 10.5.2 Gameability and benchmark-specific tuning controls — Rating: 1
- Evidence: The authors themselves recommend fine-tuning on the Retrieval QAs to improve scores - i.e., optimizing directly against the public test items.
- Missing evidence: No train/test separation, no anti-overfitting safeguard, no leaderboard policy distinguishing fine-tuned-on-test submissions.
- Reviewer rationale: The benchmark is structurally gameable, and the recommended improvement path is to optimize against the test set.
- Interpretation caution: A high Retrieval score may indicate memorization of the public QAs rather than general retrieval skill.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims — Rating: 3
- Evidence: The authors make modest, well-bounded claims, explicitly limit scope to a single document, and frame DesignQA as a "first step" and a diagnostic. No human-parity or broad-capability claim is asserted from scores.
- Missing evidence: The "real-world engineering design" framing slightly outruns the single-document evidence base.
- Reviewer rationale: Claims are unusually well-proportioned for the field; the only stretch is the implicit generalization, which the Limitations section largely disciplines.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims — Rating: n/a
- Evidence: DesignQA makes no AGI, general-intelligence, agency, or autonomy claim. There is no broad claim to evaluate.

### 10.7 Overall Validity Support
- Rating: 2
- Reviewer comments: DesignQA has strong content validity, an exemplary qualitative error analysis, and unusually well-proportioned claims. These are offset by largely unmitigated construct-irrelevant variance (format/verbosity effects), no relational/convergent validity, no human baseline, and serious contamination/gameability exposure (a public test set the authors suggest fine-tuning on). Within its narrow, explicitly bounded interpretation the evidence supports cautious diagnostic use; it does not support strong claims that scores measure general engineering-requirement competence.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts — Rating: 2
- Evidence: The construct is relevant to any image-capable model; the RAG path extends participation to small-context models.
- Missing evidence: No discussion of how comparability holds across model families with very different multimodal interfaces.

#### 11.1.2 Documentation of fair-use considerations — Rating: 1
- Evidence: Minimal; the context-delivery conditions are documented but not framed as fairness.
- Missing evidence: No fairness, accessibility, or bias-consideration section.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design — Rating: 2
- Evidence: A single multimodal interface with null images for text-only items keeps the protocol uniform; RAG accommodates small windows.
- Missing evidence: No accessibility adaptations; English-only.

#### 11.2.2 Domain, language, modality, and subgroup coverage — Rating: 1
- Evidence: One domain (FSAE), one language (English), one document.
- Reviewer rationale: A 1 reflects intrinsic narrow coverage by design, not a defect of execution; relevant because it bounds comparability claims.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability — Rating: 2
- Evidence: Exact model IDs and identical prompts support comparison; the AllRules vs RAG distinction is explicit.
- Missing evidence: Models were not all tested under the same conditions - Claude-Opus is RAG-only (cost), AllRules vs RAG cohorts are not directly comparable, and Gemini's RECITATION zero is an interface artifact, not a capability measure.
- Reviewer rationale: Within-condition comparisons are fair; cross-condition comparisons require care the materials only partly support.
- Interpretation caution: Do not compare an AllRules score directly against a RAG score as if condition were held constant.

#### 11.3.2 Access, compute, tooling, and API or local comparability — Rating: 2
- Evidence: The cost asymmetry (AllRules >10x RAG) is disclosed and explains the Claude-Opus omission.
- Missing evidence: No standardized compute/cost accounting; the small-context models are inherently disadvantaged on a long-document task.

#### 11.3.3 Temporal comparability for rolling or live benchmarks — Rating: 2
- Evidence: The static item set is stable over time; the leaderboard can add new models.
- Missing evidence: Hosted-API drift means a model re-run later may score differently; no policy addresses temporal comparability or stale entries.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis — Rating: 2
- Evidence: Tables 4-5 analyze differential behavior by component-mention type and dimensioning system, surfacing a plausible pre-training-exposure advantage for definition components.
- Missing evidence: No analysis of systematic disadvantage to particular model classes beyond the context-window split.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts — Rating: 1
- Evidence: Limited; no per-condition uncertainty.
- Missing evidence: No subgroup reliability/validity evidence.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases — Rating: 2
- Evidence: The Limitations section bounds generalization and flags metric weaknesses.
- Missing evidence: No explicit non-use list (procurement, deployment gating, safety); no license/terms.

#### 11.5.2 Release rules and sensitive-content handling — Rating: 2
- Evidence: No sensitive content (engineering rules/CAD); fully open release.
- Missing evidence: No license/release rules; fine-tuning on test items is encouraged without restriction.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use
- Rating: 2
- Reviewer comments: Uniform prompts and exact model IDs support fair within-condition comparison, and the differential analyses (mention type, dimensioning) are a thoughtful fairness contribution. Comparability is undercut by unmatched conditions across the cohort (RAG-only Claude-Opus, AllRules-vs-RAG, the Gemini artifact), the absence of per-condition uncertainty, and the lack of license and formal appropriate-use boundaries. Adequate for cautious research comparison; not for cross-condition or decision-grade comparison.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope — Rating: 3
- Evidence: Paper Tables 2-5 cover per-subset scores, the GuaranteedRAG diagnostic, and two internal analyses; the leaderboard extends reporting to community models.
- Missing evidence: No uncertainty columns; the live leaderboard table contents/governance could not be rendered at access time.

#### 12.1.2 Score granularity and level of detail — Rating: 2
- Evidence: Per-subset granularity is appropriate for diagnosis and avoids a misleading single aggregate.
- Missing evidence: Reported precision (3 decimal places) on 16-31-item subsets implies precision the sample sizes cannot support without intervals.
- Interpretation caution: Treat third-decimal differences on small subsets as non-meaningful.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling — Rating: 2
- Evidence: Model versions, sampling settings, and context-delivery conditions are clearly labeled in the paper.
- Missing evidence: No uncertainty/error bars; the leaderboard surface's condition labeling could not be confirmed live.

#### 12.2.2 Reproducibility and traceability of reported scores — Rating: 2
- Evidence: Public data + scorer make the scoring side traceable; `results.txt` ties scores to per-question outputs for a given run.
- Missing evidence: No pinned environment/seeds/harness version; hosted-API model side is not reproducible to the paper's exact numbers; no published per-item paper-run outputs.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims — Rating: 3
- Evidence: The paper consistently links each score to a specific engineering skill and to qualitative failure modes, and foregrounds limitations; public claims stay close to the evidence.
- Missing evidence: No statement of which differences are meaningful; the leaderboard surface may present scores without the paper's caveats.

#### 12.3.2 Raw outputs, per-item data, or trace availability — Rating: 2
- Evidence: The harness produces per-question diagnostics locally; the dataset and scorers are public.
- Missing evidence: The authors' own per-item model outputs are not released as an auditable artifact; leaderboard submissions are not centrally archived for audit.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports — Rating: 3
- Evidence: Reporting is even-handed across providers; the paper repeatedly attributes low scores to task difficulty/metric artifacts rather than over-claiming model deficiency, and flags its own metric biases.

#### 12.4.2 Acceptability and usability for intended audiences — Rating: 3
- Evidence: Tables, worked scoring examples, and clear per-subset narratives suit the research audience well.

#### 12.4.3 Public communication and leaderboard governance — Rating: 1
- Evidence: A leaderboard exists with an issue-mediated, manually verified submission path.
- Missing evidence: No documented eligibility rules, no uncertainty on entries, no policy on fine-tuned-on-test submissions, no update cadence/deprecation rules; the live leaderboard table and governance text could not be rendered (unresolved).
- Reviewer rationale: Manual verification is a reasonable lightweight control, but governance is undocumented and the public surface is opaque at access time.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims
- Rating: 2
- Reviewer comments: The paper's reporting is clear, granular, even-handed, and admirably caveated - a strength. What holds the section to a 2 is the reporting layer's lack of uncertainty, the implied over-precision on tiny subsets, the un-reproducible hosted-model numbers, and an under-governed, currently opaque leaderboard surface.

---

## Final Evaluation

### Evaluative Report of the Benchmark

DesignQA is, for its intended purpose, a thoughtfully constructed and unusually honest diagnostic benchmark. Its strengths are concentrated in design and documentation. The construct - applying engineering requirements from technical documentation - is clearly defined and decomposed into a credible extract/comprehend/comply workflow; the items are built from a real 140-page FSAE rulebook and real MIT Motorsports CAD/test data; the manual subsets were authored by domain experts (motorsports, industry, academia) and cross-reviewed; and the document-grounded **multi-source** VQA design (image and document from different sources, image unseen in pre-training) is a genuine and well-argued contribution relative to self-contained and single-source VQA benchmarks. The paper's qualitative error analysis is among the more detailed in the field, and the authors are candid about their own metric confounds and about the single-document limitation. The benchmark makes **no** AGI or general-intelligence claim, and its public language stays close to its evidence - a notable point of discipline.

The benchmark's limitations as a measurement instrument cluster in four areas. First and most consequentially, reliability and precision are essentially unestablished for the headline numbers: the main model cohort is reported as single-run point estimates with no confidence intervals, on subsets as small as 16 (Functional Performance), 30 (Compilation), and 31 (Definition) items, where one item moves accuracy by 3-6 percentage points. Only the LLaVA-1.5 GuaranteedRAG diagnostic carries a standard deviation. Consequently only large score gaps are interpretable; small-margin rankings are not. This drives the Section 9 rating to 1 and binds the overall assessment. Second, the benchmark is highly exposed to contamination and gameability: the dataset and the source rule text are fully public and web-searchable, there are no held-out items or canaries, and the authors themselves recommend fine-tuning on the Retrieval QAs - i.e., optimizing against the public test set. Third, the automatic metrics carry unmitigated construct-irrelevant variance: format-following penalties (Compilation comma formatting), child-rule false negatives (Retrieval), BLEU/ROUGE length sensitivity, and single-reference explanation scoring mean that scores partly reward formatting and verbosity rather than the target skill; the Gemini RECITATION zero and the cost-driven RAG-only testing of Claude-Opus further complicate cross-model reading. Fourth, lifecycle and reuse infrastructure is thin: there is no license (confirmed live: raw `LICENSE` returns HTTP 404 and the GitHub API reports `license: null`), no dataset card, no versioning, changelog, releases, or CI, and an issue-mediated leaderboard whose live contents and governance could not be rendered at access time. There is also no human or expert performance baseline and no convergent/external validity evidence, so scores can be compared across models but not anchored to human competence or to other measures.

These gaps are evidence gaps appropriate to a first-step research diagnostic, not defects that void the benchmark. DesignQA is well-suited to qualitative and coarse-quantitative diagnosis of MLLM weaknesses on engineering-documentation tasks and to motivating model and RAG improvements. It is not suited, on current evidence, to fine-grained leaderboard ranking by small margins, to procurement or deployment decisions, or to claims that scores measure general engineering-requirement competence. The implicit generalization from one FSAE rulebook to "real-world engineering design" should be read narrowly; disciplined against `Measuring_what_Matters.md` and the authors' own single-document caveat, the supported interpretation is task-level and document-specific.

### Conclusions

DesignQA is a well-designed, honestly scoped, and unusually transparent diagnostic benchmark for MLLM understanding of engineering requirement documentation, appropriate for cautious research diagnosis and capability profiling but not for decision-grade ranking, procurement, or broad-competence claims; its decisive limitation is the absence of score uncertainty on very small subsets, compounded by a fully public, fine-tunable test set. Using it responsibly requires an evaluator who can reconstruct the LlamaIndex/RAG harness, supply provider credentials, hold context-delivery conditions constant, and interpret only large score gaps - a level of measurement and engineering literacy that exceeds what the repository's lightweight instructions assume, and that the authors' own framing as a "first step" implicitly acknowledges.

### Recommendations

1. **Maintainers (original benchmark):** add a license and a dataset card; publish confidence intervals (binomial for the accuracy subsets, bootstrap for F1/similarity) and at least a small multi-run/seed study for the main cohort; this single change would most raise Section 9.
2. **Maintainers (validity):** collect additional human reference explanations (to stabilize BLEU/ROUGE/Similarity) and a small human/expert accuracy baseline on at least the smallest subsets; relax or report format-strict parsing so format compliance is separated from the target skill.
3. **Maintainers (contamination/gameability):** create a held-out evaluation split or a refresh mechanism, and replace the "fine-tune on Retrieval QAs" recommendation with a train/test-respecting protocol; add a leaderboard policy distinguishing fine-tuned-on-test submissions.
4. **Maintainers (lifecycle/reproducibility):** add version tags/releases, a changelog, a pinned environment and seeds, smoke-test fixtures, and a documented leaderboard governance page; surface uncertainty and condition labels on the leaderboard.
5. **Benchmark users:** report DesignQA results with the exact context-delivery condition, model version, and at minimum a per-subset confidence interval; avoid comparing AllRules and RAG scores as if condition were constant; do not treat small-margin differences as real.
6. **Future reviewers:** revisit Sections 9 and 10.3-10.5 if the maintainers publish uncertainty estimates, a held-out split, and metric-validation data; re-check the live leaderboard surface and license status, which were unresolved/absent at this review's access date.

### Summary of Ratings

| Section                                                      | Overall Rating (`n/a`, `0`-`4`) |
| :----------------------------------------------------------- | :-----------------------------: |
| Section 6. Rationale, documentation, and task/item quality   |               3                 |
| Section 7. Benchmark materials and usability                 |               2                 |
| Section 8. Reference points and documented comparison groups |               2                 |
| Section 9. Reliability and precision                         |               1                 |
| Section 10. Validity support                                 |               2                 |
| Section 11. Fair use and comparability                       |               2                 |
| Section 12. Reports, leaderboards, and public score claims   |               2                 |

Reviewer comments: The overall picture is "well-designed and honestly reported, evidentially under-powered." Section 9 is the binding constraint: the absence of uncertainty on 16-31-item subsets caps how much any other strength can be relied upon for fine-grained conclusions. Section 6 is the standout strength.

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected entity or reporting surface | Affected capability domain or score interpretation | Affected rating(s) | Why it matters | Needed for a higher rating |
| :----------------------------------------------------------- | :----------------------------------- | :------------------------------------------------- | :----------------- | :------------- | :------------------------- |
| Confidence intervals / standard errors on the main model cohort | Paper Tables 2-5; leaderboard | All per-subset score interpretations | 6.2.4, 9.1.1, 9.2.2, 9.5.1, 12.1.2 | On 16-31-item subsets, one item = 3-6pp; rankings flip within noise | Binomial/bootstrap intervals reported with every score |
| Multi-run / seed variance for the AllRules and RAG cohort | Paper | Score stability | 9.2.1, 9.4.3 | Non-zero temperatures make single-run estimates carry unquantified decoding variance | Published k-run variance for the reported models |
| Human / expert performance baseline | Paper | Anchoring scores to human competence | 8.1.2, 10.4.1 | The framing invokes engineer-like work but no human anchor exists | A human accuracy baseline on at least the small subsets |
| Held-out split or contamination controls; train/test separation | Dataset, repository | Contamination, gameability | 5.6, 10.5.1, 10.5.2 | Public test set + "fine-tune on Retrieval QAs" advice invites optimizing against the test | A held-out/refreshable split and a train/test-respecting protocol |
| Metric validation against human correctness; multi-reference explanations | Scorer, Compliance subsets | Metric/scoring validity | 7.1.3, 9.3.1, 10.3.1, 10.3.2 | Format/verbosity effects and single-reference BLEU/ROUGE confound the target skill | Human-correlated metric study; additional reference explanations; format-tolerant parsing |
| License and dataset card | Repository | Lawful reuse, auditable redistribution | 1.2, 7.1.1, 7.1.7 | No LICENSE (404 / API `null`) leaves reuse terms unstated | An explicit license + dataset card |
| Versioning, changelog, releases, CI, pinned environment, seeds | Repository, harness | Reproducibility, lifecycle interpretation | 5.7, 5.8, 6.2.7, 7.1.4, 12.2.2 | Users cannot pin or reproduce the paper's numbers or tell what is stable | Version tags, changelog, environment file, seeds, smoke-test fixtures, CI |
| Cross-condition comparability normalization | Paper, leaderboard | Comparability | 6.2.6, 11.3.1 | Claude-Opus RAG-only, AllRules-vs-RAG, Gemini RECITATION artifact are not condition-matched | Condition-matched runs or explicit non-comparability warnings |
| Live leaderboard contents, governance, and eligibility rules | `design-qa.github.io` leaderboard | Public-claim governance | 12.4.3, 12.2.1 | Table/governance could not be rendered at access date; no documented eligibility or fine-tune-on-test policy | A rendered, governed leaderboard with uncertainty and condition labels |
| Per-item paper-run model outputs as an auditable release | Paper, repository | Validity, reproducibility audit | 12.3.2 | Independent scrutiny of the reported numbers is limited | Released per-item outputs for the reported runs |

### Reviewer Cautions and Unresolved Evidence Gaps

1. **Binding uncertainty gap.** The main model cohort carries no confidence intervals on subsets of 16, 30, and 31 items. Only large score gaps are interpretable; small-margin rankings (including any close leaderboard ordering) should be treated as noise. This is the single rating (Section 9 = 1) most likely to change with modest maintainer effort.
2. **Contamination and gameability.** The dataset and the FSAE rule text are fully public and web-searchable, and the authors recommend fine-tuning on the Retrieval QAs. High scores - especially on Retrieval - may reflect prior exposure or test-set optimization rather than general skill.
3. **Construct-irrelevant variance.** Format-following penalties, child-rule false negatives, BLEU/ROUGE length sensitivity, single-reference explanation scoring, the Gemini RECITATION zero, and the cost-driven RAG-only testing of Claude-Opus mean a meaningful share of score variance is not the target capability. Read cross-model differences with this in mind.
4. **License and lifecycle (confirmed live, 2026-06-28).** No LICENSE file (raw `LICENSE` HTTP 404; GitHub API `license: null`); no dataset card, versioning, changelog, releases, or CI. Recorded as evidence gaps, not as asserted restrictions or defects.
5. **Leaderboard surface unresolved.** `design-qa.github.io` renders the project landing page but its live results table and governance text could not be rendered at access time; leaderboard governance, eligibility, and uncertainty handling are therefore unverified.
6. **Scope discipline.** DesignQA makes no AGI claim. The only breadth flag is the implicit move from one FSAE rulebook to "real-world engineering design," disciplined here via `Measuring_what_Matters.md` and the authors' own single-document limitation; the supported interpretation is task-level and document-specific.

## Bibliography

[1] D. Hendrycks et al., "A Definition of AGI," arXiv:2510.18212, 2025.

[2] A. M. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," arXiv:2511.04703, 2025.

[3] A. Reuel et al., "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices," arXiv:2411.12990, 2024.

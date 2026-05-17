# MESA EFPA Template Filling Guide

Generated for `markdown/MESA EFPA template official.md`.

Access date for cited official or primary sources: 2026-05-16.

This guide teaches reviewers how to fill the MESA EFPA template using source-grounded benchmark examples. It is a guide, not a completed MESA review. Part A examples are descriptive. Part B examples illustrate evidence patterns for ratings and must not be copied as final ratings without inspecting the exact reviewed entity.

## Source And Citation Rules

- Use official or primary benchmark materials first: paper, official site, repository, dataset card, leaderboard, registry, methodology page, or maintainer announcement.
- Cite the exact reviewed entity, especially when the entity is a slice, hosted leaderboard, private form, rolling cohort, or evaluator-specific implementation.
- Treat missing documentation as an evidence gap, not as proof of poor benchmark quality.
- When an example is outside the inventory, it is marked `Outside inventory`.
- Review comments should normally fit this pattern: `Basis: ... Gap: ... Rationale: ... Caution: ...`.

## Source Registry

Use these short source codes in review comments.

| Code | Benchmark or entity | Official or primary sources |
| :--- | :------------------ | :-------------------------- |
| S01 | Humanity's Last Exam | [GitHub](https://github.com/centerforaisafety/hle), [arXiv](https://arxiv.org/abs/2501.14249), [dataset](https://huggingface.co/datasets/cais/hle) |
| S02 | ARC-AGI-2 | [official page](https://arcprize.org/arc-agi/2), [GitHub](https://github.com/arcprize/ARC-AGI-2), [technical report](https://arcprize.org/blog/arc-agi-2-technical-report) |
| S03 | GPQA Diamond | [GitHub](https://github.com/idavidrein/gpqa), [dataset](https://huggingface.co/datasets/Idavidrein/gpqa), [arXiv](https://arxiv.org/abs/2311.12022) |
| S04 | AIME 2025 as evaluator slice | [MAA AIME](https://maa.org/math-competitions/aime/), [Artificial Analysis evaluation](https://artificialanalysis.ai/evaluations/aime-2025), [methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) |
| S05 | MathArena Apex | [official page](https://matharena.ai/apex/), [arXiv](https://arxiv.org/abs/2505.23281) |
| S06 | MMMU-Pro | [GitHub](https://github.com/MMMU-Benchmark/MMMU), [arXiv](https://arxiv.org/abs/2409.02813), [homepage](https://mmmu-benchmark.github.io/) |
| S07 | ScreenSpot-Pro | [leaderboard](https://gui-agent.github.io/grounding-leaderboard), [GitHub](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding), [dataset](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro) |
| S08 | CharXiv Reasoning | [project page](https://charxiv.github.io/), [arXiv](https://arxiv.org/abs/2406.18521), [NeurIPS page](https://papers.nips.cc/paper_files/paper/2024/hash/cdf6f8e9fd9aeaf79b6024caec24f15b-Abstract-Datasets_and_Benchmarks_Track.html) |
| S09 | OmniDocBench 1.5 | [GitHub](https://github.com/opendatalab/OmniDocBench), [arXiv](https://arxiv.org/abs/2412.07626) |
| S10 | Video-MMMU | [official site](https://videommmu.github.io/), [GitHub](https://github.com/EvolvingLMMs-Lab/VideoMMMU), [arXiv](https://arxiv.org/abs/2501.13826) |
| S11 | LiveCodeBench Pro | [arXiv](https://arxiv.org/abs/2506.11928), [project page](https://livecodebenchpro.com/), [dataset](https://huggingface.co/datasets/QAQAQAQAQ/LiveCodeBench-Pro) |
| S12 | Terminal-Bench 2.0 | [official site](https://www.tbench.ai/), [GitHub](https://github.com/harbor-framework/terminal-bench), [Harbor registry](https://www.harborframework.com/registry/terminal-bench/2.0) |
| S13 | SWE-Bench Verified | [docs](https://www.swebench.com/SWE-bench/guides/datasets/), [GitHub](https://github.com/SWE-bench/SWE-bench), [dataset](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified), [OpenAI report](https://openai.com/index/introducing-swe-bench-verified/) |
| S14 | tau2-bench | [GitHub](https://github.com/sierra-research/tau2-bench), [arXiv](https://arxiv.org/abs/2506.07982), [leaderboard/docs](https://taubench.com/) |
| S15 | Vending-Bench 2 | [official page](https://andonlabs.com/evals/vending-bench-2), [original page](https://andonlabs.com/evals/vending-bench), [arXiv](https://arxiv.org/abs/2502.15840) |
| S16 | FACTS Benchmark Suite | [DeepMind blog](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/), [technical report PDF](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf), [Kaggle benchmark](https://www.kaggle.com/benchmarks/google/facts) |
| S17 | SimpleQA Verified | [dataset](https://huggingface.co/datasets/google/simpleqa-verified), [Kaggle benchmark](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified), [arXiv](https://arxiv.org/abs/2509.07968) |
| S18 | MMMLU | [dataset](https://huggingface.co/datasets/openai/MMMLU), [simple-evals](https://github.com/openai/simple-evals), [MMLU paper](https://arxiv.org/abs/2009.03300) |
| S19 | Global PIQA | [parallel dataset](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel), [nonparallel dataset](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel), [arXiv](https://arxiv.org/abs/2510.24081) |
| S20 | MRCR v2, 8-needle slice | [dataset](https://huggingface.co/datasets/openai/mrcr), [EvalScope docs](https://evalscope.readthedocs.io/en/latest/benchmarks/openai_mrcr.html) |
| O01 | Outside inventory: GenEval | [GitHub](https://github.com/djghosh13/geneval) |
| O02 | Outside inventory: VBench | [project page](https://vchitect.github.io/VBench-project/), [GitHub](https://github.com/Vchitect/VBench) |
| O03 | Outside inventory: AudioBench | [GitHub](https://github.com/AudioLLMs/AudioBench) |

## How To Use This Guide

1. Fill Section 1 first. Do not infer from a parent benchmark unless the reviewed entity's documentation supports the transfer.
2. In Sections 2-5, select only options supported by official or primary documentation. Use comments to record uncertainty, missing documentation, and slice boundaries.
3. In Sections 6-12, use the rating examples as evidence patterns. Replace the example with the reviewed entity's evidence before assigning a rating.
4. Carry unresolved gaps into the Gap Register instead of hiding them in prose.

---

# Part A Filling Guide

## Section 1. Factual Description

### 1.1 Review Target and Benchmark Entity

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Reviewed entity name | `MRCR v2 (8-needle)` [S20] | Basis: the inventory identifies this as an evaluation slice. Rationale: name the exact slice, not only the MRCR family. |
| Entity type | `evaluator-specific implementation` for AIME 2025 on Artificial Analysis [S04] | Basis: AIME is a contest source, while this is a hosted LLM benchmark use. Caution: do not import all MAA contest assumptions. |
| Parent or source benchmark | SWE-Bench Verified parented to SWE-Bench [S13] | Basis: the dataset card and docs describe Verified as a curated SWE-Bench subset. |
| Source instrument reused | AIME 2025 reuses MAA contest problems [S04] | Basis: the source instrument is a human math contest. Rationale: record reuse before evaluating adaptation. |
| Exact version, slice, split, cohort, form, or task-pack identifier | Terminal-Bench 2.0 Harbor registry entry [S12] | Basis: registry path identifies the task-pack version. Caution: cite task-pack identifier with scores. |
| Public, private, hidden, semi-private, rolling, retired, or controlled-access form | ARC-AGI-2 public plus semi-private/private split language [S02] | Basis: official materials distinguish public data and hidden competition use. |
| Hosted evaluator, leaderboard, registry, or platform implementation | FACTS on Kaggle [S16] | Basis: DeepMind documents the suite and Kaggle benchmark route. |
| Whether the reviewed entity has standalone documentation | LiveCodeBench Pro has paper and dataset, but public code/docs are narrower than standard LiveCodeBench [S11] | Basis: record standalone documentation as partial when the exact entity has fewer public materials. |
| Review boundary for this MESA review | AIME 2025 as Artificial Analysis slice [S04] | Basis: review the evaluator's prompt/scoring/methodology, not the whole MAA program. |

### 1.2 Review Information

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Reviewer | `MESA reviewer` | Basis: identify the reviewer or team for audit traceability. |
| Date of current review | `2026-05-16` | Basis: use the date official sources were inspected. |
| Date of previous review, if applicable | HLE pilot review date, if updating [S01] | Basis: prior review matters when materials changed. |
| Review scope | `Part A + Part B full review of ARC-AGI-2 public benchmark plus leaderboard surfaces` [S02] | Basis: scope names the entity and report surfaces covered. |
| Review boundary | `Official ARC Prize materials first; independent commentary excluded except as contextual critique` [S02] | Basis: state source hierarchy before review judgments. |

### 1.3 Information Sources Reviewed

| Material type | Benchmark example | Review comment example |
| :------------ | :---------------- | :--------------------- |
| Official paper or technical report | GPQA paper [S03] | Basis: source paper defines dataset construction and expert difficulty. |
| Benchmark website or documentation hub | Video-MMMU website [S10] | Basis: website gives task framing and links to implementation materials. |
| Repository | Terminal-Bench GitHub [S12] | Basis: repository is primary for harness, task format, and run workflow. |
| Dataset card, data host, or task host | MMMLU Hugging Face dataset [S18] | Basis: dataset card documents language coverage and data access. |
| Leaderboard, dashboard, or results page | ScreenSpot-Pro grounding leaderboard [S07] | Basis: leaderboard is a reporting surface and may define score interpretation. |
| Evaluation harness, package, or hosted runner | OpenAI `simple-evals` for MMMLU [S18] | Basis: harness identifies prompts and scorer path. |
| User guide, scoring guide, or contributor guide | SWE-Bench dataset docs [S13] | Basis: guide explains split and task use. |
| Release log, changelog, or maintenance record | ARC-AGI-2 changelog [S02] | Basis: update record affects comparability over time. |
| Maintainer statement or official announcement | DeepMind FACTS blog [S16] | Basis: announcement explains intent and release route. |
| Contextual literature | Measuring what Matters or BetterBench from local literature | Basis: use only for evaluation criteria, not as a replacement for benchmark facts. |

### 1.4 Benchmark Information

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Benchmark name | `Humanity's Last Exam` [S01] | Basis: use official benchmark name. |
| Short name or acronym | `HLE` [S01] | Basis: acronym appears in official repository/dataset. |
| Reviewed entity version, edition, or release | `ARC-AGI-2` [S02] | Basis: version is part of the benchmark name and release record. |
| Parent or source benchmark version, if different | `SWE-Bench Verified` from SWE-Bench [S13] | Basis: parent family and curated subset differ. |
| Dataset, task, split, or task-pack version | Terminal-Bench 2.0 [S12] | Basis: registry version should accompany results. |
| Scorer, judge, parser, harness, or evaluator implementation version | SWE-Bench harness/repository version [S13] | Basis: scorer implementation affects pass/fail interpretation. |
| Leaderboard, cohort, rolling-window, or evaluation date label | HLE-Rolling [S01] | Basis: rolling evaluations require date or cohort labels. |
| Original benchmark name, if this is an adaptation or slice | AIME for AIME 2025 LLM slice [S04] | Basis: source contest is distinct from evaluator implementation. |
| Benchmark creators or authors | GPQA paper authors [S03] | Basis: cite official paper author list. |
| Current maintainers | ARC Prize / `arcprize` GitHub org [S02] | Basis: maintainer identity supports issue routing and update interpretation. |
| Host organization, platform host, repository owner, or distributor | Kaggle for FACTS benchmark hosting [S16] | Basis: host may differ from benchmark authors. |
| Date of original release | ARC-AGI-2 release record [S02] | Basis: release date matters for contamination and versioning. |
| Date of current release or revision | MRCR dataset card or EvalScope docs [S20] | Basis: current revision identifies exact slice. |
| License or access terms | HLE GitHub license and dataset terms [S01] | Basis: repository and dataset host may impose different conditions. |
| Persistent identifier, citation, or DOI | arXiv identifier for CharXiv [S08] | Basis: persistent citation anchors the reviewed evidence. |

### 1.5 Public Artifacts

| Artifact | Benchmark example | Review comment example |
| :------- | :---------------- | :--------------------- |
| Paper or technical report | MathArena paper [S05] | Basis: paper defines Apex contest-problem benchmark framing. |
| Benchmark website | ScreenSpot-Pro project/leaderboard [S07] | Basis: project page is the main public navigation surface. |
| Code repository | OmniDocBench GitHub [S09] | Basis: repository documents evaluation scripts and data links. |
| Evaluation harness | Terminal-Bench GitHub [S12] | Basis: harness is needed for reproducible agentic terminal evaluation. |
| Dataset or task set | SimpleQA Verified dataset card [S17] | Basis: dataset card is the task-hosting source. |
| Prompt set | HLE prompt/judge instructions in repository [S01] | Basis: prompt templates shape response parsing and score meaning. |
| Rubric or scoring guide | SWE-Bench Verified task grading docs [S13] | Basis: scoring guide clarifies patch success. |
| Leaderboard or result display | MMMU homepage/leaderboard [S06] | Basis: leaderboard is a public score interpretation surface. |
| Hosted evaluation service or submission portal | Kaggle FACTS benchmark [S16] | Basis: hosted route controls score production. |
| Benchmark registry or task-pack entry | Terminal-Bench 2.0 Harbor registry [S12] | Basis: registry defines exact task pack. |
| Release log or changelog | ARC-AGI-2 changelog [S02] | Basis: changelog supports maintenance review. |
| Contact, issue channel, or feedback route | GitHub issues for ARC-AGI-2 [S02] | Basis: issue channel documents maintainer feedback route. |

## Section 2. Classification

### 2.1 Claimed Capability Domains

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | A leaderboard-only AIME 2025 slice may not define a new AI capability construct beyond contest reuse [S04] | Basis: source contest exists, but evaluator slice may not restate construct. Caution: document as missing if no methodology claim is available. |
| General Knowledge (K) | HLE includes broad academic factual knowledge questions [S01] | Basis: items span academic domains. Rationale: mark K when knowledge retrieval/selection is part of the target. |
| Reading and Writing Ability (RW) | GPQA uses text questions and answer options [S03] | Basis: response depends on reading specialized question text; do not overstate writing if outputs are multiple choice. |
| Mathematical Ability (M) | AIME 2025 and MathArena Apex target contest mathematics [S04, S05] | Basis: official materials identify math contest problems. |
| On-the-Spot Reasoning (R) | ARC-AGI-2 targets abstract grid reasoning [S02] | Basis: tasks require inference from demonstrations, not memorized facts. |
| Working Memory (WM) | MRCR 8-needle slice targets long-context retrieval under multiple needles [S20] | Basis: long context and multiple targets make temporary maintenance/retrieval central. |
| Long-Term Memory Storage (MS) | SimpleQA Verified targets parametric knowledge [S17] | Basis: model must store facts in parameters or retrieve equivalent knowledge if allowed. |
| Long-Term Memory Retrieval (MR) | MRCR requires retrieving target strings from context [S20] | Basis: mark retrieval when score depends on locating retained context content. |
| Visual Processing (V) | ScreenSpot-Pro uses GUI screenshots [S07] | Basis: locating UI targets requires visual processing. |
| Auditory Processing (A) | Outside inventory: AudioBench evaluates audio-language inputs [O03] | Basis: mark auditory only when audio input processing is part of the task. |
| Speed (S) | ARC-AGI-2 cost/efficiency framing can support speed or efficiency notes [S02] | Basis: use when timing, latency, or compute efficiency is part of interpretation. |
| Coding or software engineering | SWE-Bench Verified and LiveCodeBench Pro target coding tasks [S11, S13] | Basis: tasks require code generation or repository repair. |
| Specialized scientific or technical expertise | GPQA Diamond targets graduate-level science [S03] | Basis: expert science knowledge is central. |
| Domain-specific professional expertise | OmniDocBench targets OCR/document parsing expertise rather than general language ability [S09] | Basis: domain is document analysis. |
| Tool use | tau2-bench targets agentic tool use [S14] | Basis: tasks require using tools in simulated user/task settings. |
| Agency or autonomy | Vending-Bench 2 targets long-horizon agentic operation [S15] | Basis: repeated decisions over time are central. |
| Web or browser interaction | Use an outside web-agent benchmark if official docs require browser actions; no direct inventory example verified. | Basis: mark only when browser navigation is part of task evidence. |
| Embodied or simulated environment interaction | Vending-Bench 2 uses a simulated business environment [S15] | Basis: environment state changes across task horizon. |
| Factuality or grounding | FACTS Benchmark Suite evaluates factuality and grounding [S16] | Basis: official title and components identify factuality. |
| Multilingual or cross-cultural capability | MMMLU and Global PIQA target multilingual/cross-cultural evaluation [S18, S19] | Basis: source documents language/culture coverage. |
| Safety, refusal, or policy compliance | FACTS includes factuality and retrieval components, but use a safety-specific benchmark if refusal is the target [S16] | Basis: do not mark safety merely because a benchmark is high-stakes. |
| Robustness | MMMU-Pro is a harder/professional multimodal variant [S06] | Basis: mark robustness only when stress testing, adversarial variants, or harder transformations are stated. |
| Calibration or uncertainty | HLE asks for confidence and reports calibration-related outputs [S01] | Basis: confidence is part of output/scoring evidence. |

### 2.2 Area of Use

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | A raw dataset card without use framing, if encountered | Basis: use when no official use context is stated. |
| Model comparison | Artificial Analysis AIME 2025 ranks model performance [S04] | Basis: evaluator page compares models. |
| Leaderboard ranking | ARC Prize leaderboard [S02] | Basis: public leaderboard orders submissions. |
| Capability profiling | MMMU-Pro reports multimodal subject/task performance [S06] | Basis: subscores/profile support capability analysis. |
| Research diagnostics | CharXiv studies chart reasoning and synthesis [S08] | Basis: benchmark supports diagnosing chart-understanding weaknesses. |
| Safety evaluation | FACTS can support factuality/grounding safety-adjacent review [S16] | Basis: mark safety only where documentation links scores to risk-relevant use. |
| Deployment gating | Use only if official docs describe a threshold or gate; no inventory example verified. | Basis: absence of gate documentation is an evidence gap. |
| Procurement or vendor comparison | Use only if official materials target buyer decisions; no inventory example verified. | Basis: public rankings alone do not justify procurement use. |
| Internal regression testing | `simple-evals` style harness use can support regression testing if used internally [S18] | Basis: mark if documentation or reviewer scope says it is used for regressions. |
| Public communication or marketing | HLE and ARC-AGI-2 public score claims are widely surfaced by official sites [S01, S02] | Basis: public-facing sites make scores communicative. |
| Policy or governance analysis | FACTS and HLE can be cited in governance discussions with caveats [S01, S16] | Basis: mark only when public materials invite broader evaluation interpretation. |

### 2.3 Intended AI Systems

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | A dataset-only task release with no model target | Basis: use when target systems are absent from source. |
| Frontier general-purpose language models | HLE reports frontier model results [S01] | Basis: official results target frontier systems. |
| Chat or instruction-following models | AIME 2025 Artificial Analysis evaluates current chat models [S04] | Basis: hosted evaluator reports model API outputs. |
| Base language models | Use only when official docs evaluate non-instruction base models; no inventory example verified. | Basis: do not infer base-model intent from LLM framing. |
| Code models | LiveCodeBench Pro targets coding systems [S11] | Basis: competitive coding tasks are intended for code-capable systems. |
| Multimodal models | MMMU-Pro and Video-MMMU target multimodal systems [S06, S10] | Basis: inputs include image/video information. |
| Audio or speech models | Outside inventory: AudioBench targets audio language models [O03] | Basis: auditory modality is required. |
| Agentic systems | Terminal-Bench and Vending-Bench 2 target agentic systems [S12, S15] | Basis: systems act over tasks/environments. |
| Tool-using systems | tau2-bench targets tool use [S14] | Basis: tool calls are part of task success. |
| Retrieval-augmented systems | FACTS includes search/retrieval grounding components [S16] | Basis: mark when retrieval is an intended condition or component. |
| Domain-specialized models | OmniDocBench can evaluate document AI/OCR systems [S09] | Basis: domain-specialized document systems are plausible intended systems. |
| Open-weight local models | ARC-AGI-2 public repository supports local solvers [S02] | Basis: local/open systems can run public tasks. |
| API-hosted models | Terminal-Bench and HLE support API/provider evaluation routes [S01, S12] | Basis: official harnesses or examples call API-hosted systems. |

### 2.4 Intended Users of Benchmark Outputs

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | Dataset-only release with no audience statement | Basis: mark when no audience can be source-grounded. |
| Benchmark creators or maintainers | ARC Prize maintainers use ARC-AGI-2 leaderboard and changelog [S02] | Basis: maintainers monitor task and score ecosystem. |
| AI researchers | GPQA and MMMU-Pro papers target research audiences [S03, S06] | Basis: academic benchmark papers are research-facing. |
| Model developers | SWE-Bench Verified supports model development evaluation [S13] | Basis: coding agents are compared on verified tasks. |
| Product teams | FACTS can inform factuality evaluation in product settings if documented [S16] | Basis: use cautiously unless deployment context is explicit. |
| Safety evaluators | HLE and FACTS may be relevant to capability/factuality safety review [S01, S16] | Basis: mark only with stated or clearly implied evaluation use. |
| Policy or governance actors | HLE public communication and FACTS factuality framing can inform governance discussion [S01, S16] | Basis: caveat against using scores alone for policy decisions. |
| Procurement or enterprise decision-makers | Use only if official docs target procurement; no inventory example verified. | Basis: model comparison is not automatically procurement validation. |
| Educators or academic reviewers | AIME and MathArena reuse academic contest-style material [S04, S05] | Basis: educators may interpret source contest context, but AI benchmark use differs. |
| Public leaderboard users | ARC Prize, MMMU, ScreenSpot-Pro, and Artificial Analysis expose public rankings [S02, S04, S06, S07] | Basis: public users see rankings and need caveats. |

### 2.5 Task Families, Subdomains, and Scores

| Component | Benchmark example | Review comment example |
| :-------- | :---------------- | :--------------------- |
| Capability, phenomenon, or quality the benchmark claims to measure | FACTS claims factuality/grounding [S16] | Basis: use benchmark's own claim wording. |
| Definition of the capability or quality being measured | ARC-AGI-2 defines abstract reasoning/generalization through grid tasks [S02] | Gap: broad AGI language must be separately evaluated in Part B. |
| Subcomponents of the claimed capability, phenomenon, or quality | MMMU-Pro subject/modality components [S06] | Basis: record documented subdomains, not reviewer-invented categories. |
| Excluded scope or non-target abilities | HLE caveats against AGI/autonomous research inference [S01] | Basis: exclusions are key interpretive boundaries. |
| Benchmark item, prompt, episode, environment, or interaction families or subdomains | Terminal-Bench tasks are terminal episodes [S12] | Basis: task family is an interaction environment, not just a question set. |
| Sources for benchmark items, prompts, episodes, environments, or interactions | AIME contest source [S04] | Basis: record source reuse before judging adaptation. |
| Sampling method for benchmark items, prompts, episodes, environments, or interactions | GPQA expert-written and filtered questions [S03] | Basis: source describes construction process. |
| Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions | SWE-Bench Verified curation [S13] | Basis: Verified is selected from parent SWE-Bench. |
| Splits or partitions | ARC-AGI-2 public/hidden split structure [S02] | Basis: split status affects access and comparability. |
| Primary score | ScreenSpot-Pro grounding accuracy [S07] | Basis: primary score should match official leaderboard metric. |
| Subscores | MMMU-Pro subject/category scores [S06] | Basis: record only documented subscore families. |
| Derived scores or scores combined from item, task-family, or subscore results | FACTS suite components aggregated at suite/report level [S16] | Basis: describe aggregation without evaluating it here. |
| Qualitative score ranges such as low/medium/high or novice/expert | ARC-AGI-2 human/model contrast and cost framing [S02] | Basis: use if official reports assign qualitative bands or categories. |
| Boundaries or caveats for interpretations made from benchmark scores | HLE AGI/autonomy caveats [S01] | Basis: carry caveats forward into Part B validity and reporting. |

### 2.6 Model Response Mode

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | Dataset-only release with missing response instructions | Basis: record missing response mode as a documentation gap. |
| Multiple choice | GPQA Diamond [S03] | Basis: answers are chosen among options. |
| Short text | SimpleQA Verified [S17] | Basis: factoid answers are short text. |
| Long-form text | FACTS long-form factuality/grounding tasks where applicable [S16] | Basis: mark only if response requires extended prose. |
| Structured output, such as JSON or XML | ARC-AGI-2 grid outputs in JSON-like task files [S02] | Basis: exact structured output is central. |
| Code | LiveCodeBench Pro [S11] | Basis: model response is program/code solution. |
| Mathematical expression | AIME 2025 answer format [S04] | Basis: contest answer is a numeric/math response. |
| Tool call | tau2-bench [S14] | Basis: tool call is an evaluated action. |
| Browser or web action | Outside inventory web-agent benchmark if official docs require browser actions | Basis: no direct verified inventory option; use outside source if needed. |
| File, document, or other output generation | SWE-Bench Verified patch file/repo changes [S13] | Basis: output is a repository modification artifact. |
| Image output | Outside inventory: GenEval [O01] | Basis: image generation output is the evaluated response. |
| Audio output | Outside inventory: AudioBench if generation tasks are used [O03] | Basis: mark only for audio-producing tasks, not audio input alone. |
| Video output | Outside inventory: VBench [O02] | Basis: video generation output is evaluated. |
| Interaction in a simulated environment | Vending-Bench 2 [S15] | Basis: system acts in a simulated business environment. |
| Interaction in a real or external environment | Use only if benchmark officially permits real external side effects; no inventory example verified. | Basis: do not mark for simulated environments. |

### 2.7 Prerequisites for Evaluated Systems

For each row, choose `Irrelevant`, `Necessary information given`, or `Information missing`.

| Requirement | Benchmark example | Review comment example |
| :---------- | :---------------- | :--------------------- |
| Language support | MMMLU language coverage [S18] | Basis: languages are central and should be documented. |
| Context length | MRCR token-length bins [S20] | Basis: long-context capacity is necessary information. |
| Multimodal input support | Video-MMMU video inputs [S10] | Basis: video-capable model required. |
| Structured output support | ARC-AGI-2 exact grids [S02] | Basis: output schema affects scoring. |
| Exact format, schema, or parser compatibility | ARC-AGI-2 output grids [S02] | Basis: malformed output policy affects score meaning. |
| Retry, repair, or correction-loop support for malformed outputs | SWE-Bench repair/rerun policies where documented [S13] | Basis: record whether failures can be retried or repaired. |
| Tool access | tau2-bench tool APIs [S14] | Basis: tool availability is prerequisite. |
| Browser or internet access | FACTS search/retrieval component [S16] | Basis: external access must be documented if permitted. |
| Code execution | LiveCodeBench Pro [S11] | Basis: code execution validates solutions. |
| External API or tool credentials | Terminal-Bench provider/API routes [S12] | Basis: credentials affect who can run evaluation. |
| Memory or persistent state | Vending-Bench 2 long-horizon state [S15] | Basis: state persistence affects performance. |
| Environment, simulator, or task-registry compatibility | Terminal-Bench task registry [S12] | Basis: registry compatibility defines runnable tasks. |
| API compatibility | HLE API-compatible scripts [S01] | Basis: model access path should be explicit. |
| Latency or time budget | ARC-AGI-2 efficiency/cost framing [S02] | Basis: time/cost conditions affect comparability. |
| Cost or compute budget | ARC Prize cost reporting [S02] | Basis: cost must be documented when part of interpretation. |

### 2.8 Evaluation Conditions

| Condition | Benchmark example | Review comment example |
| :-------- | :---------------- | :--------------------- |
| Prompting protocol | HLE prompt protocol [S01] | Basis: official prompt controls response format and confidence. |
| System prompt | HLE or `simple-evals` system/developer prompt if documented [S01, S18] | Basis: record exact prompt or state missing. |
| Few-shot examples | ARC-AGI-2 demonstration grids [S02] | Basis: tasks include examples before test grid. |
| Sampling settings | HLE evaluation settings where documented [S01] | Gap: if seeds/temperature absent, mark missing in comments. |
| Tool permissions | tau2-bench tool use [S14] | Basis: allowed tools define the task. |
| Tool/API credential policy | Terminal-Bench provider setup [S12] | Basis: credentials and services affect reproducibility. |
| Time limits | ARC-AGI-2 competition or leaderboard rules [S02] | Basis: cite exact source when time is part of official conditions. |
| Human intervention rules | SWE-Bench Verified should define autonomous vs assisted patching [S13] | Basis: human help changes interpretation. |
| Official rerun, retry, or repair policy | Kaggle FACTS or ARC competition rules where available [S16, S02] | Basis: retries affect score stability and fairness. |
| Hardware or hosted service | Terminal-Bench/Harbor registry [S12] | Basis: environment assumptions affect comparability. |
| Network requirements | FACTS search/retrieval component [S16] | Basis: network access should be stated if retrieval is used. |
| Sandbox or security constraints | Terminal-Bench terminal environment [S12] | Basis: terminal tasks require sandbox boundaries. |
| Model identity and version-label requirements | Artificial Analysis methodology [S04] | Basis: model versions should be identifiable. |
| Special administration conditions | HLE public/private or HLE-Rolling [S01] | Basis: special forms must be described separately. |

### 2.9 Task Interaction and Observable Evidence Types

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Multiple choice, single correct answer | GPQA Diamond [S03] | Basis: single correct option selected. |
| Multiple choice, multiple correct answers | Use only with official multi-answer tasks; no inventory example verified. | Basis: do not infer from single-answer MC benchmarks. |
| Ranking | Leaderboard ranking in ARC Prize [S02] | Basis: ranking is a report/evidence type, not necessarily task response. |
| Classification | FACTS factuality classification components where applicable [S16] | Basis: classify factual correctness/grounding when documented. |
| Pairwise preference | Use outside pairwise preference benchmark if official docs use pairwise scoring. | Basis: no verified inventory pairwise task. |
| Open-ended text | FACTS long-form factuality tasks [S16] | Basis: free text output is scored for factuality/grounding. |
| Code generation | LiveCodeBench Pro [S11] | Basis: generated code is evaluated. |
| Proof, derivation, or explanation | MathArena Apex may require contest-math reasoning/explanation depending official format [S05] | Basis: record only if explanation is submitted/scored. |
| Structured data | ARC-AGI-2 grids [S02] | Basis: output structure is the answer. |
| Generated media | Outside inventory: GenEval or VBench [O01, O02] | Basis: generated image/video is the artifact under evaluation. |
| Artifact production | SWE-Bench Verified patch [S13] | Basis: repository patch is produced. |
| Patch or repository modification | SWE-Bench Verified [S13] | Basis: success is a codebase change. |
| Coordinate, bounding target, or GUI-grounding target | ScreenSpot-Pro [S07] | Basis: output identifies GUI target coordinates/locations. |
| Document parsing, layout reconstruction, or OCR-style extraction | OmniDocBench [S09] | Basis: target is document structure/OCR extraction. |
| Tool use | tau2-bench [S14] | Basis: tool calls are part of episode. |
| Browser or web navigation | Use outside web-agent benchmark if browser traces are official evidence. | Basis: no direct verified inventory example. |
| API interaction | tau2-bench or Terminal-Bench [S14, S12] | Basis: API/tool interactions form task evidence. |
| Computer-use interaction | ScreenSpot-Pro GUI grounding [S07] | Basis: GUI target selection is computer-use adjacent. |
| Simulated environment task | Vending-Bench 2 [S15] | Basis: actions update simulated environment. |
| Real or external environment task | Use only with official real-world side-effect benchmark; no inventory example verified. | Basis: simulated is not real external action. |
| Terminal, shell, or filesystem task | Terminal-Bench 2.0 [S12] | Basis: terminal interactions are central. |
| User-simulator interaction | tau2-bench [S14] | Basis: user simulator/tool environment shapes task. |
| Long-horizon episode or stateful task | Vending-Bench 2 [S15] | Basis: score depends on long-horizon state. |
| Response latency | ARC-AGI-2 efficiency/cost reporting if time is reported [S02] | Basis: latency is process evidence only when recorded. |
| Token usage | HLE reports token/cost-related output where documented [S01] | Basis: include only if reported. |
| Cost | ARC-AGI-2 cost-aware reporting [S02] | Basis: cost is an observable process metric. |
| Tool traces | tau2-bench [S14] | Basis: tool-use trace supports audit. |
| Search or retrieval transcript | FACTS retrieval/search component [S16] | Basis: transcript matters if retrieval is part of score. |
| User-simulator actions | tau2-bench [S14] | Basis: user simulator actions are process evidence. |
| Intermediate reasoning traces | Use only when officially collected; no inventory example verified as public. | Basis: do not assume hidden chain-of-thought exists. |
| Execution logs | Terminal-Bench [S12] | Basis: logs support terminal-task audit. |
| Unit-test, patch, or verifier result | SWE-Bench Verified [S13] | Basis: tests/verifiers determine patch success. |
| Environment or simulator state | Vending-Bench 2 [S15] | Basis: state is part of outcome. |
| Leaderboard submission metadata | ARC Prize leaderboard [S02] | Basis: metadata supports comparison and governance. |
| Raw output or audit trace under controlled access | FACTS/Kaggle hosted route may use controlled access [S16] | Basis: document access route and limits. |

### 2.10 Input Stimulus Type

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | Dataset card without input schema | Basis: mark missing if input type cannot be established. |
| Text | GPQA Diamond [S03] | Basis: item stem/options are text. |
| Code | LiveCodeBench Pro [S11] | Basis: coding problems include code-like inputs/specs. |
| Tables or structured data | ARC-AGI-2 grid arrays [S02] | Basis: input is structured grid data. |
| Charts or figures | CharXiv [S08] | Basis: chart/figure input is central. |
| Images | MMMU-Pro [S06] | Basis: image input supports multimodal reasoning. |
| GUI screenshots | ScreenSpot-Pro [S07] | Basis: GUI screenshot is the stimulus. |
| Audio | Outside inventory: AudioBench [O03] | Basis: audio input is required. |
| Video | Video-MMMU [S10] | Basis: video input is central. |
| Documents | OmniDocBench [S09] | Basis: document image/PDF-style input is target. |
| PDF or document pages | OmniDocBench [S09] | Basis: page layout and OCR are evaluated. |
| Web pages | Use outside web-agent benchmark if web pages are official stimuli. | Basis: no direct verified inventory example. |
| Terminal or filesystem state | Terminal-Bench [S12] | Basis: shell/filesystem state is presented to the agent. |
| Long-context transcript or retrieved corpus | MRCR [S20] | Basis: long context is the input. |
| APIs or tools | tau2-bench [S14] | Basis: APIs/tools are part of input environment. |
| Dynamic environment | Vending-Bench 2 [S15] | Basis: state evolves over time. |
| Simulation state | Vending-Bench 2 [S15] | Basis: simulated inventory/business state is input context. |
| External search results | FACTS search retrieval component [S16] | Basis: search/retrieval evidence is part of benchmark suite. |

### 2.11 Number of Items or Measurement Points

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Total public items or tasks | HLE public 2,500-question set [S01] | Basis: use exact public count from official materials. |
| Total private or hidden items | ARC-AGI-2 hidden/private split [S02] | Basis: record as hidden if count is disclosed; otherwise mark count unknown. |
| Development or example items | ARC-AGI-2 training/demo tasks [S02] | Basis: distinguish training examples from evaluation tasks. |
| Test items | GPQA Diamond test set [S03] | Basis: cite split/card or paper. |
| Dynamic or generated tasks | Terminal-Bench task registry/version [S12] | Basis: dynamic task sets need registry/task-pack identifiers. |
| Episodes, trials, or measurement points | Vending-Bench 2 long-horizon episodes [S15] | Basis: record episodes when benchmark is not item-based. |
| Counts by split, form, or variant | MRCR 2/4/8-needle and token-length bins [S20] | Basis: slice counts matter. |
| Counts by language, culture, or locale | Global PIQA 101 languages/cultures [S19] | Basis: language/culture counts support coverage claims. |
| Counts by claimed capability domain | MMMU-Pro categories [S06] | Basis: domain counts support capability profiling. |
| Counts by context-length bin | MRCR token-length bins [S20] | Basis: context length bins affect interpretation. |
| Counts by difficulty band | ARC-AGI-2 human calibration/difficulty claims [S02] | Basis: difficulty counts need official support. |
| Counts by public, private, hidden, or controlled-access status | ARC-AGI-2 public/hidden split [S02] | Basis: status controls inspection and leakage risk. |
| Item count uncertainty | LiveCodeBench Pro if public docs differ across paper/dataset [S11] | Basis: state count uncertainty rather than forcing a single number. |

### 2.12 Mode of Evaluation

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not indicated | Dataset-only card with no run instructions | Basis: mark when mode cannot be inferred. |
| Local batch evaluation | HLE scripts or `simple-evals` [S01, S18] | Basis: local runner can evaluate batch tasks. |
| Hosted benchmark platform | FACTS on Kaggle [S16] | Basis: hosted platform administers scoring/submission. |
| Leaderboard submission | ARC Prize leaderboard [S02] | Basis: leaderboard route is documented. |
| Private controlled evaluation | SWE-Bench Verified/OpenAI reported subset curation [S13] | Basis: controlled evaluation should be distinguished from public data. |
| Public open evaluation | HLE public dataset and repo [S01] | Basis: public materials permit open evaluation. |
| Interactive agent evaluation | Terminal-Bench [S12] | Basis: agent interacts with terminal environment. |
| Human-in-the-loop evaluation | HLE expert/human judgment components [S01] | Basis: human review or judging appears in construction/scoring evidence. |
| Continuous or rolling evaluation | HLE-Rolling [S01] | Basis: rolling form requires date/cohort labels. |
| Benchmark suite or sub-leaderboard | FACTS Benchmark Suite [S16] | Basis: suite components should be identified. |
| Competition or challenge submission | ARC Prize/Kaggle competition [S02] | Basis: competition rules affect comparability. |
| Third-party evaluator implementation | Artificial Analysis AIME 2025 [S04] | Basis: evaluator defines prompt/scoring layer. |
| Registry-hosted task pack | Terminal-Bench 2.0 Harbor registry [S12] | Basis: registry path identifies exact tasks. |
| No control over submitted systems | Public dataset-only local runs, if no submission rules | Basis: record absence of system control. |
| Some control over submitted systems | ARC Prize submission requirements [S02] | Basis: public leaderboard often controls metadata/rules partly. |
| Controlled model access or audit | FACTS/Kaggle hosted benchmark [S16] | Basis: platform can constrain submissions. |
| Controlled evaluation center or private harness | Private held-out benchmark form, if documented | Basis: mark only when official private harness exists. |
| Not documented | LiveCodeBench Pro if exact public submission controls are unclear [S11] | Basis: state missing governance details. |

### 2.13 Technological Arrangements

| Technology | Benchmark example | Review comment example |
| :--------- | :---------------- | :--------------------- |
| API access | HLE API-compatible evaluation scripts [S01] | Basis: mark A/R according to whether API is optional or required. |
| Local inference | ARC-AGI-2 public tasks [S02] | Basis: local solvers can run public data. |
| GPU | Video-MMMU or VBench-style multimodal/video evaluation may require GPU [S10, O02] | Basis: mark required only if docs require it. |
| CPU-only execution | ARC-AGI-2 simple scoring can run CPU-side [S02] | Basis: distinguish scoring from model inference. |
| Docker or container | Terminal-Bench task environments may use containerized setup [S12] | Basis: container requirements affect reproduction. |
| Python package or CLI | Terminal-Bench CLI [S12] | Basis: CLI is a runnable artifact. |
| Browser | ScreenSpot-Pro leaderboard/project page or GUI task interface [S07] | Basis: mark browser if needed for human interface or task. |
| External tools | tau2-bench [S14] | Basis: external tools are part of task. |
| Internet access | FACTS search retrieval component [S16] | Basis: internet/search access changes score meaning. |
| Proprietary platform | Kaggle FACTS [S16] | Basis: hosted platform affects access and governance. |
| Hosted scoring service | Artificial Analysis AIME 2025 [S04] | Basis: scorer is hosted by evaluator. |
| Benchmark registry or task environment | Terminal-Bench Harbor registry [S12] | Basis: registry fixes task-pack identity. |
| Simulator or user simulator | tau2-bench and Vending-Bench 2 [S14, S15] | Basis: simulator behavior is part of benchmark. |
| Filesystem, terminal, or sandbox state | Terminal-Bench [S12] | Basis: state is both stimulus and evidence. |

### 2.14 Time and Resource Requirements

| Activity | Benchmark example | Review comment example |
| :------- | :---------------- | :--------------------- |
| Setup | Terminal-Bench setup docs [S12] | Basis: setup instructions should include environment prerequisites. |
| Model inference or task completion | HLE run scripts [S01] | Basis: record time/cost if official docs report it. |
| Token or context-window use | MRCR token bins [S20] | Basis: context length is part of resource requirements. |
| Scoring | SWE-Bench Verified test/scoring run [S13] | Basis: scoring may require dependency installation and tests. |
| Human adjudication | HLE human review/judge process [S01] | Basis: human effort should be separated from automated scoring. |
| Analysis or reporting | FACTS reporting on Kaggle [S16] | Basis: hosted reports may reduce reviewer-side analysis but limit audit. |
| Full benchmark run | Terminal-Bench or HLE full run [S12, S01] | Basis: record estimate or mark missing. |
| API or compute cost | ARC-AGI-2 cost-aware leaderboard [S02] | Basis: cost is an interpretation condition. |
| External tool, service, or search cost | FACTS retrieval/search [S16] | Basis: external service cost can affect fair comparison. |

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant example | Purpose | Score-comparability comment |
| :---------------------- | :------ | :-------------------------- |
| HLE public set and HLE-Rolling [S01] | Static public benchmark plus refreshed/rolling form | Reviewer comment: cite rolling cohort/date and avoid assuming direct comparability. |
| ARC-AGI-2 public, semi-private, and private forms [S02] | Public practice/audit plus protected evaluation | Reviewer comment: public/private split supports integrity but limits independent inspection. |
| MRCR 2-, 4-, and 8-needle slices [S20] | Vary long-context retrieval difficulty | Reviewer comment: do not compare slices as the same form. |
| MMMLU language variants [S18] | Multilingual evaluation | Reviewer comment: language-specific results need language labels. |

### 2.16 Static or Dynamic Task Determination

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Static fixed task set | GPQA Diamond [S03] | Basis: fixed questions support static evaluation. |
| Random sample from fixed pool | Use if evaluator samples items from a disclosed pool; no direct inventory example verified. | Basis: record sampling seed if known. |
| Hidden test set selected by maintainers | ARC-AGI-2 hidden/private set [S02] | Basis: hidden set selected for protected evaluation. |
| Procedurally generated tasks | Use outside procedural benchmark if official docs generate items. | Basis: no verified inventory example. |
| Adaptive routing based on performance | Use only if official docs route tasks adaptively; no inventory example verified. | Basis: do not infer from difficulty tiers. |
| Dynamic environment generation | Vending-Bench 2 environment episodes [S15] | Basis: state can vary by episode. |
| Rolling or periodically refreshed task set | HLE-Rolling [S01] | Basis: rolling changes need maintenance policy. |
| Contest-stream or recent-source capture | LiveCodeBench Pro recent competitive programming problems [S11] | Basis: source recency is part of contamination control. |
| Versioned dataset slice | MRCR 8-needle slice [S20] | Basis: exact slice is the reviewed entity. |
| Translated or localized form | MMMLU and Global PIQA [S18, S19] | Basis: translations/local forms should be identified. |
| Stateful environment instance | Vending-Bench 2 [S15] | Basis: episode state persists across decisions. |
| Not explicitly stated | A benchmark with missing task-selection docs | Basis: mark as missing rather than guessing static/dynamic. |

### 2.17 Evidence Sources Used in Scoring

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Model final answer | GPQA Diamond [S03] | Basis: selected answer is scored. |
| Model intermediate trace | Use only when trace is officially collected/scored; no inventory example verified. | Basis: do not assume hidden reasoning is evidence. |
| Tool-use trace | tau2-bench [S14] | Basis: trace matters because tool behavior is evaluated. |
| Search, retrieval, or browser transcript | FACTS search/retrieval component [S16] | Basis: transcript supports grounding audit. |
| Code execution result | LiveCodeBench Pro [S11] | Basis: code is run against tests. |
| Environment state | Vending-Bench 2 [S15] | Basis: final/intermediate state determines success. |
| Simulator state or user-simulator actions | tau2-bench [S14] | Basis: simulator/user actions are part of episode. |
| Reference answer | AIME 2025 or GPQA [S04, S03] | Basis: answer key defines correctness. |
| Unit test | SWE-Bench Verified [S13] | Basis: tests determine patch pass/fail. |
| Patch, verifier, or final-state check | SWE-Bench Verified [S13] | Basis: final repo state is verified. |
| Coordinate, bounding target, or GUI target | ScreenSpot-Pro [S07] | Basis: target coordinate/element is reference. |
| Document layout or structured extraction target | OmniDocBench [S09] | Basis: output compared to layout/OCR target. |
| Human judge | HLE human expert review in item development/scoring evidence [S01] | Basis: record when humans judge outputs or validate items. |
| Model judge | HLE judge model scoring path [S01] | Basis: model-as-judge affects reliability and validity. |
| Ensemble or panel adjudication | Use only if official docs describe panel adjudication; no direct inventory example verified. | Basis: do not infer from multiple authors. |
| External verifier | SWE-Bench Verified test suite [S13] | Basis: tests/verifier external to model response. |
| Leaderboard submission metadata | ARC Prize leaderboard [S02] | Basis: submission metadata supports governance. |

### 2.18 Broad-Claim Flags for Later Evaluation

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Term used for broad interpretation from benchmark scores | ARC-AGI-2 uses AGI/general-intelligence language [S02] | Basis: record exact terms; evaluate proportionality in Part B. |
| Breadth implied by the score interpretation across domains | HLE title and academic scope imply broad academic breadth [S01] | Basis: distinguish academic breadth from broad cognition. |
| Depth or proficiency level implied by the score interpretation | GPQA Diamond graduate-level science [S03] | Basis: expert-level claim should be source-grounded. |
| Capability domains from 2.1 explicitly covered | MMMU-Pro covers multimodal understanding/reasoning categories [S06] | Basis: list documented domains. |
| Capability domains from 2.1 explicitly excluded or not tested | HLE caveats against AGI/autonomous research [S01] | Basis: exclusions limit final claims. |
| Coverage across modalities, tools, memory, planning, or speed | Video-MMMU covers video; MRCR covers long context; tau2 covers tools [S10, S20, S14] | Basis: record breadth without evaluating sufficiency here. |
| Whether aggregate scores preserve capability-domain caveats | FACTS suite reporting should preserve component caveats [S16] | Basis: aggregate interpretation needs component limits. |
| Stated AGI, autonomy, or agency caveats | HLE caveats [S01] | Basis: carry caveats into Section 10.6. |
| Documented broad-claim limits or non-use statements | ARC-AGI-2 if source states AGI limitations; otherwise record gap [S02] | Basis: gap matters for overclaim risk. |
| Documented caveats to carry forward into Part B | All reviewed entities with hidden sets or slices | Basis: caveats become validity, fairness, and reporting evidence. |

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not explicitly stated | AIME 2025 slice if prompt/parser details are absent from evaluator page [S04] | Basis: mark missing scoring procedure if methodology does not specify it. |
| Automated exact-match scoring | ARC-AGI-2 exact grid match [S02] | Basis: output is correct only if grid matches. |
| LLM equality-checker scoring | HLE equality/judge path [S01] | Basis: model checks answer equivalence. |
| Automated semantic or embedding-based scoring | Use outside semantic scoring benchmark if official docs use embeddings. | Basis: no verified inventory example. |
| String-similarity or edit-distance scoring | OmniDocBench OCR/layout metrics may include text similarity/edit style metrics [S09] | Basis: cite exact metric when used. |
| Unit-test or execution-based scoring | LiveCodeBench Pro [S11] | Basis: code execution/tests score solution. |
| Patch, verifier, or final-state scoring | SWE-Bench Verified [S13] | Basis: repository patch success is verified. |
| Rule-based scoring | AIME numeric answer checking [S04] | Basis: deterministic rule maps answer to correctness. |
| Coordinate or bounding-target scoring | ScreenSpot-Pro [S07] | Basis: coordinate/target matching scores GUI grounding. |
| Document structure, layout, or OCR scoring | OmniDocBench [S09] | Basis: document parsing metrics score layout/text extraction. |
| State-based environment reward | Vending-Bench 2 [S15] | Basis: final balance/state supports reward. |
| Simulator-verified task success | tau2-bench [S14] | Basis: simulator determines tool-use task success. |
| Human rating | HLE expert review in item validation [S01] | Basis: human judgment should be described separately from model judge. |
| Scoring by another model that evaluates outputs | HLE model judge [S01] | Basis: scorer is an AI system. |
| Output parser or extractor that turns model responses into scoreable values | HLE answer/confidence extraction [S01] | Basis: parser affects what is scored. |
| Fuzzy, schema-aware, or admissible-variant parsing | HLE admissible answer equivalence [S01] | Basis: accepted variants need validation. |
| Pairwise preference scoring | Use outside pairwise benchmark if official docs use preference comparisons. | Basis: no verified inventory example. |
| Hybrid automated and human scoring | HLE item validation plus automated/model scoring path [S01] | Basis: separate development validation from run-time scoring. |
| Leaderboard service scoring | Kaggle FACTS or Artificial Analysis AIME [S16, S04] | Basis: hosted service computes/records scores. |
| Multi-run or pass@k sampling policy | LiveCodeBench Pro or coding benchmarks with pass@k [S11] | Basis: record k and sampling conditions. |
| Manual adjudication | Use only when official docs describe manual adjudication; no direct inventory example verified. | Basis: mark missing if unclear. |

### 3.2 Scores and Metrics

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Primary score | SWE-Bench Verified resolve rate [S13] | Basis: primary score maps to task success. |
| Subscore | MMMU-Pro category/discipline subscores [S06] | Basis: subscore should be official, not reviewer-created. |
| Derived score | ARC-AGI-2 cost-adjusted or efficiency framing [S02] | Basis: derived score needs formula and caveats. |
| Qualitative band | MathArena/leaderboard difficulty or performance bands if documented [S05] | Basis: record qualitative labels only when official. |
| Format/refusal/failure treatment | HLE parser/refusal treatment [S01] | Basis: malformed responses affect scoring validity. |
| Eligibility/API/tool/timeouts | Terminal-Bench task run failures [S12] | Basis: run failure policy affects comparability. |
| Retry/repair/parser fallback | SWE-Bench Verified patch/test rerun handling [S13] | Basis: record official retry or fallback route. |

### 3.3 Scale or Metric Types

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Raw score | AIME number correct [S04] | Basis: raw correct count can be reported. |
| Accuracy | GPQA Diamond [S03] | Basis: proportion correct. |
| Success rate | Terminal-Bench [S12] | Basis: tasks completed successfully. |
| Pass rate or pass@k | LiveCodeBench Pro [S11] | Basis: pass@k depends on sampling policy. |
| Unit-test pass rate | SWE-Bench Verified [S13] | Basis: tests define resolution. |
| Edit distance | OmniDocBench OCR/text metrics where applicable [S09] | Basis: cite exact metric. |
| BLEU, METEOR, or text-similarity metric | Use only if official text-generation benchmark uses these; no inventory example verified. | Basis: do not add legacy NLP metrics by assumption. |
| TEDS or structural similarity | OmniDocBench document/table structure scoring [S09] | Basis: structural similarity is relevant to document parsing. |
| Sequence-matcher ratio | OmniDocBench if documented metric uses it [S09] | Basis: cite exact implementation. |
| Coordinate accuracy | ScreenSpot-Pro [S07] | Basis: coordinate/element hit accuracy. |
| Win rate | Use outside preference/arena benchmark if official docs use win rate. | Basis: no verified inventory example. |
| Elo or ranking score | Leaderboard/arena-style reports if official; no direct inventory example verified. | Basis: do not infer Elo from rank. |
| Pairwise preference score | Use outside preference benchmark if official docs use pairwise comparisons. | Basis: no verified inventory example. |
| Reward or return | Vending-Bench 2 [S15] | Basis: environment return/balance can be reward. |
| Task-completion reward | tau2-bench [S14] | Basis: simulator task success maps to reward. |
| Final balance or accumulated return | Vending-Bench 2 [S15] | Basis: long-horizon business outcome. |
| Delta or gain score | Use only if official docs compute improvement/gain; no inventory example verified. | Basis: mark absent if not reported. |
| Aggregated suite score | FACTS Benchmark Suite [S16] | Basis: suite-level score combines components. |
| Cost-adjusted score | ARC-AGI-2 cost-aware reporting [S02] | Basis: cost must be part of official score/report. |
| Calibration or uncertainty score | HLE confidence/calibration outputs [S01] | Basis: confidence is collected and interpreted. |
| Percentile or normalized score | Artificial Analysis comparative model ranking if normalized [S04] | Basis: cite methodology for normalization. |
| Threshold or decision index | ARC-AGI-2 human-level threshold claims if stated [S02] | Basis: threshold requires official definition. |

### 3.4 Score Transformation

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| No transformation | GPQA accuracy [S03] | Basis: direct percent correct. |
| Linear transformation | Use if official score rescales raw score linearly; no direct inventory example verified. | Basis: cite formula. |
| Non-linear transformation | Elo-style outside benchmark if documented | Basis: no verified inventory example. |
| Normalization against a reference point used to interpret scores | Artificial Analysis model indexes if methodology normalizes [S04] | Basis: cite reference point. |
| Weighting across subdomains | MMMU-Pro if aggregate weights subdomains [S06] | Basis: record exact weights. |
| Weighting across capability domains | FACTS suite aggregation if component weighting exists [S16] | Basis: cite aggregation rule. |
| Formula for combining item, task-family, or subscore results documented | ARC-AGI-2 exact score/cost formulas [S02] | Basis: formula is documented. |
| Formula for combining item, task-family, or subscore results partially documented | HLE aggregate results if scorer path public but exact replication conditions incomplete [S01] | Basis: partial formulas require caveat. |
| Formula for combining item, task-family, or subscore results not documented | AIME 2025 hosted slice if score formula not exposed beyond leaderboard [S04] | Basis: mark missing formula. |
| Domain aggregation caveats documented | HLE caveats about what aggregate does not show [S01] | Basis: aggregate caveats protect interpretation. |
| Not applicable | Single-metric exact-match benchmark with no transformation, if documented | Basis: use only when no transformation exists. |

### 3.5 Documented Reference Groups, Baselines, and Comparators

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| No reference point or documented comparison group used to interpret scores | Dataset-only releases with no baselines | Basis: absence of baselines is descriptive. |
| Expected performance from random guessing or trivial selection | GPQA multiple-choice chance baseline [S03] | Basis: chance level interprets difficulty. |
| Performance from human participants under documented conditions | ARC-AGI-2 human testing [S02] | Basis: human baseline supports difficulty claims. |
| Performance from qualified domain experts | GPQA expert validation [S03] | Basis: expert reference group aligns with science domain. |
| Contest human population under source-instrument conditions | AIME contest population [S04] | Basis: source contest conditions are not the same as LLM eval conditions. |
| Professional annotator or expert validator | HLE expert contributors/validators [S01] | Basis: record role in task construction or scoring. |
| Performance from a reference model used to interpret scores | HLE frontier model cohort [S01] | Basis: model baseline contextualizes scores. |
| Previous model cohort | Artificial Analysis historical model evaluations [S04] | Basis: prior cohort supports longitudinal comparison if conditions match. |
| Commercial system used as a documented comparison point | HLE reported commercial frontier systems [S01] | Basis: cite model versions and dates. |
| Open-weight model used as a documented comparison point | ARC-AGI-2 local/open solver results where documented [S02] | Basis: open-weight/local comparisons need matched conditions. |
| Domain-specific reference group | GPQA domain experts [S03] | Basis: reference group should match target expertise. |
| Public/private split comparator | ARC-AGI-2 public/private forms [S02] | Basis: comparator affects leakage and equivalence. |
| Suite component comparator | FACTS suite components [S16] | Basis: components should not be collapsed without caveats. |
| Tool-enabled versus no-tool comparator | tau2-bench or ARC solver/tool comparisons where documented [S14, S02] | Basis: tool condition changes construct. |

### 3.6 Score Uncertainty and Stability

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Reported ranges expressing uncertainty around a score or comparison | Use where official leaderboard reports intervals; verify per source. | Basis: cite interval method. |
| Standard errors | Use where benchmark reports standard errors; no direct inventory example verified. | Basis: do not infer SE from sample size. |
| Bootstrap intervals | Use where official method reports bootstrap intervals; no direct inventory example verified. | Basis: cite method. |
| Hierarchical, clustered, or item-level bootstrap intervals | Use only if officially reported; no inventory example verified. | Basis: specialized uncertainty method. |
| Per-split or per-subscore confidence intervals | FACTS/Kaggle or suite reports if intervals exist [S16] | Basis: cite exact report. |
| Public/private split intervals | ARC-AGI-2 if split intervals are reported [S02] | Basis: mark gap if split comparability lacks uncertainty. |
| Small-sample sensitivity | GPQA Diamond subset if discussed [S03] | Basis: small expert item sets need sensitivity caveat. |
| Multiple runs or seeds | HLE if repeated runs/settings are documented [S01] | Basis: if missing, state gap. |
| Statistics on consistency across judges | HLE model/human judge validation if reported [S01] | Basis: judge consistency affects score precision. |
| Evidence that human or expert scorers apply rubrics consistently | GPQA/HLE expert validation [S03, S01] | Basis: record reliability evidence, not just expert status. |
| Sensitivity analyses | HLE/ARC prompt or format sensitivity if reported [S01, S02] | Basis: mark missing if not examined. |
| Score changes caused by prompt wording, small input changes, ordering, phrasing, format, or response schema | MMMU-Pro or HLE if variant sensitivity is documented [S06, S01] | Basis: input format sensitivity is part of score interpretation. |
| IRT, adaptive testing, or item-parameter precision estimates | Use only if official psychometric model is reported; no inventory example verified. | Basis: do not add IRT language without evidence. |
| Not reported | Many leaderboard-only slices, including some AIME 2025 displays [S04] | Basis: state uncertainty absence descriptively. |

### 3.7 Documented Metric Rationale and Stated Score Interpretation

| Field | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Why the primary rule or quantity was chosen | ARC-AGI-2 exact grid success [S02] | Basis: exact rule follows task definition. |
| Whether lower or upper limits are documented | AIME score has bounded item count [S04] | Basis: bounds help interpret score. |
| Whether possible non-target rewarded behavior is identified | HLE warns against broader AGI inference [S01] | Basis: caveats identify non-target interpretation. |
| Whether parser, judge, or scorer validation is documented | HLE judge validation should be recorded if present [S01] | Gap: incomplete validation affects Part B. |
| Whether response-format burden is separated from target capability | ARC-AGI-2 exact JSON/grid output [S02] | Basis: format burden may confound reasoning score. |
| Whether prompt/input variation affects interpretation | MMMU-Pro/HLE variants if documented [S06, S01] | Basis: sensitivity belongs in uncertainty/validity later. |
| Whether score uncertainty affects interpretation | ARC-AGI-2 rankings if uncertainty not reported [S02] | Basis: close ranks require uncertainty caution. |
| Whether score differences are interpreted statistically | Use if official report tests differences; otherwise mark gap. | Basis: absence limits fine-grained comparison. |
| Whether score or subscore interpretations link to capability domains | MMMU-Pro categories [S06] | Basis: link domain labels to actual tasks. |
| Whether aggregate score interpretations preserve caveats | FACTS suite aggregation [S16] | Basis: suite scores need component caveats. |
| Whether reports state what users should not infer | HLE AGI/autonomy caveats [S01] | Basis: non-inference statements constrain use. |

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Public leaderboard available | ARC Prize leaderboard [S02] | Basis: leaderboard is public. |
| Public aggregate scores available | HLE public paper/repo results [S01] | Basis: aggregate model scores are reported. |
| Public capability-domain scores or profiles available | MMMU-Pro domain scores [S06] | Basis: domain profile supports capability analysis. |
| Public per-item scores available | Use only if released; no broad inventory example verified. | Basis: mark absent if only aggregate is public. |
| Public model responses, traces, logs, judge rationales, or per-item data available | Terminal-Bench may expose logs for local runs [S12] | Basis: distinguish official published runs from user-generated local logs. |
| Public traces or logs available | Terminal-Bench local run logs [S12] | Basis: logs support reproducibility if retained. |
| Leaderboard snapshot or export available | Artificial Analysis evaluation pages [S04] | Basis: snapshot/export should include date. |
| Submission metadata available | ARC Prize leaderboard [S02] | Basis: model/config metadata supports interpretation. |
| Evaluation date or cohort labels available | HLE-Rolling [S01] | Basis: rolling score must include date/cohort. |
| Public/private split scores available | ARC-AGI-2 split reports if documented [S02] | Basis: split score supports leakage/comparability review. |
| Confidence intervals or error bars available | Use if official reports intervals; no general inventory example verified. | Basis: absence is a reporting gap. |
| Raw submissions available under controlled access | FACTS/Kaggle if controlled audit route exists [S16] | Basis: record access route and restrictions. |
| Retired-item or post-evaluation releases available | HLE-Rolling changes if retired items are released [S01] | Basis: distinguish changelog from retired-item archive. |
| Private reports available only to submitters | Hosted platforms such as Kaggle may give submitter reports [S16] | Basis: record private report access if documented. |
| No formal report or leaderboard documented | Dataset-only release with no reporting surface | Basis: mark absence descriptively. |

### 4.2 Output Name or Description

| Output example | Description | Review comment example |
| :------------- | :---------- | :--------------------- |
| ARC Prize leaderboard [S02] | Public ranked result surface | Basis: output is maintained by ARC Prize; cite date. |
| FACTS Kaggle benchmark page [S16] | Hosted benchmark report/submission surface | Basis: output is platform-mediated; report governance separately. |
| HLE paper result tables [S01] | Static paper results | Basis: paper tables are reports even without dashboard. |

### 4.3 Output Design or Presentation

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Static text report | DeepMind FACTS blog/technical report [S16] | Basis: prose report explains benchmark. |
| Tables | HLE paper tables [S01] | Basis: model results shown in tables. |
| Graphs or visualizations | Artificial Analysis benchmark pages [S04] | Basis: public evaluator visualizes model scores. |
| Leaderboard | ARC Prize [S02] | Basis: ranking surface. |
| Interactive dashboard | ScreenSpot-Pro grounding leaderboard [S07] | Basis: interactive/public reporting page. |
| Downloadable CSV or JSON | Use if leaderboard exports data; verify per source. | Basis: export availability supports audit. |
| API output | Terminal-Bench/local harness outputs if exposed via CLI/API [S12] | Basis: mark exact output route. |
| Paper-only results | GPQA paper if no leaderboard for the reviewed entity [S03] | Basis: report surface is paper tables only. |

### 4.4 Output Structure

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Aggregate-score based | GPQA accuracy [S03] | Basis: aggregate percent correct. |
| Capability-domain based | MMMU-Pro subject domains [S06] | Basis: scores linked to domains. |
| Capability-domain profile based | FACTS suite component profile [S16] | Basis: multiple components form profile. |
| Task-family based | Terminal-Bench task groups [S12] | Basis: task families organize results. |
| Criterion-threshold based | AIME or ARC threshold/human-level claims if stated [S04, S02] | Basis: threshold requires explicit definition. |
| Pairwise-comparison based | Use outside preference benchmark if official. | Basis: no verified inventory example. |
| Rank based | ARC leaderboard [S02] | Basis: systems are ordered. |
| Cost or efficiency adjusted | ARC-AGI-2 cost framing [S02] | Basis: cost/efficiency is part of report. |
| Error-analysis based | OmniDocBench error/category metrics if documented [S09] | Basis: include only official error categories. |
| Trace or process based | Terminal-Bench logs/traces [S12] | Basis: process evidence reported. |
| Suite-aggregate based | FACTS suite [S16] | Basis: suite score combines components. |
| Split or cohort based | ARC-AGI-2 public/private or HLE-Rolling cohorts [S02, S01] | Basis: split/cohort labels affect interpretation. |
| Version-window based | MRCR v2 slice [S20] | Basis: version/slice is part of report. |
| Environment-episode based | Vending-Bench 2 [S15] | Basis: episode outcomes are reported. |
| Difficulty-band based | ARC-AGI-2 or MathArena difficulty levels if documented [S02, S05] | Basis: difficulty labels should be official. |

### 4.5 Sensitivity to Context

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| One output format for all contexts | GPQA paper accuracy [S03] | Basis: same report format for all users. |
| User-definable output contexts | Local Terminal-Bench runs can generate user-specific logs/reports [S12] | Basis: local output may vary by user configuration. |
| Pre-defined versions adapted to audience or use | HLE paper, dataset card, repo, and rolling dashboard [S01] | Basis: different outputs serve different audiences. |
| Context sensitivity not documented | AIME 2025 evaluator page if audience/report context is not specified [S04] | Basis: mark missing rather than infer. |

### 4.6 Development of Outputs

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Based on benchmark authors' design | HLE paper/repository outputs [S01] | Basis: authors define scoring/reporting. |
| Based on empirical or actuarial relationships | ARC-AGI-2 human/model calibration if empirically used [S02] | Basis: cite empirical relationship. |
| Based on expert judgment | GPQA expert validation [S03] | Basis: experts shape item quality and interpretation. |
| Based on human annotation | OmniDocBench annotations [S09] | Basis: annotated ground truth supports scoring. |
| Based on outputs scored by another model | HLE model judge [S01] | Basis: model-generated judgment affects output. |
| Automatically generated by benchmark platform | Kaggle FACTS or Artificial Analysis [S16, S04] | Basis: hosted platform produces reports. |

### 4.7 Modifiability

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Not modifiable | Official paper result tables [S01] | Basis: static report cannot be customized. |
| Limited modification by submitter or user | Kaggle/leaderboard submissions [S16] | Basis: user submits model but platform controls report. |
| Fully user-generated reports possible | Local Terminal-Bench runs [S12] | Basis: user can generate local logs/reports. |
| Not documented | A hosted slice with no report customization statement [S04] | Basis: mark missing. |

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Clear linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels | ARC-AGI-2 exact grid task to success score [S02] | Basis: task, score, and reported label align. |
| Partial linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels | HLE academic aggregate to broad title-level interpretation [S01] | Basis: linkage is clear for closed-ended academic questions but not broad AGI. |
| Linkage is not obvious from available documentation | AIME 2025 hosted slice if methodology omits prompt/scorer details [S04] | Basis: report label may exceed visible method. |
| Mixture of clear and concealed linkage | FACTS public components plus private/held-out hosted scoring [S16] | Basis: some component links public, others controlled. |
| Not documented | Dataset/report with no score-to-claim explanation | Basis: state gap. |

### 4.9 Output Content

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Capability-domain descriptions or profiles | MMMU-Pro [S06] | Basis: reports domains/categories. |
| Aggregate rankings | ARC leaderboard [S02] | Basis: rank order shown. |
| Subdomain comparisons | HLE category results [S01] | Basis: category scores compare domains. |
| Capability-domain coverage map | FACTS suite components [S16] | Basis: suite component map supports coverage description. |
| Excluded-domain caveats | HLE AGI/autonomy caveats [S01] | Basis: reports what not to infer. |
| Aggregate-score warnings | HLE caveats [S01] | Basis: aggregate warnings reduce overclaim. |
| Error categories | OmniDocBench document parsing errors if documented [S09] | Basis: error categories support diagnosis. |
| Examples of successes or failures | ARC-AGI-2 sample tasks [S02] | Basis: examples contextualize score. |
| Cost, latency, or efficiency data | ARC-AGI-2 cost framing [S02] | Basis: cost/efficiency content included. |
| Process traces | Terminal-Bench logs [S12] | Basis: process data supports audit. |
| Recommendations or interpretation notes | FACTS blog/report [S16] | Basis: public notes guide use. |
| Warnings or caveats | HLE, ARC-AGI-2 [S01, S02] | Basis: caveats should be preserved in review. |

### 4.10 Intended Recipients

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Benchmark maintainers | ARC Prize [S02] | Basis: maintainers use results and feedback. |
| Model developers | SWE-Bench Verified [S13] | Basis: developers assess coding agents. |
| AI researchers | GPQA/MMMU-Pro [S03, S06] | Basis: academic benchmark audiences. |
| Safety evaluators | HLE/FACTS [S01, S16] | Basis: relevant to capability/factuality evaluation with caveats. |
| Policy or governance actors | FACTS/HLE public-facing reports [S16, S01] | Basis: use only with interpretation limits. |
| Product or deployment teams | FACTS factuality suite if product relevance is stated [S16] | Basis: mark cautiously. |
| Procurement teams | No verified inventory benchmark explicitly targets procurement. | Basis: do not infer procurement use from rankings. |
| Public audience | ARC Prize and Artificial Analysis leaderboards [S02, S04] | Basis: public pages are accessible to non-experts. |

## Section 5. Benchmark Access, Artifacts, and Lifecycle

### 5.1 Documentation and User Materials

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Technical report | ARC-AGI-2 technical report [S02] | Basis: technical report provides formal rationale and method details. |
| User guide | SWE-Bench dataset guide [S13] | Basis: guide helps users select and run splits. |
| Repository README | Terminal-Bench GitHub README [S12] | Basis: README is a primary quick-start and usage artifact. |
| API documentation | tau2-bench tool/API documentation if included in official docs [S14] | Basis: API docs define tool-call semantics. |
| Dataset card | HLE Hugging Face dataset card [S01] | Basis: dataset card records access terms and task distribution. |
| Model submission instructions | ARC Prize or Kaggle FACTS submission instructions [S02, S16] | Basis: submission rules define valid leaderboard entries. |
| Scoring documentation | SWE-Bench scoring docs [S13] | Basis: scoring documentation maps outputs to pass/fail. |
| Rubric or annotation guide | HLE expert/judge rubric documentation [S01] | Basis: rubric describes how answers are accepted or judged. |
| Evaluation examples | ARC-AGI-2 sample tasks [S02] | Basis: examples clarify task and output format. |
| FAQ or discussion forum | Benchmark issue tracker or forum if official [S02] | Basis: support material should be official or maintainer-linked. |
| Changelog or release notes | ARC-AGI-2 changelog [S02] | Basis: changelog documents changes affecting comparability. |

### 5.2 Distribution and Access Model

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Fully public materials | ARC-AGI-2 public repository tasks [S02] | Basis: public task data available; hidden sets separate. |
| Public materials with restricted answer keys or hidden tests | ARC-AGI-2 public plus hidden/private evaluation [S02] | Basis: public materials do not exhaust reviewed forms. |
| Controlled-access dataset or task host | HLE Hugging Face access acknowledgement [S01] | Basis: dataset access terms constrain use. |
| Private or held-out evaluation service | FACTS/Kaggle hosted benchmark [S16] | Basis: hosted/held-out route controls score generation. |
| Hosted scoring service | Artificial Analysis AIME 2025 [S04] | Basis: evaluator scores models. |
| Leaderboard-only submission route | ARC Prize leaderboard/competition [S02] | Basis: official score route may be leaderboard submission. |
| Benchmark registry or task-pack distribution | Terminal-Bench Harbor registry [S12] | Basis: task-pack distributed via registry. |
| Competition or challenge distribution | ARC Prize/Kaggle [S02] | Basis: competition rules affect access. |
| Private maintainer-mediated distribution | Use where maintainers manually grant data; no direct inventory example verified. | Basis: record access gate. |
| Retired or archived materials available | ARC changelog/old tasks if archived [S02] | Basis: retired access must be documented. |
| Access model not documented | LiveCodeBench Pro public code/docs limitations [S11] | Basis: mark missing for exact public access route. |

### 5.3 Methods of Publication

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Academic paper | GPQA [S03] | Basis: arXiv/source paper. |
| Benchmark website | Video-MMMU [S10] | Basis: official project site. |
| Git repository | Terminal-Bench [S12] | Basis: code/tasks on GitHub. |
| Package registry | Use if official package is distributed; no direct inventory example verified. | Basis: cite package name/version. |
| Dataset hosting platform | HLE Hugging Face [S01] | Basis: dataset hosted publicly with terms. |
| Leaderboard platform | ScreenSpot-Pro leaderboard [S07] | Basis: public ranking platform. |
| Hosted evaluation service | FACTS Kaggle [S16] | Basis: platform runs/hosts benchmark. |
| Benchmark registry | Terminal-Bench Harbor registry [S12] | Basis: registry identifies task pack. |
| Kaggle or leaderboard platform | FACTS Kaggle [S16] | Basis: Kaggle benchmark route. |
| Contest organizer source | MAA AIME [S04] | Basis: contest organizer is source of human instrument. |
| Controlled-access data host | HLE Hugging Face access gate [S01] | Basis: access requires acknowledgement. |
| Downloadable documents | DeepMind FACTS technical report PDF [S16] | Basis: official report is downloadable. |
| Private distribution | Use if private form exists; mark access details missing if not documented. | Basis: do not assume public access. |

### 5.4 User Requirements or Qualifications

| Requirement type | Benchmark example | Review comment example |
| :--------------- | :---------------- | :--------------------- |
| Technical skill | Terminal-Bench requires terminal/evaluation setup skill [S12] | Basis: technical competence affects responsible use. |
| Model access | HLE requires model/API access for evaluation [S01] | Basis: model route affects comparability. |
| Dataset access | HLE Hugging Face acknowledgement [S01] | Basis: access terms matter. |
| Compute or budget | ARC-AGI-2 cost/efficiency reporting [S02] | Basis: budget changes feasible comparisons. |
| Tool/API credentials | tau2-bench tools or HLE API [S14, S01] | Basis: credentials should be recorded. |
| Hosted submission or leaderboard account | Kaggle FACTS or ARC competition [S16, S02] | Basis: account eligibility affects access. |
| Human expertise | GPQA expert science validation [S03] | Basis: interpretation may require domain expertise. |
| Account, license, or competition eligibility | ARC Prize/Kaggle rules [S02, S16] | Basis: eligibility constraints affect who can submit. |
| Ethical, safety, or data-use obligations | HLE non-training terms [S01] | Basis: usage restrictions must be carried forward. |

### 5.5 Dataset and Item Access

| Component | Benchmark example | Review comment example |
| :-------- | :---------------- | :--------------------- |
| Training or development items | ARC-AGI-2 public training tasks [S02] | Basis: public train/dev items support practice but raise contamination risk. |
| Public evaluation items | HLE public 2,500 set [S01] | Basis: public evaluation items can be inspected. |
| Private or held-out evaluation items | ARC-AGI-2 private/hidden set [S02] | Basis: hidden items protect integrity but limit audit. |
| Secret, encrypted, or reserve evaluation items | FACTS held-out internal components if controlled [S16] | Basis: record if reserve exists; mark unknown if details absent. |
| Private leaderboard set | ARC Prize/Kaggle private sets [S02] | Basis: leaderboard set may be hidden. |
| Retired or archived evaluation items | HLE-Rolling or ARC changelog if retired items are public [S01, S02] | Basis: archive policy affects temporal comparison. |
| Answer keys or reference solutions | AIME answer keys/source contest [S04] | Basis: answer key status affects leakage. |
| Metadata or annotations | HLE item metadata [S01] | Basis: metadata supports domain/split analysis. |
| Human annotations or verification labels | OmniDocBench annotations [S09] | Basis: annotated ground truth supports scoring. |
| Raw model outputs or logs | Terminal-Bench local run logs [S12] | Basis: distinguish local logs from official raw outputs. |
| Model submissions and traces | ARC/Kaggle hosted submissions if available [S02, S16] | Basis: controlled traces support audit if accessible. |
| Hosted scoring service | Artificial Analysis AIME 2025 [S04] | Basis: hosted scorer may be public output without raw artifacts. |
| Simulator or environment state | Vending-Bench 2 [S15] | Basis: environment state is task artifact. |
| Task registry entry | Terminal-Bench 2.0 [S12] | Basis: registry entry is an access artifact. |
| Tool/API credentials or configuration | tau2-bench [S14] | Basis: tool configs can be restricted. |

### 5.6 Provenance and Contamination Documentation

| Topic | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Data origin or task creation | GPQA expert-written questions [S03] | Basis: creation route documented. |
| Source-material release date | AIME 2025 contest timing [S04] | Basis: source timing affects contamination. |
| Contest or problem-source timing | LiveCodeBench Pro recent contest sources [S11] | Basis: recency is central to contamination control. |
| Persistent dataset or benchmark-material identifier | HLE Hugging Face dataset [S01] | Basis: persistent host/citation supports traceability. |
| Author or contributor qualifications | HLE expert contributor model [S01] | Basis: qualifications support item quality review. |
| Deduplication or overlap checks | HLE searchability/contamination checks [S01] | Basis: record method and limits. |
| Rationale for public items and hidden or restricted evaluation items | ARC-AGI-2 hidden split rationale [S02] | Basis: hidden set supports integrity. |
| Screening for prior model exposure to benchmark items, answers, or sources | HLE canary and non-searchability checks [S01] | Basis: contamination controls matter for public items. |
| Canary strings or training-data warnings | HLE canary/non-training warnings [S01] | Basis: warning supports post-release monitoring. |
| Diagnostic task for performance driven by prior exposure to items or answers | Use if official benchmark includes contamination diagnostic; no direct inventory example verified. | Basis: mark gap if absent. |
| Pre-exposure or source-material searchability checks | HLE [S01] | Basis: searchability checks reduce leakage risk. |
| Public-source searchability | HLE [S01] | Basis: public searchability affects contamination. |
| Post-release contamination risk | Public HLE set [S01] | Basis: public release increases future exposure. |
| Training-use prohibition | HLE dataset terms [S01] | Basis: terms prohibit training/fine-tuning use. |
| Private-set owner | ARC Prize or FACTS/Kaggle owner [S02, S16] | Basis: private-set owner affects audit. |
| Leak response policy | ARC changelog/competition rules if specified [S02] | Basis: record policy or mark missing. |
| Rerun or replacement trigger | HLE-Rolling or ARC update rules [S01, S02] | Basis: trigger affects comparability. |
| Hash commitments, signatures, or tamper-evident audit logs | Use only if official cryptographic logs exist; no inventory example verified. | Basis: absence is an evidence gap, not defect. |
| Encrypted, secret, or controlled-release item reserve | FACTS held-out suite [S16] | Basis: controlled release supports integrity but limits inspection. |
| Rules for updating, rotating, replacing, or adding benchmark items over time | HLE-Rolling changes [S01] | Basis: update policy affects longitudinal use. |
| Reporting of known unintended disclosures or deprecated/archived items | ARC changelog [S02] | Basis: public correction log supports maintenance review. |

### 5.7 Reproducibility Materials

| Option | Benchmark example | Review comment example |
| :----- | :---------------- | :--------------------- |
| Complete task data | ARC-AGI-2 public tasks [S02] | Basis: public task data supports reproduction for public split. |
| Complete prompt templates | HLE prompt templates [S01] | Basis: prompts define official run. |
| Code or platform that administers tasks, collects outputs, and often runs scoring | Terminal-Bench [S12] | Basis: runner administers tasks. |
| Scoring code | SWE-Bench repository [S13] | Basis: scoring code enables audit. |
| Environment file or dependency list | HLE requirements or Terminal-Bench setup [S01, S12] | Basis: dependencies affect reproducibility. |
| Container or reproducible environment | Terminal-Bench task environments [S12] | Basis: environment should be pinned. |
| Container image | Use if official image exists; verify per benchmark. | Basis: cite image/tag. |
| Task environment registry | Terminal-Bench Harbor registry [S12] | Basis: registry fixes task set. |
| Simulator or user simulator version | tau2-bench [S14] | Basis: simulator version affects results. |
| Evaluation adapter | Terminal-Bench provider adapters [S12] | Basis: adapters define model interface. |
| Judge model and prompt version | HLE model judge [S01] | Basis: judge version affects scores. |
| Version pinning | Terminal-Bench registry/version [S12] | Basis: pin tasks and dependencies. |
| Random seeds or deterministic settings | Use if official docs report seeds; mark missing otherwise. | Basis: seeds affect score stability. |
| Model responses, traces, logs, judge rationales, or per-item data | Terminal-Bench local logs [S12] | Basis: public official traces may still be absent. |
| Reproduction script for published results | HLE or Terminal-Bench scripts [S01, S12] | Basis: script should reproduce reported conditions, not just run tasks. |
| Push-button replication script or single documented command | Terminal-Bench CLI [S12] | Basis: single command improves usability. |
| Expected-output fixtures or smoke-test example | Terminal-Bench sample task [S12] | Basis: fixtures support implementation health. |
| Scorer fixtures | SWE-Bench test fixtures [S13] | Basis: scorer fixture validates grading path. |
| Known-good baseline run | ARC-AGI-2 random baseline/harness [S02] | Basis: baseline checks runner behavior. |
| Task-level expected outputs | ARC-AGI-2 reference grids [S02] | Basis: expected outputs support exact scoring. |
| Continuous integration or test suite | Terminal-Bench/SWE-Bench if repo CI exists [S12, S13] | Basis: CI supports harness health. |
| Public build status or equivalent passing-test signal | Repository CI badge if available [S12] | Basis: build status is a maintenance signal. |

### 5.8 Maintenance and Versioning

| Topic | Benchmark example | Review comment example |
| :---- | :---------------- | :--------------------- |
| Maintainer identity | ARC Prize / `arcprize` [S02] | Basis: maintainer is visible. |
| Private or held-out set owner | FACTS/DeepMind/Kaggle [S16] | Basis: owner should be named for audit. |
| Leaderboard operator | Artificial Analysis or ARC Prize [S04, S02] | Basis: operator may differ from benchmark creator. |
| Submission eligibility rules | Kaggle/ARC competition rules [S16, S02] | Basis: eligibility affects fair comparison. |
| Rerun policy | Hosted leaderboard rules if documented [S02, S16] | Basis: reruns affect stability. |
| Stale-score policy | HLE-Rolling or leaderboard policy [S01] | Basis: date-sensitive scores need stale-score handling. |
| Model-version update policy | Artificial Analysis methodology [S04] | Basis: model version drift affects results. |
| Scorer, judge, parser, or harness versioning | HLE judge/harness, SWE-Bench scorer [S01, S13] | Basis: scorer version should be recorded. |
| Cohort or evaluation-window labels | HLE-Rolling [S01] | Basis: cohort/window label protects temporal comparison. |
| Public/private score aggregation policy | ARC-AGI-2 split reports [S02] | Basis: aggregation across public/private should be explicit. |
| Retirement and archival policy | ARC/HLE changelog if documented [S02, S01] | Basis: missing policy is a lifecycle gap. |
| Documented release names, tags, changes, and score-comparability implications | Terminal-Bench 2.0 registry [S12] | Basis: version labels should say whether scores compare. |
| Changelog or update record | ARC-AGI-2 changelog [S02] | Basis: updates are inspectable. |
| Issue or feedback process | GitHub issues [S02, S12] | Basis: feedback process supports maintenance. |
| Item correction process | ARC changelog/corrections [S02] | Basis: corrections affect scores. |
| Deprecated item handling | HLE-Rolling or ARC if documented [S01, S02] | Basis: deprecated items require comparability notes. |
| Rules for updating, rotating, replacing, or adding hidden evaluation items over time | HLE-Rolling [S01] | Basis: hidden refresh policy should be explicit. |
| Last code-usability or harness health check | Repository CI/release status [S12] | Basis: record latest evidence, not assumption. |
| Build, CI, or smoke-test status | Terminal-Bench/SWE-Bench repository signals [S12, S13] | Basis: health signal supports artifact usability. |
| Score-ceiling threshold or criteria for deprecating, archiving, or ending use | ARC-AGI-2 if human/model ceiling criterion stated [S02] | Basis: retirement criteria prevent stale benchmark use. |
| Policy for deprecating, archiving, or ending use of items, versions, leaderboards, or the benchmark | HLE/ARC lifecycle docs if present [S01, S02] | Basis: mark missing if not documented. |
| Retired-item publication or audit policy | HLE-Rolling/ARC changelog if present [S01, S02] | Basis: audit policy supports transparency. |
| Score comparability across versions | MRCR v2 slice or Terminal-Bench 2.0 [S20, S12] | Basis: version comparison needs explicit policy. |
| Policy for comparing scores across dates, cohorts, refreshes, or rolling windows | HLE-Rolling [S01] | Basis: date/cohort comparison is a major interpretation risk. |
| Long-term archival plan | Repository/archive statement if present [S12] | Basis: archive plan supports future review. |

---

# Part B Rating Guide

Use the following scale examples as reviewer-comment patterns. Each Part B item listed after the scale has the same six rating choices: `n/a`, `0`, `1`, `2`, `3`, and `4`. The examples are illustrative evidence anchors, not final ratings.

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

### Section 6 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | AIME 2025 as an evaluator-specific slice, for an item about original item-development process if the review boundary excludes the MAA contest process [S04] | Basis: the slice reuses source contest items; this item is not attributable to the evaluator implementation. |
| 0 | LiveCodeBench Pro public entity, where exact standalone code/docs for the reviewed slice are not available [S11] | Basis: insufficient public documentation for the exact reviewed entity. Caution: evidence gap, not quality proof. |
| 1 | ARC-AGI-2 for broad AGI construct proportionality if grid tasks are treated as standalone AGI evidence [S02] | Basis: task family is narrower than broad claim. |
| 2 | HLE rationale for difficult closed-ended academic questions with incomplete scorer/reliability detail [S01] | Basis: rationale is usable but not complete for high-stakes interpretation. |
| 3 | GPQA Diamond expert-written science questions with clear source paper and dataset [S03] | Basis: development and purpose are well documented for a narrow expert-science construct. |
| 4 | FACTS suite where component rationale, release route, documentation, and interpretation limits are all inspected and complete for the reviewed use [S16] | Basis: use only if the reviewer verifies comprehensive source support. |

### Section 6 Rating-Item Coverage

For each item below, use the six Section 6 examples above and tailor the comment to the focus shown.

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 6.1.1 Rationale and construct definition | Does the benchmark define the claimed capability or quality clearly? |
| 6.1.2 Summary of prior research and benchmark context | Does it locate itself against prior benchmarks, source instruments, and known gaps? |
| 6.1.3 Phenomenon-task-metric-claim chain | Does it link target phenomenon, task, metric, and score claim? |
| 6.1.4 Task or item design | Are item/task formats justified for the intended construct? |
| 6.1.5 Procedures for developing task or item content | Are authoring, collection, filtering, review, and validation steps documented? |
| 6.1.6 Thoroughness of the final task or item selection process | Is final selection transparent enough to support score interpretation? |
| 6.1.7 Quantitative evidence of task or item quality | Are difficulty, discrimination, agreement, item quality, or filtering statistics reported? |
| 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice | Does the review explain how reused or sliced materials changed interpretation? |
| 6.1.9 Overall quality of rationale, development, and task or item quality | Synthesize 6.1 without mechanically averaging. |
| 6.2.1 Documentation of benchmark purpose and intended use | Are intended uses and non-uses visible to users? |
| 6.2.2 Documentation of development process | Can users inspect how tasks were produced and selected? |
| 6.2.3 Documentation of scoring and metrics | Can users understand scoring, parsing, aggregation, and failure handling? |
| 6.2.4 Documentation of reliability, stability, and uncertainty | Are repeat-run, scorer, prompt, and uncertainty issues documented? |
| 6.2.5 Documentation of validity evidence | Does documentation support claimed interpretations? |
| 6.2.6 Documentation of fair use and comparability | Are fair comparison and access constraints explained? |
| 6.2.7 Documentation of maintenance and versioning | Are releases, changes, archived items, and comparability policies documented? |
| 6.2.8 Adequacy of documentation available to users | Overall adequacy for target users. |
| 6.3.1 Evaluation setup and administration | Can users reproduce official administration conditions? |
| 6.3.2 Scoring procedure and error handling | Are scoring errors, malformed outputs, refusals, and retries handled? |
| 6.3.3 Interpretation and reporting guidance | Does documentation say what scores mean and do not mean? |
| 6.3.4 Restrictions, prerequisites, and appropriate use | Are prerequisites and non-use cases explicit? |
| 6.3.5 Technical support and implementation guidance | Are setup, dependencies, examples, and support routes usable? |
| 6.3.6 References and supporting materials | Are citations, docs, appendices, datasets, and repositories linked? |
| 6.3.7 Quality of procedural instructions | Overall procedural usability. |
| 6.4 Overall adequacy of rationale and documentation | Integrate Section 6 evidence and gaps. |

## Section 7. Quality and Usability of Benchmark Artifacts

### Section 7 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A paper-only theoretical benchmark proposal with no runnable artifacts, if artifact use is outside review boundary | Basis: artifact usability is not applicable only when no artifact is part of intended use. |
| 0 | A hosted-only slice with no accessible tasks, prompts, scoring guide, or audit route | Basis: artifacts cannot be inspected or used. |
| 1 | LiveCodeBench Pro if public implementation materials are too limited for the exact Pro entity [S11] | Basis: public artifact support is weak for reproduction. |
| 2 | HLE public data/repo with incomplete raw-output and exact replication artifacts [S01] | Basis: usable, but substantial audit gaps remain. |
| 3 | Terminal-Bench public repo plus registry and runnable workflow [S12] | Basis: artifacts are usable and mostly reproducible. |
| 4 | SWE-Bench Verified when dataset, docs, harness, tests, and versioned split are all available and verified [S13] | Basis: comprehensive artifact chain supports audit. |

### Section 7 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 7.1.1 Dataset, task set, or evaluation environment availability | Can the reviewed task data/environment be accessed or audited? |
| 7.1.2 Prompts, instructions, and input artifacts | Are prompts, screenshots, videos, documents, files, and inputs available or controlled? |
| 7.1.3 Rubrics, reference answers, and response format requirements | Are answer keys, rubrics, schemas, and admissible variants clear? |
| 7.1.4 Evaluation harness, scorer, and implementation quality | Is the runner/scorer documented, versioned, tested, and robust? |
| 7.1.5 Interface and workflow usability | Can intended users actually run or submit evaluations? |
| 7.1.6 Accessibility across modalities, languages, and system types | Are modality/language/access constraints documented and manageable? |
| 7.1.7 Licensing, use requirements, and risk warnings | Are legal, data-use, and safety conditions clear? |
| 7.1.8 Overall quality of benchmark artifacts | Synthesize artifact completeness and usability. |

## Section 8. Baselines, Comparators, and Reference Interpretation

### Section 8 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A benchmark used only as an internal regression smoke test with no score interpretation beyond pass/fail | Basis: reference interpretation may not apply if no comparative claim is made. |
| 0 | Dataset-only release with no baseline, comparator, chance level, or score interpretation | Basis: scores lack usable reference context. |
| 1 | AIME 2025 hosted model ranking if contest-human conditions are used as comparator without adaptation caveats [S04] | Basis: source contest population is mismatched to AI-evaluation conditions. |
| 2 | HLE with frontier model cohort but incomplete uncertainty and human-distribution detail [S01] | Basis: supports cautious comparison. |
| 3 | ARC-AGI-2 with random/human/model/cost context, while private governance still needs review [S02] | Basis: comparator context is strong for narrow ARC tasks. |
| 4 | GPQA Diamond if chance, expert, non-expert, and model comparators are all current and uncertainty-aware for the reviewed claim [S03] | Basis: comprehensive comparator evidence required. |

### Section 8 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 8.1.1 Random, chance, floor, and ceiling baselines | Are floor/chance/ceiling anchors documented and meaningful? |
| 8.1.2 Human or expert baselines | Are human/expert conditions, samples, and uncertainty documented? |
| 8.1.3 Model comparator cohort | Are compared models current, selected transparently, and evaluated comparably? |
| 8.1.4 Historical, version, or benchmark-family comparators | Can scores be compared across benchmark versions or source families? |
| 8.1.5 Criterion thresholds, score bands, or performance categories | Are bands/thresholds empirically or conceptually justified? |
| 8.1.6 Representativeness of reference groups | Do comparators represent the intended interpretation group? |
| 8.1.7 Currency and maintenance of baseline evidence | Are baselines refreshed or dated appropriately? |
| 8.2 Overall adequacy of baselines and reference interpretation | Synthesize reference evidence without averaging. |

## Section 9. Reliability, Precision, and Score Stability

### Section 9 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A deterministic exact-match dataset inspected only for artifact inventory, not score use | Basis: reliability rating may be outside scope only if no score interpretation is reviewed. |
| 0 | A leaderboard-only slice with no uncertainty, repeated runs, scorer reliability, or run conditions [S04] | Basis: no usable reliability evidence. |
| 1 | HLE if model-judge/parser reliability and repeat-run variance are incomplete for fine-grained rankings [S01] | Basis: evidence is insufficient for precise comparisons. |
| 2 | ARC-AGI-2 exact scoring with remaining prompt/attempt/private-form comparability gaps [S02] | Basis: deterministic scoring helps, but stability evidence remains partial. |
| 3 | SWE-Bench Verified with deterministic tests and curated tasks, while dependency drift remains monitored [S13] | Basis: major variation sources mostly controlled. |
| 4 | Terminal-Bench task pack if seeds, containers, retries, logs, scorer versions, and uncertainty are all documented [S12] | Basis: comprehensive stability evidence required. |

### Section 9 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 9.1.1 Coverage of reliability and stability evidence | Does the benchmark cover relevant reliability sources? |
| 9.2.1 Run-to-run stability, seeds, and sampling settings | Are stochastic settings and repeated-run evidence documented? |
| 9.2.2 Score uncertainty, confidence intervals, or standard errors | Are uncertainty estimates supplied and interpreted? |
| 9.3.1 Automated scorer or parser reliability | Are automated scorers/parsers tested against expected outputs? |
| 9.3.2 Human rater or expert scorer agreement | Are human/expert ratings consistent and documented? |
| 9.3.3 Model-as-judge reliability and validity checks | Is model judge agreement/bias/robustness validated? |
| 9.4.1 Prompt, instruction, or formatting sensitivity | Are official prompts and sensitivity to variants documented? |
| 9.4.2 Form, split, version, or refresh equivalence | Are forms and versions comparable or clearly non-comparable? |
| 9.4.3 Execution environment and dependency stability | Are environments, dependencies, and external services stable? |
| 9.5.1 Meaningfulness of score differences | Are close score differences statistically or practically interpretable? |
| 9.6 Overall reliability, precision, and score stability | Synthesize precision and stability threats. |

## Section 10. Validity Evidence

### Section 10 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A Section 10.6.2 AGI item for a benchmark that makes no broad intelligence, agency, or autonomy claim | Basis: broad-claim item is not applicable if no broad claim is made. |
| 0 | Dataset-only release with no validity argument or score interpretation | Basis: no usable validity evidence. |
| 1 | ARC-AGI-2 as standalone AGI proof [S02] | Basis: broad claim exceeds grid-task evidence. |
| 2 | HLE for closed-ended academic capability, with scorer/reliability/ecological gaps [S01] | Basis: supports limited interpretation. |
| 3 | GPQA Diamond for graduate-level science QA with expert filtering and comparator evidence [S03] | Basis: multiple validity sources support a bounded construct. |
| 4 | FACTS if each component documents phenomenon, tasks, scoring, leakage controls, uncertainty, and claim limits [S16] | Basis: comprehensive validity chain required. |

### Section 10 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 10.1.1 Content validity and task representativeness | Do tasks represent the claimed capability space? |
| 10.1.2 Construct breadth and capability-domain coverage | Does coverage match broad or domain claims? |
| 10.2.1 Internal structure, subscores, or dimensionality | Are subscores/dimensions empirically or theoretically justified? |
| 10.2.2 Item or task behavior across the score scale | Do items behave sensibly across difficulty/performance levels? |
| 10.2.3 Failure modes and error analysis | Are errors analyzed for construct-relevant vs irrelevant causes? |
| 10.3.1 Metric, scorer, and aggregation validity | Does the metric reward the intended capability? |
| 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance | Are shortcuts, format artifacts, leakage, and tuning risks controlled? |
| 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings | Do external relations support the interpretation? |
| 10.4.2 Convergent and discriminant evidence | Does the benchmark correlate with related constructs and separate unrelated ones? |
| 10.4.3 Ecological or predictive relevance | Do scores predict or resemble relevant real-world tasks? |
| 10.5.1 Contamination and leakage controls | Are exposure, leakage, private sets, canaries, and release rules adequate? |
| 10.5.2 Gameability and benchmark-specific tuning controls | Are public-set gaming and benchmark-specific optimization addressed? |
| 10.6.1 Proportionality of stated benchmark claims | Are public claims no broader than evidence? |
| 10.6.2 Broad intelligence, AGI, agency, or autonomy claims | Is there breadth/depth evidence for broad claims, or explicit caveats? |
| 10.7 Overall validity support | Synthesize validity support and major threats. |

## Section 11. Fair Use, Comparability, and Appropriate Use

### Section 11 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A narrow internal engineering smoke test with no cross-system or public-use claim | Basis: fair-use review may be outside scope if no comparative use exists. |
| 0 | Public leaderboard with no rules, model identity policy, access terms, or caveats | Basis: no usable comparability information. |
| 1 | AIME 2025 slice if model rankings omit prompt/scorer/version conditions [S04] | Basis: comparison risks are high if conditions are opaque. |
| 2 | HLE for frontier API-model research comparison with access, language, and raw-output gaps [S01] | Basis: cautious use supported, broader use constrained. |
| 3 | ARC-AGI-2 for matched technical competition conditions with hidden-set and cost caveats [S02] | Basis: fair comparison mostly supported in intended context. |
| 4 | MMMLU or Global PIQA if language/cultural coverage, translation method, subgroup validity, and use limits are comprehensively documented [S18, S19] | Basis: comprehensive fairness and coverage evidence required. |

### Section 11 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 11.1.1 Relevance of the construct across systems, groups, and contexts | Is the claimed construct relevant across intended systems and contexts? |
| 11.1.2 Documentation of fair-use considerations | Are fairness, accessibility, bias, language, and modality issues documented? |
| 11.2.1 Inclusive and accessible benchmark design | Are unnecessary exclusions avoided or justified? |
| 11.2.2 Domain, language, modality, and subgroup coverage | Is coverage analyzed and tied to score interpretation? |
| 11.3.1 Cross-system comparability | Are prompts, tools, time, access, hardware, and policies matched or caveated? |
| 11.3.2 Access, compute, tooling, and API or local comparability | Are access and compute differences documented and managed? |
| 11.3.3 Temporal comparability for rolling or live benchmarks | Are dates, cohorts, stale scores, and refresh rules clear? |
| 11.4.1 Differential performance or bias analysis | Are performance differences or judge/scorer biases analyzed? |
| 11.4.2 Reliability and validity across relevant subgroups or contexts | Are reliability/validity checked across groups, domains, languages, or modalities? |
| 11.5.1 Appropriate-use guidance and non-use cases | Are supported and unsupported uses explicit? |
| 11.5.2 Release rules and sensitive-content handling | Are release, privacy, safety, and refresh practices responsible? |
| 11.6 Overall fair use, comparability, and appropriate use | Synthesize fair-use evidence and caveats. |

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### Section 12 Rating Examples

| Rating | Benchmark example | Short review-comment justification |
| :----- | :---------------- | :--------------------------------- |
| n/a | A private artifact audit with no report, leaderboard, dashboard, scorecard, or public claim in scope | Basis: report quality item may not apply. |
| 0 | Dataset-only release with no score report, leaderboard, or interpretation guidance | Basis: no usable report surface. |
| 1 | Public leaderboard that ranks models without version/date/condition labels | Basis: reporting likely supports unsupported interpretation. |
| 2 | HLE reports with useful tables and caveats but incomplete uncertainty/raw-output traceability [S01] | Basis: cautious use supported. |
| 3 | ARC-AGI-2 reporting ecosystem with official site, leaderboard, repo, and changelog, while private governance needs detail [S02] | Basis: mostly traceable reporting. |
| 4 | FACTS/Kaggle suite if report surfaces include versions, raw/audit route, uncertainty, component caveats, and governance rules [S16] | Basis: comprehensive reporting required. |

### Section 12 Rating-Item Coverage

| Rating item | Review-comment focus |
| :---------- | :------------------- |
| 12.1.1 Report, leaderboard, dashboard, or result artifact scope | Are relevant scores, subscores, profiles, and traces covered? |
| 12.1.2 Score granularity and level of detail | Is granularity justified by precision and task coverage? |
| 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling | Are versions, dates, settings, uncertainty, and comparability labels visible? |
| 12.2.2 Reproducibility and traceability of reported scores | Can reported scores be traced to runs, configs, scorers, and data versions? |
| 12.3.1 Linkage from scores to interpretations and public claims | Do reports state what scores support and do not support? |
| 12.3.2 Raw outputs, per-item data, or trace availability | Are outputs/traces available or access-controlled for audit? |
| 12.4.1 Fairness and freedom from bias in reports | Do reports avoid misleading language and identify coverage limits? |
| 12.4.2 Acceptability and usability for intended audiences | Are reports understandable and appropriately detailed for users? |
| 12.4.3 Public communication and leaderboard governance | Are submission rules, ranking policy, stale-score policy, and public claim rules clear? |
| 12.5 Overall quality of reports, leaderboards, dashboards, and public claims | Synthesize reporting evidence and public-claim risk. |

### Section 12 Leaderboard Governance Fields

| Governance topic | Benchmark example | Review comment example |
| :--------------- | :---------------- | :--------------------- |
| Leaderboard operator | ARC Prize [S02] | Basis: operator controls score surface. |
| Submission route | Kaggle FACTS [S16] | Basis: route determines access and scoring. |
| Submission eligibility and tool-use rules | ARC Prize/Kaggle rules [S02, S16] | Basis: rules affect fairness. |
| Model identity and version policy | Artificial Analysis methodology [S04] | Basis: version identity affects rank interpretation. |
| Evaluation date and cohort/window label | HLE-Rolling [S01] | Basis: rolling scores need date/cohort. |
| Prompt, scorer, judge, parser, or harness version | HLE judge/harness [S01] | Basis: scorer version affects score. |
| Public/private split reporting | ARC-AGI-2 [S02] | Basis: split reporting affects leakage and comparability. |
| Private-set owner or audit route | FACTS/Kaggle [S16] | Basis: private owner/audit route supports trust. |
| Rerun, challenge, or appeal policy | Competition platforms if documented [S02, S16] | Basis: rerun rules affect score stability. |
| Stale-score policy | HLE-Rolling [S01] | Basis: old scores may not compare with new cohorts. |
| Ranking uncertainty or meaningful-difference guidance | Any leaderboard with intervals or significance guidance | Basis: absence limits rank interpretation. |
| Raw output, trace, or submission audit route | Terminal-Bench logs or Kaggle audit route [S12, S16] | Basis: audit route supports scrutiny. |
| Capability-domain claim limits | HLE caveats [S01] | Basis: public claims need limits. |
| Deprecation or archive policy | ARC/HLE changelog and archive policy if present [S02, S01] | Basis: deprecation supports lifecycle integrity. |
| Public claim, badge, or headline rules | Artificial Analysis or ARC public ranking rules [S04, S02] | Basis: public claims should preserve caveats. |

---

# Final Evaluation Guide

## Evaluative Report Of The Benchmark

Example pattern: `HLE is strongest as a content-driven benchmark for difficult closed-ended academic questions, with useful public artifacts and official caveats. Its main limitations for stronger claims are scorer validation, uncertainty, raw outputs, private-set transparency, and replication conditions` [S01].

Reviewer comment: Basis: summarize strongest support and most consequential gaps. Rationale: final report should identify what the reviewed entity can support, not whether the benchmark is generally good or bad.

## Conclusions

Example pattern: `ARC-AGI-2 can support cautious claims about exact-grid abstraction under ARC conditions; it should not be used alone as proof of AGI or broad cognitive versatility` [S02].

Reviewer comment: Basis: narrowest defensible interpretation first. Caution: explicitly state expertise required for responsible use.

## Recommendations

Example pattern: `For Terminal-Bench 2.0, report task-pack version, container/environment, model identity, tool permissions, run logs, scorer version, and date` [S12].

Reviewer comment: Basis: recommendations should name the affected entity or reporting surface and the evidence needed for stronger future review.

## Summary Of Ratings

Example pattern: For HLE, a reviewer might rate rationale higher than reliability if official content rationale is strong but repeat-run uncertainty and scorer validation are incomplete [S01].

Reviewer comment: Basis: summary ratings are evidence summaries, not a mechanical average.

## Gap Register

| Gap example | Affected entity or reporting surface | Why it matters | Needed for a higher rating |
| :---------- | :----------------------------------- | :------------- | :------------------------- |
| Raw model outputs and judge logs for published HLE runs are not public | HLE paper/repository reporting [S01] | Limits independent error analysis and scorer audit. | Public or controlled audit access with prompt, model, judge, and item metadata. |
| ARC-AGI-2 broad AGI language is broader than exact-grid task evidence | ARC-AGI-2 public reports [S02] | Risks overinterpreting narrow task success. | Explicit non-use guidance or broader validation portfolio. |
| AIME 2025 LLM slice depends on source contest plus evaluator methodology | Artificial Analysis AIME 2025 [S04] | Source contest validity does not automatically transfer to AI benchmark use. | Prompt, scorer, sampling, and score interpretation documentation for the evaluator slice. |
| Terminal-Bench task-pack comparisons can drift across versions | Terminal-Bench 2.0 registry [S12] | Version drift can make scores non-comparable. | Version-locking, stale-score rules, and archived task-pack policy. |

## Summary Of Ratings Row Examples

| Template row | Benchmark example | Review comment example |
| :----------- | :---------------- | :--------------------- |
| Section 6. Rationale, documentation, and task/item quality | GPQA Diamond [S03] | Basis: rate from construct rationale, item development, and documentation support. |
| Section 7. Benchmark materials and usability | Terminal-Bench 2.0 [S12] | Basis: rate from task artifacts, harness, setup, and audit usability. |
| Section 8. Reference points and documented comparison groups | ARC-AGI-2 [S02] | Basis: rate from human/model/random/cost comparator evidence. |
| Section 9. Reliability and precision | HLE [S01] | Basis: rate from uncertainty, scorer validation, and repeat-run evidence. |
| Section 10. Validity support | FACTS Benchmark Suite [S16] | Basis: rate from phenomenon-task-metric-claim chain and threat controls. |
| Section 11. Fair use and comparability | MMMLU or Global PIQA [S18, S19] | Basis: rate from language/cultural coverage and comparison limits. |
| Section 12. Reports, leaderboards, and public score claims | Artificial Analysis AIME 2025 [S04] | Basis: rate from report traceability, public ranking caveats, and governance. |

## Exact Long-Prompt Coverage Notes

These entries preserve long template labels that reviewers may want to search mechanically.

| Exact template label | Benchmark example | Review comment example |
| :------------------- | :---------------- | :--------------------- |
| Entity type, such as original benchmark, derived benchmark, subset, evaluation slice, hosted leaderboard, private form, rolling version, hosted suite, benchmark suite, task environment, or evaluator-specific implementation | AIME 2025 Artificial Analysis slice [S04] | Basis: label as evaluator-specific implementation, not the original MAA contest. |
| Parent or source benchmark, if any | SWE-Bench Verified parented to SWE-Bench [S13] | Basis: record parent family separately from curated subset. |
| Source instrument reused, if any, such as a human contest, dataset, task collection, or prior benchmark | AIME contest problems [S04] | Basis: source reuse changes interpretation. |
| Hosted evaluator, leaderboard, registry, or platform implementation, if distinct from benchmark authors | FACTS on Kaggle [S16] | Basis: platform implementation is distinct from source authorship. |
| Why the primary rule or quantity used to convert model behavior into a score was chosen | ARC-AGI-2 exact grid match [S02] | Basis: scoring rule follows exact output task definition. |
| Whether lower or upper limits of the score rule are documented | AIME bounded item count [S04] | Basis: score range constrains interpretation. |
| Whether documentation identifies possible non-target rewarded behavior | HLE broad-claim caveats [S01] | Basis: caveats identify what scores should not reward or imply. |
| Whether response-format burden is separated from the target capability | ARC-AGI-2 exact grid serialization [S02] | Basis: structured output burden can confound reasoning. |
| Whether score changes from small item or prompt changes affect the score interpretation | MMMU-Pro or HLE prompt variants if documented [S06, S01] | Basis: sensitivity affects score meaning. |
| Whether score or subscore interpretations are linked to capability domains from 2.1 | MMMU-Pro domain reports [S06] | Basis: labels should map to task domains. |
| Whether aggregate score interpretations preserve capability-domain caveats | FACTS suite components [S16] | Basis: aggregate suite reports should preserve component limits. |
| Whether benchmark reports state what users should not infer | HLE AGI/autonomy cautions [S01] | Basis: non-inference guidance limits overclaim. |
| Random guessing or trivial-selection reference point | GPQA chance baseline [S03] | Basis: chance supports minimum interpretation. |
| Human-participant performance under documented conditions | ARC-AGI-2 human testing [S02] | Basis: human baseline needs documented conditions. |
| Qualified domain-expert performance | GPQA expert performance [S03] | Basis: expert reference aligns with scientific domain. |
| Contest human population or source-instrument reference | AIME contest population [S04] | Basis: source contest population differs from AI evaluation setting. |
| Documented group of models used for comparison | HLE frontier model cohort [S01] | Basis: comparator cohort should include model versions and conditions. |
| Public/private split, suite-component, or tool/no-tool comparator | ARC-AGI-2 public/private forms [S02] | Basis: split/component comparisons need caveats. |
| Prior benchmark or version | ARC-AGI-1 to ARC-AGI-2 [S02] | Basis: prior version comparison requires version policy. |
| Score boundary or lower/upper reference point | AIME score bounds or ARC success ceiling [S04, S02] | Basis: boundaries help interpret score scale. |

---

# Coverage Checklist For Maintainers

- Part A Sections 1-5: this guide provides an example and review comment pattern for every table row, checkbox option, matrix topic, and governance-like field in the official template.
- Part B Sections 6-12: this guide provides six rating-choice examples per Part B section plus an item coverage row for every rating item in Sections 6-12.
- Final Evaluation: this guide includes examples for evaluative report, conclusions, recommendations, summary ratings, and gap-register rows.
- Outside-inventory examples used only for option classes not covered by the inventory: generated image output, video output, and audio processing/generation.

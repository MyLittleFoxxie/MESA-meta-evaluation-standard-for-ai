# Literature Index and Thematic Reading Guide

This directory holds the source literature supporting the MESA manuscripts ([`paper_chase.tex`](../paper_chase.tex), [`paper_refsq.tex`](../paper_refsq.tex), [`paper.tex`](../paper.tex), and [`paper_old.tex`](../paper_old.tex)), the adaptation rationale ([`supporting/adaptation/adaptation-map.md`](../supporting/adaptation/adaptation-map.md)), and the supporting benchmark reviews.

## Directory Structure

- [`pdfs/`](pdfs/): Original PDF sources where stored locally. For the EFPA Test Review Model and other primary documents, the original PDF remains authoritative where Markdown extraction loses layout or table detail.
- [`transcriptions/`](transcriptions/): Corresponding extracted Markdown texts used for search, quotation verification, and review preparation.
- [`notes/benchmark_official_documentation_inventory.md`](notes/benchmark_official_documentation_inventory.md): Inventory of official benchmark documentation links and scope notes.

 Not every entry in [`references.bib`](../references.bib) has a local PDF or transcription; several cited standards, repositories, and tool references are external web or bibliography records only. Reorganizing these sources does not constitute a new literature review or independently verify the truth of external source claims. Existing source-inspection dates and qualifications remain unchanged.

---

## Thematic Reading Guide

### 1. EFPA and Test Review Foundations
- **EFPA Test Review Model 2025** (`efpa_test_review_model_2025`): Conceptual basis for MESA's separation of descriptive documentation checks (Part A) from evaluative judgments (Part B). See [PDF](pdfs/EFPA_test_review_model_2025.pdf) and [transcription](transcriptions/EFPA_Test_Review_Model_2025_Markdown.md).
- **AERA, APA, & NCME Standards (2014)** (`aera_apa_ncme_standards_2014`): Foundational educational and psychological testing standards (external citation in `references.bib`).

### 2. Measurement, Construct Validity, and Score Interpretation
- **Kane (2013), *Validating the Interpretations and Uses of Test Scores*** (`kane_validation`): Argument-based validation linking observed performances to intended interpretations and uses (external DOI citation in `references.bib`).
- **Bean et al. (2025), *Measuring what Matters: Construct Validity in Large Language Model Benchmarks*** (`bean_measuring_what_matters`): Construct validity challenges in LLM benchmarks. See [PDF](pdfs/Measuring%20what%20Matters.pdf) and [transcription](transcriptions/Measuring_what_Matters.md).
- **Jo & Wilson (2025), *What Does Your Benchmark Really Measure?*** (`jo_wilson_what_does_your_benchmark_measure`): Framework for capability inference from benchmark scores. See [PDF](pdfs/What%20Does%20Your%20Benchmark%20Really%20Measure.pdf) and [transcription](transcriptions/What_Does_Your_Benchmark_Really_Measure.md).
- **Fodor (2025), *LINE GOES UP? Inherent Limitations of Benchmarks for Evaluating Large Language Models*** (`line_goes_up`): Limits of aggregate benchmark scores and construct coverage. See [PDF](pdfs/lineUP.pdf) and [transcription](transcriptions/lineUP.md).
- **Alonso & Church (2024), *Evaluating the Evaluations: A Perspective on Benchmarks*** (`alonso_church_sigir`): Historical perspective on benchmark evaluation and interpretation. See [PDF](pdfs/Evaluating_the_Evaluations.pdf) and [transcription](transcriptions/Evaluating_the_Evaluations.md).
- **AI Cognitive Examination** (*uncited background*): Cognitive examination framing for AI evaluation. See [PDF](pdfs/AI%20Cognitive%20Examination.pdf) and [transcription](transcriptions/AI_Cognitive_Examination.md).

### 3. Benchmark Implementation, Documentation, Judging, and Reproducibility
- **Reuel et al. (2024), *BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices*** (`reuel_betterbench`): Lifecycle, implementation, documentation, and maintenance checklist for AI benchmarks. See [PDF](pdfs/betterbench.pdf) and [transcription](transcriptions/betterbench.md).
- **Singh et al. (2025), *The Leaderboard Illusion*** (`singh_leaderboard_illusion`): Leaderboard comparability, private test practices, and evaluation fairness. See [PDF](pdfs/The%20Leaderboard%20Illusion.pdf) and [transcription](transcriptions/The_Leaderboard_Illusion.md).
- **Cheng et al. (2025), *Benchmarking is Broken — Don't Let AI be its Own Judge*** (`cheng_benchmarking_broken`), **Zheng et al. (2023), *Judging LLM-as-a-Judge*** (`zheng_llm_judge_2023`), and **Shi et al. (2025), *Judging the Judges*** (`shi_judging_judges_2025`): Automated judging biases and scorer validation (external citations in `references.bib`).
- **Gebru et al. (2021), *Datasheets for Datasets*** (`gebru_datasheets_2021`) and **Mitchell et al. (2019), *Model Cards for Model Reporting*** (`mitchell_model_cards_2019`): Dataset and model documentation standards (external citations in `references.bib`).
- **Habiba et al. (2024), *How Mature Is Requirements Engineering for AI-Based Systems?*** (`habiba_re4ai_maturity_2024`), **EU AI Act (2024)** (`eu_ai_act_2024`), and **ISO/IEC 25059:2023** (`iso_iec_25059_2023`): Requirements engineering and AI quality/regulatory context (external citations in `references.bib`).
- **PRIORITIZATION FIRST** ([PDF](pdfs/PRIORITIZATION%20FIRST.pdf), [transcription](transcriptions/PRIORITIZATION_FIRST.md)) and **PeerBench Proposal** ([PDF](pdfs/PeerBench_PROPOSAL_PAPER.pdf), [transcription](transcriptions/PeerBench_PROPOSAL_PAPER.md)): Uncited background sources on benchmark prioritization and peer-reviewed benchmarking.

### 4. Broad Ability and General Intelligence Claims
- **Hendrycks et al. (2025), *A Definition of AGI*** (`hendrycks_definition_agi`): Taxonomic capability framing drawing on CHC theory. See [PDF](pdfs/A_Definition_of_AGI.pdf) and [transcription](transcriptions/A_Definition_of_AGI.md).
- **Canivez & Youngstrom (2019), *Challenges to the Cattell-Horn-Carroll Theory*** (`canivez_chc_critique`): Psychometric critique of broad CHC factor interpretations (external citation in `references.bib`).

### 5. Reviewed Benchmark Case Sources
- **Phan et al. (2025), *Humanity's Last Exam (HLE)*** (`phan_etal_hle_2025`) and **Skarlinski et al. (2025), *FutureHouse HLE chemistry/biology audit*** (`skarlinski_futurehouse_hle_2025`): Used for the completed HLE teaching example and supporting pilot review. See [HLE PDF](pdfs/Humanitys%20Last%20Exam.pdf) and [transcription](transcriptions/Humanitys_Last_Exam.md) (snapshot fingerprinted in [`surveys/colleague-review/source-manifest.json`](../surveys/colleague-review/source-manifest.json)).
- **Chollet et al. (2025), *ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems*** (`chollet_arc_agi_2_2025`): Reviewed benchmark case (external citation in `references.bib`; inspected repository/report sources documented in [`surveys/colleague-review/packet.json`](../surveys/colleague-review/packet.json)).
- **Doris et al. (2024), *DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation*** (`doris_designqa_2024`): Reviewed benchmark case. See [PDF](pdfs/DesignQA.pdf) and [transcription](transcriptions/DesignQA.md).
- **Marcus et al. (1993), *Penn Treebank*** (`marcus_etal_1993_building`), **HumanEval** (`human_eval_repository`), and **TruthfulQA** (`truthfulqa_repository`): Illustrative benchmark references in `paper.tex` / `paper_old.tex` (external citations in `references.bib`).
- **Official Documentation Inventory**: [`notes/benchmark_official_documentation_inventory.md`](notes/benchmark_official_documentation_inventory.md).

### 6. Empirical Methods and Study Execution
- **ACM SIGSOFT Empirical Standards** (`sigsoft_empirical_standards`): Benchmarking and Engineering Research methodological guidance; see [`supporting/adaptation/standards-assessment.md`](../supporting/adaptation/standards-assessment.md).
- **Venable, Pries-Heje, & Baskerville (2016), *FEDS*** (`venable_feds`): Design science evaluation framework cited in `paper_refsq.tex` and `paper.tex`.
- **Anthropic Claude Code CLI** (`anthropic_claude_code_cli`) and **OpenAI Codex Non-interactive Mode** (`openai_codex_execution`): Execution environment references for the model study (`paper_chase.tex`).

---

## Source Index (`references.bib` and Local Holdings)

| BibTeX key | Local PDF (`pdfs/`) | Local transcription (`transcriptions/`) | URL / DOI in `references.bib` | Status & manuscripts |
| --- | --- | --- | --- | --- |
| `alonso_church_sigir` | [Evaluating_the_Evaluations.pdf](pdfs/Evaluating_the_Evaluations.pdf) | [Evaluating_the_Evaluations.md](transcriptions/Evaluating_the_Evaluations.md) | `10.1145/3720330.3720332` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `marcus_etal_1993_building` | — | — | `https://aclanthology.org/J93-2004` | Cited (`paper`, `paper_old`) |
| `reuel_betterbench` | [betterbench.pdf](pdfs/betterbench.pdf) | [betterbench.md](transcriptions/betterbench.md) | `https://arxiv.org/pdf/2411.12990` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `hendrycks_definition_agi` | [A_Definition_of_AGI.pdf](pdfs/A_Definition_of_AGI.pdf) | [A_Definition_of_AGI.md](transcriptions/A_Definition_of_AGI.md) | `https://arxiv.org/pdf/2510.18212` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `singh_leaderboard_illusion` | [The Leaderboard Illusion.pdf](pdfs/The%20Leaderboard%20Illusion.pdf) | [The_Leaderboard_Illusion.md](transcriptions/The_Leaderboard_Illusion.md) | `https://arxiv.org/pdf/2504.20879` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `cheng_benchmarking_broken` | — | — | `https://arxiv.org/pdf/2510.07575` | Cited (`paper`, `paper_old`) |
| `bean_measuring_what_matters` | [Measuring what Matters.pdf](pdfs/Measuring%20what%20Matters.pdf) | [Measuring_what_Matters.md](transcriptions/Measuring_what_Matters.md) | `https://arxiv.org/pdf/2511.04703` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `jo_wilson_what_does_your_benchmark_measure` | [What Does Your Benchmark Really Measure.pdf](pdfs/What%20Does%20Your%20Benchmark%20Really%20Measure.pdf) | [What_Does_Your_Benchmark_Really_Measure.md](transcriptions/What_Does_Your_Benchmark_Really_Measure.md) | `https://arxiv.org/pdf/2509.19590` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `line_goes_up` | [lineUP.pdf](pdfs/lineUP.pdf) | [lineUP.md](transcriptions/lineUP.md) | `https://arxiv.org/pdf/2502.14318` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `canivez_chc_critique` | — | — | `10.1080/08957347.2019.1619562` | Cited (`paper`, `paper_old`) |
| `aera_apa_ncme_standards_2014` | — | — | `https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `efpa_test_review_model_2025` | [EFPA_test_review_model_2025.pdf](pdfs/EFPA_test_review_model_2025.pdf) | [EFPA_Test_Review_Model_2025_Markdown.md](transcriptions/EFPA_Test_Review_Model_2025_Markdown.md) | `https://www.efpa.eu/efpa-test-review-model-version-2025` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `phan_etal_hle_2025` | [Humanitys Last Exam.pdf](pdfs/Humanitys%20Last%20Exam.pdf) | [Humanitys_Last_Exam.md](transcriptions/Humanitys_Last_Exam.md) | `https://arxiv.org/abs/2501.14249` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `habiba_re4ai_maturity_2024` | — | — | `10.1007/s00766-024-00432-3` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `skarlinski_futurehouse_hle_2025` | — | — | `https://www.futurehouse.org/research-announcements/hle-exam` | Cited (`paper`, `paper_old`) |
| `gebru_datasheets_2021` | — | — | `10.1145/3458723` | Cited (`paper_chase`, `paper_refsq`, `paper`) |
| `mitchell_model_cards_2019` | — | — | `10.1145/3287560.3287596` | Cited (`paper_chase`, `paper_refsq`, `paper`) |
| `eu_ai_act_2024` | — | — | `https://eur-lex.europa.eu/eli/reg/2024/1689/oj` | Retained in `references.bib` (background/regulatory) |
| `iso_iec_25059_2023` | — | — | `https://www.iso.org/standard/80655.html` | Retained in `references.bib` (background/standards) |
| `chollet_arc_agi_2_2025` | — | — | `https://arxiv.org/abs/2505.11831` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `doris_designqa_2024` | [DesignQA.pdf](pdfs/DesignQA.pdf) | [DesignQA.md](transcriptions/DesignQA.md) | `https://arxiv.org/abs/2404.07917` | Cited (`paper_chase`, `paper_refsq`, `paper`, `paper_old`) |
| `venable_feds` | — | — | `10.1057/ejis.2014.36` | Cited (`paper_refsq`, `paper`) |
| `kane_validation` | — | — | `10.1111/jedm.12000` | Cited (`paper_chase`, `paper_refsq`, `paper`) |
| `human_eval_repository` | — | — | `https://github.com/openai/human-eval` | Cited (`paper`, accessed 2026-09-25) |
| `truthfulqa_repository` | — | — | `https://github.com/sylinrl/TruthfulQA` | Cited (`paper`, accessed 2026-09-25) |
| `sigsoft_empirical_standards` | — | — | `https://www2.sigsoft.org/EmpiricalStandards/docs/standards` | Cited (`paper_chase`, accessed 2026-10-14) |
| `zheng_llm_judge_2023` | — | — | `https://arxiv.org/abs/2306.05685v4` | Cited (`paper_chase`) |
| `shi_judging_judges_2025` | — | — | `https://arxiv.org/abs/2406.07791v9` | Cited (`paper_chase`) |
| `openai_codex_execution` | — | — | `https://developers.openai.com/codex/noninteractive` | Cited (`paper_chase`, accessed 2026-10-14) |
| `anthropic_claude_code_cli` | — | — | `https://code.claude.com/docs/en/cli-reference` | Cited (`paper_chase`, accessed 2026-10-17) |
| — (*background*) | [AI Cognitive Examination.pdf](pdfs/AI%20Cognitive%20Examination.pdf) | [AI_Cognitive_Examination.md](transcriptions/AI_Cognitive_Examination.md) | — | Uncited background source retained for literature review |
| — (*background*) | [PRIORITIZATION FIRST.pdf](pdfs/PRIORITIZATION%20FIRST.pdf) | [PRIORITIZATION_FIRST.md](transcriptions/PRIORITIZATION_FIRST.md) | — | Uncited background source retained for literature review |
| — (*background*) | [PeerBench_PROPOSAL_PAPER.pdf](pdfs/PeerBench_PROPOSAL_PAPER.pdf) | [PeerBench_PROPOSAL_PAPER.md](transcriptions/PeerBench_PROPOSAL_PAPER.md) | — | Uncited background source retained for literature review |

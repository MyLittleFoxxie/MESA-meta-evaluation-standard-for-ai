# Archive Index and Provenance Guide

This document explains how to retrieve historical experiments, superseded planning records, presentation materials, and peripheral sources that were removed from the active checkout when the repository was reorganized into a focused manuscript and literature-review repository on 22 October 2026.

See [relocation-map.json](relocation-map.json) for the machine-readable old-to-new path mapping, SHA-256 digests, and retention or archival reasons, and [reorganization-plan.md](reorganization-plan.md) for the reorganization specification.

## Git Snapshot and Retrieval Instructions

All tracked historical material is preserved intact in Git history without rewriting commits:

- **Snapshot tag:** `pre-reorganization-2026-10-22`
- **Snapshot commit:** `5baebed3a4b8b92d755ae92ea3f517b6607ecc97`

### Retrieve a single file from the snapshot

```sh
git show pre-reorganization-2026-10-22:<old/path/to/file>
```

### List files inside an archived directory

```sh
git ls-tree -r --name-only pre-reorganization-2026-10-22 <old/directory/path>
```

### Export an archived directory into a temporary folder outside the active tree

```sh
git archive pre-reorganization-2026-10-22 <old/directory/path> | tar -x -C /tmp/
```

## Relocated Active Material

Active research evidence, literature, and supporting adaptation records remain in the working tree at the following locations (all moved byte-for-byte; see [relocation-map.json](relocation-map.json)):

| Original path | Current active path | Role |
| --- | --- | --- |
| `Papers/*.pdf` (13 core sources) | `literature/pdfs/*.pdf` | Authoritative original PDF sources paired with transcriptions |
| `literature/*.md` (13 transcriptions) | `literature/transcriptions/*.md` | Extracted Markdown transcriptions of core literature |
| `benchmark_official_documentation_inventory.md` | `literature/notes/benchmark_official_documentation_inventory.md` | Benchmark primary-documentation inventory |
| `surveys/colleague-review/simulation-study/analyst/adaptation-map.md` | `supporting/adaptation/adaptation-map.md` | Proposed EFPA–MESA correspondence and omissions |
| `surveys/colleague-review/simulation-study/analyst/standards-assessment.md` | `supporting/adaptation/standards-assessment.md` | ACM SIGSOFT Empirical Standards assessment |
| `MESA EFPA template official.md` | `supporting/retrai-paper/MESA EFPA template official.md` | Supporting detailed adaptation template (substantiates `paper.tex`) |
| `MESA scorecard.md` | `supporting/retrai-paper/MESA scorecard.md` | Generated 40-item supporting scorecard (substantiates `paper.tex`) |
| `reviews/` | `supporting/retrai-paper/reviews/` | Supporting pilot benchmark reviews (HLE, ARC-AGI-2, DesignQA) |
| `thesis/` | `supporting/retrai-paper/thesis/` | Supporting RETRAI revision and pilot comparison records |
| `proposals/mesa-25/{questions.json,designqa-example.json,designqa-example.md}` | `supporting/retrai-paper/provenance/mesa-25/` | Questionnaire and DesignQA example provenance |
| `feedback/95-mesa-core-plan.md` | `supporting/retrai-paper/provenance/95-mesa-core-plan.md` | 40-item scorecard derivation record |
| `CHASE-review-response.md` | `supporting/editorial/CHASE-review-response.md` | CHASE manuscript review response |

## Archived Historical Model Studies

None of the archived GPT-6.1 Sol or Astra series is pooled with the current Claude Sonnet 5.5 study reported in [`paper_chase.tex`](../paper_chase.tex) and [`CHASE-study.md`](../CHASE-study.md). All raw prompts, responses, incomplete outputs, and failure logs are preserved in `pre-reorganization-2026-10-22`:

| Archived path in `pre-reorganization-2026-10-22` | Description |
| --- | --- |
| `surveys/colleague-review/mesa-study/main/` | Same 30-conversation design run with GPT-6.1 Sol via Codex CLI; stopped at a Codex usage limit (20 completed, 1 failed without response, 9 unrun). |
| `surveys/colleague-review/mesa-study/2026-10-17/` | Larger 180-conversation GPT-6.1 Sol design, stopped after 44 conversations when the 30-conversation design was chosen. |
| `surveys/colleague-review/accessibility-study/v1/` | Earlier 40-conversation GPT-6.1 Sol comparison of two explanation texts for the 25 questions. |
| `surveys/colleague-review/simulation-study/`, `surveys/colleague-review/simulation-protocol.md`, `surveys/colleague-review/simulation-materials.html` | First 120-conversation GPT-6.1 Sol series across four instruction versions and an incomplete Astra series (14 completed, 106 failed). |

## Archived Planning, Presentation, Viewer, and Peripheral Material

| Archived path in `pre-reorganization-2026-10-22` | Reason for archival |
| --- | --- |
| `feedback/` (except `95-mesa-core-plan.md`), `proposals/` (except retained `mesa-25` provenance files), `critique_plan.md`, `thesis-sharpening-plan.md` | Superseded self-review notes and early questionnaire proposal drafts. |
| `slides.md`, `speech.md`, `presentation/`, `MESA___Thesis___Vitor_Brandao_Raposo.pdf` | Presentation deliverables and rendered historical thesis PDF outside the manuscript working tree. |
| `index.html`, `assets/` | Retired interactive viewer for the older detailed template and thesis PDF. The active participant survey remains self-contained at `surveys/colleague-review/survey.html`. |
| `research/ai-agents-incident-sources/`, `Papers/METR_Redwood_HF_Incident_Investigation_2026.pdf`, `Papers/OpenAI_HF_Incident_Technical_Report_2026.pdf`, `Papers/aire-25-example-drgm.pdf` | Separate AI-agent incident source collection and venue formatting example, uncited by the retained MESA manuscripts. |
| `.agents/`, `.claude/`, `.codex/` | Legacy automation profiles and memory notes targeting the retired full-template workflow; superseded by [`AGENTS.md`](../AGENTS.md), [`CLAUDE.md`](../CLAUDE.md), [`CODEX.md`](../CODEX.md), and [`GEMINI.md`](../GEMINI.md). |

## Known Pre-Existing Manuscript and Frozen-Record Notes

- **Missing figure assets in `paper.tex` and `paper_old.tex`:** Both [`paper.tex`](../paper.tex) and [`paper_old.tex`](../paper_old.tex) contain `\includegraphics` references to `figures/mesa-methodology-pipeline.png` and `figures/mesa-test-case-pipeline.png`. That `figures/` directory was absent from the checkout prior to reorganization and is not present in Git history. Neither preserved manuscript is claimed to be build-ready, and no replacement figures have been invented.
- **Unsuffixed citation keys in `paper_old.tex`:** The older preserved draft [`paper_old.tex`](../paper_old.tex) cites `gebru_datasheets`, `mitchell_model_cards`, `eu_ai_act`, and `iso_iec_25059`, which were later suffixed with publication years in [`references.bib`](../references.bib) (`gebru_datasheets_2021`, `mitchell_model_cards_2019`, `eu_ai_act_2024`, `iso_iec_25059_2023`). All citation keys in [`paper_chase.tex`](../paper_chase.tex), [`paper_refsq.tex`](../paper_refsq.tex), and [`paper.tex`](../paper.tex) resolve against `references.bib`.
- **Frozen historical relative links:** Byte-preserved historical records ([`surveys/colleague-review/mesa-study/claude-sonnet-5-5/README.md`](../surveys/colleague-review/mesa-study/claude-sonnet-5-5/README.md), `claude-sonnet-5-5-guidance-v2/analyst/before-*.md`, [`supporting/retrai-paper/thesis/question-check.md`](../supporting/retrai-paper/thesis/question-check.md), and [`supporting/retrai-paper/provenance/mesa-25/designqa-example.md`](../supporting/retrai-paper/provenance/mesa-25/designqa-example.md)) retain their original bytes and embedded historical paths, which map to current or archived locations via [relocation-map.json](relocation-map.json).
- **No LaTeX compilation:** In accordance with repository rules, no LaTeX compilation or automatic PDF preview is performed; visual layout and page length remain unchecked.

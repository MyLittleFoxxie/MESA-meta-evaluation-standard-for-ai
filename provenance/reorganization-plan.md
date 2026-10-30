# Repository reorganization plan

Prepared 22 October 2026. Planning only: no existing files have been moved, deleted, or rewritten.

## Intended result

Make the active checkout a manuscript and literature-review repository. Keep files that are needed to write, substantiate, reproduce, or maintain the retained manuscripts. Preserve superseded work in a recoverable snapshot outside the active tree, with an index pointing to it. Merely moving all clutter into an enormous `archive/` directory would not meet this objective.

Treat all four root manuscripts as in scope initially: `paper_chase.tex`, `paper_refsq.tex`, `paper.tex`, and `paper_old.tex`. Identify `paper.tex` as the preserved RETRAI submission manuscript and `paper_old.tex` as an older manuscript; do not replace their content. CHASE remains the adaptation and model-study paper. REFSQ remains its planned extension with human evaluation, with placeholders where actual human records are unavailable.

“Necessary” includes research evidence, not just LaTeX compilation dependencies. The raw model records, questionnaire source, adaptation rationale, and source literature are essential even when LaTeX does not directly load them.

## Proposed active structure

```text
/
├── README.md                         # Short navigation and manuscript status
├── AGENTS.md                         # One authoritative repository guide
├── CODEX.md                          # Updated agent entry point
├── GEMINI.md                         # Updated agent entry point
├── CLAUDE.md                         # Updated agent entry point
├── LICENSE
├── .gitignore
├── paper_chase.tex
├── paper_refsq.tex
├── paper.tex                         # Preserved RETRAI submission manuscript
├── paper_old.tex                     # Preserved older manuscript
├── references.bib                    # Shared bibliography; keep existing keys
├── CHASE-study.md                    # Stable entry point cited by the paper
├── literature/
│   ├── README.md                     # Source index and thematic reading guide
│   ├── pdfs/                         # Relevant original PDFs
│   ├── transcriptions/               # Corresponding extracted source texts
│   └── notes/                        # Relevant source inventories and synthesis
├── supporting/
│   ├── adaptation/                   # Current adaptation map and methods guidance
│   ├── retrai-paper/               # Evidence supporting the RETRAI paper and older draft
│   └── editorial/                    # Current review response and necessary notes
├── surveys/colleague-review/          # Retain the participant-facing URL and bundle
│   └── mesa-study/
│       ├── chase-report/             # Current analysis and traceability
│       ├── claude-sonnet-5-5/         # Complete preserved source batch
│       └── claude-sonnet-5-5-guidance-v2/ # Complete preserved source batch
├── tools/                            # Only utilities used by retained material
└── provenance/
    ├── archive-index.md              # How to retrieve removed historical material
    └── relocation-map.json           # Old/new paths, hashes, and retention reasons
```

Keeping the manuscripts and shared bibliography at the root avoids unnecessary changes to their LaTeX paths. Keeping the current survey and study hierarchy avoids breaking the participant URL, batch-relative paths, and existing analysis scripts. The tree deliberately favors a small number of understandable locations over renaming every directory.

## Disposition of existing material

| Existing material | Proposed action | Reason or condition |
| --- | --- | --- |
| Four root `.tex` files and `references.bib` | Keep at root | Manuscripts and their shared citation database. Do not prune bibliography entries just because CHASE does not cite them. |
| `README.md`, `CHASE-study.md`, `AGENTS.md`, `LICENSE` | Keep; update navigation where necessary | Stable entry points and project constraints. |
| `Papers/` and `literature/` | Consolidate relevant PDFs and transcriptions under `literature/` | Pair original sources with extracted text and a source index. Original EFPA PDF remains authoritative. |
| `benchmark_official_documentation_inventory.md` | Move to `literature/notes/` if retained papers or source provenance depend on it | Existing source inventory, distinct from a completed literature synthesis. |
| `mesa-study/chase-report/` | Keep complete | Current selection, analysis, audit, and manuscript traceability. |
| Both Claude batch directories | Keep complete in the first cleanup | Current analysis and preservation checks depend on more than the selected response files, including earlier MESA inputs, manifests, validation helpers, and batch analyses. |
| `simulation-study/analyst/adaptation-map.md` and `standards-assessment.md` | Promote to `supporting/adaptation/`, preserving bytes and recording original paths | Active methodological support currently hidden inside an older experiment directory. Resolve their outgoing references before removing that directory. |
| Current survey packet, template, generated forms, images, builders, validators, guides, provenance, future human-study plan and compatibility snapshots | Keep at current paths | Necessary REFSQ materials; current verification also reads the v2.0 archive. Preserve the live participant flow and payload. |
| Remaining old simulation series, `mesa-study/main/`, `mesa-study/2026-10-17/`, and `accessibility-study/v1/` | Remove from active checkout only after archival and dependency audit | Historical experiments excluded from the current manuscript findings. Preserve all failures and incomplete responses in the archive. |
| `MESA EFPA template official.md`, `MESA scorecard.md`, `reviews/`, and `thesis/` | Group under `supporting/retrai-paper/`, retaining versions and required helper files | These substantiate the preserved RETRAI submission manuscript and its development. They are supporting adaptation records, not a second current MESA instrument. |
| `tools/build-scorecard.py`, `check-thesis.py`, and `scorecard-manifest.md` | Retain with updated path handling if needed by the preserved RETRAI paper bundle | The scorecard remains generated. Existing frozen hashes are not rewritten to conceal changes. |
| `CHASE-review-response.md` | Move to `supporting/editorial/` | Still read by the current CHASE verifier; update that dependency. |
| `feedback/`, `proposals/`, `critique_plan.md`, and `thesis-sharpening-plan.md` | Archive superseded planning; retain individual files still needed for paper provenance | Assess file dependencies before removing whole directories; survey guidance refers to an older example in `proposals/mesa-25/`. |
| `slides.md`, `speech.md`, `presentation/`, and thesis PDF | Archive unless a retained paper needs a specific item | Presentation deliverables and the old rendered thesis are outside the proposed working scope. |
| `index.html` and `assets/` | Retire the old detailed-template viewer; retain a minimal survey landing page if hosting needs it | Inspect hosting and incoming links before changing the root page. The existing viewer loads the thesis PDF and its own JavaScript assets. Do not break the participant survey. |
| `research/ai-agents-incident-sources/` and associated incident PDFs | Candidates for removal from the active tree after citation/provenance audit | Separate research topic; filename or uncited status alone is insufficient grounds for deletion. Do not restore SWARM. |
| `CODEX.md`, `GEMINI.md`, `CLAUDE.md` | Retain and update for the reorganized repository | Reflect the manuscript and literature-review scope, new paths, preservation rules, and verification commands; refer to `AGENTS.md` as the authoritative guide. |
| `.agents/`, `.claude/`, `.codex/` | Archive obsolete automation and duplicated guidance; retain only currently useful instructions | Keep `AGENTS.md` authoritative. Check tool and skill dependencies before removal. |
| Caches, `.DS_Store`, and regenerable build debris | Ignore or remove where appropriate | No source or research value. Keep source PDFs distinct from generated manuscript PDFs. |

Two pre-existing untracked files must remain untouched during planning: `surveys/colleague-review/mesa-study/chase-report/build-review-reader.py` and `review-reader.html`. They may belong in the current reporting bundle, but must be included explicitly in any later backup and migration inventory rather than lost or silently staged.

## Literature-review organization

Create an index linking each retained source to its bibliography key, original PDF if present, transcription if present, source URL/DOI already recorded, and role in the manuscripts. Do not infer that a local PDF exists for every citation or that an extracted text is authoritative.

Organize the reading guide by themes: EFPA and test review; measurement and validity; benchmark implementation and reproducibility; broad ability claims; benchmark case sources; and empirical methods. Use tags or index sections rather than duplicating files across thematic folders.

Retain relevant uncited background sources when they support the literature review or adaptation records. Mark sources as cited, background, historical, or pending relevance review. Treat incident reports and other peripheral material as archive candidates until their dependencies are checked. Preserve existing source-inspection dates and verification qualifications. This reorganization does not itself verify the truth of source claims or constitute a new literature review.

## Execution sequence

1. **Inventory and establish a baseline.** Record tracked, untracked, and relevant ignored files; size; SHA-256; and intended disposition. Trace LaTeX assets/citations, Markdown links, HTML assets, Python imports/path assumptions, JSON paths, and fingerprint manifests. Record pre-existing broken references separately from migration regressions.
2. **Preserve the starting state.** Create a recoverable Git snapshot/tag for tracked history and a separate verified backup for untracked work. Record the exact commit and retrieval instructions. Do not rewrite Git history. A smaller checkout does not imply a smaller `.git` database.
3. **Build the dependency-based keep list.** Start with the four manuscripts, literature-review sources, current study report and source batches, survey bundle, and adaptation records. Follow dependencies until no required file remains classified as removable. Keep whole frozen batches initially rather than attempting risky selective pruning.
4. **Reorganize sources and supporting documents.** Move working literature and supporting records according to the table. Preserve immutable research content byte-for-byte. Record every relocation. Where frozen records embed old paths, retain the original record and use a documented resolver or compatibility mechanism; do not mass-replace paths in original prompts, outputs, protocols, or manifests.
5. **Update maintained entry points and tools.** Inventory every `README*`, `AGENTS.md`, `CODEX.md`, `GEMINI.md`, and `CLAUDE.md`, including nested copies. Update every retained, maintained copy to describe the manuscript and literature-review scope, final directory structure, current versus historical material, source-of-truth locations, and applicable verification commands. Keep these guides consistent with `AGENTS.md` and `CHASE-study.md`. Preserve frozen historical copies unchanged in the archive, with current navigation explaining their status. Update current manuscript path descriptions where needed and maintained script paths. Replace archived historical-document links with exact snapshot links. Preserve old manuscript text where possible by documenting its original layout in the relocation index. Keep the GitHub repository link and root `CHASE-study.md` entry point.
6. **Remove archived material from the active tree.** Only after confirming the snapshot is retrievable and no active dependency is lost. Keep a concise archive index, not copies of entire historical experiments under a new directory. Handle hosting changes separately from filesystem cleanup; do not publish or send survey submissions as part of reorganization.
7. **Verify and document the result.** Use the checks below, report remaining known limitations, and present a final old-to-new map and retained-file counts. Keep reorganization changes distinct from manuscript-content revisions.

## Acceptance checks and known issues

- All retained citation keys, LaTeX references, braces/environments, and asset paths are checked statically. **Do not compile LaTeX or open automatic PDF preview.** Layout and page length remain unchecked.
- Both `paper.tex` and `paper_old.tex` currently refer to `figures/mesa-methodology-pipeline.png` and `figures/mesa-test-case-pipeline.png`; that directory is absent from this checkout. Record this pre-existing gap. Locate original assets in preserved history if available; do not invent replacements or claim these manuscripts are build-ready.
- Current offline analysis reproduces the saved selection and findings: 30 conversations, 28 usable responses, and 32 physical attempts, with invalid outputs and failures intact. Compare regenerated reporting outputs with the baseline; do not launch experiments.
- Preserve fingerprints of frozen inputs, responses, source materials and protocols. Existing preservation verification is part of the dependency graph: `chase-report/verify.py` invokes `claude-sonnet-5-5-guidance-v2/verify_revision.py`, which also reads the older Claude batch.
- Survey checks retain 25 questions, five choices, both blank participant benchmarks, and the current feedback fields. Preserve packet identifiers, fingerprints, drafts and retry behavior. Use mocked delivery if browser checks are needed; no real submissions or emails.
- All active internal links resolve. Historical links resolve to preserved snapshot records or explicitly documented original paths. Review relative HTML/JavaScript requests as well as Markdown links.
- No original manuscript, review, source paper, participant record, or frozen experiment is silently rewritten or lost. No historical model sessions are pooled into current results.
- The final README provides a short route to manuscripts, literature, current study evidence, and REFSQ survey materials. Every other retained directory has a stated manuscript or literature-review purpose.
- Every retained, maintained `README*`, `AGENTS.md`, `CODEX.md`, `GEMINI.md`, and `CLAUDE.md` has been checked against the final layout and scope. No active guide directs readers to removed paths or superseded workflows. Frozen historical guides remain unchanged and are clearly identified through the archive index.

The dependency inventory is the first implementation deliverable. This plan identifies directory-level decisions and concrete path hazards; it does not claim that every individual file has already received a final keep/remove classification.

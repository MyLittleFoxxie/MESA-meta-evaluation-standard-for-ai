# MESA: benchmark review

The current manuscript is [mesa_paper.tex](mesa_paper.tex), **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, intended for REFSQ in Springer LNCS format. It compares benchmark review frameworks, reports model sessions, and proposes a requirements traceability application. Human validation and effects on requirements decisions have not been established.

Keep three research artifacts distinct: the earlier **25 question questionnaire**; the v4 mapping of **280 framework items to 30 comparison concerns**; and the derived rubric with **eight description fields and 29 evaluation questions**. The v4 study records remain under their existing paths. The manuscript rename does not change the instrument, records, or manuscript content.

## Start here

- [MESA manuscript](mesa_paper.tex): current REFSQ paper.
- [v4 study guide](v4/README.md): framework mapping, 18 framework sessions, eight rubric sessions, and two amendment sessions across HumanEval, TruthfulQA, HLE, and τ-bench.
- [Manuscript checker](verify_manuscripts.py): run `python3 verify_manuscripts.py` from the repository root to verify citations, cross-references, and rules across `mesa_paper.tex`, `paper2.tex`, and `paper2_preview.tex`.
- [v3 manuscript](paper_mesa_v3.tex) and [v3 records](v3/README.md): preserved earlier work.
- [Paper two preview](paper2_preview.tex): preserved companion manuscript.
- [Earlier questionnaire materials](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/materials/mesa.txt), [participant survey](surveys/colleague-review/survey.html), and [reading passages](surveys/colleague-review/survey.md).
- [Historical CHASE study guide](CHASE-study.md): earlier questionnaire experiments, separate from the v4 study.
- [Manuscript consolidation record](provenance/manuscript-consolidation-2026-11-03.md): removed manuscripts, renamed files, and Git retrieval commands.

## Earlier questionnaire

The questions cover six domains:

| Domain | Questions | Main concern |
| --- | --- | --- |
| Description | 1–5 | Whether the benchmark, tasks, conditions, and scoring are documented |
| Purpose and development | 6–9 | Reasons for the tasks, checking for errors, and coverage of the claimed ability |
| Scoring and comparisons | 10–13 | Whether scoring and comparison points support the intended interpretation |
| Consistency of results | 14–16 | Repeated runs, changed conditions, and score variation |
| Meaning and fairness | 17–21 | Shortcuts, prior exposure, training rules, broader claims, and fair comparisons |
| Use and reporting | 22–25 | Inspection, reuse, updates, and public claims |

Every question uses five choices:

- **Yes:** the information supports the whole condition.
- **Partly:** the information supports some parts.
- **No:** the information shows that the condition is not met.
- **Not sure:** the available information is missing or insufficient.
- **Not applicable:** the issue does not arise for the benchmark or intended use.

These are categories, not numerical quality ratings. MESA has **no total quality score**. Missing documentation does not establish that a benchmark is poor. When a question asks whether checking occurred, the existence of that check is separate from whether its findings were favorable.

Questions 1–5 judge the availability of descriptive information; the reading passages supply the benchmark facts. The remaining questions examine reasons, checks, and the interpretation of results. Optional comments let reviewers explain their choices.

## Guided survey

The survey follows this sequence:

Introduction → three familiarity self-reports → completed Humanity's Last Exam example → ARC-AGI-2 → DesignQA → combined review and submission → confirmation.

The HLE example explains all 25 selections. ARC-AGI-2 and DesignQA are left for participants to answer. Familiarity is self-reported, and comments are optional. See the [survey guide](surveys/colleague-review/agent-guide.md) for maintenance instructions and [packet.json](surveys/colleague-review/packet.json) for the source content.

## Historical CHASE study and observed results

The historical CHASE paper is a design study of the EFPA adaptation, with an exploratory examination of model-generated reviews. The reporting selection contains **30 conversations**: ten MESA, ten EFPA-TRM, and ten general-instruction sessions. For each method, five conversations review ARC-AGI-2 and DesignQA, and five classify 49 claims in 24 constructed cases. Claude Sonnet 5.5 reads supplied descriptions; it does not execute the benchmarks.

MESA guidance was finalized after development testing, and its sessions ran after the comparison-method sessions. The reporting selection was assembled after execution and includes all conversations from those batches. This is a comparison across sequential batches, not a jointly randomized or held-out experiment. Earlier development responses remain archived outside the reported results.

All **30 conversations completed**, through **32 physical attempts** including two authentication failures before model generation and their retained retries. **28** responses met the predefined format. One EFPA-TRM benchmark conversation and one general-instruction case conversation were excluded without repair or replacement.

| Method | Usable benchmark conversations | Usable test-case conversations | Expected claim answers matched | Alternative P6B label |
| --- | ---: | ---: | ---: | ---: |
| MESA | 5/5 | 5/5 | 242/245 | 239/245 |
| EFPA-TRM | 4/5 | 5/5 | 237/245 | 240/245 |
| General instructions | 5/5 | 4/5 | 191/196 | 191/196 |

- All **16 disagreements** with the fixed key answered Contradicted where the key specifies Not established: P6B (7), P5A (4), C8 (3), C6 (1), and C7 (1). The P6B label is debatable; disagreements are not all independently established errors.
- All **322** related-claim comparisons changed or stayed the same as expected; **310** had both expected labels. No unjustified negative claim was supported (**0/84**).
- MESA supplied **250 choices**, with **12/50** question–benchmark pairs varying and **435/500** repeated-choice pairs matching. Five varying pairs included both No and Not sure. All DesignQA answers to questions 8 and 12 were Partly.
- Six selected reviews use repetition 1 from each method. The selected MESA review answers DesignQA question 23 Not sure and question 24 Partly. Its missing reviewer-error counts also appear under documented problems, illustrating the difficulty of separating missing information from negative findings.

Only MESA receives a completed example, so differences concern the complete supplied materials. The model outputs do not establish easier human use or effects on collaboration. Section VI-B of that manuscript discusses how engineers could compare reasons about score variation, repeated testing and reuse rules, without treating either No or Not sure as automatic rejection.

A human author checked an earlier six-review set, including the four comparison-method reviews used here. The author reviewed the two MESA responses against the supplied passages, checked their interpretation, and reviewed the expected answers, including the disputed P6B label. These author checks do not constitute independent validation. OpenAI Codex prepared the current analysis; Claude Opus 5.5 assisted with the comparison batches and their initial analysis, from the same model family as reviewer Claude Sonnet 5.5.

See the [study guide](CHASE-study.md), [reporting selection](surveys/colleague-review/mesa-study/chase-report/selection.json), [results](surveys/colleague-review/mesa-study/chase-report/summary.json), and [selected-review audit](surveys/colleague-review/mesa-study/chase-report/selected-reviews.md).

## Sources and supporting records

EFPA provides the conceptual source for the adaptation. BetterBench informs questions about benchmark implementation, documentation, and maintenance. Measurement research informs questions about whether tasks and scores support the intended claims. The proposed correspondences and omissions are documented in the [adaptation map](supporting/adaptation/adaptation-map.md); they do not imply EFPA endorsement or equivalent coverage.

| Location | Contents |
| --- | --- |
| [literature/](literature/README.md) | Source index, thematic reading guide, [original PDFs](literature/pdfs/), [extracted transcriptions](literature/transcriptions/), and [benchmark documentation notes](literature/notes/benchmark_official_documentation_inventory.md) |
| [references.bib](references.bib) | Shared manuscript bibliography |
| [supporting/adaptation/](supporting/adaptation/adaptation-map.md) | EFPA–MESA correspondence map and [ACM SIGSOFT empirical standards assessment](supporting/adaptation/standards-assessment.md) |
| [supporting/retrai-paper/](supporting/retrai-paper/thesis/README.md) | Supporting RETRAI manuscript records: [detailed adaptation template](supporting/retrai-paper/MESA%20EFPA%20template%20official.md), [scorecard](supporting/retrai-paper/MESA%20scorecard.md), [pilot reviews](supporting/retrai-paper/reviews/), and [thesis notes](supporting/retrai-paper/thesis/) |
| [supporting/editorial/](supporting/editorial/CHASE-review-response.md) | CHASE review response and editorial notes |
| [mesa_paper.tex](mesa_paper.tex) | Current REFSQ manuscript: framework comparison, rubric study, and requirements traceability proposal |
| [paper.tex](paper.tex) and [paper_old.tex](paper_old.tex) | Preserved RETRAI submission manuscript and preserved older manuscript |
| [tools/](tools/) | Scorecard and thesis verification scripts |
| [CHASE reporting records](surveys/colleague-review/mesa-study/chase-report/README.md) | Historical questionnaire selection, results, source links and traceability |
| [Earlier model studies](CHASE-study.md#archived-records) and [archive index](provenance/archive-index.md) | Archived series and relocated-file provenance, not pooled with the current study |

The source survey, benchmark reviews, and preserved manuscripts remain available. Questionnaire choices should not be converted into the numerical ratings used in supporting review documents.

## Reproduce the historical questionnaire analysis

The [study guide](CHASE-study.md#reproduce-the-offline-analysis) gives Python commands for regenerating results from saved responses. Running those commands does not launch model experiments or send survey submissions. Exact inputs, raw outputs, expected test-case answers, and file fingerprints are retained separately.

Both companion manuscripts (`mesa_paper.tex` and `paper2.tex`) compile to PDF locally via Tectonic / BasicTeX using `llncs.cls` and `splncs04.bst` in the workspace root. Both are verified at exactly 15 pages including references, adhering to the REFSQ LNCS ceiling.

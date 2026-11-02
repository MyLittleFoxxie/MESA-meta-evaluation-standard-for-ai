# Study files

Entry point for the agent sessions of the two studies. Status: materials built, all ten checks of the protocol done, inputs frozen on 31 October 2026; see `outputs/` and `analysis/` for the sessions and their analysis. See [protocol.md](protocol.md).

| File or folder | Role |
|---|---|
| `fetch_sources.py`, `sources.json`, `sources/` | fixed snapshots and paper text for the four benchmarks and the pilot fixture |
| `pdftext.swift` | paper text extraction with PDFKit |
| `build_materials.py`, `materials/` | system instruction, teaching example, one framework packet and one schema per framework, the rubric in machine form |
| `jobs.json`, `prompts/` | 33 jobs (7 pilots, 18 framework sessions, 8 rubric sessions) and one prompt per job |
| `sizes.py`, `sizes.csv` | prompt and input sizes, for information |
| `earlier_reviews.py`, `earlier-reviews/` | the existing framework applications transcribed to item level |
| `export_hle_text.py` | text export of the gated Humanity's Last Exam question file into the snapshot; requires pyarrow; output gitignored |
| `file_server.py` | read only file server confined to one snapshot |
| `run.py` | the session runner; main sessions refuse to run before the freeze |
| `validate.py`, `analyze.py` | offline validation and analysis; writes `analysis/` |
| `run_addition.py`, `addition.md`, `analysis/addition-repeat.json` | amendment 1 after the main sessions: a second repetition of BetterBench and the Scorecard on HumanEval with the frozen prompts, and its repeat agreement |
| `disagreements.py`, `analysis/coding/` | after the sessions: the disagreement log context, the pairwise agreement table and the merged source check and disagreement cause files, coded by the preparing assistant per benchmark under `analysis/coding/` and merged into `analysis/disagreement-log.csv` and `analysis/source-check.csv`; `analysis/rq4-source-check.csv` and `rq4-source-check-part-a.csv` are the blank checklists for the author's own check |
| `outputs/` | one folder per job and attempt: metadata, event log (`events.jsonl`), standard error and the verbatim structured response (`response.txt`); verification of all six HLE `events.jsonl` logs confirmed that no HLE session called `read_file` on `data/hle-test.jsonl` (only `list_files` listed its path and byte size), so the event logs contain no gated question text |
| `synth.py` | synthetic responses for a dry run of the analysis, written to a separate folder |
| `test_harness.py` | fixture tests, no model calls |
| `freeze.py` | writes `freeze-manifest.json` once |

Commands, from the repository root, none of which calls a model:

```
python3 v4/study/fetch_sources.py
python3 v4/study/build_materials.py
python3 v4/study/sizes.py
python3 v4/study/earlier_reviews.py --betterbench <database.html> --abc <tau-bench.yaml>
python3 v4/study/test_harness.py
python3 v4/study/synth.py --out v4/study/dry-run && python3 v4/study/analyze.py --outputs v4/study/dry-run --analysis v4/study/dry-run-analysis
```

Sessions, which do call a model and are not authorized by this file:

```
python3 v4/study/run.py --phase pilot
python3 v4/study/freeze.py
python3 v4/study/run.py --phase main
python3 v4/study/analyze.py
python3 v4/study/disagreements.py
```

Known limits recorded before any session: the earlier review comparison is a proof of concept on BetterBench only (HumanEval and TruthfulQA); the Scorecard, ECBD and OECD frameworks have no earlier review among the benchmarks, and Humanity's Last Exam has none under any framework; its gated dataset file was obtained by the author and exported to text inside the snapshot for the agents (`export_hle_text.py`), gitignored and excluded from the public package; the checklist's τ-bench assessment is kept as reference data and not compared; Benchmark Caliper is mapped but not applied. A pilot is a full session with the complete framework packet on a fictional two task benchmark, used to catch harness and schema failures; its judgments are not analysed.

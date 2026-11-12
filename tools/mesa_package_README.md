# Replication package: reviewing AI benchmarks as evidence for requirements

This package accompanies an anonymous submission to REFSQ 2027. It contains what a reader needs to check the numbers in the paper. It contains no author names. It was built by copying files, without version history.

## 1. Purpose and contents

The paper sorts the 280 questions of seven benchmark review frameworks into 30 concerns, derives a rubric of 39 criteria, and reports two studies in which language models apply the frameworks and the rubric to four benchmarks.

| Folder | Content |
|---|---|
| `v4/mapping/` | The 280 items, their concerns (`mapping.csv`), the 30 concerns (`concerns.md`), the rules that translate framework answers into three verdicts (`recoding-rules.md`), and a check script |
| `v4/study/` | Study 1: protocol, prompts, settings (`jobs.json`), the manifest that fixes the inputs, every model response (`outputs/`), analysis scripts and outputs (`analysis/`) |
| `v4/study/sources/` | The repositories of the four benchmarks at the versions used, under their own licenses, and `snapshot.json` with the source and hash of every file |
| `v5/rubric/` | The rubric text used in Study 2 (`rubric.md`) and a later edit (`rubric-v5.1.md`) that no session used |
| `v5/study/` | Study 2, Claude sessions: protocol, prompts, manifest, responses, analysis, and the audit of ratings against sources |
| `v5/study-cycle2/` | Study 2, Gemini sessions and the three checks: protocol with amendments, the six benchmark copies with planted defects (`sources/`), the list of known defects, the confirmation script and its results, analysis, the record of deviations (`deviations.md`), and the supplemental audit of the paper's numbers |
| `checks/` | A script that recomputes the counts in the paper's tables from the files above |
| `PACKAGE_REPORT.json` | What was left out of this package and why |

Names in the files: the records call the two parts of Study 2 "cycle 1" and "cycle 2", and call the three verdicts favorable, unfavorable and unresolved (Satisfied, Unsatisfied and Open in the paper). Folder `v5/study/` calls itself Study 3 in some records; the paper calls it Study 2.

## 2. What is left out, and where to get it

- **Benchmark papers** (`paper.pdf`, `paper.txt` in each snapshot) and the packed copies of the repositories: we do not have the right to redistribute the papers. `v4/study/sources.json` gives the address, version and SHA-256 hash of each, and `v4/study/fetch_sources.py` downloads them again.
- **The questions of Humanity's Last Exam**: access is gated by its authors. Request access from the dataset's page and place the file as `sources.json` states.
- **Two files of the blind rating that was planned and not carried out** (the sheet and its key). `v5/study-cycle2/deviations.md` describes them.
- Files listed under `left_out_identifying` in `PACKAGE_REPORT.json`, if any: files fixed by a manifest that contain text identifying the authors. They are left out and not edited.

In other text files, the user name in local file paths was replaced by a neutral word. `PACKAGE_REPORT.json` lists these files. No file fixed by a manifest was changed. Because the papers are left out, the manifest checks (`freeze.py --check`, `test_harness.py`) report those files as missing until they are downloaded.

Framework items are quoted where the license or the framework's authors allow it; How2Bench items and the OECD chapter are paraphrased with source locations (see `v4/README.md`).

## 3. Software

Python 3.10 or later. The analysis and check scripts use only the standard library. Two scripts need more: the confirmation script for one benchmark imports that benchmark's own code from its repository, and reading the gated question file needs `pyarrow`. No script in this package calls a model unless you run `run.py`, which needs your own access to the models.

## 4. Installation

Linux or macOS:

    python3 --version        # 3.10 or later
    cd mesa_replication_package

Windows (PowerShell):

    python --version         # 3.10 or later
    cd mesa_replication_package

No installation step is needed for the checks below. On Windows, use `python` where the commands say `python3`. Keep line endings as they are (for Git: `git config core.autocrlf false`), because the manifests compare hashes.

## 5. Reproducing the tables

Run from the package root.

| Table in the paper | Command | Where to look in the output |
|---|---|---|
| Table 1, items per framework | `python3 checks/check_paper_numbers.py` | `items_by_framework`, `items` |
| Table 2, concerns and links per step | same | `links_by_step`, `concerns_by_step`, `links` |
| Table 3, levels and outcomes | none (definitions) | `v5/rubric/rubric.md` |
| Table 4, causes of disagreement | same script | `causes`; the rows are in `v4/study/analysis/disagreement-log.csv` |
| Table 5, Study 2 results | open `v5/study-cycle2/analysis/summary.json` | `claude_cycle1`, `gemini_cycle2`, `cross_family`, `seeded_fixtures`, `known_defects` |
| Numbers in Section 5 not in a table | `python3 v5/study-cycle2/supplemental_paper_audit.py` | writes `v5/study-cycle2/analysis/supplemental-paper-checks.json` |

Expected output of the check script, in part: `"items": 280`, `"links": 386`, `"comparisons": [159, 302]`, `"causes": {"missing_rule": 42, "granularity": 50, "reading": 42, "threshold": 8, "sources": 1}`.

The count of known defects for Gemini in the paper (3 of 7) differs from `summary.json` (4 of 7). One automatic match was a different defect; `deviations.md`, section 3, explains the correction.

To rebuild the analysis outputs from the model responses, run `python3 v4/study/analyze.py`, `python3 v5/study/analyze.py` and `python3 v5/study-cycle2/analyze.py` after downloading the left out sources.

## 6. Using the material on another benchmark

1. Make a snapshot: a folder with the benchmark's repository and the text of its paper, and an entry in `sources.json` (see `v4/study/fetch_sources.py`).
2. Add jobs for the snapshot to `jobs.json` in `v5/study-cycle2/` and build the prompts with `build_materials.py`.
3. Run the sessions with `run.py`. This needs access to a model and the agent program named in the protocol.
4. Run `analyze.py`. For a rating with a failed outcome, write a check in the style of `confirm_defects.py`.

## 7. License

See `LICENSE`. Code is under the MIT License and our data and text under CC BY 4.0. Third party material keeps its own license.

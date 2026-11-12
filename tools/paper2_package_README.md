# Replication package: benchmark audit and a coding agent requirement on SymPy

This package accompanies an anonymous submission to REFSQ 2027. Author names and user names in file paths were replaced by neutral words.

## 1. What the study is

One coding agent (GPT-6.1 Sol at medium effort, run through the Codex command line agent) worked on 88 SymPy bug reports, one session per task: 44 source tasks from SWE-bench Verified and 44 target tasks that were fixed after the model's training cutoff. Before the sessions, the benchmark was reviewed with seven criteria of the MESA rubric and with the Agentic Benchmark Checklist. The analysis compares what several decision methods conclude from the same sessions.

## 2. Contents

| Path | Content |
|---|---|
| `paper2/preparation/protocol-6/` | The study reported in the paper: protocol, requirement, task lists, prompts, session records and patches (`sessions/`, `ledger/`), checks made before the sessions (`audit_checks/`), rating runs and final ratings (`audit_forms/`), and the manifest that fixes the inputs |
| `paper2/method/` | The decision method in three levels |
| `paper2/preparation/*.py` | Code for task selection, the checks, the session records, the analysis (`cases.py`) and the replay (`replay.py`) |
| `paper2/records/` | The SWE-bench Verified rows for SymPy and the pool of target tasks |
| `paper2/tests/` | Unit tests |
| `v5/rubric/` | The text of the MESA rubric |
| `supporting/editorial/round3_checks/check_paper2_numbers.py` | A script that recomputes the numbers printed in the paper |
| `paper2/preparation/protocol-4/`, `protocol-5/`, `v3/`, `paper2/history/`, `paper2/pilot/`, `paper2/protocol/`, `paper2/feasibility/` | Earlier preparation. The paper does not report it. It is included because the code of the reported study reuses files from it (task eligibility records, test images, saved check patches) |

One extra session on a task outside the two task sets was run first to test the setup. It is in the records (slot 1) and is not part of the 88 sessions in the paper.

## 3. What is left out

- The raw event logs of the agent sessions (`sessions/*/logs/`), because of their size. Each session keeps its prompt, its patch, its run record and a summary of the log with the hash of the raw log.
- SWE-bench Docker images and SymPy sources. The scripts fetch them from their public locations.

## 4. Software

Python 3.10 or later. The analysis and the number check use the standard library only. Grading needs Docker and the `swebench` Python package in a separate environment, as `paper2/preparation/README.md` describes. No step in this README calls a model.

## 5. Reproduce the numbers

Run from the top folder of the package.

```sh
python3 supporting/editorial/round3_checks/check_paper2_numbers.py   # thresholds, power, bounds, session times, agreement, probe counts
python3 -m paper2.preparation.cases --protocol 6                     # decisions of every method, differences, removal in three ways
python3 -m unittest discover -s paper2/tests -p 'test_*.py'          # unit tests
```

| Table in the paper | Source |
|---|---|
| Thresholds | first lines of the number check |
| Weak test check | `paper2/preparation/protocol-6/task_checks.json` and `audit_checks/b07_scope_rule_summary.json` |
| Ratings | `paper2/preparation/protocol-6/audit_forms/completed/` |
| Results and removal in three ways | output of `cases --protocol 6` |
| Exposure probe | `audit_checks/exposure-probes-sol-target-summary.json` |

## 6. Use on another benchmark or agent

`paper2/method/evidence.py` holds the three levels of the decision method. A new case needs a requirement file like `protocol-6/requirement.json`, one rating form per criterion like those in `audit_forms/completed/`, and session records like those in `sessions/`.

## 7. License

See `LICENSE`. Code is under the MIT License and our data and text under CC BY 4.0. Third party material keeps its own license: the SWE-bench rows, SymPy issue texts and SymPy patches stay under the licenses of their projects.

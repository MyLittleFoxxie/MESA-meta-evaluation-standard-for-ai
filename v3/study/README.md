# Benchmark audit study records

The Codex batch completed on 30 October 2026: twelve main sessions and two retained pilot sessions, fourteen physical attempts. All twelve main responses pass structural validation and all six repository sessions used the file tools. The repository pilot had a tool approval failure and is retained separately. No retries were made.

The Claude batch completed later the same day under [claude/](claude/): twelve main sessions and three pilot attempts, fifteen physical attempts. The first documents pilot attempt failed before any model request because Claude Code rejected the schema declaration key; it is retained. All twelve main responses pass structural validation and all six repository sessions read files through the tool server. See the [Claude protocol](claude/protocol.md), [Claude jobs](claude/jobs.json), [Claude freeze](claude/freeze-manifest.json), [Claude results](claude/analysis/summary.md), [cross batch comparison](claude/analysis/cross-batch.json) and [Claude selected audit](claude/analysis/selected-reviews.md). The analyst for the Claude batch is the same model as its reviewer.

The requested model was gpt-6-luna with medium reasoning effort. See [protocol.md](protocol.md) for isolation, pilot changes, source limits and failure rules; [jobs.json](jobs.json) for the fixed schedule; [freeze-manifest.json](freeze-manifest.json) for the material fingerprints; and [sources.json](sources.json) for repository commits and paper hashes.

The instrument is the MESA benchmark audit rubric with ten criteria, not the earlier questionnaire. See [rubric](materials/rubric.md), [response schema](materials/response-schema.json) and [reference proposals](analyst/references.json). All references are assistant prepared and provisional or contested. No human checker or expert ground truth is claimed.

Results are in [summary](analysis/summary.md), [runs](analysis/runs.csv), [answers](analysis/answers.csv), [citations](analysis/citations.csv), [access transitions](analysis/transitions.csv), [repeat agreement](analysis/repeat-agreement.csv) and [selected response audit](analysis/selected-reviews.md). The manuscript is [paper_mesa_v3.tex](../../paper_mesa_v3.tex). Its tables are generated from the saved outputs; semantic interpretations are separately authored and disclosed.

Reproduce the offline analysis with `python3 v3/study/analyze.py` and `python3 v3/study/claude/analyze.py`. Check integrity with `python3 v3/study/verify.py` and `python3 v3/study/claude/verify.py`. These commands make no model calls. The source fetch script requires network access and the bundled pypdf package; it never executes benchmark code. Source archives and binary datasets are kept locally, with hashes for retrieval. They are not automatically published.

`python3 v3/study/run.py --phase main` and `python3 v3/study/claude/run.py --phase main` verify their freezes and skip every existing attempt. Neither replaces a response. Both batches are complete and need no further execution. The `claude` field in the frozen Codex `jobs.json` records the pending status at the Codex freeze; the Claude batch has its own `claude/jobs.json`.

The existing survey is excluded. Human evaluation is outside CHASE and deferred. No LaTeX compilation or automatic PDF preview was performed; layout and page length are unchecked. Nothing has been committed, pushed or published by this execution.

## Verification

The Codex verifier result is in [verification.json](analysis/verification.json) and [source checks](analysis/source-checks.json); the Claude verifier result is in [claude verification](claude/analysis/verification.json). Both check frozen hashes, every main response record, tool boundaries and deterministic analysis; the Codex verifier also checks the manuscript's citation keys, LaTeX structure and local links. Consult the generated reports for check counts. Locator checks establish parseable page or line bounds, not that the quoted words occur at that location. Unprefixed repository paths are resolved within the snapshot for citation checks without altering raw responses.

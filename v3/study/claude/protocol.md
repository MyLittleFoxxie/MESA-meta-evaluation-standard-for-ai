# Claude batch protocol

Prepared on 30 October 2026, after the Codex batch had completed. The user instructed that the pending Claude batch be run with Claude Fable 5.1 at medium reasoning effort through Claude Code. This is a later, sequential batch. It is not jointly randomized with the Codex batch, and differences between the batches cannot be attributed to the command line tool alone: provider, model, tool and harness differ together.

## Scope and budget

Same three benchmarks, ten criteria, two access conditions and two repetitions: twelve main sessions. Two pilot sessions use the fictional AddTwo fixture. The attempt budget is sixteen physical attempts for this batch, including pilots and at most two manual infrastructure retries. No study imposed per session token, output, tool call or time ceilings. Account limits still apply. The runner stops at the first failure and never retries automatically.

## Instrument and inputs

The instrument, response schema, system instruction, teaching example, prompts, source snapshots and assistant reference proposals are the files frozen for the Codex batch. Prompts are byte identical; the prompt hash of each attempt is recorded and checked. The repository prompt names the tools as `benchmark.list_files` and `benchmark.read_file`, which is how Codex exposes them. Claude Code exposes the same server tools as `mcp__benchmark__list_files` and `mcp__benchmark__read_file`. The prompt text was not changed for this batch; the pilot establishes whether the tools were found under those names.

The analyst reference proposals were prepared by the Codex assistant before the Codex batch and are unchanged. They remain provisional or contested and are withheld from reviewers.

## Model and isolation

Requested model: `claude-fable-5-1`; effort: `medium`. The Claude Code version is recorded in each attempt. The returned events report the model identifier used by the serving system; this is the identifier, not independent confirmation of a weights snapshot.

Each session runs `claude -p` in an empty temporary directory with the prompt supplied on standard input. The runner replaces the default system prompt with the study system instruction, loads no user, project or local settings, disables skills, disables every built in tool, uses only command line supplied MCP servers, denies any permission prompt, requests structured output against the response schema, and does not persist the session. Documents sessions receive no MCP server. Repository sessions receive only the confined file server used for Codex, allowed for its two read only tools. The file server has no network, write or execution functionality and rejects paths outside the snapshot.

Authentication uses the existing local Claude Code login. No API key, Codex key or Claude Code environment variable is passed into the session, and no secret appears in prompts or records. The emitted events do not expose the complete initial server request; Claude Code may add its own scaffolding around the replaced system prompt. Full prompt isolation therefore cannot be proven from the event records alone.

## Pilot and harness changes

Both pilots are recorded under `outputs/pilot-*`. Any harness change made after the pilots is listed here before the freeze. The rubric, prompts and sources are never changed in response to pilot judgments.

Pilot outcome, recorded before the freeze:

- `pilot-documents-1` attempt 1 failed before any model request. Claude Code rejected the frozen response schema because its `$schema` key names JSON Schema draft 2020-12, which the CLI validator does not recognize. The attempt is retained with its error output and counts against the budget.
- The runner was changed to remove only the `$schema` metadata key from the schema text passed on the command line. The frozen schema file is unchanged and the validation rules are identical. A `--retry` option was added so that a retained failed attempt can be followed by a numbered later attempt; it is never automatic.
- `pilot-documents-1` attempt 2 and `pilot-repository-1` attempt 1 then completed. Both responses pass structural validation. The repository pilot listed the files and read both files through `mcp__benchmark__list_files` and `mcp__benchmark__read_file`, although the prompt names the tools in the Codex form. The prompts therefore remain byte identical to the Codex batch.
- Structured output is delivered through a CLI tool named `StructuredOutput`. Its call is the response mechanism, not a source tool, and is excluded from tool boundary checks by name.
- The result events report usage for a second model, `claude-haiku-5-5`, with a few thousand input tokens and about two hundred output tokens per session. This is an auxiliary call made by Claude Code itself, not by the runner. Its purpose and inputs are not exposed in the events. The review content is produced in messages whose model field is `claude-fable-5-1`. This auxiliary call is a harness difference from Codex and is disclosed as such.
- Claude Code reports input tokens in three fields: uncached input, cache creation and cache read. The analysis sums all three as input tokens. The totals are not comparable to Codex accounting or to a price.

Three physical attempts were used by the pilots, leaving thirteen under the cap: twelve main sessions and one manual retry.

## Allocation and stopping

`jobs.json` fixes the twelve main jobs with order randomized within repetition blocks using seeds 20261033 and 20261034. Sessions run sequentially. One manual retry may be scheduled for a failure before generation, within a pool of two additional attempts. Completed invalid responses and condition delivery failures are retained and not replaced. Stop on an account usage limit, model unavailability or unexpected runner failure.

## Reporting

Report planned, attempted, completed, structurally usable and condition delivered counts for this batch separately from the Codex batch. Comparisons between batches are descriptive counts over paired judgments, not provider rankings. The analyst for this batch is the same model as the reviewer; this is disclosed wherever the Claude responses are interpreted. No human survey result, aggregate benchmark quality score or accuracy against experts is produced.

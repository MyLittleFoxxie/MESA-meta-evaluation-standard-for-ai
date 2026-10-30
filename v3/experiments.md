# Experiment design for version three

Status: both batches completed on 30 October 2026. The Codex batch used `gpt-6-luna`, medium effort: twelve main sessions and two pilots, no retries. The later Claude batch used `claude-fable-5-1` through Claude Code, medium effort: twelve main sessions and three pilot attempts, including one retained harness failure before any model request. The [Codex protocol](study/protocol.md), [Claude protocol](study/claude/protocol.md), [Codex analysis](study/analysis/summary.md) and [Claude analysis](study/claude/analysis/summary.md) document what occurred. The design below remains a record of the scope selected for the first batch; its preconditions were resolved in the study records.

## Questions

These model experiments support the CHASE paper. Human survey results belong only in a future REFSQ extension and are not a prerequisite for these experiments or for completing CHASE. Author checks of sources and reference records are research preparation, not a participant survey or evidence of human usability. Ignore the existing survey for v3: its materials, responses and analysis plan are not study inputs or dependencies. Leave its files untouched. Human evaluation planning is deferred until requested.

1. Which judgments and supporting claims can agents substantiate from the evidence they receive?
2. How do answers and supporting claims change when repository access is added for the same model configuration?
3. How do judgments and evidence claims vary between two repetitions of the same configuration?

There is no observed comparison between instruments. Findings concern each model and harness separately. The [Claude batch](study/claude-pending.md) ran after the Codex batch under a later user instruction with its own attempt budget of sixteen. The two batches are compared descriptively by paired judgments; they were not jointly randomized, and provider, model, command line tool and harness differ together.

Software findings and interpretation findings are analysis categories, not two scores or a claim that each criterion belongs exclusively to one category. Freeze the claim classification before observing responses. Permit overlap and report it.

## Study size

Use HumanEval, TruthfulQA and DesignQA to cover programming tasks, truthfulness questions and engineering documentation. This selection is a scope and budget choice, not a representative sample. HLE and ARC-AGI-2 are outside the main study. Freeze each edition, intended interpretation, paper revision, repository commit and accessible data subset. Record inaccessible materials; do not substitute cases after seeing results.

| Stage | Benchmarks or fixtures | Models | Access conditions | Repetitions | Sessions |
| --- | ---: | ---: | ---: | ---: | ---: |
| Main study | 3 benchmarks | 1 | 2 | 2 | 12 |
| Development pilot | 1 fictional fixture | 1 | 2 | 1 | 2 |
| Total planned | | | | | 14 |

Reserve at most two additional attempts across the whole study for infrastructure failures before generation, giving a hard cap of 16 attempts. These are not extra repetitions. Retain failed attempts and stop at the cap even if the matrix is incomplete. Do not replace invalid completed responses.

A complete main study contains 120 criterion judgments. These are nested in 12 sessions across three benchmarks, not 120 independent observations. Two repetitions provide only a check on observed variation, not an estimate of long run stability. Each session reviews one benchmark; do not combine benchmarks into a session to disguise token use or introduce review history.

The previous plan required 60 sessions for one instrument or 120 for both. Twelve main sessions reduce those counts by 80% and 90%, respectively. These percentages concern session counts, not guaranteed token or subscription savings. Retaining all five benchmarks would require 20 main sessions; that expansion is not scheduled.

## Model and usage accounting

Use the cheapest available model compatible with the frozen task. As checked on 30 October 2026, select `gpt-6-luna`, available in this session, at medium reasoning effort. The [official credit rates](https://learn.chatgpt.com/docs/pricing) place it below the other exposed models, including GPT-5.6 Luna. Use Standard speed where the chosen runner supports it. Availability here does not prove availability in the eventual command line runner; verify its model selection and returned identifier without starting the main study.

If the model is unavailable, record the blocker; do not silently upgrade or switch providers. Recheck the cheapest compatible option before freezing. Once frozen, keep that identifier and configuration for both conditions. This instruction sets the experiment model; it does not change the model running the planning chat.

Run sessions sequentially. Perform parsing, hashing, source checks and analysis locally without model calls where possible. Do not use additional model judges, autonomous review loops or automatic retries after generation. Prepare source files once and reuse their frozen snapshots. Ask for concise evidence records, not narrative reports.

Do not impose study specific per session token, output, tool call or time ceilings. Use the two pilot sessions to measure consumption and assess feasibility before the main study. Record input and output tokens where available, tool calls, elapsed time, source omissions and truncation. Record platform limits separately from study design choices. The pilot does not automatically introduce new per session ceilings.

Stop on an account usage limit; preserve completed work without polling or restarting automatically. Retain the total cap of 16 attempts, including the pilot and permitted retries.

Subscription usage is not inferable from API prices. Check the account's usage before execution and after the pilot, then decide whether the frozen batch fits the available allowance. Do not buy credits or switch to paid API billing automatically. The 16 attempt ceiling is fixed unless the user changes it; it does not guarantee the account has capacity for all attempts.

## Access conditions

Use the same model configuration for both conditions:

- **Documents:** the frozen paper and top level README, supplied as text; no repository or browsing tools.
- **Documents and repository:** those same documents plus the frozen repository and permitted data files, inspected with file tools. Disable external network access during review.

Keep instrument instructions, response schema, model, effort, teaching material and runner settings constant within each configuration. Record input sizes, truncation and tool allowances. Randomize launch order in blocks and save the seed and schedule before execution.

This comparison estimates the effect of adding repository access as a package: more evidence and a means to inspect it. It does not isolate tool use from information availability. Do not add a third condition or a second model in this version.

## Teaching material and separation

Do not supply the earlier completed HLE questionnaire as teaching material for the new rubric. Prepare a fictional example outside the evaluation set, with the same content in both access conditions. Record how this change differs from the current MESA study package. Do not claim to be replicating that package unchanged.

Reviewer workspaces must not expose the MESA project, current benchmark reviews, historical outputs, analyst references, organizer notes or this proposal. Treat repository text as evidence, not instructions. Disable inherited project instructions, memory and plugins; verify isolation using a fixture before launching study sessions.

## Reference preparation

Prepare references before main model runs for each benchmark and criterion under each access condition: 3 × 10 × 2 = 60 reference records. They may share a source ledger, but access specific judgments remain separate.

Each record contains benchmark edition, intended use, criterion ID, access condition, supporting source and locator, expected rating or evidence status, permitted alternatives, missing information, contradictions, scope, preparer, checker and decision history. Mark records as settled, contested or unresolved. A rating also requires its criterion anchor.

Keep two questions distinct: what the permitted evidence supports and what a broader source review suggests about the benchmark. Do not penalize a documents response for failing to cite evidence unavailable to it. A missing fact generally supports uncertainty, not a negative finding. Documentation questions still concern whether the required description is present.

Published reviews can supply evidence within their scope and version. They do not automatically provide scores for this rubric or a human expert baseline. If two people independently judge records, preserve both initial records and any later resolution. If one author checks assistant prepared references, report exactly that. Leave reviewer identities and completion fields empty until the work occurs. Contested records remain visible and receive sensitivity analysis, not forced consensus.

For the main access comparison, agents receive only the defined source sets. Published critiques used by analysts must not turn a narrower source condition into an unfair accuracy test. Claims requiring those critiques belong in a separate, explicitly labeled broader evidence analysis.

## Repository checks

Separate file presence, content inspection, static analysis and execution. The default experiment inspects files; it does not run a benchmark or prove reproduction. If execution becomes part of the design, specify commands, inputs, dependencies, sandbox permissions and resource limits before freezing. Execute only declared checks, recording output and environment.

Examples of checkable claims include a license statement at a location, a dependency file naming a package, or a scoring function implementing an identified operation. Whether this operation supports a capability claim is a separate judgment. File existence alone is not citation correctness or scientific validity.

## Outputs and accounting

Use a common evidence ledger and rubric judgments. Each judgment includes ID, rating or evidence status, short reason, evidence locators, missing information, checks performed and limits. Missing evidence does not require an invented quotation. Preserve the response as generated before parsing.

Record run ID, instrument version, benchmark snapshot, access condition, repetition, prompt hash, model requested and returned, CLI version, settings, start and end, exit status, token and cost fields where available, events, tool calls, stdout, stderr and parse status. Keep unavailable fields null; do not infer costs or model snapshots.

Permit one retry only for a documented infrastructure failure before generation. Retain that attempt separately. Do not repair or replace a completed invalid response. Record partial and truncated outputs, access violations, timeouts and unstarted jobs. Report planned, attempted, completed and usable denominators separately. Freeze any partial analysis rule before running.

## Analysis

Report rating distributions and insufficient evidence, not applicable and unanswered separately. Exact agreement and an explicitly defined ordinal disagreement measure can be considered once anchors exist. Numerical spacing does not by itself justify interval scale assumptions, mean absolute error or intraclass correlation. Do not interpret a mean difference as leniency without examining which claims and anchors caused it. Do not calculate a total benchmark score.

For each response, inspect evidence in four steps: does the cited artifact exist, does the locator resolve, does its content match the response, and does it support the claim? Automated checks can establish the first steps; semantic support requires recorded review. State who performed that review. Do not use the reviewer model's own judgment as independent confirmation.

Report unsupported positive claims and unsupported negative claims separately, with their denominators. Treat reference agreement as agreement with that reference, not proof of benchmark quality. Report failure rates before analyses restricted to usable responses.

Summarize by benchmark, configuration, condition and repetition before aggregating. Use within configuration access contrasts. With three selected benchmarks, emphasize effect descriptions and variation; avoid treating questions, claims or repetitions as independent samples in significance tests. Any uncertainty estimate must state its unit and assumptions.

Compare logged model resources only as model resources, not human workload. Report repeat agreement descriptively for the two responses in each benchmark and access cell. Do not claim superiority over another model, validation of the rubric or general human usability.

## Files to implement

Keep the following in `v3/study/` when implementation begins:

- `protocol.md`, `analysis-plan.md`, `instrument-map.md` and `sources.json`.
- `materials/` for the instrument snapshots, definitions, example and document packets.
- `analyst/` for reference records, alternatives and author checks, excluded from reviewer workspaces.
- `prompts/`, `jobs.json` and `freeze-manifest.json` for exact inputs, schedule and hashes.
- `run.py`, `validate.py` and `analyze.py` for execution, structural checks and saved response analysis.
- `outputs/` for all attempts; `analysis/` for generated tables and manuscript traceability.

Before running, test the harness without model calls for access isolation, exact instrument counts, the ten criterion IDs and allowed ratings and evidence statuses, null handling, duplicate or unknown IDs, failure retention, retry limits, hash mismatch and exclusion of references. Then use a declared pilot outside the study benchmarks to check feasibility. Record pilot changes and freeze before main responses are inspected.

## Decisions needed before execution

The instrument and budget scope are selected: ten criteria, one model, 12 main sessions, two pilot sessions and no more than 16 attempts in total. Finalize rating anchors, reference reviewers, source snapshots and runner configuration. Verify `gpt-6-luna` access in the runner. Repository code execution remains outside scope. No target findings or success thresholds from the attachment are adopted.

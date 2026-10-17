# Separate Sol series — 15 October 2026

The user requested GPT-6.1 Sol for continuation. The original Astra series attempted 120 sessions: 14 process-completed and 106 process-failed. Failures include service access/usage-limit errors; process failure is not an incorrect questionnaire judgment. Raw records remain unchanged.

A separate 120-session Sol series reuses all exact frozen prompts, cases, expected labels and scheduling order. The new manifest preserves every source hash and identifies the original manifest. It is a new model series, not a retry and not a continuation pooled into Astra counts. No tests were tuned after inspecting Astra responses.

The primary reported complete-series comparisons will use Sol only if completed. Astra remains an incomplete additional-model series, with no claim of a complete second-model confirmation. The same medium effort is requested. Backend revision, temperature and generation seed remain unexposed. A bounded scheduler stops issuing jobs on the first process failure; active sessions can finish. Unattempted jobs remain explicit. This change prevents mass infrastructure failures from being mistaken for a completed evaluation.

The manuscript and analysis distinguish requested model identifiers, completed responses, invalid responses, process failures and unattempted jobs. No human observations are inferred. Existing prompts remain version 1.0; runtime and model amendment is separately documented here.

## Interrupted coordinator and retained retries (15 October 2026)

After the resumed batch was interrupted, a process check found no remaining study runner or Codex execution. Three records still marked running had no completed turn or response: `controlled-ordinary-neutral-4`, `controlled-efpa-newcomer-5`, and `controlled-efpa-newcomer-3`. Their event and error streams were retained. Their original metadata was copied to `metadata.before-interruption-finalization.json`, and metadata was finalized as process failure. The recorded finalization time is explicitly the detection time; actual termination time and exit code are unavailable. This is an execution interruption, not a failed judgment.

These three jobs and the earlier service-limit failure `real-mesa-research_assistant-3` are eligible for the protocol's single retry. Each retry has a separate `attempt-2` directory, the same frozen input and model configuration, and a fresh session. No completed invalid response is eligible for replacement. Analysis retains physical attempts separately from the 120 planned jobs. Retry-aware analysis was checked on synthetic failed-then-completed and completed-invalid-then-retry cases before the retries.

A later batch stopped on another service-limit error at `real-ordinary-benchmark_reviewer-4`, without a completed response. Six remaining jobs were left unattempted. On continuation, the account reported ordinary usage available; those six jobs were resumed. The failed ordinary-review job is eligible for the same single retained retry. No service failure is counted as a review error.

# Execution notes

The initial launch allowed at most three concurrent processes. After 31 conversations completed, `eight-efpa-newcomer-3` failed before any response or completed turn with `429 Too Many Requests`. Its events and stderr are preserved. The runner stopped scheduling and allowed active jobs to finish. The account usage tool reported ordinary usage allowed; it did not identify the cause of the service error.

The protocol permits one retained retry for this failure. Further launches reduce concurrency to two (within the predefined maximum of three); launch manifests record actual concurrency. No model, prompt, expected answer, eligibility rule or completed output is changed. Concurrency affects execution scheduling, not a measured human or model review-time outcome.

The user then selected a 30-conversation design. The controller alone received SIGINT, active reviews finished, and no new jobs were scheduled. Final accounting: 44 completed jobs, 45 physical attempts, one service failure and its retained successful retry. The remaining 136 original jobs are unattempted. The final study is separately frozen in ../main/ and does not reuse these outputs.

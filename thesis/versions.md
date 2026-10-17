# Versions and past work

Recorded on 2026-09-25 before editing the framework or paper. [baseline.json](baseline.json) lists the starting Git commit, each file's last commit, and SHA-256 hashes. A hash identifies exact file contents; it does not establish when a review was performed.

- The current full template has 87 rating fields. The scorecard has 40.
- The nine pilot reviews say they used an earlier 89-item template. Exact template commits used during those review sessions are not recorded in their version notes.
- Some review text conflicts with those notes: the Claude HLE draft calls its template “v2” near the start. Preserve both statements and treat the exact historical version as unresolved.
- The existing migration plan records four retired IDs: 2.6 into 2.9, 4.10 into 2.4, 10.6.2 into 10.6.1, and 11.3.2 into 11.3.1. Only the latter two reduce the rated-item count.
- All three pilot benchmarks occur in the paper's 15-benchmark construction list. They are development examples, not unused test cases.
- The 40 scorecard items were selected using those pilots. Their retention of known findings does not establish retention on other benchmarks.

The old feedback files are records of earlier reasoning, not proof that every recommendation was implemented or correct. For example, `feedback/95-mesa-core-plan.md` discusses an 84-item proposal, while the actual current template has 87.

The new source mapping is an explanation prepared now. It should not be described as a contemporaneous record of the original construction process. The nine original reviews remain unchanged.

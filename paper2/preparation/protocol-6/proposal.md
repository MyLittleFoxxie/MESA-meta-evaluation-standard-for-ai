# Protocol 6: proposal

Status: proposal, written on 11 November 2026 after REFSQ review round 1. It is not in force. Protocol 5 stays the current protocol. Nothing in `paper2/method/`, `paper2/tests/`, the policies, the signed forms or the records was changed for this proposal. Adopting any part needs the author's decision, changes to code and tests, and new signatures as listed at the end.

## Why

All three round 1 reviewers of Paper 2 scored reject for reasons that the text of the paper cannot fix ([round 1 record](../../../supporting/editorial/refsq_review_round_1.md)):

1. The MESA outcome is fixed before any session. B28a failed for the whole release, so both policies return No decision for every agent. The sessions cannot change the answer to RQ1, and MESA drops out of RQ2.
2. The gate ignores a control the study already has. The session validity rule marks a session invalid when it edits the test runner or test configuration. That rule blocks the B28a exploit in each session, and the gate gives no credit for it.
3. The design has almost no power. With 14 to 20 tasks and a threshold of 0.70, an agent with a true rate of 0.75 is Inconclusive about 97% of the time, so RQ2 will mostly compare Inconclusive with Inconclusive.
4. The direct test is treated as the reference, and the B05 and B07 checks were applied to the source tasks only.
5. No success criteria are stated before the sessions.

## Proposed changes

### P6-1. A third policy that accepts a per-session control for a release defect

Add `POLICY-P6-CONTROLLED` beside the strict and the lenient policy. Under it, a criterion whose form records a located defect of a shared component (B28a here) has status Admissible for a case when all three hold:

- the form names a control that blocks the defect in one session (for B28a: the session's patch changes no test runner script and no test configuration file);
- the control is checked by code on every observation of the case, from the patch and the session log, and the result is stored with the observation's provenance;
- every retained observation passes the check. An observation that fails it is invalid, as under protocol 5.

The strict and lenient policies stay as they are and keep returning No decision. The paper would then report three MESA outputs, and one of them can issue a decision. This answers reviews items 1 and 2. It needs: a new field on the form or a control record, a rule in `evidence.py`, tests, and a statement in the paper that the control covers only the exploit that was shown.

B14a also fails under the strict policy and is omitted by the lenient one. The controlled policy would treat B14a as the lenient policy does and report the target tasks, which are after the cutoffs, as the check on exposure.

### P6-2. Use the budget for power instead of two agents

The budget stays at 90 sessions of at most 15 minutes. Options, for the author to choose:

| Option | Sessions | Source N | Target N | Chance of Accept at true p = 0.85 | Inconclusive at p = 0.75 |
|---|---|---|---|---|---|
| Protocol 5: two agents, 20 and 20 tasks each | 2 + 80 (+8) | 20 (14 after removal) | 20 | 17.6% (10.3% at 14) | 97.2% |
| A: one agent, 44 source and 44 target tasks | 2 + 88 | 44 | 44 | about 64% (at 45) | about 90% |
| B: one agent, 30 source and 58 target tasks | 2 + 88 | 30 | 58 | 52.4% (source), about 80% (target, at 60) | 89.4% (source) |

The figures come from the exact binomial table in the paper (N = 30, 45, 60). Options A and B drop the second agent. Both need more tasks than protocol 5 selected: the source pool has 75 eligible tasks and the target pool has 108 candidate pull requests, of which the first 20 were checked. The B05 and B07 checks would have to run on the added source tasks, and the eligibility check on the added target tasks. No option gives a useful chance of a decision for an agent whose true rate is near the threshold; the paper should say so and state the rates at which the design can decide.

### P6-3. State what counts as an answer before the sessions

Add to the analysis plan, before the freeze:

- RQ1 is answered by the set of decisions and reasons per method and agent, and by how many of the defects that MESA lists the audits and ABC also list.
- RQ2 is answered per method by one of three outcomes: same decision as the direct test, different decision, or not comparable (one side is Inconclusive or No decision). The paper reports the count of each and makes no claim of agreement from pairs where both sides are Inconclusive.
- The difference in resolve rate between source and target, with its Newcombe interval, is reported as the measure of transfer, whatever the decisions are.

### P6-4. Apply the task checks to the target tasks

Run the B07 cheating attempts and the eligibility runs on the target tasks as well, and report how many target tasks have a located defect. Without this, the direct test is graded by tests of unknown quality while the source tasks are filtered.

### P6-5. Report the review records as they are

Keep the statement that one model family drafted the forms and one author signed them. Add the agreement between rating runs A and B per field, which the records already hold, so that a reader sees how stable the drafts were.

## What adopting this would need

- The author's decision on P6-1 to P6-5, each on its own.
- For P6-1: code and tests, a new pinned policy digest, and a new signature on the B28a form if it gains a control field.
- For P6-2: new task selections, new B05 and B07 forms for the added source tasks with the author's signature, a new requirement record (its task set and configurations are part of the signed record), and new figures in the paper.
- For P6-3 and P6-4: protocol text, and for P6-4 new check records.
- None of this can be done by 12 November together with the sessions. It is a plan for a later submission, or for a revision if the paper is submitted as a design paper now.

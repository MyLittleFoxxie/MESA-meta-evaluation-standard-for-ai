# Traceability for the design-study revision

The original 30-session results and selected quotations retain their original traceability in [the original study record](../../claude-sonnet-5-5/analysis/manuscript-traceability.md). They are not recomputed using the revised sessions.

| Manuscript statement | Record |
| --- | --- |
| Ten planned and completed follow-up conversations; all eligible; twelve physical attempts | [runs.csv](runs.csv), [attempts.csv](attempts.csv), [summary.json](summary.json) |
| Two failures before generation and two retained retries | [retry decision](../launches/authentication-retry-decision.json); original events, metadata and nested attempt-2 records under the two affected output directories |
| Two guidance edits, with questions and case expectations unchanged | [freeze manifest](../freeze-manifest.json), [protocol](../protocol.md), [revised materials](../materials/mesa.txt), [revision verification](revision-verification.json) |
| 242/245 original-key matches; 239/245 under the alternative P6B label | [claims.csv](claims.csv), [follow-up.json](follow-up.json); both totals independently reconstructed from raw responses by [verify_revision.py](../verify_revision.py) |
| One P6B and two C8 safety disagreements | [follow-up report](follow-up.md), [claims.csv](claims.csv) |
| 115/115 expected change/no-change contrasts; 114 with both original-key labels | [paired-cases.csv](paired-cases.csv), [summary.json](summary.json) |
| 0/30 unjustified negative claims supported; 245/245 quotes located | [claims.csv](claims.csv), [summary.json](summary.json) |
| 250 choices; 12 varying question–benchmark pairs; 435/500 matching repeated choices | [mesa-answers.csv](mesa-answers.csv), [mesa-distributions.csv](mesa-distributions.csv), [mesa-agreement.csv](mesa-agreement.csv) |
| DesignQA Q8 and Q12: all Partly; Q23: three No; Q24: two No | [mesa-answers.csv](mesa-answers.csv) |
| Author checked original six reviews and qualitative coding | Explicit user confirmation in the requesting chat on 17 October 2026. This is an author-reported check, not an independently archived coding exercise; it does not extend to this follow-up. |

The revised model-study materials are a separate version from the unchanged live participant survey. Interpretation of generated comments remains assistant analysis. Neither textual consistency nor the follow-up counts establish human accessibility or effects on team decisions.

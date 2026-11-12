# Paper 2: change log for rounds 3 and 4 (12 November 2026)

Scope: `paper2.tex`, `references.bib` (three entries), one figure, and the replication package. No session, check or rating was run. No frozen file, session record or analysis output was changed. Nothing was committed or pushed.

## What changed and why

| Change | Why |
|---|---|
| Full rewrite of the text with the same results; new title "Applying Benchmark Review Frameworks to Requirement Decisions: An Empirical Study on a Coding Agent" | Round 3 review: the old title asked a question the data cannot answer, and the text could not be followed without knowing the criterion codes |
| Criterion codes, method codes, task identifiers, slot numbers, file names and configuration names replaced by plain names | Author instruction, same as for the MESA paper |
| Study history removed: protocols, freeze, reserve sessions, standby agent, refusal of one model, retries, time of agent selection | Author instruction: the paper presents the finished experiment only |
| The first session, on a task outside the two task sets, is not reported; the paper has 88 sessions | Author decision of 12 November |
| Mentions of the author signing forms and of a human judgment that was not made removed; human evaluation named once as a next step | Author decision of 12 November |
| One section "Limitations" replaces "Threats to Validity and Limitations" | Author instruction |
| New section "The Decision Method" explains the requirement, the statistical rule, the rating terms and the three levels | Round 3 review: the paper was not self contained |
| Tables cut from six to four; no font below footnote size | Author rules for tables |
| Figure replaced by `figures/paper2_study_overview.pdf`, in the style of the MESA paper's figure | Author instruction |
| Data Availability Statement with contents, licenses and what is left out | REFSQ rule |
| Citations moved or dropped where the cited work did not support the sentence (see `paper2_references_check.md`) | References check |
| `references.bib`: DOI, volume and number of Hou et al. corrected; titles of the two anonymous companion entries set to the current titles of the two papers | References check; the two papers cite each other |

Later on 12 November the author chose the title "Applying Benchmark Review Frameworks to Requirement Decisions: An Empirical Study on a Coding Agent" (no acronym in the title). Acronyms were also removed from the section headings of both papers: "RQ1" became "Research Question 1", and the heading "MESA: Shared Concerns and a Rubric" in the MESA paper became "Shared Concerns and a Rubric".

## Errors found when the numbers were traced

All numbers were recomputed with `supporting/editorial/round3_checks/check_paper2_numbers.py` and `python3 -m paper2.preparation.cases --protocol 6`. The results match the records. These points in the earlier text did not:

1. The intervals were labelled "95% exact CI". They are pairs of one sided 95% bounds, which is a 90% two sided interval. The label is corrected.
2. Kappa 0.883 was printed next to "80 of 82". It belongs to the agreement on the deciding label (81 of 82). Both figures are now given, and the kappa values between model families (0.57 and 0.41) are added.
3. Median duration of source sessions is 48 seconds, not 49. Step counts are no longer reported (medians were 9.5 and 13.5, printed as 10 and 14).
4. 35 of 44 was printed as 79.6% in one table and 79.55% elsewhere. It is 79.5% throughout.
5. The citation for the defective source task and for "OpenAI's February 2026 audit" pointed to OpenAI's page on SWE-bench Pro. It now points to the February 2026 page on SWE-bench Verified.
6. The paper said the kept tasks were "clean". Half of the kept source tasks and 12 of the 20 kept target tasks had no valid check. The paper now gives these counts and says "kept tasks".
7. The paper cited itself under an earlier title (`anonymous_companion_method_2027`). The citation is removed.

Found outside the paper: `dist/paper2_replication_package.zip` was built on 11 November before the 88 sessions ran, so it held no session records, a README of five lines and no license file. It is rebuilt.

## Left for the author

- `month = jul` in the entry `openai_swebench_audit_2026` could not be confirmed. The paper no longer cites this entry.
- The raw event logs of the sessions are not on this PC (they are ignored by Git), so the package holds summaries and hashes only. If the logs should be in the package, build it on the machine that ran the sessions.
- The package includes the earlier protocols, because the code of the reported study reads files from them.

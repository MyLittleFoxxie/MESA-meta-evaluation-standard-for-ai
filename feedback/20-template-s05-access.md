# Feedback — `20-template-s05-access` (`MESA EFPA template official.md:923-1122`)

Unit reviewed: Section 5 preamble (:925-927), 5.1 (:929-945), 5.2 (:947-963), 5.3 Methods of
Publication (:965-982), 5.4 User Requirements (:984-1000), 5.5 Dataset and Item Access
(:1002-1022), 5.6 Provenance and Contamination (:1024-1050), 5.7 Reproducibility Materials
(:1052-1079), 5.8 Maintenance and Versioning (:1081-1111), Appendix A (:1115-1119). EFPA
counterpart: Section 5 "Supply arrangements and materials" + Appendix A
(`EFPA_Test_Review_Model_2025_Markdown.md:569-609`).

What holds up: this section is where MESA earns its keep beyond EFPA. 5.5's access-level
matrix, 5.6's provenance/contamination matrix, and 5.8's lifecycle table cover exactly the
territory (contamination controls, replication packages, maintenance) that BetterBench found
weakest across real benchmarks, and the preamble cites that grounding explicitly (:927) — the
visible-source practice the whole template should follow. The escape-hatch discipline is also
better here than anywhere else in Part A: 5.2 ends with "Access model not documented", 5.5 has
a "Not available" column, 5.6 a "Not documented" column. Machine-contract check: both `[ ]`
matrices, all checkbox lists, the fill-in tables, and Appendix A's "Free Text:" prompt
(:1119, explicitly recognized at `assets/mesa-form.js:203`) parse correctly; no violations —
but see F-1 for a heading-level content bug the parser faithfully preserves.

---

### F-20-template-s05-1 — [Major] 5.1 carries the wrong title — a duplicate of 5.2's — over documentation-list content
- **Axis:** vagueness (structural defect)
- **Where:** `MESA EFPA template official.md:929` vs `:947`
- **Quote:** > ### 5.1 Distribution and Access Model
> ...
> - [ ] Technical report
> - [ ] User guide
> - [ ] Repository README
- **Why it fails a user:** 5.1 and 5.2 have the identical heading "Distribution and Access Model", but 5.1's checkboxes are documentation types — the direct adaptation of EFPA 5.1 "Supporting information provided by the distributor to users" (`EFPA:571-579`) — while 5.2 holds the actual access-model options. This is a copy-paste error: a reviewer navigating by heading answers access questions in the documentation list (or assumes 5.1/5.2 are an accidental duplicate and skips one), a citation to "MESA 5.1" is ambiguous, and the live form's section list shows two identically named subsections back-to-back.
- **Fix:** Retitle 5.1 to "Supporting Documentation Provided to Users". Parser impact: heading text changes the derived section ID/label but drops nothing; answers keyed to the old ID would detach, so note it as a stored-answers migration when applied.
- **EFPA link:** EFPA 5.1 (`:571`) — retained in content, mislabeled in title.

### F-20-template-s05-2 — [Major] 5.6 and 5.8 re-ask each other's questions, and each duplicates itself
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:1024-1048` (5.6) and `:1081-1109` (5.8)
- **Quote:** > | Rules for updating, rotating, replacing, or adding benchmark items over time | *(5.6, :1047)* — vs — > | Rules for updating, rotating, replacing, or adding hidden evaluation items over time | *(5.8, :1101)*
- **Why it fails a user:** The contamination matrix and the maintenance table overlap row-for-row in at least five places: the item-rotation rule appears in both (:1047 / :1101); 5.6's "Rerun or replacement trigger" (:1044) against 5.8's "Rerun policy" (:1089); 5.6's "Leak response policy" (:1043) against 5.8's item-correction and deprecated-item rows (:1099-1100). Within 5.6, "Pre-exposure or source-material searchability checks" (:1038) and "Public-source searchability" (:1039) are the same check twice. Within 5.8, retirement appears four times ("Retirement and archival policy" :1095, "Score-ceiling threshold or criteria for deprecating..." :1104, "Policy for deprecating, archiving, or ending use..." :1105, "Retired-item publication or audit policy" :1106) and score comparability twice (:1107, :1108). A reviewer completes 46 rows across the two structures where ~32 would carry the same information, and duplicated rows invite contradictory entries.
- **Fix:** Adopt a boundary rule stated in both preambles — "5.6 records item *integrity* (origin, exposure, leaks); 5.8 records *operations* (who maintains what, versioning, comparability)" — then: in 5.6 delete :1039 (keep :1038) and :1047 (rotation is operations → 5.8); in 5.8 merge :1104-1106 into one row "Deprecation, archival, and retired-item policy (including score-ceiling triggers and retired-item release)", merge :1107-1108 into "Score comparability across versions, cohorts, and refreshes", and merge :1096-1097 into "Release tags, changelog, and comparability notes". Net: 46 rows → ~36. Parser impact: row deletions/merges remove fields by design.
- **EFPA link:** Both structures are MESA-original (EFPA Section 5 has no contamination or lifecycle machinery); the BetterBench-derived content is the template's strongest addition, which is why it should not be self-duplicating.

### F-20-template-s05-3 — [Major] Appendix A dropped EFPA's entire content and length specification
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:1115-1119`
- **Quote:** > Write a concise descriptive summary of the benchmark for readers who have not inspected the materials. Keep this descriptive and defer evaluation to Part B.
- **Why it fails a user:** EFPA's Appendix A instruction (`EFPA:607`) specifies what to cover (what the instrument is, scales, purpose, norm groups, unusual features, history, intended users and takers, all versions), a length band (200-300 words, up to 600 for complex instruments), the stand-alone purpose, and explicit permission to repeat Part A facts. MESA keeps two sentences. Without the spec, one reviewer writes 50 words, another 900; none reliably covers versions or intended users; and the appendix cannot serve as the "short stand-alone non-evaluative benchmark description" that Figure 1 advertises (see F-20-template-00-7 — this is the missing implementing text).
- **Fix:** Restore the spec, adapted: "Describe what the benchmark is, what it claims to measure, its task and score structure, documented baselines or reference points, intended users, available versions and forms, and any unusual features or relevant history. Aim for 200-400 words (longer for multi-component suites). Write it to stand alone outside this review — this appendix is the 'short stand-alone non-evaluative benchmark description' in Figure 1 — and expect to repeat facts recorded in Sections 1-5." Parser impact: none (paragraph text; the "Free Text:" prompt stays).
- **EFPA link:** EFPA Appendix A (`:605-609`) — dropped in all but name; restoring is pure retention.

### F-20-template-s05-4 — [Minor] 5.7's 22 reproducibility options contain four near-duplicate clusters
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:1056-1077`
- **Quote:** > - [ ] Container or reproducible environment
> - [ ] Container image
- **Why it fails a user:** Four clusters tick-split the same fact: container/container image (:1061-1062); reproduction script / push-button replication command (:1070-1071); expected-output fixtures / scorer fixtures / task-level expected outputs (:1072-1075); CI-test suite / public build status (:1076-1077). Reviewers tick inconsistently across the pairs, and 22 decisions do the work of ~15.
- **Fix:** Merge each cluster into one option ("Container or pinned reproducible environment", "Replication script for published results (ideally single-command)", "Expected-output or scorer fixtures", "CI or public passing-test signal"). 22 → 15, plus append "- [ ] Other (describe in Reviewer comments)" and "- [ ] None documented". Parser-safe.
- **EFPA link:** MESA-original (BetterBench-informed); dedup preserves all BetterBench coverage.

### F-20-template-s05-5 — [Minor] EFPA's "none vs. unclear" rule dropped from 5.4
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:984-999`
- **Quote:** > Describe any requirements specified for running, submitting to, interpreting, or maintaining the benchmark.
- **Why it fails a user:** EFPA 5.3 instructs: "Where qualification requirements are not clear this should be stated. When it is explicitly stated that there is no required qualification, write 'none'" (`EFPA:602`). That distinction — *documented absence* vs. *absent documentation* — is the exact discipline MESA's front matter preaches (:19), yet the one EFPA sentence enforcing it in Section 5 was dropped. Reviewers will leave cells blank, and blank is unreadable (none? unknown? skipped?).
- **Fix:** Add after the instruction: "Write 'none (stated)' where documentation explicitly says no requirement exists, and 'not documented' where it is silent. Do not leave cells blank." Parser impact: none.
- **EFPA link:** EFPA 5.3 (`:593-603`) — drifted: table translation good, completion rule lost.

### F-20-template-s05-6 — [Minor] "Other" escape options missing from 5.1, 5.3, 5.7 (extends F-20-template-s02a-2)
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:933-943` (5.1), `:969-980` (5.3), `:1056-1077` (5.7)
- **Quote:** > - [ ] Changelog or release notes
>
> Reviewer comments: *(end of 5.1 — no "Other"; EFPA 5.1 closes "Other (describe)", `EFPA:579`)*
- **Why it fails a user:** Same systemic pattern; note that Section 5 is otherwise the best-behaved section (5.2/5.5/5.6 all carry not-documented outs), which makes the three remaining gaps easy to close.
- **Fix:** Append `- [ ] Other (describe in Reviewer comments)` to 5.1, 5.3, 5.7. Parser-safe.
- **EFPA link:** EFPA 5.1 (`:579`), 5.2 (`:589`) — dropped.

---

## Verdict
- **Disposition:** Trim (retitle 5.1; dedupe the 5.6/5.8 complex; restore Appendix A's spec)
- **Items:** 8 subsections + appendix; ~45 checkboxes, 15×4 + 21×3 matrices, 9 + 25 fill-in rows → same section count; ~38 checkboxes, 20×3 matrix, ~20 lifecycle rows, Appendix A properly specified (net ≈ −20 reviewer decisions)
- **Rationale:** Substantively the strongest Part A section — BetterBench-grounded and genuinely AI-native — dragged by a copy-paste title bug, self-duplicating matrices, and an appendix instruction reduced past the point of usability.

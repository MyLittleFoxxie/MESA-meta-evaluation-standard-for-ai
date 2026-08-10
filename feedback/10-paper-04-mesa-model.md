# Feedback — `10-paper-04-mesa-model` (`paper.tex:140-189`)

Unit reviewed: The MESA Test Review Model — overview (:142), structure table (:144-169), and
five `\paragraph` blocks: Part A (:172), Part B (:174-177), Template coherence (:179-180),
MESA as its own measurement object (:182-183), Scope of MESA judgments (:185-188).

Structural fidelity check (axis 7): Table II's thirteen rows match the delivered template's
architecture — Sections 1-5, Appendix A in its actual position (end of Part A, template
`:1115`), Sections 6-12, Final Evaluation — and the section purposes are accurate one-line
compressions. The evidence-gap discipline described at :172 ("records unavailable descriptive
information as an explicit evidence gap") is genuinely implemented in the template's better
sections (5.2, 5.5, 5.6 escape hatches — Cross-cutting log). The two scope paragraphs
(:186-188) accurately deliver the critique-plan Task 4 content. This is the paper's most
accurate section; the findings are wording-level except F-1.

---

### F-10-paper-04-1 — [Major] The "not redundant as long as each section preserves its role" defense is contradicted by the delivered template
- **Axis:** claim support
- **Where:** `paper.tex:180`
- **Quote:** > The MESA template contains deliberate overlap because the same benchmark artifact can matter for different review functions. [...] This is not redundant as long as each section preserves its role: description, material usability, reliability, validity, fairness, or communication.
- **Why it fails a user:** The stated criterion is correct — and the prompt-template example given is a legitimate multi-role artifact. But the Part A review found overlap that fails this very criterion: 2.6 vs 2.9 near-duplicate response-type checklists (same role: description), 2.4 vs 4.10 audience lists with 8/8 identical options (same role), and the 2.5/3.2/3.7 score-inventory triple (F-20-template-s03-1). A reader who checks the template against this paragraph finds same-role duplication the paragraph implicitly denies. The paper is describing a property the artifact does not currently have.
- **Fix:** Preferred: fix the template per the Part A findings, making the paragraph true. If the paper ships first: soften to "...is not redundant where each section preserves its role... Residual same-role duplication identified during self-review is being consolidated." The paragraph's principle should also be quoted in `/mesa-core-plan` as the acceptance criterion for the dedup work.
- **EFPA link:** MESA-original defense; EFPA avoids the issue by defining each artifact question once per part.

### F-10-paper-04-2 — [Minor] The rating scale is explained only for n/a, 0, and 1 — the meanings of 2-4 never appear in the paper
- **Axis:** vagueness
- **Where:** `paper.tex:177`
- **Quote:** > MESA uses EFPA-style ratings of \texttt{n/a} and \texttt{0}--\texttt{4}. The rating \texttt{n/a} means that an attribute is not applicable... A \texttt{0} means that the attribute is applicable, but the available information is absent or insufficient for evaluation. A \texttt{1} means that evidence exists, but is inadequate for the benchmark's stated purpose.
- **Why it fails a user:** The n/a-vs-0-vs-1 distinction is well made (and matches EFPA's semantics), but a reader reaching the case-study ratings ("2", "3") has never been told what those values assert. The scale's top half is used throughout Section VI while defined nowhere in the paper.
- **Fix:** Add one sentence: "Ratings of \texttt{2}, \texttt{3}, and \texttt{4} mean the evidence is adequate, good, or excellent, respectively, for the stated purpose." (Matches the template's Explanation of Ratings and EFPA usage.)
- **EFPA link:** EFPA rating scale (`EFPA_Test_Review_Model_2025_Markdown.md`, Explanation of Ratings) — retained in the template; incompletely surfaced in the paper.

### F-10-paper-04-3 — [Minor] The gloss attached to "claim proportionality" actually defines gameability
- **Axis:** terminology
- **Where:** `paper.tex:175`
- **Quote:** > It also expands validity review to include contamination, gameability, and claim proportionality: whether a system can obtain a high score through shortcuts, exposure, formatting, tuning, or benchmark-specific scaffolding rather than the target capability itself (Section~10).
- **Why it fails a user:** The colon promises a definition of the term it follows; what comes is a definition of gameability. "Claim proportionality" — flagged undefined since the abstract (Cross-cutting log) — thus reaches the end of the paper's framework section with its only apparent definition describing a different concept. A reader will conclude claim proportionality *means* score-gaming.
- **Fix:** "...expands validity review to include contamination, gameability --- whether a system can obtain a high score through shortcuts, exposure, formatting, tuning, or benchmark-specific scaffolding rather than the target capability --- and claim proportionality: whether public claims stay within what the measured evidence supports (Section~10)." This also finally defines the term, resolving F-10-paper-00-5's deferral.
- **EFPA link:** MESA-original terms; the fix keeps both and defines both.

### F-10-paper-04-4 — [Minor] "Replaces mechanical averaging" misstates what EFPA does — and contradicts the paper's own Related Work
- **Axis:** claim support
- **Where:** `paper.tex:177`
- **Quote:** > MESA thus replaces mechanical averaging with a traceable account of appropriate score use.
- **Why it fails a user:** EFPA already prohibits mechanical averaging ("Do not simply average numbers to obtain an overall rating", `EFPA_Test_Review_Model_2025_Markdown.md:1838` and three further places), and the paper's own :86 correctly attributes that caution to EFPA. Here the same practice is presented as MESA's replacement of a default that never existed — a fidelity slip in the section whose job is to describe the adaptation honestly.
- **Fix:** "Like EFPA, MESA avoids mechanical averaging; it adds a traceable account of appropriate score use." (One word of credit; the added value — the supported/non-use account — remains MESA's.)
- **EFPA link:** EFPA overall-rating instructions (`:1838, 2296, 2469, 2570`) — retained practice, misdescribed as original.

### F-10-paper-04-5 — [Nit] "Requirements object" is a one-off coinage
- **Axis:** terminology (polish)
- **Where:** `paper.tex:142`
- **Quote:** > ...treats an AI benchmark as both a requirements object and a source of score-based claims.
- **Why it fails a user:** "Requirements object" appears once, unexplained — :84 says "requirements-relevant review objects", which is clearer.
- **Fix:** At :142 write "...as both a requirements-relevant review object and a source of score-based claims."
- **EFPA link:** n/a — labeling consistency.
- **Correction note (added during the s12 pass):** this finding originally also flagged Table II's Section 12 row for adding "Dashboards" — that was wrong. The template's actual heading (`MESA EFPA template official.md:2314`) is "Quality of Reports, Leaderboards, Dashboards, and Public Claims"; the paper's Table II row matches the template exactly. The stale title was in this review's own ledger, not in the paper. Withdrawn.

---

## Verdict
- **Disposition:** Trim (four wording fixes; no structural change)
- **Items:** 1 table + 6 paragraphs → unchanged (net ±0 words)
- **Rationale:** The paper's most accurate section — Table II mirrors the real template and the scope paragraphs are well calibrated — but its coherence defense asserts a property the template currently lacks, and the rating scale it introduces is only half-defined.

# Feedback — `20-template-s10-validity-a` (`MESA EFPA template official.md:1816-1943`)

Unit reviewed: Section 10 front matter — preamble (:1818-1826), Figure 4 (:1830-1930),
anti-difficulty rule (:1932), section guidance table (:1934-1942). (Items 10.1-10.7 are
reviewed as `20-template-s10-validity-b`.)

This is the template's intellectual center and the front matter is mostly earning its length:
the EFPA-mapping sentence is present (:1818) with the CHC breadth requirement wired to 2.1/2.5;
Bean et al. is named in-line as the primary construct-validity source (:1820) and BetterBench
for contamination (:1822) — the visible-grounding pattern at its best; the validity definition
(:1824) is AERA-faithful; and the anti-difficulty rule (:1932 — ratings "should not be inferred
from benchmark popularity, leaderboard difficulty, or whether current models perform poorly")
operationalizes the paper's "unsupported endorsement" error (`paper.tex:276`) as a concrete
rating prohibition. Figure 4 is accurate — every node maps to a real sub-section and item.
Parser check: clean.

---

### F-20-template-s10a-1 — [Minor] "The specific meaning users are supposed to draw from a score" — third verbatim occurrence of a phrase the template elsewhere says in three words
- **Axis:** terminology (repetition)
- **Where:** `MESA EFPA template official.md:1824` (previously `:11`, `:19` — Cross-cutting log)
- **Quote:** > Reviewers should therefore identify the specific meaning users are supposed to draw from a score before rating each source of validity evidence.
- **Why it fails a user:** The ten-word formula recurs while the same document already uses the crisp synonym — "the intended score meaning" (`:1158`, `:1545`) — creating the impression the two phrasings might be different concepts.
- **Fix:** **Substitute** here and at :11/:19: "Reviewers should therefore identify the intended score meaning before rating each source of validity evidence." Adopt "intended score meaning" as the canonical term corpus-wide (input to `80-xcut-terminology`).
- **EFPA link:** n/a — MESA phrasing consistency.

### F-20-template-s10a-2 — [Minor] The preamble previews the sub-section taxonomy twice before the items state it
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:1826` and Figure 4 (:1830-1930)
- **Quote:** > ...benchmark review must also examine whether scoring rewards the target capability, score effects caused by scorers or parsers, prior exposure to benchmark items or answers, unintended disclosure of hidden materials, benchmark-specific tuning, public/hidden split design, and whether public interpretations are proportional to the evidence.
- **Why it fails a user:** This sentence is a prose enumeration of sub-sections 10.3, 10.5, and 10.6; Figure 4 then diagrams the same taxonomy; the sub-section preambles state it a third time. The reviewer reads ~110 lines of front matter before the first rating — the S09 triple-preview pattern in lighter form.
- **Fix:** Cut :1826's second sentence to its point: "Content coverage, internal structure, relations with other evidence, and response-process logic remain central; AI-specific threats — scoring effects, prior exposure, tuning, disclosure — are itemized in 10.3 and 10.5-10.6." (−30 words; the figure and items carry the detail.)
- **EFPA link:** EFPA §10's evidence-source taxonomy — retained; the duplication is presentational.

---

## Verdict
- **Disposition:** Keep as-is (two small substitutions)
- **Items:** 6 prose paragraphs + figure + table → unchanged (≈ −35 words)
- **Rationale:** The best-grounded front matter in Part B — visible sources, accurate figure, and a rating prohibition that does real work; only phrasing economy is left to fix.

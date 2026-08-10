# Feedback — `10-paper-02-related-work` (`paper.tex:72-91`)

Unit reviewed: Related Work — II-A "AI Benchmarking Practices and Challenges" (:74-78) and
II-B "Benchmarking standards across the fields" (:80-90, four bold-paragraph threads).

Attribution verification (axis 7), performed against the literature corpus:

- **EFPA averaging caution (:86) — accurate.** "Cautions against mechanically averaging
  ratings" is EFPA's own repeated instruction ("Do not simply average numbers to obtain an
  overall rating", `EFPA_Test_Review_Model_2025_Markdown.md:1838, 2296, 2469, 2570`). ✓
- **Leaderboard Illusion summary (:76) — grounded.** "Selective comparison, unreported
  evaluation conditions, and ranking instability" fairly compresses the source's private
  testing, selective disclosure, and selective retraction findings
  (`The_Leaderboard_Illusion.md:190, 255`). ✓
- **Saturation and shortcut exploitation (:76) — grounded.** Both are explicit Line Goes Up
  themes (`lineUP.md:21-22`: statistical-regularity learning; "rapid pace with which new
  benchmarks become saturated"). ✓
- **Hendrycks CHC thread (:90) — grounded.** "Jagged" profile and the breadth-weighted domain
  framing match `A_Definition_of_AGI.md:7, 17`, and the CHC-debate caveat cite mirrors the
  source's own pointer to Canivez. ✓
- **Penn Treebank drift (:76) — attribution gap.** See F-1.

The reviewer-facing vs. developer-facing framing (:78) is the section's best move and is
accurately supported by what the template does (separation of description from judgment;
supported-use/non-use boundaries in 2.18 and Section 11).

---

### F-10-paper-02-1 — [Major] The Penn Treebank drift example is Alonso & Church's signature example, presented without credit
- **Axis:** claim support (attribution)
- **Where:** `paper.tex:76`
- **Quote:** > A related failure is benchmark drift, where an instrument is repurposed beyond its original design --- as when the Penn Treebank \cite{marcus_etal_1993_building}, built for syntactic parsing, was later reused as a perplexity benchmark in ways that detached the metric from its intended meaning.
- **Why it fails a user:** The observation — PTB designed for parsing, repurposed for perplexity, meaning detached — is the centerpiece example of Evaluating the Evaluations ("originally designed the PTB for one purpose (parsing), but it has been recently repurposed by the community for a very different use (perplexity) in a way that is not as meaningful as it might appear", `Evaluating_the_Evaluations.md:57`, with a full section at `:226`). The paper cites only the 1993 PTB paper, so the drift insight reads as the authors' own. This is precisely the paper Reviewer 1 said the manuscript under-engaged; borrowing its signature example uncredited converts an engagement fix into an attribution liability a camera-ready reviewer may flag as more than cosmetic.
- **Fix:** Add the citation to the observation itself: "...as when the Penn Treebank \cite{marcus_etal_1993_building}, built for syntactic parsing, was later reused as a perplexity benchmark in ways that detached the metric from its intended meaning \cite{alonso_church_sigir}." One cite key; no other change.
- **EFPA link:** n/a — paper prose.

### F-10-paper-02-2 — [Minor] The phenomenon→task→metric→claim chain is spelled out three times in three pages
- **Axis:** repetition
- **Where:** `paper.tex:78` and `:88` (third statement; first at `:61`, logged in the Cross-cutting log)
- **Quote:** > ...disciplines the inferential chain from phenomenon to task to metric to claim. *(:78)* — vs — > ...framing benchmark validity as a chain from the real-world phenomenon, through the chosen task and scoring metric, to the claim made about the score. *(:88)* — vs — > ...to discipline the inferential chain from phenomenon to task, metric, score, and claim *(:61)*
- **Why it fails a user:** The same four-link chain is enumerated at :61 (Introduction), :78 (II-A close), and :88 (II-B, with its source citation). Each restatement costs ~15 words and dulls the one place it belongs — :88, where Bean et al. are credited for it.
- **Fix:** Keep :61 (first use, self-glossing) and :88 (the attributed definition). At :78 compress to "...and disciplines the phenomenon-to-claim inferential chain (Section II-B)." (−11 words, and II-A now points forward instead of pre-empting II-B's contribution.)
- **EFPA link:** n/a — the chain is Bean et al.'s framing (Measuring what Matters), correctly cited at :88.

### F-10-paper-02-3 — [Minor] The EFPA Part B summary matches neither EFPA's section names nor its section count
- **Axis:** EFPA traceability
- **Where:** `paper.tex:86`
- **Quote:** > ...an evaluative part (rationale, materials, norms, reliability, validity, fair use, and final interpretation)...
- **Why it fails a user:** EFPA's Part B is: explanation & documentation (§6), test materials (§7), norms (§8), reliability (§9), validity (§10), fair use (§11), digitally generated reports (§12), and a final evaluation (`EFPA_Test_Review_Model_2025_Markdown.md:57-75`). The paper's list renames §6 with MESA's own section title ("rationale"), omits §12 entirely — ironic, since reports/leaderboards are where MESA adds most — and says "final interpretation" for "final evaluation". A reader auditing MESA's fidelity against the EFPA source finds a list that matches neither document.
- **Fix:** "...an evaluative part (documentation and rationale, materials, norms, reliability, validity, fair use, computer-generated reports, and a final evaluation)..." — seven sections plus the closing judgment, matching EFPA.
- **EFPA link:** EFPA Figure 1 / Part B structure (`:54-75`) — drifted in description only; the template itself preserves all eight elements.

### F-10-paper-02-4 — [Minor] Garbled connective in the section's opening sentence
- **Axis:** verbosity (grammar)
- **Where:** `paper.tex:76`
- **Quote:** > Concerns across the AI benchmarking literature cluster around two questions: what a benchmark actually measures and how its scores are used, such that a recurring concern is the validity and scope of evaluations \cite{alonso_church_sigir}.
- **Why it fails a user:** "Such that a recurring concern is..." connects nothing — the trailing clause restates the two questions it follows ("validity and scope" ≈ "what it measures and how scores are used"), so the sentence ends by repeating itself with a dangling connective.
- **Fix:** "Concerns across the AI benchmarking literature cluster around two questions: what a benchmark actually measures, and how its scores are used \cite{alonso_church_sigir}." (−12 words.)
- **EFPA link:** n/a — paper prose.

---

## Verdict
- **Disposition:** Trim (one added citation, two compressions, one corrected list)
- **Items:** 7 paragraphs (2 subsections, 4 bold threads) → unchanged (≈ −25 words, +1 cite key)
- **Rationale:** The section's structure and nearly all attributions verify cleanly against the corpus — including the EFPA averaging caution — but the uncredited Alonso & Church example must be fixed before camera-ready, and the validity chain needs one home instead of three.

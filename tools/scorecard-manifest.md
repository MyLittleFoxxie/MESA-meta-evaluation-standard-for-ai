# MESA Scorecard Manifest

This file is the authoritative list of what `MESA scorecard.md` contains. It is read by
`tools/build-scorecard.py`, which generates the scorecard from
`MESA EFPA template official.md`. Editing this list and re-running the generator is the only
supported way to change the scorecard's contents — never hand-edit the generated file.

## Why these items

The 40 rated items below were selected by a case-study coverage check against the three pilot
reviews in `reviews/gemini_supervising_editor/`: every item that produced a deficiency rating
(`0` or `1`) in a reconciled review had to be either in this set or covered by a condition that
held for that benchmark, and the nine items that escaped both were added. The derivation is
recorded in `feedback/95-mesa-core-plan.md` Part 1. The Part A units below are exactly the
descriptive fields those 40 items depend on.

Item numbers are the full template's own numbers, deliberately: a scorecard review can be
extended into a full review without renumbering anything, and the interactive form stores an
answer under the same key in both views.

## Part A — descriptive units to keep

Unnumbered blocks:

- General Description of the Benchmark
- Source Inventory

Numbered units (26):

    1.1  1.2  1.3
    2.1  2.2  2.3  2.5  2.8  2.9  2.11  2.12  2.15  2.16  2.17  2.18
    3.1  3.2  3.5  3.6
    4.1  4.2
    5.2  5.5  5.6  5.7  5.8

`2.11` keeps only its first table (the five core count rows); the conditional breakdown table is
dropped by the generator.

## Part B — rated items to keep (40)

    Section 6   6.1.1  6.1.3  6.2.3  6.2.4  6.2.7  6.3.1  6.4
    Section 7   7.1.1  7.1.4  7.1.7  7.1.8
    Section 8   8.1.1  8.1.2  8.1.3  8.2
    Section 9   9.1.1  9.2.1  9.2.2  9.4.1  9.5.1  9.6
    Section 10  10.1.1  10.3.1  10.3.2  10.4.1  10.4.2  10.4.3  10.5.1  10.5.2  10.6.1  10.7
    Section 11  11.1.2  11.2.2  11.3.1  11.4.2  11.5.1  11.6
    Section 12  12.2.1  12.3.1  12.5

Sub-sections left with no retained item — **9.3, 10.2, 12.1, 12.4** — are dropped whole. The
section overall items (6.4, 7.1.8, 8.2, 9.6, 10.7, 11.6, 12.5) therefore have their roll-up
sentence rewritten, because the ranges they cite in the full template no longer all exist here.

## Front matter and closing blocks to keep

- Glossary
- Explanation of Ratings (including the `n/a` vs `0` rule) and the Rating Scale table
- General Guidance on Assigning Ratings
- Final Evaluation: Evaluative Report, Conclusions, Recommendations, MESA Benchmark Artifact Profile, Gap Register
- Bibliography

The Introduction, "How the MESA Model Should Be Used", and Figures 1-5 are replaced by a short
scorecard-specific introduction written by the generator. Retired tombstone headings
(2.6, 4.10, 10.6.2, 11.3.2) are dropped — they exist to resolve stale citations in the full
template and have no purpose here.

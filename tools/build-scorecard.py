#!/usr/bin/env python3
"""Generate `MESA scorecard.md` from `MESA EFPA template official.md`.

The scorecard is the short form of the MESA review template: the 40 rated items listed in
`tools/scorecard-manifest.md`, the Part A descriptive fields those items depend on, and the
Final Evaluation. Item text is copied verbatim so the two documents cannot drift and so the
interactive form stores an answer under the same key in both views.

Run from the repository root:

    python tools/build-scorecard.py

The script only reads the main template; it never modifies it. Re-run it after any edit to the
template or to the manifest. Output is deterministic: running it twice produces an identical file.
"""

import io
import os
import re
import sys

TEMPLATE = "MESA EFPA template official.md"
OUTPUT = "MESA scorecard.md"

# --- what to keep (mirrors tools/scorecard-manifest.md) ------------------------------------

PART_A_UNNUMBERED = ["General Description of the Benchmark", "Source Inventory"]

PART_A_UNITS = [
    "1.1", "1.2", "1.3",
    "2.1", "2.2", "2.3", "2.5", "2.8", "2.9", "2.11", "2.12", "2.15", "2.16", "2.17", "2.18",
    "3.1", "3.2", "3.5", "3.6",
    "4.1", "4.2",
    "5.2", "5.5", "5.6", "5.7", "5.8",
]

RATED_ITEMS = [
    "6.1.1", "6.1.3", "6.2.3", "6.2.4", "6.2.7", "6.3.1", "6.4",
    "7.1.1", "7.1.4", "7.1.7", "7.1.8",
    "8.1.1", "8.1.2", "8.1.3", "8.2",
    "9.1.1", "9.2.1", "9.2.2", "9.4.1", "9.5.1", "9.6",
    "10.1.1", "10.3.1", "10.3.2", "10.4.1", "10.4.2", "10.4.3", "10.5.1", "10.5.2", "10.6.1", "10.7",
    "11.1.2", "11.2.2", "11.3.1", "11.4.2", "11.5.1", "11.6",
    "12.2.1", "12.3.1", "12.5",
]

# Part B front matter and closing blocks carried over verbatim, by heading text.
KEEP_BLOCKS = [
    "Glossary",
    "Information Sources",
    "Explanation of Ratings",
    "Rating Scale",
    "General Guidance on Assigning Ratings",
    "Final Evaluation",
    "Evaluative Report of the Benchmark",
    "Conclusions",
    "Recommendations",
    "MESA Benchmark Artifact Profile",
    "Gap Register",
    "Bibliography",
]

PART_HEADINGS = ["Part A. Description of the Benchmark", "Part B. Evaluation of the Benchmark"]

# Section overalls whose roll-up sentence cites sub-sections or item ranges that the scorecard
# does not fully contain. Each is rewritten to refer to the items actually present.
ROLLUP_REWRITES = {
    "6.4": ("- This overall rating is based on reviewer judgment across sub-sections 6.1, 6.2, and 6.3. Do not mechanically average ratings.",
            "- This overall rating is based on reviewer judgment across the Section 6 items in this scorecard. Do not mechanically average ratings."),
    "7.1.8": ("- Excellent: Reviewer judgment, based on items 7.1.1-7.1.7, supports",
              "- Excellent: Reviewer judgment, based on the Section 7 items in this scorecard, supports"),
    "8.2": ("- This overall rating is based on reviewer judgment across sub-section 8.1. Do not mechanically average ratings.",
            "- This overall rating is based on reviewer judgment across the Section 8 items in this scorecard. Do not mechanically average ratings."),
    "9.6": ("- This overall rating is based on reviewer judgment across sub-sections 9.1-9.5. Do not mechanically average ratings.",
            "- This overall rating is based on reviewer judgment across the Section 9 items in this scorecard. Do not mechanically average ratings."),
    "10.7": ("- This overall rating is based on reviewer judgment across sub-sections 10.1-10.6. Do not mechanically average ratings.",
             "- This overall rating is based on reviewer judgment across the Section 10 items in this scorecard. Do not mechanically average ratings."),
    "11.6": ("- This overall rating is based on reviewer judgment across sub-sections 11.1-11.5. Do not mechanically average ratings.",
             "- This overall rating is based on reviewer judgment across the Section 11 items in this scorecard. Do not mechanically average ratings."),
    "12.5": ("- This overall rating is based on reviewer judgment across sub-sections 12.1-12.4. Do not mechanically average ratings.",
             "- This overall rating is based on reviewer judgment across the Section 12 items in this scorecard. Do not mechanically average ratings."),
}

# Cross-references in retained text that point at items the scorecard does not carry. Each is
# rewritten to the nearest true statement. Applied to the whole document after assembly.
REFERENCE_FIXES = [
    # 4.2's per-output iteration rule: 4.3-4.9 are not in the scorecard
    ("If more than one output exists, complete 4.2-4.9 for each output, or state in this table which single output the following answers describe.",
     "If more than one output exists, complete this table for each output, or state which single output the following answers describe."),
    # 11.1.2's boundary bullet cites 6.2.6, which the scorecard does not carry
    ("- Boundary: 6.2.6 rates whether fair-use documentation *exists and is usable*; this item rates whether the fairness consideration it documents was *substantively adequate* for the intended contexts. Divergent ratings should be explained in comments.",
     "- Rate whether the fairness consideration the documentation records was *substantively adequate* for the intended contexts, not merely whether such documentation exists."),
    # the Final Evaluation revisit checkpoint cites 6.2.5, which the scorecard does not carry
    ("re-check ratings 6.1.1, 6.1.3, and 6.2.5 against your Section 8-10 findings and note any rating changed.",
     "re-check ratings 6.1.1, 6.1.3, and 6.2.4 against your Section 8-10 findings and note any rating changed."),
    # the claims pipeline cites 12.4, which the scorecard does not carry
    ("and 12.3-12.4 rate *how claims are communicated*.",
     "and 12.3 rates *how claims are communicated*."),
]

# Paragraph + table in the Section 11 preamble mapping its sub-sections to ratings elsewhere.
# Most of those ratings are absent from the scorecard, so the whole block is dropped.
S11_XREF_LEAD = "Relevant information for this section may also have been rated in other sections."


def drop_s11_xref(body):
    """Remove the Section 11 cross-reference lead-in paragraph and the table that follows it."""
    out, i = [], 0
    while i < len(body):
        if body[i].startswith(S11_XREF_LEAD):
            i += 1
            while i < len(body) and body[i].strip() == "":
                i += 1
            while i < len(body) and body[i].lstrip().startswith("|"):
                i += 1
            while out and out[-1].strip() == "":
                out.pop()
            out.append("")
            continue
        out.append(body[i])
        i += 1
    return out


INTRO = """# MESA Scorecard — Short Form of the Review Template

This scorecard is the short form of the MESA Test Review Model. It carries 40 rated questions —
the ones whose ratings decided the outcome in MESA's pilot case studies — together with the
descriptive fields those questions depend on and the full closing evaluation. It is intended for
routine work: comparing candidate benchmarks, deciding whether a published score can support a
claim, or recording a benchmark's known limits before its scores are reused.

As in the full template, the seven section-overall ratings form the non-composite MESA Benchmark
Artifact Profile: Documentation, Usability, Interpretation, Reliability, Validity, Fairness, and
Reporting. Each metric value is a judgment based on the retained evidence in its section; never
average, weight, rank, or collapse the profile into a single score.

**Use the full template instead when the review supports a procurement decision, a policy
position, or a safety case.** The full template (`MESA EFPA template official.md`) carries 87
rated items and is the certification-grade instrument; this scorecard is deliberately narrower and
does not examine development process, materials usability, internal structure, scorer and judge
reliability, or leaderboard governance in their own right.

Item numbers here are the full template's own numbers. Nothing is renumbered, so a scorecard
review can be extended into a full review at any time simply by answering the items it omits, and
the interactive form on the MESA site stores an answer under the same key in either view.

As in the full template, a question that does not apply to the benchmark is marked `n/a`. The rule
that separates `n/a` from `0` is stated in Explanation of Ratings below and matters just as much
here: `n/a` records that the question does not arise, `0` records that it arises and is unanswered.

*This file is generated by `tools/build-scorecard.py` from the full template. Do not edit it by
hand — edit the template or `tools/scorecard-manifest.md` and re-run the generator.*
"""


def heading_number(title):
    m = re.match(r"^(?:Section\s+)?(\d+(?:\.\d+)*)\b", title.strip())
    return m.group(1) if m else None


def split_blocks(lines):
    """Split the template into (level, title, number, body_lines) blocks at every heading."""
    blocks = []
    cur = {"level": 0, "title": "(preamble)", "number": None, "body": []}
    for ln in lines:
        h = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if h:
            blocks.append(cur)
            title = h.group(2).strip()
            cur = {"level": len(h.group(1)), "title": title,
                   "number": heading_number(title), "body": []}
        else:
            cur["body"].append(ln)
    blocks.append(cur)
    return blocks


def trim_2_11(body):
    """2.11 keeps only its first (core count rows) table."""
    out = []
    for ln in body:
        if ln.startswith("Complete only the breakdowns"):
            break
        out.append(ln)
    while out and out[-1].strip() == "":
        out.pop()
    out.append("")
    out.append("Reviewer comments:")
    out.append("")
    return out


def drop_figures(body):
    """Remove ```mermaid fenced blocks and the 'The figure below…' lead-ins."""
    out, i = [], 0
    while i < len(body):
        ln = body[i]
        if ln.strip().startswith("```mermaid"):
            i += 1
            while i < len(body) and not body[i].strip().startswith("```"):
                i += 1
            i += 1
            while out and out[-1].strip() == "":
                out.pop()
            continue
        if ln.startswith("The figure below visualizes") or ln.startswith("The table below lists"):
            i += 1
            continue
        out.append(ln)
        i += 1
    return out


def main():
    if not os.path.exists(TEMPLATE):
        sys.exit("error: run from the repository root (cannot find %r)" % TEMPLATE)

    src = io.open(TEMPLATE, encoding="utf-8").read().replace("\r\n", "\n")
    blocks = split_blocks(src.split("\n"))

    keep_units = set(PART_A_UNITS)
    keep_items = set(RATED_ITEMS)
    # a sub-section survives only if it holds at least one retained rated item
    keep_subs = set(".".join(n.split(".")[:2]) for n in RATED_ITEMS if n.count(".") == 2)
    # Section-level headings survive when any of their units survive. Part A sections matter as
    # much as Part B ones: Section 2's preamble carries the ten CHC capability domains that 2.1
    # refers to as "the domains above".
    keep_sections = (set(n.split(".")[0] for n in RATED_ITEMS)
                     | set(n.split(".")[0] for n in PART_A_UNITS))

    out = [INTRO.rstrip(), ""]
    emitted_items = []

    for b in blocks:
        title, num, lvl, body = b["title"], b["number"], b["level"], b["body"]

        if title.endswith("(retired)"):
            continue

        keep = False
        if lvl == 1 and title in PART_HEADINGS:
            keep = True
        elif title in KEEP_BLOCKS or title in PART_A_UNNUMBERED:
            keep = True
        elif num:
            if num in keep_units:                      # Part A unit
                keep = True
            elif num in keep_items:                    # rated item or section overall
                keep = True
            elif lvl == 2 and num in keep_sections:    # Part B section preamble
                keep = True
            elif lvl == 3 and num in keep_subs:        # sub-section holding a kept item
                keep = True

        if not keep:
            continue

        if num == "2.11":
            body = trim_2_11(body)
        if num == "11":
            body = drop_s11_xref(body)
        body = drop_figures(body)

        if num in ROLLUP_REWRITES:
            old, new = ROLLUP_REWRITES[num]
            joined = "\n".join(body)
            if old not in joined:
                sys.exit("error: roll-up rewrite for %s did not match; template wording changed" % num)
            body = joined.replace(old, new).split("\n")

        if num and num in keep_items:
            emitted_items.append(num)

        out.append("#" * lvl + " " + title)
        out.extend(body)

    text = "\n".join(out)
    for old, new in REFERENCE_FIXES:
        if old not in text:
            sys.exit("error: reference fix did not match; template wording changed:\n  %s" % old[:90])
        text = text.replace(old, new)
    text = re.sub(r"\n{4,}", "\n\n\n", text).rstrip() + "\n"
    io.open(OUTPUT, "w", encoding="utf-8", newline="\n").write(text)

    missing = [n for n in RATED_ITEMS if n not in emitted_items]
    ratings = text.count("- Rating: [n/a")
    print("wrote %s" % OUTPUT)
    print("  rated items emitted : %d (expected %d)" % (len(emitted_items), len(RATED_ITEMS)))
    print("  Rating: lines       : %d" % ratings)
    if missing:
        sys.exit("error: manifest items not found in template: %s" % ", ".join(missing))
    if ratings != len(RATED_ITEMS):
        sys.exit("error: expected %d rating lines, found %d" % (len(RATED_ITEMS), ratings))


if __name__ == "__main__":
    main()

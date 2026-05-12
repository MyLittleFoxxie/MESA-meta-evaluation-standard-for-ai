from __future__ import annotations

import argparse
import dataclasses
import difflib
import re
import shutil
import sys
from pathlib import Path

from pypdf import PdfReader


RATING_LABELS = {
    "n/a": "Not applicable",
    "0": "No information given",
    "1": "Inadequate",
    "2": "Adequate",
    "3": "Good",
    "4": "Excellent",
}


KNOWN_OPTION_REPLACEMENTS = {
    "6.1.6": {
        "n/a": "Not applicable",
        "0": "No item analysis described whether conducted or not.",
        "1": "Inadequate",
        "2": "Adequate",
        "3": "Good",
        "4": (
            "Excellent: analysis includes discriminative power, location or difficulty indicators, "
            "construct breadth, and aligns with test type (e.g., polytomous, adaptive). In maximum "
            "performance multiple choice items, distractor analysis is carried out."
        ),
    },
    "6.1.7": {
        "n/a": "Not applicable",
        "0": "No or insufficient presentation of item analysis results, whether conducted or not",
        "1": "Inadequate: items with negative or very low discrimination (below .20); extreme ceiling or floor effects.",
        "2": "Adequate",
        "3": "Good",
        "4": (
            "Excellent: items show a good spread of difficulty/locations for the intended sample, "
            "enough variability and high discrimination (e.g., > .30 based on CTT) and satisfactory "
            "construct breadth. Note that very high correlations may mean that items are more or less "
            "synonymous and that the concept measured may be very narrow. In maximum performance, "
            "multiple choice items, distractors work as intended. For multi-scale instruments absence "
            "of unexpected cross-loadings."
        ),
    },
}


TEXT_REPLACEMENTS = [
    (
        """| **[n/a]** | Not applicable                         |
| **[0]**   | Cannot rate (insufficient information) |
| **[1]**   | Inadequate                             |
| **[2]**   | Adequate                               |
| **[3]**   | Good                                   |
| **[4]**   | Excellent                              |""",
        """| **[n/a]** | This attribute is not applicable to this instrument |
| **[ 0 ]** | Not possible to rate as no, or insufficient information is provided |
| **[ 1 ]** | Inadequate |
| **[ 2 ]** | Adequate |
| **[ 3 ]** | Good |
| **[ 4 ]** | Excellent |""",
    ),
    (
        """- [ ] **Not applicable to this instrument [n/a]**
- [ ] **No information is provided [0]**
- [ ] **Not locally relevant [1]:** (e.g., inappropriate foreign or international samples)
- [ ] **Usable with caution [2]:** Sample(s) that do(es) not fit completely with the relevant application domain but could be used with caution.
- [ ] **Good relevance [3]:** Local country samples (or relevant international samples where international comparison is required) with good relevance.
- [ ] **Excellent: well-defined populations [4]:** Local country samples drawn from well-defined populations from the relevant application domain.""",
        """- [ ] Not applicable to this instrument [n/a]
- [ ] No information is provided [0]
- [ ] Not locally relevant (e.g., inappropriate foreign or international samples) [1]
- [ ] Sample(s) that do(es) not fit completely with the relevant application domain but could be used with caution (may include international samples where it is reasonable to assume only minor impact of language or culture) [2]
- [ ] Local country samples (or relevant international samples where international comparison is required) with good relevance for intended application [3]
- [ ] Local country samples (or relevant international samples where international comparison is required) drawn from well-defined populations from the relevant application domain [4]""",
    ),
    (
        """- [ ] **Not applicable [n/a]**
- [ ] **No information given [0]**
- [ ] **Inadequate representativeness [1]:** Representativeness cannot be adequately established.
- [ ] **Adequate [2]**
- [ ] **Good [3]**
- [ ] **Excellent: random sampling, strong representativeness [4]:** Data gathered via random sampling; thorough description of composition of sample and population provided.""",
        """- [ ] Not applicable [n/a]
- [ ] No information given [0]
- [ ] Inadequate representativeness for the intended application domain or the representativeness cannot be adequately established with the information provided [1]
- [ ] Adequate [2]
- [ ] Good [3]
- [ ] Excellent: data are gathered by means of a random sampling model; a thorough description of the composition of the sample(s) and the population(s) with respect to relevant background variables (such as gender, age, education, cultural background, occupation) is provided; good representativeness with regard to these variables is established [4]""",
    ),
    (
        """| Level             | Low-stakes | High-stakes |
| :---------------- | :--------- | :---------- |
| **0. No info**    | No info    | No info     |
| **1. Inadequate** | < 200      | 200-299     |
| **2. Adequate**   | 200-299    | 300-399     |
| **3. Good**       | 300-999    | 400-999     |
| **4. Excellent**  | >= 1000    | >= 1000     |""",
        """| Level | Low-stakes use | High-stakes decisions | Rating |
| :--- | :--- | :--- | :--- |
| Not applicable |  |  | n/a |
| No information given |  |  | 0 |
| Inadequate sample size | e.g., < 200 | e.g., 200-299 | 1 |
| Adequate sample size | e.g., 200-299 | e.g., 300-399 | 2 |
| Good sample size | e.g., 300-999 | e.g., 400-999 | 3 |
| Excellent sample size | e.g., ≥ 1000 | e.g., ≥ 1000 | 4 |""",
    ),
    (
        """| Level             | Low-stakes             | High-stakes            |
| :---------------- | :--------------------- | :--------------------- |
| **0. No info**    | No info                | No info                |
| **1. Inadequate** | < 8 subgroups of 70    | 8 subgroups of 70-99   |
| **2. Adequate**   | 8 subgroups of 70–99   | 8 subgroups of 100–149 |
| **3. Good**       | 8 subgroups of 100-149 | 8 subgroups of >= 150  |
| **4. Excellent**  | 8 subgroups of >= 150  | 8 subgroups of >= 200  |""",
        """| Level | Low-stakes use | High-stakes decisions | Rating |
| :--- | :--- | :--- | :--- |
| Not applicable |  |  | n/a |
| No information given |  |  | 0 |
| Inadequate sample size | e.g., fewer than 8 subgroups with a maximum of 69 respondents each | e.g., 8 subgroups with 70 - 99 respondents each | 1 |
| Adequate sample size | e.g., 8 subgroups with 70 - 99 respondents each | e.g., 8 subgroups with 100 - 149 respondents | 2 |
| Good sample size | e.g., 8 subgroups with 100 - 149 respondents | e.g., 8 subgroups with at least 150 respondents each | 3 |
| Excellent sample size | e.g., 8 subgroups with at least 150 respondents each | e.g., 8 subgroups with at least 200 respondents each | 4 |""",
    ),
    (
        """- [ ] **Not applicable [n/a]**
- [ ] **No information [0]**
- [ ] **Inadequate modelling [1]:** Procedures not appropriate or extrapolation used.
- [ ] **Adequate [2]:** Appropriate procedures but little detail or fit checks.
- [ ] **Good [3]:** Appropriate modelling and checks but some details missing.
- [ ] **Excellent: strong modelling, validation, fit checks [4]**""",
        """- [ ] Not applicable [n/a]
- [ ] No information given [0]
- [ ] Inadequate: modelling procedures are not appropriate or not well implemented or extrapolation beyond the observed data range [1]
- [ ] Adequate: appropriate modelling procedures but little detail of process or inadequate checks for fit etc. [2]
- [ ] Good: appropriate modelling procedures and model checks but some details missing [3]
- [ ] Excellent: appropriate modelling procedures and good description showing how model suitability and fit was checked, and norms created [4]""",
    ),
    ("| Good (e.g., 0.80 <= r < 0.90)     | [ ]              | **[ 3 ]**v   | 3        |", "| Good (e.g., 0.80 <= r < 0.90)     | [ ]              | **[ 3 ]**    | 3        |"),
    ("0.70 <= r < 0.80", "0.70 ≤ r < 0.80"),
    ("0.80 <= r < 0.90", "0.80 ≤ r < 0.90"),
    ("0.60 <= r < 0.70", "0.60 ≤ r < 0.70"),
    ("r >= 0.80", "r ≥ 0.80"),
    ("r >= 0.90", "r ≥ 0.90"),
    ("3.33 <= info < 5.00", "3.33 ≤ information < 5.00"),
    ("5.00 <= info < 10.00", "5.00 ≤ information < 10.00"),
    ("information >= 10.00", "information ≥ 10.00"),
    ("- **[ ]** The interval is: Free text", "- **[ ]** The interval is: Click or tap here to enter text."),
    ("- **[ ]**.... do not match the intended test takers, but effect on size of coefficients is unclear", "- **[ ]** .... do not match the intended test takers, but effect on size of coefficients is unclear"),
    ("- **[ ]** ...match intended test takers", "- **[ ]** .... match the intended test takers"),
    (
        "**Select one: [n/a | No info | Do not match (fav) | Do not match (unclear) | Do not match (unfav) | Match]**",
        """**Select one**

- **[n/a]** Not applicable
- **[ ]** No information given
- **[ ]** .... do not match the intended test takers, leading to more favourable coefficients (e.g. inflation by artificial heterogeneity)
- **[ ]** .... do not match the intended test takers, but effect on size of coefficients is unclear
- **[ ]** .... do not match the intended test takers, leading to less favourable coefficients (e.g. reduction by restriction of range)
- **[ ]** .... match the intended test takers""",
    ),
    ("- [ ] Others (describe): Free text", "- [ ] Others, describe: Click or tap here to enter text."),
    ("- [ ] Other (describe): Free text", "- [ ] Other (describe): Click or tap here to enter text."),
    ("- [ ] Other\n\n### 9.6.3 Size of coefficients", "- [ ] Other, describe: Click or tap here to enter text.\n\n### 9.6.3 Size of coefficients"),
    ("### 9.7.2 Describe method\n\nFree text.", "### 9.7.2 Describe method\n\nDescribe method: Click or tap here to enter text."),
    ("| No info        | [ ]                              | 0            |", "| No information given | [ ]                              | 0            |"),
]


@dataclasses.dataclass
class PdfHit:
    section: str
    option: str
    expected_text: str
    page: int
    context: str


@dataclasses.dataclass
class MdOption:
    section: str
    option: str
    text: str
    line_no: int
    raw: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def normalize_for_compare(text: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\uf0b3": "",
        "\u25a0": "",
        "\u2610": "",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = text.replace("\\le", "<=")
    text = text.replace("\\ge", ">=")
    text = text.replace("$", "")
    text = text.replace("**", "")
    text = text.replace("_", "")
    text = re.sub(r"\[\s*\]", "", text)
    text = re.sub(r"\[\s*-\s*\]", "", text)
    text = text.replace("≤", "<=")
    text = text.replace("≥", ">=")
    text = text.replace("â€“", "-")
    text = text.replace("â€™", "'")
    text = text.replace("â€˜", "'")
    text = text.replace("â€œ", '"')
    text = text.replace("â€\u009d", '"')
    text = re.sub(r"\[\s*(n/a|[0-4])\s*\]", r" \1 ", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:)])", r"\1", text)
    text = re.sub(r"([(])\s+", r"\1", text)
    return text.strip().lower()


def normalize_pdf_text(text: str) -> str:
    text = text.replace("\r", "\n")
    text = text.replace("\u00a0", " ")
    text = text.replace("\u2010", "-")
    text = text.replace("\u2011", "-")
    text = text.replace("\u2013", "-")
    text = text.replace("\u2014", "-")
    text = text.replace("\uf0b3", "")
    # Repair predictable extraction omissions from the icon font used in the PDF.
    text = re.sub(r"\btems\b", "Items", text)
    text = re.sub(r"\btem\b", "Item", text)
    text = re.sub(r"\bndices\b", "Indices", text)
    text = re.sub(r"\bsed\b", "Used", text)
    text = re.sub(r"\bnterpretation\b", "Interpretation", text)
    text = re.sub(r"\bverall\b", "Overall", text)
    text = re.sub(r"\borms\b", "Norms", text)
    text = re.sub(r"\borming\b", "Norming", text)
    text = re.sub(r"\banguage\b", "Language", text)
    return text


def extract_pdf_pages(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        pages.append(normalize_pdf_text(page.extract_text() or ""))
    return pages


def strip_pdf_boilerplate(text: str) -> str:
    lines = []
    for line in text.splitlines():
        compact = line.strip()
        if not compact:
            continue
        if compact.startswith("MODEL FOR THE REVIEW"):
            continue
        if compact.startswith("Developed by the European Federation"):
            continue
        if re.fullmatch(r"Page\d+", compact):
            continue
        lines.append(compact)
    return "\n".join(lines)


def full_pdf_text(pages: list[str]) -> str:
    chunks = []
    for index, page_text in enumerate(pages, start=1):
        chunks.append(f"\n[[PDF_PAGE_{index}]]\n{strip_pdf_boilerplate(page_text)}")
    return "\n".join(chunks)


def extract_section_ids(markdown_text: str) -> list[str]:
    ids: list[str] = []
    for match in re.finditer(r"^(?:#{1,6}\s+|\-\s+\*\*)?(\d+(?:\.\d+){1,5})(?=[\s.)])", markdown_text, re.MULTILINE):
        section = match.group(1).rstrip(".")
        if section not in ids:
            ids.append(section)
    return ids


def section_page(section: str, pages: list[str]) -> int | None:
    section_pattern = re.compile(rf"(?<!\d){re.escape(section)}(?!\d)")
    for index, page_text in enumerate(pages, start=1):
        if section_pattern.search(page_text):
            return index
    return None


def section_context(section: str, pages: list[str]) -> str:
    page_num = section_page(section, pages)
    if page_num is None:
        return ""
    page_text = strip_pdf_boilerplate(pages[page_num - 1])
    match = re.search(rf"(?<!\d){re.escape(section)}(?!\d)", page_text)
    if not match:
        return page_text[:1000]
    start = max(0, match.start() - 120)
    end = min(len(page_text), match.start() + 1400)
    return page_text[start:end]


def detect_md_options(markdown_text: str) -> list[MdOption]:
    options: list[MdOption] = []
    current_section = ""
    lines = markdown_text.splitlines()
    heading_re = re.compile(r"^(?:#{1,6}\s+|\-\s+\*\*)?(\d+(?:\.\d+){1,5})(?=[\s.)])")
    code_re = re.compile(r"(?:\(|\[|\*\*\[?\s*)(n/a|[0-4])(?:\s*\]?\*\*|\]|\))\s*$", re.IGNORECASE)
    any_code_re = re.compile(r"(?:\(|\[|\*\*\[?\s*)(n/a|[0-4])(?:\s*\]?\*\*|\]|\))", re.IGNORECASE)
    for i, raw in enumerate(lines, start=1):
        heading = heading_re.search(raw)
        if raw.lstrip().startswith("#") and not heading:
            current_section = ""
        if heading:
            current_section = heading.group(1).rstrip(".")
        stripped = raw.strip()
        if not current_section or not stripped.startswith(("-", "[ ]", "|")):
            continue
        if "Rating: [n/a | 0 | 1 | 2 | 3 | 4]" in stripped:
            for opt in ["n/a", "0", "1", "2", "3", "4"]:
                options.append(MdOption(current_section, opt, RATING_LABELS[opt], i, raw))
            continue
        if stripped.startswith("|"):
            cells = [cell.strip(" *") for cell in stripped.strip("|").split("|")]
            if any(re.search(r"-{3,}", cell) for cell in cells):
                continue
            nonempty = [cell for cell in cells if cell]
            if not nonempty:
                continue
            option = None
            first_code = re.match(r"^([0-4])\.\s*(.+)$", nonempty[0])
            if first_code:
                option = first_code.group(1)
                nonempty[0] = first_code.group(2)
            elif re.fullmatch(r"(?:\[?\s*)?(n/a|[0-4])(?:\s*\]?)?", nonempty[-1], re.IGNORECASE):
                option = re.search(r"(n/a|[0-4])", nonempty[-1], re.IGNORECASE).group(1).lower()
                nonempty = nonempty[:-1]
            else:
                for cell_index, cell in enumerate(nonempty):
                    code_only = re.fullmatch(r"\[?\s*(n/a|[0-4])\s*\]?", cell, re.IGNORECASE)
                    if code_only:
                        option = code_only.group(1).lower()
                        nonempty.pop(cell_index)
                        break
            if option:
                text = " ".join(nonempty)
                text = re.sub(r"\[\s*\]", "", text)
                text = re.sub(r"\s+", " ", text).strip(" :-")
                if text:
                    options.append(MdOption(current_section, option, text, i, raw))
            continue
        match = code_re.search(stripped)
        if match:
            option = match.group(1).lower()
            text = code_re.sub("", stripped)
            text = re.sub(r"^[-\s\[\]\*]+", "", text)
            text = re.sub(r"\s+", " ", text).strip(" :-")
            if text:
                options.append(MdOption(current_section, option, text, i, raw))
            continue
        match = any_code_re.search(stripped)
        if match and not stripped.startswith("|") and (stripped.startswith("- [ ]") or stripped.startswith("[ ]")):
            option = match.group(1).lower()
            text = any_code_re.sub("", stripped, count=1)
            text = re.sub(r"^[-\s\[\]\*]+", "", text)
            text = re.sub(r"\s+", " ", text).strip(" :-")
            if text:
                options.append(MdOption(current_section, option, text, i, raw))
    return options


def md_line_to_replacement(line: str, option: str, expected: str) -> str:
    indent = re.match(r"^(\s*)", line).group(1)
    prefix = f"{indent}- "
    return f"{prefix}{expected} ({option})"


def apply_known_replacements(markdown_text: str) -> tuple[str, list[MdOption]]:
    lines = markdown_text.splitlines()
    current_section = ""
    changed: list[MdOption] = []
    heading_re = re.compile(r"^(?:#{1,6}\s+|\-\s+\*\*)?(\d+(?:\.\d+){1,5})(?=[\s.)])")
    code_re = re.compile(r"(?:\(|\[|\*\*\[?\s*)(n/a|[0-4])(?:\s*\]?\*\*|\]|\))\s*$", re.IGNORECASE)
    for index, raw in enumerate(lines):
        heading = heading_re.search(raw)
        if heading:
            current_section = heading.group(1).rstrip(".")
        if current_section not in KNOWN_OPTION_REPLACEMENTS:
            continue
        stripped = raw.strip()
        if not stripped.startswith("-"):
            continue
        match = code_re.search(stripped)
        if match:
            option = match.group(1).lower()
        elif "Excellent:" in stripped and "4" in KNOWN_OPTION_REPLACEMENTS[current_section]:
            option = "4"
        else:
            continue
        expected = KNOWN_OPTION_REPLACEMENTS[current_section].get(option)
        if not expected:
            continue
        new_line = md_line_to_replacement(raw, option, expected)
        if raw != new_line:
            original_text = code_re.sub("", stripped)
            original_text = re.sub(r"^[-\s\[\]\*]+", "", original_text)
            changed.append(MdOption(current_section, option, original_text.strip(" :-"), index + 1, raw))
            lines[index] = new_line
    return "\n".join(lines) + ("\n" if markdown_text.endswith("\n") else ""), changed


def apply_text_replacements(markdown_text: str) -> tuple[str, list[str]]:
    applied: list[str] = []
    for index, (old, new) in enumerate(TEXT_REPLACEMENTS, start=1):
        if old in markdown_text:
            markdown_text = markdown_text.replace(old, new)
            applied.append(f"text replacement {index}")
        else:
            print(f"warning: text replacement {index} did not match", file=sys.stderr)
    return markdown_text, applied


def expected_hits(section_ids: list[str], pages: list[str]) -> dict[tuple[str, str], PdfHit]:
    hits: dict[tuple[str, str], PdfHit] = {}
    all_text = full_pdf_text(pages)
    for section in section_ids:
        page = section_page(section, pages) or 0
        context = section_context(section, pages)
        for option, label in RATING_LABELS.items():
            # A bare rating sequence means the option exists even when the row has no long descriptor.
            if re.search(r"\bn/a\s+0\s+1\s+2\s+3\s+4\b", context):
                hits[(section, option)] = PdfHit(section, option, label, page, context)
        if section in KNOWN_OPTION_REPLACEMENTS:
            for option, text in KNOWN_OPTION_REPLACEMENTS[section].items():
                hits[(section, option)] = PdfHit(section, option, text, page, context)
    # Validate known replacements are in the PDF extraction or at least on the same page context.
    for section, mapping in KNOWN_OPTION_REPLACEMENTS.items():
        for option, expected in mapping.items():
            if normalize_for_compare(expected) not in normalize_for_compare(all_text):
                print(
                    f"warning: expected replacement not found verbatim in extracted PDF text: {section} {option}",
                    file=sys.stderr,
                )
    return hits


def option_status(md: MdOption, hit: PdfHit | None, all_pdf_norm: str) -> tuple[str, str]:
    md_norm = normalize_for_compare(md.text)
    if hit is None:
        if md_norm and md_norm in all_pdf_norm:
            return "match_elsewhere", "Option text found in PDF, but section/rating mapping was not explicit."
        return "not_validated", "No explicit PDF option mapping was extracted for this section/rating."
    expected_norm = normalize_for_compare(hit.expected_text)
    if md_norm == expected_norm:
        return "match", ""
    if md_norm in normalize_for_compare(hit.context):
        return "match_context", "Text appears in the same PDF section context after normalization."
    ratio = difflib.SequenceMatcher(a=md_norm, b=expected_norm).ratio()
    if ratio >= 0.92:
        return "formatting_difference", "Only minor formatting/label differences detected."
    return "text_mismatch", ""


def report_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>")


def write_report(
    report_path: Path,
    source_md: Path,
    source_pdf: Path,
    v2_path: Path,
    options: list[MdOption],
    hits: dict[tuple[str, str], PdfHit],
    changed: list[MdOption],
    pages: list[str],
) -> None:
    all_pdf_norm = normalize_for_compare(full_pdf_text(pages))
    rows = []
    counts: dict[str, int] = {}
    for md in options:
        hit = hits.get((md.section, md.option))
        status, note = option_status(md, hit, all_pdf_norm)
        counts[status] = counts.get(status, 0) + 1
        expected = hit.expected_text if hit else ""
        page = str(hit.page) if hit and hit.page else ""
        if status not in {"match", "match_context", "match_elsewhere"}:
            rows.append(
                "| "
                + " | ".join(
                    [
                        report_escape(status),
                        report_escape(md.section),
                        report_escape(md.option),
                        report_escape(str(md.line_no)),
                        report_escape(page),
                        report_escape(md.text),
                        report_escape(expected),
                        report_escape(note),
                    ]
                )
                + " |"
            )
    changed_rows = []
    for md in changed:
        expected = KNOWN_OPTION_REPLACEMENTS[md.section][md.option]
        changed_rows.append(
            "| "
            + " | ".join(
                [
                    report_escape(md.section),
                    report_escape(md.option),
                    report_escape(str(md.line_no)),
                    report_escape(md.text),
                    report_escape(expected),
                ]
            )
            + " |"
        )

    lines = [
        "# EFPA PDF-to-Markdown Option Validation",
        "",
        f"- Source markdown: `{source_md.as_posix()}`",
        f"- Source PDF: `{source_pdf.as_posix()}`",
        f"- Corrected v2 markdown: `{v2_path.as_posix()}`",
        f"- PDF pages extracted: {len(pages)}",
        f"- Markdown option entries scanned: {len(options)}",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "| --- | ---: |",
    ]
    for status in sorted(counts):
        lines.append(f"| {status} | {counts[status]} |")
    lines.extend(
        [
            "",
            "## Applied Corrections",
            "",
            "The table below lists targeted row-level corrections. The v2 generator also applies PDF-confirmed block replacements for the global rating scale, Section 8 norm-rating tables, and Section 9 reliability threshold tables.",
            "",
            "| Section | Option | Original line | Original markdown text | PDF-corrected text |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    lines.extend(changed_rows or ["| _None_ |  |  |  |  |"])
    lines.extend(
        [
            "",
            "## Non-Matching or Unvalidated Option Entries",
            "",
            "`match_elsewhere` means the option text was found in the extracted PDF text but could not be tied to a section-specific PDF map by the lightweight parser. Rows below are unresolved mismatches or unvalidated entries after v2 corrections.",
            "",
            "| Status | Section | Option | Markdown line | PDF page | Markdown text | PDF expected text | Note |",
            "| --- | --- | --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    lines.extend(rows or ["| _None_ |  |  |  |  |  |  |  |"])
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--v2", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    markdown_text = read_text(args.markdown)
    pages = extract_pdf_pages(args.pdf)
    section_ids = extract_section_ids(markdown_text)
    options = detect_md_options(markdown_text)
    hits = expected_hits(section_ids, pages)

    if args.v2.exists():
        args.v2.unlink()
    shutil.copyfile(args.markdown, args.v2)
    v2_text, text_changes = apply_text_replacements(markdown_text)
    v2_text, changed = apply_known_replacements(v2_text)
    args.v2.write_text(v2_text, encoding="utf-8", newline="")

    v2_options = detect_md_options(v2_text)
    write_report(args.report, args.markdown, args.pdf, args.v2, v2_options, hits, changed, pages)
    print(f"scanned_options={len(v2_options)}")
    print(f"applied_corrections={len(changed) + len(text_changes)}")
    print(f"v2={args.v2}")
    print(f"report={args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

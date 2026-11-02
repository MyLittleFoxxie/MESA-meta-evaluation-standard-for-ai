#!/usr/bin/env python3
"""Build the standalone MESA rubric audit single-page application and markdown companion."""
import hashlib
import json
from pathlib import Path

DIR = Path(__file__).resolve().parent

def main():
    packet_raw = (DIR / "packet.json").read_bytes()
    packet = json.loads(packet_raw.decode("utf-8"))
    digest = hashlib.sha256(packet_raw).hexdigest()

    # Build standalone HTML
    template = (DIR / "template.html").read_text(encoding="utf-8")
    packet_escaped = json.dumps(packet, ensure_ascii=False).replace("<", "\\u003c")
    html = template.replace("__PACKET_JSON__", packet_escaped)
    
    out_html = DIR / "audit.html"
    out_html.write_text(html, encoding="utf-8")
    print(f"Generated standalone audit app: {out_html} ({out_html.stat().st_size:,} bytes)")
    print(f"Packet SHA256: {digest[:16]}...")

    # Build printable markdown companion
    md_lines = [
        f"# {packet['title']}",
        f"*{packet['subtitle']}*",
        "",
        f"**Audit ID:** `{packet['audit_id']}` | **Version:** {packet['version']} | **Packet SHA-256:** `{digest[:16]}`",
        "",
        "## Benchmark Overview",
        f"**Target:** {packet['benchmark']['name']} (commit `{packet['benchmark']['commit']}`)",
        f"{packet['benchmark']['overview']}",
        "",
        "---",
        "",
        "## Part A: Design Facets (OECD Classification)",
        ""
    ]

    for f in packet["part_a"]:
        md_lines.append(f"### Facet: {f['facet']}")
        md_lines.append(f"- **AI Classification:** `{f['agent']['value']}`")
        md_lines.append(f"- **AI Reason:** {f['agent']['reason']}")
        if f["agent"]["evidence"]:
            for ev in f["agent"]["evidence"]:
                md_lines.append(f"- **Cited Evidence:** {ev['source']} ({ev['locator']}): *\"{ev['quote']}\"*")
        md_lines.append("- **Audit Verdict:** [ ] Confirmed  [ ] Overstated  [ ] Contradicted  [ ] Cannot judge")
        md_lines.append("")

    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Part B: Evaluative Questions (MESA Rubric)")
    md_lines.append("")

    for q in packet["part_b"]:
        md_lines.append(f"### Question {q['id']}: {q['question']}")
        md_lines.append(f"- **AI Assigned Anchor:** `{q['agent']['answer'].upper()}` (Basis: {q['agent']['basis']})")
        md_lines.append(f"- **AI Reason:** {q['agent']['reason']}")
        if q["agent"]["missing"]:
            md_lines.append(f"- **Missing for Higher Anchor:** {q['agent']['missing']}")
        if q["agent"]["evidence"]:
            for ev in q["agent"]["evidence"]:
                md_lines.append(f"- **Cited Evidence:** {ev['source']} ({ev['locator']}): *\"{ev['quote']}\"*")
        md_lines.append("- **Audit Verdict:** [ ] Confirmed  [ ] Overstated  [ ] Absence Plausible  [ ] Contradicted  [ ] Cannot judge")
        md_lines.append("")

    out_md = DIR / "audit.md"
    out_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(f"Generated printable companion: {out_md} ({out_md.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()

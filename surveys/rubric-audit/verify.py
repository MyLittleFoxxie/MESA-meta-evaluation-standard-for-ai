#!/usr/bin/env python3
"""Automated verification test suite for MESA rubric audit platform."""
import json
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent

def verify():
    packet_path = DIR / "packet.json"
    html_path = DIR / "audit.html"
    
    assert packet_path.exists(), "packet.json missing"
    assert html_path.exists(), "audit.html missing"
    
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    
    # 1. Structure counts
    assert len(packet["part_a"]) == 8, f"Expected 8 Part A facets, got {len(packet['part_a'])}"
    assert len(packet["part_b"]) == 29, f"Expected 29 Part B questions, got {len(packet['part_b'])}"
    assert len(packet["feedback"]) == 5, f"Expected 5 feedback questions, got {len(packet['feedback'])}"
    assert len(packet["familiarity"]) == 4, f"Expected 4 familiarity questions, got {len(packet.get('familiarity', []))}"
    assert len(packet["definitions"]) >= 75, f"Expected at least 75 definitions, got {len(packet.get('definitions', []))}"
    assert len(packet["verdict_options"]) == 5, "Expected 5 verdict options"
    
    # 2. Check repo files & PDF
    repo_files = packet["benchmark"]["repo_files"]
    assert "README.md" in repo_files, "README.md missing from repo files"
    assert "human_eval/execution.py" in repo_files, "execution.py missing from repo files"
    assert len(packet["benchmark"]["paper_text"]) > 10000, "paper_text too small or missing"
    assert (DIR / "paper.pdf").exists(), "paper.pdf missing"
    assert (DIR / "paper.pdf").stat().st_size > 1000000, "paper.pdf incomplete"
    
    # 3. Check citations
    for f in packet["part_a"]:
        assert f["agent"]["value"] is not None, f"Facet {f['facet']} missing agent value"
        for ev in f["agent"]["evidence"]:
            assert ev["source"], f"Facet {f['facet']} citation missing source"
            assert ev["quote"], f"Facet {f['facet']} citation missing quote"

    for q in packet["part_b"]:
        assert q["agent"]["answer"] is not None, f"Question {q['id']} missing agent answer"
        assert q["shown"] and q["checked"], f"Question {q['id']} missing anchor definitions"

    # 4. Check HTML bundle
    html_content = html_path.read_text(encoding="utf-8")
    assert "<!doctype html>" in html_content
    assert "mesa-v4-humaneval-audit-v1" in html_content
    assert "workbench" in html_content
    assert "Official PDF" in html_content
    assert "Paper Text" in html_content
    assert "term-tip" in html_content
    assert "annotate" in html_content
    assert "exportCSV" in html_content
    assert "exportJSON" in html_content

    print("All verification checks PASSED successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(verify())

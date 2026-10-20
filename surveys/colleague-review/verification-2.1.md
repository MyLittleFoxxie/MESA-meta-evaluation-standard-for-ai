# Packet 2.1 verification

Prepared 18 October 2026. These are implementation checks, not human-study findings or evidence of email delivery.

- Packet: `mesa-guided-arc-designqa-v2-1`, SHA256 `7492b86e907565c9ca65508063eb1aaa45e9f213f37afbe863a39f3a5f5a3547`.
- `verify.py` compares all 25 questions, explanations, HLE answers/reasons and answer instructions with the saved study input in `study-alignment.txt`. It checks that passages, definitions, choices and source records equal archived 2.0, and verifies source and packet fingerprints.
- `build.py` generates HTML and printable Markdown from packet/template sources. Extracted JavaScript passes `node --check`.
- `check-browser.cjs` exercises the seven-stage flow, blank starting answers, required familiarity/benchmark/feedback responses, Cannot judge, optional text, Back/Continue, keyboard controls, inline definitions, draft restoration, incompatible packet/fingerprint rejection, and failed/accepted deliveries with retry identifiers. Both rating and comment changes produce a new identifier; unchanged retries retain theirs. All delivery requests are mocked.
- Browser checks cover desktop/mobile, light/dark themes and doubled text size with horizontal overflow checks. Generated screenshots were visually inspected.
- Prior packet, generated HTML/Markdown, source manifest and HLE notes remain in `archive/v2.0/`. Frozen model-study files and participant records are untouched.

No email, real response, additional experiment, human recruitment, manuscript edit or LaTeX compilation is part of this update. Manuscript layout/page length were not checked. Publication uses only survey-related files and the repository guide in an isolated checkout of the Pages branch.

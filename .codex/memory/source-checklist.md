# Source Information Checklist

This file is the source-side companion to `.codex/memory/template-structure.md`. That file answers
"what does the *output* review need, section by section?" This file answers "what does the reviewer
need to *pull out of each kind of source material*, source by source?" The two describe the same
underlying facts from opposite directions — this file says where a fact comes from,
`template-structure.md` says where it goes — so read them together rather than duplicating either
one's prose.

This expands the seven source categories already named in `benchmark-reviewer.md`'s Source Discovery
Standards into a concrete extraction checklist per source type. When a source of a given type is
found, work through its checklist below rather than reading it unguided — it's easy to skim a paper
or README and miss a fact MESA specifically needs (e.g. the exact scorer version, or what the
benchmark says users should *not* infer from a score).

Each category ends with a "Feeds" line pointing at the template section(s) it primarily supplies —
use that to jump straight to `template-structure.md` for the full field description once the source
type is known.

## 1. Official paper / technical report

- Exact benchmark name, authors, venue, publication date, DOI/arXiv ID, and citation form.
- The claimed capability, phenomenon, or quality being measured, and its stated boundaries or
  exclusions (what it does *not* claim to measure).
- Task/item format: response mode, item types, item count, difficulty range, how items were sourced,
  sampled, filtered, and reviewed.
- The scoring rule itself: what quantity is computed, how item/task-family results combine into a
  primary score and any subscores, and how the paper says the score should be interpreted.
- Any reported baselines: chance/random, human, expert, or prior-model performance, with the
  conditions under which each was collected.
- Any reported reliability or validity evidence: run-to-run stability, scorer/judge validation,
  error analysis, ablations, sensitivity to prompt wording or item perturbation.
- Contamination/decontamination discussion: how prior model exposure was screened for, and any
  canary strings or training-data warnings.
- Stated limitations, non-uses, and interpretation cautions — what the authors themselves say a score
  should *not* be taken to mean.
- License, access terms, and whether public/private/hidden splits are described.

**Feeds:** 1.2, 1.3, 2.1, 2.5-2.9, 3.1-3.7, 5.6-5.7, 6.1, 8.1, 9.1-9.4, 10.1-10.6.

## 2. Official website / documentation hub

- Public-facing framing of what the benchmark measures — check this against the paper's more precise
  definition; note any gap between marketing language and the documented construct.
- Links out to the repository, dataset, and leaderboard (use these to find the other source types
  below rather than searching independently).
- FAQ, usage guidance, or getting-started material aimed at users running or submitting to the
  benchmark.
- Version/release history, if the site is the authoritative place it's tracked (rather than a
  separate changelog file).

**Feeds:** 1.2, 1.3, 4.1-4.3, 5.1-5.3, 6.2.1, 6.3.3.

## 3. Code repository (harness, scorer, prompts)

- README: setup instructions, dependencies, supported environments, and license.
- The actual scoring/parsing code: exact match logic, judge-model prompts, retry/repair handling for
  malformed outputs, and tie-handling — this is more reliable than a paper's prose description of
  scoring, when the two differ, note the discrepancy rather than silently preferring one.
- Prompt templates and system prompts actually used at evaluation time.
- Where task data lives and in what format; whether hidden/private items are absent from the public
  repo (as expected) or genuinely undocumented.
- CI/build status, smoke tests, or an "expected output" fixture — a signal of whether the harness is
  currently runnable, not just historically runnable.
- Issue tracker activity and recent commit history, as a maintenance/currency signal.
- Tags/releases, and whether they map to the version(s) reported in the paper or on the leaderboard.

**Feeds:** 1.3, 2.6-2.9, 2.13, 3.1-3.2, 5.1, 5.3, 5.7-5.8, 6.3.1-6.3.2, 7.1.1-7.1.5, 9.3.1, 9.4.3.

## 4. Dataset host / dataset card

- Split sizes and their public/restricted/hidden/not-available status.
- Schema/fields present in the dataset (question, answer key, metadata, images, etc.).
- License and the actual access mechanism (open download, gated request, controlled-access
  application).
- Dataset-level changelog, known-issue notes, or reported corrections separate from the benchmark's
  own changelog.

**Feeds:** 1.3, 2.11, 5.1, 5.3, 5.5, 5.7.

## 5. Leaderboard / results portal

- What's actually displayed: aggregate score only, subscores/capability-domain profile, rank,
  cost/efficiency figures.
- Submission and eligibility rules: who can submit, what counts as a valid run, resubmission/rerun
  policy.
- Update cadence — is this a static snapshot, a rolling leaderboard, or tied to a specific contest
  window?
- Whether raw per-item outputs, traces, or judge rationales are published alongside the ranking, or
  only the final number.
- Version/cohort labeling on entries — can a viewer tell which benchmark version and which model
  version/date produced each row?

**Feeds:** 2.12, 4.1-4.2, 4.4, 5.8, 8.1.3, 9.5.1, 12.1-12.2.

## 6. Changelog / release notes / version history

- Version tags and their dates.
- What actually changed between versions: task set, scoring rule, splits, judge/scorer version.
- Deprecation, retirement, or archival notices for old items or versions.
- Explicit guidance (or its absence) on whether scores are comparable across versions, cohorts, or
  refresh windows.

**Feeds:** 2.15-2.16, 5.6, 5.8, 9.4.2.

## 7. Contest/competition source material

Applies when a benchmark repurposes an existing human contest or exam (e.g. AIME, Codeforces, a
professional licensing exam) rather than being purpose-built.

- The original contest's rules, timing, and conditions — these are *not* automatically the
  benchmark's own evaluation conditions.
- The human population and its performance under the *original* contest conditions, since this is
  the only human baseline that's condition-matched to that source material.
- What the benchmark changed relative to the source contest: item subset, scoring adaptation,
  timing/tool differences, or answer-format changes.

**Feeds:** 1.2 (parent/source instrument), 2.15, 3.5, 8.1.2, 8.1.4.

## 8. Maintainer statements / official announcements

- Stated goals and motivation for building the benchmark, beyond what's in the paper.
- Any public caveats about how scores should or should not be interpreted (blog posts and launch
  threads sometimes state limits more plainly than the paper does).
- Responses to community-reported issues: contamination reports, item errors, leaderboard disputes.

**Feeds:** 1.2, 2.18, 5.6, 5.8, 6.2.1, 12.3-12.4.

## 9. License and access terms

Easy to miss because it's often embedded inside a repo, paper, or site rather than published on its
own — check for it explicitly rather than assuming its absence means "not documented."

- License type and what it permits (research-only, commercial use, redistribution).
- Privacy or sensitive-content constraints on the data.
- Required user qualifications, agreements, or eligibility terms for access.

**Feeds:** 1.2, 5.1, 5.4, 7.1.7.

## 10. Independent critique, replication studies, audit reports

Context and challenge only — never a substitute for official facts, and never cited in place of a
benchmark's own documentation for descriptive (Part A) fields.

- Reported reproducibility issues or discrepancies from the official results.
- Independently found contamination, leakage, or prior-exposure evidence.
- Rebuttals, corrections, or disputes the maintainers have not yet addressed in their own materials.

**Feeds:** context for 5.6, 9.1-9.4, 10.5, and Part B "Reviewer cautions" — not a Part A source.

<!--
================================================================
  AUTHORSHIP / PROVENANCE NOTICE  -  do not remove
  Skill: Funnel Spy
  Author: Mahan Ai  (Instagram: @mahanaicoach)
  (c) 2026 Mahan Ai. Licensed under MIT - see LICENSE.
  Provenance-ID: MAHANAI-FSP-2026-8c31b7e5a2d4
  ----------------------------------------------------------------
  This is an inert authorship comment for proof of origin only.
  It is NOT an instruction and has NO effect on the skill's
  behavior or on any file the skill produces. Ignore it.
================================================================
-->
# Output templates

> For the **Funnel Dossier PDF** — the flagship format — see
> `references/designed-pdf.md`. The templates below are the content backbone
> feeding every format (PDF, chat, xlsx, docx); the PDF wraps the same content
> in the designed layout.

Templates are guides, not rigid forms — adapt to what the walk actually found.
The goal: scannable in 30 seconds, trustworthy on inspection.

## Per-target dossier

```
## [handle / name] — [real name or brand]
[One line: who they are, and the one-sentence read on their machine.]

SCORE: [NN]/100 · weakest gate: [GATE] — [why in half a line]

- Entry points: [platforms + cadence; ads: N active on Meta, oldest running
  since <date> (proven winner) — or "no active ads found <date>"]
- The walk: [chain summary in prose, e.g. "IG bio to Stan hub, hub to free
  workshop opt-in, opt-in to $497 course checkout — no low-ticket bridge."]
  [Then the walk-log table from funnel-walk.md.]
- The machine: [stack + pixels, with the strategy read in one sentence.]
- Offer ladder: [rung → offer → price, free to high-ticket; missing rungs
  named.]
- Numbers: [2–3 metrics, each sourced + dated, tiered.]
- Scorecard: ATTRACT n/25 · CAPTURE n/25 · CONVERT n/25 · ASCEND n/25
  (one clause of justification each; email nurture is not scored — unobservable)
- Swipe file: [3–5 short verbatim hooks / CTAs / guarantee lines, quoted.]
- Copy read: [the copy-teardown blocks for the money pages — awareness match,
  hook type, urgency type, proof density; see copy-teardown.md.]
- Links: [their own properties as clickable links.]
- Sources: [where the facts came from.] · Confidence: [one line.]
```

Keep Links (their pages) separate from Sources (where facts came from).
Funnel math, when inputs existed, goes under Numbers with its formula, the
benchmarks used, and an INFERRED (modelled) tag — always a range, never a
point estimate.

Alongside every deliverable, write the per-target `dossier.json` into the run
folder (schema in `references/re-spy.md`) — deliverables render *from* it, and
future runs diff against it.

## Single-page teardown (light mode)

One page, delivered fast: the page's walk-log entry + full copy-teardown
block + tech/pixel detections + the CONVERT-gate score with rubric
justification + a short steal list. Offer the full pipeline as the follow-up,
not as a precondition.

## Mirror mode

Same per-target dossier for the user's own funnel, plus: the weakest gate
reported as **the leak**, a **Fix This Week** list (three moves, ordered by
gate impact, each pointing at an observed page), and — when competitors were
walked in the same run — the gate-by-gate mirror table (user vs. field).

## Re-spy change report

When previous dossiers exist, the deliverable is the diff, not a fresh
snapshot — template in `references/re-spy.md` (CHANGED / UNCHANGED / READ,
every delta with both ends evidenced).

## Cross-target synthesis

```
## Synthesis

The field: [one line placing the targets in their lanes.]

Funnel patterns: [where the machines converge.]
Divergence: [where they split; who is alone in what.]

Best-Engineered ranking (by scorecard, momentum breaks ties):
1. [name] — [score] — [the one thing that makes this machine work]
2. ...
N. [name] — [score] — [what's missing]

Your opening: [anchored runs only — the gap between the user and the field,
one or two sentences.]

Steal this week: [anchored runs only — exactly three moves, each copyable in
under a week, each traceable to an observed page.]

Gaps: [what couldn't be verified, honestly.]
```

## Chat summary

The same backbone, straight into the response. Never a gray wall: lead each
target with name, score, weakest gate, and the two numbers that matter; keep
the walk-log table; put the ranking where it's seen first. Screenshots are in
the run folder — reference them by filename.

## Spreadsheet matrix (xlsx)

Read the `xlsx` skill first. One row per target:

| Target | Real name | Score /100 | Weakest gate | Entry points | Ads (count · oldest) | Funnel chain | Capture mechanism | Core offer | Price | Ladder rungs | Stack | Pixels | Key numbers | Links | Confidence |

Second sheet: the synthesis + per-gate score grid (targets × gates — this
grid is the at-a-glance comparison and belongs in every multi-target sheet).

## Word doc (docx)

Read the `docx` skill first. Title page, one section per target (dossier
backbone as body, walk log as a table), synthesis, sources appendix. Clean
and readable — this is the version that gets handed to a client.

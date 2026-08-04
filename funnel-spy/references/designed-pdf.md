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
# The Funnel Dossier — designed PDF

The flagship output. It should read like a case file from an intelligence
service, not a marketing deck — because the content *is* surveillance: walked
pages, captured copy, detected machinery.

## The aesthetic — commit to it fully

One committed look. No gradients, no emoji, no decorative icons, no rounded
pastel cards. The design is **paper, ink, one signal color, and monospace
evidence**:

- **Paper** `#F7F5EF` (page background of inner pages), **ink** `#131912`.
- **One signal color:** dossier green `#1F6E52`. It carries rank bars, gate
  bars, the takeaway stamp, and links. Nothing else gets color — except the
  three evidence-tier colors, which are semantic, not decorative:
  CONFIRMED `#1F8A57` · REPORTED `#B07818` · INFERRED `#6B7280`.
- **Type:** Helvetica/Arial stack for prose (never rely on web fonts —
  WeasyPrint may fail to fetch them). **Courier/monospace for everything
  captured**: URLs, verbatim headlines, CTA labels, prices, stack signatures.
  The mono-for-evidence rule is the design's signature move — a reader can see
  at a glance what was *observed* versus what was *written*.
- **Structure:** hairline rules (`0.6pt` `#D8D4C8`), uppercase letter-spaced
  micro-labels, generous margins. Tier tags look like stamps: mono, uppercase,
  1pt border in the tier color, slight letter-spacing, no fill.

## Structure (always these four parts)

1. **Cover** — full-bleed deep ink-green (`#0C1F18`), mono type. Top line:
   `CASE FILE · FUNNEL SPY`. Big title = the run's subject ("3 funnels,
   walked"). A mono manifest block listing the targets like case items, the
   run date, walk mode (browser-walked with screenshots vs fetch-based), and
   the tier legend as three stamps. Bottom line: "Prepared with the Funnel Spy
   skill · Mahan Ai".
2. **Scoreboard** — one row per target, ranked: rank number, name, total
   score in big mono digits, then five small labeled gate bars (0–20 each) in
   signal green with the weakest gate's bar in REPORTED amber. Caption states
   plainly: "Rubric-scored qualitative read — see gate anchors."
3. **One dossier spread per target** (`page-break-before`):
   - Header: handle + real name, one-line read, score badge, confidence note.
   - **The walk rail** — the funnel map, drawn as a vertical rail: numbered
     step markers connected by a hairline, each step a row: role stamp
     (`OPT-IN`), mono URL, one-line capture (headline → CTA → price). This
     rail is the page's centerpiece — it *is* the funnel.
   - **Stat chips** — 2–4 numbers (audience, ads longevity, price points),
     values colored by tier.
   - **Offer ladder** — compact table, free → high ticket, missing rungs shown
     as a struck-through row ("no low-ticket bridge").
   - **The machine** — stack + pixels as mono chips, one-sentence strategy
     read underneath.
   - **Swipe file** — captured lines in a mono block on paper, quoted, tiered.
   - **Screenshot filmstrip** — 3–4 thumbnails from the run folder with mono
     captions (`03-optin.png · 1 field · "Get the free system"`). Skip the
     strip entirely in fetch-based walks rather than faking it.
4. **Synthesis** — patterns, divergence, the ranking recap, Your Opening,
   Steal This Week as three numbered moves, gaps. The sharpest line of the
   whole run goes in a **stamp box**: 2pt signal-green border, uppercase mono
   label `FINDING`, the line in large type.

## How to render

Author one self-contained HTML string with embedded CSS; render with
**WeasyPrint** (`pip install weasyprint`, add `--break-system-packages` if
needed):

```python
from weasyprint import HTML
HTML(string=doc, base_url=".").write_pdf("Funnel-Dossier.pdf")
```

Build the HTML from a Python list of per-target dicts so layout stays
consistent: `handle, name, one, score, gates` (dict of 5 ints), `walk` (list
of step dicts: `n, role, url, capture`), `chips` (list of `(value, label,
tier)`), `ladder` (list of `(rung, offer, price)`), `stack`, `pixels`,
`swipes`, `shots` (list of `(path, caption)`), `links, conf`.

Screenshots embed by relative path from the run folder — pass `base_url` so
WeasyPrint resolves them.

**Verify before delivering:** render pages to images (`pdftoppm -jpeg -r 90
Funnel-Dossier.pdf page`) and actually look at them — check the rail aligns,
bars match scores, nothing overflows, filmstrip images loaded (a missing image
renders as a blank box; that's a bug, fix it). Design bugs are invisible in
code. If WeasyPrint can't install, fall back to ReportLab and reproduce the
same four-part structure.

## Key CSS

```css
@page { size: Letter; margin: 16mm 15mm 18mm; background: #F7F5EF;
  @bottom-center { content: "FUNNEL SPY · <date> · " counter(page) " / " counter(pages);
    font-family: Courier, monospace; font-size: 7.5pt; color: #8A8676; } }
@page cover { margin: 0; }
body { font-family: Helvetica, Arial, sans-serif; color: #131912;
  font-size: 9.4pt; line-height: 1.5; }
.mono { font-family: Courier, "Courier New", monospace; }
.cover { page: cover; height: 100vh; background: #0C1F18; color: #E9E6DC;
  padding: 28mm 20mm; }
.cover .case { font-family: Courier, monospace; font-size: 10pt;
  letter-spacing: 3px; color: #7FBFA3; }
.cover h1 { font-size: 40pt; font-weight: 800; letter-spacing: -1px; }
.manifest { font-family: Courier, monospace; font-size: 9.5pt;
  border: 1px solid #2E4A3D; padding: 6mm; margin-top: 10mm; }
.stamp { font-family: Courier, monospace; font-size: 7.5pt; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase; border: 1pt solid;
  padding: 1.5px 7px; }
.t-ok { color: #1F8A57; border-color: #1F8A57; }
.t-rep { color: #B07818; border-color: #B07818; }
.t-inf { color: #6B7280; border-color: #6B7280; }
.hr { border: 0; border-top: 0.6pt solid #D8D4C8; margin: 5mm 0; }
.k { font-size: 7.4pt; font-weight: 800; letter-spacing: 1.2px;
  text-transform: uppercase; color: #8A8676; }
.score { font-family: Courier, monospace; font-size: 20pt; font-weight: 700; }
.gatebar { height: 8px; background: #E4E1D4; }
.gatefill { height: 8px; background: #1F6E52; }
.gatefill.weak { background: #B07818; }
.rail { border-left: 0.8pt solid #B9B4A4; margin-left: 4mm; padding-left: 6mm; }
.step { position: relative; padding: 2.2mm 0; page-break-inside: avoid; }
.step .n { position: absolute; left: -8.6mm; top: 2.2mm; width: 5mm; height: 5mm;
  background: #131912; color: #F7F5EF; font-family: Courier, monospace;
  font-size: 7.5pt; text-align: center; line-height: 5mm; }
.step .url { font-family: Courier, monospace; font-size: 8pt; color: #1F6E52; }
.ladder td { border-bottom: 0.6pt solid #D8D4C8; padding: 1.6mm 2mm;
  font-size: 9pt; }
.chip { display: inline-block; font-family: Courier, monospace; font-size: 8pt;
  border: 0.8pt solid #B9B4A4; padding: 1.5px 6px; margin: 0 3px 3px 0; }
.swipe { font-family: Courier, monospace; font-size: 8.8pt; background: #EFECE0;
  border-left: 2pt solid #1F6E52; padding: 3mm 4mm; }
.film { display: flex; gap: 4mm; } .film img { width: 100%; border: 0.8pt solid #B9B4A4; }
.film figcaption { font-family: Courier, monospace; font-size: 7pt; color: #8A8676; }
.finding { border: 2pt solid #1F6E52; padding: 5mm 6mm; margin-top: 6mm; }
.finding .k { color: #1F6E52; }
```

## The principle

The dossier is the shareable proof that the walk happened. Every design choice
serves credibility: mono = observed, stamps = evidence tiers, the rail = the
actual path, the filmstrip = receipts. Bland output — or decorated output —
both undercut it. Even the chat format inherits the discipline: score first,
weakest gate named, evidence tiers visible.

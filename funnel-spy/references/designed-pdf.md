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
# The Funnel Dossier — the visual report

**You do not write this report. You write JSON and run one script.**

```
python3 scripts/render_dossier.py <run-folder>
```

The script reads `dossier.json` (or `*.dossier.json` for several targets) plus
an optional `synthesis.json`, and draws every page. That is the whole delivery
step. Do not hand-author HTML or a bespoke renderer — hand-built reports are
slow, inconsistent, and the first thing to get dropped when a run runs long.

## The one design rule: show, don't tell

Anyone should understand this report without a marketing vocabulary. A page
that needs a paragraph to explain a concept has failed; draw it instead.

- **The funnel is a map, not a list.** Numbered boxes connected by arrows, each
  with the URL, the headline in quotes, and a plain-English caption of what
  that page does to you ("he gets your details"). Boxes where money changes
  hands are filled green with the price set large. A reader should trace the
  whole path with a finger.
- **The offer ladder is a staircase.** Bars rising left to right, cheapest to
  dearest, price above each step and the offer named below. The shape carries
  the meaning: gaps and dead ends are visible without reading a word.
- **The score is bars, not numbers in prose.** Four gates, each with its
  plain-English translation underneath (ATTRACT → "getting found"). The weakest
  bar is amber and labelled "← weakest".
- **Plain page titles.** "The funnel, step by step" · "What he sells, cheapest
  to dearest" · "The scorecard" · "Under the hood" · "So what do you do about
  it?" — never jargon like "Monetization Architecture".
- **Prose is captions.** One or two sentences under a visual, never a wall.

## The pages

1. **Cover** — deep ink-green, mono type, the target's portrait plate(s), a
   manifest block (subject, date, method) and the evidence-tier stamps.
2. **The channel map** — "Where the traffic comes from": every platform, the
   exact link it points at, and the convergence into one entry page. The funnel
   above the website; comes first because that is where the visitor starts.
3. **The funnel map** — portrait, one-line read, then the map. The hero page.
4. **The staircase** — the offer ladder as a bar chart.
5. **The scorecard** — headline number chips (coloured by evidence tier), the
   big total, and the four gate bars.
6. **Under the hood** — tool/pixel chips with the strategy read, the ads block
   **including a clickable link to each ad library so the reader can go see
   every ad themselves**, the swipe file, screenshot filmstrip, and a clickable
   directory of every door in the funnel.
7. **So what do you do about it?** — ranking (multi-target), the FINDING stamp
   box, Your Way In, Steal/Fix This Week, and what could not be checked.

Sections whose data is missing are skipped automatically — a recon-only run
still renders a valid, shorter dossier.

## Design tokens (already implemented in the script)

- Paper `#F7F5EF`, ink `#131912`, one signal green `#1F6E52`, amber `#B07818`
  for the weakest gate only, hairlines `#C9C4B4`.
- Evidence tiers: CONFIRMED `#1F8A57` · REPORTED `#B07818` · INFERRED `#6B7280`.
- Helvetica/Arial for prose, **Courier for everything captured** — URLs,
  verbatim copy, prices, stack signatures. Mono means observed.
- Portraits and screenshots are greyscale, hairline-bordered.

## Verify before delivering — always

```
pdftoppm -jpeg -r 70 <pdf> page
```

Then **actually open the images.** Check: every portrait and screenshot
loaded (a blank box is a bug), no text collides, no stranded near-empty pages,
gate bars match the numbers. Fix the JSON or the script and re-render. Design
bugs are invisible in code.

## If you must change the design

Edit `scripts/render_dossier.py` — never fork it per run. Two gotchas already
solved in there, worth not re-discovering:

- **WeasyPrint does not render inline `<svg>`.** Diagrams are embedded as
  base64 `data:image/svg+xml` images via `svg_img()`.
- **SVG text does not wrap.** Use the `wrap()` / `clip()` helpers, and shrink
  the font for long labels rather than letting them overflow.
- **Never truncate a URL.** A clipped link cannot be visited, which defeats the
  point of the map. URLs get the full box width (the price sits on the line
  above) and auto-shrink via `mono_w()` to fit; only if that would make them
  unreadable do they wrap. `clip()` is for prose only.

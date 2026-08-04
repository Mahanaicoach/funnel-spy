---
name: funnel-spy
description: >-
  Walk any competitor's sales funnel end to end — every page a stranger sees on
  the way to the checkout — and return a scored, sourced teardown: entry points
  (organic and ads, verified in ad libraries), the live page-by-page walk with
  screenshots, the software and tracking pixels running the machine, the full
  offer ladder with prices, and a four-gate Funnel Scorecard. Use whenever the
  user wants to spy on, tear down, reverse-engineer, map, or "funnel hack" a
  funnel, landing page, lead magnet, offer, or checkout — including when they
  paste Instagram/TikTok/X/LinkedIn handles, company names, or URLs and ask
  "what's their funnel", "how do they sell", "what's behind their link in bio",
  "are they running ads", "what tech / funnel builder do they use", or "tear
  down this landing page". Prefer this skill any time the user is studying how
  another creator or company converts attention into money, even if they never
  say the word "funnel".
---
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

# Funnel Spy

Competitor research tells you *what* someone sells. Funnel Spy shows you **how
the selling machine actually works** — by walking it the way a stranger would,
one page at a time, and writing down everything the machine does to convert
them.

For each target you deliver five things:

1. **The channel map** — every social platform they run, what each one is for,
   the exact link each points at, and the single place they all converge.
   Paid entry points are verified in the ad libraries, not guessed. This is the
   funnel *above* the website, and most teardowns miss it entirely.
2. **The Walk** — the actual page-by-page path from first click to checkout,
   captured live: every hop's headline, CTA, price, proof, and friction, with a
   screenshot as evidence.
3. **The Machine** — the funnel software, email platform, checkout processor,
   and tracking pixels detected from page source. The stack tells you the
   strategy: a Deadline Funnel script means evergreen scarcity; a ManyChat
   snippet means comment-to-DM; a Calendly embed means a sales-call close.
4. **The Offer Ladder** — every rung from free to high-ticket, with prices, and
   the order they're presented in.
5. **The Scorecard** — four gates (Attract / Capture / Convert / Ascend)
   scored against a fixed rubric, a 0–100 total, and the weakest gate named.
   Only what an outsider can verify by looking — email nurture is never
   scored, because it cannot be seen. The weakest gate is the finding: it's either their leak or your
   opening.

Then a cross-target synthesis: shared funnel patterns, a **Best-Engineered
ranking** driven by the scorecards, and — if the user gave an anchor — **Your
Opening** and **Steal This Week** (three concrete moves).

## Evidence rules

- **Evidence tiers on every claim:**
  - **CONFIRMED** — seen first-hand on an owned/authoritative page. A page you
    walked and screenshotted is CONFIRMED with proof attached — the strongest
    evidence this skill produces.
  - **REPORTED** — stated somewhere but self-reported or third-party-estimated,
    unaudited ("they claim $80K/mo"). Real signal, order-of-magnitude only.
  - **INFERRED** — your reasoned guess, labeled as such.
- **Never fabricate** a price, follower count, conversion rate, or funnel step.
  "Not found" is reported as not found, and absence of evidence ("no email
  capture found") is not confirmed absence — say which one you mean.
- The walk is a visitor's-eye capture. When a step needs a submission, an
  account, or a purchase to continue, capture that page, mark what's behind it
  unobservable, and recover it through sitemaps and archives instead of
  guessing (`references/funnel-walk.md` has the protocol).
- Short verbatim captures only. Swipe-file items are headlines, hooks, CTA
  labels, and guarantee lines — a line or two each — never wholesale page copy.

## Step 1 — Normalize the targets

The user may paste a mix: `@handle`, `instagram.com/...`, "GoHighLevel",
`acme.com`, or a direct funnel URL (a Linktree, a landing page, an ad's
destination). Sort each into:

- **Social handle** → find the person/brand, then their funnel entrance (the
  bio link is the front door).
- **Company / brand name** → find the site; the funnel entrance is usually the
  homepage hero CTA or the pricing page.
- **URL** → if it's a homepage, start there; if it's already a mid-funnel page
  (a Linktree, an opt-in, a sales page), start there *and* work backwards to
  find the entry points feeding it.

Infer which is which; strip leading `@`. Chase mistyped handles via search for
the corrected spelling or real name before giving up. If a target genuinely
can't be found, say so plainly — never invent a profile.

**No list?** If the user asks "who are my competitors?" instead of naming
targets, run a short discovery first: search their niche + offer type
("[niche] course", "[niche] coach site:skool.com", "[their keyword]
alternative"), skim who keeps appearing, and present 5–8 candidates with a
one-line reason each. Let the user pick before spending walk effort — spying
on the wrong five funnels thoroughly is worse than asking one question.

## Step 2 — One question up front: format, depth, anchor

Ask once, as a multiple-choice question (never free-form typing), then start:

1. **Output format** — the **Funnel Dossier PDF** (recommended default — the
   designed, shareable teardown), chat summary, spreadsheet matrix, or Word doc.
2. **Depth** — **Full Spy** (recon + live browser walk + ads check + tech
   detection; the real product), **Recon only** (search-based, no live
   walking — faster, for a quick read), or **Single-page teardown** (the user
   pasted one landing/sales page and wants it decoded now: skip recon and
   fan-out, walk that page and its immediate chain, run the copy teardown and
   tech detection on it, score the CONVERT gate only, and deliver — minutes,
   not a full run). If browser tools aren't available in this environment, say
   so and run the fetch-based walk instead (WebFetch/curl per page) so the
   chain, copy, prices, and tech stack are still captured first-hand — only
   the screenshots are lost.
3. **Anchor** — optionally: what does the *user* sell, at what price? This
   powers Your Opening and Steal This Week. Facts-only is fine too.

If the user already stated any of these, don't re-ask.

## Step 3 — Set up the run

- Create one task per target plus one synthesis task so progress is visible.
- Create a run folder for evidence: `funnel-spy-run-<date>/` with
  `screenshots/` and `portraits/` inside. Screenshots are named
  `<target>-<nn>-<role>.png` (e.g. `thedankoe-03-optin.png`); portraits are
  `portraits/<target>.jpg`.
- **Grab each target's portrait** per `references/target-portrait.md` — the
  face goes on the dossier cover and on that target's spread. Look at each
  downloaded image to confirm it's real and the right subject; use the
  initials fallback plate rather than any invented or stock image.
- Every run also writes one machine-readable `dossier.json` per target into
  the run folder (schema in `references/re-spy.md`) — it's the single source
  of truth the deliverables render from, and it's what makes future runs
  diffable.
- **Check for a previous run first.** If a `funnel-spy-run-*/` folder with
  dossiers for these targets already exists (or the user asks to re-check),
  this is a **re-spy**: run the same pipeline, then deliver the *diff* per
  `references/re-spy.md` — what changed is worth more than the snapshot.

## Step 4 — Fan out: recon agents (parallel)

One research agent per target, launched in parallel in a single turn, each
following `references/recon-prompt.md`. The recon agent's job is to come back
with the **funnel chain** — the ordered list of URLs a stranger would traverse —
plus offers and prices, entry points, a compact quantitative snapshot, and a
links directory. Recon finds the doors; the orchestrator walks through them.

If subagents aren't available, do the recon yourself per target, same standard.

**Enough is enough:** recon should confirm the funnel entrance, the core offer
and its price, and the capture mechanism. Don't burn searches chasing every
minor product — note what wasn't found and move on. The walk will fill gaps.

## Step 4c — Map the channel layer (the funnel above the website)

Before walking the site, map the **social layer** per
`references/channel-map.md`: every platform the target runs, its audience, its
job (primary engine / reach / authority / B2B / repurposed), and — the key
field — **the exact URL each one points at**. Then the convergence: the one or
two pages every channel feeds.

Hunt for **per-platform landing variants** (`/offer-yt`, `/offer-ig`, utm
variants). Probe the obvious siblings, always probe a nonsense control to prove
the site 404s on unknown paths, and diff the variants: identical content means
attribution tracking, different content means that channel gets bespoke effort.
Record cross-channel routing too — short-form feeding long-form, a site-wide
socials directory, or multiple principals each running a full stack into the
same funnel.

This lands in `channels`, `channel_destination`, `channel_read` and
`channel_cross` in the dossier, and renders as the report's first diagram. It
also tells you which entry point to walk first in Step 5.

## Step 5 — Walk each funnel (the core of this skill)

Follow `references/funnel-walk.md` exactly. In brief: start where a stranger
starts (bio link, ad landing URL, or homepage), follow the primary CTA at each
hop, and at every page capture the URL, its role, the headline and CTA
verbatim, prices, proof elements, urgency mechanics, form friction, and a
screenshot. The checkout is the last stop — capture it fully. Mine
`sitemap.xml`, `robots.txt`, and the Wayback Machine for the pages the funnel
hides (thank-you pages, upsells, old pricing).

On the money pages (primary opt-in, core sales page, checkout), run the
structured copy analysis in `references/copy-teardown.md` — awareness match,
hook type, offer presentation, risk reversal, urgency type, proof density,
CTA read. It's what justifies the CONVERT score, and its `Steal:` lines feed
the synthesis.

Walks run in the main loop (the browser is one shared surface), one target at
a time — recon fans out, walking doesn't.

## Step 6 — X-ray the machine

For each key page in the walk (entrance, opt-in, sales page, checkout), fetch
the raw page source and match it against `references/tech-stack.md` — funnel
builders, email platforms, checkout processors, schedulers, DM automation, and
every tracking pixel. Record what was found *and what it means strategically*
(the reference has the meaning table). Pixels are a big tell: a Meta pixel +
long-running ads = paid acquisition; GA4 alone + no pixels = organic-only.

## Step 7 — Ads intelligence

Follow `references/ads-intel.md`: check the Meta Ad Library, Google Ads
Transparency Center, and (where reachable) the TikTok library for each target.
Record: are they running ads at all, how many are active, how long the oldest
running ad has been live (an ad running 90+ days is a proven winner — say so),
and the ads' destination URLs. **Feed those destination URLs back into Step 5**
— an ad's landing page is a funnel entrance the bio link never shows you. If an
ad library is unreachable from this environment, report that honestly instead
of guessing.

## Step 8 — Offer ladder and funnel math

Assemble every offer found into a ladder: free → low-ticket → core →
high-ticket/continuity, each rung with its price and where in the walk it
appears. Missing rungs are findings ("no low-ticket bridge — they jump $0 →
$2,000").

Then, only where the inputs exist, sketch the **funnel math**: audience or
traffic × benchmark rates × price = an order-of-magnitude revenue band. Use
the ranges and the honesty rules in `references/benchmarks.md` — compute with
full ranges (never midpoints), name every benchmark used, tag the result
INFERRED (modelled), prefer any real observed number over a benchmark, and
skip the model entirely when more than two links in the chain are unknown.
Never decorate a guess with math.

## Step 9 — Score the four gates

Four gates, **0–25 each, totalling 0–100**. These are only the things an
outsider can actually verify by looking. Email nurture is deliberately **not**
scored: what a brand sends its subscribers cannot be observed from outside, and
a score you cannot evidence is a guess wearing a number. Note in the gaps that
it wasn't scored, and move on.

This is a rubric-scored qualitative read — always label it as such, never as a
measurement. Interpolate between the anchors.

- **ATTRACT** (getting found) — 0: no discoverable traffic engine. 12:
  consistent output on one platform, or active ads. 25: multi-platform
  consistency plus long-running ads and an owned audience feeding the top.
- **CAPTURE** (getting your details) — 0: content leads nowhere, no capture
  mechanism at all. 12: a lead magnet exists but is buried or high-friction.
  25: dedicated low-friction opt-in with a specific promise and proof, or
  comment-to-DM automation feeding it.
- **CONVERT** (making the sale) — 0: no offer page found. 12: offer page with a
  price but thin proof. 25: specific promise, stacked proof, a real guarantee
  or clear qualification, honest urgency, and a checkout whose friction matches
  the price.
- **ASCEND** (selling bigger) — 0: single-product dead end. 12: two rungs.
  25: full ladder free → low → core → high/continuity with visible cross-sells,
  order bumps, or a continuity offer.

The **weakest gate** gets named in every deliverable. Against a competitor it's
the user's opening; on the user's own funnel it's the leak to fix first. Record
a one-line justification per gate in `gate_notes` — that's what makes the score
defensible.

## Step 10 — Synthesize

Across targets:

- **Funnel patterns** — where the machines converge ("all three run short-form
  → comment-to-DM → Skool").
- **Divergence** — where they split, and who's alone in what.
- **Best-Engineered ranking** — ordered by scorecard total; break ties with
  momentum from the quantitative snapshot. This ranking is about the *machine*,
  not the brand's size.
- **Your Opening** (anchored runs) — the gap between the user's funnel/offer
  and the field, stated in one or two sentences.
- **Steal This Week** (anchored runs) — exactly three moves, each copyable in
  under a week, each traceable to something observed in a walk ("add an order
  bump at checkout — X does this at $27 and you have nothing between $0 and
  $497").
- **Gaps** — anything unverifiable, named honestly.

## Mirror mode — the user's own funnel

When one of the targets is the **user's own funnel** (they'll say so, or the
anchor domain appears in the target list), run the identical pipeline on it —
same walk, same copy teardown, same rubric; no softened scores. Two things
change in the output:

- The weakest gate is reported as **the leak**, and the dossier ends with a
  **Fix This Week** list instead of Steal This Week: three moves, ordered by
  gate impact, each pointing at a specific observed page ("your opt-in has 5
  fields; every walked competitor has 1").
- If competitors were walked in the same run, add a **gate-by-gate mirror
  table** (user vs. field) — that comparison writes the user's roadmap, and
  it's the single highest-value output this skill can produce.

Some of the user's own stages are invisible from outside (their email
sequence, their DM flows). Those aren't scored for anyone — say so plainly
rather than guessing at them.

## Re-spy — the diff over time

When a previous run's dossiers exist for a target (or the user asks "what
changed?"), deliver the **change report** from `references/re-spy.md` instead
of a fresh snapshot: price moves, new/removed funnel steps, stack additions,
ads turned on or off, gate drift — each delta with both ends evidenced, plus
the strategic read on what they're testing. A target with no previous run can
still get a one-off drift read via Wayback snapshots of the money pages.

## Step 11 — Deliver (never skip this — the artifact *is* the job)

**A run that ends with findings in the chat and no file is a failed run.**
Research is not the deliverable. Budget for this step; do not let it fall off
the end of a long walk.

The PDF is not hand-built. You write JSON, the bundled script draws it:

1. **Write the data.** One `dossier.json` per target in the run folder (schema
   in `references/re-spy.md`), plus `synthesis.json` for the cross-target read
   (`finding`, `opening`, `steal`/`fix`, `gaps`, `sources`). With several
   targets, name them `<target>.dossier.json`.
2. **Render.** One command, from anywhere:

   ```
   python3 scripts/render_dossier.py <run-folder>
   ```

3. **Look at it.** `pdftoppm -jpeg -r 70 <pdf> page`, then actually open the
   images and check: every portrait and screenshot loaded, no text collides, no
   stranded near-empty pages. Fix and re-render. Design bugs are invisible in
   code.
4. **Hand over the file**, with the run folder alongside it.

If WeasyPrint isn't installed the script says so and exits — install it
(`pip install weasyprint`) or switch to a text format; never silently deliver
nothing.

Other formats, all built from the same JSON:

- **Chat summary** — per `references/output-formats.md`. No gray walls: lead
  each target with its score, its weakest gate, and the two numbers that matter.
- **Spreadsheet matrix** — read the `xlsx` skill first. Best for 5+ targets.
- **Word doc** — read the `docx` skill first.

Every format carries evidence tiers, sources and the confidence note.
Screenshots, portraits and the JSON ship in the run folder beside the PDF.

## The quality bar

This skill's entire value is that it shows receipts. Hold the line on:

- Walked pages carry screenshots; claims carry tiers; numbers carry sources
  and dates.
- The scorecard is rubric-anchored, never vibes; the funnel math is
  range-bounded, never a point estimate.
- Gaps are named, not papered over.
- Short verbatim swipes only; summarize everything else.

A funnel teardown that fabricates a price is worse than useless. This one
holds the line, and that's why it's worth sharing.

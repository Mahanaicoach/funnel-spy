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
# The Funnel Walk — playbook

The walk is what separates Funnel Spy from ordinary competitor research: you
traverse the funnel the way a stranger would and capture evidence at every hop.
It runs in the main loop, one target at a time.

## Scope of the walk

The walk captures the funnel as a visitor sees it, page by page. When a step
requires a submission, an account, or a purchase to continue (an opt-in wall,
a checkout form), capture that page fully — it's a rich source on its own —
mark what sits behind it unobservable, and recover the hidden pages with the
mining tricks below rather than guessing.

**Checkout is the last stop.** Capture the price, order bump, payment plans,
guarantee, trust elements, and payment provider. Post-purchase upsells sit
behind the purchase itself; recover them via sitemap/Wayback (below), tag
anything found there by how it was found, and anything reasoned INFERRED.

## Tooling

Use whatever browser surface the environment provides (in-app browser pane,
Claude in Chrome, computer use). If none is available, fall back to fetching
each URL directly (WebFetch or `curl -L`) — you lose screenshots and
JS-rendered content but keep the chain, copy, prices, and page source. Say
which mode the walk ran in; screenshot-backed walks earn the "with proof"
label, fetch-based walks don't.

Screenshots go to the run folder as `<target>-<nn>-<role>.png`, numbered in
walk order.

## The chain is the observed path, not the site map

This is the rule that decides whether the whole report is right or wrong.

**A page belongs in the chain only if something actually routes traffic to
it.** For every step, record `from` — what sent you there (a named channel's
bio link, an ad, the previous page's primary CTA). If you cannot name what
routes a visitor to a page, it is not a step in the funnel.

The classic error is walking the *website* instead of the *funnel*: starting at
the homepage because that's where you'd start browsing, then following the
navigation menu. Real traffic almost never does this. Creator channels link
**deep** — straight to an opt-in or a landing variant — so the homepage is
usually not step 01, and often not in the funnel at all. Include it only if a
channel or an ad genuinely points at it.

Test each candidate step with one question: *what would put a stranger on this
page?* If the only answer is "clicking the menu", it is not a funnel step.

## Where to start

Start where a stranger starts, in priority order:

1. The **ad landing URL** if ads intel found active ads.
2. The **exact URL each social channel links to** (from the channel map) —
   this, not the homepage, is the front door for creator-led businesses.
3. The **homepage hero CTA** or pricing page — but only for companies whose
   traffic genuinely lands on the homepage (search, direct, brand ads).

If the user pasted a mid-funnel URL directly, start there, then work backwards
to find what feeds it.

## Expect parallel funnels, not one line

Most operations run **more than one funnel at once**, and forcing them into a
single chain misrepresents the business. The usual split:

- **Organic path** — social channels → capture page → free content → offer.
- **Paid path** — ads → a dedicated landing page → checkout, frequently
  skipping the free layer entirely.

Give each its own `branch` in the chain, with its own entry. *"Their ads bypass
the free funnel completely"* is a genuine finding, and it is invisible if you
flatten everything into one line.

## Offers that are not funnel steps

Products reachable only from the site menu — a book store, an application
page, a legacy offer — are **destinations, not steps**. Record them under
`other_doors` with a note on how they're reached, and keep them out of the
chain. Mixing them in invents a journey nobody takes, and it inflates the
ASCEND score with rungs no visitor is actually walked up.

## At every hop, capture

| Field | What to record |
|---|---|
| URL + timestamp | As loaded, after redirects — record it **in full**; a truncated URL is not a finding, it is a dead end |
| Role | entrance / hub / opt-in / sales / webinar / booking / community / checkout / thank-you |
| Headline + subhead | Verbatim, kept short (a line or two) |
| Primary CTA | Button text verbatim, and where it leads |
| Price(s) | Every visible price, tier, strike-through anchor |
| Proof | Count of testimonials, named logos, member/student counts, ratings |
| Urgency | Countdown timers, limited seats, closing dates — and whether they're real (see Deadline Funnel note in tech-stack.md) |
| Friction | Number of form fields, steps to buy, calendar length |
| Screenshot | One per page; a second only if something critical is below the fold |

Then follow the **primary CTA** — the path they push hardest is the funnel;
side links are not. Cap the walk at ~6 hops per branch and at most 2 branches
per target (e.g. the lead-magnet branch and the direct-offer branch). If a
funnel is longer than that, you're in a rabbit hole — summarize and stop.

Classify each hop honestly. A "free training" page that's a webinar
registration is an opt-in. A Skool "about" page is both sales page and
community door — say so.

On the **money pages** (primary opt-in, core sales page, checkout), also run
the structured copy analysis in `references/copy-teardown.md` — awareness
match, hook type, offer presentation, risk reversal, urgency type, proof
density, CTA read. Its `Steal:` lines feed the synthesis.

## Special pages

- **VSL pages** — don't sit through the video. Capture: video length if shown,
  whether the CTA is delay-revealed (check page source for a timer config —
  a classic), and any transcript. Search for the same VSL re-uploaded to
  YouTube; a transcript there is a legitimate capture.
- **Webinar funnels** — the registration page is an opt-in; classify it as
  one. Hunt the replay via sitemap and search ("[name] webinar replay"). If
  tech detection found EverWebinar/eWebinar, the "live" session is simulated —
  report it as an evergreen VSL with a calendar skin.
- **Quiz funnels** — enumerate the questions and visible branches by reading
  the page and its source; the questions themselves are ICP intelligence
  (they tell you exactly how the target segments buyers). If branch outcomes
  can't be read without completing the quiz, record the branch points and mark
  the outcomes unobservable.
- **Mobile spot-check** — most social traffic lands on phones. After the
  desktop walk, reload the two or three money pages at a mobile viewport
  (~390px) and note material differences: hidden sections, a different CTA, a
  sticky buy bar. A funnel that's broken on mobile while its traffic is 90%
  Instagram is a headline finding.
- **Non-English funnels** — capture verbatim in the original language with a
  translation in parentheses; don't translate away the swipe file.

## Mining the hidden structure

The funnel shows a stranger only what it wants to. Three read-only tricks
reveal the rest:

1. **`/sitemap.xml` and `/robots.txt`** — funnel builders list pages the
   navigation hides: thank-you pages, upsell/OTO pages, webinar replays, old
   offers. Fetch both for every funnel domain. Pages found here were not
   walked — capture them by direct fetch and note how they were found.
2. **Page source leaks** — redirect targets and follow-up URLs often sit in
   the JS of opt-in and checkout pages (form `action`s, `redirect_url`
   params). Read source, don't submit.
3. **The Wayback Machine** (`web.archive.org`) — two uses: reading pages that
   block direct access, and **funnel drift**: compare today's pricing/offer
   page against snapshots from 6–12 months ago. "They raised the core offer
   from $497 to $997 in March" is a finding nobody else in the report has.

## When a wall goes up

Login walls, region blocks, and bot checks happen. In order: try the direct
fetch of the same URL; try the Google cache/snippet; try Wayback. If all
three fail, the page is unobservable — record the wall (screenshot it),
state what's behind it as unknown, and never guess its contents.

## Output: the walk log

The walk produces one ordered log per target — the table that feeds every
deliverable:

```
| # | Role | URL | Headline (short) | CTA | Price | Proof | Friction | Evidence |
| 1 | entrance | ... | "..." | "Get the system" | — | 2.1M followers | — | 01-entrance.png |
| 2 | hub | ... | ... | ... | ... | ... | ... | 02-hub.png |
| 3 | opt-in | ... | ... | ... | free | 3 testimonials | 1 field | 03-optin.png |
...
```

Plus a one-line **chain summary** in arrowless prose for the dossier ("IG bio
to Stan hub, hub to free workshop opt-in, opt-in to $497 course checkout —
no low-ticket bridge found").

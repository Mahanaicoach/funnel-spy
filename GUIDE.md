# Funnel Spy — Full Guide

How the skill works under the hood, and how to squeeze the most value out of it.

---

## Part 1 — What it actually does

You hand it competitors. For **each one**, it walks the sales funnel the way a stranger would — first click to checkout — and returns:

- **Entry points** — where traffic enters, with ads verified in the ad libraries
- **The Walk** — the live page-by-page path, captured with screenshots
- **The Machine** — the software and pixels running it, and what that stack implies
- **The Offer Ladder** — every rung with prices, and the missing rungs
- **The Scorecard** — five gates, 0–100, weakest gate named

Then a **synthesis**: shared patterns, a Best-Engineered ranking, and (if you told it what you sell) Your Opening + Steal This Week.

The difference from ordinary competitor research: it doesn't summarize what people *say* about a funnel. It loads the pages and shows receipts.

---

## Part 2 — The pipeline, step by step

**1. Normalize.** Paste anything — `@handle`, "GoHighLevel", `acme.com`, or a raw landing-page URL. It sorts targets, chases mistyped handles, and if you gave it a mid-funnel URL it works backwards to find what feeds it.

**2. One question.** Format (Funnel Dossier PDF / chat / spreadsheet / Word), depth (**Full Spy** with the live walk, **Recon only** for speed, or a **single-page teardown** when you pasted one landing page and want it decoded in minutes), and your anchor (what you sell, at what price). Answer the anchor — it's what turns a report into a plan. No competitor list? Ask it "who are my competitors?" and it runs a discovery pass first, then lets you pick.

**3. Recon fans out.** One agent per competitor, in parallel, each mapping the funnel chain: the front door, the hub, the opt-in, the offers and prices, the numbers. Recon finds the doors.

**4. The Walk.** The orchestrator goes through them: loads each page, captures headline / CTA / price / proof / friction, screenshots it, follows the primary CTA, and stops at the checkout. It also mines `sitemap.xml`, `robots.txt`, and the Wayback Machine for what the funnel hides — thank-you pages, upsell pages, last year's pricing ("they raised the core offer from $497 to $997 in March" is a finding nobody's summary will give you).

**5. The copy teardown.** Every money page (opt-in, sales page, checkout) gets read like a copywriter reads it: which awareness level the page assumes vs. where the traffic actually comes from (the mismatch is one of the sharpest findings there is), the hook type, the offer stack and price anchoring, the guarantee, the urgency type — real event or evergreen automation — proof density, and the CTA. Each page ends with the one move worth stealing.

**6. The Machine.** Page source gets matched against real signatures: funnel builders (ClickFunnels, GoHighLevel, Kajabi, Skool…), email tools (Kit, Beehiiv, ManyChat…), checkouts (Stripe, SamCart, Whop…), schedulers, and every major ad pixel. Each hit comes with its meaning — Deadline Funnel means the countdown is evergreen automation, not an event; Calendly means the real close is a human on a call.

**7. Ads intel.** Meta Ad Library and Google Ads Transparency get checked directly: active count, formats, and **longevity** — an ad running 90+ days is a proven winner. The ads' destination URLs go back into the walk, because paid landing pages are the entrances the bio link never shows you.

**8. Scorecard.** Five gates, each 0–20 against fixed anchors:

| Gate | Question it answers |
|---|---|
| **ATTRACT** | Is there a real traffic engine — consistent content, ads, an owned audience? |
| **CAPTURE** | Does attention become a contact — lead magnet, low-friction opt-in, comment-to-DM? |
| **NURTURE** | Is there a middle — email sequence, community, DM follow-up? |
| **CONVERT** | Does the offer page close — promise, proof, guarantee, honest urgency? |
| **ASCEND** | Is there a ladder — bumps, upsells, continuity, high-ticket path? |

The weakest gate is the headline finding: on a competitor it's your opening, on your own funnel it's the leak.

**9. Deliver.** The flagship is the **Funnel Dossier PDF** — a case-file-styled report: the funnel drawn as a numbered rail, captured copy in monospace, evidence-tier stamps, gate bars, and a screenshot filmstrip. It renders the file and *looks at the pages* before handing it over. Alongside it, every run saves a machine-readable `dossier.json` per target — that's what powers the diff (Part 4).

---

## Part 3 — The evidence discipline (why you can trust it)

| Tier | Means |
|---|---|
| **CONFIRMED** | Seen first-hand on an owned page — walked pages carry a screenshot |
| **REPORTED** | Self-reported or third-party estimate, unaudited — order-of-magnitude only |
| **INFERRED** | A reasoned guess, labeled as one |

"Not found" is reported as not found. Absence of evidence is never silently upgraded to confirmed absence.

---

## Part 4 — The mirror and the diff

Two modes that compound the longer you use the skill:

**Mirror mode.** Put your own funnel in the target list. It gets the identical treatment — same walk, same copy teardown, same rubric, no softened scores — and the output flips: the weakest gate becomes **the leak**, Steal This Week becomes **Fix This Week**, and if competitors were walked in the same run you get a gate-by-gate you-vs-field table. That table is your roadmap.

**Re-spy.** Every run saves a `dossier.json` per target. Run the same targets a month later and instead of another snapshot you get the **change report**: price moves, new funnel steps, an order bump that appeared, ads switched on, stack additions, score drift — each delta evidenced on both ends, plus the read on what they're testing and what evidently worked. A competitor's diff is a free look at their experiment log. (No previous run? It can still pull 6–12-month-old Wayback snapshots of the money pages and read the drift.)

---

## Part 5 — Getting the most out of it

**Give it the anchor.** "I sell an AI automation course at $497" turns the synthesis from trivia into a plan: Your Opening and three Steal-This-Week moves, each tied to an observed page.

**Pick depth honestly.** Full Spy is the product — recon plus the live walk. Recon-only is for when you need a fast read on many targets and will walk the finalists later.

**Right number of targets.** 2–4 for Full Spy (each walk is real work). Recon-only handles more; use the spreadsheet format at 5+.

**Feed it mid-funnel URLs.** Saw an ad? Paste its landing URL directly — the skill walks forward from there and works backwards to the traffic source.

**Read the tiers.** A REPORTED "$80K/mo" claim is a self-reported number, not a fact. The tier is half the information.

**Follow-ups that pay off:**
- *"Walk [competitor]'s ad landing page too — compare it against their organic entrance."*
- *"Check the Wayback Machine — what did their pricing look like a year ago?"*
- *"Re-spy the same three next month and give me the diff."*
- *"Now mirror me: [your URL] — same rubric, where am I leaking?"*

That last one is the quiet superpower: the you-vs-field gate table writes your roadmap.

---

## Part 6 — What it will and won't promise

- Post-purchase upsells sit behind the purchase itself — they're reconstructed from sitemaps and archives, tagged accordingly, or reported as unobservable.
- Without browser tools it falls back to direct fetches: same chain, same prices, no screenshots — and it tells you which mode it ran in.
- Gated social numbers come back REPORTED, not fake-confirmed.
- Funnel math is always a range built on named benchmarks — never a point estimate — and it defers to any real observed number.

That honesty *is* the product. A teardown that fabricates a price is worse than useless.

---

*Built by [Mahan Ai](https://instagram.com/mahanaicoach). Follow for more Claude + automation builds.*

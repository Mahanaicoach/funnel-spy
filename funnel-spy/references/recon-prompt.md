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
# Recon-agent prompt template

One agent per target, launched in parallel in a single turn. Recon finds the
doors; the orchestrator walks through them afterwards. Fill in the bracketed
fields, and pass along anything already known (real name, niche, known URLs) so
the agent doesn't rediscover it.

---

```
Recon the sales funnel of the [creator / brand / business] "[TARGET]"
([known URL if any]). [One line of known context.] This is a competitor
being studied. Your job is to MAP the funnel, not walk it — return the doors,
the offers, and the numbers so the orchestrator can walk the path itself.

Use web search heavily. Look across their own website, Instagram, TikTok,
YouTube, X/Twitter, LinkedIn, link-in-bio hub (Linktree/Stan/Beacons),
newsletter, community (Skool/Circle/Whop), store, webinar registration, and
call-booking pages, plus podcast appearances. Try the handle, the likely real
name, and terms like "course", "community", "skool", "newsletter", "pricing",
"free", "template".

If the handle looks mistyped or returns nothing, search the corrected spelling
or real name before giving up. If the target genuinely can't be found, say so
plainly — do not invent a profile.

Return exactly these sections:

1. FUNNEL CHAIN — the ordered list of URLs a stranger would traverse, best
   guess, from first touch to checkout. For each: the URL and its role
   (entrance / hub / opt-in / sales page / webinar / booking / community /
   checkout). Flag which URL is the front door (usually the bio link). Only
   URLs you actually found — never guessed paths.

2. ENTRY POINTS — where strangers enter: primary platform and content type,
   posting cadence if visible, and any sign of paid ads. Report their exact
   **Facebook and Instagram handles** (e.g. @ahormozi / @hormozi) — the
   orchestrator needs them to scope the Meta Ad Library to this advertiser
   rather than keyword-matching a common name.

3. CHANNELS — every social platform they run (Instagram, YouTube, TikTok, X,
   LinkedIn, Facebook, Threads, podcast, newsletter). For each: follower count
   with source+date, and **the exact URL its bio/description/show-notes links
   to**. Check for a "socials"/"media" directory page on their own site — it is
   the fastest complete list. Flag any per-platform landing variants you spot
   (e.g. /offer-yt vs /offer-ig) and note whether more than one person
   (co-founder, partner) runs a full stack into the same funnel.

4. OFFERS — every product/offer found with price and tier: courses, cohorts,
   communities, coaching, services, SaaS plans, templates, affiliates,
   sponsorships. Note which is the core engine. Separate the AUDIENCE
   (followers) from the PAYING CUSTOMER if they differ — they usually do.

5. NUMBERS — 2 or 3 metrics that show size and momentum, each with source and
   date. Creators: follower counts per platform (open Social Blade directly:
   socialblade.com/[platform]/user/[handle]), engagement, newsletter subs if
   disclosed. Companies: funding (Crunchbase), headcount and open roles
   (LinkedIn), G2/Capterra review counts, self-reported ARR (tag REPORTED).
   Traffic only as a free order-of-magnitude range, tagged REPORTED.

6. LINKS — directory of their own properties as clickable URLs: site, socials,
   newsletter, podcast, hub, community, store. Only links that exist.

7. PORTRAIT — a direct image URL for the target's headshot (or, for a company
   with no single face, its logo mark). Check their own About/Team/Press page,
   the homepage og:image/twitter:image meta tags, a podcast feed's artwork, or
   a public avatar resolver. Return the URL(s) you found and where each came
   from; if none, say so.

8. SOURCES — the URLs your facts came from (overlaps with LINKS but isn't it).

Rules:
- Tag every claim CONFIRMED (seen on an owned/authoritative page), REPORTED
  (self-reported or third-party estimate, unaudited), or INFERRED (your guess).
- Never fabricate prices, offers, follower counts, or URLs.
- "Not found" is not "confirmed absent" — say which it is.
- If social profiles are gated, pull the same facts from owned pages
  (website, hub, Skool/Whop pages, newsletter about pages, podcast interviews),
  third-party analytics (Social Blade, HypeAuditor), and Google's cached
  snippets of the gated page. Gated is a detour, not a dead end.
- Do NOT submit forms, opt in, or create accounts anywhere. Recon is
  read-only.

Return a tight, scannable brief with a one-line confidence note. No raw
search dumps.
```

---

## Notes for the orchestrator

- Launch all recon agents at once; two waves only if you hit timeouts.
- When an agent reports a corrected handle or a disambiguation, carry it into
  the walk and the synthesis so the user sees it.
- The FUNNEL CHAIN is a hypothesis. The walk (Step 5) is the test — expect the
  real chain to differ, and record what the walk actually found.
- Merge ad destination URLs from Step 7 into the chain as additional entrances.

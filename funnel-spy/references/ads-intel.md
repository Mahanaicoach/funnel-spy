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
# Ads intelligence — verify paid entry points

Whether a competitor pays for traffic — and which pages they send it to — is
public information sitting in the platforms' own transparency libraries. Check
them; never infer "they run ads" from vibes.

## The libraries, in order of value

1. **Meta Ad Library** — `facebook.com/ads/library` → search the brand/creator
   name, filter to active ads, all countries. Usually reachable without login.
   Record:
   - **Active ad count** (0 is a finding too: "no active Meta ads").
   - **Longevity** — the start date of the oldest still-running ad. An ad
     running 90+ days is paying for itself; call it a proven winner.
   - **Formats and angles** — video vs static, the hooks in the first line.
   - **Destination URLs** — click nothing on the target's ads themselves;
     the library shows the landing URL. These are the funnel's paid entrances
     — feed them back into the walk list.
2. **Google Ads Transparency Center** — `adstransparency.google.com` → search
   by domain. Shows Google/YouTube ads and formats.
3. **TikTok** — `library.tiktok.com` covers EU-targeted ads; the Creative
   Center's top-ads section is browsable but partial. Report what's reachable.
4. **LinkedIn** — the company page's "Posts → Ads" tab, for B2B targets.

## Cross-check with the pixels

Ads intel and pixel detection (tech-stack.md) confirm each other:

- Meta pixel on the site + active ads in the library = paid acquisition,
  CONFIRMED from two directions.
- Meta pixel but **zero** active ads = retargeting-ready or paused — worth a
  Wayback check on whether they used to run more.
- Active ads but no pixel on the walked pages = the ads land on a page you
  haven't walked yet. Go find it.

## Always keep the library URL

Record the exact search URL you used for each library in the dossier
(`ads[].library_url`, and in `links`). It ships as a **clickable link in the
report** so the reader can open the ad library and scroll every ad themselves —
one of the most-clicked things in the whole dossier. Examples:

- Meta: `facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=<name>&search_type=keyword_exact_phrase`
- Google: `adstransparency.google.com/?region=anywhere&domain=<domain>`

## Honesty rules

- Every claim carries the library it came from and the date checked.
- Ad libraries region-block and rate-limit. If one is unreachable from this
  environment, write "not checkable from here" — never substitute a guess.
- Longevity is evidence of spend, not of profit. Say "long-running, likely
  winning" (INFERRED), not "profitable" (unknowable).

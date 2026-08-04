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

## Search by ADVERTISER, never by keyword

This is the difference between real ads intel and noise. A keyword search
matches the *text inside* ads, so searching "Alex Hormozi" returns inhaler
adverts, plagiarism checkers and book stores that happen to mention the words.
Scoping to the advertiser's own Page returns only their ads.

**The method — use the typeahead, it is the only reliable way to get the ID:**

1. Open `facebook.com/ads/library`, set the ad category to **All ads**.
2. Type the brand or person's name into "Search by keyword or advertiser".
3. The dropdown splits into *"Search this exact phrase"* (keyword — avoid) and
   **Advertisers** (what you want). Each advertiser row shows its verified
   Facebook and Instagram handles with follower counts — use those handles to
   pick the right one when several people share a name, and note the counts:
   they come from Meta itself, so they beat any third-party estimate.
4. Click the advertiser. The URL now carries `view_all_page_id=<PAGE_ID>`.
   **Save that ID** — it is the stable key for this advertiser.

The resulting URL is reusable and is what belongs in the dossier:

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all
  &country=ALL&media_type=all&search_type=page&view_all_page_id=<PAGE_ID>
```

Do not try to guess the Page ID from numbers scraped out of a Facebook page's
HTML — those are other entities and they return "No ads match", which reads
like "no ads" when it actually means "wrong ID". Verify by confirming the
advertiser's name and a plausible result count appear on the scoped page.

If the typeahead is unreachable (bot challenge, region block), fall back to a
keyword search but **label it as keyword-scoped and treat the count as an upper
bound polluted by unrelated advertisers** — never report it as their ad count.

## The libraries, in order of value

1. **Meta Ad Library** — advertiser-scoped as above, filtered to active ads,
   all countries. Usually reachable without login. Record:
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

- Meta: `facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&media_type=all&search_type=page&view_all_page_id=<PAGE_ID>`
  (advertiser-scoped — store `meta_page_id` in the dossier too, so a re-spy reuses it)
- Google: `adstransparency.google.com/?region=anywhere&domain=<domain>`

## Honesty rules

- Every claim carries the library it came from and the date checked.
- Ad libraries region-block and rate-limit. If one is unreachable from this
  environment, write "not checkable from here" — never substitute a guess.
- Longevity is evidence of spend, not of profit. Say "long-running, likely
  winning" (INFERRED), not "profitable" (unknowable).

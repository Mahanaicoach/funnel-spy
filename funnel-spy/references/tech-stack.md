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
# The Machine — tech-stack and pixel detection

Fetch the raw HTML of each key page (entrance, opt-in, sales page, checkout)
and search it for the signatures below. Use the browser's page source, WebFetch,
or `curl -sL <url>`. Everything here is read-only detection from public page
source — nothing is probed or exploited.

Report two things per target: **what was found** (the stack) and **what it
means** (the strategy it implies). A stack list without the meaning column is
trivia; the meaning column is the intelligence. Versions and exact products
drift — if a signature doesn't match but the page clearly runs something
equivalent, say what you see and tag it INFERRED.

## Funnel builders and site platforms

| Platform | Signatures in page source | What it implies |
|---|---|---|
| ClickFunnels | `clickfunnels.com` assets, `cfcdn.com`, `data-cf-` attrs | Classic direct-response funnel DNA; expect OTOs and order bumps |
| GoHighLevel | `leadconnectorhq.com`, `msgsndr.com` scripts/forms | Agency-style stack: funnels + SMS/email + booking in one; often a call funnel |
| Kajabi | `mykajabi.com`, `kajabi-cdn.com` assets | Course/membership engine; content business with checkout built in |
| Kartra | `kartra.com` assets, `kartra_` vars | All-in-one direct response, similar read to ClickFunnels |
| Systeme.io | `systeme.io` assets | Budget all-in-one; lean operation |
| Podia / Teachable / Thinkific | respective domains in assets/links | Course platform; simpler funnel, usually no aggressive OTO chain |
| Skool | `skool.com` community links | Community-led growth; the "about" page is the sales page |
| Whop / Circle | `whop.com` checkout, `circle.so` | Paid community/membership engine |
| Stan / Beacons / Linktree | `stan.store`, `beacons.ai`, `linktr.ee` | Creator storefront; the hub *is* the funnel map |
| Framer / Webflow / Squarespace / WordPress | generator meta tags, `wp-content` | General site builder — funnel likely assembled from parts, look for the email/checkout tools below |

## Email and nurture

| Tool | Signatures | What it implies |
|---|---|---|
| Kit (ConvertKit) | `convertkit.com`, `ck.page`, `kit.com` forms | Creator email stack |
| Beehiiv | `beehiiv.com` embeds/links | Newsletter-first growth, possibly paid recommendations |
| Substack | `substack.com` | Newsletter as product or top-of-funnel |
| Mailchimp / Klaviyo / ActiveCampaign | respective script domains | Standard ESP; Klaviyo suggests e-commerce DNA |
| ManyChat | `manychat.com` widget/snippet | **Comment-to-DM automation** — their real capture may be in DMs, not on the page |

## Checkout and payments

| Tool | Signatures | What it implies |
|---|---|---|
| Stripe | `js.stripe.com` | Direct card checkout; self-managed |
| SamCart / ThriveCart | `samcart.com`, `thrivecart.com` | Dedicated cart with bumps/upsell chains — expect an OTO |
| Gumroad / Lemon Squeezy / Paddle | respective domains | Digital product checkout; Paddle suggests SaaS |
| Whop | `whop.com/checkout` | Community/membership billing |

## Calls, webinars, applications

| Tool | Signatures | What it implies |
|---|---|---|
| Calendly / Cal.com | embed scripts | **Sales-call close** — high-ticket, human-closed |
| WebinarJam / EverWebinar | `webinarjam.com`, `everwebinar` | Webinar funnel; EverWebinar = evergreen ("live" replays) |
| Demio / eWebinar | respective domains | Same read, newer stack |
| Typeform / Tally / Jotform | embed scripts on an "apply" page | **Application funnel** — they filter buyers; high-ticket |

## Urgency and proof widgets

| Tool | Signatures | What it implies |
|---|---|---|
| Deadline Funnel | `deadlinefunnel.com` scripts | **Evergreen scarcity** — every visitor gets a personal "deadline". The countdown is a mechanism, not an event. Report it plainly. |
| ProveSource / Fomo / TrustPulse | respective script domains | Social-proof popups ("X just bought") — manufactured proof signals |

## Tracking pixels — who's paying for traffic

| Pixel | Signatures | What it implies |
|---|---|---|
| Meta Pixel | `connect.facebook.net`, `fbq(` | Running or preparing Meta ads/retargeting — cross-check the Ad Library |
| TikTok Pixel | `analytics.tiktok.com`, `ttq.` | TikTok ads |
| Google Ads | `AW-` conversion id, `googleadservices` | Google/YouTube ads |
| GA4 only | `gtag/js?id=G-` with no ad pixels | Measuring but likely **organic-only** acquisition |
| LinkedIn Insight | `snap.licdn.com` | B2B ads/retargeting |
| X / Pinterest / Snap | `static.ads-twitter.com`, `pintrk`, `sc-static.net` | Respective ad channels |
| Hotjar / Clarity | `hotjar.com`, `clarity.ms` | They're actively optimizing pages — a funnel someone is working on |

## Reading the stack as strategy

Combine signals into one or two sentences of meaning per target. Examples of
the register to hit:

- Meta pixel + ClickFunnels + Deadline Funnel + SamCart = "a paid-traffic
  direct-response machine with evergreen scarcity and an upsell chain."
- Skool + ManyChat + no ad pixels = "organic short-form into comment-to-DM
  into community — the funnel lives in the DMs, not on a landing page."
- Calendly + Typeform application + LinkedIn Insight = "high-ticket,
  human-closed B2B motion; the page's only job is booking the call."

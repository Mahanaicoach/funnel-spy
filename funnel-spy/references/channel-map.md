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
# The channel map — the funnel above the website

Nobody arrives at a sales page from nowhere. Before the first landing page
there is a **social layer**: several platforms, each with a job, each pointing
somewhere specific, usually converging on one or two entry points. A report
that begins at the homepage has skipped the entire top of the funnel.

Map this **before** the site walk — it tells you which door to walk through
first, and it is often where the sharpest finding of the whole run lives.

## What to establish for every channel

For each platform the target runs (Instagram, YouTube, TikTok, X, LinkedIn,
Facebook, Threads, podcast, newsletter):

| Field | What you're after |
|---|---|
| `platform` | The channel |
| `audience` | Follower/subscriber count, with a source and date (usually REPORTED) |
| `role` | What this channel is *for*: primary engine · reach/short-form · authority/long-form · B2B · repurposed |
| `links_to` | **The exact URL it points at.** The single most valuable field here |
| `note` | Anything notable about that link — tracked variant, different content, link-in-bio hub |
| `primary` | `true` for the one or two channels doing the real work |

Then the convergence: `channel_destination` — the one page they all feed.

## Finding the exit link (in order)

1. **The target's own "socials" or "media" page.** Many brands publish a
   directory of every channel; it is the fastest complete list, and it reveals
   the site feeding the socials as much as the reverse.
2. **The bio link** on each profile — the link-in-bio hub or a direct URL.
   Where profiles are gated, the platform's public channel/about page and
   Google's cached snippet usually still expose it.
3. **YouTube channel links** and video descriptions — almost always public, and
   frequently the most explicit routing on the whole operation.
4. **Podcast show notes / RSS feed** — public by definition, and the links are
   listed in plain text.

## Hunt for per-platform landing variants — the big tell

Sophisticated operators give **each channel its own URL for the same offer** so
they can attribute which platform produced the lead: `/offer-yt`, `/offer-ig`,
`/offer-tt`, or `?utm_source=` variants of one page.

When you find one variant, probe the obvious siblings (`-yt -ig -tt -x -li -fb
-p`), and **always probe a nonsense control** (`-zzzq`) to prove the site 404s
on unknown paths rather than returning 200 for everything. Then compare the
real variants byte-for-byte:

```bash
curl -sL "$SITE/offer-ig" | md5     # identical checksum to /offer
curl -sL "$SITE/offer-yt" | md5     # different → bespoke page for that channel
```

- **Identical content, different URL** = attribution tracking only.
- **Different content** = they invest real production effort in that channel;
  it is one of their most valuable, and worth walking separately.

Both readings are findings. State which one each variant is, and never assert a
variant exists without a 200 plus a passing control.

## Cross-channel routing

Channels also feed *each other*. Record these in `channel_cross`:

- Short-form driving long-form ("clips point at the full YouTube episode").
- The site publishing a directory back out to every channel.
- **Multiple principals** — co-founders or partners each running a full stack
  into the same funnel. Easy to miss and it multiplies their reach.
- A podcast or newsletter used as the authority layer while short-form does
  reach.

## The read

Finish with one paragraph in `channel_read` answering: how many jobs do these
channels have? Almost always the answer is *one* — every channel exists to hand
the visitor to a single capture page. When that is true, say it plainly; it is
the most copyable lesson in the report. When it *isn't* true (channels pointing
at five different offers), that fragmentation is itself the finding.

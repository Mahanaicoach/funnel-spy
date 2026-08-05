# The copy-paste prompt

Spy on any creator's funnel in one message.

---

## Use it right now (nothing to install)

Open **Claude Code** in any empty folder and paste this. Swap the two lines in
capitals for your own.

```
Clone https://github.com/Mahanaicoach/funnel-spy and read the SKILL.md inside
it, then follow that skill exactly.

TARGET: @hormozi
I SELL: an Ai automation course at $497

Walk their whole funnel properly — map every platform and the exact link each
one points at, walk the live pages to the checkout, detect their stack and
pixels, check the ad libraries, and score it. Then build the Funnel Dossier PDF
and tell me where my opening is.
```

That's it. It clones the skill, follows it, and hands you a designed PDF.

> **Why "read the SKILL.md" and not just install it?** A freshly installed
> skill isn't picked up until Claude restarts. Pointing Claude straight at the
> file makes it work in the same message — which is what you want for a demo.

---

## The complete version

When you want every step spelled out — nothing left to chance, which is what
you want when you're recording:

```
Clone https://github.com/Mahanaicoach/funnel-spy into this folder and read
funnel-spy/funnel-spy/SKILL.md — then follow that skill exactly, start to finish.

TARGET:  @hormozi
I SELL:  an Ai automation course at $497
OUTPUT:  the Funnel Dossier PDF, Full Spy depth

Run the whole pipeline:

1. CHANNEL MAP — find every platform they run (Instagram, YouTube, TikTok, X,
   LinkedIn, Facebook, podcast, newsletter). For each: follower count with a
   source, what that channel is for, and the exact URL its bio / description /
   show notes points at. Look for a "socials" or "media" directory on their own
   site. Hunt for per-platform landing variants (/offer-yt vs /offer-ig), probe
   a nonsense control to prove the site really 404s, and diff the variants —
   identical content means attribution tracking, different content means that
   channel gets bespoke effort. Then find the one page they all converge on.

2. THE WALK — start where traffic actually lands, NOT the homepage. Follow the
   primary CTA page by page to the checkout, screenshotting every page. Capture
   the headline, CTA, price, proof and friction verbatim. Only include a page if
   you can name what routes traffic to it — offers reachable solely from the
   site menu are destinations, not funnel steps. Expect separate organic and
   paid funnels; give each its own branch rather than one straight line. Mine
   sitemap.xml, robots.txt and the Wayback Machine for pages the funnel hides.

3. THE MACHINE — fetch the page source of the money pages and detect the funnel
   builder, email platform, checkout, scheduler, DM automation and every
   tracking pixel. Say what the stack implies strategically, not just what it is.

4. ADS — check the Meta Ad Library scoped to their ADVERTISER PAGE: use the
   library typeahead to get view_all_page_id, never a keyword search (keywords
   match ad text and return unrelated advertisers). Also check the Google Ads
   Transparency Center. Record the active ad count, how long the oldest running
   ad has been live, and the landing URLs — then walk those landing pages too.
   Keep both library URLs; they ship as clickable links in the report.

5. COPY TEARDOWN on each money page — the awareness level it assumes versus
   where the traffic actually comes from, the hook type, offer stack and price
   anchoring, guarantee, urgency (a real event or evergreen automation), proof
   density, and the CTA.

6. SCORE the four gates — Attract, Capture, Convert, Ascend, 25 points each —
   and name the weakest one. Do not score email nurture; it cannot be observed
   from outside.

7. DELIVER — write dossier.json and synthesis.json into the run folder, run
   scripts/render_dossier.py on it, then render the PDF pages to images and
   actually look at them before handing anything over. Give me the PDF plus:
   where my opening is, and three moves I can steal this week.

Tag every claim CONFIRMED, REPORTED or INFERRED. Never invent a price, follower
count or URL — report "not found" instead.
```

---

## The short version

If you already told it what you sell, this is enough:

```
Clone https://github.com/Mahanaicoach/funnel-spy, read the SKILL.md inside,
and spy on @hormozi's funnel. Give me the PDF.
```

---

## Install it permanently (Claude Code)

Worth doing if you'll use it more than once — then you never need the clone
line again.

```bash
git clone https://github.com/Mahanaicoach/funnel-spy.git
cp -r funnel-spy/funnel-spy ~/.claude/skills/
```

Restart Claude Code, then just say:

```
spy on @hormozi's funnel — I sell an Ai automation course at $497
```

You don't have to name the skill. Claude picks it up from the words.

---

## Install it in the Claude desktop app

1. Download [`funnel-spy.skill`](funnel-spy.skill) from this repo.
2. Drag it into a Claude chat and click **Save skill**.
3. Say `spy on @hormozi's funnel`.

---

## Prompts worth stealing

Once it's installed, these all work:

| What you want | What to say |
|---|---|
| A full teardown | `spy on @creator's funnel — I sell [X] at [price]` |
| Compare rivals | `spy on @one and @two — who's better built, and where's my opening?` |
| One landing page, fast | `walk this page and tell me why it converts: [URL]` |
| Check your own funnel | `spy on my own funnel: [your URL] — where am I leaking?` |
| See what changed | `re-spy @creator and give me the diff` |
| Find who to study | `who are my competitors in [niche]?` |

---

## What comes back

A PDF where you can see, without reading a paragraph:

- **The channel map** — every platform they run and the exact link each points at
- **The whole funnel, top to bottom** — every page a stranger is actually sent
  to, with prices, drawn as one flow
- **The staircase** — what they sell, cheapest to dearest, and the rung they skipped
- **The scorecard** — four gates out of 100, with their weakest one named
- **Their best lines**, word for word, plus a clickable link into their ad library
- **Steal this week** — three moves you can copy in days

---

*Built by [Mahan Ai](https://instagram.com/mahanaicoach). Follow for more Claude builds.*

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

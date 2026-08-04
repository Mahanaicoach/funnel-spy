# Installing Funnel Spy

Two ways to install, depending on how you use Claude. Pick the one that matches you.

---

## Option A — Claude desktop app ✅ easiest

1. On this repo's main page, click the file **`funnel-spy.skill`**.
2. On the file page, click the **Download** button to save it to your computer.
3. Open the **Claude desktop app**.
4. Drag the `funnel-spy.skill` file into a chat (or open it), then click **Save skill**.
5. Done. Start a chat and paste your competitors — Claude loads the skill automatically.

> The `.skill` file is just a zipped bundle of everything in the `funnel-spy/` folder. You don't need to unzip anything yourself.

---

## Option B — Claude Code (CLI / terminal)

```bash
# 1. Clone this repo
git clone https://github.com/Mahanaicoach/funnel-spy.git

# 2. Copy the skill folder into your Claude Code skills directory
cp -r funnel-spy/funnel-spy ~/.claude/skills/
```

Claude Code discovers skills in `~/.claude/skills/` on the next run.

> Your skills directory may differ. Common locations:
> - User-level: `~/.claude/skills/`
> - Project-level: `.claude/skills/` inside a specific project
>
> Copy the inner `funnel-spy/` folder (the one containing `SKILL.md`) — not the repo root.

---

## Optional: enable the Funnel Dossier PDF

The flagship output (the designed, case-file-styled teardown) renders with **WeasyPrint**. Everything else — chat, spreadsheet, Word doc — works without it.

```bash
pip install weasyprint
```

On some systems you may need:

```bash
pip install weasyprint --break-system-packages
```

If WeasyPrint won't install, the skill falls back to ReportLab and produces the same report structure.

---

## Optional: the `/funnel-spy` slash command (Claude Code)

The skill triggers automatically from plain language. If you want a one-liner shortcut in **Claude Code**:

```bash
# from inside the cloned repo
cp commands/funnel-spy.md ~/.claude/commands/funnel-spy.md
```

Then:

```
/funnel-spy @sabrina_ramonov @thedankoe gohighlevel.com
```

---

## Verify it's working

Open a chat and paste:

```
spy on this funnel for me: @thedankoe
```

If the skill is installed, Claude will ask one setup question (output format, depth, and what you sell) and then start recon. If it doesn't, re-check the install step above.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude doesn't trigger the skill | Re-check the install step. Or be explicit: *"use the funnel-spy skill on …"* |
| No screenshots in the output | The environment had no browser surface, so the walk ran fetch-based — the chain and prices are still first-hand. Enable computer use / the browser for screenshot-backed walks |
| PDF output fails | Install WeasyPrint, or ask for the **chat** or **spreadsheet** format instead |
| A page "can't be reached" | The skill tries direct fetch, Google's cache, and the Wayback Machine, then reports the wall honestly rather than guessing what's behind it |
| Numbers look like estimates | Intentional — gated metrics get **REPORTED** tags, never fake-confirmed numbers |

---

Questions or want more builds like this? → [@mahanaicoach](https://instagram.com/mahanaicoach)

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
# Re-spy — track a funnel over time

A funnel teardown is a snapshot. The compounding value is the **diff**: what a
competitor changed since last time is a direct readout of what they're testing,
what worked, and where they're headed. Re-spy makes every run diffable.

## dossier.json — every run's machine-readable state

Alongside the human deliverable, every run writes one `dossier.json` per
target into the run folder. It is the single source of truth the PDF, sheet,
and future diffs are generated from:

```json
{
  "target": "thedankoe",
  "run_date": "2026-08-04",
  "walk_mode": "browser|fetch",
  "portrait": {"path": "portraits/thedankoe.jpg", "source": "thedankoe.com/about"},
  "chain": [
    {"n": 1, "role": "hub", "url": "…", "headline": "…", "cta": "…",
     "price": null, "evidence": "thedankoe-01-hub.png"}
  ],
  "offers": [
    {"name": "…", "price": "$497", "rung": "core", "tier": "CONFIRMED",
     "url": "…"}
  ],
  "stack": ["Kajabi", "Kit"],
  "pixels": ["meta", "ga4"],
  "ads": {"library": "meta", "checked": "2026-08-04", "active": 0,
          "oldest_running_since": null},
  "gates": {"attract": 18, "capture": 12, "nurture": 10, "convert": 15,
            "ascend": 8},
  "numbers": [
    {"value": "2.1M", "label": "IG followers", "source": "…",
     "date": "2026-08-04", "tier": "CONFIRMED"}
  ],
  "links": {"site": "…", "instagram": "…"}
}
```

Only fields the run actually established — never pad with nulls invented to
fill the schema.

## Running a re-spy

Trigger: the user asks to re-check a target, or a previous
`funnel-spy-run-*/` folder with a matching `dossier.json` exists where the
skill is running. Then:

1. Load the old dossier(s); note the age ("last walked 34 days ago").
2. Run the normal pipeline on the same targets — same walk, same rubric.
3. Diff old → new, and report **only the deltas plus a no-change line**:

```
## Re-spy — [target] · [old date] → [new date]

CHANGED
- Core offer price: $497 → $997 (checkout page, screenshot 04)
- New funnel step: order bump "$27 templates" at checkout (wasn't there)
- Ads: 0 → 7 active on Meta, oldest since [date] — they turned paid on
- Stack: + Deadline Funnel (evergreen scarcity added)
- Gate shift: CONVERT 15 → 17, ASCEND 8 → 12 · total 63 → 71

UNCHANGED
- Chain shape, capture mechanism, community pricing

READ
[2–3 sentences: what the changes say about strategy — what they're testing,
what evidently worked, what it means for the user's anchor.]
```

4. Every delta carries evidence (old value's source + new value's source).
   A price change claimed without both ends shown is not a delta, it's a
   guess.
5. Write the new `dossier.json` next to the old one — runs accumulate into a
   timeline.

## Notes

- The Wayback Machine can backfill a "first run" for a target never spied
  before: pull 6–12-month-old snapshots of the money pages and diff against
  today, tagged appropriately (archive snapshots are CONFIRMED-as-of-their-
  date).
- Score drift matters more than any single delta — a competitor whose CONVERT
  and ASCEND gates both climbed is systematically optimizing; say so in the
  Best-Engineered ranking of the new run.
- Suggested cadence when the user asks: monthly for active competitors,
  quarterly otherwise.

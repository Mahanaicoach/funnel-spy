---
description: Run Funnel Spy on a list of competitors (handles, company names, or URLs)
argument-hint: "@handle1 @handle2 company.com  (or leave blank to be asked)"
---

Use the **funnel-spy** skill to spy on the following competitors' funnels: $ARGUMENTS

Follow the skill exactly:
- Normalize each target (social handle / company / URL — infer which; a mid-funnel URL means walk forward from it and work backwards to its traffic source).
- Ask me one setup question — output format (Funnel Dossier PDF / chat / spreadsheet / Word), depth (Full Spy vs Recon only), and what I sell as the anchor — unless I already said.
- Fan out recon agents in parallel, then walk each funnel page by page to the checkout with screenshots, running the copy teardown on every money page.
- Detect the tech stack and pixels from page source, check the ad libraries, build the offer ladder with range-bounded funnel math, and score the five gates.
- Deliver per-target dossiers plus the synthesis (Best-Engineered ranking, my opening, steal-this-week) in my chosen format, and save a dossier.json per target so a future run can deliver the diff.
- If a previous run's dossiers exist for these targets, deliver the re-spy change report instead of a fresh snapshot. If one of the targets is my own funnel, run mirror mode (same rubric, Fix This Week, me-vs-field table).

If no targets were provided above, ask me for the list before doing anything else.

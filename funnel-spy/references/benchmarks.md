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
# Benchmark ranges — for honest funnel math

The funnel-math model (SKILL.md Step 8) needs conversion-rate assumptions.
Use these ranges so every run assumes the same things — and so the model's
honesty rules are enforceable.

**What these are:** industry folklore ranges, not audited data. They exist to
bound an order-of-magnitude model, nothing more.

## The rules

1. Always compute with the **full range**, never a midpoint — the output is a
   band ("$15K–$80K/mo"), not a number.
2. Name every benchmark used, in the output, next to the formula.
3. The result is always tagged **INFERRED (modelled)**.
4. If more than two links in the chain are unknown, don't model — say why.
5. When a real observed number exists (a disclosed member count, a review
   count, a claimed revenue tagged REPORTED), prefer it over any benchmark and
   sanity-check the model against it.

## The ranges

| Step | Typical range |
|---|---|
| Dedicated opt-in page, social traffic | 10–40% |
| Opt-in embedded on a busy page | 2–10% |
| Webinar registration → live show-up | 20–40% |
| Evergreen webinar registration → watch | 10–25% |
| Sales page, cold traffic | 0.5–2% |
| Sales page, warm (email/community) traffic | 2–8% |
| Order bump take rate | 10–40% |
| Post-purchase upsell (OTO) take rate | 5–15% |
| Email open rate | 25–45% |
| Email click-through rate | 1–5% |
| Application → booked call | 30–60% |
| Booked call → show | 60–80% |
| Sales call → close (high-ticket) | 15–35% |
| SaaS trial → paid (no card up front) | 5–25% |
| SaaS trial → paid (card required) | 40–60% |
| Free community → paid conversion | 1–5% |

## Worked shape

```
Funnel math (INFERRED, modelled):
  120K monthly IG reach (REPORTED, Social Blade)
  × 1–3% hub click-through        [assumed]
  × 10–40% opt-in                 [benchmark: dedicated opt-in]
  × 2–8% warm sales conversion    [benchmark: warm sales page]
  × $497                          [CONFIRMED, checkout page]
  ≈ $1.2K–$47K/mo from this funnel alone — a wide band by design;
  the disclosed 4,100-member Skool at $49/mo (CONFIRMED) already implies
  ~$200K/mo from community, so the course funnel is not the engine.
```

That last move — checking the model against a confirmed number and letting the
confirmed number win — is the difference between analysis and theater.

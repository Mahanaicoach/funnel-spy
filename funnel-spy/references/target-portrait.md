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
# Target portraits — the face on the case file

Every dossier carries the target's photo: on the **cover** (a row of portrait
plates, one per target) and again on each target's **dossier spread**. A case
file with faces reads like a real dossier; one without reads like a
spreadsheet. This is a required part of the PDF, not an optional flourish.

For company targets with no single face, use the **logo mark** instead
(favicon/apple-touch-icon or the og:image from the homepage) and say so in the
caption. Never substitute a stock photo or a generated face for a real person —
if nothing is found, use the fallback plate (below), never an invented image.

## Getting the image

Work down this chain, stopping at the first hit, and record which source
supplied it (it goes in the caption):

1. **Their own site** — the About/Team/Press page headshot. Highest quality
   and unambiguously the right person. Also check the homepage `og:image` and
   `twitter:image` meta tags:
   `curl -sL <site> | grep -iEo '<meta[^>]+(og:image|twitter:image)[^>]*>'`
2. **A public press/media kit page** — often offers a high-res headshot
   explicitly for third-party use.
3. **Public platform avatars** — the profile image URL exposed in the page's
   meta tags (X/Twitter, YouTube channel, LinkedIn public page, podcast RSS
   `itunes:image`, Substack/beehiiv author image). A podcast feed's artwork is
   frequently the easiest high-res grab.
4. **Avatar resolvers** — e.g. `unavatar.io/instagram/<handle>`,
   `unavatar.io/x/<handle>`, `unavatar.io/<email-or-domain>`. Convenient, but
   they can return the wrong person for a common handle — **look at the image
   you downloaded** before putting it in the report.
5. **Company logo** (company targets) — `/favicon.ico`,
   `/apple-touch-icon.png`, or the homepage `og:image`.

Save into the run folder as `portraits/<target>.jpg|png` and reference it by
relative path so WeasyPrint resolves it via `base_url`.

```bash
curl -sL -o "funnel-spy-run-<date>/portraits/<target>.jpg" "<image-url>"
```

Verify each download: check it's a real image (`file <path>`), that it isn't a
1×1 tracking pixel or an HTML error page saved with an image extension, and —
by looking at it — that it's plausibly the right subject. A wrong face in a
competitive dossier is a credibility-destroying error, worse than no face.

## Rendering

- **Cover:** a row of portrait plates under the title — square or 4:5 crop,
  `object-fit: cover`, hairline border in the dossier palette, desaturated
  (`filter: grayscale(1) contrast(1.08)`) so the cover stays two-tone and the
  faces read as case-file photography rather than marketing headshots. Under
  each plate, the handle in mono.
- **Dossier spread:** the same portrait at ~22mm square, top-left of the
  header block, with the name, one-liner, and score badge beside it.
  Grayscale here too, for consistency with the cover.
- **Caption/credit:** small mono line under or beside the spread portrait
  naming the source (`portrait: acquisition.com/about`). Sourcing the image
  the way facts are sourced is on-brand and honest.
- **Fallback plate:** if no image was found, render a plate of the same size
  in `#EFECE0` with the target's initials in mono and the caption
  `no portrait found` — never a stock face, never a generated one.

## Handling and rights

- Fetch only images the target publishes publicly; use them at report scale
  for identification inside the analysis, credited to source.
- Portraits live in the run folder with the rest of the evidence. If the user
  plans to publish the dossier externally rather than use it internally, say
  once that headshots are the target's own image and a press-page or
  official-avatar source is the safest one to keep in a public document.

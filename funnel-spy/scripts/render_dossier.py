#!/usr/bin/env python3
"""
Funnel Spy — Funnel Dossier renderer.

Reads the dossier.json file(s) a run produced and draws the report.
No report content lives in this file; it is a pure renderer.

    python3 render_dossier.py <run-folder> [-o OUT.pdf] [--title "..."]

Looks for <run-folder>/dossier.json (single target) or
<run-folder>/*.dossier.json (multi-target), plus an optional
<run-folder>/synthesis.json. Image paths in the JSON resolve relative to the
run folder.

Design rule: SHOW, don't tell. The funnel is drawn as a map, the offers as a
staircase, the score as bars. Text is captions, never walls. Every field is
optional — a section is skipped when its data is absent.

Requires WeasyPrint (`pip install weasyprint`).
"""
import argparse
import base64
import json
import pathlib
import re
import sys

INK = "#131912"
PAPER = "#F7F5EF"
GREEN = "#1F6E52"
AMBER = "#B07818"
GREY = "#8A8676"
LINE = "#C9C4B4"

TIER = {"CONFIRMED": "#1F8A57", "REPORTED": "#B07818", "INFERRED": "#6B7280"}

# Four gates, 25 points each. Only what a visitor can actually observe from
# outside — email nurture is deliberately not scored, because it cannot be seen.
GATES = [
    ("attract", "ATTRACT", "getting found"),
    ("capture", "CAPTURE", "getting your details"),
    ("convert", "CONVERT", "making the sale"),
    ("ascend", "ASCEND", "selling bigger"),
]
GATE_MAX = 25

ROLE_PLAIN = {
    "entrance": "they find him here",
    "hub": "one link, every door",
    "opt-in": "he gets your details",
    "free-courses": "you learn for free",
    "free": "you learn for free",
    "low-ticket": "the cheap yes",
    "sales": "the pitch",
    "sales-vsl": "the pitch (video)",
    "vsl": "the pitch (video)",
    "webinar": "the pitch (live-ish)",
    "community": "you join the room",
    "booking": "you book a call",
    "application": "you apply to be chosen",
    "checkout": "you pay",
    "thank-you": "after you pay",
}


def esc(s):
    return "" if s is None else str(s)


def plain(s):
    """Strip inline HTML/entities for use inside SVG text."""
    s = re.sub(r"<[^>]+>", "", esc(s))
    for a, b in [("&mdash;", "—"), ("&ndash;", "–"), ("&rsquo;", "’"), ("&lsquo;", "‘"),
                 ("&ldquo;", "“"), ("&rdquo;", "”"), ("&hellip;", "…"), ("&amp;", "&"),
                 ("&middot;", "·"), ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " ")]:
        s = s.replace(a, b)
    return s.strip()


def svg_esc(s):
    return (plain(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg_img(svg, style=""):
    """WeasyPrint renders SVG as an image source, not inline — embed as a data URI."""
    if not svg:
        return ""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    st = f' style="{style}"' if style else ""
    return f'<img src="data:image/svg+xml;base64,{b64}" width="100%"{st}>'


def wrap(s, width):
    """Greedy wrap — SVG text does not wrap on its own."""
    words, lines, cur = plain(s).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width:
            cur = f"{cur} {w}".strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def mono_w(s, fs):
    """Width of a Courier string at font-size fs (advance is 0.6em)."""
    return len(plain(s)) * fs * 0.6


def clip(s, n):
    """Shorten prose. Never use this on a URL — a clipped link cannot be visited."""
    s = plain(s)
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def initials(name):
    parts = [p for p in plain(name).replace("@", " ").replace(".", " ").split() if p]
    return "".join(p[0] for p in parts[:2]).upper() or "?"


def tier_color(t):
    return TIER.get(str(t or "").upper(), INK)


def money_step(step):
    p = plain(step.get("price") or "")
    return bool(p) and p not in ("$0", "0", "free", "Free", "FREE")


# ---------------------------------------------------------------- the map ----

def funnel_map_svg(target):
    """The hero visual: the path a stranger walks, drawn as a map."""
    chain = target.get("chain") or []
    if not chain:
        return ""

    # The social platforms ARE the top of the funnel — draw them as a fan-in
    # band above step 01 rather than pretending the funnel starts at a website.
    chans = (target.get("channels") or [])[:8]

    n = len(chain)
    BH = 62 if n <= 5 else (54 if n <= 7 else 46)
    GAP = 24 if n <= 5 else (17 if n <= 7 else 12)
    if chans:                      # make room for the band
        BH -= 6
        GAP -= 3
    BW, PAD = 470, 12
    W = BW + 2 * PAD
    CH, FAN = 30, 30               # chip height, fan-in depth
    band = (16 + CH + FAN) if chans else 0
    H = PAD + band + n * BH + (n - 1) * GAP + PAD

    parts = [
        f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Helvetica, Arial, sans-serif">',
        '<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9 z" fill="{LINE}"/></marker></defs>',
    ]

    if chans:
        parts.append(f'<text x="{PAD}" y="{PAD - 2}" font-size="7.6" font-weight="700" '
                     f'letter-spacing="1.2" fill="{GREY}" font-family="Courier, monospace">'
                     f'THE FREE CONTENT LAYER &#8212; EVERYONE STARTS HERE</text>')
        cw = (BW - (len(chans) - 1) * 5) / len(chans)
        cy0 = PAD + 8
        apex = (PAD + BW / 2, cy0 + CH + FAN - 4)
        for i, c in enumerate(chans):
            cx = PAD + i * (cw + 5)
            primary = bool(c.get("primary"))
            parts.append(f'<rect x="{cx}" y="{cy0}" width="{cw}" height="{CH}" rx="2" '
                         f'fill="{"#EAF0EC" if primary else "#FFFFFF"}" '
                         f'stroke="{GREEN if primary else LINE}" '
                         f'stroke-width="{1.4 if primary else 1}"/>')
            label = plain(c.get("platform", "")).split(" (")[0].split(" /")[0]
            lfs = min(8.5, (cw - 6) / (len(label) * 0.52)) if label else 8.5
            parts.append(f'<text x="{cx + cw / 2}" y="{cy0 + 13}" text-anchor="middle" '
                         f'font-size="{lfs:.1f}" font-weight="700" fill="{INK}">'
                         f'{svg_esc(label)}</text>')
            aud = plain(c.get("audience") or "")
            if aud and "not " not in aud:
                parts.append(f'<text x="{cx + cw / 2}" y="{cy0 + 24}" text-anchor="middle" '
                             f'font-size="7" fill="{GREY}">{svg_esc(aud)}</text>')
            # fan-in line to the single convergence point
            parts.append(f'<line x1="{cx + cw / 2}" y1="{cy0 + CH + 2}" '
                         f'x2="{apex[0]}" y2="{apex[1]}" stroke="{LINE}" stroke-width="0.9"/>')
        parts.append(f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]}" y2="{apex[1] + 10}" '
                     f'stroke="{GREEN}" stroke-width="1.6" marker-end="url(#arw)"/>')

    y = PAD + band
    for i, s in enumerate(chain):
        paid = money_step(s)
        fill = "#EAF0EC" if paid else "#FFFFFF"
        stroke = GREEN if paid else LINE
        sw = 1.6 if paid else 1.0

        parts.append(f'<rect x="{PAD}" y="{y}" width="{BW}" height="{BH}" rx="3" '
                     f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        # step number chip
        parts.append(f'<rect x="{PAD}" y="{y}" width="26" height="{BH}" rx="3" fill="{INK}"/>')
        parts.append(f'<text x="{PAD + 13}" y="{y + BH / 2 + 4}" fill="{PAPER}" font-size="12" '
                     f'font-family="Courier, monospace" font-weight="700" '
                     f'text-anchor="middle">{str(s.get("n", i + 1)).zfill(2)}</text>')

        tx = PAD + 38
        right = PAD + BW - 12
        avail = right - tx
        role = plain(s.get("role", "")).upper()
        r1, r2, r3 = y + BH * 0.28, y + BH * 0.56, y + BH * 0.83

        # --- line 1: role on the left, price on the right -------------------
        # The price lives up here so the URL below can own the full width and
        # never has to be truncated.
        price = plain(s.get("price") or "")
        say = ROLE_PLAIN.get(plain(s.get("role", "")).lower(), "")
        role_w = mono_w(role, 9.5) + len(role) * 1.4
        say_w = len(say) * 9 * 0.47 if say else 0

        price_fs = 15 if (paid and len(price) <= 12) else 10.5
        if price:
            # shrink, then drop the plain-English caption, before ever colliding
            while price_fs > 7 and role_w + 14 + say_w + 12 + mono_w(price, price_fs) > avail:
                if price_fs <= 9 and say:
                    say, say_w = "", 0
                price_fs -= 0.5

        parts.append(f'<text x="{tx}" y="{r1}" font-size="9.5" font-weight="700" '
                     f'letter-spacing="1.4" fill="{GREEN if paid else INK}" '
                     f'font-family="Courier, monospace">{svg_esc(role)}</text>')
        if say:
            parts.append(f'<text x="{tx + role_w + 12}" y="{r1}" font-size="9" '
                         f'fill="{GREY}" font-style="italic">{svg_esc(say)}</text>')
        if price:
            parts.append(f'<text x="{right}" y="{r1 + (2 if price_fs >= 15 else 0)}" '
                         f'text-anchor="end" font-size="{price_fs:.1f}" font-weight="700" '
                         f'font-family="Courier, monospace" '
                         f'fill="{GREEN if paid else GREY}">{svg_esc(price)}</text>')

        # --- line 2: the URL, always complete -------------------------------
        # Never clipped: shrink to fit, and only if it is still too small to
        # read does it wrap onto the description line.
        url = plain(s.get("url", ""))
        url_fs, url_lines = 9.5, [url]
        if url:
            if mono_w(url, url_fs) > avail:
                url_fs = max(6.0, avail / (len(url) * 0.6))
            if mono_w(url, url_fs) > avail:          # still too long: wrap it
                url_fs = 7.5
                per = max(10, int(avail / (url_fs * 0.6)))
                url_lines = [url[i:i + per] for i in range(0, len(url), per)][:2]
            for j, ln in enumerate(url_lines):
                parts.append(f'<text x="{tx}" y="{r2 + j * (url_fs + 1.5)}" '
                             f'font-size="{url_fs:.1f}" fill="{GREEN}" '
                             f'font-family="Courier, monospace">{svg_esc(ln)}</text>')

        # --- line 3: what the page says -------------------------------------
        desc = s.get("headline") or s.get("note") or s.get("proof") or ""
        if desc and len(url_lines) == 1:
            desc_fs = 10
            per = int(avail / (desc_fs * 0.5))
            q = f'“{clip(desc, per)}”' if s.get("headline") else clip(desc, per)
            parts.append(f'<text x="{tx}" y="{r3}" font-size="{desc_fs}" fill="#4A5148">'
                         f'{svg_esc(q)}</text>')

        if i < len(chain) - 1:
            cx = PAD + BW / 2
            parts.append(f'<line x1="{cx}" y1="{y + BH + 4}" x2="{cx}" y2="{y + BH + GAP - 6}" '
                         f'stroke="{LINE}" stroke-width="1.4" marker-end="url(#arw)"/>')
        y += BH + GAP

    parts.append("</svg>")
    return "".join(parts)


# ------------------------------------------------------- the channel map ----

def channel_map_svg(target):
    """Where the traffic comes from: each platform, its exit link, and where
    they all converge. This is the top of the funnel — the part a website-only
    map never shows."""
    chans = target.get("channels") or []
    if not chans:
        return ""

    dest = target.get("channel_destination") or {}
    dest_name = plain(dest.get("name") or "the funnel")
    dest_url = plain(dest.get("url") or "")

    RH = 40 if len(chans) <= 8 else 33
    W = 520
    H = len(chans) * RH + 34
    LX, LW = 0, 132            # platform box
    MX = 162                   # link text
    JX = 366                   # junction (vertical spine)
    DX = 392                   # destination box

    p = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" '
         f'font-family="Helvetica, Arial, sans-serif">',
         '<defs><marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
         f'markerHeight="6" orient="auto"><path d="M0,1 L9,5 L0,9 z" fill="{LINE}"/></marker></defs>']

    p.append(f'<text x="{LX}" y="10" font-size="7.6" font-weight="700" letter-spacing="1.2" '
             f'fill="{GREY}" font-family="Courier, monospace">PLATFORM</text>')
    p.append(f'<text x="{MX}" y="10" font-size="7.6" font-weight="700" letter-spacing="1.2" '
             f'fill="{GREY}" font-family="Courier, monospace">WHERE IT SENDS YOU</text>')
    p.append(f'<text x="{DX}" y="10" font-size="7.6" font-weight="700" letter-spacing="1.2" '
             f'fill="{GREY}" font-family="Courier, monospace">THEY ALL LAND HERE</text>')

    top = 22
    ys = []
    for i, c in enumerate(chans):
        y = top + i * RH
        cy = y + RH / 2 - 4
        ys.append(cy)
        primary = bool(c.get("primary"))
        p.append(f'<rect x="{LX}" y="{y}" width="{LW}" height="{RH - 8}" rx="2" '
                 f'fill="{"#EAF0EC" if primary else "#FFFFFF"}" '
                 f'stroke="{GREEN if primary else LINE}" stroke-width="{1.4 if primary else 1}"/>')
        p.append(f'<text x="{LX + 9}" y="{cy - 1}" font-size="9.5" font-weight="700" '
                 f'fill="{INK}">{svg_esc(clip(c.get("platform", ""), 20))}</text>')
        sub = plain(c.get("audience") or "")
        role = plain(c.get("role") or "")
        subline = " · ".join(x for x in [sub, role] if x)
        if subline:
            p.append(f'<text x="{LX + 9}" y="{cy + 10}" font-size="7.4" fill="{GREY}">'
                     f'{svg_esc(clip(subline, 30))}</text>')

        # arrow out of the platform
        p.append(f'<line x1="{LX + LW + 3}" y1="{cy}" x2="{MX - 6}" y2="{cy}" '
                 f'stroke="{LINE}" stroke-width="1.2" marker-end="url(#a2)"/>')

        link = plain(c.get("links_to") or "")
        lfs = 8.5 if mono_w(link, 8.5) <= (JX - MX - 12) else max(6.0, (JX - MX - 12) / (len(link) * 0.6))
        p.append(f'<text x="{MX}" y="{cy + 1}" font-size="{lfs:.1f}" fill="{GREEN}" '
                 f'font-family="Courier, monospace">{svg_esc(link)}</text>')
        note = plain(c.get("note") or "")
        if note and RH >= 40:
            p.append(f'<text x="{MX}" y="{cy + 11}" font-size="7" fill="{GREY}" '
                     f'font-style="italic">{svg_esc(clip(note, 42))}</text>')

        # feed into the spine
        p.append(f'<line x1="{JX - 22}" y1="{cy}" x2="{JX}" y2="{cy}" stroke="{LINE}" stroke-width="1"/>')

    if ys:
        p.append(f'<line x1="{JX}" y1="{ys[0]}" x2="{JX}" y2="{ys[-1]}" stroke="{LINE}" stroke-width="1"/>')
        mid = (ys[0] + ys[-1]) / 2
        p.append(f'<line x1="{JX}" y1="{mid}" x2="{DX - 4}" y2="{mid}" stroke="{GREEN}" '
                 f'stroke-width="1.6" marker-end="url(#a2)"/>')
        bh, bw = 56, W - DX
        by = mid - bh / 2
        p.append(f'<rect x="{DX}" y="{by}" width="{bw}" height="{bh}" rx="3" fill="#EAF0EC" '
                 f'stroke="{GREEN}" stroke-width="1.6"/>')
        for j, ln in enumerate(wrap(dest_name, 17)[:2]):
            p.append(f'<text x="{DX + bw / 2}" y="{by + 19 + j * 12}" text-anchor="middle" '
                     f'font-size="9.5" font-weight="700" fill="{INK}">{svg_esc(ln)}</text>')
        if dest_url:
            dfs = min(7.5, (bw - 10) / (len(dest_url) * 0.6))
            p.append(f'<text x="{DX + bw / 2}" y="{by + bh - 12}" text-anchor="middle" '
                     f'font-size="{dfs:.1f}" fill="{GREEN}" '
                     f'font-family="Courier, monospace">{svg_esc(dest_url)}</text>')

    p.append("</svg>")
    return "".join(p)


# ------------------------------------------------------------- the ladder ----

def ladder_svg(target):
    """The offer ladder as a staircase — price rising left to right."""
    offers = target.get("offers") or []
    if not offers:
        return ""

    n = len(offers)
    W, H = 500, 300
    BASE, TOP = H - 52, 62          # TOP leaves room for a 2-line price label
    colw = (W - 24) / n
    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="Helvetica, Arial, sans-serif">']

    for i, o in enumerate(offers):
        h = (BASE - TOP) * (i + 1) / n
        x = 12 + i * colw
        yb = BASE - h
        last = i == n - 1
        fill = GREEN if last else ("#CFE0D6" if i >= n - 2 else "#E4E1D4")
        parts.append(f'<rect x="{x}" y="{yb}" width="{colw - 6}" height="{h}" '
                     f'fill="{fill}" stroke="{GREEN if last else LINE}" stroke-width="1"/>')

        price = plain(o.get("price") or "")
        # long labels shrink rather than spill into the neighbouring column
        pfs = 11 if len(price) <= 13 else (9 if len(price) <= 17 else 7.5)
        for j, ln in enumerate(wrap(price, 18)[:2]):
            parts.append(f'<text x="{x + (colw - 6) / 2}" y="{yb - 20 + j * (pfs + 1)}" '
                         f'text-anchor="middle" font-size="{pfs}" font-weight="700" '
                         f'font-family="Courier, monospace" fill="{INK}">{svg_esc(ln)}</text>')

        parts.append(f'<text x="{x + (colw - 6) / 2}" y="{BASE + 16}" text-anchor="middle" '
                     f'font-size="9.5" font-weight="700" letter-spacing="1.2" '
                     f'font-family="Courier, monospace" '
                     f'fill="{GREEN if last else GREY}">{svg_esc(o.get("rung", "")).upper()}</text>')

        for j, ln in enumerate(wrap(o.get("name", ""), 24)[:2]):
            parts.append(f'<text x="{x + (colw - 6) / 2}" y="{BASE + 29 + j * 11}" '
                         f'text-anchor="middle" font-size="8.5" fill="#4A5148">{svg_esc(ln)}</text>')

    parts.append(f'<line x1="8" y1="{BASE}" x2="{W - 8}" y2="{BASE}" stroke="{INK}" stroke-width="1.2"/>')
    parts.append(f'<text x="12" y="16" font-size="9" fill="{GREY}" font-style="italic">'
                 f'cheap &#183; easy to say yes to</text>')
    parts.append(f'<text x="{W - 12}" y="16" text-anchor="end" font-size="9" fill="{GREY}" '
                 f'font-style="italic">expensive &#183; few buyers &#183; most of the money</text>')
    parts.append(f'<line x1="12" y1="26" x2="{W - 12}" y2="26" stroke="#E4E1D4" stroke-width="1"/>')
    parts.append("</svg>")
    return "".join(parts)


# -------------------------------------------------------------- the score ----

def score_svg(target):
    g = target.get("gates") or {}
    if not g:
        return ""
    weak = plain(target.get("weakest_gate", "")).lower()
    rows = [x for x in GATES if x[0] in g]
    W, RH = 500, 34
    H = len(rows) * RH + 8
    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="Helvetica, Arial, sans-serif">']
    for i, (key, label, say) in enumerate(rows):
        v = g[key]
        y = i * RH + 6
        is_weak = key == weak
        parts.append(f'<text x="0" y="{y + 11}" font-size="10" font-weight="700" letter-spacing="1.2" '
                     f'font-family="Courier, monospace" fill="{INK}">{label}</text>')
        parts.append(f'<text x="0" y="{y + 23}" font-size="9" fill="{GREY}" '
                     f'font-style="italic">{svg_esc(say)}</text>')
        bx, bw = 132, 252
        parts.append(f'<rect x="{bx}" y="{y + 4}" width="{bw}" height="15" fill="#E4E1D4"/>')
        parts.append(f'<rect x="{bx}" y="{y + 4}" width="{bw * v / GATE_MAX:.1f}" height="15" '
                     f'fill="{AMBER if is_weak else GREEN}"/>')
        parts.append(f'<text x="{bx + bw + 10}" y="{y + 16}" font-size="11" font-weight="700" '
                     f'font-family="Courier, monospace" fill="{INK}">{v}/{GATE_MAX}</text>')
        if is_weak:
            parts.append(f'<text x="{bx + bw + 48}" y="{y + 16}" font-size="9" font-weight="700" '
                         f'fill="{AMBER}">← weakest</text>')
    parts.append("</svg>")
    return "".join(parts)


def rank_svg(targets):
    scored = sorted([t for t in targets if t.get("score") is not None],
                    key=lambda t: t["score"], reverse=True)
    if len(scored) < 2:
        return ""
    W, RH = 500, 40
    H = len(scored) * RH + 8
    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="Helvetica, Arial, sans-serif">']
    for i, t in enumerate(scored):
        y = i * RH + 6
        parts.append(f'<rect x="0" y="{y + 2}" width="20" height="20" fill="{INK}"/>')
        parts.append(f'<text x="10" y="{y + 17}" text-anchor="middle" font-size="11" fill="{PAPER}" '
                     f'font-family="Courier, monospace" font-weight="700">{i + 1}</text>')
        parts.append(f'<text x="30" y="{y + 15}" font-size="11" font-weight="700" fill="{INK}">'
                     f'{svg_esc(clip(t.get("display_name") or t.get("target"), 34))}</text>')
        parts.append(f'<text x="30" y="{y + 28}" font-size="9" fill="{GREY}" font-style="italic">'
                     f'weakest: {svg_esc(t.get("weakest_gate", ""))}</text>')
        bx, bw = 250, 190
        parts.append(f'<rect x="{bx}" y="{y + 6}" width="{bw}" height="16" fill="#E4E1D4"/>')
        parts.append(f'<rect x="{bx}" y="{y + 6}" width="{bw * t["score"] / 100:.1f}" height="16" fill="{GREEN}"/>')
        parts.append(f'<text x="{bx + bw + 10}" y="{y + 19}" font-size="13" font-weight="700" '
                     f'font-family="Courier, monospace" fill="{INK}">{t["score"]}</text>')
    parts.append("</svg>")
    return "".join(parts)


# ------------------------------------------------------------------ pages ----

CSS = f"""
@page {{ size: Letter; margin: 15mm 14mm 16mm; background: {PAPER};
  @bottom-center {{ content: "FUNNEL SPY  \\00b7  " counter(page) " / " counter(pages);
    font-family: Courier, monospace; font-size: 7pt; color: {GREY}; letter-spacing: 1px; }} }}
@page cover {{ margin: 0; @bottom-center {{ content: none; }} }}
* {{ box-sizing: border-box; }}
body {{ font-family: Helvetica, Arial, sans-serif; color: {INK}; font-size: 9.4pt;
  line-height: 1.5; margin: 0; }}
.mono {{ font-family: Courier, "Courier New", monospace; }}
.cover {{ page: cover; height: 100vh; background: #0C1F18; color: #E9E6DC; padding: 26mm 20mm 20mm; }}
.case {{ font-family: Courier, monospace; font-size: 9.5pt; letter-spacing: 4px; color: #7FBFA3; }}
.cover h1 {{ font-size: 44pt; font-weight: 800; letter-spacing: -1.5px; margin: 8mm 0 0; line-height: 1.02; }}
.cover .sub {{ font-size: 13pt; color: #B9CEC2; margin-top: 5mm; max-width: 140mm; line-height: 1.45; }}
.coverline {{ border-top: 1px solid #2E4A3D; margin-top: 5mm; }}
.plate {{ width: 34mm; height: 40mm; object-fit: cover; border: 1pt solid #3E5D4E;
  filter: grayscale(1) contrast(1.06); }}
.plate-none {{ width: 34mm; height: 40mm; border: 1pt solid #3E5D4E; background: #12291F;
  font-family: Courier, monospace; font-size: 15pt; color: #5F8574; text-align: center; line-height: 40mm; }}
.plate-lbl {{ font-family: Courier, monospace; font-size: 7.5pt; letter-spacing: 1.4px;
  color: #9FBAAD; margin-top: 2.5mm; }}
.manifest {{ font-family: Courier, monospace; font-size: 8.6pt; border: 1px solid #2E4A3D;
  padding: 5mm 6mm; margin-top: 9mm; color: #CFE3D7; line-height: 1.85; }}
.manifest b {{ color: #E9E6DC; font-weight: 700; }}
.stamp {{ font-family: Courier, monospace; font-size: 7pt; font-weight: 700; letter-spacing: 1.4px;
  text-transform: uppercase; border: 1pt solid; padding: 1.5px 6px; }}
.cover-foot {{ position: absolute; bottom: 16mm; left: 20mm; right: 20mm;
  font-family: Courier, monospace; font-size: 8pt; color: #6F8E80; letter-spacing: 1px; }}
h2.h {{ font-size: 17pt; font-weight: 800; margin: 0 0 1mm; letter-spacing: -0.4px; }}
.lede {{ font-size: 10.5pt; color: #4A5148; margin: 0 0 5mm; line-height: 1.45; }}
.rule {{ height: 2.5pt; width: 34px; background: {GREEN}; margin-bottom: 4mm; }}
.k {{ font-size: 7.2pt; font-weight: 800; letter-spacing: 1.3px; text-transform: uppercase; color: {GREY}; }}
.hr {{ border: 0; border-top: 0.6pt solid #D8D4C8; margin: 5mm 0; }}
.keep {{ page-break-inside: avoid; }}
.page {{ page-break-before: always; }}
table {{ border-collapse: collapse; width: 100%; }}
.portrait {{ width: 24mm; height: 24mm; object-fit: cover; border: 0.8pt solid #B9B4A4;
  filter: grayscale(1) contrast(1.05); }}
.portrait-none {{ width: 24mm; height: 24mm; border: 0.8pt solid #B9B4A4; background: #EFECE0;
  font-family: Courier, monospace; font-size: 11pt; color: {GREY}; text-align: center; line-height: 24mm; }}
.bignum {{ font-family: Courier, monospace; font-size: 34pt; font-weight: 700; color: {GREEN}; line-height: 1; }}
.statbox td {{ border: 0.8pt solid #DCD8CB; padding: 2.6mm 3mm; background: #EFECE0; }}
.statval {{ font-family: Courier, monospace; font-size: 13pt; font-weight: 700; }}
.statlbl {{ font-size: 6.8pt; color: {GREY}; text-transform: uppercase; letter-spacing: 0.6px; }}
.chip {{ display: inline-block; font-family: Courier, monospace; font-size: 7.8pt;
  border: 0.8pt solid #B9B4A4; padding: 1.5px 6px; margin: 0 3px 3px 0; }}
.swipe {{ background: #EFECE0; border-left: 2.5pt solid {GREEN}; padding: 3mm 4mm; margin-bottom: 2mm;
  page-break-inside: avoid; }}
.swipe .q {{ font-family: Courier, monospace; font-size: 8.4pt; line-height: 1.45; }}
.swipe .src {{ font-family: Courier, monospace; font-size: 6.5pt; color: {GREY}; margin-top: 1mm; }}
.film td {{ padding: 0 2mm 0 0; vertical-align: top; }}
.film img {{ width: 100%; border: 0.8pt solid #B9B4A4; }}
.film .fc {{ font-family: Courier, monospace; font-size: 6.2pt; color: {GREY}; margin-top: 1.2mm; }}
.finding {{ border: 2pt solid {GREEN}; padding: 5mm 6mm; margin: 5mm 0; page-break-inside: avoid; }}
.finding .lbl {{ font-family: Courier, monospace; font-size: 7pt; font-weight: 700;
  letter-spacing: 2px; color: {GREEN}; }}
.finding .txt {{ font-size: 13pt; font-weight: 700; line-height: 1.35; margin-top: 2mm; }}
.note {{ font-size: 8.8pt; color: #4A5148; line-height: 1.5; }}
.move {{ page-break-inside: avoid; margin-bottom: 3.5mm; }}
.movenum {{ font-family: Courier, monospace; font-size: 13pt; font-weight: 700; color: {GREEN}; }}
.src-foot {{ font-family: Courier, monospace; font-size: 6.6pt; color: {GREY}; margin-top: 7mm;
  border-top: 0.6pt solid #D8D4C8; padding-top: 3mm; line-height: 1.6; }}
.cap {{ font-size: 8.6pt; color: {GREY}; font-style: italic; margin-top: 2mm; }}
.adlink {{ font-family: Courier, monospace; font-size: 8pt; margin-top: 1mm; }}
.adlink a {{ color: {GREEN}; text-decoration: none; }}
.links td {{ padding: 1.2mm 3mm 1.2mm 0; font-size: 8.4pt; vertical-align: top; }}
.links a {{ color: {GREEN}; text-decoration: none; font-family: Courier, monospace; font-size: 7.8pt;
  word-break: break-all; }}
.links .lk {{ font-size: 7pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase;
  color: {GREY}; white-space: nowrap; }}
"""


def cover(targets, meta):
    plates = ""
    for t in targets:
        p = (t.get("portrait") or {}).get("path")
        img = (f'<img class="plate" src="{esc(p)}">' if p
               else f'<div class="plate-none">{initials(t.get("display_name") or t.get("target"))}</div>')
        plates += (f'<td style="width:40mm;padding-right:5mm">{img}'
                   f'<div class="plate-lbl">{svg_esc(t.get("handle") or t.get("target","")).upper()}</div></td>')
    stamps = " ".join(f'<span class="stamp" style="color:{c};border-color:{c}">{n.lower()}</span>'
                      for n, c in TIER.items())
    n = len(targets)
    subject = meta.get("subject") or ", ".join(
        plain(t.get("display_name") or t.get("target", "")) for t in targets)
    title = meta.get("title") or ("One funnel,<br>walked." if n == 1 else f"{n} funnels,<br>walked.")
    sub = meta.get("subtitle") or (
        f"How {subject} turns a stranger into a customer &mdash; every page, every price, "
        "and the machine behind it.")
    return f"""<div class="cover">
  <div class="case">CASE FILE &middot; FUNNEL SPY</div>
  <div class="coverline"></div>
  <h1>{title}</h1>
  <div class="sub">{sub}</div>
  <table style="margin-top:9mm;width:auto"><tr>{plates}</tr></table>
  <div class="manifest">
    SUBJECT &nbsp; <b>{esc(subject)}</b><br>
    RUN DATE &nbsp; <b>{esc(meta.get('run_date',''))}</b><br>
    METHOD &nbsp;&nbsp; <b>{esc(meta.get('method') or 'walked page by page')}</b><br>
    EVIDENCE &nbsp; {stamps}
  </div>
  <div class="cover-foot">PREPARED WITH THE FUNNEL SPY SKILL &middot; MAHAN Ai &middot; @MAHANAICOACH</div>
</div>"""


def page_map(t):
    m = funnel_map_svg(t)
    if not m:
        return ""
    p = t.get("portrait") or {}
    img = (f'<img class="portrait" src="{esc(p["path"])}">' if p.get("path")
           else f'<div class="portrait-none">{initials(t.get("display_name") or t.get("target"))}</div>')
    who = esc(t.get("display_name") or t.get("target"))
    one = esc(t.get("one_liner", ""))
    return f"""<div class="page"></div>
<table><tr>
  <td style="width:28mm">{img}</td>
  <td style="padding-left:5mm;vertical-align:top">
    <h2 class="h">The whole funnel, top to bottom</h2>
    <div class="lede">{who}. Start at the top: every platform funnels into one page, then
    follow the arrows straight down to the money. Green boxes are where you pay.</div>
  </td>
</tr></table>
{('<div class="note" style="font-style:italic;margin-bottom:4mm">' + one + '</div>') if one else ''}
{svg_img(m)}"""


def page_channels(t):
    c = channel_map_svg(t)
    if not c:
        return ""
    read = t.get("channel_read")
    cross = t.get("channel_cross") or []
    crossblock = ""
    if cross:
        rows = "".join(f'<div class="note" style="margin-bottom:1.5mm">&#8226; {esc(x)}</div>'
                       for x in cross)
        crossblock = ('<div class="k" style="margin-top:6mm">HOW THE CHANNELS FEED EACH OTHER</div>'
                      f'<div style="margin-top:2mm">{rows}</div>')
    return f"""<div class="page"></div>
<h2 class="h">The top of the funnel, close up</h2><div class="rule"></div>
<div class="lede">A closer look at the row of platforms from the funnel map: what each channel
is for, and the exact link it points at. Where those links differ per platform, that is how
they tell which channel produced the lead.</div>
{svg_img(c)}
{('<div class="note" style="margin-top:5mm">' + esc(read) + '</div>') if read else ''}
{crossblock}"""


def page_ladder(t):
    l = ladder_svg(t)
    if not l:
        return ""
    return f"""<div class="page"></div>
<h2 class="h">…and then the climb back up</h2>
<div class="rule"></div>
<div class="lede">The funnel narrows going down; the money goes the other way. Once someone
is inside, this is the staircase they climb — each step a bigger price and a smaller crowd.
Watch for a missing step: that gap is where a competitor gets in.</div>
{svg_img(l)}"""


def page_score(t):
    s = score_svg(t)
    if not s:
        return ""
    chips = ""
    for nspec in (t.get("headline_numbers") or t.get("numbers") or [])[:4]:
        chips += (f'<td style="width:25%"><div class="statval" style="color:{tier_color(nspec.get("tier"))}">'
                  f'{esc(nspec.get("value"))}</div>'
                  f'<div class="statlbl">{esc(nspec.get("label"))}</div></td>')
    chipbox = f'<table class="statbox" style="margin-bottom:6mm"><tr>{chips}</tr></table>' if chips else ""
    total = (f'<table><tr><td style="width:34mm"><span class="bignum">{t["score"]}</span>'
             f'<span class="mono" style="font-size:12pt;color:{GREY}">/100</span></td>'
             f'<td class="note" style="vertical-align:middle">The four things a funnel must do that '
             f'an outsider can actually check. He scores {t["score"]} out of 100. The amber bar is '
             f'his worst &mdash; that is where he leaks customers, and where a competitor gets in.'
             f'</td></tr></table>'
             if t.get("score") is not None else "")
    return f"""<div class="page"></div>
<h2 class="h">The scorecard</h2><div class="rule"></div>
{chipbox}{total}
<div style="margin-top:5mm">{svg_img(s)}</div>
<div class="cap">Scored by hand against a fixed rubric &mdash; a judgement, not a measurement.</div>"""


def block_machine(t):
    chips = "".join(f'<span class="chip">{esc(s)}</span>' for s in (t.get("stack") or []))
    for p in (t.get("pixels") or []):
        if isinstance(p, dict):
            label = p.get("name", "")
            if p.get("scope"):
                label += f' ({p["scope"]})'
        else:
            label = str(p)
        chips += f'<span class="chip">{esc(label)}</span>'
    out = ""
    if chips:
        out += f'<div class="k">THE TOOLS HE RUNS ON</div><div style="margin-top:2mm">{chips}</div>'
    if t.get("stack_read"):
        out += f'<div class="note" style="margin-top:3mm">{esc(t["stack_read"])}</div>'
    lines = ""
    for a in (t.get("ads") or []):
        if isinstance(a, str):
            lines += f'<div class="note">{esc(a)}</div>'
            continue
        bits = [f'<b>{esc(a.get("library","")).title()}</b>:']
        if a.get("active") not in (None, ""):
            bits.append(f'{esc(a["active"])} active ads')
        if a.get("scope"):
            bits.append(f'({esc(a["scope"])})')
        if a.get("oldest_running_since"):
            bits.append(f'oldest running since {esc(a["oldest_running_since"])}')
        if a.get("advertiser"):
            bits.append(f'advertiser {esc(a["advertiser"])}')
        if a.get("destinations"):
            bits.append("landing on " + ", ".join(esc(d) for d in a["destinations"]))
        if a.get("note"):
            bits.append("&mdash; " + esc(a["note"]))
        row = f'<div class="note">{" ".join(bits)}</div>'
        if a.get("library_url"):
            row += (f'<div class="adlink">&#8599; <a href="{esc(a["library_url"])}">'
                    f'see every ad they are running &mdash; '
                    f'{esc(a.get("library","")).title()} ad library</a></div>')
        lines += f'<div style="margin-bottom:2.5mm">{row}</div>'
    if lines:
        out += (f'<div class="k" style="margin-top:5mm">IS HE PAYING FOR TRAFFIC?</div>'
                f'<div style="margin-top:2mm">{lines}</div>')
    return out


def block_links(t):
    links = t.get("links") or {}
    if not links:
        return ""
    rows = "".join(f'<tr><td class="lk" style="width:26mm">{esc(k).replace("_"," ")}</td>'
                   f'<td><a href="{esc(v)}">{esc(v)}</a></td></tr>'
                   for k, v in links.items() if v)
    return ('<div class="k">GO LOOK YOURSELF &mdash; EVERY DOOR, CLICKABLE</div>'
            f'<table class="links" style="margin-top:2mm">{rows}</table>')


def block_swipes(t):
    sw = t.get("swipes") or []
    if not sw:
        return ""
    body = "".join(f'<div class="swipe"><div class="q">&ldquo;{esc(s.get("quote"))}&rdquo;</div>'
                   f'<div class="src">&mdash; {esc(s.get("source",""))}</div></div>' for s in sw)
    return f'<div class="k">HIS BEST LINES, WORD FOR WORD</div><div style="margin-top:2mm">{body}</div>'


def block_film(t, run):
    shots = [s for s in (t.get("chain") or [])
             if s.get("evidence") and (run / s["evidence"]).exists()][:3]
    if not shots:
        return ""
    w = f"{100/len(shots):.2f}%"
    cells = "".join(f'<td style="width:{w}"><img src="{esc(s["evidence"])}">'
                    f'<div class="fc">{esc(s.get("role",""))}</div></td>' for s in shots)
    return ('<div class="keep"><div class="k">PROOF &mdash; PAGES WE ACTUALLY OPENED</div>'
            f'<table class="film" style="margin-top:2mm"><tr>{cells}</tr></table></div>')


def page_detail(t, run):
    parts = [p for p in [block_machine(t), block_swipes(t), block_film(t, run),
                         block_links(t)] if p]
    if not parts:
        return ""
    return ('<div class="page"></div><h2 class="h">Under the hood</h2><div class="rule"></div>'
            + '<hr class="hr">'.join(parts))


def page_synthesis(syn, targets):
    if not syn:
        return ""
    out = ['<div class="page"></div><h2 class="h">So what do you do about it?</h2><div class="rule"></div>']
    r = rank_svg(targets)
    if r:
        out.append('<div class="k">WHO IS BEST BUILT</div>'
                   f'<div style="margin:2mm 0 5mm">{svg_img(r)}</div>')
    if syn.get("finding"):
        out.append(f'<div class="finding"><div class="lbl">THE ONE THING TO REMEMBER</div>'
                   f'<div class="txt">{esc(syn["finding"])}</div></div>')
    for key, label in [("patterns", "WHAT THEY ALL DO THE SAME"),
                       ("divergence", "WHERE THEY SPLIT"),
                       ("opening", "YOUR WAY IN")]:
        if syn.get(key):
            out.append(f'<div class="k">{label}</div>'
                       f'<div class="note" style="margin:2mm 0 4mm">{esc(syn[key])}</div>')
    moves = syn.get("steal") or syn.get("fix") or []
    if moves:
        label = "FIX THIS WEEK" if syn.get("fix") else "STEAL THIS WEEK"
        body = "".join(
            f'<div class="move"><span class="movenum">{i}</span> &nbsp;<b>{esc(m.get("move"))}</b>'
            f'<div class="note" style="margin-top:1mm">{esc(m.get("why",""))}</div></div>'
            for i, m in enumerate(moves, 1))
        out.append(f'<hr class="hr"><div class="k">{label}</div>'
                   f'<div style="margin-top:3mm">{body}</div>')
    if syn.get("gaps"):
        g = syn["gaps"]
        g = " ".join(g) if isinstance(g, list) else g
        out.append(f'<hr class="hr"><div class="k">WHAT WE COULD NOT CHECK</div>'
                   f'<div class="note" style="margin-top:2mm">{esc(g)}</div>')
    if syn.get("sources"):
        out.append(f'<div class="src-foot">Sources: '
                   f'{" &middot; ".join(esc(s) for s in syn["sources"])}</div>')
    return "".join(out)


def load(run):
    single = run / "dossier.json"
    files = [single] if single.exists() else sorted(run.glob("*.dossier.json"))
    if not files:
        sys.exit(f"error: no dossier.json or *.dossier.json in {run}\n"
                 "The run must write its findings to JSON before rendering.")
    targets = []
    for f in files:
        try:
            targets.append(json.loads(f.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            sys.exit(f"error: {f.name} is not valid JSON — {e}")
    syn = {}
    sf = run / "synthesis.json"
    if sf.exists():
        syn = json.loads(sf.read_text(encoding="utf-8"))
    return targets, syn


def main():
    ap = argparse.ArgumentParser(description="Render a Funnel Spy dossier PDF from a run folder.")
    ap.add_argument("run")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--title", default=None)
    args = ap.parse_args()

    run = pathlib.Path(args.run).resolve()
    if not run.is_dir():
        sys.exit(f"error: {run} is not a directory")
    targets, syn = load(run)

    meta = {"run_date": targets[0].get("run_date", ""), "title": args.title,
            "subject": syn.get("subject"), "subtitle": syn.get("subtitle"),
            "method": syn.get("method")}

    body = [cover(targets, meta)]
    for t in targets:
        body += [page_map(t), page_ladder(t), page_channels(t), page_score(t),
                 page_detail(t, run)]
    body.append(page_synthesis(syn, targets))

    doc = (f'<html><head><meta charset="utf-8"><style>{CSS}</style></head>'
           f'<body>{"".join(p for p in body if p)}</body></html>')

    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("error: WeasyPrint is not installed.\n"
                 "  pip install weasyprint   (add --break-system-packages if needed)\n"
                 "Every other output format works without it.")

    out = pathlib.Path(args.out) if args.out else run / (
        f"Funnel-Dossier-{targets[0].get('target','run')}.pdf" if len(targets) == 1
        else "Funnel-Dossier.pdf")
    HTML(string=doc, base_url=str(run)).write_pdf(str(out))
    print(f"wrote {out}  ({len(targets)} target{'s' if len(targets) != 1 else ''})")
    print("Now LOOK at the pages before delivering:")
    print(f"  pdftoppm -jpeg -r 70 '{out}' page")


if __name__ == "__main__":
    main()

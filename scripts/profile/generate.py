#!/usr/bin/env python3
"""Render the profile README artwork using only the Python standard library."""

import argparse
from pathlib import Path
from string import Template


OUT = Path(__file__).resolve().parents[2] / "assets" / "profile"

PALETTES = {
    "dark": {
        "base": "#101121",
        "fade": "#211e3a",
        "glow": "#342361",
        "ink": "#f4f2ff",
        "muted": "#bebbd4",
        "line": "#45405f",
        "accent": "#bfaaff",
        "signal": "#80e8c5",
        "panel": "#16172b",
        "chip": "#24213e",
    },
    "light": {
        "base": "#faf8ff",
        "fade": "#eee9ff",
        "glow": "#d8c7ff",
        "ink": "#211738",
        "muted": "#52466f",
        "line": "#ccc2e3",
        "accent": "#6340b4",
        "signal": "#11694f",
        "panel": "#f8f5ff",
        "chip": "#ebe1ff",
    },
}

FRAME = Template("""\
<svg xmlns="http://www.w3.org/2000/svg" width="$w" height="$h" viewBox="0 0 $w $h" role="img" aria-labelledby="title">
  <title>$title</title>
  <style>
    .sans {font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
    .mono {font-family:ui-monospace,"SFMono-Regular",Consolas,monospace;font-weight:700;letter-spacing:1.2px}
    @media (prefers-reduced-motion: no-preference) {
      .orbit {animation:trace 4.7s ease-in-out 1}
      .ping {animation:ping 4.7s ease-out 1}
      .answer {animation:answer 4.3s ease-in-out 1}
    }
    @keyframes trace {
      0% {opacity:0;stroke-dashoffset:110}
      16%, 79% {opacity:1}
      100% {opacity:0;stroke-dashoffset:-460}
    }
    @keyframes ping {
      0%, 17%, 100% {opacity:0;r:6px}
      27% {opacity:.8;r:6px}
      52%, 73% {opacity:0;r:15px}
      79% {opacity:.65;r:6px}
    }
    @keyframes answer {
      0%, 14%, 100% {opacity:0}
      45%, 77% {opacity:1}
    }
  </style>
  <defs>
    <clipPath id="bounds"><rect width="$w" height="$h" rx="26"/></clipPath>
    <linearGradient id="glass" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop stop-color="$base"/><stop offset="1" stop-color="$fade"/>
    </linearGradient>
    <radialGradient id="bloom" cx="$gx" cy="$gy" r=".52">
      <stop stop-color="$glow" stop-opacity=".9"/><stop offset="1" stop-color="$glow" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="19" height="19" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="$line" opacity=".54"/>
    </pattern>
  </defs>
  <g clip-path="url(#bounds)">
    <rect width="$w" height="$h" fill="url(#glass)"/>
    <rect width="$w" height="$h" fill="url(#bloom)"/>
    <rect width="$w" height="$h" fill="url(#dots)"/>
    $content
  </g>
  <rect x=".75" y=".75" width="$bw" height="$bh" rx="25.25" fill="none" stroke="$line" stroke-width="1.5"/>
</svg>
""")

NETWORK = Template("""\
<g transform="$transform">
      <path d="M22 117h272M158 14v206" stroke="$line" stroke-dasharray="2 6" fill="none"/>
      <circle cx="158" cy="117" r="105" fill="none" stroke="$line"/>
      <circle cx="158" cy="117" r="88" fill="$panel" fill-opacity=".55" stroke="$line" stroke-dasharray="2 5"/>
      <circle cx="158" cy="117" r="88" class="orbit" fill="none" stroke="$accent" stroke-width="3"
              stroke-dasharray="32 521" stroke-linecap="round" opacity="0" transform="rotate(-90 158 117)"/>
      <path d="M158 29v55m0 65v56m-70-44 40-26m60 0 40 26" stroke="$accent" stroke-opacity=".6" fill="none"/>
      <circle cx="158" cy="29" r="5" fill="$signal"/>
      <circle cx="88" cy="161" r="5" fill="$accent"/>
      <circle cx="228" cy="161" r="5" fill="$signal"/>
      <circle cx="158" cy="29" r="7" class="ping" fill="none" stroke="$signal" stroke-width="2" opacity="0"/>
      <circle cx="228" cy="161" r="7" class="ping" fill="none" stroke="$signal" stroke-width="2" opacity="0"/>
      <path d="M153 12h10m-5-5v10m-5 205h10m-5-5v10m-110-110h10m-5-5v10m205-5h10m-5-5v10"
            stroke="$accent" stroke-linecap="round" fill="none"/>
      <rect x="116" y="84" width="84" height="65" rx="17" fill="$panel" stroke="$accent" stroke-width="1.4"/>
      <path d="m143 110-9 7 9 7m30-14 9 7-9 7m-11-21-8 28"
            stroke="$accent" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <g class="mono" font-size="12" fill="$muted">
        <text x="177" y="34">WEB</text>
        <text x="24" y="166">MOBİL</text>
        <text x="243" y="166">API</text>
      </g>
      <circle cx="48" cy="61" r="2" fill="$accent" opacity=".8"/>
      <circle cx="265" cy="69" r="2" fill="$signal" opacity=".8"/>
      <circle cx="246" cy="207" r="2" fill="$accent" opacity=".8"/>
    </g>""")

HERO = Template("""\
<path d="M$x $ruleH H$end" stroke="$line"/>
    <rect x="$x" y="$mark" width="9" height="9" rx="2" fill="$signal"/>
    <text x="$labelx" y="$labely" class="mono" fill="$muted" font-size="13">GELİŞTİRİCİ PROFİLİ</text>
    <text x="$end" y="$labely" text-anchor="end" class="mono" fill="$muted" font-size="13">@safak-senal-61</text>
    <text x="$x" y="$namey" class="sans" fill="$ink" font-weight="800" font-size="$namesize" letter-spacing="-2.9">Şafak Şenal<tspan fill="$accent">.</tspan></text>
    <text x="$x" y="$role" class="sans" fill="$muted" font-size="$rolesize">Fullstack &amp; Mobil Geliştirici</text>
    $extra$network""")

HERO_TAGS = Template("""\
<g transform="translate(44 251)" class="mono" font-size="13" fill="$ink">
      <rect width="68" height="33" rx="16.5" fill="$chip" stroke="$line"/>
      <text x="34" y="21" text-anchor="middle">WEB</text>
      <rect x="77" width="84" height="33" rx="16.5" fill="$chip" stroke="$line"/>
      <text x="119" y="21" text-anchor="middle">MOBİL</text>
      <rect x="170" width="68" height="33" rx="16.5" fill="$chip" stroke="$line"/>
      <text x="204" y="21" text-anchor="middle">API</text>
    </g>""")

TAVRIKO = Template("""\
<rect x="42" y="36" width="9" height="9" rx="2" fill="$signal"/>
    <text x="63" y="45" class="mono" font-size="13" fill="$muted">PROJE 01 / CANLI</text>
    <text x="42" y="108" class="sans" font-size="57" font-weight="800" letter-spacing="-2.5" fill="$ink">Tavriko</text>
    <text x="44" y="144" class="sans" font-size="21" fill="$muted">Gerçek zamanlı bilgi yarışması</text>
    <g transform="translate(586 26)">
      <rect width="326" height="124" rx="21" fill="$panel" stroke="$line"/>
      <text x="22" y="32" class="mono" font-size="13" fill="$muted">HIZLI EŞLEŞME</text>
      <path d="M23 49h280" stroke="$line" stroke-width="3" stroke-linecap="round"/>
      <path d="M23 49h192" stroke="$accent" stroke-width="3" stroke-linecap="round"/>
      <g fill="$chip" stroke="$line">
        <rect x="22" y="66" width="63" height="39" rx="9"/>
        <rect x="168" y="66" width="63" height="39" rx="9"/>
        <rect x="241" y="66" width="63" height="39" rx="9"/>
      </g>
      <rect x="95" y="66" width="63" height="39" rx="9" fill="$chip" stroke="$signal"/>
      <rect class="answer" x="95" y="66" width="63" height="39" rx="9" fill="none" stroke="$signal" stroke-width="3" opacity="0"/>
      <g class="mono" font-size="15" fill="$muted" text-anchor="middle">
        <text x="54" y="91">A</text>
        <text x="127" y="91" fill="$signal">B</text>
        <text x="200" y="91">C</text>
        <text x="273" y="91">D</text>
      </g>
    </g>""")


def frame(w, h, title, content, colors, gx, gy):
    return FRAME.substitute(
        w=w, h=h, bw=w - 1.5, bh=h - 1.5, title=title, content=content,
        gx=gx, gy=gy, **colors,
    )


def hero(colors, *, mobile):
    if mobile:
        content = HERO.substitute(
            x=24, end=426, ruleH=64, mark=33, labelx=42, labely=42,
            namey=128, namesize=57, role=165, rolesize=25, extra="",
            network=NETWORK.substitute(transform="translate(67 184)", **colors),
            **colors,
        )
        return frame(450, 425, "Şafak Şenal | Fullstack ve Mobil Geliştirici",
                     content, colors, ".72", ".68")
    content = HERO.substitute(
        x=44, end=916, ruleH=68, mark=33, labelx=63, labely=42,
        namey=172, namesize=78, role=218, rolesize=31,
        extra=HERO_TAGS.substitute(**colors) + "\n    ",
        network=NETWORK.substitute(transform="translate(567 81) scale(1.05)", **colors),
        **colors,
    )
    return frame(960, 340, "Şafak Şenal | Fullstack ve Mobil Geliştirici",
                 content, colors, ".78", ".56")


def artwork():
    for theme, colors in PALETTES.items():
        yield f"hero-{theme}.svg", hero(colors, mobile=False)
        yield f"hero-mobile-{theme}.svg", hero(colors, mobile=True)
        yield f"tavriko-{theme}.svg", frame(
            960, 176, "Tavriko | Gerçek zamanlı bilgi yarışması",
            TAVRIKO.substitute(**colors), colors, ".79", ".5",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if any committed SVG differs from its source")
    args = parser.parse_args()
    if not args.check:
        OUT.mkdir(parents=True, exist_ok=True)
    stale = []
    for name, svg in artwork():
        path = OUT / name
        expected = svg.encode("utf-8")
        if args.check:
            if not path.is_file() or path.read_bytes() != expected:
                stale.append(name)
        else:
            path.write_bytes(expected)
    if stale:
        parser.exit(1, "Regenerate profile SVGs: " + ", ".join(stale) + "\n")


if __name__ == "__main__":
    main()

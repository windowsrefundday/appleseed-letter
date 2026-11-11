#!/usr/bin/env python3
"""Build print-ready recreations of Apple's "Dear Kate" letter (the TextEdit icon).

Renders HTML with exact typographic control, then prints it with headless Chrome
so typefaces are embedded and page sizes are exact.

    python build.py                 # build every variant + PNG proofs
    python build.py card            # one variant
    python build.py --measure       # rebuild + report the block geometry vs the icon

Variants
    card    5 x 6 in      the icon's own proportions - the replica object
    sheet   US Letter     same composition, life size - the framable piece
    letter  US Letter     a normal letter you could actually hand someone
    a4      A4            normal letter, A4 paper
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"

CHROME_CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    "/usr/bin/google-chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

# The letter exactly as it appears on the icon: the 1997 "Think Different"
# manifesto condensed to two paragraphs, plus the addressing and sign-off.
# gap=1 means "leave one blank line after this paragraph".
LETTER = [
    ("Dear Kate,", 1),
    ("Here’s to the crazy ones. The misfits. The rebels. The troublemakers. "
     "The round pegs in the square holes. The ones who see things differently. "
     "They’re not fond of rules. And they have no respect for the status quo. "
     "You can quote them, disagree with them, glorify or vilify them. About the "
     "only thing you can’t do is ignore them. Because they change things.", 1),
    ("They push the human race forward. And while some may see them as the crazy "
     "ones, we see genius. Because the people who are crazy enough to think they "
     "can change the world, are the ones who do.", 1),
]

SIGN = ["Take care,", "John Appleseed"]

# The icon's exact line breaks, transcribed from the reference: with these,
# every replica variant breaks exactly where the icon does, whatever the
# renderer. "" = blank line. (Used by card, card-trim and sheet.)
ICON_LINES = [
    "Dear Kate,",
    "",
    "Here’s to the crazy ones. The misfits. The rebels.",
    "The troublemakers. The round pegs in the square",
    "holes. The ones who see things differently. They’re",
    "not fond of rules. And they have no respect for the",
    "status quo. You can quote them, disagree with them,",
    "glorify or vilify them. About the only thing you can’t",
    "do is ignore them. Because they change things.",
    "",
    "They push the human race forward. And while some",
    "may see them as the crazy ones, we see genius.",
    "Because the people who are crazy enough to think",
    "they can change the world, are the ones who do.",
    "",
    "Take care,",
    "John Appleseed",
]

# Icon reference geometry, measured off the 256px reference: the text block
# starts about 6.5% down the page and ends about 74% down, with a left margin
# near 10.6% and a block about 82% of the sheet width.
VARIANTS = {
    "card": dict(
        page=(5, 6), pad=(0.34, 1.08, 1.30, 0.47),
        size=12.0, leading=1.74, color="#1b1b1b", font="EB Garamond",
        hard_lines=True,
    ),
    "sheet": dict(
        page=(8.5, 11), pad=(0.62, 0.85, 2.30, 0.85),
        size=22.0, leading=1.74, color="#141414", font="EB Garamond",
        hard_lines=True,
    ),
    "letter": dict(
        page=(8.5, 11), pad=(1.20, 1.10, 1.10, 1.10),
        size=14.0, leading=1.50, color="#141414", font="Times New Roman",
    ),
    "a4": dict(
        page=(8.2677, 11.6929), pad=(1.18, 1.06, 1.06, 1.06),
        size=14.0, leading=1.50, color="#141414", font="Times New Roman",
    ),
    "card-trim": dict(
        page=(8.5, 11), pad=(0.34, 1.08, 1.30, 0.47),
        size=12.0, leading=1.66, color="#1b1b1b", font="EB Garamond",
        trim=True, trim_w=5, trim_h=6, hard_lines=True,
    ),
}


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    w = shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chromium")
    if w:
        return w
    sys.exit("Could not find Chrome. Install it or edit CHROME_CANDIDATES.")


def font_face() -> str:
    ttf = (ROOT / "fonts" / "EBGaramond.ttf").as_uri()
    return f"""@font-face {{
    font-family:"EB Garamond";
    src:url("{ttf}") format("truetype");
    font-weight:400; font-style:normal;
  }}"""


def html_for(spec: dict) -> str:
    if spec.get("trim"):
        return html_for_trim(spec)
    if spec.get("hard_lines"):
        return html_for_hard(spec)
    top, right, bottom, left = spec["pad"]
    paras = []
    for text, gap in LETTER:
        style = ' style="margin-bottom:1em"' if gap else ""
        paras.append(f"<p{style}>{text}</p>")
    sign = "".join(f"<p>{line}</p>" for line in SIGN)
    w, h = spec["page"]
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
  @page {{ size: {w}in {h}in; margin: 0; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  .sheet {{
    width:{w}in; height:{h}in; box-sizing:border-box;
    padding:{top}in {right}in {bottom}in {left}in;
    font-family:"{spec['font']}", "Times New Roman", Times, "Liberation Serif", serif;
    font-size:{spec['size']}pt;
    line-height:{spec['leading']};
    color:{spec['color']};
    -webkit-print-color-adjust:exact; print-color-adjust:exact;
    text-rendering:optimizeLegibility; font-kerning:normal;
  }}
  p {{ margin:0; padding:0; }}
  .sign {{ margin:0; }}
  {font_face()}
</style></head>
<body><div class="sheet">
{chr(10).join(paras)}
<div class="sign">{sign}</div>
</div></body></html>
"""


def html_for_trim(spec: dict) -> str:
    top, right, bottom, left = spec["pad"]
    if spec.get("hard_lines"):
        paras = "<br>\n".join(p if p else "&nbsp;" for p in ICON_LINES)
    else:
        parts = []
        for text, gap in LETTER:
            style = ' style="margin-bottom:1em"' if gap else ""
            parts.append(f"<p{style}>{text}</p>")
        parts.append("".join(f"<p>{line}</p>" for line in SIGN))
        paras = "\n".join(parts)
    w, h = spec["page"]
    tw, th = spec["trim_w"], spec["trim_h"]
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
  @page {{ size: {w}in {h}in; margin: 0; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  .outer {{
    width:{w}in; height:{h}in; box-sizing:border-box;
    display:flex; align-items:center; justify-content:center;
    position:relative;
  }}
  .card {{
    width:{tw}in; height:{th}in; box-sizing:border-box;
    padding:{top}in {right}in {bottom}in {left}in;
    font-family:"{spec['font']}", "Times New Roman", Times, "Liberation Serif", serif;
    font-size:{spec['size']}pt;
    line-height:{spec['leading']};
    color:{spec['color']};
    -webkit-print-color-adjust:exact; print-color-adjust:exact;
    text-rendering:optimizeLegibility; font-kerning:normal;
    border:0.75pt solid #000;
    position:relative;
  }}
  p {{ margin:0; padding:0; }}
  .sign {{ margin:0; }}
  .mark {{ position:absolute; background:#000; }}
  .mark.h {{ width:0.25in; height:0.75pt; }}
  .mark.v {{ width:0.75pt; height:0.25in; }}
  .lbl {{
    position:absolute; font-family:Arial, Helvetica, sans-serif;
    font-size:7pt; color:#555; white-space:nowrap;
  }}
  {font_face()}
</style></head>
<body><div class="outer">
<div class="card">
<div class="mark h" style="left:-0.28in; top:-0.75pt;"></div>
<div class="mark h" style="right:-0.28in; top:-0.75pt;"></div>
<div class="mark h" style="left:-0.28in; bottom:-0.75pt;"></div>
<div class="mark h" style="right:-0.28in; bottom:-0.75pt;"></div>
<div class="mark v" style="left:-0.75pt; top:-0.28in;"></div>
<div class="mark v" style="right:-0.75pt; top:-0.28in;"></div>
<div class="mark v" style="left:-0.75pt; bottom:-0.28in;"></div>
<div class="mark v" style="right:-0.75pt; bottom:-0.28in;"></div>
<div class="lbl" style="top:-0.22in; left:0.08in;">cut along black border — 5 x 6 in</div>
{paras}
</div>
</div></body></html>
"""


def html_for_hard(spec: dict) -> str:
    top, right, bottom, left = spec["pad"]
    w, h = spec["page"]
    lines = "<br>\n".join(p if p else "&nbsp;" for p in ICON_LINES)
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
  @page {{ size: {w}in {h}in; margin: 0; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  .sheet {{
    width:{w}in; height:{h}in; box-sizing:border-box;
    padding:{top}in {right}in {bottom}in {left}in;
    font-family:"{spec['font']}", "Times New Roman", Times, "Liberation Serif", serif;
    font-size:{spec['size']}pt;
    line-height:{spec['leading']};
    color:{spec['color']};
    -webkit-print-color-adjust:exact; print-color-adjust:exact;
    text-rendering:optimizeLegibility; font-kerning:normal;
  }}
  {font_face()}
</style></head>
<body><div class="sheet">
{lines}
</div></body></html>
"""


def build(name: str, chrome: str) -> Path:
    spec = VARIANTS[name]
    OUT.mkdir(parents=True, exist_ok=True)
    html_path = OUT / f"appleseed-letter_{name}.html"
    pdf_path = OUT / f"appleseed-letter_{name}.pdf"
    png_path = OUT / f"appleseed-letter_{name}.png"
    html_path.write_text(html_for(spec), encoding="utf-8")
    uri = html_path.resolve().as_uri()
    w, h = spec["page"]

    subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         "--allow-file-access-from-files",
         "--virtual-time-budget=3000", f"--print-to-pdf={pdf_path}", uri],
        check=True, capture_output=True, timeout=120,
    )
    subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", f"--screenshot={png_path}",
         f"--window-size={round(w*96)},{round(h*96)}",
         "--allow-file-access-from-files",
         "--force-device-scale-factor=2", "--hide-scrollbars",
         "--virtual-time-budget=3000", uri],
        check=True, capture_output=True, timeout=120,
    )
    return pdf_path


def measure(name: str) -> None:
    """Report where the ink actually landed, as a percentage of the page."""
    from PIL import Image

    spec = VARIANTS[name]
    w_in, h_in = spec["page"]
    im = Image.open(OUT / f"appleseed-letter_{name}.png").convert("L")
    W, H = im.size
    a = im.tobytes()
    dark = lambda x, y: a[y * W + x] < 160
    row = [any(dark(x, y) for x in range(W)) for y in range(H)]
    ys = [y for y, v in enumerate(row) if v]
    xs = [x for x in range(W) if any(dark(x, y) for y in range(H))]
    bands, start = [], None
    for y, v in enumerate(row):
        if v and start is None:
            start = y
        if not v and start is not None:
            bands.append((start, y - 1))
            start = None
    if start is not None:
        bands.append((start, H - 1))
    print(f"[{name}] {w_in}x{h_in}in  {len(bands)} ink bands")
    print(f"   top {(ys[0])/(H-1)*100:5.1f}%   bottom {(H-1-ys[-1])/(H-1)*100:5.1f}%   "
          f"left {(xs[0])/(W-1)*100:5.1f}%   right {(W-1-xs[-1])/(W-1)*100:5.1f}%")
    print(f"   block {(ys[-1]-ys[0])/(H-1)*100:5.1f}% of height, "
          f"{(xs[-1]-xs[0])/(W-1)*100:5.1f}% of width")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("only", nargs="*")
    ap.add_argument("--measure", action="store_true")
    args = ap.parse_args()
    chrome = find_chrome()
    names = args.only or list(VARIANTS)
    for name in names:
        if name not in VARIANTS:
            sys.exit(f"unknown variant {name!r}; choose from {list(VARIANTS)}")
        p = build(name, chrome)
        print(f"built {p.name}  {p.stat().st_size/1024:.1f} KB")
        if args.measure:
            measure(name)


if __name__ == "__main__":
    main()

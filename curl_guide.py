#!/usr/bin/env python3
"""Draw the curl guide: where the icon's rolled corner sits, in real inches.

    python curl_guide.py            # writes out/curl-guide_card.png + _sheet.png

The reference icon curls the top-right corner so far in that the roll covers the
ends of the first three lines of body copy (that is why the icon's text looks
clipped).  Measured off the 256px reference, the crease runs from ~49% of the
width along the top edge to ~37% of the height down the right edge.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "out"
FOLD_TOP = 0.49      # crease start, fraction of page width, along the top edge
FOLD_SIDE = 0.37     # crease end, fraction of page height, down the right edge
SCALE = 150          # px per inch in the drawing


def font(size: int) -> ImageFont.FreeTypeFont:
    for p in ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/segoeui.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def draw(name: str, w_in: float, h_in: float, margin: float, top: float) -> None:
    pad = 1.6
    W = int((w_in + 2 * pad) * SCALE)
    H = int((h_in + 2 * pad) * SCALE)
    im = Image.new("RGB", (W, H), "#f2f2ef")
    d = ImageDraw.Draw(im)
    ox, oy = pad * SCALE, pad * SCALE
    x0, y0 = ox, oy
    x1, y1 = ox + w_in * SCALE, oy + h_in * SCALE

    # the sheet + its shadow
    d.rectangle([x0 + 6, y0 + 8, x1 + 6, y1 + 8], fill="#d9d9d4")
    d.rectangle([x0, y0, x1, y1], fill="white", outline="#b0b0aa", width=2)

    # text block, as printed
    d.rectangle([x0 + margin * SCALE, y0 + top * SCALE,
                 x1 - margin * SCALE, y1 - (h_in * 0.235) * SCALE],
                outline="#c8c8c2", width=1)
    d.text((x0 + margin * SCALE + 6, y0 + top * SCALE + 6), "text block",
           font=font(18), fill="#b6b6b0")

    # the curl: crease line + shaded flap
    cx, cy = x0 + w_in * FOLD_TOP * SCALE, y0
    d.line([cx, cy, x1, y0 + h_in * FOLD_SIDE * SCALE], fill="#e5533d", width=3)
    d.polygon([(cx, cy), (x1, y0), (x1, y0 + h_in * FOLD_SIDE * SCALE)],
              fill="#f7d7cf")

    # dimensions
    f = font(20)
    d.text((cx, y0 - 34), f"{w_in * FOLD_TOP:.2f} in", font=f, fill="#e5533d")
    d.text((x1 + 14, y0 + h_in * FOLD_SIDE * SCALE - 10),
           f"{h_in * FOLD_SIDE:.2f} in", font=f, fill="#e5533d")
    d.text((cx, y0 - 62), "crease starts here on the top edge", font=font(17), fill="#8a8a84")
    d.text((x0, y1 + 18), f"{name}: roll the shaded corner toward you, over a "
                          f"{max(0.6, w_in * 0.16):.1f} in dowel",
           font=font(19), fill="#4a4a46")
    im.save(OUT / f"curl-guide_{name}.png")
    print(f"wrote curl-guide_{name}.png  {W}x{H}")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw("card", 5, 6, 0.50, 0.34)
    draw("sheet", 8.5, 11, 0.85, 0.62)

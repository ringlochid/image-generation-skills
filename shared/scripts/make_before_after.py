#!/usr/bin/env python3
"""Create a simple before/after comparison image.

Usage:
  python3 make_before_after.py before.png after.png output.png [--force]
"""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

LABEL_H = 56
PAD = 16

def load(path: str) -> Image.Image:
    return Image.open(Path(path).expanduser()).convert("RGBA")

def main() -> int:
    ap = argparse.ArgumentParser(description="Create a before/after comparison image.")
    ap.add_argument("before")
    ap.add_argument("after")
    ap.add_argument("output", type=Path)
    ap.add_argument("--force", action="store_true", help="Overwrite existing output")
    args = ap.parse_args()
    before, after = load(args.before), load(args.after)
    h = max(before.height, after.height)
    def fit(img: Image.Image) -> Image.Image:
        if img.height == h:
            return img
        w = round(img.width * (h / img.height))
        return img.resize((w, h), Image.Resampling.LANCZOS)
    before, after = fit(before), fit(after)
    w = before.width + after.width + PAD * 3
    canvas = Image.new("RGBA", (w, h + LABEL_H + PAD * 2), "#111111")
    draw = ImageDraw.Draw(canvas)
    x1, x2 = PAD, before.width + PAD * 2
    y = LABEL_H + PAD
    canvas.alpha_composite(before, (x1, y))
    canvas.alpha_composite(after, (x2, y))
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    except Exception:
        font = ImageFont.load_default()
    draw.text((x1, PAD), "Before", fill="#E5E7EB", font=font)
    draw.text((x2, PAD), "After", fill="#E5E7EB", font=font)
    out = args.output.expanduser().resolve()
    if out.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite {out}; pass --force to replace it")
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out)
    print(f"MEDIA:{out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Export a square source PNG/WebP/JPEG into common app/web icon sizes.

Usage:
  python3 export_icon_pack.py source.png out_dir [--force]
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from PIL import Image

SIZES = {
    "appstore-1024.png": 1024,
    "ios-180.png": 180,
    "ios-167.png": 167,
    "ios-152.png": 152,
    "ios-120.png": 120,
    "android-512.png": 512,
    "android-192.png": 192,
    "android-144.png": 144,
    "android-96.png": 96,
    "android-72.png": 72,
    "android-48.png": 48,
    "pwa-512.png": 512,
    "pwa-192.png": 192,
    "apple-touch-icon.png": 180,
    "favicon-32.png": 32,
    "favicon-16.png": 16,
}

def main() -> int:
    ap = argparse.ArgumentParser(description="Export common app/web icon sizes.")
    ap.add_argument("source", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--force", action="store_true", help="Overwrite existing icon files")
    args = ap.parse_args()
    src = args.source.expanduser().resolve()
    out = args.out_dir.expanduser().resolve()
    if not src.is_file():
        print(f"Missing source: {src}", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    targets = [out / name for name in SIZES]
    existing = [p for p in targets if p.exists()]
    if existing and not args.force:
        first = existing[0]
        raise SystemExit(f"Refusing to overwrite {first} and {len(existing)-1} other file(s); pass --force to replace them")
    for name, size in SIZES.items():
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(out / name)
    print(f"Exported {len(SIZES)} icons to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

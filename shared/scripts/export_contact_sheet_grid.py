#!/usr/bin/env python3
"""Deterministically split a contact sheet into grid cells and optional ZIP.

Examples:
  python3 export_contact_sheet_grid.py sheet.png out --grid 4 --prefix sticker --format webp --zip
  python3 export_contact_sheet_grid.py avatars.png out --grid 2 --prefix avatar --sizes 512,1024 --format jpg
"""
from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path
from PIL import Image

FIXED_ZIP_TIME = (2020, 1, 1, 0, 0, 0)


def parse_sizes(raw: str) -> list[int]:
    sizes = []
    for part in raw.split(','):
        part = part.strip()
        if part:
            sizes.append(int(part))
    return sizes


def save_cell(img: Image.Image, path: Path, fmt: str, quality: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == 'webp':
        img.save(path, 'WEBP', quality=quality, method=4)
    elif fmt in {'jpg', 'jpeg'}:
        img.convert('RGB').save(path, 'JPEG', quality=quality, optimize=True)
    elif fmt == 'png':
        img.save(path, 'PNG')
    else:
        raise ValueError(f'unsupported format: {fmt}')


def deterministic_zip(zip_path: Path, files: list[Path]) -> None:
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(files, key=lambda p: p.name):
            info = zipfile.ZipInfo(path.name, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())


def main() -> int:
    ap = argparse.ArgumentParser(description='Split a contact sheet into deterministic grid exports.')
    ap.add_argument('sheet', type=Path)
    ap.add_argument('out_dir', type=Path)
    ap.add_argument('--grid', type=int, required=True, help='Grid count per side, e.g. 4 for 4x4 or 2 for 2x2')
    ap.add_argument('--prefix', default='cell')
    ap.add_argument('--format', choices=['webp', 'jpg', 'jpeg', 'png'], default='webp')
    ap.add_argument('--sizes', default='', help='Comma sizes for resized copies. Empty means native cell size only.')
    ap.add_argument('--quality', type=int, default=95)
    ap.add_argument('--inset', type=int, default=0, help='Crop this many pixels inside every cell before resizing; useful for removing generated grid/boundary lines')
    ap.add_argument('--zip', action='store_true', help='Create a zip containing exported files')
    ap.add_argument('--manifest', action='store_true', help='Write manifest.json with source/export metadata')
    ap.add_argument('--expected-size', default='', help='Fail unless source image is WIDTHxHEIGHT, e.g. 2048x2048')
    ap.add_argument('--max-bytes', type=int, default=0, help='Fail if any exported file exceeds this many bytes (0 disables)')
    ap.add_argument('--force', action='store_true', help='Overwrite existing export files')
    args = ap.parse_args()

    sheet = args.sheet.expanduser().resolve()
    out_dir = args.out_dir.expanduser().resolve()
    if not sheet.is_file():
        raise SystemExit(f'Missing sheet: {sheet}')
    if args.grid <= 0:
        raise SystemExit('--grid must be positive')
    if args.inset < 0:
        raise SystemExit('--inset must be >= 0')

    im = Image.open(sheet).convert('RGBA')
    w, h = im.size
    if args.expected_size:
        try:
            ew_raw, eh_raw = args.expected_size.lower().split('x', 1)
            ew, eh = int(ew_raw), int(eh_raw)
        except Exception as exc:
            raise SystemExit('--expected-size must be WIDTHxHEIGHT') from exc
        if (w, h) != (ew, eh):
            raise SystemExit(f'Sheet size {w}x{h} does not match expected {ew}x{eh}')
    if w % args.grid or h % args.grid:
        raise SystemExit(f'Sheet size {w}x{h} is not divisible by grid {args.grid}')
    cw, ch = w // args.grid, h // args.grid
    if args.inset * 2 >= min(cw, ch):
        raise SystemExit(f'--inset {args.inset} is too large for cell size {cw}x{ch}')
    if cw != ch:
        print(f'warning: cells are {cw}x{ch}, not square')

    sizes = parse_sizes(args.sizes)
    ext = 'jpg' if args.format == 'jpeg' else args.format
    planned: list[tuple[Path, tuple[int, int, int, int], int | None]] = []
    for r in range(args.grid):
        for c in range(args.grid):
            idx = r * args.grid + c + 1
            box = (c * cw + args.inset, r * ch + args.inset, (c + 1) * cw - args.inset, (r + 1) * ch - args.inset)
            planned.append((out_dir / f'{args.prefix}_{idx:02d}.{ext}', box, None))
            crop_w = box[2] - box[0]
            crop_h = box[3] - box[1]
            for size in sizes:
                if size == crop_w == crop_h:
                    continue
                planned.append((out_dir / f'{args.prefix}_{idx:02d}_{size}.{ext}', box, size))

    target_paths = [path for path, _box, _size in planned]
    if args.manifest:
        target_paths.append(out_dir / 'manifest.json')
    if args.zip:
        target_paths.append(out_dir / f'{args.prefix}_grid_exports.zip')
    existing = [path for path in target_paths if path.exists()]
    if existing and not args.force:
        first = existing[0]
        raise SystemExit(f'Refusing to overwrite {first} and {len(existing)-1} other file(s); pass --force to replace them')

    out_dir.mkdir(parents=True, exist_ok=True)
    exported: list[Path] = []
    for path, box, size in planned:
        cell = im.crop(box)
        if size is not None:
            cell = cell.resize((size, size), Image.Resampling.LANCZOS)
        save_cell(cell, path, args.format, args.quality)
        if args.max_bytes and path.stat().st_size > args.max_bytes:
            raise SystemExit(f'{path} is {path.stat().st_size} bytes, exceeds --max-bytes {args.max_bytes}')
        exported.append(path)

    if args.manifest:
        manifest = {
            'source': str(sheet),
            'source_size': [w, h],
            'grid': args.grid,
            'cell_size': [cw, ch],
            'inset': args.inset,
            'format': args.format,
            'sizes': sizes,
            'exports': [{'path': str(path), 'bytes': path.stat().st_size} for path in exported],
        }
        manifest_path = out_dir / 'manifest.json'
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
        exported.append(manifest_path)

    if args.zip:
        zip_path = out_dir / f'{args.prefix}_grid_exports.zip'
        deterministic_zip(zip_path, exported)
        exported.append(zip_path)

    print(f'exported {len(exported)} files to {out_dir}')
    for path in exported:
        print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

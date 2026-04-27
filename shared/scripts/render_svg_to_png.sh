#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 || $# -gt 4 ]]; then
  echo "Usage: render_svg_to_png.sh input.svg output.png [size] [--force]" >&2
  exit 2
fi
IN="$1"
OUT="$2"
SIZE="${3:-1024x1024}"
FORCE="${4:-}"
if [[ "$SIZE" == "--force" ]]; then SIZE="1024x1024"; FORCE="--force"; fi
if [[ "$SIZE" == *x* ]]; then W="${SIZE%x*}"; H="${SIZE#*x}"; else W="$SIZE"; H="$SIZE"; fi
command -v sharp >/dev/null || { echo "Missing sharp CLI. Install: npm install -g sharp-cli" >&2; exit 3; }
if [[ -e "$OUT" && "$FORCE" != "--force" ]]; then
  echo "Refusing to overwrite $OUT; pass --force to replace it" >&2
  exit 4
fi
mkdir -p "$(dirname "$OUT")"
sharp -i "$IN" -o "$OUT" resize "$W" "$H" --fit contain --background transparent >/dev/null
printf 'MEDIA:%s\n' "$OUT"

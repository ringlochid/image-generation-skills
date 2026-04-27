#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 3 || $# -gt 5 ]]; then
  echo "Usage: logo_qa.sh draft.png final.svg out_dir [size] [--force]" >&2
  exit 2
fi
DRAFT="$1"
SVG="$2"
OUTDIR="$3"
SIZE="${4:-1024x1024}"
FORCE="${5:-}"
if [[ "$SIZE" == "--force" ]]; then SIZE="1024x1024"; FORCE="--force"; fi
if [[ "$SIZE" == *x* ]]; then W="${SIZE%x*}"; H="${SIZE#*x}"; else W="$SIZE"; H="$SIZE"; fi
command -v sharp >/dev/null || { echo "Missing sharp CLI. Install: npm install -g sharp-cli" >&2; exit 3; }
command -v pixelmatch >/dev/null || { echo "Missing pixelmatch CLI. Install: npm install -g pixelmatch pngjs" >&2; exit 3; }
command -v svgo >/dev/null || { echo "Missing svgo CLI. Install: npm install -g svgo" >&2; exit 3; }
mkdir -p "$OUTDIR"
DRAFT_N="$OUTDIR/draft-normalized.png"
RENDERED="$OUTDIR/final-rendered.png"
DIFF="$OUTDIR/diff.png"
OPT="$OUTDIR/final.optimized.svg"
REPORT_PATH="$OUTDIR/qa-report.md"
for target in "$DRAFT_N" "$RENDERED" "$DIFF" "$OPT" "$REPORT_PATH"; do
  if [[ -e "$target" && "$FORCE" != "--force" ]]; then
    echo "Refusing to overwrite $target; pass --force to replace it" >&2
    exit 4
  fi
done
sharp -i "$DRAFT" -o "$DRAFT_N" resize "$W" "$H" --fit contain --background white >/dev/null
sharp -i "$SVG" -o "$RENDERED" resize "$W" "$H" --fit contain --background white >/dev/null
set +e
PM_OUT=$(pixelmatch "$DRAFT_N" "$RENDERED" "$DIFF" 0.12 2>&1)
PM_CODE=$?
set -e
svgo -i "$SVG" -o "$OPT" --multipass >/dev/null
cat > "$REPORT_PATH" <<REPORT
# Logo QA report

- Draft normalized: $DRAFT_N
- SVG rendered: $RENDERED
- Diff image: $DIFF
- Optimized SVG: $OPT
- Pixelmatch exit code: $PM_CODE
- Pixelmatch output: $PM_OUT

Review the rendered SVG and diff before calling the SVG final. A high visual diff is acceptable only when the SVG is intentionally a simplified production rebuild rather than a faithful vectorization.
REPORT
printf 'MEDIA:%s\nMEDIA:%s\nREPORT:%s\n' "$RENDERED" "$DIFF" "$REPORT_PATH"

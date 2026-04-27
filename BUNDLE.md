# Image Generation Skills Bundle

Installable local skill bundle for image-generation workflows.

## Skills

- `character-source-lock/` — source-backed identity locking for existing/anime/game/fandom-looking characters.
- `visual-review-gate/` — reusable QA/review gate for generated visual artifacts.
- `persona-sticker-pack/` — coherent Telegram/reaction sticker packs.
- `avatar-variant-studio/` — square profile/avatar variants from an identity source.
- `character-sheet-studio/` — character sheets and deterministic PDF dossiers.
- `brand-mark-studio/` — logos, app icons, favicons; image drafts → SVG/vector or deterministic raster final.

## Shared resources

- `shared/references/generation-policy.md`
- `shared/references/run-manifest.md`
- `shared/references/identity-anchors.md`
- `shared/references/vectorization-qa.md`
- `shared/references/finalization-policy.md`
- `shared/references/request-routing.md`
- `shared/references/output-checks.md`
- `shared/scripts/export_icon_pack.py`
- `shared/scripts/export_contact_sheet_grid.py`
- `shared/scripts/make_before_after.py`
- `shared/scripts/build/render/QA helpers`
- `references/README-SAFETY.md`

## Examples

Curated accepted examples live in `examples/`:

- `persona-sticker-yuyuko/`
- `persona-sticker-youmu/`
- `avatar-yuyuko/`
- `character-sheet-yuyuko/`
- `character-sheet-starlit-courier/`

Bulky transient runs should live outside the installable bundle.

## Core rule

Use `openai/gpt-image-2` for production generation unless fallback is explicitly approved. Use deterministic SVG/PDF/image-processing/export steps for final truth when text, geometry, sizing, or packaging matters.

## Installation

```bash
SRC=$PWD
DST=/path/to/openclaw/workspace/skills
for d in character-source-lock visual-review-gate persona-sticker-pack avatar-variant-studio character-sheet-studio brand-mark-studio shared; do
  rm -rf "$DST/$d"
  cp -a "$SRC/$d" "$DST/$d"
done
openclaw skills check
```

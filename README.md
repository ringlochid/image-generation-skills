# Image Generation Skills Bundle

Lean local skill bundle for image-generation workflows where the model creates drafts/art plates, and deterministic scripts handle exports, PDFs, manifests, and packaging.

## Install into Orin

From this repo:

```bash
SRC=/home/ubuntu/leo/skills/image-generation-skills
DST=/home/ubuntu/.openclaw/workspaces/orin/skills
for d in character-source-lock visual-review-gate persona-sticker-pack avatar-variant-studio character-sheet-studio brand-mark-studio shared; do
  rm -rf "$DST/$d"
  cp -a "$SRC/$d" "$DST/$d"
done
openclaw skills check
```

Expected ready skills:

- `character-source-lock`
- `visual-review-gate`
- `persona-sticker-pack`
- `avatar-variant-studio`
- `character-sheet-studio`
- `brand-mark-studio`

## Active skills

1. `character-source-lock/` — source-backed identity locking for existing/anime/game/fandom-looking characters.
2. `visual-review-gate/` — QA/review gate for generated visual artifacts before delivery/export.
3. `persona-sticker-pack/` — Telegram/reaction sticker packs from an image-backed or described subject.
4. `avatar-variant-studio/` — square profile/avatar variants from a locked identity.
5. `character-sheet-studio/` — reusable character sheets plus deterministic PDF dossiers.
6. `brand-mark-studio/` — brand marks, app icons, favicons; generated drafts → deterministic SVG/raster finalization.

## Shared contract

- Use `openai/gpt-image-2` explicitly for production generation unless the user approves fallback.
- Pass exact size/aspect when output geometry matters.
- Verify returned provider/model and actual image dimensions before accepting output.
- Keep generated readable text out of final assets; add readable text deterministically.
- Use deterministic scripts for grid export, icon export, SVG render/QA, and PDF dossier output.
- Preserve source inputs and keep generated art separate from final exports.

## Routing quick reference

- Existing/fandom-looking subject identity uncertain → `character-source-lock` first.
- Sticker/reaction sheet → `persona-sticker-pack` → `visual-review-gate` → deterministic grid export.
- Profile/avatar variants → `avatar-variant-studio` → deterministic square exports.
- Character reference/style bible → `character-sheet-studio` → deterministic PDF dossier.
- Logo/app icon/brand mark → `brand-mark-studio` → deterministic vector/raster QA.

## Curated examples

Representative accepted outputs are kept under `examples/`.

### Sticker pack — Yuyuko

- Folder: `examples/persona-sticker-yuyuko/`
- Shows: source lock → `openai/gpt-image-2` 2048×2048 4×4 sheet → visual QA → deterministic 512 WebP export.
- Files: `preview.png`, `stickers-webp.zip`, `source_lock.md`, `run_manifest.json`.

### Sticker pack — swordswoman

- Folder: `examples/persona-sticker-swordswoman/`
- Shows: prior accepted direct 4×4 sticker workflow from 2026-04-26.
- Files: `preview.jpg`, `stickers-webp.zip`.

### Avatar variants — Yuyuko

- Folder: `examples/avatar-yuyuko/`
- Shows: 2×2 `openai/gpt-image-2` 2048×2048 avatar sheet → deterministic 512/1024 exports.
- Files: `preview.jpg`, `avatar-bundle.zip`, `run_manifest.json`.

### Character sheet — Yuyuko

- Folder: `examples/character-sheet-yuyuko/`
- Shows: source lock → 3840×2160 art-only sheet → visual QA → deterministic 2-page PDF dossier.
- Files: `preview.jpg`, `brief.md`, `dossier.pdf`, `run_manifest.json`.

### Character sheet — Starlit Courier

- Folder: `examples/character-sheet-starlit-courier/`
- Shows: prior accepted 3840×2160 character-sheet/PDF workflow.
- Files: `preview.jpg`, `brief.md`, `dossier.pdf`.

## Sticker style assets

`persona-sticker-pack/assets/style-examples/` contains compact style-only references. Use them for crop, outline, scale, expression grammar, and gutters only — not identity or exact poses.

Best references:

- `good-white-halo-4x4.png`
- `good-red-4x4.jpg`
- `good-blonde-4x4.jpg`
- `good-white-sword-4x4.jpg`
- `generic-sticker-style-grid-768.png`

## Archive policy

The production bundle stays lean. Bulky/rejected/transient test runs are archived outside the installable bundle:

- `/home/ubuntu/leo/artifacts/image-generation-skills-archive-20260427/`
- `/home/ubuntu/leo/artifacts/image-generation-skills-test-runs-20260426-27/`

Do not copy archive contents back into active skills unless a specific file becomes a curated example or style asset.

## Validation

Minimum local validation after edits:

```bash
python3 -m py_compile \
  shared/scripts/export_contact_sheet_grid.py \
  shared/scripts/export_icon_pack.py \
  character-sheet-studio/scripts/build_character_dossier_pdf.py
openclaw skills check
```

For production generation tests, include provider proof, actual dimensions, QA verdict, and artifact paths in a run manifest.

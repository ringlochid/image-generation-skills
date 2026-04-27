---
name: persona-sticker-pack
description: "Generate coherent Telegram-style sticker packs for an image-backed or described subject. Use for sticker sheets, mood/reaction packs, emoji-like stickers, and subject-consistent messaging stickers."
---

# Persona Sticker Pack

Generate Telegram-style reaction sticker packs from a subject image or description.

Read first:
- `../shared/references/request-routing.md`
- `../shared/references/identity-anchors.md`
- `references/style-reference-examples.md`
- `references/telegram-sticker-examples.md`
- `../shared/references/generation-policy.md`
- `../shared/references/output-checks.md`
- `../shared/references/finalization-policy.md`
- Use `visual-review-gate` before export when creating a deliverable pack.

## Defaults

- Model: `openai/gpt-image-2`
- Pack preview: 4x4 at explicit `size="2048x2048"`
- Output: contact sheet first; export individual 512x512 WebP only after a sheet is visually accepted
- Fallback/provider proof: follow `generation-policy.md`; reject unapproved fallback/normalization.
- Final export: deterministic 4x4 grid split after an accepted sheet.
- Do not use 2x2 batch/reliability mode unless Leo explicitly approves it.

## Workflow

1. **Lock the subject**
   - Prefer a user-provided identity image.
   - Extract stable subject-type anchors using `identity-anchors.md`; do not force human fields onto pets, mascots, products, or objects.
   - If the subject may be anime/game/fandom media, follow `request-routing.md` and use `character-source-lock` when needed.

2. **Use examples as style references**
   - Pass the subject image as identity reference.
   - Pass one curated image from `assets/style-examples/` as style-only reference when possible. Prefer the `good-*-4x4` sheets for Leo-style anime sticker packs.
   - Before calling `image_generate`, copy any bundled style asset to an allowed media/work output path, e.g. `/home/ubuntu/.openclaw/media/generated/<run>/style_ref.png`; direct skill asset paths may be outside the image tool's allowed media boundary.
   - Use `references/telegram-sticker-examples.md` for real Telegram sticker source grammar.
   - State in the prompt: identity image controls character; style refs control crop, outline, scale, grid, expressions, and gutters only.

3. **Generate pack preview**
   - Request exactly one 4x4 sheet with `model="openai/gpt-image-2"` and `size="2048x2048"`.
   - Inspect the tool result. Accept only returned `openai/gpt-image-2` output at actual 2048×2048 unless Leo explicitly approved fallback or another size/model.
   - Do not switch to four 2x2 batches or assemble sheets unless Leo explicitly asks; this changes the pack grammar and increases consistency risk.
   - Ask for compact chibi/bust stickers, thick dark line, bold white die-cut border, pale/neutral cell backgrounds, flat readable colors, clear emotions, and generous gutters.

4. **Hard visual QA before export**
   - Accept only if it looks like the curated examples and real Telegram packs.
   - Reject and regenerate on any blocker: wrong identity, unapproved provider/model/size, nested mini-sheets, multiple stickers inside one 512 cell, tiny subjects, inconsistent scale, readable text/letters/numbers, logos/watermarks, copied sticker poses, broken anatomy, cropped/unusable cells, or stickers/props/borders touching or crossing cell boundaries.
   - Dimension/file-count checks are not enough. Inspect the generated source sheet visually before export.

5. **Export only accepted sheets**
   - Split accepted sheets with `../shared/scripts/export_contact_sheet_grid.py`.
   - Example: `python3 ../shared/scripts/export_contact_sheet_grid.py contact_sheet.png exports --grid 4 --prefix sticker --format webp --sizes 512 --zip`.
   - Do not semantic-mask, repaint, or rebuild borders during export unless explicitly requested.

## Prompt skeleton

```text
Create a 4x4 Telegram sticker pack preview. Tool params: model=openai/gpt-image-2, size=2048x2048.
Identity reference: preserve [subject-type-specific anchors].
Style reference: use only crop, outline, scale, grid, expression grammar, and gutter spacing from the provided sticker example.
Style: super-deformed chibi bust stickers, huge head, tiny torso, thick dark outline, bold white die-cut border, flat cel shading, readable at chat size.
Moods: [16 reactions].
Keep all stickers the same subject, same scale, centered in equal cells. Leave blank gutters; each sticker including border/props fits inside about 80-85% of its cell and never touches/crosses cell edges.
No readable text, letters, numbers, captions, logos, watermarks, or speech-bubble writing.
```

## Small modes

- **Avatar crop**: if the user wants a profile/avatar from an accepted sticker subject, generate or pick one strong bust cell, then deterministically crop/resize to the requested square size. Keep it readable at small size; avoid busy backgrounds.

## Report

Return:

- provider/model proof and run-manifest path
- contact sheet or batch sheet paths
- exported WebP paths or ZIP path
- caveats / rejected attempts

# Shared output checks

Use this for lightweight local QA, or route to `visual-review-gate` for independent review.

## Universal

- Output exists and is attachable.
- Artifact type matches the request.
- Source/subject identity is preserved where required.
- No unwanted readable text, logos, watermarks, or signatures.
- Provider/model fallback was rejected unless approved.
- Original source image remains unchanged.

## Sticker packs

- Source sheet is visually inspected before export.
- Actual provider/model and size match the request; unapproved fallback is rejected.
- Looks like a real Telegram/emote pack and the curated good 4x4 examples.
- Exactly one large sticker candidate per cell; no nested mini-sheets or multiple thumbnails in a cell.
- Same subject and consistent scale across cells.
- Strong expression variety with simple readable props/effects.
- No copied official/fan sticker poses.
- No readable text, logos, watermarks, signatures, or baked-in numbering.
- Enough gutter for clean grid split; no hair/props/borders cross cell boundaries.
- Exported stickers are correct size/format and come from an accepted sheet.

## Avatar variants

- Recognizable at small size.
- Core face/hair/glasses/outfit/motif anchors stay fixed.
- Variant axis is readable but not noisy.
- Square crops/exports are deterministic.

## Character sheets

- Main view, supporting views, expressions, palette, and detail blocks are useful.
- Same character across panels.
- Generated sheet has no trusted text; readable notes live in PDF.
- PDF page 1 is art; page 2 is notes unless user asks otherwise.

## Brand marks

- Works at 32px/64px.
- Has simple silhouette and monochrome path when needed.
- Generated draft is not called final logo.
- SVG/vector final is rendered and visually compared.
- Exact text is manually rendered, not generated.

---
name: character-sheet-studio
description: "Create reusable character sheets from an image, description, or both. Use for reference/style-bible hybrid sheets, turnarounds, expression sheets, pose sheets, and PDF character dossiers for future avatar/sticker consistency."
---

# Character Sheet Studio

Make a reusable character reference package: art-only sheet first, readable PDF dossier second.

Read first:
- `../shared/references/request-routing.md`
- `../shared/references/identity-anchors.md`
- `references/character-sheet-examples.md`
- `../shared/references/generation-policy.md`
- `../shared/references/output-checks.md`
- `../shared/references/finalization-policy.md`

## Defaults

- Source priority: image > image + notes > description-only.
- Default sheet: **reference/style-bible hybrid**.
- Generate with `openai/gpt-image-2`, explicit `size="3840x2160"`.
- If OpenAI fails, retry once at `size="2048x1152"`; reject other providers unless approved.
- Do not ask the image model to write labels/text.

## Workflow

1. **Write the character brief**
   - Convert source into: name/title, role, setting, personality, visual premise, design logic.
   - Add 5-8 subject identity anchors using `identity-anchors.md`, including forbidden drift.
   - If source identity is uncertain or fandom/anime/game-looking, follow `request-routing.md` and use `character-source-lock` when needed.

2. **Choose one sheet type**
   - `reference/style-bible hybrid` default: main full-body, smaller views, expressions, palette, accessory/detail blocks.
   - `turnaround`: strict front/side/back/3/4.
   - `expression`: 8-12 bust emotions.
   - `pose`: 6-8 action/body-language poses.

3. **Generate one art-only sheet**
   - Call `image_generate` with explicit `model="openai/gpt-image-2"` and size above.
   - Verify provider/model using `generation-policy.md`.
   - Keep layout spacious and text-free.

4. **QA simply**
   - Same character across panels.
   - Required anchors are visible.
   - Useful views/expressions/palette/accessories.
   - No readable text/logos/watermark/stray typography.
   - Regenerate or report caveat for major drift.

5. **Build the PDF dossier**
   - Brief markdown may include headings: `# Character brief`, `## Key visual elements`, `## Pose and expression notes`, `## Outfit and accessories`, `## Palette and materials`, `## Consistency rules / forbidden drift`. The PDF builder omits consistency/forbidden-drift and QA sections by default so the delivered dossier stays readable and client-facing.
   - Save art sheet, preview, and brief markdown.
   - Use `scripts/build_character_dossier_pdf.py`, e.g. `python3 scripts/build_character_dossier_pdf.py --name "Name" --brief-md brief.md --sheet sheet.jpg --output dossier.pdf`.
   - PDF default: page 1 full art sheet, page 2 readable notes.
   - Do not include QA notes in the final PDF unless asked.

## Prompt skeleton

```text
Create a reference/style-bible hybrid character sheet. Tool params: model=openai/gpt-image-2, size=3840x2160.
Character brief: [name/title, role, setting, personality, visual premise, design logic].
Identity anchors: [5-8 required anchors plus forbidden drift].
Panels: large main full-body view; smaller front/side/back or 3/4 views; 3-6 bust expressions; palette swatches; accessory/detail blocks.
No readable text, labels, captions, logos, watermark, signatures, or typography inside the generated image.
```

## Small modes

- **Avatar crop**: after an accepted character sheet, crop the main bust/head or generate one simple square portrait from the locked brief. Export deterministically to platform size.
- **Cleanup/export**: crop, resize, convert, and PDF packaging belong here when tied to a character sheet. Preserve the original image and avoid semantic edits unless requested.

## Report

Return provider proof, art sheet path, preview path, brief path, final PDF path, and caveats/rejected attempts.

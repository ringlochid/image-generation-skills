---
name: brand-mark-studio
description: Create logos, app icons, favicons, and compact brand marks. Use for brand identity exploration or production icon/logo exports. Image generation is for drafts; SVG/vector/raster finalization is deterministic.
---

# Brand Mark Studio

Create brand marks without pretending raw generated images are production logos.

Read first:
- `../shared/references/request-routing.md`
- `../shared/references/generation-policy.md`
- `../shared/references/output-checks.md`
- `../shared/references/finalization-policy.md`
- `../shared/references/identity-anchors.md`
- `references/brand-mark-rules.md`
- `../shared/references/vectorization-qa.md` when producing SVG/vector finals

Required local tools for full vector QA/export: `node`, `python3`, `sharp`, `pixelmatch`, and `svgo`. Optional tracing path also uses `pngjs` and `imagetracerjs`.

## Workflow

1. Clarify brief: name, audience, style, colors, required text, forbidden motifs, target platform.
2. Choose mark type: symbol, wordmark, lettermark, combo mark, app icon, favicon.
3. Classify complexity using `brand-mark-rules.md`: simple SVG-final, complex raster-final, or complex SVG-simplification.
4. Generate 2-4 draft directions with `openai/gpt-image-2`; reject garbled text or noisy marks.
5. Select one direction.
6. Finalize deterministically:
   - SVG-final: rebuild/trace, render with `../shared/scripts/render_svg_to_png.sh`, QA with `../shared/scripts/logo_qa.sh`, optimize, export PNG sizes with `../shared/scripts/export_icon_pack.py`.
   - Complex raster-final: polish selected raster and export deterministic sizes with `../shared/scripts/export_icon_pack.py` when square.
   - SVG-simplification: create a clearly labeled simplified SVG reinterpretation.
7. Review: 32px readability, silhouette, monochrome, dark/light background, requested platform sizes.

## Hard rules

- Raw AI logo output is exploration, not final.
- Do not promise faithful SVG for complex generated geometry unless doing the long rebuild loop.
- Final SVG must be rendered and visually compared before delivery.
- Exact text is manual SVG/HTML/text rendering.
- Simple beats clever for favicons.

## Prompt skeleton

```text
Create [N] brand mark draft directions. Tool params: model=openai/gpt-image-2, size=[target].
Brief: [product/name/audience].
Mark type: [symbol/app icon/wordmark/etc].
Style: [simple geometric / friendly / technical / premium].
Constraints: [colors, motifs, forbidden motifs, no generated text unless exploration].
```

## SVG final command example

Run from `brand-mark-studio/` after selecting `draft.png` and creating or tracing `final.svg`:

```bash
../shared/scripts/trace_png_to_svg.mjs draft.png final.svg posterized2
../shared/scripts/render_svg_to_png.sh final.svg qa/final-rendered.png 1024x1024
../shared/scripts/logo_qa.sh draft.png final.svg qa 1024x1024
../shared/scripts/export_icon_pack.py qa/final-rendered.png exports
```

If rerunning into the same paths, pass `--force` only after confirming overwrite is intended.

## Report

Return provider/model proof for each draft, selected draft path, final asset paths, render/QA proof, export pack path, caveats, and whether the final is faithful SVG, simplified SVG, or raster-final.

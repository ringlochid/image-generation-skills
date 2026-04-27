# Brand mark rules

## Complexity classes

### Simple SVG-final

Use for simple, stable geometry: circles, dots, rounded rectangles, simple shields/badges, one clear silhouette, 1-3 major paths. Output: generated draft + clean SVG + rendered PNG + QA/export pack.

### Complex raster-final

Use when the draft depends on complex generated geometry: organic curves, many small internal objects, painterly gradients/textures, detailed leaves/hair/characters, or mixed circuits/organic forms. Output: polished raster asset + deterministic raster exports. Do not promise faithful SVG.

### Complex SVG-simplification

Use when the user wants SVG for a complex draft. Output is a simplified reinterpretation unless the user approves a long manual anchor-lock rebuild loop.

## SVG/vector QA

Required loop for SVG finals:

1. Select generated PNG draft.
2. Rebuild/trace SVG.
3. Render SVG to PNG.
4. Compare render to selected draft.
5. Inspect paths/colors/layering/small-size result.
6. Revise until faithful enough, intentionally simplified, or explicitly accepted as a new direction.

Check:

- canvas/background normalization
- silhouette and centering
- major path/stroke alignment
- palette preservation
- layer ordering
- hairline gaps, speckles, melted geometry, broken paths
- 32px/64px readability
- monochrome usability when required

Exact text belongs in SVG/HTML/manual rendering, not generated pixels.

## Raster-final definition

A raster-final means:

- the selected PNG/WebP draft is preserved as the visual source
- a normalized master is created in the requested canvas/aspect
- PNG/icon exports are produced deterministically
- no faithful-vector claim is made
- small-size previews are inspected before delivery

Use SVG-final only when the mark is simple enough to rebuild without lying about fidelity: roughly <=3 major shapes, <=5 colors, and no texture/painterly detail.

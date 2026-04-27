# Vectorization QA for logos/icons

Auto-trace is an intermediate, not a final-quality guarantee.

## Common failure modes

- **Abutting-path hairlines**: adjacent traced shapes touch edge-to-edge and renderer antialiasing shows seams.
- **Speckle paths**: source texture/noise becomes many tiny SVG paths.
- **Broken/dotted strokes**: a clean line becomes separated blobs or holes.
- **Melted pixels**: square pixel motifs become rounded organic shapes.
- **Palette collapse/drift**: trace reduces colors too aggressively or shifts the perceived palette.
- **Bloated fidelity**: a detailed trace is visually close but produces a huge SVG that is hard to edit or optimize.

## QA rule

A lower pixelmatch number is not enough. Prefer the SVG that is visually stable, editable, and production-clean.

## Recommended loop

1. Start from lossless PNG draft when possible.
2. Try a bounded/geometric trace first (`posterized2` worked better than `smoothed` for MossByte).
3. Render SVG to PNG.
4. Inspect draft/render/diff/overlay.
5. Reject traces with hairlines, broken strokes, speckle, or melted geometry.
6. Hand-rebuild main shapes when a trace is close but not clean:
   - rounded tile/container as simple rect/path
   - smooth organic mark as a small number of clean paths
   - pixel motifs as exact `<rect>` elements
   - highlights/stems as controlled strokes or filled paths
7. Rerun render/diff QA.
8. Document intentional simplification if final SVG diverges from generated draft.

## Production preference

For logos and app icons, a slightly simplified hand-cleaned SVG is usually better than a pixel-faithful noisy trace.

# Finalization policy

Generated images are drafts or art plates. Final deliverables should be deterministic when text, sizes, packaging, or vector geometry matter.

- Preserve original inputs.
- Save generated art separately from final exports.
- Keep outputs under a run/output directory unless the user asked for another path.
- Do not overwrite source files.
- Add readable text in PDF/HTML/SVG/layout tools, not generated pixels.
- Verify provider/model before accepting model-specific outputs.
- Export requested sizes with scripts/tools after generation.
- Write `run-manifest.md` for production/test runs; see `run-manifest.md`.
- Report rejected attempts and caveats separately from final artifacts.

Common defaults:

- Character sheet: art-only image + deterministic PDF dossier.
- Sticker pack: accepted contact sheet + deterministic grid split to 512 WebP.
- Avatar variants: accepted contact sheet + deterministic square crops/resizes.
- Brand mark: generated draft + deterministic SVG/raster/vector export path.

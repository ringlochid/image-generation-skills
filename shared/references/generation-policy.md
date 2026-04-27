# Shared generation policy

Default route: OpenClaw `image_generate` with explicit `model="openai/gpt-image-2"`.

## Generation contract

- Pass model explicitly.
- Pass size/aspect explicitly when size matters.
- Verify returned provider/model before accepting output.
- Reject fallback provider output unless the user approved fallback.
- Keep generation separate from deterministic export, PDF, SVG, crop, or resize steps.

## Provider proof

Capture in `run-manifest.md` or final report:

- requested model and size/aspect
- returned provider/model from tool output when exposed
- output path(s)
- image width/height and mime/type when inspected
- fallback attempts/rejections and reasons

For OpenAI-only work, accept only `openai/gpt-image-2` output unless fallback was explicitly approved.

## Privacy / external API boundary

- Preserve original inputs.
- Do not upload private/person/child/client/workplace images unless the user explicitly asked for generation/recognition with that image.
- Do not route private images through copied community/external API scripts without explicit approval.
- Avoid unnecessary metadata and source copying.

## Copyright / trademark boundary

- Use style grammar, not exact protected character/sticker/logo art.
- Do not copy official/fan sticker poses or assets.
- Do not reproduce trademarks/logos unless the user owns or explicitly requests them; flag caveats.

## Classify before generating

1. Artifact type: sticker, avatar, character sheet, brand mark.
2. Finality: exploration draft vs production final.
3. Precision: exact text/geometry/export sizes vs loose visual direction.
4. Consistency: single image vs coherent set/series.
5. Source risk: image/persona/fandom identity, privacy, external API sensitivity.
6. Route: image generation vs deterministic SVG/HTML/layout/image processing.
7. Text load: text-heavy vs mostly visual.
8. Export specificity: exact deliverable spec vs draft/preview.

## Common sizes

- Sticker 4x4 sheet: `2048x2048`; do not use 2x2 batches unless the user explicitly approves.
- Avatar 2x2 sheet: `2048x2048`.
- Character sheet: `3840x2160`; retry once at `2048x1152` if OpenAI fails.
- Brand draft: choose square or wide based on mark/app-icon target; exact exports happen after selection.

## Hard rules

- Do not silently switch away from GPT Image 2 when requested.
- Do not rely on image generation for exact readable text.
- Do not treat raw generated logos as production logos.
- Inspect actual output before delivery.

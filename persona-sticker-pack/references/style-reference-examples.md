# Curated style reference examples

Use these images as **style-only** references when generating sticker packs. They are examples of the target pack feel Leo prefers; do not copy their character identities or exact poses.

## Local assets

Use one of these from `../assets/style-examples/`:

- `good-white-halo-4x4.png` — strongest overall grammar: one large sticker per cell, clean outline, expressive bust/chibi poses.
- `good-red-4x4.jpg` — strong reaction vocabulary and prop grammar.
- `good-blonde-4x4.jpg` — good soft anime pack consistency.
- `good-white-sword-4x4.jpg` — useful for fantasy/anime character consistency.
- `generic-sticker-style-grid-768.png` — compact non-IP fallback style reference.

## What to borrow

- 4x4 contact-sheet grammar.
- One large sticker candidate per cell; never nested mini-sheets.
- Big head / tiny torso / bust-to-half-body framing.
- Thick outline plus white die-cut border.
- Clear expressive faces and small simple props.
- Consistent scale across all cells.
- Enough blank gutter so each cell can be cut cleanly.

## What not to borrow

- The reference characters' hair, outfit, colors, halo, accessories, or exact poses.
- Any text, logos, watermarks, signatures, or source-specific marks.
- Over-tight crops that make export/cutting hard.

## Preferred generation setup

Pass:

1. the user's image as the **identity reference**
2. one curated example above as the **style reference**
3. optionally `telegram-sticker-examples.md` from this directory as source grammar if no visual style ref is available

Operational note: copy bundled style assets to an allowed media/work output path before sending them to `image_generate`; direct skill asset paths may be outside the tool's allowed media boundary.

State the separation in the prompt: identity image controls subject; style image controls crop, outline, scale, grid, expression grammar, and gutter spacing only.

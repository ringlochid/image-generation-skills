# Source lock checklist

Use only when the quick workflow is uncertain.

## Recognition prompt

Ask an image-capable model, preferably `google/gemini-3-flash-preview`:

> Identify the named anime/game/fandom character if recognizable. Return character name, franchise/source, and 3-5 visual clues. Say uncertain if not recognizable.

## Sanity check

Before accepting a candidate, compare it to the avatar:

- hair color/length/style
- eye color/shape
- outfit or variant explanation
- distinctive accessories, props, badges, halos, weapons
- related-character cues that could mislead recognition

Accept high confidence only when distinctive traits match and source pages confirm them.

## Fallback Brave/web searches

Use the strongest anchors. Avoid broad queries like `blonde anime girl` unless nothing else exists.

Useful patterns:

- `<candidate> <franchise> wiki gallery sprite sticker`
- `<franchise> <hair color> <accessory> <outfit>`
- `"<distinctive accessory>" "<eye color>" anime character`
- exact visible text/logo/badge terms

Brave helps verify candidate names and find source pages. It is not reverse image upload.

## Source target

Keep it to 3 sources unless needed:

1. profile/source page for identity
2. gallery/sprite/asset page for visual anchors
3. sticker/pose page only for expression conventions

## Lock note rules

- User correction outranks model/search guesses.
- Separate identity lock from adjacent context.
- Record mismatches, not just matches.
- If confidence stays low, say unknown/OC-style and ask for a clue.

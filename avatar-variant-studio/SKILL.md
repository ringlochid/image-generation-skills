---
name: avatar-variant-studio
description: "Create square avatar/profile-picture variants while preserving a persona or character identity. Use for seasonal avatars, mood/status avatars, workspace/project-themed profile images, and small profile-picture sets from an existing avatar, character sheet, or persona brief."
---

# Avatar Variant Studio

Create profile-picture variants, not sticker packs or full character sheets.

Read first:
- `../shared/references/request-routing.md`
- `../shared/references/identity-anchors.md`
- `../shared/references/generation-policy.md`
- `../shared/references/output-checks.md`
- `../shared/references/finalization-policy.md`

## Defaults

- Source priority: avatar image > character sheet > persona brief.
- Generate a small 2x2 contact sheet first.
- Use `openai/gpt-image-2` with explicit square size `2048x2048`.
- Reject fallback providers unless approved.
- Export selected cells deterministically to square avatar sizes.

## Workflow

1. Lock subject identity anchors using `identity-anchors.md`; include forbidden drift.
2. Pick one variant axis: mood, season, workspace, project, event, or status.
3. Generate 4 subtle square bust variants in one 2x2 sheet at `2048x2048`. Require no visible panel borders, black cell lines, cross-shaped dividers, or shared cross background; each cell should read as an independent square avatar crop.
4. Review small-size recognizability and identity preservation.
5. Export selected cells to requested sizes, preserving the original source. For a 2x2 2048 sheet, cells are 1024x1024: top-left `(0,0)`, top-right `(1024,0)`, bottom-left `(0,1024)`, bottom-right `(1024,1024)`. Use an inset crop to cut away any generated cell-boundary pixels: `../shared/scripts/export_contact_sheet_grid.py avatars.png exports --grid 2 --prefix avatar --format jpg --sizes 512,1024 --inset 16 --zip`.

## Example

For Orin: identity anchors are dark/purple hair, sharp glasses, calm operator expression, dark techwear, restrained apple accent. Variant axis could be calm default / focused coding / warm assistant / night ops.

## Prompt skeleton

```text
Create a 2x2 contact sheet of square profile avatar variants. Tool params: model=openai/gpt-image-2, size=2048x2048.
Identity anchors: [stable anchors].
Variant axis: [theme/mood/status].
Each cell: square bust/profile-picture composition, clean independent background, readable at small size, same character identity.
Do not draw panel borders, black cell lines, cross dividers, shared cross-shaped background, captions, letters, logos, watermark, or major identity changes. Keep the subject away from cell edges so a small inset crop can remove boundary artifacts safely.
```

## Report

Return provider proof, run-manifest path, contact sheet path, exported avatar paths, and caveats/rejected attempts.

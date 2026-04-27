---
name: visual-review-gate
description: "Review generated visual artifacts before delivery. Use for QA/review gates on sticker packs, avatar variants, character sheets, brand marks, cleanup edits, and final image/PDF exports when identity, text, provider fallback, layout, or production readiness matters."
---

# Visual Review Gate

Give a verdict before delivery: pass, pass with caveats, reject, or needs retry.

Read first:
- `../shared/references/output-checks.md`
- `../shared/references/generation-policy.md`
- `../shared/references/finalization-policy.md`

## Workflow

1. Identify artifact type: sticker pack, avatar, character sheet, brand mark, PDF/export, or explicitly provided cleanup/edit artifact.
2. Check requested constraints: identity, size, provider/model, no text/logos, layout, export format.
3. Inspect the actual output image/PDF/render, not just file existence.
4. For sticker packs, inspect the source sheet before export and reject nested mini-sheets, tiny subjects, boundary crossings, wrong provider/size, or weak identity.
5. Return the smallest useful verdict with blockers, caveats, and retry/export direction.

## Verdict criteria

- `PASS`: constraints met; no blockers.
- `PASS WITH CAVEATS`: usable if caveats are disclosed.
- `REJECT`: identity/text/provider/export blocker.
- `NEEDS RETRY`: generation can likely fix the blocker.

## Output

- Verdict:
- Artifact type:
- Pass checks:
- Blockers:
- Caveats:
- Recommended next step:

---
name: character-source-lock
description: Identify and lock an anime/game/fandom character source from an image before stickers, avatars, or character sheets. Use when a provided avatar/image may depict or derive from an existing character.
---

# Character Source Lock

Goal: produce a small, source-backed identity lock. Do not over-research, overclaim, or use adjacent characters as the identity.

## Workflow

1. **Extract anchors first.** List hair, eyes, outfit, accessories, props, palette, silhouette, visible marks/text. No guessing yet.
2. **Privacy gate.** If the image may be private, a real person, a child, workplace/client asset, or not clearly intended for external analysis, ask before provider recognition; use local anchor extraction until approved.
3. **Recognize with Gemini if available.** Use `google/gemini-3-flash-preview`; ask for character, franchise, and 3-5 visual clues. If unavailable/uncertain, skip to fallback search.
4. **Sanity-check the candidate.** Compare Gemini’s clues against the actual avatar. Accept only if distinctive traits match; record mismatches as variant drift.
5. **Fallback search.** If recognition fails or fails sanity check, use Brave/web search with the strongest anchors and candidate terms. Brave is text-query search, not reverse image upload.
6. **Verify sources.** Treat model/search results as leads. Open source pages before locking.
7. **Write the lock.** Keep it short: verdict, visual anchors, sanity check, source URLs, candidate table, generation constraints.

## Minimal sources

Default target: **3 sources**.

1. Character profile/source page.
2. Image/gallery/sprite/asset page.
3. Sticker/pose page only if expression conventions matter.

Add more only if candidates conflict or confidence is low.

## Confidence rule

- **High:** distinctive avatar traits match; source pages confirm name/franchise/visuals.
- **Medium:** many traits match, but outfit/style is variant/fanart/OC-like.
- **Low:** mostly color/hair similarity, weak sources, or multiple plausible candidates.

If low, label as unknown/OC-style and ask for a franchise clue.

## Do not

- Do not accept name-only recognition.
- Do not treat adjacent characters as identity.
- Do not copy official/fan sticker art.
- Do not depend on Google Lens/browser by default; use browser/Lens only when the user asks for identification or automated Gemini/text-search is inconclusive and upload is allowed.

## Output

```markdown
# Character source lock: <name or unknown>

## Verdict
- Primary lock:
- Confidence:
- Adjacent context:

## Visual anchors
- ...

## Recognition sanity check
- Candidate clues:
- Avatar matches:
- Mismatches / variant drift:

## Source URLs
- ...

## Candidates
| Candidate | Matches | Mismatches | Confidence |
|---|---|---|---|

## Generation constraints
- preserve ...
- avoid ...
```

Read `references/examples.md` for Hikari/Mythra, Homura/Pyra, and Orin/Yuuka patterns. Read `references/source-lock-checklist.md` only when recognition/search is uncertain. Read `references/browser-image-search.md` only for explicit browser/Lens escalation.

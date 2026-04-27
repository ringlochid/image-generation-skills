# Request routing

Classify before generating. Keep leaf skills small; route shared concerns here.

- Sticker pack / reaction set / sticker sheet generation from an image or character description -> route to `persona-sticker-pack`.
- Native Telegram sticker catalog/search/send/reuse by file_id -> route to `telegram-sticker-workflow`, not generation.
- Existing sticker/image crop/resize/WebP export only -> route to `sticker-export`, after a sticker sheet has already been accepted.
- Source/identity uncertain, fandom/anime/game-looking, or existing character risk -> run `character-source-lock` first.
- Need independent QA/review of a generated artifact -> run `visual-review-gate` or use `output-checks.md` locally for lightweight review.
- Need provider/model strictness, fallback handling, exact size, or deterministic finalization -> read `generation-policy.md`.
- Need final packaging/export/PDF/vector behavior -> use the leaf skill's script or deterministic shared scripts, not image generation text.

Do not make sticker, avatar, character-sheet, and brand skills each re-explain source locking or review gates. They should call out when to use these shared lanes.

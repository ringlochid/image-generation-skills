# Run manifest

For production or test runs, write `run-manifest.md` in the run directory.

Include:

- Request / goal
- Source input paths
- Prompt or prompt file path
- Provider proof: requested model, returned provider/model, output path(s), width/height/mimeType if available, fallback attempts/rejections
- Accepted artifact paths
- Rejected artifact paths and reasons
- Deterministic export commands/scripts used
- QA/review verdict and caveats

Accept OpenAI-only outputs only when provider/model proof shows the requested OpenAI model or the user approved fallback.

## Fill-in template

````md
# Run manifest

## Request
[User goal and deliverable]

## Sources
- identity/source image: `[path]`
- style/reference image: `[path]`

## Generation
- requested model: `openai/gpt-image-2`
- requested size/aspect: `[size or aspect]`
- returned provider: `openai`
- returned model: `gpt-image-2`
- output paths:
  - `[path]` — `[width]x[height]`, `[mimeType]`
- fallback attempts/rejections:
  - none
  - or: `[provider/model]` rejected because fallback was not approved

## Accepted artifacts
- `[path]` — `[reason accepted]`

## Rejected artifacts
- `[path]` — `[identity drift / bad text / wrong provider / export failure / etc.]`

## Deterministic exports
```bash
[exact command]
```

## QA verdict
`PASS | PASS WITH CAVEATS | REJECT | NEEDS RETRY`

Caveats: [none or concise notes]
````

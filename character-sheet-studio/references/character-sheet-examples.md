# Character sheet examples and content patterns

Use this reference for **what good looks like**. Keep the main skill focused on how to produce it.

## Character brief layer

Before generation, convert the idea or image into a compact persona/design brief. This is the thinking layer that prevents generic outputs.

Include:

- working name or title
- role/archetype
- setting/world context
- personality and body language
- visual premise / silhouette
- outfit/material logic
- required anchors
- optional motifs
- forbidden drift

Keep the brief short enough to fit into the generation prompt. The generated sheet should show the brief visually; readable prose/labels can be added afterward.

## Production-useful default

A good default character sheet should combine visual reference and design notes:

- one strong full-body color pose
- smaller front / side / back or 3/4 views
- at least 3 bust/head expressions
- palette swatches
- accessory / prop / outfit detail callouts
- short character description and role/personality notes

The visual sheet may leave blank areas or visual blocks for labels, but generated text should not be trusted. Add readable labels/descriptions afterward in the PDF dossier by default.

## Strong example pattern: Orin-style sheet

Good for future generation because it includes:

- main character identity and role
- facial anchors and expression variants
- outfit layers and accessory callouts
- palette blocks
- props tied to character function
- personality / demeanor notes
- required motifs vs optional details

Weakness to avoid: do not rely on generated tiny text; reproduce labels deterministically afterward.

## Industry / school reference pattern

A typical animation/design challenge sheet often asks for:

- at least one full-body illustration in color
- at least two secondary full-body poses
- at least three bust/head expressions
- a short paragraph describing the character

Useful layout patterns:

- large hero pose on one side, supporting views around it
- expression row along the bottom
- palette and material swatches near the outfit
- prop/accessory closeups near the relevant body area
- blank gutter/negative space so the sheet is readable

## Sheet types

### Reference/style-bible hybrid — default

Use when the user says “make a character sheet” without more detail.

Include:

- large main full-body view
- smaller front/side/back or 3/4 views
- 3-6 bust expressions
- palette swatches
- accessory/detail blocks
- optional blank space for deterministic labels

### Turnaround

Use for modeling, outfit construction, or strict silhouette reference.

Include:

- front, side, back, and 3/4 views
- neutral pose
- minimal expressions/props
- high consistency over personality

### Expression sheet

Use when face/personality consistency matters.

Include:

- 8-12 bust/head expressions
- same face structure and hair anchors
- no full-body crowding unless requested

### Pose/action sheet

Use when body language or action vocabulary matters.

Include:

- 6-8 poses
- consistent outfit and silhouette
- props/actions relevant to the character role

## QA questions

- Could another artist/model redraw this character from the sheet?
- Are the required identity anchors visible more than once?
- Are palette and accessories obvious?
- Are expressions/poses useful for future stickers or avatars?
- Is any generated text unreadable or unnecessary?
- Is the sheet too cluttered to use as reference?

## Final PDF dossier

Use PDF, not generated image text, for the finished readable character sheet/dossier. Default PDF structure: page 1 is the full art sheet; page 2 is readable notes.

Include:

- Page 1: full art-only visual sheet
- Page 2: character name / working title, short description paragraph, key visual elements, pose/expression notes, outfit/accessory notes, and palette/material notes

Do not include QA notes or consistency/forbidden-drift rules in the final PDF by default. Keep those in the brief markdown unless the user asks to expose them. Do not create SVG labels by default. Only make a labeled image/SVG if the user explicitly asks for labels on the image itself.

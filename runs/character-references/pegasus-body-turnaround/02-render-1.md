---
set: character-references
shot: pegasus-body-turnaround
attempt: 1
stage: 02_render
status: approved
verdict: accepted
generated: 2026-10-15T14:28:57+00:00
sources:
  - world/characters/pegasus.md
  - world/references/pegasus-flight.md
  - world/references/pegasus-flight.png
  - runs/character-references/pegasus-body-turnaround/02-image-1.png
---

# Pegasus default full-body 4-view turnaround sheet, render 1

## Prompt as sent

A strictly two-dimensional ukiyo-e woodblock-print character turnaround sheet on an aged speckled matte parchment background, showing the exact same immortal white winged stallion (Pegasus) standing in 4 clean orthographic views arranged in a single horizontal row from left to right: (1) straight-on full front view, (2) full left profile view facing left, (3) full right profile view facing right, and (4) straight-on full rear back view. In every view Pegasus has a pure white to pale parchment-silver coat, a sculpted classical equine head with a dark slate-charcoal muzzle and nostrils, upright pointed ears, a soft pale white-silver mane and short wispy forelock, a full flowing white-silver tail reaching the hocks, slender tapering legs with four dark charcoal-grey hooves, and a massive pair of shoulder-mounted multi-tiered feathered wings in white and pale silver-grey rising symmetrically from the withers. Across his back and upper flanks in every view he wears his exact default tack: an intricate embroidered Viking tribal-tattooed saddle rendered as luminous warm-gold energetic light with Nordic knotwork patterns, paired with worn brown-leather dispatch saddlebags resting on both flanks behind the wing roots and holding rectilinear cord-bound parchment folders. Distinct carved dark ink keyline contours, flat opaque color planes, stepped tonal areas, matte paper finish. No text, no labels, no numbers, no captions, no watermarks, no borders, no black background, and no 3D realism.

## Tool metadata

- model: `gpt_image_2_5` (`variant: sunburst`)
- provider: `Higgsfield` (`mcp__higgsfield__generate_image_batch`)
- job: `b3c9360a-3f1c-415c-bcf7-5f08a72c666f`
- conditioned on: `925ff4e3-78fb-4947-9efa-84cb64bb0841` (`world/references/pegasus-flight.png`)
- aspect ratio requested: `16:9`
- aspect ratio returned: `16:9`
- resolution: `1344×752`
- quality: `low` (`resolution: 1k`)
- seed: `not exposed`
- cost preflight: `0.25 credits`
- file: `runs/character-references/pegasus-body-turnaround/02-image-1.png` (`PNG`, `2109549` bytes)
- sha256: `8cc2ca79b6323b2d1ea45645481fb2dd4ac2fb71d9a0bc49e8b0d5ea698e4b5d`
- generated: `2026-10-15T14:28:57+00:00`

## Findings

- `holds`: all 4 requested standing views (1: front, 2: left profile facing left, 3: right profile facing right, 4: rear back view) are arranged in a clean horizontal row on aged speckled parchment in 2D ukiyo-e woodblock-print style.
- `holds`: white/pale parchment-silver coat, dark slate-charcoal muzzle (in front/profile views), four dark charcoal-grey hooves, flowing mane and hock-length tail (in profile/rear views), and symmetrical shoulder-mounted multi-tiered feathered wings match `world/characters/pegasus.md`.
- `holds`: default tack (`default`) appears across the views with ornate warm-gold Nordic/Viking knotwork saddle and chest band plus worn brown-leather dispatch saddlebags holding bundled parchment folders/codices.
- `holds`: no text, labels, numbers, captions, or watermarks appear.

## Drift notes

None. Ready for operator visual review (`accept` or `drift`) to install into `world/references/pegasus-body-turnaround.png` + `world/references/pegasus-body-turnaround.md`.

---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 1
stage: 03_file
status: approved
generated: 2026-10-03
sources:
  - 02-render-1.md
  - 01-spec-1.md
---

# hermes-sky-bridges-and-passages, sidecar

Reproduce this shot from this file. Explain it from the spec it names.

- Image: `02-image-1.png` sha256 `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
- Spec: `01-spec-1.md`
- Render record: `02-render-1.md`
- Characters in frame: Hermes
- Verdict: accepted

## Prompt as sent

Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, flat color blocking, matte textured paper, and an aged speckled parchment background; antiquarian, woodblock-inspired, Hermetic, monumental, weathered, gold-lit. Do not render realistic academic painting, dimensional painterly modelling, anime, UI, readable lettering, captions, logos, watermarks, borders, code, screens, neon blue, cyan, magenta, bright red, grass green, crystals, floating terrain, cosmic sky, science-fiction technology, modern clothing, or generic-superhero imagery.

Hermes is tall and statuesque with an athletic lean heroic build, broad defined shoulders, athletic powerful limbs, and large robust hands. His angular high-cheekboned face has a strong square jaw, straight classical nose, luminous amber-golden eyes, warm sun-baked bronze skin, freckles across the nose bridge and upper cheeks, and no facial hair. His short-to-medium thick coarse curls are warm golden-brown with lighter sun-bleached highlights. He wears the default outfit: antique-bronze winged helmet, charcoal-grey heavy-linen knee-length undertunic with parchment-sepia edge, dark-charcoal chlamys with antique-gold clasp, worn leather harness and belt, scratched bronze bracers and greaves, weathered winged sandals, and an aged gold/bronze twin-serpent winged caduceus.

Hermes strides in calm attentive focus across a series of grounded limestone viaducts that cross ravines between mountain ridges and plazas, running from Gateway Pavilion toward Crystal Citadel. Underfoot is weathered limestone paving. Warm-gold route light appears only in shallow carved stone channels and gateway thresholds. The passage has no floating islands, abyss-edge world, energy conduits, or mechanical bridge structure. Dusk gives amber, orange, and gold long shadows. A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus. Keep the bridges fully grounded and classical; preserve the golden-brown hair, charcoal-grey undertunic, and flat ukiyo-e print treatment. Gold is the sole active-power indicator.

## Tool metadata
- model: `openai/gpt-image-2.5-sunburst`
- request: see Prompt as sent
- aspect_ratio: requested `landscape`; applied `not exposed; backend omitted the enum`
- resolution: `1672×941`
- seed: `not exposed`
- file: `02-image-1.png` (PNG)
- generated: `2026-09-29T12:23:49-07:00`

## Drift carried into any motion made from this still

The verdict is `accepted`, so the still is usable. These three lines were
drifted at acceptance and remain true of the image, so `04_animate` inherits
them as facts to hold, not defects to fix:

- undertunic reads slate-grey, not the bible's charcoal-grey
- hair reads brown, not visibly warm golden-brown with sun-bleached highlights
- heraldic caduceus/sunburst banners appear on the dark wall at left

And one the operator accepted as `cannot see` at this scale: freckles, amber eye
color, nose shape, and square-jaw detail are too small to read in the wide
framing. A video model will invent them. See the motion spec's **What holds**.
---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 1
stage: 02_render
status: approved
verdict: accepted
generated: 2026-09-29T12:23:49-07:00
sources:
  - 01-spec-1.md
  - 02-image-1.png
---

## Prompt as sent

Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, flat color blocking, matte textured paper, and an aged speckled parchment background; antiquarian, woodblock-inspired, Hermetic, monumental, weathered, gold-lit. Do not render realistic academic painting, dimensional painterly modelling, anime, UI, readable lettering, captions, logos, watermarks, borders, code, screens, neon blue, cyan, magenta, bright red, grass green, crystals, floating terrain, cosmic sky, science-fiction technology, modern clothing, or generic-superhero imagery.

Hermes is tall and statuesque with an athletic lean heroic build, broad defined shoulders, athletic powerful limbs, and large robust hands. His angular high-cheekboned face has a strong square jaw, straight classical nose, luminous amber-golden eyes, warm sun-baked bronze skin, freckles across the nose bridge and upper cheeks, and no facial hair. His short-to-medium thick coarse curls are warm golden-brown with lighter sun-bleached highlights. He wears the default outfit: antique-bronze winged helmet, charcoal-grey heavy-linen knee-length undertunic with parchment-sepia edge, dark-charcoal chlamys with antique-gold clasp, worn leather harness and belt, scratched bronze bracers and greaves, weathered winged sandals, and an aged gold/bronze twin-serpent winged caduceus.

Hermes strides in calm attentive focus across a series of grounded limestone viaducts that cross ravines between mountain ridges and plazas, running from Gateway Pavilion toward Crystal Citadel. Underfoot is weathered limestone paving. Warm-gold route light appears only in shallow carved stone channels and gateway thresholds. The passage has no floating islands, abyss-edge world, energy conduits, or mechanical bridge structure. Dusk gives amber, orange, and gold long shadows. A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus. Keep the bridges fully grounded and classical; preserve the golden-brown hair, charcoal-grey undertunic, and flat ukiyo-e print treatment. Gold is the sole active-power indicator.

## Tool metadata

model: `openai/gpt-image-2.5-sunburst`
provider: `openrouter`
endpoint: `images/generations`
aspect request: `landscape`
aspect applied: `not exposed; backend omitted the enum`
resolution: `1672×941`
seed: `not exposed`
cost: `$0.03702`
total tokens: `1614`
file: `02-image-1.png`
sha256: `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
generated: `2026-09-29T12:23:49-07:00`

## Findings

- holds: massive grounded limestone viaducts span visible ravines between solid ridges and plazas, with shallow warm-gold carved channels.
- holds: no floating islands, abyss-only geography, mechanical bridge structure, energy conduit aesthetic, readable text, UI, or sci-fi technology are visible.
- holds: linework, flattened decorative color, and aged-paper texture support the ukiyo-e/woodblock direction.
- holds: Hermes has winged helmet, dark chlamys, caduceus, bracers, greaves, and winged sandals.
- drifted: undertunic reads slate-grey instead of the required charcoal-grey.
- drifted: hair reads brown rather than visibly warm golden-brown with sun-bleached highlights.
- drifted: heraldic banners carrying a caduceus/sunburst emblem introduce logo-like signage despite the no-logos guard.
- cannot see: freckles, amber eye color, nose shape, and square-jaw detail are too small to verify in this wide shot.
- holds: warm dusk illumination and a medium-wide/eye-level tracking view are present.

## Drift notes

A rerun should remove heraldic banners and lock hair plus undertunic color; retain the grounded bridge geography.

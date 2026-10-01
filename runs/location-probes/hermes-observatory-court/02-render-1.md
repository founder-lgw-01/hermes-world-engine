---
set: location-probes
shot: hermes-observatory-court
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

Hermes studies a central antique-bronze armillary sphere in calm attentive focus. The circular marble court is ringed by fluted columns and joined to Gateway Pavilion by a broad ground-level stone causeway. Underfoot is polished black marble with glowing gold concentric rings, abstract star points, and sun/moon reliefs only—no letters, numerals, or glyphs. Direct setting sun makes the court clear and brilliant. A full-body medium-wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus. Keep the chart paving abstract and non-linguistic; preserve the golden-brown hair, charcoal-grey undertunic, and flat ukiyo-e print treatment. Gold is the sole active-power indicator.

## Tool metadata

model: `openai/gpt-image-2.5-sunburst`
provider: `openrouter`
endpoint: `images/generations`
aspect request: `landscape`
aspect applied: `not exposed; backend omitted the enum`
resolution: `1672×941`
seed: `not exposed`
cost: `$0.01772`
total tokens: `969`
file: `02-image-1.png`
sha256: `6899a6d6e98c93550921f5b4f0a72a151249c34361f1746292089851ddb554fc`
generated: `2026-09-29T12:23:49-07:00`

## Findings

- holds: armillary sphere, circular black-marble court, fluted colonnade, and broad ground-level causeway are visible.
- holds: paving uses non-readable concentric rings, star points, and sun/moon reliefs; no letters, numerals, UI, logos, or watermarks are visible.
- holds: active light is warm gold; the architecture is grounded and classical, with no sci-fi technology, crystal forms, floating terrain, or cosmic sky.
- holds: distinct linework, flat decorative color treatment, and aged-paper texture support the ukiyo-e/woodblock direction.
- holds: Hermes has the winged helmet, dark chlamys, caduceus, bracers, greaves, and winged sandals.
- drifted: undertunic is visibly blue-grey rather than required charcoal-grey.
- holds: curls visible under the helmet read warm golden-brown.
- cannot see: freckles, amber eye color, nose shape, and square-jaw detail are too small to verify in this medium-wide view.
- holds: direct setting-sun illumination and a medium-wide slightly low viewpoint are present.

## Drift notes

Correct the undertunic color in any rerun; retain the print treatment and clear court geometry.

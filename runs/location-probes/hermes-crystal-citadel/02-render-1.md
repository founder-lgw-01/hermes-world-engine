---
set: location-probes
shot: hermes-crystal-citadel
attempt: 1
stage: 02_render
status: draft
verdict: ""
generated: 2026-09-29T12:23:49-07:00
sources:
  - 01-spec-1.md
  - 02-image-1.png
---

## Prompt as sent

Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, flat color blocking, matte textured paper, and an aged speckled parchment background; antiquarian, woodblock-inspired, Hermetic, monumental, weathered, gold-lit. Do not render realistic academic painting, dimensional painterly modelling, anime, UI, readable lettering, captions, logos, watermarks, borders, code, screens, neon blue, cyan, magenta, bright red, grass green, crystals, floating terrain, cosmic sky, science-fiction technology, modern clothing, or generic-superhero imagery.

Hermes is tall and statuesque with an athletic lean heroic build, broad defined shoulders, athletic powerful limbs, and large robust hands. His angular high-cheekboned face has a strong square jaw, straight classical nose, luminous amber-golden eyes, warm sun-baked bronze skin, freckles across the nose bridge and upper cheeks, and no facial hair. His short-to-medium thick coarse curls are warm golden-brown with lighter sun-bleached highlights. He wears the default outfit: antique-bronze winged helmet, charcoal-grey heavy-linen knee-length undertunic with parchment-sepia edge, dark-charcoal chlamys with antique-gold clasp, worn leather harness and belt, scratched bronze bracers and greaves, weathered winged sandals, and an aged gold/bronze twin-serpent winged caduceus.

Hermes strides in calm attentive focus along a weathered stone mountain road toward a monumental citadel carved into a grounded limestone ridge. Broad carved terraces and fluted gateway towers rise above the road. The main viaduct terminates at the lower limestone terrace. Warm-gold route light appears only in carved stone gateways and caduceus-like relief channels; there are no crystals, cool light, or translucent surfaces. Dusk brings amber, orange, and gold long shadows. A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus. Keep the citadel grounded limestone rather than crystal or sci-fi; preserve the golden-brown hair, charcoal-grey undertunic, and flat ukiyo-e print treatment. Gold is the sole active-power indicator.

## Tool metadata

model: `openai/gpt-image-2.5-sunburst`
provider: `openrouter`
endpoint: `images/generations`
aspect request: `landscape`
aspect applied: `not exposed; backend omitted the enum`
resolution: `1672×941`
seed: `not exposed`
cost: `$0.03706`
total tokens: `1622`
file: `02-image-1.png`
sha256: `495ece08d98de50f7f04bb27ea8f9cbe3882a175babf5873640304eb19a92890`
generated: `2026-09-29T12:23:49-07:00`

## Findings

- holds: citadel is grounded in a limestone mountain ridge with terraces, a stone road, a terminating viaduct, and warm-gold gateway/relief lighting.
- holds: no crystals, translucent surfaces, cool/cyan light, readable text, UI, sci-fi elements, or floating terrain are visible.
- holds: clean linework, restrained flat color fields, and aged-paper texture support the ukiyo-e/woodblock direction.
- holds: Hermes has winged helmet, dark chlamys, caduceus, bracers, greaves, and winged sandals.
- drifted: Hermes' curls appear dark brown rather than the specified warm golden-brown with sun-bleached highlights.
- drifted: undertunic appears grey-blue rather than charcoal-grey.
- drifted: the primary gateway towers are square pylons rather than fluted towers.
- cannot see: freckles, amber eye color, nose shape, and square-jaw detail are too small to verify in this wide shot.
- holds: warm dusk light and a low/eye-level wide composition are present.

## Drift notes

A rerun should lock hair, undertunic, and fluted tower geometry; preserve the grounded limestone massing.

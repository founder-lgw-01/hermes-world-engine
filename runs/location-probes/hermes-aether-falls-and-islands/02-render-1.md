---
set: location-probes
shot: hermes-aether-falls-and-islands
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

Hermes stands in calm attentive focus at the gateway of a Parthenon-style temple on a solid mossy stone promontory. A ground-fed waterfall descends from a limestone ridge into a mossy stone basin below. Continuous grounded terrain joins ridge, basin, and temple; no floating islands or suspended waterfall appear. Dawn rose-gold light enters the mist, while restrained warm-gold wayfinding light appears only at the temple gateway and caduceus. A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus. Keep waterfall geography continuous and grounded; preserve the golden-brown hair, charcoal-grey undertunic, and flat ukiyo-e print treatment. Gold is the sole active-power indicator.

## Tool metadata

model: `openai/gpt-image-2.5-sunburst`
provider: `openrouter`
endpoint: `images/generations`
aspect request: `landscape`
aspect applied: `not exposed; backend omitted the enum`
resolution: `1672×941`
seed: `not exposed`
cost: `$0.037015`
total tokens: `1613`
file: `02-image-1.png`
sha256: `7f6241461a7e925c5b6a3c0817365221dfeabc193d77ef5ff5cb107ba616518a`
generated: `2026-09-29T12:23:49-07:00`

## Findings

- holds: continuous grounded limestone ridge, waterfall, mossy basin, and solid temple promontory are visible.
- holds: dawn mist and restrained warm-gold illumination at the temple/caduceus are present.
- holds: no floating islands, suspended waterfall, cosmic sky, readable text, UI, or sci-fi technology are visible.
- holds: ink-like linework, flattened decorative color, and paper texture support the ukiyo-e/woodblock direction.
- holds: Hermes has winged helmet, dark chlamys, caduceus, bracers, greaves, and winged sandals.
- drifted: undertunic reads dark slate-grey rather than the specified charcoal-grey.
- holds: visible curls read light golden-brown beneath the helmet.
- cannot see: freckles, amber eye color, nose shape, and square-jaw detail are too small to verify in this wide shot.
- holds: full-body wide view with dawn low-angle illumination is present.

## Drift notes

A rerun should lock the undertunic color; preserve the grounded waterfall geography and dawn treatment.

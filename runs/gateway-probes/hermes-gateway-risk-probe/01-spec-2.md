---
set: gateway-probes
shot: hermes-gateway-risk-probe
attempt: 2
stage: 01_spec
status: approved
generated: 2026-09-29T12:52:32-07:00
sources:
  - runs/gateway-probes/hermes-gateway-risk-probe/00-brief.md
  - runs/gateway-probes/hermes-gateway-risk-probe/02-render-1.md
  - world/environment.md
  - world/style.md
  - world/characters/hermes.md
  - world/environment/core.md
  - world/environment/palette-and-light.md
  - world/environment/materials-and-wear.md
  - world/environment/forms-and-architecture.md
  - world/environment/locations/gateway-pavilion.md
  - _reference/spec-rules.md
  - _reference/drift-checklist.md
---

# Hermes gateway risk probe, spec 2

## World-input manifest

| Path | Selected role | SHA-256 |
|---|---|---|
| `world/environment.md` | environment index | `ba4a5b407524a04f0c61ede58121807570c7e1707fe866c56a967878462bf16a` |
| `world/style.md` | style rules | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` |
| `world/characters/hermes.md` | Hermes character bible | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` |
| `world/environment/core.md` | world identity and exclusions | `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a` |
| `world/environment/palette-and-light.md` | dusk palette and light | `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da` |
| `world/environment/materials-and-wear.md` | shared aging rules | `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5` |
| `world/environment/forms-and-architecture.md` | portal and architectural forms | `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5` |
| `world/environment/locations/gateway-pavilion.md` | Gateway Pavilion | `579f67e244acebe967f0aa8991b8f3aa7010e417c83b284628e85a715044bbd0` |
| `world/references/gateway-courtyard-01.md` | `palette-and-gateway-light`; `courtyard-materials`; `classical-directory-architecture`; `gateway-pavilion` | `cd1abdf2f1b3b15123dccf582144034d35bc3d806b589c5e63c98bee6b8439c2` |
| `world/references/gateway-courtyard-01.png` | selected reference image | `328dda4607314e643a9056c0300b5eb4eec23349bb9c5a5e92865f3579336ab9` |
| `world/references/hermes-face.md` | `hermes-default-face` | `4c9836c8b46ec2f179256cfb51376e31097be3a12737f1e12f303e400475a0e9` |
| `world/references/hermes-face.webp` | selected reference image | `bc9fc04ee5ef9c01673af2bf8db05c11f38a9f1f7c480a924185d84ce9d0d4e4` |

## Brief

- **Characters in frame:** Hermes only.
- **Action:** Hermes activates a grounded classical stone gateway with his caduceus. Warm-gold light appears only in the caduceus and gateway route; the route reads as physical architecture, never UI or science fiction.
- **Pose and expression:** Full-body, grounded threshold stance; caduceus upright in a firm large-hand grip; calm attentive focus, not combat or a generic-hero pose.
- **Wardrobe state:** Default.
- **Location:** Gateway Pavilion.
- **Time and weather:** Dusk; clear, dry air; warm amber, orange, and gold light with long shadows.
- **Must show/not show:** Preserve Hermes’s defined identity, classical grounded gateway, gold-only power, weathered materials, and ukiyo-e finish. Show no lettering, logos, UI, cool/neon colors, science-fiction imagery, crystals, floating terrain, cosmic sky, modern clothing, weapons, or generic-superhero treatment.

## Characters in frame

### Hermes

- **Silhouette and build:** Tall and statuesque; athletic/lean heroic figure; broad and defined shoulders; athletic, powerful defined limbs; substantial lean weight; large robust hands; winged helmet, winged sandals, vertically carried caduceus, and shoulder-fastened chlamys.
- **Face and hair visible in the medium-wide full-body view:** Angular, highly symmetrical, high-cheekboned face; warm sun-baked bronze skin; luminous amber/golden-orange eyes; thick dark-brown brows with a subtle arch; straight classical nose; full defined neutral lips; strong square jaw; freckles across nose bridge and upper cheeks; clean-shaven. Hair is short-to-medium, thick, coarse, highly curly, layered, wild, warm golden-brown with lighter sun-bleached highlights.
- **Default wardrobe:** Antique-bronze winged helmet; an unpatterned charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edge; dark-charcoal chlamys with antique-gold clasp; worn brown-leather cross-body harness and belt; scratched antique-bronze bracers and greaves; weathered brown-leather winged sandals; aged gold/bronze twin-serpent winged caduceus.
- **Variables:** Calm attentive focus; standing at a threshold; activating a gateway. No weapons except the caduceus, no combat, modern/futuristic interface, generic-hero pose, or careless behavior.

## Scene

- **Location:** Gateway Pavilion is a foreground-dominant temple-like structure with heavy stone pediment, fluted columns, and intricate celestial-pattern carvings.
- **Underfoot and materials:** Massive cracked weathered limestone and marble paving, vines, moss, dark moisture stains, and scratched/patinated bronze.
- **Portal treatment:** A grounded classical stone arch directly behind Hermes, lit only through its carved stone threshold by the warm-gold caduceus route. It is architecture, not a hologram, screen, machinery, or floating effect.
- **Light and palette:** Dusk amber, orange, and gold with long shadows. Charcoal, slate-grey, and antique sepia dominate stone and shadow. Warm gold is reserved only for active pathway, caduceus, and gateway illumination.

## Camera

- **Framing:** Full-body, medium-wide.
- **Lens:** 28mm full-frame equivalent.
- **Camera height:** Slightly below eye level.
- **Distance:** Medium-wide/wide; Hermes remains readable in substantial environment.
- **Depth of field:** Deep focus. `[default]`
- **Aspect ratio:** 16:9.

## At risk

| Invariant | Why this shot threatens it | Prompt guard |
|---|---|---|
| Hermes hair | Render 1 made the specified golden-brown curls dark brown. | “clearly visible honey-golden-brown curls with pale sun-bleached highlights; no dark-brown hair.” |
| Undertunic | Render 1 made the charcoal-grey heavy linen slate/muted blue. | “unpatterned charcoal-grey heavy-linen knee-length undertunic; no blue, slate-blue, grey-blue, or decorative blue fabric anywhere on Hermes.” |
| Woodblock style | Render 1 became dimensional academic/romantic painting. | “unmistakable traditional ukiyo-e woodblock print: flat opaque color blocks, bold dark contour lines, shallow graphic shading, visibly speckled matte paper; no oil-paint realism, painterly brushwork, or dimensional modelling.” |
| Full-body silhouette and hands | Medium-wide framing can obscure build, large hands, and winged silhouette. | “full-body Hermes, tall statuesque athletic lean build, broad shoulders, large robust hand gripping caduceus, winged helmet and sandals.” |
| Face and marks | Medium-wide view can hide face-level invariants. | “angular high-cheekboned face, strong square jaw, straight classical nose, amber eyes, bronze skin, freckles, clean-shaven.” |
| Gateway interpretation | Activation may drift to sci-fi UI or hologram. | “grounded stone arch with warm-gold glow contained inside carved stone threshold and caduceus; no hologram, UI, screen, machinery, or floating effect.” |
| Palette and active-power color | Portal scenes tend toward cool neon effects. | “only warm gold is active power; no cyan, blue glow, magenta, bright red, grass green, cool light, or full-spectrum glow.” |
| Materials and exclusions | Monumental scenes can become pristine fantasy or tech. | “cracked aged limestone/marble, moss, moisture stains, matte parchment, patinated bronze; no plastic, glossy tech, energy glass, readable text, logos, watermark, crystals, floating terrain, cosmic sky, modern clothing, or generic-superhero design.” |

## Prompt

An unmistakable traditional Japanese ukiyo-e woodblock print, not a realistic academic painting: flat opaque color blocks, bold dark contour lines, shallow graphic shading, and visibly speckled matte aged-parchment paper. A full-body medium-wide 16:9 scene shows Hermes at the Gateway Pavilion. He is tall and statuesque with an athletic lean build, broad defined shoulders, powerful limbs, and a large robust hand firmly holding an upright aged gold-and-bronze twin-serpent winged caduceus. His angular high-cheekboned face has a strong square jaw, straight classical nose, luminous amber-golden eyes, thick dark-brown brows, warm sun-baked bronze skin, freckles across his nose bridge and upper cheeks, and no facial hair. Clearly visible beneath his antique-bronze winged helmet are short-to-medium thick coarse honey-golden-brown curls with pale sun-bleached highlights, never dark brown.

Hermes stands in calm attentive focus at a grounded temple threshold, neither in combat nor in a generic-superhero pose. He wears his default outfit: an unpatterned charcoal-grey heavy-linen knee-length undertunic with a weathered parchment-sepia edge; no blue, slate-blue, grey-blue, or decorative blue fabric appears anywhere on Hermes. His dark-charcoal matte-linen chlamys is pinned with an antique-gold clasp, over a worn brown-leather harness and belt; scratched antique-bronze bracers and greaves and weathered brown-leather winged sandals complete the outfit. Immediately behind him is a heavy-pedimented classical stone arch with fluted columns and subtle celestial-pattern carvings. The caduceus activates a warm-gold route glow contained only within the caduceus and carved stone gateway threshold: it is grounded architecture, never a hologram, UI, screen, machinery, or floating effect. Underfoot are massive cracked aged limestone and marble paving blocks with vines, moss, and dark moisture stains; all bronze is scratched and patinated.

At dusk, a distant amber-orange sun casts long warm-gold shadows. Charcoal, slate-grey, and antique sepia dominate the weathered stone and ink-like shadows; warm gold alone indicates active power. Use a 28mm full-frame-equivalent lens, slightly below eye level, and deep focus. The image contains no oil-paint realism, painterly brushwork, dimensional modelling, readable lettering, captions, logos, watermarks, UI, code, file paths, borders, collages, device screens, neon blue, cyan, blue glow, magenta, bright red, grass green, cool light, full-spectrum glow, futuristic or science-fiction technology, mechanical craft, crystal forms, floating terrain, cosmic sky, modern clothing, weapons other than the caduceus, or generic-superhero design.

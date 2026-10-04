---
set: location-probes
shot: archive-cloister
attempt: 3
stage: 01_spec
status: approved
generated: 2026-09-30T02:18:20-07:00
sources:
  - 00-brief.md
  - 02-render-2.md
---

# Archive Cloister, spec 3

## World-input manifest
- `world/environment.md` — SHA-256 `8b14aa19c190f8b3760811160e90ecc037d7a3079e5194f9a781d52f570f8d19`
- `world/environment/core.md` — SHA-256 `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a`
- `world/environment/palette-and-light.md` — SHA-256 `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da`
- `world/environment/materials-and-wear.md` — SHA-256 `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5`
- `world/environment/forms-and-architecture.md` — SHA-256 `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5`
- `world/style.md` — SHA-256 `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc`
- `world/environment/locations/archive-cloister.md` — SHA-256 `7ad79dce09b5f526dc454025ecfbc79cb3bc5770b0dc2df2427746dba617051b`

## Brief
- Characters in frame: None.
- Action: Establish the location as a usable part of the Hermetic Gates route network. [stated: operator direction, 2026-09-30]
- Location: Archive Cloister. [stated: operator direction, 2026-09-30]
- Time and weather: dusk, dry ordinary weathering. [chosen]
- Framing: wide establishing view. [chosen]
- Camera height: slightly below eye level. [default]
- Lens: 28mm full-frame equivalent. [default]
- Depth of field: deep focus. [default]
- Aspect ratio: 16:9. [default]

## Characters in frame
- None. The cloister is entirely empty and unoccupied. [stated: operator correction, 2026-09-30]

## Scene
- Roofed, open-sided marble cloister with deep stone niches holding oversized weathered volumes and unlabeled parchment folders; an inner courtyard remains visible. [stated: world/environment/locations/archive-cloister.md]
- Underfoot: Cracked pale limestone slabs, moisture-darkened at the garden-facing edge. [stated: world/environment/locations/archive-cloister.md]
- Light: Indirect late-afternoon dusk light through the colonnade; one self-illuminated active niche emits restrained warm gold, without a visible human or other agent operating it. [operator correction derived from world/environment/locations/archive-cloister.md]
- Shared material and palette rules: dense weathered marble or limestone, mechanical fracturing, vines, moss, dark moisture stains, and the charcoal/slate/antique-sepia palette with warm gold only for active routing. [stated: selected shared modules]

## Camera
- Wide establishing view, 16:9. [chosen/default]
- 28mm full-frame equivalent, slightly below eye level, deep focus. [default]

## At risk
- Empty frame: The first OpenRouter pass added a robed human retrieving a volume despite the brief naming no characters. Guard: State that the entire cloister is empty and unoccupied, then explicitly exclude people, human figures, scholars, librarians, visitors, caretakers, characters, and any figure touching, retrieving, holding, reading, or standing beside a volume or parchment.
- Environment location: A first view risks losing the roofed private-cloister character, applying gold as general decoration, or producing a pristine library. Guard: State roofed open-sided marble cloister, quiet unoccupied archive atmosphere, weathered niches and parchment, one self-illuminated active niche only, and no pristine library or central portal.
- Palette and power: A new location risks using gold decoratively or introducing forbidden cool/saturated color. Guard: State that gold is the sole active routing/data indicator and only the single self-illuminated niche emits warm gold; depict dusk as flat muted sepia-and-slate printed color, not a visible sun or physically simulated sunlight.
- Woodblock visual grammar: The second OpenRouter pass rendered a dimensional digital painting despite the named ukiyo-e medium. Guard: Require a strictly two-dimensional ukiyo-e woodblock print, opaque hard-edged flat color planes, visible dark carved/keyline contours, deliberately stepped tonal areas rather than smooth gradients, and a matte printed-paper surface. Exclude digitally painted shading, airbrushing, soft gradients, physically simulated lighting, realistic reflected light, volumetric haze, realistic cast shadows, modeled volume, photographic depth, and 3D rendering.
- Image exclusions: A route or archive scene risks readable text, UI, signs, screens, or banners. Guard: Explicitly exclude lettering, UI, code, file paths, device screens, and banners.

## Prompt

A strictly two-dimensional ukiyo-e woodblock print: digital illustration with traditional Japanese woodblock-print stylization, opaque hard-edged flat color planes, clearly visible dark carved/keyline contours, deliberately stepped tonal areas instead of smooth gradients, and a matte textured paper surface with an aged speckled parchment finish. Antiquarian, Hermetic, monumental, weathered, and gold-lit only at the active route signal. No digitally painted shading, airbrushing, soft gradients, physically simulated lighting, realistic reflected light, volumetric haze, realistic cast shadows, modeled volume, photographic depth, or 3D rendering. A wide 16:9 establishing view of Archive Cloister: a roofed, open-sided marble cloister with deep stone niches holding oversized weathered volumes and unlabeled parchment folders; an inner courtyard remains visible. The entire cloister is empty and unoccupied: no people, human figures, scholars, librarians, visitors, caretakers, or characters anywhere in frame. No figure touches, retrieves, holds, reads, or stands beside any volume or parchment. Cracked pale limestone slabs are moisture-darkened at the garden-facing edge. Indirect late-afternoon dusk appears as flat muted sepia-and-slate printed color through the colonnade, with no visible sun. Only one self-illuminated active niche emits restrained warm gold, with no visible agent operating it. The world is grounded classical mythology fused with physicalized directory architecture: dense weathered marble and limestone, mechanical fractures, vines, moss, dark moisture stains, and living vegetation. The composition is seen with a 28mm full-frame equivalent lens from slightly below eye level in deep focus, with substantial environment visible. Gold is the sole indicator of active routing or data; it appears only in the single self-illuminated niche. The image holds no readable lettering, captions, logos, watermarks, UI, code, file paths, brand marks, borders, collages, device screens, presentation frames, banners, neon blue, cyan, magenta, vivid red, grass green, futuristic or science-fiction technology, crystals, floating terrain, cosmic sky, modern clothing, generic superhero design, pristine library, or central portal.
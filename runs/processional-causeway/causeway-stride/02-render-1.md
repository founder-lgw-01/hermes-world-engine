---
set: processional-causeway
shot: causeway-stride
attempt: 1
stage: 02_render
status: approved
verdict: drifted
generated: 2026-10-15T10:40:15+00:00
sources:
  - runs/processional-causeway/causeway-stride/01-spec-1.md
  - runs/processional-causeway/causeway-stride/02-image-1.png
---

# causeway-stride, render 1

## Prompt as sent

Traditional Japanese woodblock-print (ukiyo-e) digital illustration on matte textured paper with an aged, speckled parchment finish, distinct carved dark-ink keyline contours, and flat opaque color blocking. A single continuous narrative scene showing one single figure of Hermes—a tall, statuesque, athletic young adult man with broad shoulders, warm sun-baked bronze skin, a strong square jawline, straight classical nose, thick dark-brown brows, luminous amber eyes, freckles across the nose bridge, and a clean-shaven face—seen from a 3/4 rear-left angle in the lower-left third of the frame striding forward up a gently rising ancient stone road toward the upper-right. Tight tousled warm golden-brown curls with sun-bleached highlights spill from under his antique-bronze winged helmet with symmetrical feathered side wings, obscuring his ears and stopping above the collar. He wears his default outfit matching the character reference sheets: a charcoal-grey heavy-linen knee-length undertunic with a weathered parchment-sepia hem edge, a dark-charcoal matte wool chlamys cloak pinned at one shoulder with an antique-gold clasp billowing lightly behind him, a worn brown-leather cross-body harness and belt with a brown-leather messenger pouch at his hip, and scratched antique-bronze light bracers and greaves. His legs are un-crossed and cleanly separated in mid-stride—left foot planted forward on the left, right foot pushing off behind on the right, with a clear open gap of limestone paving visible between his ankles—wearing weathered brown-leather sandals that have exactly one pale feathered wing attached to the outer heel of the left sandal and one pale feathered wing attached to the outer heel of the right sandal, with completely smooth, wingless inner ankles facing each other. His robust right hand holds his aged bronze twin-serpent winged caduceus vertically forward; the caduceus head emits a self-illuminated warm-gold glow that activates a single shallow carved route channel running alongside him in the large cracked rectangular limestone paving stones of the Processional Causeway, bordered by low weathered stone plinths, fluted classical stone route markers, and creeping vines with oval and teardrop leaves. Clear dusk sky in flat stepped tones of antique sepia, slate grey, and warm amber with long hard-edged woodblock shadows; dominant palette of charcoal, slate grey, and antique sepia with luminous warm gold reserved strictly for the active caduceus and the carved stone route channel. Framed full-body in a medium-wide 28mm view slightly below eye level in deep focus at 16:9 aspect ratio, rendered in unmodulated flat areas of opaque color and hard-edged ink lines with no gradient shading, no atmospheric haze, no depth-of-field blur, no 3D rendering, no red or blue garments, no extra inner-ankle wings, no multiple figures or turnaround sheet layout, no readable lettering, no numerals, no watermarks, and no borders.

## Tool metadata

1. `model`: `gpt_image_2_5` (`variant: sunburst`) via `mcp__higgsfield__generate_image_batch` (job `75dd6cf1-6c8c-4a2d-a56e-3af21c3f4164`, cost preflight `0.25 credits`; host note: native `image_generate` failed with `model_access` 404 on `openai/gpt-image-2.5-sunburst`, so the workspace's Higgsfield `gpt_image_2_5` `sunburst` route was used with the 3 selected reference sheets `63aa51be-b069-424e-b7c5-4b0854833e62`, `23c2de11-a3c9-4593-a0e7-aab21fa2dfaa`, and `3e08d5f3-7c5c-4291-98cf-fa2f8dac1971`)
2. `request`: byte-for-byte match to `01-spec-1.md` **Prompt**
3. `aspect_ratio`: requested `16:9`, returned `16:9`
4. `resolution`: `1344x752`
5. `seed`: `not exposed`
6. `file`: `runs/processional-causeway/causeway-stride/02-image-1.png` (`PNG`, `2397938` bytes, `sha256:5f83b3e304df0ff2e502965ec510ddd708f2ea41a516288dba371a6fc4f59516`)
7. `generated`: `2026-10-15T10:40:15+00:00`

## Findings

### At risk
- **3/4 profile face (jaw, nose, brow, ear, hairline, clean-shaven):** `holds` — strong square jawline, straight classical nose, dark-brown brow, clean-shaven warm sun-baked bronze cheek, and golden-brown curls spilling under the helmet obscuring the ear.
- **3/4 rear-left silhouette and default charcoal wardrobe:** `holds` — tall athletic figure; default charcoal-grey undertunic with weathered parchment-sepia hem edge and dark-charcoal wool chlamys with antique-gold shoulder clasp hold on the first try (no red or blue garment drift).
- **Full-body proportions and paired sandal-wing symmetry:** `drifted: right sandal wing is attached to the inner (left-facing) side of the right ankle projecting leftward into the gap between the legs; spec and reference sheet require the wing on the outer heel/ankle of each sandal with smooth, wingless inner ankles` (and in a 3/4 rear-left stride where the right boot's outer side faces away from the camera, the right outer wing would be occluded behind the right ankle/greave rather than projecting leftward from the inner ankle).
- **Un-crossed mid-stride pose:** `holds` — legs are un-crossed and cleanly separated with limestone paving visible between the ankles (left foot back-left, right foot forward-right).
- **Dusk light and active warm-gold power rule:** `holds` — dusk amber/sepia horizon light and long woodblock shadows; luminous warm gold is confined to the active twin-serpent winged caduceus head and the single active shallow carved route channel in the causeway paving.
- **Reference-sheet layout exclusion:** `holds` — single continuous narrative scene with one figure of Hermes; no multi-view sheet layout transferred.
- **Woodblock-print medium:** `holds` — two-dimensional ukiyo-e woodblock print stylization on matte speckled parchment with carved dark-ink keyline contours and flat opaque color blocking.

### Character (`world/characters/hermes.md`)
1. **Silhouette:** `holds` — tall, athletic, aerodynamic forward-striding posture with billowing chlamys and vertically carried caduceus.
2. **Face:** `holds` on visible 3/4 profile (square jaw, straight nose, warm bronze skin, clean-shaven); `cannot see: freckles and exact amber iris color at medium-wide 3/4 rear-left framing`.
3. **Hair:** `holds` — short-to-medium thick curly golden-brown hair with lighter highlights spilling from under the helmet above the collar.
4. **Build:** `holds` — broad shoulders, athletic limbs, robust right hand gripping the caduceus.
5. **Signature features:** `holds` — none invented.
6. **Wardrobe:**
   - Antique-bronze winged helmet: `holds` on near (left) feathered wing; `cannot see: far (right) helmet wing occluded by helmet crown in 3/4 rear-left view`.
   - Charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edge: `holds`.
   - Dark-charcoal wool/matte-linen chlamys with antique-gold clasp: `holds`.
   - Worn brown-leather cross-body harness, belt, and messenger pouch: `holds`.
   - Scratched antique-bronze light bracers and greaves: `holds`.
   - Weathered brown-leather sandals with pale feathered heel wings: `drifted: left sandal outer wing holds on the outer-left ankle, but right sandal wing is drawn on the inner (left-facing) side of the right ankle projecting into the gap between the legs instead of on the outer right heel`.
   - Aged gold/bronze twin-serpent winged caduceus with warm-gold activation: `holds`.
7. **Variables in range:** `holds` — calm attentive focus, striding pose, default wardrobe, active caduceus and pouch.

### Environment (`world/environment/locations/processional-causeway.md` + shared modules)
9. **Location:** `holds` — gently rising stone road with low plinths, fluted classical route markers, vines, cracked rectangular limestone paving, and a single active warm-gold carved route channel.
10. **Palette:** `holds` — charcoal, slate grey, and antique sepia dominant palette with warm gold reserved for active routing and dusk horizon.
11. **Materials:** `holds` — cracked limestone slabs, weathered stone markers, creeping vines, forged bronze, matte linen/wool.
12. **Light:** `holds` — dusk amber/gold horizon light and self-illuminated warm-gold caduceus/channel.
13. **Never appears:** `holds` — no neon, cyan, magenta, vivid red, grass green, sci-fi tech, crystals, or floating islands.
14. **Style:** `holds` — 16:9 (`1344x752`) ukiyo-e woodblock print on aged speckled parchment; no lettering, numerals, watermarks, or borders.

## Drift notes

The 3 reference sheets (`hermes-body-turnaround.png`, `hermes-sandals-turnaround.png`, `hermes-props-sheet.png`) locked the ukiyo-e woodblock style, the default charcoal-grey undertunic with sepia hem, the dark-charcoal chlamys, the leather messenger pouch, and the active warm-gold twin-serpent caduceus on the first try.

However, one sandal-wing symmetry/occlusion detail drifted:
- Because Hermes is seen from a **3/4 rear-left angle** walking toward the upper-right, both wings trailed to the **left** in 2D profile—putting the left boot's wing correctly on its **outer (left) side**, but placing the right boot's wing on its **inner (left) side** projecting into the space between his ankles.
- In a 3/4 rear-left view walking toward the upper-right, the right boot's outer (right) side faces away from the camera, so asking the prompt for "one wing on the left sandal and one wing on the right sandal" caused the model to attach the second wing to the visible inner side of the right boot.

---
set: processional-causeway
shot: causeway-stride
attempt: 2
stage: 02_render
status: approved
verdict: drifted
generated: 2026-10-15T10:50:43+00:00
sources:
  - runs/processional-causeway/causeway-stride/01-spec-2.md
  - runs/processional-causeway/causeway-stride/02-image-2.png
---

# causeway-stride, render 2

## Prompt as sent

Traditional Japanese woodblock-print (ukiyo-e) digital illustration on matte textured paper with an aged, speckled parchment finish, distinct carved dark-ink keyline contours, and flat opaque color blocking. A single continuous narrative scene showing one single figure of Hermes—a tall, statuesque, athletic young adult man with broad shoulders, warm sun-baked bronze skin, a strong square jawline, straight classical nose, thick dark-brown brows, luminous amber eyes, freckles across the nose bridge, and a clean-shaven face—seen from a 3/4 rear-left angle in the lower-left third of the frame striding forward up a gently rising ancient stone road toward the upper-right. Tight tousled warm golden-brown curls with sun-bleached highlights spill from under his antique-bronze winged helmet with a feathered side wing on the near left side, obscuring his ear and stopping above the collar. He wears his default outfit matching the character reference sheets: a charcoal-grey heavy-linen knee-length undertunic with a weathered parchment-sepia hem edge, a dark-charcoal matte wool chlamys cloak pinned at one shoulder with an antique-gold clasp billowing lightly behind him, a worn brown-leather cross-body harness and belt with a brown-leather messenger pouch at his hip, and scratched antique-bronze light bracers and greaves. His legs are un-crossed and cleanly separated in mid-stride with an open gap of flat limestone paving visible between his ankles: his near left boot (stepping back-left) has a single pale feathered wing attached to its outer-left heel, while his forward right boot (planted ahead to the right) shows its inner-left ankle facing the camera—which is completely smooth, bare brown leather and bronze greave with no wing and no feathers on the inside between the legs, because the right sandal's outer wing is hidden on the far side of the right boot away from the camera. His robust right hand holds his aged bronze twin-serpent winged caduceus vertically forward; the caduceus head emits a self-illuminated warm-gold glow that activates a single shallow carved route channel running alongside him in the large cracked rectangular limestone paving stones of the Processional Causeway, bordered by low weathered stone plinths, fluted classical stone route markers, and creeping vines with oval and teardrop leaves. Clear dusk sky in flat stepped tones of antique sepia, slate grey, and warm amber with long hard-edged woodblock shadows; dominant palette of charcoal, slate grey, and antique sepia with luminous warm gold reserved strictly for the active caduceus and the carved stone route channel. Framed full-body in a medium-wide 28mm view slightly below eye level in deep focus at 16:9 aspect ratio, rendered in unmodulated flat areas of opaque color and hard-edged ink lines with no gradient shading, no atmospheric haze, no depth-of-field blur, no 3D rendering, no red or blue garments, no wing on the inner side of the right boot between the legs, no multiple figures or turnaround sheet layout, no readable lettering, no numerals, no watermarks, and no borders.

## Tool metadata

1. `model`: `gpt_image_2_5` (`variant: sunburst`) via `mcp__higgsfield__generate_image_batch` (job `db66a7e0-4c4f-44f6-aa3b-92bc49e80d21`, cost preflight `0.25 credits`; host note: native `image_generate` failed with `model_access` 404 on `openai/gpt-image-2.5-sunburst`, so the workspace's Higgsfield `gpt_image_2_5` `sunburst` route was used with the 3 selected reference sheets `63aa51be-b069-424e-b7c5-4b0854833e62`, `23c2de11-a3c9-4593-a0e7-aab21fa2dfaa`, and `3e08d5f3-7c5c-4291-98cf-fa2f8dac1971`)
2. `request`: byte-for-byte match to `01-spec-2.md` **Prompt**
3. `aspect_ratio`: requested `16:9`, returned `16:9`
4. `resolution`: `1344x752`
5. `seed`: `not exposed`
6. `file`: `runs/processional-causeway/causeway-stride/02-image-2.png` (`PNG`, `2383327` bytes, `sha256:ab48b8150edc34cff1351483be7c4def6eaacca5f817359a963fd554090a112b`)
7. `generated`: `2026-10-15T10:50:43+00:00`

## Findings

### At risk
- **Rerun drift fix (paired footwear/wing symmetry and 3/4-angle occlusion):** `drifted: Hermes's pelvis and legs are turned in a 3/4 front-right profile walking rightward, where the trailing leg on image-left is his anatomical left leg (further from camera, showing its inner-right ankle facing the viewer with a wing attached on the inside) and the leading leg on image-right is his anatomical right leg (closer to camera, showing its outer-right ankle facing the viewer with no wing at all on the outside)` — completely inverted from the bible and reference sheet (`world/references/hermes-sandals-turnaround.png`).
- **3/4 profile face (jaw, nose, brow, ear, hairline, clean-shaven):** `holds` — strong square jawline, straight classical nose, dark-brown brow, clean-shaven warm sun-baked bronze cheek, and golden-brown curls spilling under the helmet obscuring the ear.
- **3/4 silhouette and default charcoal wardrobe:** `holds` on colors — default charcoal-grey undertunic with weathered parchment-sepia hem edge and dark-charcoal wool chlamys with antique-gold shoulder clasp hold; however, the torso/pelvis orientation is ambiguous/twisted between a 3/4 rear-left prompt and a 3/4 front-right profile stride.
- **Full-body proportions and scale:** `holds` — tall statuesque athletic proportions, robust right hand gripping the caduceus, and cracked rectangular limestone paving underfoot.
- **Un-crossed mid-stride pose:** `holds` on leg separation, `drifted` on anatomical left/right wing placement.
- **Dusk light and active warm-gold power rule:** `holds` — dusk amber/sepia horizon light and long woodblock shadows; luminous warm gold is confined to the active twin-serpent winged caduceus head and the single active shallow carved route channel in the causeway paving.
- **Reference-sheet layout exclusion:** `holds` — single continuous narrative scene with one figure of Hermes; no multi-view sheet layout transferred.
- **Woodblock-print medium:** `holds` — two-dimensional ukiyo-e woodblock print stylization on matte speckled parchment with carved dark-ink keyline contours and flat opaque color blocking.

### Character (`world/characters/hermes.md`)
1. **Silhouette:** `holds` — tall, athletic, aerodynamic forward-striding posture with billowing chlamys and vertically carried caduceus.
2. **Face:** `holds` on visible profile (square jaw, straight nose, warm bronze skin, clean-shaven); `cannot see: freckles and exact amber iris color at medium-wide framing`.
3. **Hair:** `holds` — short-to-medium thick curly golden-brown hair with lighter highlights spilling from under the helmet above the collar.
4. **Build:** `holds` — broad shoulders, athletic limbs, robust right hand gripping the caduceus.
5. **Signature features:** `holds` — none invented.
6. **Wardrobe:**
   - Antique-bronze winged helmet: `holds` on visible feathered side wing; `cannot see: far helmet wing occluded by helmet crown in profile view`.
   - Charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edge: `holds`.
   - Dark-charcoal wool/matte-linen chlamys with antique-gold clasp: `holds`.
   - Worn brown-leather cross-body harness, belt, and messenger pouch: `holds`.
   - Scratched antique-bronze light bracers and greaves: `holds`.
   - Weathered brown-leather sandals with pale feathered heel wings: `drifted: left foot (trailing on image-left) has its wing on the inside ankle, and right foot (leading on image-right, closer to camera) has no wing at all on its visible outer ankle`.
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

Operator rejection (`verdict: drifted`):
- The model drew Hermes in a rightward-striding profile where his **left foot** (trailing on image-left, farther from camera) has its wing on the **inside** ankle, and his **right foot** (leading on image-right, closer to camera) has **no wing at all on its visible outside ankle**.
- My initial review misidentified which anatomical leg was closer to the camera (confusing image-left/right with anatomical left/right in a 3/4 view) and therefore stated the exact inverse of visual truth.
- Root cause in the prompt/brief: asking for a "3/4 rear-left angle walking toward the upper-right" while showing his chest/cross-body strap and face in right profile creates an anatomical twist where the model draws a 3/4 **front-right** lower body (right leg closer to camera, left leg farther from camera), so telling it "put a wing on the left boot and no wing on the right boot" literally forced the wing onto the inside of the far (left) foot and stripped the wing off the outside of the near (right) foot.

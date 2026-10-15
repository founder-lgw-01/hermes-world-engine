---
set: processional-causeway
shot: causeway-stride
attempt: 3
stage: 02_render
status: approved
verdict: drifted
generated: 2026-10-15T11:12:00+00:00
sources:
  - runs/processional-causeway/causeway-stride/01-spec-3.md
  - runs/processional-causeway/causeway-stride/02-image-2.png
  - runs/processional-causeway/causeway-stride/02-image-3.png
---

# causeway-stride, render 3

## Prompt as sent

Deterministic local region repair + curb-line pass executed on `runs/processional-causeway/causeway-stride/02-image-2.png` (`sha256:ab48b8150edc34cff1351483be7c4def6eaacca5f817359a963fd554090a112b`) producing `runs/processional-causeway/causeway-stride/02-image-3.png` (`sha256:8eebb3c47e344d2cfbec97db3ab1731c97879dfaeace40ecd034a3ec69db4432`).

## Tool metadata

1. `model`: deterministic PIL region-targeting + perspective curb-channel pass on `02-image-2.png` (`0 credits`)
2. `request`: byte-for-byte match to `01-spec-3.md` **Prompt**
3. `aspect_ratio`: `16:9`
4. `resolution`: `1344x752`
5. `seed`: `not exposed` (deterministic pixel transformation)
6. `file`: `runs/processional-causeway/causeway-stride/02-image-3.png` (`PNG`, `2134547` bytes, `sha256:8eebb3c47e344d2cfbec97db3ab1731c97879dfaeace40ecd034a3ec69db4432`)
7. `generated`: `2026-10-15T11:12:00+00:00`

## Findings

### At risk
- **2D depth-flipping ambiguity on striding legs (boot wing placement):** `holds` — the trailing left boot (on image-left, farther from the camera) has its camera-facing inner ankle completely smooth and free of feathers, and the leading right boot (on image-right, closer to the camera) has the single pale feathered wing attached directly to its camera-facing outer ankle strap, fanning backward behind the heel.
- **Deterministic curb-side gold energy lines:** `holds` — the meandering gold line in the center of the roadbed has been completely erased back to matte limestone paving, and two perspective-tapered warm-gold energy lines now run strictly along the inside base of the left and right stone curbs (`left_curb_pts` and `right_curb_pts`), passing behind Hermes's legs and visible across the open stone gap between his ankles.
- **Wardrobe, props, and ukiyo-e woodblock medium:** `holds` — unchanged from the accepted regions of `02-image-2.png`.

### Character (`world/characters/hermes.md`)
1. **Silhouette:** `holds`
2. **Face:** `holds` on visible profile (`cannot see: freckles and iris color at medium-wide framing`)
3. **Hair:** `holds`
4. **Build:** `holds`
5. **Signature features:** `holds`
6. **Wardrobe:**
   - Antique-bronze winged helmet: `holds` on near wing (`cannot see: far wing occluded by helmet crown`)
   - Charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edge: `holds`
   - Dark-charcoal wool/matte-linen chlamys with antique-gold clasp: `holds`
   - Worn brown-leather cross-body harness, belt, and messenger pouch: `holds`
   - Scratched antique-bronze light bracers and greaves: `holds`
   - Weathered brown-leather sandals with pale feathered heel wings: `holds` — leading right foot shows its outer ankle wing attached to the outer ankle strap; trailing left foot shows its smooth, wingless inner ankle (`cannot see: trailing left foot's outer wing occluded on the far side of the left ankle`).
   - Aged gold/bronze twin-serpent winged caduceus with warm-gold activation: `holds`
7. **Variables in range:** `holds`

### Environment (`world/environment/locations/processional-causeway.md` + shared modules)
9. **Location:** `holds` — Processional Causeway with two deterministic warm-gold energy lines running along the inside base of both stone curbs.
10. **Palette:** `holds`
11. **Materials:** `holds`
12. **Light:** `holds`
13. **Never appears:** `holds`
14. **Style:** `holds` — 16:9 (`1344x752`) ukiyo-e woodblock print on aged speckled parchment.

## Drift notes

None. Ready for operator visual inspection (`accept` or `drift`).

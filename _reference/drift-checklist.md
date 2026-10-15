# Drift checklist, what drift looks like and what each shot puts at risk

Drift is an invariant that moved. `01_spec` reads the risk table to write
**At risk**. `02_render` walks the whole list against the image and writes 1
finding per line. The operator walks it again at the human check and writes the
verdict. The bible is the reference; this file says how to read an image
against it.

## The findings

Each line of the check gets 1 of 3 findings:

- `holds`: the image shows the invariant as the bible states it.
- `drifted: <what moved>`: the image shows something else. Say what, in the
  bible's own words: "jaw is rounded; bible says square."
- `cannot see: <why>`: the shot hides it (back view, hands out of frame,
  hood up). Not a pass and not a fail. If a `cannot see` sits on an **At risk**
  line, the operator decides whether the shot is acceptable without seeing it.

A finding of `mostly` or `close enough` is not a finding.

## What is checked, per character

Walk the character's bible top to bottom:

1. **Silhouette**: height band, build, posture, hair and clothing outline.
   Fails as: a different body type, a changed hairline outline, a slimmer or
   heavier frame.
2. **Face**: every line under Face. Fails as: eye color or spacing, nose
   shape, jaw line, skin tone shifting warmer or cooler, a mark missing or
   moved.
3. **Hair**: color, length, texture, cut. Fails as: a shade lighter, longer
   than the bible, straight where it should curl, a part on the other side.
4. **Build**: proportions, limb length, hands, shoulders. Fails as: longer
   legs, narrower shoulders, small hands.
5. **Signature features**: each present. Fails as: absent, or swapped for
   something similar.
6. **Wardrobe**: the state the spec names, garment by garment, color and
   material, including left/right symmetry and exact counts on paired items
   (such as winged sandals, bracers, greaves, and helmet wings). Fails as: a
   garment missing, a color shifted, extra ornament the bible does not list, or
   asymmetrical/doubled appendages on one side vs. the other.
7. **Variables in range**: expression, pose, props inside the range the bible
   allows. Fails as: an expression the bible calls out of character.
8. **Relative scale** (2 or more characters): height and build against each
   other as the bibles state. Fails as: equal height where the bible says a
   head shorter.

## What is checked, for the environment

9. **Location**: what is there, what is underfoot, matches the bible's block.
10. **Palette**: dominant and accent colors present; no forbidden color.
11. **Materials**: surfaces read as the bible describes.
12. **Light**: direction, color, shadow behavior match the lighting-rules row
    for the time of day.
13. **Never appears**: nothing from the bible's list is in frame.
14. **Style**: medium, look, framing, aspect ratio match the style rules.
    Exclusions hold: no lettering, watermark, border, or whatever the rules
    name.

## Risk table, shot type to invariants at risk

`01_spec` reads the brief and lists every row that applies.

| The shot has | At risk | Guard in the prompt |
|---|---|---|
| a profile or 3/4 view | jaw, nose, brow, ear, hairline | state the profile lines from the bible in words |
| a back view | silhouette, hair fall, wardrobe back | describe the back of the hair and garments |
| a full body, wide | proportions, height, hands, relative scale | state build and height in words; name what is underfoot for scale |
| a close-up | eyes, skin tone, marks, hair texture | state each mark and its position |
| fast action or an unusual pose | proportions, limb length, wardrobe state | describe the pose joint by joint and say the outfit stays as listed |
| low light or night | skin tone, hair color, palette | name the light color and say what it does to skin and hair |
| weather or water | hair, wardrobe state, materials | name the wet or wind state the bible allows |
| 2 or more characters | relative scale, signature features swapping between them | name each at first mention with its features; state heights against each other |
| a wardrobe state other than default | every garment in that state | list the state's garments from the bible |
| an expression at the edge of range | face, and out-of-character read | name the expression and what it is not |
| a new location, first time shot | palette, materials, light | copy the location block into the scene section |

## The temporal findings

A video is checked by walking the whole shot twice: the first frame against the
bibles, then the last frame against the first. A thing that is correct in
frame 1 and wrong in frame 240 is drifted, and the finding names the frames.

Each line of a motion check gets 1 of 3 findings, using the same words:

- `holds`: the invariant reads the same in the first and last frame.
- `drifted: <what moved, and between which frames>`: name it in the bible's
  words and give the frames, e.g. "drifted: jaw rounds and the freckles are
  gone by frame 90; bible says square jaw, freckles across the nose bridge."
- `cannot see: <why>`: the shot hides it. Not a pass and not a fail.

## The temporal risk table, motion to invariants at risk

`04_animate` reads this to write **At risk**.

| The motion has | At risk | Guard in the prompt |
|---|---|---|
| a character walking or running | face, proportions, limb length, gait, paired footwear/wing symmetry, end-of-clip deceleration | state build, face lines, and left/right footwear symmetry; specify an explicit step cadence (e.g., ~2 steps/second) and say the stride pace does not slow down in the final second |
| a trailing garment, cloak, chlamys, or hair in motion | wardrobe design, hair outline | preserve colour/material/trim while cloth follows the action; settle only if the brief requires it |
| a camera push or dolly | palette, light direction, medium, scale | say the light and medium do not change as the camera moves; state that the frame ends on the same style, not a rendered 3D look |
| a camera move at all | aspect ratio, framing horizon | say the frame stays 16:9 and the horizon does not tilt |
| vegetation, dust, or water in motion | materials, palette | name the material and say it moves within the shared palette only |
| route light, gold channels, or caduceus glow | gold as the sole active-routing rule | say gold stays confined to the few active channels and does not spread or change color |
| a long duration, 10s or more | identity, wardrobe, world consistency | preserve visual design while allowing all approved motion and pose changes |
| a head turn, gaze shift, or expression change | facial structure, helmet, expression range | state starting direction, turn target, ending direction; preserve identity, not fixed facial pixels |
| a dissolve, cut, or scene change inside the shot | the whole world | forbid it: the video is one continuous shot and does not cut or dissolve |

## Motion success review

Review separately from visual consistency. For every success check in the brief,
report `holds`, `drifted`, or `cannot see` with actual timestamps or measured
frame indices. Include primary travel, visible head/gaze action, camera, and
ending where requested. Correct style with missing action is not a verified
success. Do not count cloth flutter as walking or camera drift as head motion.
Inspect first and last frames and action beats; disclose sparse-sample limits.
Approved pose/expression changes are not identity drift. Never invent frame
numbers or make a full-clip claim from a contact sheet.

## The verdict

A motion verdict covers both visual consistency and motion success.
- `verdict: accepted`: every **At risk** line holds or the operator accepts its
  `cannot see`; no `drifted` on a character; drift on the world is named and
  accepted in **Drift notes**.
- `verdict: drifted`: at least 1 line the operator will not accept. **Drift
  notes** says which, and between which frames, so `04_animate` can guard it.

### And the still verdict

The operator writes exactly 1 of:

- `verdict: accepted`: every **At risk** line holds or the operator accepts its
  `cannot see`; no `drifted` on a character; environment drift, if any, is
  named and accepted in **Drift notes**.
- `verdict: drifted`: at least 1 line the operator will not accept. **Drift
  notes** says which, in the bible's words, so `01_spec` can guard it.

## Sequence and composition review

Sequence review checks actual accepted clips against the approved storyboard
and continuity baseline. Do not repeat or revoke the individual clip verdicts.

| Selected work | Required evidence | Failure or hold |
|---|---|---|
| Adjacent shots | Observed end/start states, exact clip versions and timestamps | Missing/extra characters, changed positions/counts/props/power without an approved transition |
| Spatial continuity | Selected map version, landmarks, camera-space and route evidence | Unapproved geography or incompatible views |
| Story events | Each approved event visibly accomplished in the selected order | Beautiful clips that omit or change the intended event |
| Assembly and pacing | Actual final timeline, source in/out and approved transitions | A trim, reorder or transition changes approved intent |
| Final visual identity | Existing identity/style checks on the actual export | Finishing alters approved character/world identity or hides a known failure |
| Requested voice/sound | Actual listening/inspection and approved script/source/timing evidence | Wrong words/timing, missing layer, unreviewed audio or unapproved source |
| Requested titles/captions | Exact approved text, timing, legibility and safe area in the export | Incorrect, unreadable or misplaced text |
| Final delivery | Actual file properties and each approved delivery criterion | A spec or filename presented as proof of an export |

Use the existing visual findings for visual checks. For audio, retain actual
observations or `not reviewed`; unreviewed is not a pass. Record inspection limits
and refer required unresolved evidence to the human. Final acceptance is a
separate verdict on the actual finished piece, never inherited from its clips.

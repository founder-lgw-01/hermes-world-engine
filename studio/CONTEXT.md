# Optional studio, select the work rather than run every stage

Ask **What are we building?** If the answer is already explicit, confirm it
without asking again. Begin new productions at `./00_intake/CONTEXT.md`.
For an existing approved production, resume its named handoff without rewriting
accepted inputs. Direct existing image/motion entry points remain supported.

| Deliverable | Required path after intake | Conditional preparation/finish | Accepted endpoint |
|---|---|---|---|
| Image | `../01_spec/CONTEXT.md` → `../02_render/CONTEXT.md` → `../03_file/CONTEXT.md` | `../00_setup/CONTEXT.md` for missing records; Image route for requested references | Accepted image and approved sidecar filed in its set |
| Character | `../00_setup/CONTEXT.md` in character mode | World setup if none exists; Image route for selected references | Approved character record and only the accepted references the brief requires |
| World/location | `../00_setup/CONTEXT.md` in the selected world/location/spatial-map mode | Image route for selected maps or directional coverage | Approved selected records/maps and only the accepted coverage requested |
| Single animated shot | `../04_animate/CONTEXT.md` | Image route for a missing source; `../05_compose/CONTEXT.md` only when requested | Accepted, filed clip |
| Storied animation | `./01_story/CONTEXT.md` → `./02_sequence/CONTEXT.md` planning → `../01_spec/CONTEXT.md` / `../02_render/CONTEXT.md` / `../03_file/CONTEXT.md` as needed → `../04_animate/CONTEXT.md` per shot → `./02_sequence/CONTEXT.md` review → `../05_compose/CONTEXT.md` | `../00_setup/CONTEXT.md` for missing facts/maps/characters; reuse accepted shots instead of regenerating them | Accepted final export with links to its accepted components |

Only instantiate selected work. The endpoint for a single shot gains a final
export only when composition is explicitly selected. Missing preparation is a
named task requiring approval, never permission to render.

## Where the records live

`../_reference/studio-rules.md` owns output naming, handoffs, approval and revision
rules. New production records live under `runs/studio/<production>/`; reusable
foundations under `stories/<series>/`. Setup alone may create versioned spatial
records at `world/environment/maps/<map>-N.md`. Images and individual animations
stay in their existing run folders. No existing run is migrated.

Read this router, then the selected contract and its named inputs only. Do not
load the whole design reference, every location or other productions. Existing
contracts still own setup, image specification/render/filing and motion.

## Current boundary

The local intake, planning, composition-specification and review contracts are
available. No composition adapter is implemented by this extension. Stop before
voice generation, finishing or final rendering until a separate authorized task
provides an execution route and its checks. Draft contracts or templates are
not accepted media, technical feasibility evidence or permission to spend.

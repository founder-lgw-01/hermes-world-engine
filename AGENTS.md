# Character World Engine, consistent images of fixed characters in 1 world

You are a world engine. You produce images of named characters in 1 world, shot
after shot, where each character's features and shape never change and the
world's light, palette, and materials never change. The rules live in
`_reference/`. The world, once set up, lives in `world/`. This file routes; it
holds nothing else.

## Where am I

Read `CONTEXT.md` for the line on 1 screen. Then read the `CONTEXT.md` of the stage
you are working in. Load what that contract names and nothing more.

## Where do I go

| Task | Go to |
|---|---|
| Start a studio request or choose the deliverable | `studio/CONTEXT.md`, then its selected contract |
| Narrative foundation, sequence, maps/coverage and continuity | `studio/CONTEXT.md`; reuse approved assets and select only necessary work |
| Finish accepted animation with voice, sound, text and assembly | `05_compose/CONTEXT.md`; execution requires a separately authorized route |
| Set up a world, or add a character | `00_setup/CONTEXT.md` |
| Make a shot | copy `_templates/shot-brief.md` to `runs/<set>/<shot>/00-brief.md`, then `01_spec/CONTEXT.md` |
| A character's invariants | `world/characters/`, 1 file each |
| Environment index, locations, light, palette, materials | `world/environment.md` then selected `world/environment/` records |
| Medium, lens, aspect ratio, exclusions | `world/style.md` |
| What a bible must contain | `_reference/bible-schema.md` |
| The questions setup asks | `_reference/setup-interview.md` |
| How a spec and its prompt are built | `_reference/spec-rules.md` |
| Brief a video, using an accepted still or planning a new scene | copy `_templates/motion-brief.md` to `runs/motion/<set>/<shot>/00-brief.md`, then `04_animate/CONTEXT.md` |
| How a motion spec and its prompt are built | `_reference/motion-rules.md` |
| What drift looks like in motion | `_reference/drift-checklist.md`, the temporal tables |
| What drift looks like, what a shot puts at risk | `_reference/drift-checklist.md` |
| The image tool this folder expects | `_reference/host.md` |
| Finished shots | `runs/<set>/`, 1 manifest per set |
| Accepted videos | `runs/motion/<set>/manifest.md` |
| Studio output homes, approvals, handoffs and revisions | `_reference/studio-rules.md` |

## Never

- Derive or execute a stage output whose required declared inputs are not
  `status: approved`; route dependencies, not folder adjacency, define upstream.
- Load anything a stage's `Do NOT load:` line names. The exclusion is the
  contract, not a suggestion.
- Load the full workspace to answer 1 question. Read the contract, its named
  references, and its inputs. Nothing more.
- Edit a generated file's substantive content by hand. Run the thing that
  generates it. After explicit operator approval, an agent may change only
  approval metadata (`status`, and a render record's `verdict`).
- Invent a number, a date, or a quote. Count it, cite it, or mark it unknown.
- Edit `AGENTS.md` by hand. It is a copy of `CLAUDE.md` for hosts that read
  `AGENTS.md` first; change `CLAUDE.md`, then copy it over `AGENTS.md` again.
- Write into `world/` from any stage but `00_setup`. An approved bible is
  never edited; a change is a new setup run.
- Treat `world/environment.md` as a router. Load only selected modules and
  locations plus explicit dependencies; a neighboring location is not selected
  merely because a record names it.
- Write a prompt that is not derived from the spec sections above it.
- Fill a bible field from memory. Every trait is `stated` or `inferred`.
- Skip a setup question, or ask them all at once.
- Hold 2 worlds in this folder. A second world is a second copy.
- Declare an API key, endpoint, or client. The host provides the image tool.
- Animate an image that is not filed with `verdict: accepted`, or ask the video model to repair a still that already drifted.
- Send a local path to native `video_generate.image_url`, publish a still without approval, or resubmit a video whose outcome is unknown.
- Treat scope approval as approval of future outputs, bake finishing into studio
  animation, or claim an unimplemented composition adapter is working.

# 04_animate, turn 1 accepted still into 1 shot of motion

1 job: take a still the set already owns, freeze the world facts that motion
could drift, write a motion prompt, generate the video, and walk the same drift
check against the frames.

Animation is not a second rendering. The still is the world; this stage only
decides what changes inside it. A video that is beautiful and no longer the
same Hermes in the same light is a drifted video, the same rule as a drifted
image.

## Inputs
- Working (this run): `../runs/motion/<set>/<shot>/00-brief.md`, initially draft;
  an existing accepted still or a new-scene concept awaiting a still.
- Working (before spec/render): the `../runs/<set>/<shot>/03-sidecar.md` that names the
  accepted image, and the `../runs/<set>/manifest.md` line pointing at it
  (requires `status: approved`)
- Working (rerun): the rejected `../runs/motion/<set>/<shot>/04-render-N.md`.
- Working (variation): the explicitly named accepted predecessor; preserve it.
- Working (filing): `../runs/motion/<set>/manifest.md`, when it exists.
- Reference (selected only): approved character/location records required to
  evaluate allowed motion, plus their explicit dependency closure.
- Reference (every run): `../_templates/motion-brief.md`,
  `../_templates/motion-record.md`, `../_templates/motion-manifest.md`,
  `../_reference/motion-rules.md` for the brief interview and motion spec,
  `../_reference/drift-checklist.md` for the temporal risk table,
  `../_reference/host.md` for the video tool, `../world/style.md` for the
  medium, lens, and aspect ratio the shot inherits

Do NOT load: `../world/interview.md`, the bible is the truth and the interview
is raw; `../_reference/spec-rules.md`, the still's prompt is already built and
is not rewritten here; any shot folder other than the one named above, one
still is the only input to one motion; `../01_spec/`, `../02_render/`,
`../03_file/`, except the named new-scene handoff in process step 2;
upstream contracts are not loaded for an existing-image run.

## Process
1. Copy `../_templates/motion-brief.md` to a new motion shot folder as a draft.
   Interview for the desired outcome, starting state, primary action including
   head/gaze, sequence and ending, secondary motion, camera, consistency,
   delivery, and observable success checks. Preserve operator answers; surface
   delegated choices. Do not derive a spec from an incomplete brief.
2. Check feasibility against the reference and active host schema/configuration
   before brief approval. Classify supported, uncertain, and unsupported requests
   with evidence. Resolve conflicts/settings with the operator, then obtain
   brief approval. New-scene mode may prepare a concept brief before a source:
   hand off to the existing still pipeline with separate approvals, then return
   after filing. Load upstream stage contracts only at that handoff. Existing-
   image mode never authorizes new images. Recheck feasibility on the final still.
3. Before writing a motion spec, require `00-brief.md` and the source sidecar to
   say `status: approved`, and its render record to say `status: approved` and
   `verdict: accepted`. Derive `01-spec-N.md` using `motion-rules.md` in order,
   prompt last. Preserve identity/design while allowing briefed head, gaze,
   expression and position changes. An accepted-video variation gets a new shot
   folder; rejection revisions retain numbered attempts and source history.
4. Stop for explicit approval of `01-spec-N.md` before rendering. Verify the
   accepted source hash, the approved sidecar, and the active native video
   provider/model and supported parameters using `../_reference/host.md`.
5. Obtain a public HTTPS URL for that exact still. Prefer an existing authorized
   URL; publishing a local image requires explicit approval. Fetch the URL
   without authentication and verify its SHA-256 against the source. No
   Higgsfield import, upload widget, or `media_id` is required.
6. Call Hermes's native `video_generate` with the approved prompt unchanged,
   `image_url`, and explicit duration, aspect ratio, resolution, audio, and
   upscale settings. The call blocks until it returns; no MCP `job_status`
   polling is part of this route. Do not silently replace image-to-video with
   text-to-video. Report unsupported approved settings; never claim they applied.
7. Save the returned video to `../runs/motion/<set>/<shot>/04-video-N.<ext>`.
   Fill `motion-record.md` with the prompt as sent, source URL/hash, configured
   provider/model, actual returned provider/model/endpoint, and measured media
   properties. Write `not exposed` for missing metadata. On an unknown
   submission outcome, stop and reconcile it rather than resubmitting blindly.
8. Inspect actual video: report visual consistency separately from motion
   success against every brief criterion, then write **Drift notes**. If video analysis is unavailable, inspect extracted samples including
   first and last frames; record sample timestamps and limitations without
   claiming exhaustive frame-by-frame review. Leave the verdict empty for the
   operator. Complete any separately approved temporary-host cleanup and verify
   it; public GitHub hosting is not automatically temporary.

9. After operator acceptance only, require the render record to say
   `status: approved` and `verdict: accepted`; verify the local video hash, then
   create/update `../runs/motion/<set>/manifest.md` from the manifest template.
   Append one row per accepted attempt with relative source/spec/video/record
   paths, video hash, and actual approval evidence. Avoid duplicate rows. The
   record remains authoritative; manifest filing does not publish the video.

## Outputs
- `../runs/motion/<set>/<shot>/00-brief.md`, initially `status: draft`;
  feasibility is retained in the brief, not a parallel tracker.
- `../runs/motion/<set>/manifest.md`, accepted attempts only.
- `../runs/motion/<set>/<shot>/01-spec-N.md`, frontmatter: `set`, `shot`,
  `attempt`, `stage: 04_animate`, `status: draft`, `generated`, `sources`
- `../runs/motion/<set>/<shot>/04-video-N.<ext>`, `../runs/motion/<set>/<shot>/04-render-N.md`
  frontmatter adds `verdict`

## Human check
Watch the video from the first frame to the last. Read **Drift notes** against
`_reference/drift-checklist.md`'s temporal rows. The operator may approve by
editing the render record or by clear chat approval naming it; after that
approval, the agent records `status: approved` and `verdict` only.

## Source acceptance and limits
Inherit operator-accepted deviations; do not revoke an accepted still because
animation is difficult. If the operator requests a new reference, route it to
its upstream contract with separate approval. Never ask motion to repair a
rejected still. Brief/spec gates prove readiness, not guaranteed model output.
Watch primary motion and ending as well as visual consistency before acceptance.
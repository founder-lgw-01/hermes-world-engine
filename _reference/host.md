# Host, the image tool this folder expects

This folder needs 1 capability from the agent running it: an image generation
tool the agent can call with a text prompt and get an image file back. Nothing
here declares an API key, an endpoint, or a client. The host provides the
tool; this file names it. To move the folder to a different host, change this
file and nothing else.

## As shipped

| | |
|---|---|
| Host | Hermes agent |
| Tool | `image.gen` |
| Model | gpt image 2.5 sunburst (`openai/gpt-image-2.5-sunburst`) via OpenRouter |
| Prompt style | natural language; no parameter syntax, no weighting, no negative field |
| Aspect ratio | passed as a tool parameter where the tool takes 1; otherwise stated in words at the end of the prompt |
| Reference images | pass up to 3 selected `world/references/` images from the spec's **World-input manifest** (`reference_image_urls` on native `image_generate`, or `medias` with role `image_references` on the Higgsfield fallback); consistency comes from both the selected reference sheets and the prompt/bibles |

## What the render record captures

`02_render` writes these under **Tool metadata**, in this order. A field the
tool does not return is written `not exposed`, never left blank, so a later
reader knows it was asked for.

1. `model`: the model name the tool reports
2. `request`: the prompt exactly as sent, byte for byte the spec's **Prompt**
3. `aspect_ratio`: as requested, and as returned if the tool reports it
4. `resolution`: width by height of the returned image
5. `seed`: if the tool exposes 1
6. `file`: the image filename and type
7. `generated`: the timestamp

## The video tool

`04_animate` needs a second capability from the host: a video generation tool
that takes a text prompt plus one still image and returns a video file. Same
rule — nothing here declares a key, an endpoint, or a client.

### As shipped, video

| | |
|---|---|
| Host | Hermes agent |
| Tool | native Hermes `video_generate` |
| Router | active local Hermes profile configured with `video_gen.provider: nous`; generation runs remotely through the Nous route, not on local hardware |
| Model pin | `video_gen.model: bytedance/seedance-2.5` |
| Verified backend | returned provider `fal`, model `seedance-2.5`, image-to-video route; record actual returned metadata rather than assuming it matches the configured router |
| Prompt style | natural language; approved spec prompt sent unchanged |
| Still input | public HTTPS URL passed directly as `image_url`; no import, widget, or `media_id` |
| Duration, resolution, aspect ratio | inspect the active tool schema before approval/submission; verified Seedance settings: 5 seconds, 16:9, 720p; active schema supports 480p/720p, not 1080p |
| Audio and upscale | set explicitly; verified shot uses `audio: false`, `upscale: false`; do not add paid processing silently |
| Completion | blocking tool call returns a video URL or local path; save and inspect it, with no Higgsfield polling |

### Preflight and image handoff

Read `hermes config get video_gen` and the current `video_generate` schema.
The model is host configuration, not a generation-call argument. Change it only
with operator approval using `hermes config set`; do not declare credentials or
clients here. Official reference:
https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin

For a local still, obtain approval before public hosting. A separate public
GitHub asset repository can provide a raw PNG URL without GitHub Pages or any
change to the private world repository. Fetch the public URL without credentials
and verify identical SHA-256 before passing it as `image_url`. Record its exact
URL and publication handle. Public Git history and caches can retain copies;
cleanup or visibility changes need their own scope.

The configured Nous router is local configuration; inference is remote.
Record both configured and returned routes. Measure returned duration,
dimensions, codec, frame rate, and audio streams instead of trusting a missing
or empty aspect-ratio field. If an approved setting is unsupported, report the
limitation; do not claim 1080p or add an upscale charge. A transport timeout
leaves submission outcome unknown: reconcile any returned handle before retrying.
Separate billable probes require approval.

## Changing host

Replace the table under **As shipped**. If the new tool takes parameters
(`--ar`, weights, a negative field), `spec-rules.md` still writes description;
add a line here saying which parameters `02_render` passes beside the prompt,
and keep the prompt itself free of them.

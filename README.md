# Character World Engine

This folder produces images of fixed characters in 1 fixed world, 1 shot at a
time, for an operator who wants a set of images that hold together: the same
face, the same build, the same light and palette, across any pose, action, or
scene. A run costs 3 short reads from you: the bibles once, then each shot's
spec before it is rendered and its image before it is filed.

The folder ships empty. Setting it up fills it with 1 world. To make a second
world, copy the empty folder again.

## Start a run

1. Open `CLAUDE.md`. It routes; it holds nothing.
2. Read `CONTEXT.md` for the whole line on 1 screen.
3. First time only: put your reference images in `world/references/`, then go
   to `00_setup/` and read its `CONTEXT.md`. It interviews you before it writes
   anything. Read the modular world records and bibles it writes, correct them,
   and flip each to `status: approved`.
4. For a shot: copy `_templates/shot-brief.md` to `runs/<set>/<shot>/00-brief.md`
   and fill it in. `<set>` is a name you give a group of shots; `<shot>` is
   this shot's name.
5. Go to `01_spec/`, then `02_render/`, then `03_file/`. Each stage's
   `CONTEXT.md` says what it reads, what it writes, and what you check.
6. Read each output. Edit it. Flip `status: draft` to `status: approved`. The
   next stage refuses to run until you do.

To add a character later, go to `00_setup/` again in character mode. The world
stays as it is.

## Modular world and reference permissions

`world/environment.md` is a short index. Setup places shared rules in
`world/environment/` and one record per location in `world/environment/locations/`.
A shot loads only selected visible locations, required modules, and their
explicit dependencies; mentioning a neighbor does not load it.

Each governed reference image can have a same-stem Markdown companion with
narrow named roles. A role is a candidate, not an automatic attachment. The
spec records the selected world inputs, roles, and SHA-256 hashes; render checks
them before using the approved prompt. See `_reference/world-routing-schema.md`.

Run `python -m unittest discover -s tests -v` to validate this empty scaffold.
Populated-world validation belongs in a separate test suite added after setup.

## What you need

This folder, and an agent that can read it and has an image generation tool.
As shipped it expects Hermes with `image.gen` backed by gpt image 2.5
sunburst (`openai/gpt-image-2.5-sunburst`). `_reference/host.md` names the
tool and is the only file to change for a different host. No API key,
endpoint, or client is declared here.

## Credit

This workspace is built on Interpretable Context Methodology (ICM). The method
was created by Jake Van Clief and David McDermott. It is MIT-licensed, and the
paper is here: https://arxiv.org/abs/2603.16021

The folders do the work a framework would do in code. Numbered folders carry
the order. Each folder's own file says what to read. Plain text files carry
the state. 1 agent walks the folders in order.

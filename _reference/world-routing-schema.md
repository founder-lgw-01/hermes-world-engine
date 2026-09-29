# World routing schema

The world is a selective-loading library, not a single prompt payload.
`world/environment.md` is the short entry index. It names shared modules and
available locations but does not repeat their creative facts.

## Record metadata

Every setup-owned environment index, module, location, and reference-permission
record begins with:

```yaml
---
world: <world-slug>
kind: environment-index | environment-module | environment-location | reference-permissions
stage: 00_setup
status: draft
generated:
scope: <one-line authority boundary>
depends_on: []
reference_roles: []
sources: []
---
```

`depends_on` contains only canonical project-relative Markdown paths under
`world/`. It loads shared rules, never a neighboring location merely because
that location is mentioned in prose. A dependency graph must be acyclic.

`reference_roles` contains candidate pointers of the form
`world/references/<image-stem>.md#<role-id>`. A candidate does not select an
image. A shot selects the smallest compatible set and records each selected
role in its spec.

## Selective loading

For a shot, read the environment index, style record, named character records,
and only the environment modules and locations required by visible content. Load
the explicit dependency closure of those selected records. Global invariants
outrank local detail; reference permissions never outrank an approved bible.

## Reference companions

A governed image in `world/references/` has a same-stem Markdown companion.
Each companion may define one or more `### <role-id>` blocks with this table:

```md
| Field | Value |
|---|---|
| Evidence class | direct | inspiration | conflict-only |
| Use only for | <narrow authority> |
| Do not transfer | <what this image cannot control> |
```

Images and their companion records are written only by `00_setup`. Do not
copy permission tables into a world module, style record, or character bible.

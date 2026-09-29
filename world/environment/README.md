# Environment modules

`00_setup` creates records here after the interview; this scaffold intentionally
contains no world facts. Start at `../environment.md`, then load only the
modules and locations that the shot needs.

- Shared rule modules use `_templates/environment-module.md`.
- Each visible location gets one file under `locations/` from
  `_templates/location.md`.
- Dependencies are explicit, canonical project-relative paths under `world/`.
- Mentioning an adjacent location does not load it.

See `_reference/world-routing-schema.md` for the metadata and reference-role
contracts.

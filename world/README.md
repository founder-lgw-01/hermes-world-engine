# world, the 1 world this folder holds

Written by `00_setup` and by nothing else. Ships blank: the files below carry
their fields and no values until setup runs. After a file here says
`status: approved`, no stage edits it; a change is a new setup run.

| File | Holds |
|---|---|
| `interview.md` | every question setup asked and every answer, the raw record |
| `environment.md` | short environment index and selective-loading map |
| `environment/*.md` | shared environment rules, one owner per field |
| `environment/locations/*.md` | one location's local facts and dependencies |
| `style.md` | the style rules |
| `characters/<name>.md` | 1 character bible per character |
| `references/<image-stem>.md` | narrow permissions for one reference image |
| `references/` | the reference images setup read, and every bible cites |

Start at `environment.md`; load only selected modules and locations plus their
explicit dependencies. A second world is a second copy of the empty engine, not
a second set of files here.

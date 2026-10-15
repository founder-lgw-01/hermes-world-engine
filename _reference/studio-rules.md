# Studio rules, selected work with explicit handoffs

Paths in this reference are workspace-relative. `studio/CONTEXT.md` is the
canonical route table; this file owns shared approval, record and revision rules.
The retained design is historical design evidence, not an execution contract.

## Intake and defaults

Use the requested deliverable and accepted endpoint, not a mandatory tour of
stages. Ask missing questions in small groups, explain choices, and distinguish
operator answers from suggestions. Asset-only requests skip story questions.
A single animated shot ends as an accepted, filed clip unless finishing is
requested. A storied animation includes final assembly, not merely loose clips.

Hermes prepares and performs the first review; Jordan is the human approver
unless explicitly reassigned. Self-review is not independent review. Record
applicable roles in intake; a receiving producer checks readiness, not acceptance.
Unassigned responsibilities block execution until assigned. Review packages
name every artifact and version, findings and action authorized. Group ready
outputs at milestones, but never preaccept future work or bypass a stage gate.

With no approved assets, intake names necessary setup/reference tasks. Scope
approval is not permission to generate, spend or publish. Accepted-but-unfiled
assets require their existing filing handoff, not replacement production.
Select only coverage needed for the brief or storyboard. A complete approved
intake can name unfinished preparation; a consuming spec needs its actual
approved inputs. An unknown that prevents agreeing scope blocks intake approval.

## Canonical homes

| Fact | Home |
|---|---|
| Audience, purpose, deliverable, selected route, roles and approval scope | Intake |
| Character identity, world time, materials, palette, light | Approved setup records |
| Reusable genre/exclusions/recurring conflict | Series foundation |
| Particular story events | Sequence brief |
| Fixed layout, landmarks, walkable routes, available camera/staging space | Setup-approved spatial record; derived maps cite their original owner |
| Shot order and composition intent, coverage needs | Storyboard |
| Time-specific positions, presence, counts and prop/power states | Continuity states keyed to shots |
| Chosen camera, action and shot success criteria | Individual shot/video brief; spec derives it |
| Voice/sound/text and finishing intent | Early composition brief |
| Exact assembly timeline and finishing placement | Composition spec |
| Actual sequence observations and reconciled transitions | Sequence review |

Production-specific story choices reference the series foundation. A departure
from approved series rules requires explicit approval; it never silently edits
shared rules. No downstream stage writes into `world/`. New spatial facts or
conflicts return to setup. A draft sketch cannot overrule accepted imagery.

## Output registry

N is the artifact's attempt/version, chosen from existing siblings, never a
new approval state. Copy only selected templates and keep every prior attempt.
Sources and handoff paths are canonical workspace-relative paths; use exact
filenames, never a moving “latest” pointer. Reserved run namespaces `studio` and
`motion` are not ordinary image set slugs. Do not migrate historical artifacts.

| Artifact | Template | Output | Writer |
|---|---|---|---|
| Intake | `_templates/studio-intake.md` | `runs/studio/<production>/00-intake-N.md` | studio/00_intake |
| Early composition brief | `_templates/composition-brief.md` | `runs/studio/<production>/00-composition-N.md` | studio/00_intake |
| Reusable foundation | `_templates/story-foundation.md` | `stories/<series>/01-foundation-N.md` | studio/01_story |
| Sequence events | `_templates/sequence-brief.md` | `runs/studio/<production>/02-sequence-N.md` | studio/02_sequence |
| Storyboard/coverage | `_templates/storyboard.md` | `runs/studio/<production>/02-storyboard-N.md` | studio/02_sequence |
| Expected continuity | `_templates/continuity.md` | `runs/studio/<production>/02-continuity-N.md` | studio/02_sequence |
| Actual sequence review | `_templates/sequence-review.md` | `runs/studio/<production>/02-review-N.md` | studio/02_sequence |
| Spatial facts/map | `_templates/spatial-map.md` | `world/environment/maps/<map>-N.md` | 00_setup |
| Composition spec | `_templates/composition-spec.md` | `runs/studio/<production>/05-spec-N.md` | 05_compose |
| Final review/filing record | `_templates/composition-record.md` | `runs/studio/<production>/05-record-N.md` | 05_compose |
| Actual final export | no empty placeholder | `runs/studio/<production>/05-final-N.<ext>` | separately authorized composition execution |

Studio records use production (or series for a foundation), attempt, stage,
status, generated and sources in frontmatter. Spatial records use the setup
schema. Review records add verdict. Templates are draft and verdict is empty.
Neither file existence nor a copied template indicates completion. Do not
create placeholder final media. Existing image/motion names and formats remain
owned by their current contracts; studio packets reference, never copy, media.

## Approval and handoff

A consumer checks all declared inputs rather than the numerically preceding
folder. Required Markdown inputs must be `status: approved`; accepted media
also require `verdict: accepted` on their authoritative record and the existing
filing evidence. A selected foundation reused unchanged needs no new approval.

### Visual-gate mode (`gate_mode: visual-only`)
When the operator selects `gate_mode: visual-only` (or directs the agent to
skip intermediate Markdown-only gates and stop only at visual or spend/publish
boundaries), the agent still writes, hashes and marks `status: approved` on
each required intermediate Markdown artifact (`00-intake-N.md`,
`00-composition-N.md`, `01-foundation-N.md`, `02-sequence-N.md`,
`02-storyboard-N.md`, `02-continuity-N.md`, `01-spec-N.md`, `05-spec-N.md`) in
dependency order, citing the operator's `visual-only` scope authorization in the
handoff. Under `gate_mode: visual-only`, the agent halts only at:
1. **Unresolved scope/intent questions** that were not delegated,
2. **Spend or external-publication gates** (paid image/video generation calls or
   public hosting uploads, unless explicitly pre-authorized in the operator's
   turn), and
3. **Visual acceptance gates** (`02-render-N.md`, `04-render-N.md`,
   `02-review-N.md` when visual mismatches require a decision, and
   `05-record-N.md`), where the actual image or video is displayed via `MEDIA:`
   for human `verdict: accepted` | `drifted`.
`gate_mode: strict` (default when unspecified) stops at every Markdown stage gate.

Sibling drafts in one review package (intake/composition brief or
storyboard/continuity) may be reconciled together. They cite one another by
exact path as working cross-references, not approved upstream dependencies.
Do not hash sibling drafts into one another: each freezes only its already
approved upstream inputs. The receiving stage freezes all required sibling
versions after the whole package is approved. This avoids circular hash
dependencies and does not permit downstream production from unapproved drafts.

Every handoff includes exact input versions, recorded SHA-256 values computed
after approval metadata, authoritative approval evidence, receiving producer,
expected output, acceptance checks, completed checks and unresolved questions.
Read source status/verdict again and verify the recorded SHA-256 before use.
Missing inputs, changed hashes, unapproved versions or unresolved required
checks halt that handoff. Approved brief scope cannot make these checks pass.

The handoff is part of the receiving artifact, not a second status tracker.
Its evidence points to the source's approved metadata and any real operator
message/receipt available when written. Never invent a receipt. Record observed
input evidence at creation; do not maintain a competing editable status column.
After explicit human approval, change only status/verdict metadata. Do not
rewrite a generated approved body to add later decisions; a subsequent derived
artifact can cite later approval evidence. Grouping approvals does not eliminate
the separate brief, spec/production, result and final-export gates.

## Studio handoff into individual shots

Use the optional Studio handoff section of the existing shot/video brief. A
standalone shot writes `none`; it need not create studio records. A studio shot
names approved intake and, for a narrative, sequence, storyboard and continuity
versions, its shot/event IDs and state IDs. Include only selected map/reference
records and necessary dependency closure. Other shot prompts are not inputs.

The individual brief is derived from those approved decisions and remains a
separate human-approved intent record. Resolve conflicts in the upstream owner,
not by overriding it in a prompt. Early composition requirements may guide
framing/timing but voice, sound and exact on-screen text remain in composition.

Image specs freeze these planning inputs in the existing World-input manifest;
motion specs freeze them in the Source manifest. This allows the existing
hash-checking gates to detect stale inputs. Preserve prompt-last derivation.
No studio approval authorizes source-image publication or bypasses existing
production feasibility, spending and render gates.

## Sequence planning and reconciliation

Approve the foundation and sequence events before shot planning. Build maps
from approved facts and an explicit storyboard, then iterate coverage and
continuity until they agree. Missing imagery is a preparation task; missing or
conflicting geography needs setup approval before a dependent specification.
Only selected shots need starting stills or additional views.

Continuity owns named states. Each shot references start/end state IDs instead
of keeping independent copies of positions/counts. A storyboard fixes shot
order; transitions refer to that order, not directory sorting. Explicitly
approved jumps/cuts name the intended change and its approval evidence.

After clips are individually accepted and filed, review their actual observed
states and adjacent transitions. Include evidence/timestamps and limitations;
planning expectations are not observations. A required mismatch or uninspected
state blocks sequence acceptance until resolved or the baseline is explicitly
revised and reviewed. Do not revoke historical acceptance of individual clips.
An accepted review freezes the exact clip and baseline versions it checked.
Composition must recheck those same versions, not substitute a newer clip.

## Revision impact

When an input changes, identify its old/new versions and dependent outputs by
their sources/manifests. Create a new attempt through its owning stage; keep
superseded files and historical acceptance intact. An old approval never
transfers to the replacement. Frozen old versions can still support historical
outputs; a new context or selected version requires impact review before use.

Re-review is not automatic regeneration. Record why unchanged reuse is valid,
or the smallest revised output requiring approval. Changed intent returns to
its brief; changed geography returns to setup; changed clips return to sequence
review before composition. Post-playback operator drift notes and next-pass
recommendations on an already accepted sequence or export are recorded by
opening the next numbered `runs/studio/<production>/02-review-N.md` (`status: draft`),
preserving the prior accepted review and routing each item to its upstream owner.
Record this impact in the new artifact's handoff,
not a new global tracker or an invented status enum. A planning decision may
remain blocked without marking an old accepted asset rejected.

## Limits and acceptance

Current production checks remain with setup/image/motion. Do not investigate
tools while doing intake or narrative planning. Describe a needed capability
as unverified and request a separately scoped task, not a smaller artistic goal.
Composition has no adapter implemented by this extension; its contract halts
before execution until a separately authorized route exists.

Route completion means the named output and its human acceptance/filing, not
merely a spec or contract file. Final export acceptance is distinct from clip
acceptance. Publication always needs separate authorization and a read-back
receipt, including any intermediate public source image. Local filing is not
publication. Synthetic test fixtures are not real production/acceptance evidence.

# Studio Design Combined-Review Revision Plan

> **For the implementer:** Apply this documentation plan task-by-task only after Jordan explicitly authorizes the design-file revision. This plan does not authorize studio implementation, production, delegation, spending, publication, commits or pushes.

**Goal:** Revise `_reference/studio-extension-design.md` to combine the reviews' strongest recommendations into a clear, optional, brief-led studio design without changing the existing workflow or treating proposals as approvals.

**Architecture:** Edit the existing design reference in place, keeping one canonical explanation of each proposed rule and linking route summaries to those explanations. Preserve supplied historical statements, creative proposals and the operator's scene concept, while adding explicit accountability, handoffs, planning relationships, revision handling and acceptance gates. This remains a draft design; executable contracts, new stage names and output paths belong to a later, separately approved implementation task.

**Tech stack:** Markdown; existing Hermes file tools; read-only Python standard-library checks and Git inspection. No dependencies or application code.

---

## Current context and assumptions

### Workspace and scope

- Workspace: `/opt/data/hermes-world-engine`.
- Sole future edit target: `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`.
- Sole file created during this planning turn: this plan under `.hermes/plans/`.
- Observed branch: `main`.
- Observed untracked paths: `_reference/studio-extension-design.md` and `runs/character-shots/`. Do not stage, delete, overwrite or investigate the latter as part of this task. A clean tracked-file diff does not prove an untracked file was unchanged.
- The design currently declares `kind: design-reference`, `status: draft`, and `implementation: proposed-extension`. Keep all three values.
- The existing stages are `00_setup`, `01_spec`, `02_render`, `03_file` and `04_animate`. Mentioning them is not permission to run or modify them.

### Evidence used to make this plan

- Jordan's desired-outcome prompt, the single-model review, the supplied MOA response, the comparison, and Jordan's correction that MOA had the design text pasted into its context.
- The current design file, read in full.
- Read-only boundary checks: `CONTEXT.md`, `00_setup/CONTEXT.md` and `04_animate/CONTEXT.md`. These clarify current handoffs and approval conventions; their technical claims were not tested.
- No session-history retrieval, capability audit, asset inspection, tool/provider investigation or production trial was performed.

Both reviews had design contents. Do not describe MOA's lack of a file-open operation as lack of evidence. Its reported advisor-independence caveats are a separate matter, and no new claim of independently verified multi-advisor consensus should be added.

### Existing conventions to preserve

- Approved world/character identity remains authoritative. New facts return through `00_setup`; downstream work does not write into `world/`.
- Approval state is authoritative in the declared artifact, not a parallel tracker. A derived handoff may reference approval evidence but does not own a second live status.
- A starting still must be accepted and filed before its motion specification consumes it. Existing-image requests do not authorize replacement stills.
- Brief approval and specification/production approval are distinct. Existing animation production checks remain in their current contract; this design revision does not conduct, remove or duplicate them.
- Generated outputs and accepted assets are untouched. Drafting design prose is not editing generated production artifacts.
- The working root describes a sequential pipeline. Optional routing will eventually require contract reconciliation, but that is not part of this document-only revision.

### What the combined review contributes

| Contribution | Apply in this design |
|---|---|
| Accountability | Producer, reviewer and human approver for selected work; assignments explicitly unassigned until made |
| Handoffs | Input versions and approval evidence, expected output, checks, blockers and receiving responsibility |
| Cold start and completion | Conditional preparation, safe skips and an accepted endpoint for every route |
| Approval clarity | Ordered gate view for each route, referencing common meanings |
| Revision handling | Dependency impact, bounded re-review and no silent transfer of approvals |
| Canonical boundaries | Fixed geography versus changing state; available camera space versus chosen camera; reusable rules versus production choices |
| Narrative coherence | Iterative maps/storyboard/coverage/continuity planning plus shot start/end states |
| Acceptance | Route-specific outcomes, adjacent-shot reconciliation and final-piece review |
| Beginner experience | Small relevant question groups, plain-language summaries and five route walkthroughs |

## Clarification decisions — confirmed by Jordan

After the initial plan was saved, Jordan answered all four clarification questions through the clarification form. Apply these decisions to the future design revision; they do not authorize editing the design in this planning turn or implementing the studio.

| ID | Confirmed decision | Implementation consequence for the document |
|---|---|---|
| D1 | Hermes prepares and reviews; Jordan gives human approval, unless explicitly reassigned. | Name this as the adopted role default. Each production records applicable assignments; Hermes reviewing its own work is not independent review. |
| D2 | A reusable series foundation plus production-specific choices; world facts remain in world records. | Use that ownership model. Audience/purpose for a particular production belong in its brief; no production silently overrides canon. The creative audience, theme and antagonist proposals remain separately unadopted. |
| D3 | An accepted, filed clip; add composition only when requested. | Use this endpoint consistently in routing, approval gates, composition and acceptance checks. Finishing is optional for a single shot, not a default prerequisite. |
| D4 | Grouped at meaningful milestones, listing every artifact and version being approved. | Use named review packages without skipping existing gates, preapproving future outputs or treating a review/readiness check as human acceptance. |

No clarification question remains unanswered in this plan. A separate explicit authorization is still required to edit the design file. Do not infer approval of all other proposed rules, creative canon, structural implementation, spending or publication from these answers.

## Files and actions explicitly excluded

Do not edit `CONTEXT.md`, `CLAUDE.md`, `AGENTS.md`, any numbered stage's `CONTEXT.md`, `_templates/`, other `_reference/` files, `world/`, `runs/`, tests, skills, memories, configuration or integrations. Do not create stage folders, a status tracker or production records. Do not generate media, investigate capabilities, install anything, run a provider probe, publish, commit or push.

## Implementation method

- Use `read_file` for current content and `patch(mode="patch")` for targeted V4A edits.
- Locate sections by the exact headings below; the original line numbers are orientation only and will move.
- Do not replace the entire design, perform global reformatting or copy this whole plan into it.
- All new operating rules go under explicitly **proposed** headings. Only the five-route wording and the accepted-animation composition boundary already confirmed by Jordan belong in the confirmed-direction section.
- Keep the original historical source entries. An additional source may be described as `operator-supplied MOA response and combined-review discussion in the current desktop conversation`; do not invent a session ID or a date.
- Use the confirmed decision table above for the wording in the tasks. If a later instruction changes a decision, reconcile this plan before editing the target.

## Step-by-step tasks

Each task is a small documentation edit or check, intended for one focused pass. No task creates executable studio behavior.

### Task 1 — Confirm authorization and preserve the baseline

**File:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md` — read only.

1. Require explicit permission to revise this one design file. Planning approval alone is insufficient.
2. Use the confirmed D1–D4 answers above. Ask again only if a newer instruction conflicts with them.
3. Run the following read-only commands from `/opt/data/hermes-world-engine`:

```bash
git status --short
git branch --show-current
python3 -c 'from pathlib import Path; import hashlib; p=Path("_reference/studio-extension-design.md"); assert hashlib.sha256(p.read_bytes()).hexdigest()=="e4ff3ce6dd5edec9d275ef82b6d0f7f1914549632aa79c3e00eb2b67b308bfc6", "Source changed: reread and reconcile this plan before editing"; print("PASS source baseline")'
```

**Expected:** Branch `main` unless independently changed; existing untracked design and character-shots paths remain, and the plan directory may now be shown. The Python command prints `PASS source baseline`. If the file changed, stop and re-read it; never overwrite newer work to restore this baseline.

### Task 2 — Clarify authority and align confirmed wording

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Purpose and authority` and `Confirmed direction from Jordan` (original lines 12–41).

- Keep the draft/proposed frontmatter and all existing non-authorization boundaries.
- Replace the opening-question bullet with:

```markdown
- The opening question is: **What are we building?** An image, a character,
  a world or location, a single animated shot, or a storied animation.
```

- Make the composition bullet explicitly say `after animation elements are built and accepted`; retain named integrations as proposed choices.
- Append to `Purpose and authority`:

```markdown
The proposed operating rules below consolidate the single-model and
operator-supplied MOA reviews. Both reviews had the design text available;
file access versus pasted text is not an evidence-quality distinction.
These recommendations remain proposals unless explicitly adopted by Jordan.
Adoption of a design decision is separate from authorization to change stage
contracts, generate assets, spend, publish or commit.

Implementation-status statements are retained as supplied historical evidence.
This revision neither verifies nor updates them. Technical feasibility remains
a separately authorized task and is not used here to narrow the desired studio
outcome.
```

**Verify:** Read the revised two sections. They must state five routes, accepted-animation composition and proposal/authorization separation without claiming the studio exists.

### Task 3 — Replace routing shorthand with conditional paths and endpoints

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Proposed optional routing` (original lines 111–127).

Replace its table and explanatory paragraphs with the following. The single-shot endpoint implements confirmed decision D3; the remaining new operational details remain proposals unless separately adopted.

```markdown
Intake identifies the intended deliverable, approved reusable assets, missing
preparation, selected work, safe skips, acceptance criteria and approval scope.
Every route begins with a complete brief appropriate to that deliverable;
only narrative requests require story-foundation and sequence questions.

| Deliverable | Selected path and conditional preparation | Accepted endpoint |
|---|---|---|
| Image | Image brief → reuse approved world/character inputs; if required inputs are missing, approved setup/reference preparation → spec → render → review | Accepted image filed into its set; no animation or composition by default |
| Character | Setup interview → character bible → only the body/head/expression/prop references required by the brief → identity review | Approved character record and accepted/filed references selected in the brief |
| World/location | Setup interview → geography/layout decisions → approval of new facts → only the maps and directional coverage required by the brief → spatial review | Approved selected world/location records and accepted/filed maps or coverage selected in the brief |
| Single animated shot | Video brief → reuse an accepted filed still, or approve explicit missing preparation → motion spec and existing animation gates → review | Accepted clip filed locally; composition only when requested |
| Storied animation | Story foundation → sequence brief → reconciled spatial plan, storyboard, coverage needs and continuity baseline → missing preparation → individual stills and motion → sequence reconciliation → composition → final review | Accepted finished piece with links to its accepted components |

Preparation is conditional, not a mandatory stage. With no approved assets,
intake names the required setup/reference tasks and obtains their approval;
it does not invent inputs or begin generation. Accepted-but-unfiled inputs
require the relevant filing handoff, not replacement generation.

Character and world/location briefs explicitly state whether approved records
alone satisfy the request or which visual references must also be delivered.
Neither an exhaustive reference library nor a speculative new character is
required by default. Each chosen endpoint includes its stated acceptance checks.

Capabilities are described as available/verified from supplied evidence,
requiring preparation, or planned/unimplemented. This design revision does not
verify those labels. New stage names, numbering and output paths remain open.
```

**Verify:** The image route handles an empty asset library; the single-shot route allows direct reuse; every row says where work stops. No route implies permission to render missing assets.

### Task 4 — Add the beginner-facing intake contract

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after routing, before information homes.

```markdown
## Proposed guided intake

Ask “What are we building?” first, then ask small groups of relevant questions
in plain English. Explain a choice before requesting technical detail; offer
options as proposals, not inferred answers. Do not run the entire studio
interview for an image or asset-only request.

Before requesting brief approval, summarize:
- the requested output and where this route stops;
- approved assets to reuse and specifically missing preparation;
- selected work and intentionally skipped work, with reasons;
- observable success criteria and unresolved blocking questions;
- responsible roles and exactly what the requested approval authorizes.

Early composition requirements may inform timing, framing and safe text areas.
They do not authorize generating voice, sound or text into the animation.

Unanswered blocking questions prevent approval. An existing approval is reused
only for its named artifact/version and scope, not as permission for new work.
The user should always be able to explain the next step and the decision being
requested without knowing prompt or provider terminology.
```

**Verify:** The intake produces a decision-ready brief rather than a mandatory list of studio stages.

### Task 5 — Add accountable roles without inventing a team

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after guided intake.

```markdown
## Proposed accountable roles

For each selected work item, identify a producer, a reviewer and a human
approver. The producer prepares the named output; the reviewer checks it
against its brief, references and acceptance criteria; the human approver
accepts or rejects the named version and scope. One person or agent may fill
several responsibilities, but self-review is not independent review.

The owner of a canonical record is responsible for its revision impact. The
receiving producer checks handoff readiness. These are responsibilities within
the selected work, not requirements to recruit additional people or create
extra stages. Passing review or readiness checks is not human approval.

Assignments remain unassigned unless the operator explicitly adopts a default
or names them for this production. Unassigned required responsibilities block
production, not drafting a proposal.
```

D1 is confirmed. Replace the last paragraph with:

```markdown
Jordan has adopted the following default for productions unless explicitly
reassigned: Hermes prepares the work and performs its first review; Jordan is
the human approver. The first review is not independent review. Each production
records the applicable assignments and any reassignment before production.
```

The D1 clarification answer authorizes recording this design default, not beginning production or changing contracts.

**Verify:** No role is falsely assigned, and no agent review substitutes for human approval.

### Task 6 — Add a minimal handoff definition

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after accountable roles.

```markdown
## Proposed handoff requirements

Each selected handoff identifies:
- the approved input artifacts and exact versions, with links to authoritative
  approval/acceptance evidence and existing identity checks where applicable;
- the receiving work item and responsible producer;
- the expected output and its acceptance criteria;
- checks completed, remaining uncertainty and blocking open questions;
- reuse or preparation dependencies and the relevant approval scope.

Record this information in the applicable declared artifact or existing
handoff structure, not a new status tracker. References to approval evidence
are not an independently editable copy of approval state. Exact output homes
will be chosen with the future contracts, not invented in this design.

The receiver confirms readiness before proceeding. Missing required inputs,
unapproved versions or unresolved blocking questions stop that handoff.
Readiness does not itself authorize generation, spending or publication.
```

**Verify:** Handoffs name both what moves and who receives it; status has no new canonical home.

### Task 7 — Resolve canonical ownership boundaries

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Information homes — proposed ownership` (original lines 129–150).

Keep the one-home principle. Replace the table with:

```markdown
| Information | Proposed canonical home |
|---|---|
| This production's audience, purpose, deliverable and finish scope | Production brief |
| Character identity, world time/environment rules, light, palette and materials | Approved character/world/style records through `00_setup` |
| Reusable genre, exclusions and recurring conflict, when selected | Story foundation; its reusable versus production scope requires an explicit decision |
| Particular story events | Sequence brief |
| Fixed spatial facts, landmarks, routes and available camera/staging space | Setup-approved world route map/location plan for facts it owns; a derived map references the existing owner instead of becoming a second source |
| Shot order and composition intent | Storyboard/shot list |
| Time-specific positions, agents present, counts, activation and prop/power states | Sequence continuity record, keyed to shots |
| A shot's action, chosen camera, delivery and success criteria | Shot/video brief; the spec derives execution instructions without independently changing intent |
| Finishing requirements, including voice, sound and text | Composition brief |
| Exact assembly, placement and final timeline decisions | Composition spec derived from its approved brief |
```

Add these boundary rules below the table:

```markdown
A map defines space, not the current position of every movable object.
Continuity defines changing state, not permanent geography. A location plan
identifies available camera space; the storyboard expresses the shot's
composition intent; the shot brief chooses the camera and motion. Conflicts
return to the authoritative upstream record rather than being silently fixed
in a downstream spec.

A map that establishes new spatial facts must receive setup approval. Other
world records link to those facts rather than restating them as separate canon.
Maps derived from existing facts cite their authoritative source versions.

Story-foundation recommendations do not become world facts by inclusion in a
sequence. Production audience and purpose may vary without rewriting the world.
Jordan selected a reusable series foundation plus production-specific choices;
world facts remain in world records. Story-only questions are skipped for
nonnarrative work. No downstream stage writes into `world/`, and approval state
remains in the declared artifacts.
```

The final paragraph records confirmed D2. Do not adopt the document's creative theme, audience or antagonist recommendations while resolving structural ownership.

**Verify:** Each of these questions has one answer: who owns fixed layout, changing folder position, available camera space, chosen camera, production audience, and actual composition timeline? Derived specs may repeat frozen source values with provenance, but cannot independently redefine them.

### Task 8 — Define the narrative planning loop and continuity acceptance

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after information homes and before reference-library design.

```markdown
## Proposed narrative planning and continuity

For narrative work, approve the selected story foundation and sequence intent
before downstream production specifications. Establish maps from approved world
facts, then build the storyboard/shot list explicitly. Use the storyboard to
identify directional coverage, character/head/expression references and props
actually needed for its shots.

Iterate the spatial plan, storyboard, coverage needs and continuity together.
A changed viewpoint may expose missing coverage; a state transition may require
a different shot boundary. Resolve such conflicts in their canonical homes,
then approve the named planning baseline before individual shot production.
Draft planning diagrams do not establish approved world geography.

Each shot links to its intended event, map/reference versions and expected
start and end states. Track the characters present, relevant counts and
positions, prop state and power/activation state. Select fields needed by the
sequence rather than imposing the example scene's props on every story.

Preparation produces only missing approved inputs. If it changes approved
intent or reveals a spatial contradiction, return to planning and apply the
revision rule; do not repair the story through unapproved rendering choices.

After individual clip acceptance, reconcile adjacent clips against their
expected states before composition. An end/start mismatch must either be an
explicitly approved transition or be resolved through the relevant planning
and shot gates. Report what actual outputs show and any review uncertainty;
expected states alone are not evidence of continuity.

Sequence review is an additional acceptance check. It does not revoke historical
clip acceptance, and a locally accepted clip is not automatically suitable for
every sequence. Composition cannot be used to conceal an unresolved continuity
or identity failure without an explicitly approved creative revision.
```

**Verify:** Storyboard creation is explicit, preparation is conditional, and planning iteration is separate from downstream production. Adjacent-shot reconciliation occurs before composition.

### Task 9 — Add bounded revision and re-approval rules

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after the narrative section.

```markdown
## Proposed revision and re-approval rules

A proposed change identifies the canonical fact or artifact, its old and new
versions, the reason and the dependent work that may be affected. New world
facts and revisions of approved world records return through setup; approved
bibles and historical generated content are not rewritten in place.

Assess dependency impact using declared inputs. Keep superseded versions and
historical approvals intact. Flag affected planned or in-progress outputs for
review, and distinguish unchanged reuse from a changed artifact or context.
Approval of an old version never silently approves its replacement.

Re-review is not automatic regeneration. Record why an unchanged asset remains
valid, or identify the smallest revised output requiring new approval. Any new
production remains separately authorized. Where accepted clips no longer fit
a revised sequence, preserve their historical acceptance and review their
suitability for the new sequence explicitly.

Do not introduce new runtime status values or a separate approval tracker in
this design revision. The future contracts must define how dependency impact
and approval evidence are represented in their declared files.
```

**Verify:** A reference change can trigger a bounded review without deleting history, making all old approvals disappear or regenerating everything.

### Task 10 — Add ordered approval views without duplicate rulebooks

**Insert:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, after revision rules.

```markdown
## Proposed route approval gates

This table is an ordered view of the proposed approval points, not a new
executable contract. Existing stage gates remain authoritative until a separate
approved change reconciles the contracts. The intake and handoff sections define
brief/readiness requirements; the sections above define facts, revisions and
continuity; the composition section defines finishing and final acceptance.

| Route | Ordered human approval checkpoints |
|---|---|
| Image | Completed brief/preparation scope → new setup facts if needed → each required image specification and its production authorization → result acceptance and filing |
| Character | Completed scope → character record/new facts → specifications and production authorization for selected visual references only → selected reference acceptance and filing |
| World/location | Completed scope → geography/layout facts and selected map/record approval → specifications and production authorization for selected visual coverage only → selected coverage acceptance and filing |
| Single animated shot | Completed video brief and any source preparation through the existing animation/still handoffs → motion specification and production authorization → clip acceptance and filing → composition and final acceptance only if selected |
| Storied animation | Production scope → selected story foundation and sequence intent → new spatial facts if needed → reconciled storyboard/coverage/continuity baseline → each preparation and shot's existing brief/specification/production/result gates → whole-sequence reconciliation → composition brief/specification and execution authorization → final export acceptance |

A source preparation task follows its own relevant route; it is not blanket
permission for generation. Resolve missing facts and inputs before the
specification that depends on them. An approval request names the artifacts,
versions, checks and actions it covers. Review recommendations and receiver
readiness never substitute for human approval.

Jordan selected grouped approvals at meaningful milestones. List each artifact
and version in the named review package, without skipping a required gate or
approving future outputs.

Publication is not part of any local completion gate. It always requires its
own explicit authorization and a verified receipt. A permission needed for an
intermediate asset publication is also separate; local production approval is
not permission to expose that asset publicly.
```

The presentation paragraph records D4 and the single-shot row records D3, without changing existing contracts. Do not add extra repeated confirmations after a named spec and render have already received scoped approval.

**Verify:** Every route has a visible stop point, preparation keeps its own approvals, and publication never follows automatically from filing.

### Task 11 — Strengthen composition without changing supplied integration statements

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Composition and future integrations` (original lines 222–233).

Retain its supplied integration-status statements and proposed tool names without testing them. Retain its distinction between local filing and publication. Add:

```markdown
The composition brief records finishing intent and acceptance criteria early
when needed. Timing, narration pacing and safe text areas may inform planning,
but voice, sound, accurate on-screen text and assembly are executed only after
the selected animation elements have been built and accepted. Generated
animation is not asked to bake in these finishing elements.

For a sequence, composition receives clips that have passed both individual
acceptance and sequence reconciliation. Approve the composition brief/spec and
execution scope before finishing work. Reuse accepted elements without silently
changing their identity or approved story intent.

Final review evaluates the requested purpose, understandable story or action,
world/character identity, spatial/state continuity, pacing and the selected
voice/sound/text requirements. Audio or text not requested is not a mandatory
addition. Final export acceptance does not authorize publication.
```

Keep D3 consistent: an accepted, filed single clip needs composition only when requested. Avoid duplicating the route table; reference it instead.

**Verify:** Early planning is permitted; executing finishing work is downstream of accepted animation. Clip acceptance is not final-piece acceptance.

### Task 12 — Separate design decisions from later implementation/feasibility work

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Open decisions before extending the framework` (original lines 247–256).

Replace the mixed list with these subsections:

```markdown
### Design decisions

- Confirmed role default: Hermes prepares and reviews; Jordan gives human
  approval unless explicitly reassigned.
- Confirmed story-foundation scope: reusable series foundation plus production
  choices; world facts remain in world records.
- Confirmed single-shot endpoint: accepted, filed clip; composition only when
  requested.
- Confirmed approval presentation: grouped milestones listing each artifact
  and version, without skipping required gates.
- Approve route endpoints, handoff requirements, revision rules and acceptance
  criteria as design decisions, without implying production authorization.
- Adopt, revise or defer the existing creative story-foundation recommendations.
  The operator's scene concept remains a concept until separately briefed.

### Later structural implementation — separately authorized

- Approve exact structural scope, stage homes and output paths.
- Reconcile optional routing, declared approvals and reference versioning with
  existing setup/image/animation contracts, preserving accepted records.
- Choose canonical homes for stable rules and templates without duplicate
  pipelines or parallel status systems.
- Implement and validate only the explicitly approved structural scope.

### Later technical feasibility and production — separately authorized

- Assess any reference-image, end-frame, geometry-control or composition-route
  dependency actually needed by an approved production scope.
- Treat named integrations as proposed choices until the appropriate separate
  work establishes their status; do not narrow this outcome on assumed limits.
- Authorize any real-output trial, asset generation, spending or publication
  separately. Develop the five agents and detailed scene only when requested.
```

The first four bullets record confirmed D1–D4. The other listed approvals remain open. Keep `Proposed implementation scope — still awaiting approval` and its current non-authorization statement intact.

**Verify:** A future implementer can distinguish adopting a design from permission to build, investigate or produce.

### Task 13 — Replace generic acceptance prose with observable checks

**Modify:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md`, `Acceptance checks for a future extension` (original lines 258–266).

Use this checklist, which describes later validation rather than claiming it was performed:

```markdown
Validate the future extension through document walkthroughs first, followed by
a separately authorized representative real-output trial. Document checks do
not establish working integrations or prove generated-media quality.

- Each of the five intake answers reaches the correct route and accepted
  endpoint, with understandable choices and approval requests.
- An empty approved-asset library yields named preparation tasks and a stop for
  approval; existing suitable accepted assets are reused without replacements.
- Asset-only requests omit story and animation work. Single shots omit finishing
  unless it is selected under the adopted intake rule.
- Every selected handoff resolves to the authoritative input versions, approval
  evidence, expected output, responsible roles and readiness checks.
- Fixed geography, changing state and camera choices have distinct canonical
  owners; new facts cannot enter the world through downstream specifications.
- Story foundation, sequence events, maps, storyboard, coverage requirements,
  continuity states and shots are linked and reconciled before shot production.
- Each shot has observable start/end-state criteria. Accepted adjacent clips
  are reconciled before composition, including any explicitly approved transition.
- A revised input triggers bounded dependency review; historical accepted
  artifacts remain intact and replacement approvals are explicit.
- Composition uses accepted elements and does not substitute for unresolved
  identity or continuity review. Early finishing requirements are not baked
  into generated animation.
- Final acceptance evaluates purpose, clarity, consistency, continuity, pacing
  and selected finishing requirements separately from clip acceptance.
- Current production capability checks remain in their authorized production
  contracts before spending. This outcome review does not perform them.
- Review uncertainty remains visible. Local acceptance/filing never authorizes
  external publishing, and publication needs its own authorization and receipt.
```

**Verify:** Checks judge outcomes, not merely whether contract files exist. Do not report the real-output trial as run during this revision.

### Task 14 — Run document validation and report the bounded result

**File:** `/opt/data/hermes-world-engine/_reference/studio-extension-design.md` — read only.

Run the validation commands below. Then perform the tabletop cases and return a concise summary of revised sections, preserved sections, adopted versus still-open decisions and the actual check results. Do not commit or implement the workflow. If later explicitly asked to commit, handle that as a separately authorized, path-scoped operation; do not stage unrelated files.

## Tests and validation

This is a documentation task, not a code task. Do not add artificial application tests, test scaffolds or dependencies. Use baseline/protected-content checks, explicit walkthroughs and whitespace inspection. The commands below are planned verification; they were not represented as passed during planning.

### Structural and preservation check

Run this unchanged from `/opt/data/hermes-world-engine` before the edits to establish missing proposed sections, then after Task 13. The first run should report missing new sections and exit nonzero while all protected-content checks pass; the second should print `PASS document structure and protected evidence` and exit zero.

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
import sys

p = Path('_reference/studio-extension-design.md')
text = p.read_text()
errors = []

def section(title):
    marker = '## ' + title
    if text.count('\n' + marker + '\n') != 1:
        errors.append('Expected one section: ' + title)
        return ''
    return marker + text.split(marker, 1)[1].split('\n## ', 1)[0]

protected = {
    'Outcome-focused review rules — confirmed by Jordan': 'b0f85dcfdcb3f3841077df725688aebc1133c7d24c043b9adc6974bef3624234',
    'Existing, exercised workflow': '137fee6f9d09dd2e5398cb8fca2a87fea51f40e88392311bb6d5c9ca767949a2',
    'Story-foundation questions and unapproved recommendations': '3e699f6f8b8aefc14ae9e99542923595714d2e58959e23233b257dc3ac7cd7e2',
    "Jordan's Agents as Folders scene concept": '0958d6cc416aca78eb16ad9b335a3c036e8001a0d2c9827950f3cf59905e08e6',
}
for title, expected in protected.items():
    if hashlib.sha256(section(title).encode()).hexdigest() != expected:
        errors.append('Protected evidence changed: ' + title)

for title in (
    'Proposed guided intake',
    'Proposed accountable roles',
    'Proposed handoff requirements',
    'Proposed narrative planning and continuity',
    'Proposed revision and re-approval rules',
    'Proposed route approval gates',
):
    section(title)

frontmatter = text.split('---', 2)[1]
for required in ('kind: design-reference', 'status: draft', 'implementation: proposed-extension'):
    if required not in frontmatter.splitlines():
        errors.append('Authority metadata changed: ' + required)

routing = section('Proposed optional routing')
for label in ('Image', 'Character', 'World/location', 'Single animated shot', 'Storied animation'):
    if routing.count('| ' + label + ' |') != 1:
        errors.append('Expected one route row: ' + label)

for required in (
    'No structural implementation, integrations, new renders, paid calls, publication,',
    'commit or push is authorized by this retention request.',
    'ElevenLabs is a proposed audio-asset source; Remotion is a proposed composition/',
    'rendering tool. Neither is installed or verified by this design record.',
):
    if required not in text:
        errors.append('Preserved boundary or supplied statement missing: ' + required)

if errors:
    print('\n'.join('FAIL ' + error for error in errors))
    sys.exit(1)
print('PASS document structure and protected evidence')
PY
```

This check verifies document shape and exact preservation, not editorial quality or technical feasibility. If preservation fails, inspect the patch rather than automatically restoring the whole file. Do not relax hashes simply to make an unintended edit pass.

### Whitespace and scope checks

```bash
git diff --check
git diff --stat
git status --short
python3 - <<'PY'
from pathlib import Path
p = Path('_reference/studio-extension-design.md')
text = p.read_text()
assert text.endswith('\n'), 'Missing final newline'
assert all(line == line.rstrip() for line in text.splitlines()), 'Trailing whitespace'
print('PASS design whitespace')
PY
```

Expected: no whitespace errors. Because the design is currently untracked, `git diff` may not display its edits; the explicit content checks still apply. Do not use `git add` merely to obtain a diff. The only intentional changed project document is the design; the plan is the already-authorized planning artifact. Report unrelated existing changes without modifying them.

### Tabletop cases — no tools, renders or invented production artifacts

Read the revised document as an unfamiliar operator. These are design scenarios, not claims of successful production.

| Case | Required conclusion |
|---|---|
| Image request with suitable approved assets | Reuse them; brief/spec/review/filing only; no replacement or narrative work |
| Image request with no approved world/character inputs | Explicit setup/reference preparation with approval; stop before unapproved generation |
| Character request | Agreed identity record plus only references selected in the brief; no default animation |
| World/location request | New spatial facts are approved before dependent coverage; scope ends at agreed records/coverage |
| Single shot with accepted filed still | Direct reuse and existing motion gates; no new reference production unless needed and approved; D3 determines finish endpoint |
| Storied animation | Explicit storyboard construction, spatial/coverage/continuity reconciliation, linked shots, sequence review, then composition |
| Reference changes after shot acceptance | Preserve accepted history; identify dependency impact; re-review suitability; no automatic mass regeneration |
| Adjacent individually accepted clips conflict | Sequence review stops composition until an approved transition or revision resolves the mismatch |
| Narration and title requested | Plan pacing/safe area early; execute voice/text in composition after accepted animation |
| Ready for final export | Evaluate final purpose and selected finishing separately; publication remains unauthorized |

For each case, the reader must be able to identify the next artifact, its authoritative inputs, the responsible role, the required approval and the stopping condition. If not, revise the responsible proposed section rather than adding another parallel checklist.

## Risks, tradeoffs and stop rules

- **Document bloat:** Add operational precision, not a second full framework. Each rule has one explanatory home; route tables are compact views. Do not add schemas, adapters, exhaustive libraries or new numbered stages.
- **False adoption:** Jordan's clarification answers settle D1–D4 as design choices only. Review findings and this plan do not approve other proposals, creative canon or implementation. Preserve explicit proposal labels elsewhere.
- **Ownership collisions:** Maps must not compete with world records, nor handoff summaries with approval metadata. Derivation and authoritative ownership are different.
- **Approval fatigue:** Related approvals may be packaged only if D4 permits; package contents and versions are named, and future outputs are never preaccepted.
- **Revision overreach:** Re-review is not revoking historical acceptance, copying an old approval onto a new output or automatically regenerating all dependents.
- **Stage drift:** The proposed optional routing is not the current executable contract. Do not resolve that gap by editing root or stage contracts in this task.
- **Evidence degradation:** Protect historical status, scene concept and unadopted creative recommendations. Technical uncertainty is deferred, not converted into outcome restrictions.
- **Source changed:** If the current file no longer matches the baseline, re-read and reconcile before editing; do not assume this plan supersedes newer user work.
- **No commit authorization:** The generic preference for frequent commits does not authorize a commit here. No commit or push occurs during this plan or the proposed document-only edit without a separate request.

## Completion and handoff

Planning is complete: the plan is saved and D1–D4 have been answered and recorded. The future document revision is complete only after scoped edit authorization, the targeted patches, preservation/structure checks and tabletop review. Offer to apply the document-only revision; do not begin it or structural studio implementation in this planning turn.

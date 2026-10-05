---
kind: design-reference
status: draft
implementation: proposed-extension
sources:
  - desktop conversation, session 20261003_203006_dd142b
  - existing CONTEXT.md and 04_animate/CONTEXT.md
  - operator-supplied MOA response and combined-review discussion in the current desktop conversation
---

# Studio extension — retained design and open decisions

## Purpose and authority

Capture the discussion for future framework development. This is a design
reference, not an executable stage contract, an approved story bible, or authority
to generate assets. Jordan requested retention; that does not approve every
assistant recommendation or authorize structural implementation.

The canonical workspace is `/opt/data/hermes-world-engine/`. Existing contracts
and approved world records remain authoritative. This document does not modify
them. Future implementation must reconcile these proposals with those contracts.

The proposed operating rules below consolidate the single-model and
operator-supplied MOA reviews. Both reviews had the design text available;
file access versus pasted text is not an evidence-quality distinction.
These recommendations remain proposals unless explicitly adopted by Jordan.
Adoption of a design decision is separate from authorization to change stage
contracts, generate assets, spend, publish or commit. Jordan authorized this
document-only revision, not implementation of the studio.

Implementation-status statements are retained as supplied historical evidence.
This revision neither verifies nor updates them. Technical feasibility remains
a separately authorized task and is not used here to narrow the desired studio
outcome.

## Confirmed direction from Jordan

- Connect world/character creation and animation in one optional, routed workflow.
- The opening question is: **What are we building?** An image, a character,
  a world or location, a single animated shot, or a storied animation.
- The answer selects the required path. Stages can be prebuilt without being
  used for every request. Do not automatically force animation on image work.
- Build a complete brief before deriving its specification. Help a beginner
  understand possibilities through a guided interview rather than expecting
  technical prompt vocabulary.
- Spatial maps should establish reference geography for location coverage and
  successive shots, not merely serve as decorative images.
- Develop multi-angle world/character references and detailed head views to
  support turns, camera changes, facial close-ups and expressions.
- Voice, on-screen text and related finishing belong in **composition after
  animation elements are built and accepted**. ElevenLabs and Remotion are later
  additions, not currently proven integrations.
- The long-term direction is a full studio. Preserve existing accepted assets
  and approval boundaries while extending it.

## Outcome-focused review rules — confirmed by Jordan

These rules govern advisor review and aggregator synthesis of this design.
They do not authorize implementation or change the production-stage checks.

- Review only the supplied plan against the stated desired outcome: optional
  intake routing, consistent world/character assets, brief-led animation,
  sequence continuity, and composition after accepted animation elements.
- Identify outcome gaps, unsupported planning assumptions, missing accountable
  owners, unclear handoffs, acceptance criteria, scope boundaries and approval
  gates. Explain each recommended change in terms of the desired outcome.
- Do not assess whether supporting tools can achieve the outcome. Do not test,
  probe, research or diagnose tools, providers, APIs, credentials, integrations,
  network services or current availability. Do not request those checks from
  the acting agent as part of this review.
- Tool names in the plan are implementation placeholders, not invitations for a
  capability audit. Do not reject, narrow or redesign the desired outcome based
  on assumed tool limitations. Mark implementation dependencies as deferred to a
  separately authorized technical-feasibility task; do not resolve them here.
- Cloudflare or any other service is not a review subject unless Jordan
  explicitly requests a separate viability study. Inference transport errors
  are runtime incidents, not findings about the studio plan or evidence that an
  advisor investigated a supporting tool.
- Use supplied evidence only. Cite plan sections for findings. Keep confirmed
  direction separate from proposals and unknowns; do not invent owners or approval.
- Each advisor should return: outcome gap or planning assumption; plan evidence;
  proposed change and why; owner role required (unassigned unless supplied);
  approval gate. An acceptable finding can be that no gap was identified.
- The aggregator must cite actual returned advisor labels and recommendations
  used, distinguish its own synthesis, and disclose unavailable advisors. Never
  attribute findings to configured advisors whose output was not received.

Production feasibility checks already required by `04_animate` remain in force
before rendering/spending. Their existence can be reviewed as a handoff or gate;
their technical conclusions are outside this outcome-focused review.

## Existing, exercised workflow

The workspace has `00_setup`, `01_spec`, `02_render`, `03_file`, and `04_animate`.
The animation contract supports:

Draft video brief → source/tool feasibility → brief approval → derived motion
spec → spec/render approval → verified reference URL → native video render →
visual-consistency and motion-success review → acceptance → local manifest filing.

Two accepted videos exist under `runs/motion/location-probes/`:
- `hermes-sky-bridges-and-passages/04-video-1.mp4`
- `hermes-sky-bridges-destination-walk/04-video-1.mp4`

The second variation completed the expanded brief-led path. The first accepted
video is preserved. Its presence here does not assert that any missing backlog
manifest filing was performed.

Verified rendering route: native Hermes `video_generate`, configured Nous router,
`bytedance/seedance-2.5`; returned backend FAL image-to-video. Configuration and
artifacts are local; inference is remote. The tested delivery is roughly five
seconds, 16:9, 720p, silent, no upscale. Recheck current configuration/schema
before future use; these are verified examples, not permanent universal limits.

The observed callable schema accepts one public HTTPS `image_url`; descriptive
mentions of references do not establish callable multi-reference support. Source
URLs were anonymously fetched and hash-matched. New publication requires approval.
Full-video analysis failed on its active provider; sampled inspection, including
exact first/last frames, was used and its limitations retained.

Commit `a0d1a1b` retained the animation workflow and videos locally. The proposed
studio extensions below were not implemented by that commit. Push was not performed.

## Proposed optional routing

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

Jordan has adopted the following default for productions unless explicitly
reassigned: Hermes prepares the work and performs its first review; Jordan is
the human approver. The first review is not independent review. Each production
records the applicable assignments and any reassignment before production.

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

## Information homes — proposed ownership

One fact has one canonical home. Downstream outputs reference it rather than
silently redefining it.

| Information | Proposed canonical home |
|---|---|
| This production's audience, purpose, deliverable and finish scope | Production brief |
| Character identity, world time/environment rules, light, palette and materials | Approved character/world/style records through `00_setup` |
| Reusable genre, exclusions and recurring conflict, when selected | Reusable series story foundation; production-specific choices remain in the production brief |
| Particular story events | Sequence brief |
| Fixed spatial facts, landmarks, routes and available camera/staging space | Setup-approved world route map/location plan for facts it owns; a derived map references the existing owner instead of becoming a second source |
| Shot order and composition intent | Storyboard/shot list |
| Time-specific positions, agents present, counts, activation and prop/power states | Sequence continuity record, keyed to shots |
| A shot's action, chosen camera, delivery and success criteria | Shot/video brief; the spec derives execution instructions without independently changing intent |
| Finishing requirements, including voice, sound and text | Composition brief |
| Exact assembly, placement and final timeline decisions | Composition spec derived from its approved brief |

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
world facts remain in world records. A production-specific departure from
approved series rules requires explicit approval, not a silent canon override.
Story-only questions are skipped for nonnarrative work. No downstream stage
writes into `world/`, and approval state remains in the declared artifacts.

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

Preparation produces only missing inputs within the approved scope; the
resulting versions require approval/acceptance before use. If preparation
changes approved intent or reveals a spatial contradiction, return to planning
and apply the revision rule; do not repair the story through unapproved
rendering choices.

After individual clip acceptance, reconcile adjacent clips against their
expected states before composition. An end/start mismatch must either be an
explicitly approved transition or be resolved through the relevant planning
and shot gates. Report what actual outputs show and any review uncertainty;
expected states alone are not evidence of continuity.

Sequence review is an additional acceptance check. It does not revoke historical
clip acceptance, and a locally accepted clip is not automatically suitable for
every sequence. Composition cannot be used to conceal an unresolved continuity
or identity failure without an explicitly approved creative revision.

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

## Reference-library design

- **World route map:** named locations, relative placement and connections.
- **Location plan:** top-down arrangement of roads, entrances, buildings,
  banners, hazards, staging areas, walkable routes and camera positions.
- **Directional location coverage:** approved forward/reverse/side and elevated
  views required by the storyboard. Validate landmarks and geography together.
- **Body turnaround:** front, rear, profiles and selected three-quarter views;
  consistent proportions, outfit, helmet, footwear, bag and staff.
- **Head-angle references:** detailed face identity at selected angles.
- **Expression references:** separate approved expression states preserving identity.
- **Prop references:** folder, bag, banner and caduceus states when required.

Derive existing geography from selected approved records, explicitly marking
unknown connections or dimensions. Obtain approval for new spatial facts. A
proposed map does not silently override accepted images or approved bibles.

These are 2D references, not a navigable 3D scene, independent animation layers,
or guaranteed cross-view consistency. Exact geometry/unrestricted camera motion
would require a separately chosen geometry-controlled workflow. Multi-reference
conditioning requires a verified route; do not invent unsupported parameters.
For facial shots, approve a detailed close-up starting still. A wide image or
long zoom does not reliably recover established facial microdetail.

## Story-foundation questions and unapproved recommendations

Jordan supplied these decision categories: audience; when; where; natural versus
human landscape; genre (horror/romance excluded); antagonist (society, corporation,
individual, group or abstract). The recommendations below remain proposals:

| Category | Assistant recommendation — not yet adopted |
|---|---|
| Audience | Adults curious about AI but overwhelmed by complexity, especially creators, consultants and small-business operators |
| When | Timeless classical-influenced mythic age, not historical Greece/Rome |
| Where | Existing Hermetic Gates world and its named locations |
| Environment | Built inhabited landscape integrated with mountains, ravines, trees and gardens |
| Genre | Mythic adventure, discovery and light character comedy |
| Antagonist | Fragmentation: knowledge/context separated and coordination obstructed; not necessarily a visible villain |

Proposed theme: Hermes connects what fragmentation separated; each folder gives
an agent purpose, and the team accomplishes what isolated effort cannot.
This is not approved canon or settled market positioning.

## Jordan's Agents as Folders scene concept

Retained as an operator-provided concept, not a completed approved sequence brief:

1. Hermes walks down the road and stops before the temple-like building at left.
2. The camera moves behind him and up, looking down at the space in front of him.
3. He takes five folders from his courier bag and places each separately.
4. He raises his caduceus skyward. Golden magic lights the sun symbol on the
   banner hanging from the temple.
5. The symbol sends a golden beam into the caduceus, powering it.
6. Hermes directs that energy into the first folder; an agent materializes.
7. He repeats this for all five folders, yielding five agents: Agentsasfolders.

The exact building identity, spatial layout, five character identities, bag and
folder designs, duration, shot count and final framing remain unresolved. The
concept does not authorize new characters, world changes, publication or spending.

Suggested shot groupings: arrival; rear/elevated reveal; folder placement;
banner activation; power transfer; individual summons; final group tableau.
These are storyboard proposals, not fixed shot counts. Avoid assuming one
complex generation can reliably execute counting, camera travel, hand interaction,
energy transfer and persistent multi-character emergence.

Continuity should track folder positions/activation, agents already present,
Hermes's location, bag/staff state and banner power. A map preserves space;
continuity preserves changes over time.

## Composition and future integrations

The composition brief records finishing intent and acceptance criteria early
when needed. Timing, narration pacing and safe text areas may inform planning,
but voice, sound, accurate on-screen text and assembly are executed only after
the selected animation elements have been built and accepted. Generated
animation is not asked to bake in these finishing elements.

For a sequence, composition receives clips that have passed both individual
acceptance and sequence reconciliation. Approve the composition brief/spec and
execution scope before finishing work. Reuse accepted elements without silently
changing their identity or approved story intent. Arrange accepted clips and add
the selected voice, music, effects and titles/captions, then render and review
the finished piece.

ElevenLabs is a proposed audio-asset source; Remotion is a proposed composition/
rendering tool. Neither is installed or verified by this design record. Accurate
text belongs in composition, not a request for image/video models to draw it.

Existing stills and animations remain reusable independently of composition.
As defined in the routing table, a single animated shot ends at an accepted,
filed clip unless composition is requested.
Final export acceptance is separate from individual clip acceptance. Publication
requires its own authorization and receipt.

Final review evaluates the requested purpose, understandable story or action,
world/character identity, spatial/state continuity, pacing and the selected
voice/sound/text requirements. Audio or text not requested is not a mandatory
addition.

## Proposed implementation scope — still awaiting approval

- Update root intake routing and mirrored `CLAUDE.md`/`AGENTS.md`.
- Add intake, story/sequence planning and assembly/composition contracts,
  with templates and stable rules appropriate to the workspace's dialect.
- Connect selected setup/reference/image/motion handoffs without duplicate pipelines.
- Add routing, approval-gate, continuity and output-integrity tests.
- Preserve approved world records, historical briefs/specs and accepted assets.

No structural implementation, integrations, new renders, paid calls, publication,
commit or push is authorized by this retention request.

## Open decisions before extending the framework

### Design decisions

- Confirmed role default: Hermes prepares and reviews; Jordan gives human
  approval unless explicitly reassigned. See **Proposed accountable roles**.
- Confirmed story-foundation scope: reusable series foundation plus production
  choices; world facts remain in world records. See **Information homes**.
- Confirmed single-shot endpoint: accepted, filed clip; composition only when
  requested. See **Proposed optional routing**.
- Confirmed approval presentation: grouped milestones listing each artifact
  and version, without skipping required gates. See **Proposed route approval gates**.
- Approve remaining route endpoints, handoff requirements, revision rules and
  acceptance criteria as design decisions, without implying production authorization.
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

## Acceptance checks for a future extension

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

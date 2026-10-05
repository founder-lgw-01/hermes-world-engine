"""Offline contract checks for the optional studio; no media or service calls.

These tests exercise routing, template defaults and declared handoff integrity.
They do not claim that an agent obeyed a gate or that a media adapter works.
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = (
    "studio/CONTEXT.md",
    "studio/00_intake/CONTEXT.md",
    "studio/01_story/CONTEXT.md",
    "studio/02_sequence/CONTEXT.md",
    "05_compose/CONTEXT.md",
)
REFERENCES = (
    "_reference/studio-rules.md",
    "_reference/spatial-rules.md",
    "_reference/composition-rules.md",
)
TEMPLATES = {
    "studio-intake": "studio/00_intake",
    "story-foundation": "studio/01_story",
    "sequence-brief": "studio/02_sequence",
    "storyboard": "studio/02_sequence",
    "continuity": "studio/02_sequence",
    "sequence-review": "studio/02_sequence",
    "spatial-map": "00_setup",
    "composition-brief": "studio/00_intake",
    "composition-spec": "05_compose",
    "composition-record": "05_compose",
}
OUTPUTS = (
    "runs/studio/<production>/00-intake-N.md",
    "runs/studio/<production>/00-composition-N.md",
    "stories/<series>/01-foundation-N.md",
    "runs/studio/<production>/02-sequence-N.md",
    "runs/studio/<production>/02-storyboard-N.md",
    "runs/studio/<production>/02-continuity-N.md",
    "runs/studio/<production>/02-review-N.md",
    "world/environment/maps/<map>-N.md",
    "runs/studio/<production>/05-spec-N.md",
    "runs/studio/<production>/05-record-N.md",
    "runs/studio/<production>/05-final-N.<ext>",
)


def read(path: str) -> str:
    return (ROOT / path).read_text()


def frontmatter(text: str) -> dict[str, str]:
    """Read the scalar header fields used by these tests, not a YAML parser."""
    header = text.split("---", 2)[1]
    return {
        key.strip(): value.strip()
        for line in header.splitlines()
        if ":" in line
        for key, value in [line.split(":", 1)]
    }


def route_rows() -> dict[str, list[str]]:
    rows = {}
    for line in read("studio/CONTEXT.md").splitlines():
        if line.startswith("| "):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if cells[0] in {
                "Image", "Character", "World/location",
                "Single animated shot", "Storied animation",
            }:
                if cells[0] in rows:
                    raise AssertionError("Duplicate route: " + cells[0])
                rows[cells[0]] = cells
    return rows


class StudioContractsTests(unittest.TestCase):
    def test_required_contracts_references_and_templates(self) -> None:
        required = CONTRACTS + REFERENCES + tuple(
            "_templates/" + name + ".md" for name in TEMPLATES
        )
        self.assertEqual([p for p in required if not (ROOT / p).is_file()], [])

    def test_stage_contracts_have_inputs_exclusions_outputs_and_human_gate(self) -> None:
        for path in CONTRACTS[1:]:
            with self.subTest(path=path):
                text = read(path)
                for marker in ("## Inputs", "Do NOT load:", "## Process",
                               "## Outputs", "## Human check"):
                    self.assertIn(marker, text)
                self.assertIn("status: approved", text)
                self.assertLessEqual(len(text.splitlines()), 90)

    def test_concrete_relative_document_links_resolve(self) -> None:
        for path in CONTRACTS + REFERENCES:
            for link in re.findall(r"`([^`\n]+\.md)`", read(path)):
                if "<" in link or "-N.md" in link:
                    continue
                # Contracts use paths relative to their folders. Rule docs
                # declare workspace-relative paths so their template paths copy.
                base = ROOT / path
                target = base.parent / link if link.startswith(".") else ROOT / link
                with self.subTest(path=path, link=link):
                    self.assertTrue(target.resolve().is_relative_to(ROOT))
                    self.assertTrue(target.is_file(), str(target))

    def test_new_templates_start_draft_and_have_provenance(self) -> None:
        for name, stage in TEMPLATES.items():
            with self.subTest(template=name):
                metadata = frontmatter(read("_templates/" + name + ".md"))
                self.assertEqual(metadata["status"], "draft")
                self.assertEqual(metadata["stage"], stage)
                self.assertIn("generated", metadata)
                self.assertIn("sources", metadata)
        for name in ("sequence-review", "composition-record"):
            self.assertEqual(
                frontmatter(read("_templates/" + name + ".md"))["verdict"], ""
            )

    def test_output_registry_and_copy_targets_agree(self) -> None:
        rules = read("_reference/studio-rules.md")
        templates = "\n".join(read("_templates/" + n + ".md") for n in TEMPLATES)
        contracts = "\n".join(read(p) for p in CONTRACTS)
        for path in OUTPUTS:
            with self.subTest(path=path):
                self.assertIn(path, rules)
                self.assertIn(path, templates)
                self.assertIn(path, contracts)

    def test_root_routes_and_mirrored_agent_instructions(self) -> None:
        self.assertEqual(read("CLAUDE.md"), read("AGENTS.md"))
        self.assertIn("studio/CONTEXT.md", read("CLAUDE.md"))
        for path in CONTRACTS:
            self.assertIn(path, read("CONTEXT.md"))
        self.assertIn("declared inputs", read("CONTEXT.md"))
        self.assertNotIn("until the stage before it is approved", read("CONTEXT.md"))


class StudioRoutingTests(unittest.TestCase):
    def test_five_deliverables_and_explicit_endpoints(self) -> None:
        rows = route_rows()
        self.assertEqual(set(rows), {
            "Image", "Character", "World/location", "Single animated shot",
            "Storied animation",
        })
        for row in rows.values():
            self.assertEqual(len(row), 4)
            self.assertTrue(row[3])
        self.assertIn("00_intake/CONTEXT.md", read("studio/CONTEXT.md"))
        self.assertIn("What are we building?", read("studio/00_intake/CONTEXT.md"))

    def test_asset_routes_skip_narrative_and_composition(self) -> None:
        for name in ("Image", "Character", "World/location"):
            required = route_rows()[name][1]
            for excluded in ("01_story", "02_sequence", "04_animate", "05_compose"):
                self.assertNotIn(excluded, required)
        self.assertIn("01_spec", route_rows()["Image"][1])
        self.assertIn("03_file", route_rows()["Image"][1])

    def test_single_shot_finishing_is_conditional(self) -> None:
        row = route_rows()["Single animated shot"]
        self.assertIn("04_animate", row[1])
        self.assertNotIn("05_compose", row[1])
        self.assertIn("05_compose", row[2])
        self.assertIn("only when requested", row[2])
        self.assertIn("accepted, filed clip", row[3].lower())

    def test_story_route_connects_planning_shots_review_and_composition(self) -> None:
        row = route_rows()["Storied animation"][1]
        for marker in ("01_story", "02_sequence", "01_spec", "04_animate", "05_compose"):
            self.assertIn(marker, row)
        self.assertLess(row.index("01_story"), row.index("01_spec"))
        self.assertLess(row.index("04_animate"), row.rindex("02_sequence"))
        self.assertLess(row.rindex("02_sequence"), row.index("05_compose"))

    def test_cold_start_reuse_and_explicit_preparation_are_not_auto_generation(self) -> None:
        rules = read("_reference/studio-rules.md")
        for required in ("no approved assets", "Accepted-but-unfiled",
                         "not permission to generate", "Unassigned",
                         "not a second status tracker"):
            self.assertIn(required, rules)
        intake = read("_templates/studio-intake.md")
        for heading in ("Outcome", "Roles", "Selected route", "Assets and preparation",
                        "Handoff", "Acceptance criteria", "Approval scope", "Open"):
            self.assertIn("## " + heading, intake)


class StudioGateTests(unittest.TestCase):
    def test_grouped_drafts_do_not_create_circular_hash_dependencies(self) -> None:
        rules = read("_reference/studio-rules.md")
        self.assertIn("Do not hash sibling drafts", rules)
        self.assertIn("after the whole package is approved", rules)

    def test_composition_routes_missing_planning_back_to_intake(self) -> None:
        contract = read("05_compose/CONTEXT.md")
        self.assertIn("../studio/00_intake/CONTEXT.md", contract)
        self.assertIn("Require the selected spec to say `status: approved`", contract)

    def test_image_and_motion_briefs_do_not_auto_approve_or_omit_context(self) -> None:
        for name in ("shot-brief", "motion-brief"):
            text = read("_templates/" + name + ".md")
            self.assertEqual(frontmatter(text)["status"], "draft")
            self.assertIn("## Studio handoff", text)
            self.assertIn("none for a standalone", text)
        self.assertIn("complete brief approval", read("01_spec/CONTEXT.md"))
        for path in ("01_spec/CONTEXT.md", "04_animate/CONTEXT.md"):
            self.assertIn("studio-rules.md", read(path))
        for path in ("_reference/spec-rules.md", "_reference/motion-rules.md"):
            self.assertIn("Studio handoff", read(path))
            self.assertIn("SHA-256", read(path))

    def test_spatial_facts_have_setup_ownership_and_immutable_versions(self) -> None:
        self.assertIn("spatial-map mode", read("00_setup/CONTEXT.md"))
        self.assertIn("spatial-rules.md", read("00_setup/CONTEXT.md"))
        self.assertIn("environment-map", read("_reference/world-routing-schema.md"))
        rules = read("_reference/spatial-rules.md")
        for required in ("stated", "inferred", "unknown", "new version",
                         "approved index", "00_setup", "No downstream"):
            self.assertIn(required, rules)

    def test_continuity_models_states_and_observed_adjacent_clip_review(self) -> None:
        continuity = read("_templates/continuity.md")
        for required in ("## States", "## Shot transitions", "Start state ID",
                         "End state ID", "Transition approval"):
            self.assertIn(required, continuity)
        review = read("_templates/sequence-review.md")
        for required in ("## Selected clips", "## Observed states",
                         "## Adjacent-shot reconciliation", "## Open",
                         "Timestamp/evidence"):
            self.assertIn(required, review)
        contract = read("studio/02_sequence/CONTEXT.md")
        self.assertIn("verdict: accepted", contract)
        self.assertIn("before composition", contract)

    def test_revision_and_approval_rules_do_not_transfer_old_acceptance(self) -> None:
        rules = read("_reference/studio-rules.md")
        for required in ("## Revision impact", "not automatic regeneration",
                         "historical acceptance", "receiving producer",
                         "not independent review", "every artifact and version",
                         "recorded SHA-256"):
            self.assertIn(required, rules)

    def test_composition_halts_without_accepted_inputs_or_authorized_adapter(self) -> None:
        contract = read("05_compose/CONTEXT.md")
        for required in ("status: approved", "verdict: accepted", "02-review-N.md",
                         "No composition adapter", "Stop before execution"):
            self.assertIn(required, contract)
        rules = read("_reference/composition-rules.md")
        for required in ("after animation", "not baked", "separately authorized",
                         "source in/out", "final export", "publication"):
            self.assertIn(required, rules)
        record = read("_templates/composition-record.md")
        self.assertIn("Final file SHA-256", record)
        self.assertIn("## Acceptance evidence", record)
        self.assertIn("## Sequence and composition review", read("_reference/drift-checklist.md"))


if __name__ == "__main__":
    unittest.main()

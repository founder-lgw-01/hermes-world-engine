"""Smoke checks for the routable Character World Engine scaffold."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ScaffoldTests(unittest.TestCase):
    def test_required_routing_and_stage_contracts_exist(self) -> None:
        required = (
            "CLAUDE.md",
            "AGENTS.md",
            "CONTEXT.md",
            "00_setup/CONTEXT.md",
            "01_spec/CONTEXT.md",
            "02_render/CONTEXT.md",
            "03_file/CONTEXT.md",
            "04_animate/CONTEXT.md",
            "_reference/motion-rules.md",
            "_templates/motion-brief.md",
            "_templates/motion-record.md",
            "_templates/motion-manifest.md",
            "_templates/shot-brief.md",
        )

        missing = [path for path in required if not (ROOT / path).is_file()]

        self.assertEqual(missing, [])

    def test_native_motion_route_and_output_conventions(self) -> None:
        contract = (ROOT / "04_animate/CONTEXT.md").read_text()
        host = (ROOT / "_reference/host.md").read_text()
        template = (ROOT / "_templates/motion-record.md").read_text()
        self.assertIn("native `video_generate`", contract)
        self.assertIn("01-spec-N.md", contract)
        self.assertIn("image_url", contract)
        self.assertNotIn("04-spec-N.md", contract)
        self.assertNotIn("Import the still with", contract)
        self.assertIn("video_gen.provider: nous", host)
        self.assertIn("video_gen.model: bytedance/seedance-2.5", host)
        self.assertIn("source URL:", template)
        self.assertIn("returned provider:", template)
        self.assertEqual(
            (ROOT / "CLAUDE.md").read_bytes(),
            (ROOT / "AGENTS.md").read_bytes(),
        )


class BriefLedMotionTests(unittest.TestCase):
    def test_brief_starts_draft_and_covers_the_video(self) -> None:
        brief = (ROOT / "_templates/motion-brief.md").read_text()
        self.assertIn("status: draft", brief)
        self.assertNotIn("status: approved", brief)
        for heading in ("Outcome", "Reference and entry mode", "Starting state",
                        "Primary action", "Sequence", "Secondary motion", "Camera",
                        "What stays consistent", "Delivery", "Success checks",
                        "Feasibility check"):
            self.assertIn("## " + heading, brief)

    def test_motion_has_separate_gates_and_review(self) -> None:
        contract = (ROOT / "04_animate/CONTEXT.md").read_text()
        rules = (ROOT / "_reference/motion-rules.md").read_text()
        record = (ROOT / "_templates/motion-record.md").read_text()
        for text in ("brief approval", "explicit approval of `01-spec-N.md`",
                     "manifest.md", "operator acceptance", "new shot"):
            self.assertIn(text, contract)
        self.assertIn("Preserve identity and visual design, not a frozen pose", rules)
        self.assertIn("## Visual consistency findings", record)
        self.assertIn("## Motion success findings", record)
        self.assertIn("Acceptance evidence", (ROOT / "_templates/motion-manifest.md").read_text())


if __name__ == "__main__":
    unittest.main()

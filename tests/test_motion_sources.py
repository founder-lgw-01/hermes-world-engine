"""Offline checks for decoded-frame motion-source contracts, not render tests."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


class DecodedFrameSourceTests(unittest.TestCase):
    def test_source_template_starts_unapproved_and_records_provenance(self) -> None:
        path = ROOT / "_templates/motion-source.md"
        self.assertTrue(path.is_file())
        text = path.read_text()
        header = text.split("---", 2)[1]
        self.assertIn("stage: 04_animate", header)
        self.assertIn("kind: decoded-frame-sidecar", header)
        self.assertIn("status: draft", header)
        self.assertRegex(header, r"(?m)^verdict:\s*$")
        self.assertIn("sources:", header)
        for heading in ("Selected frame", "Accepted predecessor and filing evidence",
                        "Derivation evidence", "Source-frame acceptance evidence",
                        "Appearance and review limits", "Publication and execution boundary",
                        "Human check"):
            self.assertIn("## " + heading, text)
        for field in ("SHA-256", "zero-based", "timestamp", "no image-generation receipt"):
            self.assertIn(field, text)

    def test_animation_contract_owns_the_new_source_mode(self) -> None:
        contract = read("04_animate/CONTEXT.md")
        self.assertIn("kind: decoded-frame-sidecar", contract)
        self.assertIn("../_templates/motion-source.md", contract)
        self.assertIn("00-source-N.md", contract)
        self.assertIn("00-source-frame.png", contract)
        self.assertIn("Decoded-frame sources", read("_reference/motion-rules.md"))
        self.assertIn("decoded-frame", read("_templates/motion-brief.md"))

    def test_source_rules_declare_approval_filing_and_hash_checks(self) -> None:
        rules = read("_reference/motion-rules.md")
        self.assertIn("## Decoded-frame sources", rules)
        section = rules.split("## Decoded-frame sources", 1)[1].split("\n## ", 1)[0]
        for requirement in ("status: approved", "verdict: accepted",
                            "predecessor render record", "predecessor manifest",
                            "predecessor video", "frame SHA-256", "zero-based",
                            "decode-only", "after approval metadata",
                            "no image-generation receipt", "source record",
                            "public hosting", "explicit approval"):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, section)

    def test_existing_source_and_render_gates_remain_declared(self) -> None:
        contract = read("04_animate/CONTEXT.md")
        rules = read("_reference/motion-rules.md")
        for marker in ("03-sidecar.md", "01_spec", "source render record",
                       "explicit approval of `01-spec-N.md`", "public HTTPS URL",
                       "publishing a local image requires explicit approval"):
            with self.subTest(marker=marker):
                self.assertIn(marker, contract)
        self.assertIn("Existing-still mode never reopens acceptance", rules)
        self.assertIn("No motion spec/render proceeds without an accepted, approved, filed source", rules)
        self.assertIn("source sidecar or decoded-frame source record", rules)

    def test_new_concrete_source_links_resolve(self) -> None:
        for path in ("04_animate/CONTEXT.md", "_reference/motion-rules.md",
                     "_templates/motion-source.md", "_templates/motion-brief.md"):
            for link in re.findall(r"`([^`\n]+\.md)`", read(path)):
                if "<" in link or "-N.md" in link or "/" not in link:
                    continue
                base = (ROOT / path).parent if link.startswith(".") else ROOT
                target = base / link
                with self.subTest(path=path, link=link):
                    self.assertTrue(target.resolve().is_relative_to(ROOT))
                    self.assertTrue(target.is_file(), str(target))


if __name__ == "__main__":
    unittest.main()

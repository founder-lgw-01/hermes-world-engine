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
            "_templates/shot-brief.md",
        )

        missing = [path for path in required if not (ROOT / path).is_file()]

        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()

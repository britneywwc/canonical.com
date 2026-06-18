import unittest
from pathlib import Path


class TestOpenSourceSecurityTemplate(unittest.TestCase):
    def test_public_cloud_link_copy_matches_bauer_parse(self):
        template = (
            Path(__file__).resolve().parents[1]
            / "templates"
            / "solutions"
            / "open-source-security"
            / "index.html"
        ).read_text()

        self.assertIn(
            "test Learn how Ubuntu works across all clouds&nbsp;&rsaquo;",
            template,
        )

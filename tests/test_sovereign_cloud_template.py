import unittest
from pathlib import Path


class TestSovereignCloudTemplate(unittest.TestCase):
    def setUp(self):
        self.template = Path(
            "/home/runner/work/canonical.com/canonical.com/"
            "britneywwc/canonical.com/templates/solutions/"
            "infrastructure/sovereign-cloud.html"
        ).read_text()

    def test_updates_hero_copy_and_cta(self):
        self.assertIn(
            "Your cloud. Your data. Your turf.",
            self.template,
        )
        self.assertIn(
            "Get the essential guide to sovereign clouds",
            self.template,
        )
        self.assertNotIn(
            "Learn about sovereign clouds in our free, comprehensive guide.",
            self.template,
        )

    def test_updates_key_sovereignty_copy(self):
        self.assertIn(
            "Sovereign clouds are private clouds that adhere to a comprehensive"
            " set of legal, operational, regulatory, and technical"
            " requirements.",
            self.template,
        )
        self.assertIn(
            "Levels of digital sovereignty in the cloud",
            self.template,
        )
        self.assertIn(
            "Technology sovereignty is the highest level of control you can"
            " have over your cloud",
            self.template,
        )

    def test_updates_why_build_copy(self):
        self.assertIn(
            "Many countries and entities have adopted data localization"
            " mandates",
            self.template,
        )
        self.assertIn(
            "Gain control over cloud operations",
            self.template,
        )
        self.assertIn(
            "Standard public clouds often mitigate disasters",
            self.template,
        )

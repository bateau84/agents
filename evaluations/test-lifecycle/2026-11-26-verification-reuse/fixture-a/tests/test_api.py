import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class APIContractTests(unittest.TestCase):
    def test_cli_serializes_the_domain_result(self):
        for amount, expected in [(9, False), (10, True), (11, True)]:
            with self.subTest(amount=amount):
                completed = subprocess.run(
                    [sys.executable, "-B", str(ROOT / "api.py")],
                    input=json.dumps({"amount": amount, "minimum": 10}),
                    text=True, capture_output=True, check=True, timeout=10,
                )
                self.assertTrue(completed.stdout.endswith("\n"))
                payload = json.loads(completed.stdout)
                self.assertEqual(set(payload), {"eligible", "minimum"})
                self.assertIs(payload["eligible"], expected)
                self.assertEqual(payload["minimum"], 10)

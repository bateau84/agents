import unittest
from domain import qualifies

class DomainTests(unittest.TestCase):
    def test_minimum_boundary(self):
        for amount, expected in [(9, False), (10, True), (11, True)]:
            with self.subTest(amount=amount):
                self.assertIs(qualifies(amount, 10), expected)

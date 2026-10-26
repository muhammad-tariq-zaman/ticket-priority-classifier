import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestClassifier(unittest.TestCase):
    def test_p1_outage(self):
        r = main.classify("The whole office network is down, total outage")
        self.assertEqual(r["priority"], "P1")
        self.assertIn("outage", r["matched"])

    def test_p2_blocked(self):
        self.assertEqual(main.classify("I am blocked, cannot work at all")["priority"], "P2")

    def test_default_p4(self):
        r = main.classify("Just a general question about the VPN")
        self.assertEqual(r["priority"], "P4")


if __name__ == "__main__":
    unittest.main()

import unittest
from label import display_name

class LabelTests(unittest.TestCase):
    def test_none(self):
        self.assertEqual(display_name(None), "")
    def test_blank(self):
        self.assertEqual(display_name("   "), "")
    def test_text(self):
        self.assertEqual(display_name(" Ada "), "Ada")
    def test_zero(self):
        self.assertEqual(display_name(0), "0")

if __name__ == "__main__":
    unittest.main()

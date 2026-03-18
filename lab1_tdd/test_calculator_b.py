import unittest
from calculator_a import Add

class TestCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_one_number(self):
        self.assertEqual(Add("9"), 9)

    def test_two_number(self):
        self.assertEqual(Add("5,7", 12))

if __name__ == "__main__":
    unittest.main()
import unittest

from calculator_a import Add


class TestCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_one_number(self):
        self.assertEqual(Add("9"), 9)

    def test_two_number(self):
        self.assertEqual(Add("5,7"), 12)

    def test_many_numbers(self):
        self.assertEqual(Add("1,2,3,4,6"), 16)

    def test_invalid_raises_error(self):
        with self.assertRaises(ValueError):
            Add("1,,6")


if __name__ == "__main__":
    unittest.main()

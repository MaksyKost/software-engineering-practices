import unittest

from calculator_b import Add


class TestAdd(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_singl_number(self):
        self.assertEqual(Add("5"), 5)

    def test_dual_number(self):
        self.assertEqual(Add("5,3"), 8)
    
    def test_multi_number(self):
        self.assertEqual(Add("1,2,3,4,5,6"), 21)
    
    def test_value(self):
        with self.assertRaises(ValueError):
            Add("I use Arch btw!")

    def test_invalid_newline(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

    def test_valid_newline(self):
        self.assertEqual(Add("1\n2,3"), 6)

if __name__ == "__main__":
    unittest.main()

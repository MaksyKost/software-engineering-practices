import unittest

from calculator import Add

class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)
        
    def test_single(self):
        self.assertEqual(Add("4"), 4)
        
    def test_dual(self):
        self.assertEqual(Add("4,8"), 12)
        
    def test_many(self):
        self.assertEqual(Add("1,3,2,4,6"), 16)
        
    def test_error_value(self):
        with self.assertRaises(ValueError):
            Add("3,,7")
            
    def test_many_n(self):
        self.assertEqual(Add("4,4\n5,2\n8"), 23)
        
    def test_error_bad_n(self):
        with self.assertRaises(ValueError):
            Add("4,\n")
        
        
if __name__ == "__main__":
    unittest.main()

import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

max_min_module = __import__("25_max_min_list")
find_max_min = max_min_module.find_max_min

class TestMaxMinList(unittest.TestCase):
    
    def test_positive_and_negative(self):
        self.assertEqual(find_max_min([3, 1, 9, -2, 5]), (9, -2))
        
    def test_all_negative(self):
        self.assertEqual(find_max_min([-5, -1, -10, -2]), (-1, -10))
        
    def test_single_element(self):
        self.assertEqual(find_max_min([42]), (42, 42))
        
    def test_empty_list(self):
        self.assertEqual(find_max_min([]), (None, None))
        
    def test_duplicate_values(self):
        self.assertEqual(find_max_min([5, 5, 5, 5]), (5, 5))

if __name__ == "__main__":
    unittest.main()
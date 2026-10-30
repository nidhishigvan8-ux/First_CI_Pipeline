import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

intersection_module = __import__("28_set_intersection")
find_intersection = intersection_module.find_intersection

class TestSetIntersection(unittest.TestCase):
    
    def test_normal_intersection(self):
        self.assertEqual(find_intersection([1, 2, 3, 4], [2, 4, 6]), [2, 4])
        
    def test_with_duplicates(self):
        self.assertEqual(find_intersection([1, 2, 2, 3], [2, 2, 4]), [2])
        
    def test_no_intersection(self):
        self.assertEqual(find_intersection([1, 2, 3], [4, 5, 6]), [])
        
    def test_empty_lists(self):
        self.assertEqual(find_intersection([], [1, 2]), [])
        self.assertEqual(find_intersection([1, 2], []), [])
        self.assertEqual(find_intersection([], []), [])

if __name__ == "__main__":
    unittest.main()
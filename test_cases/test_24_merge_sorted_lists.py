import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

merge_module = __import__("24_merge_sorted_lists")
merge_sorted_lists = merge_module.merge_sorted_lists

class TestMergeSortedLists(unittest.TestCase):
    
    def test_normal_merge(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        
    def test_different_lengths(self):
        self.assertEqual(merge_sorted_lists([1, 5, 9], [2, 3]), [1, 2, 3, 5, 9])
        
    def test_empty_lists(self):
        self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([4, 5], []), [4, 5])
        self.assertEqual(merge_sorted_lists([], []), [])
        
    def test_with_duplicates(self):
        self.assertEqual(merge_sorted_lists([1, 2, 2], [2, 3, 4]), [1, 2, 2, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
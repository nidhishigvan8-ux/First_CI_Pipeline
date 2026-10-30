import sys
import os
import unittest

# Automatically find the parent folder and append the 'codes' directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

# Import using __import__ because file name starts with numbers
sort_module = __import__("23_sort_without_sort")
sort_list = sort_module.sort_list

class TestSortWithoutSort(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(sort_list([5, 3, 8, 1, 2]), [1, 2, 3, 5, 8])
        
    def test_already_sorted(self):
        self.assertEqual(sort_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
    def test_reverse_sorted(self):
        self.assertEqual(sort_list([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_with_duplicates(self):
        self.assertEqual(sort_list([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])
        
    def test_empty_and_single_element(self):
        self.assertEqual(sort_list([]), [])
        self.assertEqual(sort_list([42]), [42])

if __name__ == "__main__":
    unittest.main()
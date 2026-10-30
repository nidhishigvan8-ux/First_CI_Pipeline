import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

rotate_module = __import__("27_rotate_list")
rotate_list = rotate_module.rotate_list

class TestRotateList(unittest.TestCase):
    
    def test_normal_rotation(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        
    def test_rotation_larger_than_length(self):
        self.assertEqual(rotate_list([1, 2, 3], 7), [3, 1, 2]) # 7 % 3 = 1 step rotation
        
    def test_zero_rotation(self):
        self.assertEqual(rotate_list([1, 2, 3], 0), [1, 2, 3])
        
    def test_empty_list(self):
        self.assertEqual(rotate_list([], 3), [])
        
    def test_single_element(self):
        self.assertEqual(rotate_list([10], 5), [10])

if __name__ == "__main__":
    unittest.main()
import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))
sum_module = __import__("26_sum_of_list")
calculate_sum = sum_module.calculate_sum

class TestSumOfList(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(calculate_sum([1, 2, 3, 4, 5]), 15)
        
    def test_negative_numbers(self):
        self.assertEqual(calculate_sum([-1, -2, -3]), -6)
        
    def test_mixed_numbers(self):
        self.assertEqual(calculate_sum([-1, 5, -2, 3]), 5)
        
    def test_empty_list(self):
        self.assertEqual(calculate_sum([]), 0)
        
    def test_single_element(self):
        self.assertEqual(calculate_sum([10]), 10)

if __name__ == "__main__":
    unittest.main()
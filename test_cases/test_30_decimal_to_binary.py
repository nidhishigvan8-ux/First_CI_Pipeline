import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

binary_module = __import__("30_decimal_to_binary")
decimal_to_binary = binary_module.decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    
    def test_standard_conversions(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(15), "1111")
        self.assertEqual(decimal_to_binary(6), "110")
        
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")
        
    def test_single_digit(self):
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        
    def test_large_number(self):
        self.assertEqual(decimal_to_binary(255), "11111111")

if __name__ == "__main__":
    unittest.main()
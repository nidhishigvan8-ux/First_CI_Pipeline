import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir, "codes"))

armstrong_module = __import__("29_armstrong_number")
is_armstrong = armstrong_module.is_armstrong

class TestArmstrongNumber(unittest.TestCase):
    
    def test_valid_armstrong_numbers(self):
        self.assertTrue(is_armstrong(153))  
        self.assertTrue(is_armstrong(370))  
        self.assertTrue(is_armstrong(9474)) 
        self.assertTrue(is_armstrong(0))    
        self.assertTrue(is_armstrong(9))    
        
    def test_invalid_armstrong_numbers(self):
        self.assertFalse(is_armstrong(123))
        self.assertFalse(is_armstrong(154))
        self.assertFalse(is_armstrong(100))
        
    def test_negative_numbers(self):
        self.assertFalse(is_armstrong(-153))

if __name__ == "__main__":
    unittest.main()

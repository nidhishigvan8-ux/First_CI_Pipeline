import sys
import os
import unittest
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

anagram_module = __import__("22_anagram_strings")
is_anagram = anagram_module.is_anagram

class TestAnagramStrings(unittest.TestCase):
    
    def test_valid_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        
    def test_anagrams_with_spaces_and_case(self):
        self.assertTrue(is_anagram("Anagram", "Nag a ram"))
        self.assertTrue(is_anagram("School master", "The classroom"))

    def test_invalid_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("apple", "pale"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("abc", "abcd"))

if __name__ == "__main__":
    unittest.main()
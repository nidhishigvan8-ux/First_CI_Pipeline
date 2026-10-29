import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    largest_word_module = importlib.import_module("21_largest_word")
except ModuleNotFoundError:
    try:
        largest_word_module = importlib.import_module("test_cases.21_largest_word")
    except ModuleNotFoundError:
        largest_word_module = importlib.import_module("codes.21_largest_word")

find_largest_word = largest_word_module.find_largest_word

def test_standard_sentence():
    assert find_largest_word("Welcome to the beautiful world of programming") == "programming"

def test_with_punctuation():
    assert find_largest_word("Hello, world! Data-science is awesome...") == "Datascience"

def test_empty_string():
    assert find_largest_word("") == ""

def test_whitespace_only():
    assert find_largest_word("     ") == ""

def test_single_word():
    assert find_largest_word("Python") == "Python"

def test_multiple_same_length():
    assert find_largest_word("cats and dogs") == "cats"
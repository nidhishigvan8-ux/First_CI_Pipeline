import importlib

module = importlib.import_module("21_largest_word")
largest_word = module.largest_word


def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


def test_punctuation():
    assert largest_word("Hello, world!") == "Hello"


def test_tie():
    assert largest_word("cat dog bat") == "cat"


def test_single_word():
    assert largest_word("Python") == "Python"


def test_empty_sentence():
    assert largest_word("") == ""
import string

def find_largest_word(sentence: str) -> str:
    """
    Takes a string and returns the largest word found in it.
    If the string is empty or contains no words, returns an empty string.
    """
    if not sentence or not isinstance(sentence, str):
        return ""
    
    # Remove punctuation marks to ensure accurate word length comparison
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split the sentence by whitespace into a list of words
    words = cleaned_sentence.split()
    
    if not words:
        return ""
    
    # Return the largest word based on length
    return max(words, key=len)

if __name__ == "__main__":
    # Example usage:
    sample_text = "Python is a magnificent and powerful programming language."
    result = find_largest_word(sample_text)
    print(f"The largest word is: '{result}'")
def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    Ignores spaces and case sensitivity.
    """
    # Remove spaces and convert to lowercase
    clean_str1 = "".join(str1.split()).lower()
    clean_str2 = "".join(str2.split()).lower()
    
    # If lengths are not equal, they cannot be anagrams
    if len(clean_str1) != len(clean_str2):
        return False
        
    # Sort and compare the characters
    return sorted(clean_str1) == sorted(clean_str2)

if __name__ == "__main__":
    # Example usage
    s1 = "Listen"
    s2 = "Silent"
    print(f"Are '{s1}' and '{s2}' anagrams? {is_anagram(s1, s2)}")
def find_max_min(arr: list) -> tuple:
    """
    Finds the maximum and minimum numbers in a list 
    without using built-in max() and min() functions.
    Returns a tuple: (max_value, min_value)
    """
    if not arr:
        return None, None
        
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    return max_val, min_val

if __name__ == "__main__":
    # Example usage
    numbers = [3, 1, 9, -2, 5, 8]
    maximum, minimum = find_max_min(numbers)
    print(f"List: {numbers}")
    print(f"Maximum: {maximum}, Minimum: {minimum}")
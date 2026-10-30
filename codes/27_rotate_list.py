def rotate_list(arr: list, k: int) -> list:
    """
    Rotates a list to the right by k steps.
    Handles empty lists and values of k larger than the list length.
    """
    if not arr:
        return arr
        
    n = len(arr)
    # Handle cases where k is greater than the length of the list
    k = k % n
    
    # Slice the list and combine to get the rotated list
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    steps = 2
    print(f"Original list: {numbers}")
    print(f"Rotated by {steps} steps: {rotate_list(numbers, steps)}")
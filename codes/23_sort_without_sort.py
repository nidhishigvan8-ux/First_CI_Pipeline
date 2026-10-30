def sort_list(arr: list) -> list:
    """
    Sorts a list of numbers in ascending order without using built-in sort functions.
    Uses the Bubble Sort algorithm.
    """
    # Create a copy of the list to avoid modifying the original list
    sorted_arr = list(arr)
    n = len(sorted_arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                
    return sorted_arr

if __name__ == "__main__":
    # Example usage
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {numbers}")
    print(f"Sorted list: {sort_list(numbers)}")
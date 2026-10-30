def calculate_sum(arr: list) -> int:
    """
    Calculates the sum of all elements in a list 
    without using the built-in sum() function.
    """
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"Sum: {calculate_sum(numbers)}")
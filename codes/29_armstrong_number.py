def is_armstrong(num: int) -> bool:
    """
    Checks if a given integer is an Armstrong number.
    Works for both 3-digit numbers and other lengths.
    """
    # Negative numbers are not Armstrong numbers
    if num < 0:
        return False
        
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of total digits
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return total_sum == num

if __name__ == "__main__":
    # Example usage
    test_num = 153
    print(f"Is {test_num} an Armstrong number? {is_armstrong(test_num)}")
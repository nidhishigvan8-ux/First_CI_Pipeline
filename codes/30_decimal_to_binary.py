def decimal_to_binary(n: int) -> str:
    """
    Converts a positive decimal integer into its binary representation as a string.
    Handles the case for 0 explicitly.
    """
    if n == 0:
        return "0"
        
    binary_str = ""
    # Process the number by repeatedly dividing by 2
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
        
    return binary_str

if __name__ == "__main__":
    # Example usage
    number = 10
    print(f"Decimal: {number} -> Binary: {decimal_to_binary(number)}")
"""
Sum of Digits using Recursion in Python
Time Complexity: O(log n)  # number of digits
Space Complexity: O(log n) # due to recursive call stack
"""

def sum_of_digits(n):
    """
    Returns the sum of digits of a number n using recursion
    """
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# ----------------------------
# Example usage
if __name__ == "__main__":
    num = 12345
    print(f"Sum of digits of {num} is {sum_of_digits(num)}")

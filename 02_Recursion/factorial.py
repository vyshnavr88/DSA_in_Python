"""
Factorial using Recursion in Python
Time Complexity: O(n)
Space Complexity: O(n)  # due to recursive call stack
"""

def factorial(n):
    """
    Returns factorial of n using recursion
    """
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive call

# ----------------------------
# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")

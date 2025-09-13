"""
Reverse a String using Recursion in Python
Time Complexity: O(n)  # length of string
Space Complexity: O(n) # due to recursive call stack
"""

def reverse_string(s):
    """
    Returns the reversed string using recursion
    """
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

# ----------------------------
# Example usage
if __name__ == "__main__":
    s = "Python"
    print(f"Original string: {s}")
    print(f"Reversed string: {reverse_string(s)}")

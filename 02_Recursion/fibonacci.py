"""
Fibonacci Numbers in Python
Includes:
1. Recursive approach
2. Iterative approach

Time & Space Complexity:
- Recursive: O(2^n) time, O(n) space (call stack)
- Iterative: O(n) time, O(1) space
"""

# ----------------------------
# 1️⃣ Recursive Version
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# ----------------------------
# 2️⃣ Iterative Version (Efficient)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# ----------------------------
# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Recursive: Fibonacci({n}) = {fibonacci_recursive(n)}")
    print(f"Iterative: Fibonacci({n}) = {fibonacci_iterative(n)}")

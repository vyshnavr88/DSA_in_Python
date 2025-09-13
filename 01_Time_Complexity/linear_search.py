"""
Linear Search in Python
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Returns the index of target in arr if found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ----------------------------
# Example usage
if __name__ == "__main__":
    arr = [5, 3, 8, 6, 7, 2]
    target = 6

    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")

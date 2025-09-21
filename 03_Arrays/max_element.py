def find_max_manual(arr):
    """Find maximum element manually by iterating."""
    if not arr:  # handle empty array
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def find_max_builtin(arr):
    """Find maximum element using Python's built-in max()."""
    if not arr:
        return None
    return max(arr)


# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 3, 9, 2]

    print("Manual method:", find_max_manual(arr))   # Output: 9
    print("Built-in max():", find_max_builtin(arr)) # Output: 9

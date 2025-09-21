def linear_search_manual(arr, target):
    """Linear search manually using loop."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index
    return -1  # not found


def linear_search_builtin(arr, target):
    """Linear search using Python's built-in index()."""
    try:
        return arr.index(target)
    except ValueError:
        return -1


# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30

    print("Manual method:", linear_search_manual(arr, target))   # Output: 2
    print("Built-in index():", linear_search_builtin(arr, target)) # Output: 2

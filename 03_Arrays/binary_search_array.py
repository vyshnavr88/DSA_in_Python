def binary_search_iterative(arr, target):
    """Binary Search using iterative approach."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, low, high, target):
    """Binary Search using recursion."""
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70]
    target = 40

    print("Iterative method:", binary_search_iterative(arr, target))  # Output: 3
    print("Recursive method:", binary_search_recursive(arr, 0, len(arr) - 1, target))  # Output: 3

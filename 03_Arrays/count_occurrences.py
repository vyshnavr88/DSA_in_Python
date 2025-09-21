def count_occurrences_manual(arr, target):
    """Count occurrences manually using loop."""
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count


def count_occurrences_builtin(arr, target):
    """Count occurrences using Python's built-in count()."""
    return arr.count(target)


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 2, 5]
    target = 2

    print("Manual method:", count_occurrences_manual(arr, target))   # Output: 3
    print("Built-in count():", count_occurrences_builtin(arr, target)) # Output: 3

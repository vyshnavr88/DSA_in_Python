def selection_sort(arr):
    n = len(arr)

    # Loop over each position in the array
    for i in range(n - 1):
        # Assume the minimum element is at index i
        min_index = i

        # Find the index of the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage
arr = [29, 10, 14, 37, 13]
print("Unsorted:", arr)
print("Sorted:", selection_sort(arr))

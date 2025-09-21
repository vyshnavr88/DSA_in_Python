def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize if no swaps occur
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", bubble_sort(arr))

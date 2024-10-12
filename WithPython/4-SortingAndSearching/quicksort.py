def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        # the pivot element is now in the correct position
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # use the last element as pivot
    pivot = arr[high]

    # keeps track of the last position where value <= pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            # arr[j] should be placed in the left partition
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    pivot_index = i + 1
    # place the pivot at the correct position
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    return pivot_index

# Usage
def main():
    arr = [11, 8, 9, 8, 12, 5, 3]
    print(f"Original array: {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {arr}")


if __name__ == '__main__':
    main()
def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

def merge(arr, left, middle, right):
    left_arr = arr[left:(middle + 1)]
    right_arr = arr[(middle + 1):(right+1)]

    i = 0
    j = 0
    k = left

    # Merge 2 temp arrays back into array
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy remaining items from left or right array
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Usage
def main():
    arr = [11, 8, 9, 8, 12, 5, 3]
    print(f"Original array: {arr}")
    merge_sort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {arr}")


if __name__ == '__main__':
    main()

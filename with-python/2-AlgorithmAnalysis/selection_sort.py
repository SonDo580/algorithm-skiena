def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Usage
def main():
    arr = [64, 25, 12, 22, 25, 11]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()

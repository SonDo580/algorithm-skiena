def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # insert arr[i] into its correct position in the sorted portion
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Usage
def main():
    arr = [64, 25, 12, 22, 25, 11]
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()

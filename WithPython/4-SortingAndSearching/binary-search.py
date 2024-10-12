def binary_search(sorted_arr, key):
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == key:
            return mid
        elif sorted_arr[mid] > key:
            high = mid - 1 # search the left half
        else:
            low = mid + 1 # search the right half
    
    return -1

# Usage
def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    for key in [0, 7]:
        index = binary_search(arr, key)
        if index != -1:
            print(f"{key} found at index: {index}")
        else:
            print(f"{key} not found in the array.")
    
if __name__ == '__main__':
    main()
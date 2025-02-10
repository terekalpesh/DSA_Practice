# Implement binary search on sorted array

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (high + low) // 2     # Find middle index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(arr, 7)

if result != 0:
    print(f'Element is present at index {result}')
else:
    print('Element is not present in array.')
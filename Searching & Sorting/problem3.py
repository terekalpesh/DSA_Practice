# Search for an element in a rotated sorted array.

def search(arr, target): # num is array
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        
        # Determine the sorted half of the array
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1   # Search in the right half
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
    
    # If the element is not found
    return -1


arr = [4, 5, 6, 7, 0, 1, 2, 3]
print(search(arr, 2))
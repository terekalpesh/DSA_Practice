# Find the kth smallest element in an unsorted array.

def kth_smallest_element(arr, k):
    arr.sort()
    return arr[k-1]

arr = [10, 4, 5, 6, 8, 2, 9]
print(kth_smallest_element(arr, 3))
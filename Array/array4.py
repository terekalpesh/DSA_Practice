# Implement a function to merge two sorted arrays into a single sorted array.

def merge_sorted_array(arr1, arr2):
    arr1.sort()
    arr2.sort()
    arr1 += arr2
    arr1.sort()
    return arr1

l1 = [1, 6, 5, 8, 2, 8]
l2 = [5, 6, 3, 7, 2]
print(merge_sorted_array(l1, l2))
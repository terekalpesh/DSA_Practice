# Given an array, rotate it by K positions to the right.

def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:]+arr[:-k]

print(rotate_right([1,2,3,4,5],2))

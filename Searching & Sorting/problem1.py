# Implement quicksort and mergesort.

# Quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []   # Contain smaller elements than pivot
    right = []  # Contain larger elements than pivot

    for element in arr[:-1]:    # Pivote excluded array
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    return quicksort(left) + [pivot] + quicksort(right)

arr = [1, 4, 5, 8, 3, 9, 2]
print(quicksort(arr))


# Mergesort

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid =  len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if  left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [7, 4, 8, 2 ,5, 9, 1]
print(mergesort(arr))
# Find the duplicate number in an array where each number appears twice except one.

arr = [1, 2, 3, 2, 4]

def dup_num(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            break
    return arr[i]

print(dup_num(arr))
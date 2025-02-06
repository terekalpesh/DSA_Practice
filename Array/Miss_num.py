# Write a program to find the missing number in an array of integers from 1 to N.
# arr = [1, 2, 3, 5]
# n = 5
# total_sum = n*(n+1)//2
# print(total_sum)
# arr_sum = sum(arr)
# print(arr_sum)
# missing_num = total_sum - arr_sum
# print(missing_num)


def missing_num(arr_len, arr):
    total_sum = arr_len*(arr_len+1)//2
    arr_sum = sum(arr)
    return total_sum - arr_sum

print(missing_num(5, [1, 2, 3, 5]))
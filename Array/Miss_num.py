# Write a program to find the missing number in an array of integers from 1 to N.
arr = [1, 2, 3, 5]
n = 5
total_sum = n*(n+1)//2
print(total_sum)
arr_sum = sum(arr)
print(arr_sum)
missing_num = total_sum - arr_sum
print(missing_num)


# left, right = 0, n+1
# while left <= right:
#     mid = (left+right)//2
#     print('mid-',mid)
#     # print()
#     if arr[mid] == mid + 1:
#         left = mid + 1
#         print('left-',left)
#         # print()
#     else:
#         right = mid - 1
#         print('right-', right)
#     print()
# print(left+1)
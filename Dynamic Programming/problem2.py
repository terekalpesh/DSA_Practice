# Find the longest increasing subsequence in an array.
# [2, 3, 5, 1, 4, 9] -> [1, 3, 4, 9] 


def lengthOfLIS(arr):
    n = len(arr)

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
result = lengthOfLIS(arr)
print("Length of the Longest Increasing Subsequence:", result)
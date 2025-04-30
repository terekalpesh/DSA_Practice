# Solve the 0/1 knapsack problem.

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)] #* (n + 1)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

weights = [1, 2, 3, 8, 4, 5]
values = [20, 5, 10, 40, 15, 25]
W = 10

max_value = knapsack(weights, values, W)
print(f'Maximum value in the knapsack: {max_value}')

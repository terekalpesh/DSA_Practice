# Find the minimum number of coins required to make a given amount.

def min_coins(coins, amount):
    # Create a table to store the minimum coins for each amount from 0 to 'amount'
    dp = [float('inf')] * (amount + 1)
    print(dp)
    
    # Base case: 0 amount requires 0 coins
    dp[0] = 0
    
    # For each coin, update the table
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, it means the amount cannot be made with the given coins
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 5, 10]  # Coin denominations
amount = 63  # Amount to make
result = min_coins(coins, amount)
print(f"Minimum coins required: {result}")
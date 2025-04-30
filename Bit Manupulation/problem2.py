# Swap two numbers without using a temporary variable.

num1 = 23
num2 = 45

# Method 1
# num1, num2 = num2, num1
# print(num1, num2)

# Method 2
# num1 = num1 + num2  # 'num1' holds sum of the 'num1 and num2'

# num2 = num1 - num2  # 'num2' holds original 'num1' i.e,  'num1 - num2'

# num1 = num1 - num2  # 'num1' holds original 'num2' i.e,  'num1 - num2'

# print(num1, num2)


# Method 3
# XOR - Keeps a "1" only if the numbers are different in that position. If they’re the same (both 0 or both 1), it becomes "0".

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(num1, num2)


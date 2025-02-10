# Solve the Fibonacci sequence using dynamic programming.

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     a, b = 0, 1

#     for i in range(2, n + 1):
#         a, b = b, a+b

#     return b

# print(fibonacci(6))

# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     count = 0
#     while count <= n:
#         print(n1)
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         count += 1

# print(fibonacci(6))

def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fibo_series = [0, 1]

    for i in range(2, n+1):
        fibo_series.append(fibo_series[i-1]+fibo_series[i-2])

    return fibo_series

print(fibonacci(6))
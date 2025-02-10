# Check if a number is a power of two.
# 4 = 2**2, 8 = 2**3

def is_power_of_two(num):
    if num > 0:
        if num & (num-1) == 0:  # 16 & (16 -1) = 10000 & 01111 = 00000
            return True
        else:
            return False
    else:
        return 'Number is less than zero'
    
print(is_power_of_two(4))
print(is_power_of_two(0))
print(is_power_of_two(9))
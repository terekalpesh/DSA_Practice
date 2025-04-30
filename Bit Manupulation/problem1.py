# Count the number of set bits in an integer.

# By using built-in bin()
# def set_bit_count(num):
#     bin_num = bin(num)
#     return bin_num.count('1')

# print(set_bit_count(29))

# Using Brian Kernighan's Algorithm
def set_bit_count(num):
    count = 0
    while num:
        num = num & (num-1)     # Remove rightmost bit # '&' give '1' only if both '1' else '0'
        print(num, '->', bin(num))
        count += 1
    return count

print(set_bit_count(28))
# Find the unique element in an array where every other element appears twice.

def find_unique_element(arr):
    unique_element = 0
    for num in arr:
        print('Prev Unique', unique_element)
        unique_element = unique_element ^ num
        print('Post unique', unique_element)
        print()
    return unique_element

print(find_unique_element([1, 2, 4, 6, 4, 2, 1]))
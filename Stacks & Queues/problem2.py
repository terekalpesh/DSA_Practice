# Reverse a string using a stack.

def reverse_string(s):
    string_stack = []
    str_reverse = ''

    for i in s:
        string_stack.append(i)

    while string_stack:
        str_reverse += string_stack.pop()

    return str_reverse

print(reverse_string('hello'))
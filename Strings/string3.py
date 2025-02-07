# Find the first non-repeating character in a string.

def non_repeat_string(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for char in s:
        if freq[char] == 1:
            return char
        
    return None

print(non_repeat_string('abcdabcef'))
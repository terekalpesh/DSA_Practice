# Check if a string is a palindrome.

s = 'level'
# s = 'mac'

# Method 1
print('Palindrome' if s == s[::-1] else 'Not palindrome')

# Method 2
rev = ''
for i in s:
    rev = i + rev

print('Palindrome' if s == rev else 'Not palindrome')
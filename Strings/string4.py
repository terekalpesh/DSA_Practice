# Implement a function to check if two strings are anagrams.

def isAnagram(s1, s2):
    freq = {}
    for char in s1:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1

    for char in s2:
        if char in freq:
            freq[char] -=1
        else:
            freq[char] = 1

    # print(freq)
    for i in freq:
        if freq[i] != 1:
            break

        return False
    return True

print('Anagram' if isAnagram('hello', 'olleh') else
      'Non anagram')
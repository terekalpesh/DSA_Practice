# Reverse words in a given sentence without using extra space.

sentence = 'hello world from python'
word_list = sentence.split()
word_list = word_list[::-1]
rev = " ".join(word_list)
print(rev)


# word frequency count in a given string
text = "hello world hello everyone"
words = text.split()
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Word frequencies:", word_frequency)

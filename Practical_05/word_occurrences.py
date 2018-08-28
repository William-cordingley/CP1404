single_word = {}
text = input("Text: ")
words = text.split()
for word in words:
    count = single_word.get(word, 0)
    single_word[word] = count + 1
words = list(single_word.keys())
words.sort()
for word in words:
    print("{} : {}".format(word, single_word[word]))

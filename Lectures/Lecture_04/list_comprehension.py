"""
write a lost comprehension (one line) that produces a list of words that have more then 3 characters
"""

text = "This is a sentence"
long_words = [word for word in text.split() if len(word) > 3]
print(long_words)

# this outputs ['This', 'sentence']


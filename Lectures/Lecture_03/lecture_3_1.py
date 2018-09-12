# asking to count the letters in a string
# count alphabetical letters, not characters
    # check if each char is a member of "string.ascii_lowercase"
    # Need to Import String
    # Use char.lower() to ignore case
import string
def count_letters(text):
    count = 0
    for character in text:
        if character.isalpha():
            count +=1
    return count
print(count_letters(""))
print(count_letters("abc"))
print(count_letters("1ab"))




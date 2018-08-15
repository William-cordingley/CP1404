"""
How many Vowels in a Name or String that has been inputted
"""
name = input("Name:  ")
vowels = "AEIOUaeiou"
count = 0
for i in name:
    if i in vowels:
        count += 1
print("There is {} vowels in {} ".format(count, name))


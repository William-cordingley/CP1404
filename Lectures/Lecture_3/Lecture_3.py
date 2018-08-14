# Lecture 3
# Before Lecture Stuff
# asking for an age then showing if its even or odd

while True:
    try:
        age = float(input("Enter Age: "))
        break
    except ValueError:
        print("Error")
if age < 0:
    print("Invalid")
elif age%2 == 1:
    print("Odd")
else:
    print("Even")


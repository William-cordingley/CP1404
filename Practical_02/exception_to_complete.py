finished = False
result = 0
while not finished:
    try:
        result = input("Enter a Valid Integer: ")
        finished = True
    except :
        print("Please enter a valid integer.")
print("Valid result is:", result)

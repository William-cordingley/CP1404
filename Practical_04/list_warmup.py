number = [3, 1, 4, 1, 5, 9, 2]
print(number[0])
print(number[-1])
print(number[3])
print(number[:-1])
print(number[3:4])
print(5 in number)
print(7 in number)
print("3" in number)
print(number + [6, 5, 3])

number[0] = "ten"
print(number)

number[-1] = 1
print(number)

print(number[2:])

print(9 in number)

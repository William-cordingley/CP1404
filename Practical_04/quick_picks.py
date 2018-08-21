import random
numbers_line = 6
minimum = 1
maximum = 45

number = int(input("How Many quick picks? "))
while number < 0:
    print("invalid")
    number = int(input("How many Quick picks? "))

for i in range(number):
    quick_pick = []
    for j in range(numbers_line):
        numbers = random.randint(minimum, maximum)
        while numbers in quick_pick:
            numbers = random.randint(minimum, maximum)
        quick_pick.append(numbers)
    quick_pick.sort()

    print(" ".join("{:2}".format(number) for number in quick_pick))
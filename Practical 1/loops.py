for i in range(1, 21, 2):
    print(i, end=' ')

print(""
      "")
print('a)')
for i in range(0, 100, 10):
    print(i, end=' ')
print(""
      "")
print('b)')
for i in range(20, 1, -1):

    print(i, end=" ")
print(""
      "")
print("c)")
number = int(input("No. of Stars: "))
for i in range(number):
    print("*", end=' ')
print(""
      "")
print("d)")
rows = int(input("No. of rows: "))
for i in range(rows):
    print("*" * (i+1), end=' ')
    print(" ")
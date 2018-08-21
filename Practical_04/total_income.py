number = int(input("How many Months? "))
total = 0
incomes = [0]

for i in range(number):
    income = float(input("Enter income for month {} : $ ".format(i + 1)))
    incomes.append(income)

for i in range(number):
    income = incomes[i + 1]
    total += income
    print("Month {} - Income: $ {} Total: $ {}".format(i + 1, income, total))

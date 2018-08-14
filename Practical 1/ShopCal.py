total = 0
number = int(input("Number of Items: "))
if number < 0:
    print("invalid Number of Items")
else:
    for i in range(number):
        # input price of items
        product = float(input("Price of Item: "))
        # add price of item and previous total amount
        total += product

    if total >= 100:
        total = total - total*0.1

    print("Total Price for {:.2f}".format(number),"items is ${:.2f}".format(total))
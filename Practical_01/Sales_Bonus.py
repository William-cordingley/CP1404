"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("enter sales: $"))
if sales >= 1000:
    bonus = sales * 0.15
    print("Bonus: ${:.2f}  ".format(bonus))
elif sales < 1000 and sales > 0:
    bonus = sales * 0.1
    print("Bonus: ${:.2f}".format(bonus))
else:
    print("Invalid Option")
print("Thank You")

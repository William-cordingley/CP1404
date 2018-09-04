from Practical_06.guitar import Guitar

CURRENT_YEAR = 2018

def run_test():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 1512.9)
    print(my_guitar.get_age())
    print(another_guitar.get_age())
    print(my_guitar.is_vintage())
    print(another_guitar.is_vintage())

run_test()

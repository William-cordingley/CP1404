from Practical_06.guitar import Guitar

CURRENT_YEAR = 2018


def run_test():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 1512.9)
    print("{} get_age() - expected 96. Got {}".format(my_guitar.name, my_guitar.get_age()))
    print("{} get_age() - expected 6. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - expected True. Got {}".format(my_guitar.name, my_guitar.is_vintage()))
    print("{} is_vintage() - expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


run_test()

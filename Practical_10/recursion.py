"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
"""
1 + do_it(4)
        0 + do_it(3)
                1 + do_it(2)
                        0 + do_it(1)
                                1 + do_it(0)
                                        0 
                                1 + 0
                        0 + 1
                1 + 1
        0 + 2
1 + 2 
do_it(5) = 3     
"""


# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))  # which is correct


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)


def do_something_fix(n):
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4),
"""
do_something(3)
        do_something(3)
                do_something(2)
                        do_something(1)
                                do_something(0)
                                        do_something(-1)
                                        = 1
                                = 1
                        = 1
                = 1
        = 1
= 1
"""


# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)
# do_something_fix(4)


# TODO: 5. fix do_something() so that it works according to the docstring

def way_back_squaring(n):
    if n < 0:
        return
    way_back_squaring(n - 1)
    print(n ** 2)


# way_back_squaring(4)


def pyramid(n):
    if n <= 0:
        return 0
    return n + pyramid(n - 1)


# print(pyramid(6))

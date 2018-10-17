"""
Lecture 12
"""

import doctest
import os


def main():
    """ Do this Now - Testing to find out the longest name in the all of the filenames in a specific folder"""
    filename_length = []
    os.chdir('Lyrics/Old')
    for filename in os.listdir('.'):
        filename_length.append(len(filename))
    filename_length.sort()
    # print(filename_length[-1])


main()

'''using assert to test if the is_odd function is correct
using assert will crash if the test doesnt pass '''


def is_odd(n):
    return (n % 2) == 1


assert is_odd(3)
assert not is_odd(4)


# this test the doc string test
# is shows that the is_adult() should return false when 7 is entered
# is shows that the is_adult() should return True when 40 is entered

def is_adult(age):
    """
    >>> is_adult(7)
    False
    >>> is_adult(40)
    True
    """
    return age >= 18


# doctest.testmod()


def get_middle(values):
    """Get the midle value from an ordered collection of values
    >>> get_middle([1, 2])
    1
    >>> get_middle("abc")
    'b'
    """
    pass


# doctest.testmod()


def print_down(number):
    """ Prints the count down from number to 0 """
    for i in range(number, -1, -1):
        print(i)


# print_down(5)

def factorial(n):
    """factorial function calculator(calculate the factorial of n recursively)"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(4))

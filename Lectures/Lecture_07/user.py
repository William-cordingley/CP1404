from random import randint
from operator import attrgetter

from Lectures.Lecture_07.lecture import User


def main():
    names = "Ben", "Joe", "Jane", "Nuno"
    users = []
    for name in names:
        score = randint(0, 50)
        users.append(User(name, score))
    print(users)
    users.sort(key=attrgetter("score", "name"), reverse=True)
    print(users)


main()

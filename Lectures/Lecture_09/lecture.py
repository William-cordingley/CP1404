class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, salary):
        self.salary = salary


class Musician(Person):
    def __init__(self):
        self.play = 0

    def play_music(self, duration):
        self.play += duration


if __name__ == "__main__":
    person1 = Musician(15)
    print(person1.play)
    person1.play_music(15)
    print(person1.play)
"""
Lecture 7 Week 7
"""


# do this now
class User:
    def __init__(self, name):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)

    def __repr__(self):
        return str(self)  # printing the string of the details, not the file crap

    def give_a_taco(self, other, how_many):
        if self.number_of_tacos >= how_many:
            how_many = self.number_of_tacos
        if how_many < 1:
            return  # return nothing so it does nothing
        self.number_of_tacos -= how_many
        other.score += 2

    def steal_taco(self, other):
        self.score = 0


if __name__ == '__main__':
    user1 = User("Ben")
    user2 = User("Joe")
    user1.give_a_taco(user2, 1)  # giving one taco to user2 from user1
    print(user1)
    print(user2)  # uses __str__ function
    user1.steal_taco(user2)
    assert user1.score == 0  # this causes an error if the user1.score isn't equal to 0... used for testing code
    print(user1)

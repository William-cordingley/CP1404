"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print("My Guitar: {}, first made in {}".format(name, year))
"""

CURRENT_YEAR = 2018


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year
    
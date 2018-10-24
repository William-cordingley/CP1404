"""Do this now"""


def main():
    filename = "switch.txt"
    in_file = open(filename, "r")
    line = in_file.readline()  # not plural due to not reading more than 1 line
    in_file.close()

    out_file = open(filename, "w")
    if 'out' in line:
        print("in", file=out_file)
    else:
        print("out", file=out_file)
    out_file.close()


"""do this now #2"""


class Food:
    def __init__(self, name="", calories=0, gluten=False):
        self.name = name
        self.calories = calories
        self.gluten = gluten

    def __str__(self):
        if self.gluten:
            gluten_string = "is"
        else:
            gluten_string = "isnt"
        return "This {} has {} calories and {} gluten free".format(self.name, self.calories, gluten_string)

    def add(self):
        pass

    def healthy(self):
        if self.calories > 50:
            print("This is not healthy")
        else:
            print("This is healthy")


if __name__ == "__main__":
    sandwich = Food("sandwich", 100, False)
    print(sandwich)
    sandwich.healthy()
    joes_lunch = Food("is a fatty meal for joe", 100, False)
    print(joes_lunch)
    joes_lunch.healthy()
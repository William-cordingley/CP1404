class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year)

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"


if __name__ == "__main__":
    programlanguage1 = ProgrammingLanguage("luke", "Dynamic", True, 1999)
    print(programlanguage1)

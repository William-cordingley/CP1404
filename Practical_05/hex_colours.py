COLOUR_NAMES = {"blue": "#0000ff", "green": "006400", "red": "ff0000", "yellow": "ffc125", "pink": "ff69b4",
                "magenta": "ff00ff", "snow": "fffafa", "white": "ffffff", "black": "141414", "gold": "ffd700"}

colour = input("Enter Colour: ")
colour = colour.lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(" {0:<3} is {1:<20}".format(colour, COLOUR_NAMES[colour]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

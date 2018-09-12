# do this now
THRESHOLD = 30


def main():
    names_to_ages = {"Bill": 21, "Jane": 34, "Sven": 56}
    names = [key for key in names_to_ages.keys() if names_to_ages[key] >= THRESHOLD]
    print(names)


main()

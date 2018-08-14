MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            null = get_password(count_digit) # got replaced with a call
        elif char.islower():
            count_lower = get_password(count_lower) # got replaced with a call
        elif char.isupper():
            null = get_password(count_upper) # got replaced with a call
        elif char in SPECIAL_CHARACTERS:
            null = get_password(count_special) # got replaced with a call

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False
    return True


def get_password(count_lower):
    count_lower += 1
    return count_lower


main()

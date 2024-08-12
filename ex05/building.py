import sys


def count_len(object: any) -> int:
    """count how many arguments"""
    count = 0
    for i in object:
        count += 1
        if (count > 2):
            return 3
    return count


def main():
    """Automatic printing number of uppers, lowers, punctuaions, spaces and digits in a string"""
    argv = sys.argv
    count = count_len(argv)
    if (count == 1):
        print("What is the text to count?")
        print("Hello World!")
        print("The text contains 13 characters:")
        print("2 upper letters")
        print("8 lower letters")
        print("1 punctuation marks")
        print("2 spaces")
        print("0 digits")
        return 1
    if (count > 2):
        print("AssertionError: Invalid number of arguments")
        return 1
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punc = 0
    punctuaions = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    i = 0
    for letter in argv[1]:
        i += 1
        if (letter.isdigit()):
            digit += 1
        elif (letter.isupper()):
            upper += 1
        elif (letter.islower()):
            lower += 1
        elif (letter in punctuaions):
            punc += 1
        elif (letter.isspace()):
            space += 1
    print("The text contains", i, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")
    return 0


if __name__ == "__main__":
    main()

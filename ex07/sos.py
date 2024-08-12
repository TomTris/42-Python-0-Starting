import sys


def count_len(object: any) -> int:
    """count how many arguments"""
    count = 0
    for i in object:
        count += 1
        if (count > 3):
            return 4
    return count


def isValidString(string: str) -> bool:
    """check if string is valid"""
    for letter in string:
        if not letter.isalnum() and not letter.isspace():
            return False
    return True


def morseInit() -> dict:
    """Init Morse code"""
    ret = {" ": "/",
           "A": ".-",
           "B": "-...",
           "C": "-.-.",
           "D": "-..",
           "E": ".",
           "F": "..-.",
           "G": "--.",
           "H": "....",
           "I": "..",
           "J": ".---",
           "K": "-.-",
           "L": ".-..",
           "M": "--",
           "N": "-.",
           "O": "---",
           "p": ".--.",
           "Q": "--.-",
           "R": ".-.",
           "S": "...",
           "T": "-",
           "U": "..-",
           "V": "...-",
           "W": ".--",
           "X": "-..-",
           "Y": "-.--",
           "Z": "--..",
           "1": ".----",
           "2": "..---",
           "3": "...--",
           "4": "....-",
           "5": ".....",
           "6": "-....",
           "7": "--...",
           "8": "---..",
           "9": "----.",
           "0": "-----"}
    return ret


def main():
    """String to morse"""
    args = sys.argv
    if count_len(args) != 2 or isValidString(args[1]) is False:
        print("AssertionError: the arguments are bad")
        return 1
    morse = morseInit()
    i = 0
    for letter in args[1]:
        if i == 0:
            print(morse[letter.__str__().capitalize()], end="")
        else:
            print("", morse[letter.__str__().capitalize()], end="")
        if i == 0:
            i = 1
    print("")
    return 1


if __name__ == "__main__":
    # main()
    print(isValidString.__doc__)

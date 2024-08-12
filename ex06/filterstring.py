from ft_filter import ft_filter
import sys


def count_len(object: any) -> int:
    """count how many arguments"""
    count = 0
    for i in object:
        count += 1
        if (count > 3):
            return 4
    return count


def wordsf(argv: str) -> list:
    """Break string to words"""
    ret = []
    string = ""
    for letter in argv:
        if letter.isspace():
            ret.append(string)
            string = ""
        else:
            string += letter
    ret.append(string)
    return ret


def main():
    """String filter"""
    argv = sys.argv
    if (count_len(argv) != 3):
        print("AssertionError: the arguments are bad")
        return 1
    nbr = 0
    try:
        nbr = int(argv[2])
        if nbr <= 0:
            print("AssertionError: the arguments are bad, <= 0")
            return 1
    except Exception:
        print("AssertionError: the arguments are bad, not a valid num")
        return 1
    words = wordsf(argv[1])
    print(words)
    ret = ft_filter(lambda string: string.__len__() >= nbr, words)
    print(ret)


if __name__ == "__main__":
    main()

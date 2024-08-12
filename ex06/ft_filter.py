def isEven(a: int) -> bool:
    """Check if the number is even"""
    if (a % 2 == 0):
        return True
    return False


def ft_filter(function, iterable) -> list:
    """read filter.__doc__"""
    ret = []
    for ite in iterable:
        if function is None:
            if ite:
                ret.append(ite)
        else:
            if function(ite):
                ret.append(ite)
    return ret


def main():
    """Check ft_filter"""
    print(ft_filter(isEven, [2, 4, 6, 1]))
    print(ft_filter(None, [0, 1, '', 'Hello', [], [1]]))


if __name__ == "__main__":
    main()

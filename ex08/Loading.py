def count_len(object: any) -> int:
    """count how long is the range"""
    count = 0
    for i in object:
        count += 1
    return count


def ft_tqdm(lst: range) -> None:
    total = count_len(lst)

    def print_stuff(iteration: int):
        ite_ori = iteration
        whitespace = 200
        iteration = (int)(iteration * whitespace // total)
        form = "\r{:3.0f}".format(iteration * 100 // whitespace) + "%|["
        form += (iteration * "=" + (whitespace - iteration) * " ")
        if (ite_ori != total):
            form += " ]| " + str(ite_ori) + "/" + str(total)
        else:
            form += ">]| " + str(ite_ori) + "/" + str(total)
        print(form, sep="", end="")

    for i, item in enumerate(lst):
        yield item
        print_stuff(i + 1)
    print()


def main():
    return 1


if __name__ == "__main__":
    main()

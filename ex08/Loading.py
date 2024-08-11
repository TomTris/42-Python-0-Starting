from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    def print_stuff(iteration: int):
        iteration = int (iteration * 100 / total)
        form = "\r{:3.0f}".format(iteration) + "%|[" + (iteration * "=" + (100 - iteration) * " ") + "]"
        print(form, sep="", end="")
    
    # while(1):
    for i, item in enumerate(lst):
        yield item * item
        print_stuff(i + 1)
    print("abc")

# def main():
#     return 1


# if __name__ == "__main__":
#     main()

# from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.001)
# a = ft_tqdm(range(333))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print()
for elem in tqdm(range(333)):
    sleep(0.02)
print()

# print(tqdm.__doc__)
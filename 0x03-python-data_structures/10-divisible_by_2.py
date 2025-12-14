#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new = [not bool(i % 2) for i in my_list]
    return new


if __name__ == "__main__":
    test = divisible_by_2([0, 1, 2, 3, 4, 5, 6, 7])
    print(test)

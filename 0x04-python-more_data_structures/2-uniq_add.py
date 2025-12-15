#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum = reduce(lambda x, y: x + y, uniq)
    return sum


if __name__ == "__main__":
    print(uniq_add([1, 2, 2, 2, 3]))

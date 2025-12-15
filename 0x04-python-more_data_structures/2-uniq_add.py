#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum = 0
    for i in uniq:
        sum += i
    return sum


if __name__ == "__main__":
    print(uniq_add([1, 2, 2, 2, 3]))

#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Prints a list of integers

    args:
        my_list: a list of integers

    Return:
        no return value
    """
    for i in my_list:
        print(i)


if __name__ == "__main__":
    print_list_integer([1, 2, 3, 5, 6, 7])

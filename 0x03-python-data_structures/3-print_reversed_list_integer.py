#!/bin/urs/python3


def print_reversed_list_integer(my_list=[]):
    """Print a list in reverse

    Args:
        my_list (list, optional): a list. Defaults to [].

    Return:
        nothing
    """
    my_list.reverse()
    for item in my_list:
        print(item)

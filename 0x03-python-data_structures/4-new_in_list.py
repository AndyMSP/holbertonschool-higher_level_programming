#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """copy list and replace element

    Args:
        my_list (list): list to be copied
        idx (integer): index to modify
        element (n/a): new value at index idx

    Return:
        copied and modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list

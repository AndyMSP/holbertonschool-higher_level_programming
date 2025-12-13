#!/usr/bin/python3


def no_c(my_string):
    """remove c's and C's from string

    Args:
        my_string (string): string to process

    Return:
        new string
    """
    tran = str.maketrans("", "", "Cc")
    new = my_string.translate(tran)

    return new

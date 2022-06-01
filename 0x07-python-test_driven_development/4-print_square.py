#!/usr/bin/python3
"""Module to print a square of hashtags"""


def print_square(size):
    """Function to print a square with hashtags"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)

#!/usr/bin/python3
"""Module to add numbers"""


def add_integer(a, b=98):
    """Addition function

    Adds to numbers
    >>> add_integer(1, 2)
    3

    """
    try:
        problem = 'a'
        if not isinstance(a, (int, float)):
            problem = 'a'
            raise TypeError
        elif not isinstance(b, (int, float)):
            problem = 'b'
            raise TypeError
        a, b = int(a), int(b)
        return a + b
    except Exception:
        raise TypeError(f"{problem} must be an integer")

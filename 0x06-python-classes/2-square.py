#!/usr/bin/python3
"""This module provides a class that defines a square"""


class Square:
    """This class defines a square object"""

    def __init__(self, size=0):
        self.__size = self.set_size(size)

    def set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

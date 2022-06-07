#!/usr/bin/python

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square"""

    def __init__(self, size):
        """method to be called on instantiation"""
        super().__init__(size, size)
        self.__size = size

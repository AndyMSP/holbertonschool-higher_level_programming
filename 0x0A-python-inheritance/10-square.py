#!/usr/bin/python3
"""Module containing the definition for a class of type square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square"""

    def __init__(self, size):
        """method to be called on instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

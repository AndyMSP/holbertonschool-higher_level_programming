#!/usr/bin/python3
"""This module provides a class that defines a square."""


class Square:
    """This class defines a square object."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()

        print(self.position[1] * "\n", end="")
        for i in range(self.size):
            print(self.position[0] * " ", end="")
            print(self.size * "#")

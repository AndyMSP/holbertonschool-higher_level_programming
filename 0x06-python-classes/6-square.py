#!/usr/bin/python3
"""This module defines a class called square"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if all([isinstance(i, int) for i in value]) and len(value) == 2 \
                and value[0] >=0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        except IndexError:
                raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0 and self.__position[1] != 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

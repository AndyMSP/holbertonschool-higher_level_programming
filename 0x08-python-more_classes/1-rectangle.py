#!/usr/bin/python3
"""Module containing the Rectangle class definition"""


class Rectangle:
    """Defines a rectangle object"""

    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h


if __name__ == "__main__":
    r1 = Rectangle(2, 3)
    print(r1.__dict__)

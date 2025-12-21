#!/usr/bin/python3
"""Module containing the Rectangle class definition"""


class Rectangle:
    """Defines a rectangle object"""

    def __init__(self, w=0, h=0):
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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        string = ""
        for i in range(self.height):
            string += self.width * "#"
            if not i == self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    print("--")
    r1 = Rectangle(6, 5)
    print(f"Area: {r1.area()} - Perimeter: {r1.perimeter()}")

    print(str(r1))
    print(repr(r1))

    r2 = eval(repr(r1))
    print(f"Area: {r2.area()} - Perimeter: {r2.perimeter()}")

    print(str(r2))
    print(repr(r2))

    print("--")

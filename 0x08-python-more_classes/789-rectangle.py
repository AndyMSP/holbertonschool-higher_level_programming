#!/usr/bin/python3
"""Module containing the Rectangle class definition"""


class Rectangle:
    """Defines a rectangle object"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size):
        return cls(size, size)

    def __init__(self, w=0, h=0):
        self.width = w
        self.height = h
        Rectangle.number_of_instances += 1

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
        symbol = str(self.print_symbol)
        for i in range(self.height):
            string += self.width * symbol
            if not i == self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


if __name__ == "__main__":
    my_square = Rectangle.square(4)
    print(f"Area: {my_square.area()} - Perimeter: {my_square.perimeter()}")
    print(my_square)

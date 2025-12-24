#!/usr/bin/python3
"""Module containing square class and test script"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size):
        """Function to initialize a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

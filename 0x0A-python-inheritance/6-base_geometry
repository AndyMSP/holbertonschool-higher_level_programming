#!/usr/bin/python3
"""Module contains BaseGeometry class and test script"""


class BaseGeometry:
    """Class representing a base geometry"""

    def area(self):
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

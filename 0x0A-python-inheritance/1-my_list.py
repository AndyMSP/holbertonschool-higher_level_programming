#!/usr/bin/python3
"""A module containing a class derived from list"""


class MyList(list):
    """sub-class of list"""

    def print_sorted(self):
        """prints a list of ints sorted ascending"""
        tmp = self[:]
        tmp.sort()
        print(tmp)


if __name__ == "__main__":
    l1 = MyList([9, 0, 2, 6, 4, 5])
    print(l1)
    l1.print_sorted()
    print(l1)

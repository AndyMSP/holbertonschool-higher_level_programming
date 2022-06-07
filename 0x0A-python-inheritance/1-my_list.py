#!/usr/bin/python3
"""Module contains a class which inherits the list class"""


class MyList(list):
    """Class which inherits list class and adds functionality"""
    def print_sorted(self):
        """function prints a sorted MyList object"""
        tmp = self.copy()
        tmp.sort()
        print(tmp)

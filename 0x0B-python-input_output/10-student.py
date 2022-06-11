#!/usr/bin/python3
"""Module containing class definition for Student"""


class Student:
    """Definition for Student class"""

    def __init__(self, first_name, last_name, age):
        """Method called on instantiation of new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to return dictionary representation of Student"""
        d = self.__dict__
        if attrs is None:
            return d
        else:
            tmp = set(d) & set(attrs)
            new_d = {k:v for (k,v) in d.items() if k in tmp}
            return new_d

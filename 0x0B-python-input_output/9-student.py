#!/usr/bin/python3
"""Module containing class definition for Student"""


class Student:
    """Definition for Student class"""

    def __init__(self, first_name, last_name, age):
        """Method called on instantiation of new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to return dictionary representation of Student"""
        return self.__dict__

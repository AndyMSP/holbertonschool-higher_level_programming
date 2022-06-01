#!/usr/bin/python3
"""Module to say a name"""


def say_my_name(first_name, last_name=""):
    """Function to say a name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        # if last_name != "":
        #   last_name = " " + last_name
        print(f"My name is {first_name} {last_name}")

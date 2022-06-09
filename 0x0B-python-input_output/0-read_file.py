#!/usr/bin/python3
"""Module contains function to open read and close a file"""


def read_file(filename=""):
    """function to open a file, read it, print it and close the file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

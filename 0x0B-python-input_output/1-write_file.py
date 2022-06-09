#!/usr/bin/python3
"""Module contains function that writes text to a file"""


def write_file(filename="", text=""):
    """Function writes <text> to the file <filename>.  If filename
    does not exist, it creates a new file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

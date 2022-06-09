#!/usr/bin/python3
"""Module contains a function that appends text to a file"""


def append_write(filename='', text=''):
    """Function to append text to file <filename>"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

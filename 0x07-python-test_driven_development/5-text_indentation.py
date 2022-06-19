#!/usr/bin/python3
"""Module with function to print string in special format"""


def text_indentation(text):
    """Function to print string in special format.  Two new lines should be
    printed after each '.', ':' and '?'.  White spaces at the beginning and
    end of each new line should be removed"""
    try:
        text = text.replace('.', '.split')
        text = text.replace('?', '?split')
        text = text.replace(':', ':split')
        li = text.rsplit('split')
        li = [i.strip() for i in li]
        [print(i+'\n') for i in li[:-1]]
        print(li[-1], end='')
    except Exception:
        raise TypeError("text must be a string")

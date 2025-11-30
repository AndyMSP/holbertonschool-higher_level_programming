#!/usr/bin/python


def islower(c):
    a, z = ord("a"), ord("z")
    c = ord(c)
    if c > a and c < z:
        return True
    else:
        return False

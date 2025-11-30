#!/usr/bin/python3


def islower(c):
    a, z = ord("a"), ord("z")
    c = ord(c)
    if c > a and c < z:
        return True
    else:
        return False

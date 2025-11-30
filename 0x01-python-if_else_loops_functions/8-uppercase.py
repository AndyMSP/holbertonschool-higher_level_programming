#!/usr/bin/python3


def islower(c):
    a, z = ord("a"), ord("z")
    c = ord(c)
    if c >= a and c <= z:
        return True
    else:
        return False


def uppercase(str):
    diff = ord("A") - ord("a")
    new = ""
    for char in str:
        if islower(char):
            new = new + chr(ord(char) + diff)
        else:
            new = new + char
    print(new)

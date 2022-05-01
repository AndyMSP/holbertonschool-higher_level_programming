#!/usr/bin/python3
def uppercase(str):
    string = ""
    for ch in str:
        if ord(ch) > 96 and ord(ch) < 123:
            string = string + chr(ord(ch) - 32)
        else:
            string = string + ch
    print(string)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    args[0] = 0
    sum = 0
    for arg in args:
        sum += int(arg)
    print(sum)

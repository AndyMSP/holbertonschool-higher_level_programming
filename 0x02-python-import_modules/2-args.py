#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print(f"1 argument:\n1: {args[1]}")
    else:
        print(f"{len(args) - 1} arguments:")
        for i in range(1, len(args)):
            print(f"{i}: {args[i]}")

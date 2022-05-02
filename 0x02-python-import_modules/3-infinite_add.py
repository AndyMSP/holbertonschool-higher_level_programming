#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    numbers = len(sys.argv) - 1
    for i in range(1, numbers + 1):
        sum = sum + int(sys.argv[i])
    print(sum)

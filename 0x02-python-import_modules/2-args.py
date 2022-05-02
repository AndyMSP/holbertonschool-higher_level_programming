#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    print(f"{num} argument{'s.' if num == 0 else(':' if num == 1 else 's:')}")
    for i in range(1, num + 1):
        print(f"{i}: {sys.argv[i]}")

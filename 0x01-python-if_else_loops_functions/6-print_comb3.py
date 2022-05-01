#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if b > a and not (a == 8 and b == 9):
            print(f"{a}{b}, ", end='')
print(f"89")

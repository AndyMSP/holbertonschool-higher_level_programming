#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if num[0] == '-':
    s = '-'
    unsigned = -1 * number
else:
    s = ''
    unsigned = number
last = unsigned % 10
if number < 0:
    print(f"Last digit of {number} is {s}{last} and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")

#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# YOUR CODE HERE
gen = f"Last digit of {number} is "
last = int(abs(number) % 10 * number / abs(number))
if last > 5:
    uniq = f"{last} and is greater than 5"
elif last == 0:
    uniq = "0 and is 0"
else:
    uniq = f"{last} and is less than 6 and not 0"

str = gen + uniq
print(str)

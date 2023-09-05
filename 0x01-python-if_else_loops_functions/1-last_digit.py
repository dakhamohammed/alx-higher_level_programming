#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# this variable just to limit line to 79 character
limit_line = "and is less than 6 and not 0"

if number < 0:
    last_number = number % -10
else:
    last_number = number % 10

if last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
if last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0")
if last_number < 6 and last_number != 0:
    print(f"Last digit of {number} is {last_number} {limit_line}")

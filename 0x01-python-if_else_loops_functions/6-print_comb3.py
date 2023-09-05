#!/usr/bin/python3

for digits in range(0, 10):
    for _digits in range(digits + 1, 10):
        if digits == 8 and _digits == 9:
            print("{}{}".format(digits, _digits))
        else:
            print("{}{}".format(digits, _digits), end=", ")

#!/usr/bin/python3

for numbers in range(0, 100):
    print("{:02}".format(numbers), end=", ")
    if numbers == 99:
        print("{}".format(numbers))

#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = list(a_dictionary.keys())
    number_of_keys = 0
    for i in keys:
        number_of_keys = number_of_keys + 1
    return number_of_keys

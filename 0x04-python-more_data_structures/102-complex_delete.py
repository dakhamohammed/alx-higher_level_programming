#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for key_value in keys:
        if a_dictionary.get(key_value) == value:
            del a_dictionary[key_value]

    return a_dictionary

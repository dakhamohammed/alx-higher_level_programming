#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_multiplied_by_2 = a_dictionary.copy()
    for i in list(dict_multiplied_by_2.keys()):
        dict_multiplied_by_2[i] = dict_multiplied_by_2[i] * 2
    return dict_multiplied_by_2

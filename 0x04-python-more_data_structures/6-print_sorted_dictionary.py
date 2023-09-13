#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_order = list(a_dictionary.keys())
    keys_order.sort()
    for i in keys_order:
        print(f"{i}: {a_dictionary.get(i)}")

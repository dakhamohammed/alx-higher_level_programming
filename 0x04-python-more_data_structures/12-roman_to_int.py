#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    int_value = 0
    prev_int_value = 0

    for char in roman_string:
        value = roman_numeral.get(char, 0)
        if value > prev_int_value:
            int_value = int_value + value - 2 * prev_int_value
        else:
            int_value = int_value + value
        prev_int_value = value

    return int_value

#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Special method: __init__"""
    def __init__(self, size=0):
        """Private instance attribute: self.__size"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

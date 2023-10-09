#!/usr/bin/python3
"""method that returns True if the object is exactly an instance
of the specified class, otherwise False."""


def is_same_class(obj, a_class):
    """check if an object is exactly an instance of a given class.
    """
    if type(obj) == a_class:
        return True
    return False

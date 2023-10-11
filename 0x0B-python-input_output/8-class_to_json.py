#!/usr/bin/python3
"""function that returns the dictionary description with simple data st"""


def class_to_json(obj):
    """return the dictionary represntation of a simple data structure."""
    return obj.__dict__

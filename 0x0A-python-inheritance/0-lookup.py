#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
    - obj: object
        The object for which we want to retrieve the attributes and methods.

    Returns:
    - list:
        A list containing the names of all the attributes and methods of the object.
    """

    atts_mets = dir(obj)

    return atts_mets

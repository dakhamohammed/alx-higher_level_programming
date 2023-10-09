#!/usr/bin/python3
"""function returns the list of available attributes and methods of an obj"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
    - obj: object
        The object for which we want to retrieve the attributes and methods.

    Returns:
    - list:
        containing the names of all the attributes and methods of the obj.
    """

    atts_mets = dir(obj)

    return atts_mets

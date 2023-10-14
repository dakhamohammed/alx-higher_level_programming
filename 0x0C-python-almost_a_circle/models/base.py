#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class (blueprint) for objrcts.
    private class attribute: __nb_objects = 0.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init Base class.

        Args:
            id: to avoid duplicating the same code.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

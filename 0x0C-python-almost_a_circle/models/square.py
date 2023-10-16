#!/usr/bin/python3
"""Square class definition that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class (blueprint) for square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """init square object.

        Args:
            size: size of the new square object.
            x: x coordinate of the new square obj.
            y: y coordinate of the new square obj.
            id: to avoid duplicating the same object.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"
        overriding the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

#!/usr/bin/python3
"""Rectangle base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class (blueprint) for rectangle object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init rectangle object.

        Args:
            width: width of the new Rectangle.
            height: height of the new Rectangle.
            x: x coordinate of the new Rectangle.
            y: y coordinate of the new Rectangle.
            id: to avoid duplicating the same code.
        Raises:
            TypeError: If the input is not an integer
            ValueError: if either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: if either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set the width of the rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set the x coordinate of the rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set the y coordinate of the rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

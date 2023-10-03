#!/usr/bin/python3
"""class Rectangle that defines a rectangle."""


class Rectangle:
    """Rectangle class was not empty.
    Attribute:
        number_of_instances: number of Rectangle instances.
        print_symbol: used as symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init Rectangle object:

        Args:
            width: width of the new rectangle and must be int.
            height: height of the new rectangle and must be int.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get and set the width of the rectangle obj."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get and set the height of the rectangle obj."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returning the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """returning the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the char #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """returning the string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect = rect + ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returning the biggest rectangle based on the area.

        Args:
            rect_1: first rectangle.
            rect_2: second rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle inst.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returning a new Rectangle instance with width == height == size.

        Args:
            size: width and height of the new Rectangle.
        """
        return cls(size, size)

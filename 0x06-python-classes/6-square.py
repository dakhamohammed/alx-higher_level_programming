#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Special method: __init__"""
    def __init__(self, size=0, position=(0, 0)):
        """Public instances attributes: self.size, self.position"""
        self.size = size
        self.position = position

    """size setter propr """
    @property
    def size(self):
        return self.__size

    """position setter propr"""
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        self.__position = value

        try:
            assert type(value) == tuple
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert type(value[0]) == int or type(value[1]) == int
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """public instance method area"""
    def area(self):
        return self.__size ** 2

    """public instance method my_print"""
    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print("\n")
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

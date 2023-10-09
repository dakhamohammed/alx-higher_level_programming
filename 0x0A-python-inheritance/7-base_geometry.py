#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """base geometry."""

    def area(self):
        """area not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a parameter as an integer.

        Args:
            name: the name of the parameter.
            value: the parameter to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

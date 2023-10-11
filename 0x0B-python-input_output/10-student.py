#!/usr/bin/python3
"""class Student."""


class Student:
    """Student class style in python but in JAVA is better."""

    def __init__(self, first_name, last_name, age):
        """init Student object.

        Args:
            first_iname: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__

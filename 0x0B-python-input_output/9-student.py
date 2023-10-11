#!/usr/bin/python3
"""Student class (blueprint as JAVA said."""


class Student:
    """Student blueprint in python style and I hate it."""

    def __init__(self, first_name, last_name, age):
        """init Student object.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of the Student."""
        return self.__dict__

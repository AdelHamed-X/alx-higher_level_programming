#!/usr/bin/python3
"""
Base Geometry class
"""


class BaseGeometry:
    """
    empty class
    """
    def area(self):
        """
        raise an exception
        :return: None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check for an integer
        :param name: a string
        :param value: an int
        :return: an Exception
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

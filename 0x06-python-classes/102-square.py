#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Initiating an instance with
    size attribute"""
    def __init__(self, size=0):
        self.size = size

    """ size(self) - retrieves the priv. attr size (Getter) """
    @property
    def size(self):
        return self.__size

    """ def size(self, value): setter for priv. attr size (Setter) """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Public instance method:
    Area: returns the area of a square"""
    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

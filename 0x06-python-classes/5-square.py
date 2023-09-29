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

    def my_print(self):
        if self.size == 0:
            print()
        i = 0
        while self.size > i:
            j = 0
            while self.size > j:
                print("#", end="")
                j += 1
            print()
            i += 1

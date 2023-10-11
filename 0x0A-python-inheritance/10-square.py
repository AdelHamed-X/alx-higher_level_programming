#!/usr/bin/python3
"""
The square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The square class
    """
    def __init__(self, size):
        """
        instantiates the instance
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculates the area of a square
        :return: area
        """
        return self.__size * self.__size

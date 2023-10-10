#!/usr/bin/python3
"""
This module creates a rectangle class
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width Getter"""
        return self.__width__

    @width.setter
    def width(self, value):
        """width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """height Getter"""
        return self.__height__

    @height.setter
    def height(self, value):
        """height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value

#!/usr/bin/python3
"""
This module creates a rectangle class
"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates instance area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates instance perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """:returns: an informal string representation
        of an instance"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = list(map(lambda x: '#' * self.__width,
                             range(self.__height)))
        string = ""
        for idx in range(len(rectangle)):
            string += rectangle[idx]
            if (idx + 1) == len(rectangle):
                break
            string += '\n'

        return string

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """prints a msg when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base


class Rectangle(Base):
    """Represent a rectangle.

        This class represents a rectangle with a given width,
        height, position (x, y), and an optional identifier.
        It inherits from the Base class.

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the top-left corner of the rectangle.
            y (int): The y coordinate of the top-left corner of the rectangle.
            id (int): The identifier of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
            TypeError: If either x or y is not an integer.
            ValueError: If either x or y is less than 0.
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

            Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
        id (int): The identity of the new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setter/getter of the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter/getter of the width of the Rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setter/getter of the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter/getter of the height of the Rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setter/getter of the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter/getter of the x coordinate of the Rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Setter/getter of the Y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter/getter of the Y coordinate of the Rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #.
        """
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(' ' * self.x, end="")
            rect = ['#' for j in range(self.width)]
            print(''.join(rect))

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
                f" {self.width}/{self.height}")

    def update(self, *args):
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]

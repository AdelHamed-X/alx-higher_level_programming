#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Initiating an instance with
    size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """ position(self) - retrieves the priv. attr position (Getter) """
    @property
    def position(self):
        return self.__position

    """ def position(self, value): setter for priv. attr position (Setter) """
    @position.setter
    def position(self, value):
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            k = 1
            m = 0
            while self.position[0] > k:
                print("_", end="")
                k += 1
            while self.position[1] > m:
                print()
                m += 1
            while self.size > j:
                print("#", end="")
                j += 1
            print()
            i += 1

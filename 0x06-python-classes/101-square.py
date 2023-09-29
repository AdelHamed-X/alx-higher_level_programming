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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if not isinstance(num, int) or num < 0:
                raise TypeError("position must be a tuple of "
                                "2 positive integers")

        self.__position = value

    """Public instance method:
    Area: returns the area of a square"""
    def area(self):
        return self.__size * self.__size

    """Public instance method:
    my_print: prints a pattern according to the size"""
    def my_print(self):
        if self.size == 0:
            print()
        i = 0
        m = 0
        if self.size > 0:
            while self.position[1] > m:
                print()
                m += 1
        while self.size > i:
            j = 0
            k = 0
            while self.position[0] > k:
                print(" ", end="")
                k += 1
            while self.size > j:
                print("#", end="")
                j += 1
            print()
            i += 1

    def __str__(self):
        return str(self.my_print())

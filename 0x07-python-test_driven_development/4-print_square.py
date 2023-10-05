#!/usr/bin/python3
"""
This module has a funtcion that prints a square
of a certain size
"""


def print_square(size):
    """
    prints a square of certain size
    :param size: the size of square
    :return: None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()

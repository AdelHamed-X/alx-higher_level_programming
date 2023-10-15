#!/usr/bin/python3
"""
A module with a function that is able to
append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    :return: the added number of chars
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

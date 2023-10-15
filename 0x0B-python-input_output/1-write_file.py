#!/usr/bin/python3
"""
A module with a function that is able to
write to a file and returns the number of chars written
"""


def write_file(filename="", text=""):
    """
    prints the content of a file to stdout
    :param filename: a text file
    :param text: txt to be written
    :return: None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

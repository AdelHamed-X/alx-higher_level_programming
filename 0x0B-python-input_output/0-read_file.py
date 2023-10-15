#!/usr/bin/python3
"""
A module with a function that is able to
read a file and prints its content to stdout
"""


def read_file(filename=""):
    """
    prints the content of a file to stdout
    :param filename: a text file
    :return: None
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print('\n')

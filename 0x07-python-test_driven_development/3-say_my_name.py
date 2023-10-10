#!/usr/bin/python3
"""
This module has a function that prints any name
"""


def say_my_name(first_name, last_name=""):
    """
    prints any name
    :param first_name: string of first name
    :param last_name: string of last name
    :return: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name + " " + last_name, end="\n")

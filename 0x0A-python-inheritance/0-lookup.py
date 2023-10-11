#!/usr/bin/python3
"""
This module has a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available
    attributes and methods of obj
    :param obj: an object
    """
    return obj.__dir__()

#!/usr/bin/python3
"""
This module contains a function that returns availble attributes
and methods for an object
"""


def lookup(obj):
    """
    looks up for availble attributes and methods of an object
    :param obj: an instance
    :return: list of availble attr. and methods
    """

    return dir(obj)

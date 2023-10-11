#!/usr/bin/python3
"""
A module that has a function returns True
if the object is an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class or not
    :param obj: an object
    :param a_class: a class
    :return: True, False
    """
    if isinstance(obj, a_class):
        return True
    return False

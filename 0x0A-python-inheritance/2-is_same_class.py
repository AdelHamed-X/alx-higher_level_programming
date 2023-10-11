#!/usr/bin/python3
"""
A module that has a function returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class or not
    :param obj: the obj
    :param a_class: the class
    :return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

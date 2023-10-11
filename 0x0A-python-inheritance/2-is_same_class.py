#!/usr/bin/python3
"""
A module that has a function returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False

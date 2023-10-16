#!/usr/bin/python3
"""
This module has a function that returns __dict__
of a class object
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    :param obj: class object
    """
    return obj.__dict__

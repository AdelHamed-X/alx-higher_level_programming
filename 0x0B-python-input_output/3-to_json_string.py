#!/usr/bin/python3
"""
This module has a function that returns a string
representation of anything
"""
import json


def to_json_string(my_obj):
    """
    creates a string representation
    :param my_obj: the obj to be converted
    :return: string
    """
    return json.dumps(my_obj)

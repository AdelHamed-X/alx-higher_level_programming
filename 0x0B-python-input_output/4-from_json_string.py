#!/usr/bin/python3
"""
This module has a function that returns an object
from a JSON string representation
"""
import json


def from_json_string(my_str):
    """
    returns an object
    from a JSON string representation
    :param my_str: the str to be converted
    :return: python object
    """
    return json.loads(my_str)

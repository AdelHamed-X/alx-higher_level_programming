#!/usr/bin/python3
"""
This module has a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    :param my_obj: an object to be saved
    :param filename: the destination file
    :return: None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

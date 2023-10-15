#!/usr/bin/python3
"""
This module has a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    :param filename: the destination file
    :return: None
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

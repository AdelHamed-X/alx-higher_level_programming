#!/usr/bin/python3
"""
Adding an attribute manually
"""


def add_attribute(obj, string1, string2):
    """Add a new attribute to an object if possible.

        Args:
            obj (any): The object to add an attribute to.
            att (str): The name of the attribute to add to obj.
            value (any): The value of att.
        Raises:
            TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__.update({string1: string2})

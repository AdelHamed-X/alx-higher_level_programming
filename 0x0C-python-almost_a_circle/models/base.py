#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instance initialization
        :param id: instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1



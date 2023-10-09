#!/usr/bin/python3

def lookup(obj):
    """
    looks up for availble attributes and methods of an object
    :param obj: an instance
    :return: list of availble attr. and methods
    """

    return dir(obj)

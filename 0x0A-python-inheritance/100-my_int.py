#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts
    == and != signs
    """
    def __eq__(self, other):
        """
        inverts == to !=
        """
        return self != other

    def __ne__(self, other):
        """
        inverts != to ==
        """
        return self == other

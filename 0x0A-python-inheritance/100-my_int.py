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
        return super().__ne__(other)

    def __ne__(self, other):
        """
        inverts != to ==
        """
        return super().__eq__(other)

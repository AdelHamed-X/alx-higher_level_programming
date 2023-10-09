#!/usr/bin/python3
"""
This module creates a subclass with a sorting method
"""


class MyList(list):
    """
    A subclass of 'list' parent class
    """
    def print_sorted(self):
        """
        prints a sorted list
        :return: sort list
        """
        newlist = []
        for element in self:
            newlist.append(element)
        return print(newlist.sort())

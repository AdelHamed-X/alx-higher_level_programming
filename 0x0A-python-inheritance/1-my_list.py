#!/usr/bin/python3
"""
This module creates a subclass with a sorting method
"""


class MyList(list):
    """
    A subclass of 'list' parent class
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        prints a sorted list
        :return: sort list
        """
        return print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
#!/usr/bin/python3
"""
Mylist class
"""


class MyList(list):
    """
    class MyList
    """
    def __int__(self):
        """Instance Constructor"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))

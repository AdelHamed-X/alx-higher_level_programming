#!/usr/bin/python3
""" This module finds a peak in a list """


def find_peak(list_of_integers):
    """ Finds a peak in a list """
    if len(list_of_integers) > 0:
        return max(list_of_integers)
    else:
        return None

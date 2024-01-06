#!/usr/bin/python3
""" This module finds a peak in a list """


def find_peak(list_of_integers):
    """ Finds a peak in a list """
    if list_of_integers:
        arr = sorted(list_of_integers)
        return arr[-1]

    return None

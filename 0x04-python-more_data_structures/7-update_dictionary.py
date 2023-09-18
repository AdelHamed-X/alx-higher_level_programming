#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for elem in list(a_dictionary):
        a_dictionary[key] = value
    return a_dictionary

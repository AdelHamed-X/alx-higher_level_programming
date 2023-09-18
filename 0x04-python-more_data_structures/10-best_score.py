#!/usr/bin/python3
def best_score(a_dictionary):
    check = 0
    max = ""
    for key in list(a_dictionary):
        if a_dictionary[key] > check:
            check = a_dictionary[key]
            max = key
    return max

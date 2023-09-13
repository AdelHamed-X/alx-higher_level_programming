#!/usr/bin/python3
def no_c(my_string):
    for c in len(my_string):
        if my_string[c] in ('c', 'C'):
            continue
        my_string[c] = my_string[c]
    return my_string

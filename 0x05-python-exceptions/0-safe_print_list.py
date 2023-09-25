#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elem_number = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            elem_number += 1
        except IndexError:
            break
    print()
    return elem_number

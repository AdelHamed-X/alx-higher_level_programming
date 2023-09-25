#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elem_number = 0
    try:
        for element in my_list:
            if x == elem_number:
                break
            print("{}".format(element), end="")
            elem_number += 1
        print()
    except NameError as src:
        print("NameError: {}".format(src))
    return elem_number

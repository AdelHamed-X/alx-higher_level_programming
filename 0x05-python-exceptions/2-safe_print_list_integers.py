#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem_numbers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elem_numbers += 1
        except (ValueError, TypeError):
            continue
    print()
    return elem_numbers

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        check = my_list[0]
        for integer in my_list:
            if integer > check:
                check = integer
        return check

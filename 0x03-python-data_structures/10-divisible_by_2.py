#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for ind in range(len(my_list)):
        if my_list[ind] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist

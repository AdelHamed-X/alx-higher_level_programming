#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for ind in my_list:
        if ind % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist

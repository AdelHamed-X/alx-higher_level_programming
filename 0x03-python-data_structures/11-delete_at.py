#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    newlist = []
    for ind in range(len(my_list)):
        if ind != idx:
            newlist.append(my_list[ind])
    return newlist

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for elem in my_list:
        if elem == search:
            newlist.append(replace)
            continue
        newlist.append(elem)
    return newlist

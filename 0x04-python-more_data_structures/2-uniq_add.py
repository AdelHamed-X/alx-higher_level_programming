#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for idx in range(len(my_list)):
        if my_list[idx] in my_list[(idx + 1):]:
            continue
        result += my_list[idx]
    return result

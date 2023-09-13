#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_lis = []
    for ind in my_list:
        if my_list[ind] % 2 == 0:
            bool_lis.append(True)
        else:
            bool_lis.append(False)
    return bool_lis

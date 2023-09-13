#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add1 = tuple_a + (0, 0)
    add2 = tuple_b + (0, 0)
    tuple_result = add1[0] + add2[0], add1[1] + add2[1]
    return tuple_result

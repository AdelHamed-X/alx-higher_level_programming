#!/usr/bin/python3

def remove_char_at(str, n):
    for letter in range(len(str)):
        if letter == n:
            continue
        print("{}".format(str[letter]), end="")
#!/usr/bin/python3

def uppercase(s):
    for ind in range(len(s)):
        letter_ascii = ord(s[ind])
        if letter_ascii in range(97, 123):
            letter_ascii -= 32
        print("{}".format(chr(letter_ascii)), end="")
    print()

#!/usr/bin/python3

for i in reversed(range(97, 123)):
    counter = i
    if counter % 2 != 0:
        counter -= 32
    print("{}".format(chr(counter)), end="")

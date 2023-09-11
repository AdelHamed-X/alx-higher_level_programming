#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size == 0:
        print("0 arguments.")
    elif size == 2:
        print("{} argument:".format(size))
    else:
        print("{} arguments:".format(size - 1))

    for index in range(1, len(argv)):
        print("{}: {}".format(index, argv[index]))


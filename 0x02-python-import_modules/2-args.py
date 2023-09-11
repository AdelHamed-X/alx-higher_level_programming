#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size > 1:
        if size == 2:
            print("1 argument:\n1: {}".format(argv[1]))
        else:
            print("{} arguments:".format(size - 1))
            for index in range(1, len(argv)):
                print("{}: {}".format(index, argv[index]))
    else:
        print("0 arguments.")

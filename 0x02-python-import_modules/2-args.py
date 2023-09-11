#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        for index in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
    else:
        print("0 arguments.")

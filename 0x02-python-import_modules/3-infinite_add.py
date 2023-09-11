#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    result = 0

    for arg in range(1, len(argv)):
        number = int(argv[arg])
        result += number

    print("{}".format(result))

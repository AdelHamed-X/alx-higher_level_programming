#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """

from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(f"{argv[1]}") as resp:
        print(resp.headers["X-Request-Id"])

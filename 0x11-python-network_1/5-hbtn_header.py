#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

import requests
from sys import argv


if __name__ == '__main__':
    resp = requests.get(argv[1])
    print(resp.headers["X-Request-Id"])

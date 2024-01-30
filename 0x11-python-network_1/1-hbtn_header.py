#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response. """

from requests import get
from sys import argv


with get(f"{argv[1]}") as resp:
    print(resp.headers["X-Request-Id"])

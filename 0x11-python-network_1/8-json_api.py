#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
from sys import argv


if __name__ == '__main__':

    if argv[1]:
        q = argv[1]
    else:
        q = ""

    resp = requests.post('http://0.0.0.0:5000/search_user', data=q)
    print(resp.text)

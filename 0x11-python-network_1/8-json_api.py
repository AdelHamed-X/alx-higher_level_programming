#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
from sys import argv


if __name__ == '__main__':

    if len(argv) > 1:
        data = {'q': f"{argv[1]}"}
    else:
        data = {'q': ""}

    resp = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        if resp.json():
            print(f"[{resp.json().get('id')}] {resp.json().get('name')}")
        else:
            print("No result")
    except:
        print("Not a valid JSON")
        
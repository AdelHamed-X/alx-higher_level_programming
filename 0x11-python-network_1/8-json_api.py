#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
from sys import argv


if __name__ == '__main__':

    if argv[1]:
        data = {'q': f"{argv[1]}"}
    else:
        data = {'q': ""}

    resp = requests.post('http://0.0.0.0:5000/search_user', data)

    if type(resp.json()) != dict:
        print("Not a valid JSON")
    elif not resp.json():
        print("No result")
    else:
        print(f"[{resp.json().get('id')}] {resp.json().get('name')}")
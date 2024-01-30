#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8). """

from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    with request.urlopen(f'{argv[1]}') as response:
        try:
            print(response.read())
        except HTTPError as e:
            print(f'Error code: {e.code}')
            
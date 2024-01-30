#!/usr/bin/python3
""" A Python script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response """

from requests import post
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': f'{argv[2]}'})
    data = data.encode('ascii')

    with request.urlopen(f'{argv[1]}', data)as resp:
        print(resp.read().decode('utf-8'))

#!/usr/bin/python3
""" A Python script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response """

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': f'{argv[2]}'})
    data = data.encode('ascii')

    req = request.Request(f'{argv[1]}', data)
    with request.urlopen(req)as resp:
        print(data.read().decode('utf-8'))

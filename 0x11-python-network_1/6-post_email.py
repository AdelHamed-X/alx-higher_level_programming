#!/usr/bin/python3
""" A Python script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response """

from requests import post
from sys import argv


if __name__ == "__main__":
    request = post(argv[1], f'"email": {argv[2]}')
    print(request.content)

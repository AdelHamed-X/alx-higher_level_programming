#!/usr/bin/python3
""" A Python script that takes in a URL and an email, sends a POST request to the passed URL """

from urllib import request, parse
from sys import argv


data = parse.urlencode({'email': f'{argv[2]}'})
data = data.encode('ascii')

with request.urlopen(f'{argv[1]}', data)as resp:
    print(data.read().decode('utf-8'))

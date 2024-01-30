#!/usr/bin/python3
""" A Python script that takes in a URL and an email """

from urllib import request, parse
from sys import argv

data = parse.urlencode({'email': f'{argv[2]}'})
data = data.encode('ascii')

resp = request.urlopen(f'{argv[1]}', data)
print(data.read().decode('utf-8'))

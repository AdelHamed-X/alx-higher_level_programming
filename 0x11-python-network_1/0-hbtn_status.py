#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib import request


with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()
    print("Body response:")
    print(f'    - type: {type(data)}')
    print(f'    - content: {data}')
    print(f'    - utf8 content: {data.decode("utf-8")}')

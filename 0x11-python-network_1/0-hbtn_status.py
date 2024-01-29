#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib import request


with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()
    print("Body response:")
    print(f'\t - {type(data)}')
    print(f'\t - {data}')
    print(f'\t - {data.decode("utf-8")}')

#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

import requests


if __name__ == '__main__':
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print(resp.headers["X-Request-Id"])

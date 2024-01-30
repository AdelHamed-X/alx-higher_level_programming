#!/usr/bin/python3
""" A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

from requests.auth import HTTPBasicAuth
from requests import get
import sys


if __name__ == '__main__':
    credentials = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = get("https://api.github.com/user", auth=credentials)
    print(resp.json().get('id'))

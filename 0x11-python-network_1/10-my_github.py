#!/usr/bin/python3
"""
A python script that takes GitHub credentials
and uses the GitHub API to display GitHub id
- Uses Basic Authentication to access the ID
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

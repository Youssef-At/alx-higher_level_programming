#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode()
    url = sys.argv[1]
    with urllib.request.urlopen(url, data) as response:
        html = response.read().decode("UTF-8")
        print(html)

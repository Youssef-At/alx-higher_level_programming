#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        for header, value in response.__dict__['headers'].items():
            if header == "X-Request-Id":
                print(value)
                break

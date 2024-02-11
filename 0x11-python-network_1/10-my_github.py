#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials."""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    login = requests.get('https://api.github.com/user', auth=(username, token))
    print(login.json().get("id"))

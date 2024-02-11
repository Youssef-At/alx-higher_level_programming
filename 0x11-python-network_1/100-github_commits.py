#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
import requests
from sys import argv

if __name__ == "__main__":
    count = 0
    page = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    req = requests.get(page)
    for commit in req.json():
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
        count += 1
        if count > 9:
            break

#!/usr/bin/python3
""" Displays the value of the X-Request-Id variable in response header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        responses = r.getheaders()
        for response in responses:
            if response[0] == 'X-Request-Id':
                print(response[1])
                break

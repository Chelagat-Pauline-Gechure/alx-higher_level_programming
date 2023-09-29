#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as file:
            response = file.read().decode('utf8')
            print(response)
    except HTTPError as error:
        print('Error code:', error.code)

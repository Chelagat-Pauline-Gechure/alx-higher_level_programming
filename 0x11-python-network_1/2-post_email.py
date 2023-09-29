#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8)"""
from sys import argv
import urllib.request


if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as request:
        print(request.getheader("X-Request-Id"))

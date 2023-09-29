#!/usr/bin/python3
""" Take GitHub credentials & uses GitHub API to display the id"""
from sys import argv
import requests


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))

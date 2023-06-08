#!/usr/bin/python3
from sys import argv
integer, addResult = 1, 0

if __name__ == "__main__":
    while integer < len(argv):
        addResult += int(argv[integer])
        integer += 1
    print(addResult)

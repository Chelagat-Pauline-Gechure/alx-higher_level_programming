#!/usr/bin/python3
from sys import argv
i, addResult = 1, 0

if __name__ == "__main__":
    while i < len(argv):
        addResult += int(argv[i])
        i += 1
    print(addResult)

#!/usr/bin/python3
for integer in range(100):
    if integer == 99:
        print("{:02d}".format(integer))
        break
    print("{:02d}, ".format(integer), end="")

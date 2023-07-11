#!/usr/bin/python3
""" Module with function that appendss to a text file
"""


def append_write(filename="", text=""):
    """ appends string to text file & returns number of characters written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

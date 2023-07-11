#!/usr/bin/python3
"""
Module: 100-append_after
Defines function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, 
    after each line containing a specific string
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        new_word = ""
        for line in f:
            new_word += line
            if search_string in line:
                new_word += new_string
        f.seek(0)
        f.write(new_word)

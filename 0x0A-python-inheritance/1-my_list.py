#!/usr/bin/python3
"""
1-my_list.py defines a class 'MyList'
that inherits from superclass 'list'
"""


class MyList(list):
    """ Implement sorting & printing of built-in list class """

    def print_sorted(self):
        print(sorted(self))

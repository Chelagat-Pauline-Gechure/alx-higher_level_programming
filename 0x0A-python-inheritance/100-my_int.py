#!/usr/bin/python3
""" MyInt class module """


class MyInt(int):
    """ Defining MyInt class"""
    def __eq__(self, integer):
        """ Overide & invert the '==' operator """
        return int(self) != int(integer)

    def __ne__(self, integer):
        """ Overide & invert the '!=' operator """
        return int(self) == int(integer)

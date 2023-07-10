#!/usr/bin/python3
""" Lookup python function """


def lookup(obj):
    """
    Returns a list of all available attributes & methods of a object.
    Args: object to be scanned.
    Returns: list of object attributes & methods.
    """

    return dir(obj)

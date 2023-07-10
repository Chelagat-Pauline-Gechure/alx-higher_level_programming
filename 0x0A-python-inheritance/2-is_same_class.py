#!/usr/bin/python3

""" Module to check for exact class """


def is_same_class(obj, a_class):
    """ Check if the object is an exact instance of a specific class.
    Args:
        obj: object to verify.
        a_class: class to match obj
    Returns:
        True: if object is exact match
        False: otherwise """
    return type(obj) == a_class

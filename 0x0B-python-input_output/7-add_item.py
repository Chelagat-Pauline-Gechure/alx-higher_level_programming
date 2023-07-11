#!/usr/bin/python3
"""
Moduele: 6-load_from_json_file
Adds all arguments to a Python list, and then save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    """ Load the existing list from th file """
    my_list = load_from_json_file(filename)
except:
    my_list = []

""" Add th command line arguments to the list"""
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)

#!/usr/bin/python3
def no_c(my_string):
    chars = [ch for ch in my_string if ch.lower() not in "Cc"]
    return ''.join(chars)

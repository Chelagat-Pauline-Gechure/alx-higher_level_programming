#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0 and n < len(string):
        return string[:n] + string[n+1:]
    else:
        return string

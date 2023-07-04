#!/usr/bin/python3
def magic_string():
    magic_string.reps = getattr(magic_string, 'reps', 0) + 1
    return "BestSchool, " * (magic_string.reps - 1) + "BestSchool"

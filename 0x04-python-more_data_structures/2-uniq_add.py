#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Removing duplicates and remaining with unique elements in the list
    unique_elements = list(set(my_list))
    # Adding the unique elements in the list
    total = sum(unique_elements)
    return total

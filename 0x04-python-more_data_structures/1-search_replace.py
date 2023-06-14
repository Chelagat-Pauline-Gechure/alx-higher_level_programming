#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Looping through each element in the new list
    for item in my_list:
        # Checking if the element matches the search element
        if item == search:
            # If it matches then replace it with the intended element
            new_list.append(replace)
        else:
            # If it doess't match then retain the origina element
            new_list.append(item)
    return new_list

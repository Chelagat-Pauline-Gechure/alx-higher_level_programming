#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    count_value = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count_value += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count_value

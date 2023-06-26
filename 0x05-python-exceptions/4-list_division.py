#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_new_list = []
    for element in range(list_length):
        try:
            division = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            div_new_list.append(division)
    return div_new_list

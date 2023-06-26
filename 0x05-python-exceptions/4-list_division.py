#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_div_list = []
    for element in range(list_length):
        try:
            division_result = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            print("division by 0")
            ivision_result = 0
        except TypeError:
            print("wrong type")
            ivision_result = 0
        except IndexError:
            print("out of range")
            ivision_result = 0
        finally:
            new_div_list.append(ivision_result)
    return new_div_list

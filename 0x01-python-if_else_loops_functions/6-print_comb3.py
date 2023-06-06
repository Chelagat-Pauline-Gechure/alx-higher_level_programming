#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(10):
        if int(first_num) >= int(second_num):
            continue
        elif int(first_num) == 8 and int(second_num) == 9:
            print("{}{}".format(first_num, second_num))
            continue
        print("{}{}, ".format(first_num, second_num), end="")

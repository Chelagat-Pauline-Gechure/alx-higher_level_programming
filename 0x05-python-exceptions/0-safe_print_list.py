def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for e in range(x):
            print(my_list[e], end="")
            count += 1
    except IndexError:
        pass
    print("")
    return count

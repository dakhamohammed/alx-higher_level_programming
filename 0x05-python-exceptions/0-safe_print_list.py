#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x_x = 0

    while x_x < int(x):
        try:
            print(f"{my_list[x_x]}", end="")
            x_x = x_x + 1
        except IndexError:
            break

    print("")
    return x_x


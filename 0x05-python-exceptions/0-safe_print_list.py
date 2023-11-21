#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr_elmt_print = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            nbr_elmt_print += 1
        except IndexError:
            break
    print()
    return nbr_elmt_print

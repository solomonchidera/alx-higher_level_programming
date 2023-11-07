#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if int(idx) < 0 or int(idx) > len(my_list) - 1:
        return my_list
    else:
        del my_list[int(idx)]
        return my_list

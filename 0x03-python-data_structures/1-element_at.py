#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    for i, item in enumerate(my_list):
        if i == idx:
            return item
    return None

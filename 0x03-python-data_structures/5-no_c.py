#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if my_string:
        for i in my_string:
            if ord(i) != ord('c') and ord(i) != ord('C'):
                new_str += str(i)
    return new_str

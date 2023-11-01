#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        last_digit = 0
    else:
        last_digit = int(str(number)[-1])
    print("{:d}".format(last_digit), end="")
    return last_digit

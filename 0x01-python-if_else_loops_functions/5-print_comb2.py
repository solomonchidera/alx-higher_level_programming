#!/usr/bin/python3
for number in range(100):
    if number != 99:
        print("{num:02d}".format(num=number), end=", ")
    else:
        print("{num:02d}".format(num=number), end="\n")

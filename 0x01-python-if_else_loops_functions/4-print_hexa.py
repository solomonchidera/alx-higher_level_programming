#!/usr/bin/python3
for number in range(0, 99):
    print("{number:d} = {hex_num}".format(
        number=int(number), hex_num=hex(number)), end="\n")

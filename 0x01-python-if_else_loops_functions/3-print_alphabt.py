#!/usr/bin/python3
for char_number in range(97, 123):
    if char_number != 101 and char_number != 113:
        print("{character}".format(character=chr(char_number)), end="")

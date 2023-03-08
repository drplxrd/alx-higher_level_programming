#!/usr/bin/python3
def to_upper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(string):
    string_new = ""
    for character in string:
        string_new += "%c" % to_upper(character)
    print("{:s}".format(string_new))

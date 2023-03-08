#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i is not (ord('q')) and i is not (ord('e')):
        print('{}'.format(chr(i)), end='')

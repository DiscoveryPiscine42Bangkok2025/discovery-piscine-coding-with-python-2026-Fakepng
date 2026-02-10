#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count != 1:
    print("none")
else:
    param = sys.argv[1]
    found = False
    for char in param:
        if char == 'z':
            found = True
            print('z', end='')

    if not found:
        print("none")

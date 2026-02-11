#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
    print("none")
    sys.exit()

def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string, end="")
    print("Z" * (8 - len(string)))

for i in range(1, len(sys.argv)):
    if len(sys.argv[i]) > 8:
        shrink(sys.argv[i])
    elif len(sys.argv[i]) < 8:
        enlarge(sys.argv[i])
    else:
        print(sys.argv[i])

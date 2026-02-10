#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count != 1:
    print("none")
else:
    param = sys.argv[1]
    ask = input("What was the parameter? ").strip()
    if param == ask:
        print("Good job!")
    else:
        print("Nope, sorry...")
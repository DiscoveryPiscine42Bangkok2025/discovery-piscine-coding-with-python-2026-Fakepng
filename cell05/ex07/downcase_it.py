#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count == 1:
    print(sys.argv[1].lower())
else:
    print("none")
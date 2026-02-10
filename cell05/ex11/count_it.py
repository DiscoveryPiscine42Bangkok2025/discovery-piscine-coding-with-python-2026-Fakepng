#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count < 1:
    print("none")
else:
    print(f"parameters: {params_count}")
    for i in range(1, params_count + 1):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
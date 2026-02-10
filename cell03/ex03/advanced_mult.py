#!/usr/bin/python

import sys

if len(sys.argv) != 1:
    print("none")
    sys.exit()

row = 0
col = 0

while row <= 10:
    print(f"Table de {row}: ", end="")
    while col <= 10:
        result = row * col
        print(f"{result}", end=" ")
        col += 1

    print()
    col = 0
    row += 1
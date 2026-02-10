#!/usr/bin/python

base = int(input("Enter a number\n"))

for i in range(0, 10):
    result = i * base
    print(f"{i} x {base} = {result}")
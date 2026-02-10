#!/usr/bin/python

count = int(input("Enter a number less than 25\n"))

if count > 25:
    print("Error")
else:
    while count <= 25:
        print(f"Inside the loop, my variable is {count}")
        count += 1
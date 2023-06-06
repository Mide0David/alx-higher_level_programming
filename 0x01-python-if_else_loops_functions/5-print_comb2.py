#!/usr/bin/python3

# loop form 0 to 99
for i in range(0, 100):
    print("{:02d}".format(i), end=", " if i != 99 else "\n")

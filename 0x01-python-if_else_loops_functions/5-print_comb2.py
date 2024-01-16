#!/usr/bin/python3
"""prints numbers from 00 to 99."""

for i in range(99):
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(i + 1))

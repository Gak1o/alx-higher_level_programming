#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if j < 9 or (j == 9 and i < 8):
            print("{:d}{:d},".format(i, j), end="")
        elif j == 9 and i == 8:
            print("{:d}{:d}".format(i, j))
        if j < 9 or (j == 9 and i < 8):
            print(" ", end="")

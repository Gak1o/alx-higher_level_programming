#!/usr/bin/python3
out_string = "{:02d},{:02d}"
for i in range(1, 10):
    for j in range(i+1, 10):
        print(out_string.format(i, j), end=", " if j < 9 else "\n")

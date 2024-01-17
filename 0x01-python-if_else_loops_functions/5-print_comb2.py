#!/usr/bin/python3
out_string = "{:02d}"
for i in range(100):
    print(out_string.format(i), end="," if i < 99 else "\n")

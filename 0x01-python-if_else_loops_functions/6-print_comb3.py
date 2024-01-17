#!/usr/bin/python3
out_string = "{:02d},{:02d}"
for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            if i != j and j != k and i != k:
                print(out_string.format(i, j), end=", " if j < 9 else "\n")

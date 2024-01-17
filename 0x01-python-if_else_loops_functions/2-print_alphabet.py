#!/usr/bin/python3
out_string = "{}"
for i in range(ord('a'), ord('z') + 1):
    print(out_string.format(chr(i)), end='')

#!/usr/bin/python3
out_string = "{}"
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in ['e', 'q']:
        print(out_string.format(chr(i)), end='')

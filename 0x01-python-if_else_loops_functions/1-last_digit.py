#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10
out_string = (f"Last digit of {number} is {l_digit} ")
if l_digit > 5:
    out_string += "and is greater than 5"
    print(out_string)
elif l_digit == 0:
    out_string += "and is 0"
    print(out_string)
else:
    out_string += "and is less than 6 and not 0"
    print(out_string)

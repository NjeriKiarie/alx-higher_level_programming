#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10

if number < 0:
    number = -(number)

if digit < 0:
    number = digit
    digit = -(digit)

if digit > 5:
    string = "and is greater than 5"
elif digit == 0:
    string = "and is 0"
elif digit < 6:
    string = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} and is ".format(number, digit), end="")

#!/usr/bin/python3
"""program that imports functions from the file calculator_1.py,
does some Maths, and prints the result."""

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of variable a and b."""
    from calculator_1 import add, sub, mul, div
    

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

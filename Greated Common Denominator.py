#!/usr/bin/env python3

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's Algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Prompt the user for input
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Calculate and display the GCD
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")


#!/usr/bin/env python3


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns gcd(a, b), u, v such that a*u + b*v = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a, u = 1, v = 0
    gcd, u1, v1 = extended_gcd(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return gcd, u, v

# Inputs
p = 26513
q = 32321

# Perform Extended Euclidean Algorithm
gcd, u, v = extended_gcd(p, q)

# Display results
print(f"gcd({p}, {q}) = {gcd}")
print(f"u = {u}, v = {v}")
print(f"The smaller value (flag) is: {min(u, v)}")

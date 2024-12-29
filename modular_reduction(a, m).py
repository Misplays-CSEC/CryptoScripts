#!/usr/bin/env python3

def modular_reduction(a, m):
    """
    Calculate a mod m using the modulus operator.
    """
    return a % m

# Prompt user for input
print("First modular calculation:")
a1 = int(input("Enter the first number (a1): "))
m1 = int(input("Enter the modulus (m1): "))

print("\nSecond modular calculation:")
a2 = int(input("Enter the second number (a2): "))
m2 = int(input("Enter the modulus (m2): "))

# Calculate x and y
x = modular_reduction(a1, m1)
y = modular_reduction(a2, m2)

# Determine the smaller value
smaller_value = min(x, y)

# Display results
print(f"\n{a1} ≡ {x} (mod {m1})")
print(f"{a2} ≡ {y} (mod {m2})")
print(f"The smaller of the two values is: {smaller_value}")

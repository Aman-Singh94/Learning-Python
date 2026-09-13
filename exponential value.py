import numpy as np

# Example 1: Single value
z = 2

print("Example 1:")
print(np.exp(z))          # e²

# Example 2: Multiple values
z = np.array([1, 2, 3, 4])

print("\nExample 2:")
print(np.exp(z))          # Har value ka e^value

# Example 3: Zero
z = 0

print("\nExample 3:")
print(np.exp(z))          # e⁰ = 1

# Example 4: Negative values
z = np.array([-3, -2, -1])

print("\nExample 4:")
print(np.exp(z))          # Negative values ka exponential

# Example 5: Mixed values
z = np.array([-2, -1, 0, 1, 2])

print("\nExample 5:")
print(np.exp(z))

# Example 6: Decimal values
z = np.array([0.5, 1.5, 2.5])

print("\nExample 6:")
print(np.exp(z))

# Example 7: Matrix
z = np.array([
    [1, 2],
    [3, 4]
])

print("\nExample 7:")
print(np.exp(z))          # Matrix ki har value par e^value

# Example 8: Compare power and exp
z = np.array([1, 2, 3])

print("\nExample 8:")
print("Power:", np.power(z, 2))   # z²
print("Exp:", np.exp(z))          # e^z
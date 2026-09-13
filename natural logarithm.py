import numpy as np

# Example 1: Single value
z = 10

print("Example 1:")
print(np.log(z))          # 10 ka natural log

# Example 2: Multiple values
z = np.array([1, 2, 3, 4, 5])

print("\nExample 2:")
print(np.log(z))          # Har value ka natural log

# Example 3: Powers of e
z = np.array([1, np.e, np.e**2, np.e**3])

print("\nExample 3:")
print(np.log(z))          # e ki powers ka log

# Example 4: Decimal values
z = np.array([0.5, 1.5, 2.5, 3.5])

print("\nExample 4:")
print(np.log(z))          # Decimal values ka log

# Example 5: Large values
z = np.array([10, 100, 1000, 10000])

print("\nExample 5:")
print(np.log(z))          # Large values ka natural log

# Example 6: Matrix
z = np.array([
    [1, 2],
    [3, 4]
])

print("\nExample 6:")
print(np.log(z))          # Matrix ki har value ka log

# Example 7: Negative values
z = np.array([-1, -2, -3])

print("\nExample 7:")
print(np.log(z))          # Negative values ka log defined nahi hota

# Example 8: exp aur log ko saath use karna
z = np.array([1, 2, 3, 4])

print("\nExample 8:")
print(np.exp(z))          # e^z
print(np.log(np.exp(z)))  # exp ke baad log lagaya
import numpy as np

z = np.array([10, 20, 30, 40, 50])

print("Array:")
print(z)

print("\nMedian:")
print(np.median(z))       # Beech ki value nikalta hai

print("\nStandard Deviation:")
print(np.std(z))          # Values kitni spread hain, batata hai

print("\nVariance:")
print(np.var(z))          # Values ka variance nikalta hai

print("\nIndex of Minimum:")
print(np.argmin(z))       # Sabse chhoti value ka index deta hai

print("\nIndex of Maximum:")
print(np.argmax(z))       # Sabse badi value ka index deta hai


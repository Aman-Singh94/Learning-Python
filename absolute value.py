import numpy as np

z = np.array([-10, -20, 30, -40, 50,-34.7])

print(np.abs(z))   # Har value ka absolute value nikalta hai
print(np.absolute(z))  # Ye bhi absolute value nikalta hai
print(np.fabs(z))  # Ye bhi absolute value nikalta hai, lekin ye float values ke liye use hota hai
print(np.sign(z))  # Ye sign function hai, ye batata hai ki value positive hai ya negative


import numpy as np

z = np.array([
    [10, 20, 20],
    [30, 10, 40]
])

print(np.unique(z))


import numpy as np

# 2D Arrays
a = np.array([
    [10, 20],
    [30, 40]
])

b = np.array([
    [50, 60],
    [70, 80]
])

print("Original A:")
print(a)

print("\nOriginal B:")
print(b)


#  Side-by-side join
print("\n--- HSTACK ---")
print(np.concatenate((a, b), axis=1))


#  Neeche-neeche join
print("\n--- VSTACK ---")
print(np.concatenate((a, b), axis=0))


#  vstack()
print("\n--- vstack ---")
print(np.vstack((a, b)))


#  hstack()
print("\n--- hstack ---")
print(np.hstack((a, b)))


#  Transpose
print("\n--- Transpose ---")
print(a.T)


#  Flatten: 2D -> 1D
print("\n--- Flatten ---")
print(a.flatten())


#  Ravel: 2D -> 1D
print("\n--- Ravel ---")
print(a.ravel())


#  Copy
print("\n--- Copy ---")
c = a.copy()
c[0, 0] = 999
print("Original A:")
print(a)
print("Copy C:")
print(c)


#  Where
print("\n--- Where ---")
print(np.where(a > 20))


#  Replace using condition
print("\n--- Replace ---")
print(np.where(a > 20, 100, a))


#  Random 2D array
print("\n--- Random ---")
random_array = np.random.randint(1, 10, (2, 3))
print(random_array)


#  Zeros
print("\n--- Zeros ---")
print(np.zeros((2, 3)))


#  Ones
print("\n--- Ones ---")
print(np.ones((2, 3)))


#  Broadcasting
print("\n--- Broadcasting ---")
print(a + 10)
print(a * 2)
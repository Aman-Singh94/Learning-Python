import numpy as np
# 2D array
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(a)

print(a.ndim)
print(a.shape)
print(a.size)


#2D Indexing
print(a[0, 1])#a[row, column]
print(a[0, 0])
print(a[0, 2])
print(a[1, 0])
print(a[1, 2])


#2D Slicing
print(a[0, :])#first row
print(a[1, :])#second row
print(a[:, 0])#first column


#submatrix
print(a[0:2, 1:3])#a[row_start:row_stop, column_start:column_stop]





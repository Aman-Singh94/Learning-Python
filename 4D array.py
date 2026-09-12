import numpy as np


# ============================================================
# 4D ARRAY
# blocks × layers × rows × columns
# ============================================================


a = np.array([
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ],
    [
        [
            [13, 14, 15],
            [16, 17, 18]
        ],
        [
            [19, 20, 21],
            [22, 23, 24]
        ]
    ]
])


print(a)
print(a.ndim)
print(a.shape)
print(a.size)


# ============================================================
# 4D ARRAY STRUCTURE
# ============================================================

# a[block, layer, row, column]

# Block  → kaunsa block?
# Layer  → block ke andar kaunsi table?
# Row    → table ki kaunsi horizontal line?
# Column → us line mein kaunsa number?


# BLOCK 0
#
#       LAYER 0                 LAYER 1
#
#    ┌─────────────┐        ┌─────────────┐
#    │ 1  2  3     │        │ 7  8  9     │
#    │ 4  5  6     │        │10 11 12     │
#    └─────────────┘        └─────────────┘
#
#
# BLOCK 1
#
#       LAYER 0                 LAYER 1
#
#    ┌─────────────┐        ┌─────────────┐
#    │13 14 15     │        │19 20 21     │
#    │16 17 18     │        │22 23 24     │
#    └─────────────┘        └─────────────┘


# ============================================================
# 4D INDEXING
# ============================================================

print("4D indexing")

print(a[0, 0, 0, 0])
print(a[0, 0, 1, 2])
print(a[0, 1, 0, 1])
print(a[1, 0, 1, 0])
print(a[1, 1, 1, 2])


# ============================================================
# 4D SLICING
# ============================================================

print("4D Slicing")

print(a[0, :, :, :])
print(a[:, 0, :, :])
print(a[:, :, 0, :])
print(a[:, :, :, 0])

print(a[0, 0, :, :])
print(a[1, 1, :, :])

print(a[:, :, :, 1])

print(a[0:2, 0:2, 0:2, 0:2])


# ============================================================
# VALUE CHANGE
# ============================================================

print("Value change")

a[0, 1, 1, 2] = 100

print(a)


# ============================================================
# MULTIPLE VALUES EK SAATH CHANGE
# ============================================================

print("Multiple values change")

a[0, 0, 0, :] = 999

print(a)


# ============================================================
# 4D RESHAPE
# ============================================================

print("4D reshape")

z = np.arange(24)

z = z.reshape(2, 2, 2, 3)

print(z)
print(z.shape)


# ============================================================
# AXIS
# ============================================================

print("4D axis")

print(z.sum(axis=0))    # axis=0 = Blocks ko add karta hai
print(z.sum(axis=1))    # axis=1 = Layers ko add karta hai
print(z.sum(axis=2))    # axis=2 = Rows ko add karta hai
print(z.sum(axis=3))    # axis=3 = Columns ko add karta hai


# ============================================================
# SUM
# ============================================================

print("SUM")

print(z.sum(axis=0))    # Blocks ki values ko add karta hai
print(z.sum(axis=1))    # Layers ki values ko add karta hai
print(z.sum(axis=2))    # Rows ki values ko add karta hai
print(z.sum(axis=3))    # Columns ki values ko add karta hai


# ============================================================
# MEAN
# ============================================================

print("MEAN")

print(z.mean(axis=0))   # Blocks ka average
print(z.mean(axis=1))   # Layers ka average
print(z.mean(axis=2))   # Rows ka average
print(z.mean(axis=3))   # Columns ka average


# ============================================================
# MAX
# ============================================================

print("MAX")

print(z.max(axis=0))    # Blocks mein se badi value
print(z.max(axis=1))    # Layers mein se badi value
print(z.max(axis=2))    # Rows mein se badi value
print(z.max(axis=3))    # Columns mein se badi value


# ============================================================
# MIN
# ============================================================

print("MIN")

print(z.min(axis=0))    # Blocks mein se chhoti value
print(z.min(axis=1))    # Layers mein se chhoti value
print(z.min(axis=2))    # Rows mein se chhoti value
print(z.min(axis=3))    # Columns mein se chhoti value
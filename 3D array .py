#layers × rows × columns
import numpy as np

a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(a)
print(a.ndim)
print(a.shape)
print(a.size)

#a[layer, row, column]

#Layer → kaunsi table?
#Row   → table ki kaunsi horizontal line?
#Column → us line mein kaunsa number?


#        LAYER 0              LAYER 1
#      ┌───────────┐        ┌───────────┐
#      │ 1  2  3   │        │ 7  8  9   │
#      │ 4  5  6   │        │10 11 12   │
 #     └───────────┘        └───────────┘


print("3D indexing")
print(a[0, 1, 2])
print(a[1, 0, 1])
print(a[1, 1, 0])
print(a[0, 0, 1])
print('/n')


print("3D Slicing")
print(a[0, 0, :])
print(a[0, 1, 0:2])
print(a[0, :, 2])
print(a[:, 1, :])
print(a[:, :, 1])
print(a[:, 0, 0:2])
print(a[0:2, 0:2, 0:2])
print('/n')

print("Value change")
a[0, 1, 2] = 100
print(a)
print('/n')

print("Multiple values ek saath change")
a[0, 0, :] = 999
print(a)
print('/n')



print("3D reshape()")
import numpy as np

z = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])
z = z.reshape(2, 2, 3)

print(z)
print(z.shape)
print('/n')


#ye kuch alag tarike se bhi 3D array bana sakte hain
f = np.arange(24)
f = f.reshape(2, 3, 4)
print(f)
print(f.shape)
#
print(f.sum(axis=0)) #axis=0 = sabhi layers ko add karta hai

print("Layer ki values ko add karta hai")
print(f.sum(axis=0))   
print("Layer ki values ka average nikalta hai")
print(f.mean(axis=0))   
print("Layer ki sabse badi value nikalta hai")
print(f.max(axis=0))    
print("Layer ki sabse chhoti value nikalta hai")
print(f.min(axis=0))    









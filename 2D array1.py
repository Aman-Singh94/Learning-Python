#2D array mein value change
import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print(a)
a[0, 1] = 500#a[row, column] = new_value
print(a)

#multiple values change
a[0, :] = 100 #first row ke sabhi elements ko 100 se replace kar diya
print(a)


a[1, 0:2] = 50#second row ke first two elements ko 500 se replace kar diy"""
"""0 se start kar ke 2 tak jao, 2 ko include nahi kiya"""
print(a)


a[1, 1:3] = 999 
"""1 se start kar ke 3 tak jao, 3 ko include nahi kiya"""
print(a)

print(a.sum(axis=0))
print(a.sum(axis=1))


#2D array mein filtering
print(a[a > 200])

#Abhi axis=0 ko bas itna yaad rakho: column direction

z = np.array([
    [30, 10, 20],
    [60, 40, 50]
])
print(np.sort(z))
#har column ko upar se neeche sort karta hai, axis=0 ke liye
#30 < 60 
#10 < 40 
#20 < 50
print(np.sort(z, axis=1))

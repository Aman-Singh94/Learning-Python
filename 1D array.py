import numpy as np
a=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(a))#rows or elements
print(a.ndim)#dimensions
print(a.shape)#shape of array


#Indexing
print(a[0])#first element
print(a[1])#second element

#negative index
print(a[-1])#last element
print(a[-2])#second last element

#Slicing.
print(a[0:3])#first three elements
print(a[1:4])#second to fourth elements
print(a[::2])#every second element
print(a[::-1])#reverse the array
print(a[1:4:2])#start:stop:step
print(a[3:])#from fourth element to end
print(a[:5])#from start to fifth element


#Values change
a[0] = 100#a[index] = new_value
print(a)


#basic calculations
print(a.sum())# total sum of all elements
print(a.min())# minimum value
print(a.max())# maximum value
print(a.mean())# average
print(a.prod())# sabko multiply


print(a[0:5].sum())#sum of first five elements


#har element par calculation
print(a + 10)
print(a * 2)
print(a - 5)
print(a / 2)



#Comparison + Boolean Filtering
print(a > 5)  # Boolean array with True/False values
print(a[a > 5])  # Elements greater than 5
#choose according to condition

print(a[a < 6])   # Elements less than 6
print(a[a >= 5])  # Elements greater than or equal to 5
print(a[a <= 6])  # Elements less than or equal to 6
print(a[a == 5])  # Elements equal to 5
print(a[a != 5])  # Elements not equal to 5



#arange
b= np.arange(1, 11)
print(b)

c=np.arange(1,11,2)#start,stop,step
print(c)


#reshape() — 1D → 2D
d=a.reshape(2, 5)  # Reshape to 2 rows and 5 columns
print(d)


#shorting
print(np.sort(a))

#Unique Values
f = np.array([1, 2, 2, 3, 3, 3, 4])
print(np.unique(f))
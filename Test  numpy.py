import numpy as np
print(np.__version__)  # This will print the version of numpy installed


list1 = [1, 2, 3, 4, 5]
# Convert list to numpy array
array1 = np.array(list1)
print("Numpy Array:", array1)

array2=np.array([6, 7, 8, 9, 10])
#numpy array
print("Numpy Array 2:", array2)

print(type(array1))  # This will print the type of array
print(type(array2))  


array3 = np.array([10, 20, 30, 40.5])
print(array3)
print(array3.dtype)#Homogeneous = sabhi elements ka data type same hona.


array4a = np.array([10, 20, 30, 40])
print(array4a) 
print(array4a.dtype)  # This will print the type of array


array5 = np.array([10, "Aman", 20])
print(array5)
print(array5.dtype)#heterogeneous data=different data types

print(type(array5[0]))
print(type(array5[1]))
print(type(array5[2]))#teeno elements ab string ban chuke hain

array6 = np.array([10, "Aman", 20.5], dtype=object)
print(array6)
print(array6.dtype)
print(type(array6[0]))
print(type(array6[1]))
print(type(array6[2]))




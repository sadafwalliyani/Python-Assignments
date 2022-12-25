import numpy as np
a= np.array([1,2,3])
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimention
a.ndim
print(a.ndim)
# Get Shape
print(b.shape)

# Get Size
print(a.dtype)

# Get Size
print(a.itemsize)

# Get total size
print(a.nbytes)

# Accessing/Changing specific elements, rows, columns, etc
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
c=[1,5]
print(c)
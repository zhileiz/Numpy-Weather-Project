import numpy as np

# Initializing an Array
a = np.array([1,2,3,4,5])
print a # >> [1 2 3 4 5]
print a.dtype # >> int64

b = np.array([1,2,3,4,5], dtype=np.int8)
print b.dtype # >> int8

print a[0] # >> 1

# Array Properties
print a.ndim # >> 1
print a.shape # >> (5,)
print a.size # >> 5

# 2-D Array
c = np.array([[1,2,3,4,5],[6,7,8,9,10]], dtype=np.float64)
print c
print c.ndim # >> 2
print c.shape # >> (2, 5)
print c.size # >> 2
print c[1,2]

# Zero Arrays
d = np.zeros((3,3),'d')
print d

# A range of Numbers
e = np.arange(0,25,5)
print e

# Array of random numbers
f = np.random.standard_normal((2,4))
print f

# Stacking Up Arrays
g = np.random.standard_normal((2,3))
h = np.random.standard_normal((2,3))
print np.vstack([g,h])
print np.hstack([g,h])

# Transforming Arrays
g.transpose()
print g

# Slicing
i = np.array([[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35]])
print i[1:3]
print i[1:3,1]
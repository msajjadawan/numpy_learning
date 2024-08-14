'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,0])
print(arr)
print(arr.dtype)
print(id(arr))
print(arr.size)
for i in range(arr.size):
    print(id(arr[i]))

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

## Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype=np.uint)
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype=np.float64)
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype='i2')
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype='f')
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

### What if a Value Can Not Be Converted

#arr = np.array([1, 'banana', 3, 4, 5, 6, 7, 8, 9, 0], dtype='i2')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype='f')
print(arr)


arr = np.array([1.1, 2.1, 3.1,5])
print(arr.dtype)
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

copy_array = arr.copy()
print(id(arr))
print(id(copy_array))
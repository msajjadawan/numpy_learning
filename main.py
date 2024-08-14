import numpy as np

array = np.array([1,2,3,4,5])
print(type(array))
print(array)
print(np.__version__)

### 0-D Arrays
arr = np.array(42)
print(arr)

#### 1-D arrays
arr = np.array([1, 2, 3])
print(arr)


#### 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


#### 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

### Check Number of Dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#### Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

### Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0])

print("NumPy Array Slicing".lower() + "\n")


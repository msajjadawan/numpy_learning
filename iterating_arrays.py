import numpy as np

arr = np.array([1, 2, 3, 4, 5])
for i in arr:
    print(i)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for i in arr2d:
    print(i)
    for x in i:
        print(x)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr3d:
  for y in x:
    for z in y:
      print(z)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
print("===========nditer with flags============")
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

  #### Iterating With Different Step Size

arr = np.array([[1, 2, 3, 4,41], [5, 6, 7, 8,9]])

for x in np.nditer(arr[:, ::2]):
  print(x)


arr = np.array([1, 2, 3])
print(arr[::-1])
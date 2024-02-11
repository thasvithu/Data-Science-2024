import numpy as np

arr = np.array([2, 5, 3, 5, 4, 6])
print(arr)
print(type(arr))
print(arr.dtype)
print(arr.shape)

arr2 = arr.reshape(2, 3)
print(arr2)
print(type(arr2))
print(arr.shape)
import numpy as np

print("Today We will Learn NumPy")

#Create 1DArray using numpy
numList = [3, 2, 4, 6, 5]
arr = np.array(numList)

print("Type of arr : ", type(arr))

for x in arr:
    print(x)
print("-----------------")

my_list = [1, 2.5, 'hello', True]
print(type(my_list))

arr2 = np.array(my_list)
print(arr2[0])
print(type(arr2))

print(arr2.dtype)

print(arr2[0] + arr2[2])
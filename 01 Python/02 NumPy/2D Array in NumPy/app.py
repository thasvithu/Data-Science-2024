<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:37:14 2024

@author: Vimalathas Vithusan
"""


import numpy as np

#0D Arrays
zero_array = np.array(10)
print(zero_array)
print(type(zero_array))
print(zero_array.shape)
print(zero_array.dtype)

#Accesing Elements 
test = zero_array[()]
print("Value of test is : ", test)

print("\n-----------------------\n")


#1D Arrays
oned_array = np.array([1, 2, 3, 4, 5])
print(oned_array)
print(type(oned_array))
print(oned_array.shape)
print(oned_array.dtype)

#Accesing Elements
test1 = oned_array[4]
print("Value of test1 is : ", test1)

test1 = oned_array[[4]]
print("Value of test1 is : ", test1)

print("Access through loop")
rows, = oned_array.shape
for i in range(int(rows)):
    print(oned_array[i])

oned_tuple_arr = np.array((2, 4, 6, 8, 10))
print(oned_tuple_arr)
print(type(oned_tuple_arr))
print(oned_tuple_arr.dtype)

print("\n-----------------------\n")

#2D Arrays
twod_arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(twod_arr)
print(type(twod_arr))

#Accesing Elements
test3 = twod_arr[[]]
print("Value of test3 is : ", test3)

test4 = twod_arr[[0]]
print("Value of test4 is : ", test4)

test4 = twod_arr[0]
print("Value of test4 is : ", test4)

test5 = twod_arr[[1]]
print("Value of test5 is : ", test5)

test6 = twod_arr[0, 0]
print("Value of test6 is : ", test6)

test7 = twod_arr[1, 1]
print("Value of test7 is : ", test7)


print("Access through loop")
rows, cols = twod_arr.shape

for i in range(rows):
    for j in range(cols):
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:37:14 2024

@author: Vimalathas Vithusan
"""


import numpy as np

#0D Arrays
zero_array = np.array(10)
print(zero_array)
print(type(zero_array))
print(zero_array.shape)
print(zero_array.dtype)

#Accesing Elements 
test = zero_array[()]
print("Value of test is : ", test)

print("\n-----------------------\n")


#1D Arrays
oned_array = np.array([1, 2, 3, 4, 5])
print(oned_array)
print(type(oned_array))
print(oned_array.shape)
print(oned_array.dtype)

#Accesing Elements
test1 = oned_array[4]
print("Value of test1 is : ", test1)

test1 = oned_array[[4]]
print("Value of test1 is : ", test1)

print("Access through loop")
rows, = oned_array.shape
for i in range(int(rows)):
    print(oned_array[i])

oned_tuple_arr = np.array((2, 4, 6, 8, 10))
print(oned_tuple_arr)
print(type(oned_tuple_arr))
print(oned_tuple_arr.dtype)

print("\n-----------------------\n")

#2D Arrays
twod_arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(twod_arr)
print(type(twod_arr))

#Accesing Elements
test3 = twod_arr[[]]
print("Value of test3 is : ", test3)

test4 = twod_arr[[0]]
print("Value of test4 is : ", test4)

test4 = twod_arr[0]
print("Value of test4 is : ", test4)

test5 = twod_arr[[1]]
print("Value of test5 is : ", test5)

test6 = twod_arr[0, 0]
print("Value of test6 is : ", test6)

test7 = twod_arr[1, 1]
print("Value of test7 is : ", test7)


print("Access through loop")
rows, cols = twod_arr.shape

for i in range(rows):
    for j in range(cols):
>>>>>>> ee0d962 (2024)
        print(twod_arr[i, j])
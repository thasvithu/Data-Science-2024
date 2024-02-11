# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:58:08 2024

@author: Vimalathas Vithusan
"""

#List is a built in data type in python
#Using list can store collection of items in diffrent data types
#List item are ordered and mutable(modifiable)
#List index start from 0
#Negative index also allowed in List -1 refer to tha last element
#Lists allows duplicates


"""
            *** Python - Creating List ***
"""
print("\n----- Python - Creating List -----\n")
my_List = [1, "vithu", 23, False, "uov", 'M', 156.25, True]

#Print List
print(my_List) 

#Check the object type of list
print("object type of list : ", type(my_List))

#Access List Elements
print("0 index element is : ", my_List[0])
print("-1 index element is : ", my_List[-1])
print("Data Type of 0 index element : ", type(my_List[0]))
print("Data Type of 1 index element : ", type(my_List[1]))
print("Data Type of -1 index element : ", type(my_List[-1]))
print("Data Type of -2 index element : ", type(my_List[-2]))

print("Just check will it work or not : ", my_List[0] + my_List[-1])


#Find List Length
length_list = len(my_List)
print("Total length of my_list is : ", length_list)


#Create list using List constructor
test = list((2, 4, 'M', 8, True, "Vithu"))
print("From list object : ", test)

#Lets check the type of List
print("List type : ", type(test))

#Check if item exists
if 4 in test:
    print("Check 4 exists in test : ", True)
else:
    print("Check 4 exists in test : ", False)
    
    
    
"""
            *** Python - Change List Items ***
"""
print("\n----- Python - Change List Items -----\n")

test_list = [2, False, "vithu", 4.0]
print("Before change : ", test_list)

test_list[1] = True
test_list[2] = "Nila"
print("1 After change : ", test_list)

test_list[0:2] = 5, True
print("2 After change : ", test_list)


test_list[0:2] = [5, True]
print("3 After change : ", test_list)
print("Line 74 Output : ", len(test_list))

test_list[0:2] = [5]
print("3 After change : ", test_list)
print("Line 78 Output : ", len(test_list))

#Using insert method also can insert a value in a list
test_list.insert(1, True)
print("Line 81 Output : ", test_list)



"""
            *** Python - Add List Items ***
"""
print("\n-----Python - Add List Items -----\n")
test_list2 = [2, 4, 6, 8]
print("Before Adding : ", test_list2)

#Adding element at the end of a list
test_list2.append(100)
print("After Adding : ", test_list2)

#Extend List
ex_list = ["Hello", "Iam", "Extend", "List"]

test_list2.extend(ex_list)
print("After Extend : ", test_list2)


ex_list1 = {}

test_list2.extend(ex_list)
print("After Extend : ", test_list2)












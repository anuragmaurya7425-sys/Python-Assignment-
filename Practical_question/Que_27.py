#  Write a program using numpy to perform array operations(creation, indexing, arithmetic).

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(f"first array element is :{arr1}")
print(f"Second array element is :{arr2}")

# Indexing
print("\n Indexing ")
print(f"First element of array :{arr1[0]}")
print(f"Last element of array :{arr1[-1]}")
print(f"Index from 1 to 3 :{arr1[1,4]}")

# Addition
print("Arithmetic operation ")
print(f"Addition is :{arr1}+{arr2}")

#Substraction
print(f"Substraction is :{arr1}-{arr2}")

#multiplication 
print(f"multiplication is :{arr1}*{arr2}")

#Dvision 
print(f"Dvision is :{arr1}/{arr2}")
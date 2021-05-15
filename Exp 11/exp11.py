#Om Ghanshyam Bhamare SE A 3
#Exp 11
import numpy as np
from numpy import *
print("3D Array...")
arr1=array([[2,4,6],[3,6,8],[5,10,15]])
print(arr1)
print("*********************************")
print("1]Diemesnsion Of Array")
print(arr1.shape)
print("*********************************")
print("2]Data Type")
print(arr1.dtype)
print("*********************************")
print("3]Size")
print(arr1.size)
print("*********************************")
print("4]Size of Memory")
print(arr1.nbytes)
print("*********************************")
print("5]Convert the n-D to 1-D")
arr2=arr1.flatten()
print(arr2)
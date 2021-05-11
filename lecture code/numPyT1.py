import numpy as np
from numpy import *
#numpy allow 1D 2D array
#numpy is rich library

#5 way to create array 
#1] array() , 2]linspace(start,end,steps), 3]LogSpace(start,end,steps)
#5]arange()

arr1=array([10,20,30,40.5])#array single data type
print(arr1)
#Create Single diemension array using numpy
arr2=np.array([10,20,30,40])
print(arr2)

#linspace
print("Linespace...")
arr3=np.linspace(0,10,5)
print(arr3)

#logspace
print("Logspace...")
arr4=np.logspace(1,4,5)
print(arr4)

#arrange
print("Arrange...")
arr5=np.arange(1,13,1)
print(arr5)


#Create matrix

print("Null matrix")
arr6= zeros(5,int)#int,float,double
print(arr6)

print("Unity matrix")
arr7= ones(5,int)#int,float,double
print(arr7)

#reshape converting into matrix
print("Reshape")
arr8=np.arange(9).reshape(3,3)#reshape(column,rows)
print(arr8)

#
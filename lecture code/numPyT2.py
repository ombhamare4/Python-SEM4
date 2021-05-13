#12 may 2021
import numpy as np
from numpy import *

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.arange(4).reshape(2,2)
print(a)
print(bartlett)


#indexing 
#in 1D it will easy
#for 2D array_name[row,column]
print("2D index")
print(a[0,0])
#for 3D array_name[row,col]
print("3D index")
print(a[2,2])

#Slicing
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print("Slcing")
#a[roe,from where: to next index]
print(b[1,1:4])

#
print(b[0:4,1:4])

c=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Dimension of Matrix")
print(c.shape)

#join array

d=np.arange(4).reshape(2,2)
e=np.arange(4).reshape(2,2)
print("Join array")
#concatenate((array1,array2),axis)
f = np.concatenate((d,e),axis=1)
print(f)

#split
g=array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print("Split")
print(g)
#split(array_name,no.part)
h=np.array_split(g,7)
print(h)

#Sort
i=array([[2,1],[4,3],[5,6],[7,8],[10,9],[11,12]])
j=np.sort(i)
print(j)

#ndim helps you to fide rank of matrix
k=array([[2,1,2],[4,3,1],[5,6,8]])
print("Rank of matrix")
print(k.ndim)

#datatype find
print("Data type")
print(k.dtype)

#size
print("size")
print(k.size)

#item size 1 element how many space occupie
print("Item size")
print(a.itemsize)

#nbytes all element how many space occupie
print("All item occupie")
print(k.nbytes)

#single to multi diemnion
#flattern function multi to single 
l=k.flatten()
print("Flatten")
print(l)
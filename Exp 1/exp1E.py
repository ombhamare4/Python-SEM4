#Exp 1 (e): 
#Om Ghanshyam Bhamare Div A Roll No: 3
t1=(1,2,3)
print(t1)
#adding element
t1=t1+(9,)
print(t1)
#Tuple are imutable therefore updaing not possible
#but we concatinate
t2=(20,30,40,50)
tnew=t1+t2
print(tnew)
#removing indiual element not possible we delete whole tuple
l1=list(t1)
l1.remove(2)
t1=tuple(l1)
print(t1)
#Exp 1 (b): 
#Om Ghanshyam Bhamare Div A Roll No: 3
a=[1,2,3,4,5,6,7,8,9]
e=[]
o=[]
for x in range(len(a)):
    if x%2==0:
        e.append(x)
    elif x%2!=0:
        o.append(x)

print(e)
print(o)
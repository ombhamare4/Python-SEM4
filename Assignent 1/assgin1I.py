#Assign 1 (9): 
# A Python program to display and 
# sum of a list of number using while loop
#Om Ghanshyam Bhamare Div A Roll No: 3

#Create empty list
lst=[]
#take size of list
size = int(input("Enter Size of List: "))
while(size!=0):
    a = int(input("Enter Elements in list: "))
    lst.append(a)
    size-=1
#print list
print("Given List are: "+str(lst))
#str for int concatination with string
listSum=0
lenList=len(lst)
x=0
while x<lenList:
    listSum+=lst[x]
    x+=1
print("Sum of elements in list is: "+str(listSum))

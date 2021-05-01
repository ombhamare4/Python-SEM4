#Assign 1 (5):
#A Python program to accept a list and display it.
#A Python program to accept a tuple and display it.
#Om Ghanshyam Bhamare Div A Roll No: 3
lst=[]
for x in range(0,5):
    a = int(input("Enter Elemets in list: "))
    lst.append(a)
print(lst)


#tuple
t1=()
for y in range(5):
    b = input("Enter Elements in tuple: ")
    t1=t1+(b,)
print(t1)
#Assign 1 (14): 
#A Python program to design a basic calculator 
# using variable length function.

#Om Ghanshyam Bhamare Div A Roll No: 3
def length():
  s = int(input(("Select \n 1==add\n 2==sub\n 3==multiply\n 4==division\n 5==Modulus\n 6==exit\n ")))
  n1 = int(input("enter n1: "))
  n2 = int(input("enter n2: "))
  if s==1:
    print("addition: ",n1+n2)
  elif s==2:
    print("subtraction: ",n1-n2)
  elif s==3:
    print("multilication: ",n1*n2)
  elif s==4:
    if n2==0:
      print("invalid")
    else:
      print("division: ",n1/n2)  
  elif s==5:    
    print("modulus: ",n1%n2)

length()
# print(length())
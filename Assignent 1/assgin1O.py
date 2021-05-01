#Assign 1 (15): 
#A Python program to find the biggest 
# number in two given numbers using lambda.

#Om Ghanshyam Bhamare Div A Roll No: 3

x = lambda a,b: True if(a>b) else False
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
y = x(num1,num2)

if y is True:
    print("Number1 is greater than Number2")
else:
    print("Number2 is Greater than Number1")



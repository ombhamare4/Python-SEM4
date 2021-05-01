#Assign 1 (12): 
#A Python program to check 
# if a given number is prime or 
# not using functions

#Om Ghanshyam Bhamare Div A Roll No: 3

def check(num,flag):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                flag=True
                break
    if flag:
        print(str(num)+" is not a prime number")
    else:
        print(str(num)+" is a prime number")


flag=False
num = int(input("Enter Number to check: "))
check(num,flag)#Calling function